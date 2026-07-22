import json
import argparse
import sys
import os

def extract_translation_job(mineru_json_path, output_dir, file_prefix="translation_job", chunk_size_chars=4000):
    """
    Reads the MinerU JSON output, extracts text blocks, and chunks them into 
    multiple JSON files to accommodate LLM token limits for sub-agents.
    """
    if not os.path.exists(mineru_json_path):
        print(f"Error: Could not find {mineru_json_path}")
        sys.exit(1)

    with open(mineru_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    pages = data.get("pdf_info", [])
    if not pages:
        print("Warning: 'pdf_info' key not found, attempting to process as a raw list of pages if applicable.")
        if isinstance(data, list):
            pages = data
        else:
            print("Error: Unrecognized MinerU JSON structure. Cannot find pages.")
            sys.exit(1)

    translation_job = []
    
    for page_index, page in enumerate(pages):
        page_no = page.get("page_no", page_index)
        blocks = page.get("para_blocks", page.get("blocks", []))
        
        for block_index, block in enumerate(blocks):
            block_type = block.get("type", "unknown")
            text_content = block.get("text", "")
            
            # Extract text from lines -> spans if text_content is empty
            if not text_content and "lines" in block:
                for line in block["lines"]:
                    if "spans" in line:
                        for span in line["spans"]:
                            if "content" in span:
                                text_content += span["content"]
            
            if text_content and block_type not in ["image", "equation"]:
                job_item = {
                    "id": f"p{page_no}_b{block_index}",
                    "page_no": page_no,
                    "type": block_type,
                    "text": text_content
                }
                translation_job.append(job_item)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Chunking logic based on character count
    chunks = []
    current_chunk = []
    current_chars = 0
    
    for item in translation_job:
        text_len = len(item["text"])
        if current_chunk and (current_chars + text_len) > chunk_size_chars:
            chunks.append(current_chunk)
            current_chunk = []
            current_chars = 0
        
        current_chunk.append(item)
        current_chars += text_len
        
    if current_chunk:
        chunks.append(current_chunk)

    # Export chunks
    for i, chunk in enumerate(chunks):
        part_num = str(i + 1).zfill(3)
        chunk_path = os.path.join(output_dir, f"{file_prefix}_part_{part_num}.json")
        with open(chunk_path, 'w', encoding='utf-8') as out_f:
            json.dump(chunk, out_f, ensure_ascii=False, indent=2)

    print(f"Successfully extracted {len(translation_job)} text blocks.")
    print(f"Split into {len(chunks)} chunk files (Max ~{chunk_size_chars} chars per chunk) in directory: {output_dir}")
    print("Next Step: Have your Sub-agents translate these JSON chunks.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract and chunk text blocks from MinerU JSON for Sub-agent translation.")
    parser.add_argument("input_json", help="Path to the MinerU output JSON (e.g. _middle.json)")
    parser.add_argument("output_dir", help="Directory to save the chunked translation job JSONs")
    parser.add_argument("--chunk-chars", type=int, default=4000, help="Maximum number of characters per JSON chunk (default: 4000)")
    
    args = parser.parse_args()
    extract_translation_job(args.input_json, args.output_dir, chunk_size_chars=args.chunk_chars)
