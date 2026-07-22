#!/usr/bin/env python3
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
