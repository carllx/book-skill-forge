import os
import json
import argparse

def merge_paragraphs_to_blocks(middle_json_path, chunks_dir, output_json_path):
    print(f"Loading {middle_json_path}...")
    with open(middle_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    all_translated_paras = []
    
    chunk_files = [f for f in os.listdir(chunks_dir) if f.startswith("para_chunk_") and f.endswith(".txt") and not f.endswith("_zh.txt")]
    chunk_files.sort()
    
    for en_file in chunk_files:
        zh_file = en_file.replace(".txt", "_zh.txt")
        zh_path = os.path.join(chunks_dir, zh_file)
        en_path = os.path.join(chunks_dir, en_file)
        
        if os.path.exists(zh_path):
            with open(zh_path, 'r', encoding='utf-8') as f:
                lines = f.read().splitlines()
            all_translated_paras.extend(lines)
            print(f"Loaded translated chunk: {zh_file} ({len(lines)} paras)")
        else:
            with open(en_path, 'r', encoding='utf-8') as f:
                lines = f.read().splitlines()
            all_translated_paras.extend(lines)
            
    print(f"Total paragraphs loaded: {len(all_translated_paras)}")
    
    pdf_info = data.get("pdf_info", [])
    
    para_index = 0
    for page in pdf_info:
        for block in page.get("para_blocks", []):
            has_text = False
            lines = block.get("lines", [])
            for line in lines:
                for span in line.get("spans", []):
                    if span.get("content", "").strip():
                        has_text = True
                        break
                if has_text: break
                
            if has_text:
                if para_index < len(all_translated_paras):
                    translated_text = all_translated_paras[para_index]
                    
                    # BLOCK-LEVEL CONSOLIDATION
                    block["lines"] = []
                    block_bbox = block.get("bbox", [0, 0, 0, 0])
                    
                    unified_span = {
                        "bbox": block_bbox,
                        "content": translated_text,
                        "type": "text",
                        "score": 1.0
                    }
                    
                    unified_line = {
                        "bbox": block_bbox,
                        "spans": [unified_span],
                        "index": 0
                    }
                    
                    block["lines"].append(unified_line)
                    para_index += 1
                else:
                    print(f"Warning: Ran out of translated paragraphs at index {para_index}")
                            
    print(f"Consolidated {para_index} paragraphs into large block containers.")
    
    print(f"Saving merged JSON to {output_json_path}...")
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print("Block container merge complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge translated paragraphs into MinerU JSON using Block-Level Containers.")
    parser.add_argument("middle_json", help="Path to original MinerU _middle.json")
    parser.add_argument("chunks_dir", help="Directory containing translated TXT chunks")
    parser.add_argument("output_json", help="Path to save the merged _middle_zh.json")
    args = parser.parse_args()
    
    merge_paragraphs_to_blocks(args.middle_json, args.chunks_dir, args.output_json)
