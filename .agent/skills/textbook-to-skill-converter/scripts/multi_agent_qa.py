#!/usr/bin/env python3
import sys
import json
import os
import time
import random
import subprocess
from pathlib import Path

def print_usage():
    print("Usage: python multi_agent_qa.py <graphify-out/graph.json> <output_skill_dir> <chunk_dir>")
    sys.exit(1)

def get_random_slice(text: str, size: int = 1500) -> str:
    if len(text) <= size:
        return text
    start = random.randint(0, len(text) - size)
    return text[start:start+size]

def generate_graph_qa_tasks(graph_data, chunk_dir_path):
    print("\n[+] --- GRAPH QA TASK GENERATION ---")
    tasks = []
    nodes = graph_data.get('nodes', [])
    if not nodes:
        print("[-] Graph is completely empty.")
        return tasks

    # 1. Reverse Sampling (Node -> Chunk) to check Hallucinations
    nodes_with_source = [n for n in nodes if n.get('source_file')]
    if nodes_with_source:
        sample_nodes = random.sample(nodes_with_source, min(3, len(nodes_with_source)))
        for node in sample_nodes:
            source_file = node.get('source_file')
            chunk_file = chunk_dir_path / source_file
            if chunk_file.exists():
                full_text = chunk_file.read_text(encoding='utf-8')
                chunk_text = get_random_slice(full_text, 1500)
                node_text = f"Label: {node.get('label')}\nDesc: {node.get('description')}"
                tasks.append({
                    "qa_type": "hallucination_check",
                    "node_id": node.get('id'),
                    "prompt": "Role: QA Agent. Task: Determine if the 'Node Info' is purely hallucinated or accurately derived from the 'Source Text'. Return exactly 'PASS' if accurate, or 'FAIL: <reason>' if hallucinated.",
                    "context": f"Source Text:\n{chunk_text}\n\nNode Info:\n{node_text}"
                })

    # 2. Forward Sampling (Chunk -> Graph) to check Knowledge Completeness
    chunks = list(chunk_dir_path.glob("*.md")) + list(chunk_dir_path.glob("*.txt"))
    if chunks:
        sample_chunks = random.sample(chunks, min(3, len(chunks)))
        node_labels = ", ".join([n.get('label', '') for n in nodes][:200]) # top 200
        
        for chunk in sample_chunks:
            full_text = chunk.read_text(encoding='utf-8')
            chunk_text = get_random_slice(full_text, 1500)
            tasks.append({
                "qa_type": "omission_check",
                "chunk_name": chunk.name,
                "prompt": "Role: QA Agent. Task: Determine if the core concepts from the 'Source Text' are represented in the 'Graph Node Labels'. Return exactly 'PASS' if the main knowledge is captured, or 'FAIL: <reason>' if critical concepts are missing.",
                "context": f"Source Text:\n{chunk_text}\n\nGraph Node Labels:\n{node_labels}"
            })

    return tasks

def generate_script_qa_tasks(skill_dir_path):
    print("\n[+] --- SCRIPT QA TASK GENERATION ---")
    tasks = []
    
    skill_md = skill_dir_path / "SKILL.md"
    if not skill_md.exists():
        print("[-] SKILL.md is missing. Skipping script QA.")
        return tasks

    workflows_dir = skill_dir_path / "references" / "workflows"
    if not workflows_dir.exists():
        print("[-] No workflows found to review. Skipping script QA.")
        return tasks

    workflows = list(workflows_dir.glob("*.md"))
    for wf in workflows:
        wf_content = wf.read_text(encoding='utf-8')[:4000000]
        prompt = """Role: Strict QA Agent checking "Progressive Disclosure".
Task: Evaluate the provided workflow document. It MUST be an actionable guide with heuristics and steps. 
It MUST NOT be a dump of heavy, dry, academic theory. Background theory should be delegated to graphify searches.
If it contains excessive theory or lacks actionability, return exactly 'FAIL: <critique explaining what is too theoretical and needs to be hidden>'.
If it's actionable and good, return exactly 'PASS'."""
        
        comm_id = wf.stem.replace("community_", "")
        tasks.append({
            "qa_type": "progressive_disclosure_check",
            "workflow_file": wf.name,
            "community_id": comm_id,
            "prompt": prompt,
            "context": wf_content
        })

    return tasks

def main():
    if len(sys.argv) != 4:
        print_usage()

    graph_path = Path(sys.argv[1])
    skill_dir = Path(sys.argv[2])
    chunk_dir = Path(sys.argv[3])

    if not graph_path.exists() or not chunk_dir.exists():
        print("Error: Invalid paths provided.")
        sys.exit(1)

    with open(graph_path, 'r', encoding='utf-8') as f:
        graph_data = json.load(f)

    print("\n================ QUEUEING QA TASKS FOR ANTIGRAVITY AGENT ================")
    
    all_qa_tasks = []
    
    # 1. Graph QA Tasks
    graph_tasks = generate_graph_qa_tasks(graph_data, chunk_dir)
    all_qa_tasks.extend(graph_tasks)
    
    # 2. Script QA Tasks
    script_tasks = generate_script_qa_tasks(skill_dir)
    all_qa_tasks.extend(script_tasks)
    
    tasks_dir = skill_dir / '.agent_tasks'
    tasks_dir.mkdir(parents=True, exist_ok=True)
    tasks_file = tasks_dir / 'qa_tasks.json'
    
    with open(tasks_file, 'w', encoding='utf-8') as f:
        json.dump(all_qa_tasks, f, indent=2, ensure_ascii=False)
        
    print(f"\n[+] Successfully queued {len(all_qa_tasks)} QA tasks to {tasks_file}")
    print("[!] AGENT ACTION REQUIRED: Instruct Antigravity Agent to process these QA tasks and trigger any necessary retries.")
    sys.exit(0)

if __name__ == "__main__":
    main()
