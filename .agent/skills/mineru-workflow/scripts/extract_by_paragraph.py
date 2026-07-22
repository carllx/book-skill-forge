import os
import json
import math
import argparse

CHUNK_SIZE = 500  # 500 paragraphs per chunk

def extract_paragraphs(middle_json_path, output_dir):
    print(f"Loading {middle_json_path}...")
    with open(middle_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    pdf_info = data.get("pdf_info", [])
    extracted_paragraphs = []
    
    for page in pdf_info:
        for block in page.get("para_blocks", []):
            block_spans_text = []
            lines = block.get("lines", [])
            for line in lines:
                spans = line.get("spans", [])
                for span in spans:
                    text = span.get("content", "").strip()
                    if text:
                        block_spans_text.append(text)
            
            if block_spans_text:
                full_paragraph = " ".join(block_spans_text).replace('\n', ' ').replace('\r', ' ')
                extracted_paragraphs.append(full_paragraph)
                        
    total_paras = len(extracted_paragraphs)
    print(f"Extracted {total_paras} coherent paragraphs.")
    
    os.makedirs(output_dir, exist_ok=True)
    num_chunks = math.ceil(total_paras / CHUNK_SIZE)
    print(f"Splitting into {num_chunks} chunks...")
    
    for i in range(num_chunks):
        chunk_paras = extracted_paragraphs[i*CHUNK_SIZE : (i+1)*CHUNK_SIZE]
        chunk_file = os.path.join(output_dir, f"para_chunk_{i+1:03d}.txt")
        with open(chunk_file, 'w', encoding='utf-8') as f:
            for para in chunk_paras:
                f.write(para + "\n")
                
    print("Extraction complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract coherent paragraphs from MinerU JSON.")
    parser.add_argument("middle_json", help="Path to original MinerU _middle.json")
    parser.add_argument("output_dir", help="Directory to save the paragraph chunk TXT files")
    args = parser.parse_args()
    
    extract_paragraphs(args.middle_json, args.output_dir)
