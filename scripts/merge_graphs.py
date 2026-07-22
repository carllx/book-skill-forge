import json
import glob
import os

input_dir = r"e:\Download\book-skill-test-bench\data\books\language_new_media_chunks"
output_dir = r"e:\Download\book-skill-test-bench\data\evaluation_out\language-of-new-media_graphify_only"
output_file = os.path.join(output_dir, "graph.json")

os.makedirs(output_dir, exist_ok=True)

merged_nodes = {}
merged_edges = set()

# Process each file
for file_path in glob.glob(os.path.join(input_dir, "graph_*.json")):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            
            local_id_to_label = {}
            
            # Merge nodes
            for node in data.get("nodes", []):
                original_id = node.get("id")
                label = node.get("label", "").strip()
                
                if not original_id or not label:
                    continue
                    
                local_id_to_label[original_id] = label
                
                if label not in merged_nodes:
                    # Create a new node using label as id to ensure global uniqueness
                    merged_nodes[label] = {
                        "id": label,
                        "label": label,
                        "description": node.get("description", "")
                    }
                else:
                    # Optionally combine descriptions if different, but here we just keep the first one
                    # or append to it if it's vastly different. For simplicity, keep first.
                    pass
            
            # Merge edges
            for edge in data.get("edges", []):
                source_id = edge.get("source")
                target_id = edge.get("target")
                edge_label = edge.get("label", "").strip()
                
                source_label = local_id_to_label.get(source_id)
                target_label = local_id_to_label.get(target_id)
                
                if source_label and target_label:
                    edge_key = (source_label, target_label, edge_label)
                    merged_edges.add(edge_key)
                    
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

final_edges = []
for edge in merged_edges:
    final_edges.append({
        "source": edge[0],
        "target": edge[1],
        "label": edge[2]
    })

final_data = {
    "nodes": list(merged_nodes.values()),
    "edges": final_edges
}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(final_data, f, ensure_ascii=False, indent=2)

print(f"Successfully merged graphs.")
print(f"Total nodes: {len(final_data['nodes'])}")
print(f"Total edges: {len(final_data['edges'])}")
print(f"Output saved to: {output_file}")
