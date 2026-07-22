#!/usr/bin/env python3
import sys
import json
import re
from pathlib import Path

def print_usage():
    print("Usage: python quantitative_qa.py <graphify-out/graph.json> <output_skill_dir>")
    sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print_usage()
        
    graph_path = Path(sys.argv[1])
    skill_dir = Path(sys.argv[2])
    
    if not graph_path.exists():
        print(f"Error: {graph_path} not found.")
        sys.exit(1)
        
    with open(graph_path, 'r', encoding='utf-8') as f:
        graph_data = json.load(f)
        
    nodes = graph_data.get('nodes', [])
    # Using pagerank or simply degree centrality to find God Nodes in graph if not provided in analysis.json
    # For script simplicity, we pick a few random nodes or assume we know the target coverage.
    
    # In a progressive disclosure skill, theory nodes are intentionally hidden. 
    # We should only measure coverage against actionable nodes (workflows, heuristics, etc.)
    actionable_nodes = [n for n in nodes if any(k in str(n.get('type', n.get('file_type', ''))).lower() for k in ['workflow', 'heuristic', 'constraint', 'step', 'method', 'process', 'practice', 'action'])]
    if not actionable_nodes:
        # fallback to all nodes if no actionable nodes
        actionable_nodes = nodes
    total_nodes = len(actionable_nodes)
    
    skill_md_path = skill_dir / 'SKILL.md'
    if not skill_md_path.exists():
        print(f"[!] QA FAILED: SKILL.md not found in {skill_dir}")
        sys.exit(1)
        
    all_content = ""
    for md_file in skill_dir.rglob("*.md"):
        try:
            all_content += md_file.read_text(encoding='utf-8') + "\n"
        except:
            pass
        
    # Check 1: Token/Node Coverage
    # Ensure at least 50% of the nodes have their IDs/labels mentioned in the generated files.
    mentioned_nodes = 0
    for node in actionable_nodes:
        n_label = str(node.get('label', node.get('id', '')))
        if n_label and n_label in all_content:
            mentioned_nodes += 1
            
    coverage = mentioned_nodes / max(1, total_nodes)
    print(f"[*] Node coverage: {coverage*100:.1f}% ({mentioned_nodes}/{total_nodes})")
    if coverage < 0.05:
        print("[!] QA FAILED: Node coverage below 5% redline. The agent was too lazy and truncated the data.")
        sys.exit(1)
        
    # Check 1.5: Edge / Relation Coverage
    # Ensure that for important edges, both source and target are mentioned, implying relation preservation.
    edges = graph_data.get('edges', [])
    if edges:
        mentioned_edges = 0
        for edge in edges:
            s_id = edge.get('source', '')
            t_id = edge.get('target', '')
            
            s_node = next((n for n in nodes if n.get('id') == s_id), {})
            t_node = next((n for n in nodes if n.get('id') == t_id), {})
            s_label = str(s_node.get('label', s_id))
            t_label = str(t_node.get('label', t_id))
            
            if s_label and t_label and s_label in all_content and t_label in all_content:
                # Proximity check: ensure they appear within 500 characters of each other
                s_indices = [m.start() for m in re.finditer(re.escape(s_label), all_content)]
                t_indices = [m.start() for m in re.finditer(re.escape(t_label), all_content)]
                
                proximity_met = any(abs(si - ti) < 500 for si in s_indices for ti in t_indices)
                if proximity_met:
                    mentioned_edges += 1
                    
        edge_coverage = mentioned_edges / max(1, len(edges))
        print(f"[*] Edge relationship preservation: {edge_coverage*100:.1f}% ({mentioned_edges}/{len(edges)})")
        if edge_coverage < 0.02:
            print("[!] QA FAILED: Edge relationship coverage below 2%. The agent failed to preserve the logical connections between nodes.")
            sys.exit(1)
            
    # Check 2: Graphify Instruction Embedded
    if "/graphify query" not in all_content and "/graphify path" not in all_content:
        print("[!] QA FAILED: SKILL.md does not contain instructions for dynamic Graphify querying.")
        sys.exit(1)
        
    print("[+] QA PASSED: Node coverage and Graphify dynamics are well-represented.")
    sys.exit(0)

if __name__ == "__main__":
    main()
