#!/usr/bin/env python3
import sys
import json
import time
from pathlib import Path
import re
import urllib.error
import shutil

def get_community_prompt_and_context(community_id: str, nodes: list, chunk_dir: Path, critique: str = None) -> tuple:
    """Prepares the prompt and context for the Agent to synthesize an actionable workflow."""
    prompt = """
    Role: Senior System Architect, Subject Matter Expert & Agent Skill Designer
    Task: Transform the provided textbook narrative (concept cluster) into a comprehensive, highly actionable Markdown workflow.
    Constraints:
    1. PRESERVE THE DEPTH AND NUANCE of the original textbook. Do NOT over-compress or strip away important technical details.
    2. PROGRESSIVE DISCLOSURE: Preserve the depth conceptually, but DO NOT embed massive blocks of raw textbook theory. Instead, use "Show, Don't Tell" and provide concrete Blockquote examples, deferring to the `graphify_query` MCP tool for bulk theory.
    3. Frame the deep knowledge as actionable heuristics and guidelines.
    4. IMAGE PATH REWRITING: If you include or reference any images from the original context (e.g., `images/img.png`), you MUST rewrite their paths to be relative to the workflows directory, i.e., `../../images/img.png`. Failure to do this will result in broken images.
    5. MUST output these sections: 
       - Prerequisites & Context (Explain the WHY and WHEN, reference graphify_query MCP tool for deep dives)
       - Comprehensive Guide & Best Practices (Detailed steps and deep textbook insights)
       - If/Then Troubleshooting Logic (Address edge cases and theoretical constraints)
       - Verification Checklists
    6. The output should be extensive and serve as a robust actionable reference, while strictly deferring to the `graphify_query` MCP tool for bulk theory.
    """
    if critique:
        prompt += f"\n    [CRITICAL QA FEEDBACK TO FIX]:\n    {critique}\n    Please strictly address the above critique in your new generation."
    
    
    # Collect all text
    context_parts = []
    for n in nodes:
        label = n.get('label', '')
        desc = n.get('description', '')
        content = n.get('content', '')
        source_file = n.get('source_file')
        
        if not content and source_file and chunk_dir and chunk_dir.exists():
            chunk_path = chunk_dir / source_file.lstrip('/')
            if not chunk_path.resolve().is_relative_to(chunk_dir.resolve()): continue
            if chunk_path.exists():
                content = chunk_path.read_text(encoding='utf-8')
                
        context_parts.append(f"Node: {label}\n{desc}\n{content}")
        
    context_text = "\n---\n".join(context_parts)
    context_text = context_text[:50000] 
    
    return prompt, context_text

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Triage router for progressive disclosure skill generation.")
    parser.add_argument("graph_path", type=str)
    parser.add_argument("output_dir", type=str)
    parser.add_argument("chunk_dir", type=str, nargs="?", default=None)
    parser.add_argument("--target-community", type=str, default=None, help="Only process this community ID for retries")
    parser.add_argument("--critique-file", type=str, default=None, help="File containing QA critique for retrying")
    args = parser.parse_args()
    
    graph_path = Path(args.graph_path)
    output_dir = Path(args.output_dir)
    chunk_dir = Path(args.chunk_dir) if args.chunk_dir else None
    
    critique = None
    if args.critique_file and Path(args.critique_file).exists():
        critique = Path(args.critique_file).read_text(encoding='utf-8')
    
    if not graph_path.exists():
        print(f"Error: {graph_path} not found.")
        sys.exit(1)
        
    output_dir.mkdir(parents=True, exist_ok=True)
    refs_dir = output_dir / 'references'
    workflows_dir = refs_dir / 'workflows'
    
    workflows_dir.mkdir(parents=True, exist_ok=True)
    
    # Ensure graphify-out exists and graph.json is copied over
    graphify_out_dir = output_dir / 'graphify-out'
    graphify_out_dir.mkdir(parents=True, exist_ok=True)
    target_graph_path = graphify_out_dir / 'graph.json'
    if graph_path.resolve() != target_graph_path.resolve():
        shutil.copy2(graph_path, target_graph_path)
    
    with open(graph_path, 'r', encoding='utf-8') as f:
        graph_data = json.load(f)
        
    nodes = graph_data.get('nodes', [])
    edges = graph_data.get('edges', graph_data.get('links', []))
    
    # Identify actionable nodes using out-degrees and relations
    actionable_node_ids = set()
    total_degrees = {}
    for edge in edges:
        s = edge.get('source')
        t = edge.get('target')
        if s is not None:
            total_degrees[s] = total_degrees.get(s, 0) + 1
        if t is not None:
            total_degrees[t] = total_degrees.get(t, 0) + 1
            
        rel = str(edge.get('relation') or '').lower()
        if any(keyword in rel for keyword in ['precede', 'require', 'resolve', 'depend', 'cause', 'lead', 'use', 'rationale_for']):
            if s is not None: actionable_node_ids.add(s)
            if t is not None: actionable_node_ids.add(t)
            
    for node in nodes:
        nid = node.get('id')
        if nid is None: continue
        ntype = str(node.get('type', node.get('file_type', ''))).lower()
        if any(keyword in ntype for keyword in ['workflow', 'heuristic', 'constraint', 'step', 'method', 'process', 'practice', 'action', 'rationale']):
            actionable_node_ids.add(nid)
        elif total_degrees.get(nid, 0) >= 2:
            actionable_node_ids.add(nid)
    
    # 1. Group nodes by Community
    communities = {}
    theory_nodes = []
    
    for node in nodes:
        nid = node.get('id')
        # Default community to 0 if not present
        comm_id = str(node.get('community', node.get('community_id', 'theory')))
        
        # Determine if it's actionable based on our set
        if nid in actionable_node_ids:
            if comm_id not in communities:
                communities[comm_id] = []
            communities[comm_id].append(node)
        else:
            theory_nodes.append(node)
            
    print(f"[*] Found {len(communities)} actionable communities and {len(theory_nodes)} theory nodes.")
    
    # 2. Queue Synthesis Tasks for each Community
    workflow_files = []
    agent_tasks = []
    
    for comm_id, c_nodes in communities.items():
        if args.target_community and str(comm_id) != args.target_community:
            # Skip if we are targeting a specific community for retry
            # Still record it so it appears in SKILL.md if it already exists
            top_node = c_nodes[0].get('label', f'community_{comm_id}')
            safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', top_node.lower())[:30]
            filename = f"{safe_name}_c{comm_id}.md"
            out_file = workflows_dir / filename
            if out_file.exists():
                workflow_files.append({
                    "name": top_node,
                    "file": f"references/workflows/{filename}"
                })
            continue

        # Heuristic name for the community
        top_node = c_nodes[0].get('label', f'community_{comm_id}')
        safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', top_node.lower())[:30]
        
        filename = f"{safe_name}_c{comm_id}.md"
        out_file = workflows_dir / filename
        
        print(f"[*] Queueing workflow task for community: {safe_name} ({len(c_nodes)} nodes)")
        prompt, context_text = get_community_prompt_and_context(comm_id, c_nodes, chunk_dir, critique)
        
        # Add title and placeholder
        final_md = f"# Workflow: {top_node}\n\n> **[Agent Action Required]** This workflow is awaiting synthesis by the Antigravity Agent.\n\n<!-- ANTIGRAVITY_CONTEXT\n{context_text[:500]}... [Context truncated in placeholder, check task queue]\n-->"
        out_file.write_text(final_md, encoding='utf-8')
        
        agent_tasks.append({
            "community_id": comm_id,
            "top_node": top_node,
            "output_file": str(out_file),
            "prompt": prompt,
            "context": context_text
        })
        
        workflow_files.append({
            "name": top_node,
            "file": f"references/workflows/{filename}"
        })
        
    tasks_dir = output_dir / '.agent_tasks'
    tasks_dir.mkdir(parents=True, exist_ok=True)
    tasks_file = tasks_dir / 'synthesis_tasks.json'
    with open(tasks_file, 'w', encoding='utf-8') as f:
        json.dump(agent_tasks, f, indent=2, ensure_ascii=False)
        
    # 3. Generate fallback lookup script
    fallback_script = output_dir / 'scripts' / 'query_graph_fallback.py'
    fallback_script.parent.mkdir(parents=True, exist_ok=True)
    fallback_code = """#!/usr/bin/env python3
import sys, json
from pathlib import Path

def search_graph(graph_file, query):
    graph_path = Path(graph_file)
    if not graph_path.exists():
        print(f"Error: {graph_path} not found.")
        sys.exit(1)
        
    with open(graph_path, 'r', encoding='utf-8') as f:
        graph = json.load(f)
        
    query_lower = query.lower()
    print(f"--- Search Results for '{query}' ---")
    
    nodes = graph.get('nodes', [])
    for n in nodes:
        label = str(n.get('label', '')).lower()
        desc = str(n.get('description', '')).lower()
        content = str(n.get('content', '')).lower()
        if query_lower in label or query_lower in desc or query_lower in content:
            print(f"Node: {n.get('label')} - {n.get('description')}")
            
    edges = graph.get('edges', graph.get('links', []))
    for e in edges:
        source = str(e.get('source', '')).lower()
        target = str(e.get('target', '')).lower()
        relation = str(e.get('relation', '')).lower()
        desc = str(e.get('description', '')).lower()
        if query_lower in source or query_lower in target or query_lower in relation or query_lower in desc:
            print(f"Edge: {e.get('source')} -[{e.get('relation')}]-> {e.get('target')} : {e.get('description')}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: query_graph_fallback.py <graph_file> <query>")
        sys.exit(1)
    search_graph(sys.argv[1], sys.argv[2])
"""
    fallback_script.write_text(fallback_code, encoding='utf-8')
    fallback_script.chmod(0o755)


    # 4. Generate the routing SKILL.md
    skill_name = output_dir.name
    
    skill_md = f"""---
name: {skill_name}
description: Provide comprehensive workflows and heuristics derived from {skill_name}. Use when executing domain-specific tasks, evaluating patterns, or needing deep structural checklists.
---

# {skill_name} Workflows & Guides

This skill provides a structured, progressive disclosure architecture. 
Please route to the specific workflow below based on your current goal.

## Quick Start
如果你是第一次调用此技能，或者不知道该用哪个具体的工作流，请仔细梳理你的目标，然后查阅下面的核心工作流：

## Core Workflows (工作流体系)

"""
    if not workflow_files:
        skill_md += "- *(No actionable workflows detected in the knowledge graph)*\n"
    else:
        for wf in workflow_files:
            skill_md += f"- **{wf['name']}**\n  ➡️ [{wf['name']} Guide]({wf['file']})\n\n"
            
    skill_md += """
## 渐进式知识检索 (Progressive Knowledge Retrieval)

> [!WARNING]  
> 原书核心概念已编译为高密度的知识图谱。**切勿使用 `view_file` 或 `read_file` 等工具尝试读取原始的大型文本块**，否则会导致严重的上下文溢出（Context Bloat）与截断。本技能严格遵循渐进式披露（Progressive Disclosure）原则。

当你在工作流中遇到未知的专属术语，或需要深挖某个模式的理论依据时，请强制使用 `graphify-mcp` MCP server 提供的 `graphify_query` 工具。

1. **深度理论推演 (Deep Theory Query)** (首选)：
   当你需要理解 "Why" 或更深层次的理论推演时使用。请调用 `graphify_query` MCP 工具，并将 `query` 参数设置为你的问题（例如："为什么我们需要采用这种设计模式？"），`graph` 参数指向当前 skill 目录下的 `graphify-out/graph.json` 的绝对路径。该工具内置 Token 限制，避免上下文爆炸。

2. **Fallback (无 MCP 时)**：
   如果因为环境限制无法使用 MCP 工具，请运行生成的 `scripts/query_graph_fallback.py` 脚本来查询 `graphify-out/graph.json`：
   `python scripts/query_graph_fallback.py graphify-out/graph.json "<你的查询>"`

3. **用户引导**：当你需要用户确认深奥的设计概念时，请建议用户在交互中直接提问，由你代为通过 MCP 工具检索，或者建议用户输入 `/graphify query "<在此处替换你的概念>"`。
"""

    (output_dir / 'SKILL.md').write_text(skill_md, encoding='utf-8')
    print(f"[+] Successfully generated progressive disclosure skill skeleton at {output_dir}")
    print(f"[!] AGENT ACTION REQUIRED: {len(agent_tasks)} synthesis tasks queued to {tasks_file}")
    print(f"[!] Please instruct the Antigravity Agent to process these tasks and overwrite the workflow files.")

if __name__ == "__main__":
    main()
