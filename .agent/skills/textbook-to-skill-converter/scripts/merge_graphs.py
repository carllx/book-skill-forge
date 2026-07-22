#!/usr/bin/env python3
import sys
import json
from pathlib import Path

def print_usage():
    print("Usage: python merge_graphs.py <input_dir> <output_graph.json>")
    sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print_usage()
        
    input_dir = Path(sys.argv[1])
    output_file = Path(sys.argv[2])
    
    if not input_dir.exists() or not input_dir.is_dir():
        print(f"Error: {input_dir} is not a valid directory.")
        sys.exit(1)
        
    merged_nodes = {}
    merged_edges = []
    
    # Recursively find all json files
    json_files = list(input_dir.rglob("*.json"))
    if not json_files:
        print(f"No JSON files found in {input_dir}.")
        sys.exit(1)
        
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            nodes = data.get('nodes', [])
            edges = data.get('edges', data.get('links', []))
            
            for node in nodes:
                nid = node.get('id')
                if nid is not None:
                    # Deduplicate by ID
                    if nid not in merged_nodes:
                        merged_nodes[nid] = node
                    else:
                        # Merge fields: prefer non-empty values
                        for k, v in node.items():
                            if not merged_nodes[nid].get(k) and v:
                                merged_nodes[nid][k] = v
                                
            merged_edges.extend(edges)
            print(f"Loaded {len(nodes)} nodes and {len(edges)} edges from {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            
    # Deduplicate edges (by source-target-relation)
    unique_edges = []
    edge_signatures = set()
    for edge in merged_edges:
        s = edge.get('source')
        t = edge.get('target')
        r = edge.get('relation', edge.get('type', ''))
        sig = f"{s}-{r}-{t}"
        if sig not in edge_signatures:
            edge_signatures.add(sig)
            unique_edges.append(edge)
            
    final_graph = {
        "nodes": list(merged_nodes.values()),
        "edges": unique_edges
    }
    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_graph, f, ensure_ascii=False, indent=2)
        
    print(f"[*] Merged graph saved to {output_file}")
    print(f"[*] Total unique nodes: {len(merged_nodes)}")
    print(f"[*] Total unique edges: {len(unique_edges)}")

if __name__ == "__main__":
    main()
