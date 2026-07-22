#!/usr/bin/env python3
import sys
import os
import json
import shutil
import re
from pathlib import Path

def print_usage():
    print("Usage: python chunking_engine.py <ir_dir> <output_dir>")
    sys.exit(1)

def process_passthrough(ir_data: dict, output_dir: Path):
    source_dir = Path(ir_data['source_dir'])
    print(f"[*] Processing Passthrough IR. Copying from {source_dir} to {output_dir}")
    
    try:
        from ingestion_pipeline import parse_markdown_to_ir
    except ImportError:
        parse_markdown_to_ir = None

    # Copy all .md files except ones containing '_full'
    for md_file in source_dir.glob('*.md'):
        if '_full' in md_file.name.lower():
            continue
            
        # Defensive Check for Massive Files
        file_size = md_file.stat().st_size
        if file_size > 15360 and parse_markdown_to_ir: # > 15KB
            print(f"[!] Passthrough interception: {md_file.name} is {file_size} bytes (too large). Forcing sub-chunking.")
            content = md_file.read_text(encoding='utf-8')
            blocks = parse_markdown_to_ir(content, md_file.name)
            process_blocks(blocks, output_dir, md_file.stem)
        else:
            shutil.copy2(md_file, output_dir / md_file.name)
        
    # Copy images folder if it exists
    images_dir = source_dir / 'images'
    if images_dir.is_dir():
        dest_images = output_dir / 'images'
        if not dest_images.exists():
            shutil.copytree(images_dir, dest_images)
            
    print("[+] Passthrough completed.")

def process_blocks(blocks: list, output_dir: Path, source_name: str):
    print(f"[*] Processing {len(blocks)} semantic blocks into chunks...")
    
    current_chunk_content = []
    current_header = "preamble"
    chunk_index = 0
    
    def write_chunk():
        nonlocal chunk_index
        if not current_chunk_content:
            return
            
        content_str = "\n\n".join(current_chunk_content)
        if len(content_str) < 50:
            return
            
        safe_header = re.sub(r'[^a-zA-Z0-9_\u4e00-\u9fa5]', '_', current_header)[:30]
        
        # Fallback split for excessively large chunks (> 8000 characters)
        if len(content_str) > 8000:
            sub_chunks = content_str.split("\n\n")
            current_sub = []
            current_len = 0
            sub_idx = 1
            for paragraph in sub_chunks:
                if current_len + len(paragraph) > 6000 and current_sub:
                    filename = output_dir / f"{source_name}_chunk_{chunk_index:03d}_{safe_header}_{sub_idx}.md"
                    filename.write_text("\n\n".join(current_sub), encoding='utf-8')
                    sub_idx += 1
                    current_sub = [paragraph]
                    current_len = len(paragraph)
                else:
                    current_sub.append(paragraph)
                    current_len += len(paragraph)
                    
            if current_sub:
                filename = output_dir / f"{source_name}_chunk_{chunk_index:03d}_{safe_header}_{sub_idx}.md"
                filename.write_text("\n\n".join(current_sub), encoding='utf-8')
                
            chunk_index += 1
            return

        filename = output_dir / f"{source_name}_chunk_{chunk_index:03d}_{safe_header}.md"
        filename.write_text(content_str, encoding='utf-8')
        chunk_index += 1

    for block in blocks:
        level = block.get('hierarchy_level', 0)
        content = block.get('content', '')
        
        is_header = bool(re.match(r'^#{1,6}\s+', content))
        if (level == 1 or level == 2) and is_header:
            write_chunk()
            current_chunk_content = [content]
            # Extract header text from "# Header"
            header_match = re.match(r'^#{1,6}\s+(.*)', content)
            if header_match:
                current_header = header_match.group(1).strip()
            else:
                current_header = content.strip().split('\n')[0]
        else:
            current_chunk_content.append(content)
            
    write_chunk()
    print(f"[+] Successfully generated chunks in {output_dir}")

def main():
    if len(sys.argv) != 3:
        print_usage()
        
    ir_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    
    if not ir_dir.is_dir():
        print(f"Error: {ir_dir} is not a valid directory.")
        sys.exit(1)
        
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for json_file in ir_dir.glob('*_ir.json'):
        print(f"[*] Reading IR file: {json_file.name}")
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if data.get('passthrough'):
            process_passthrough(data, output_dir)
        else:
            process_blocks(data.get('blocks', []), output_dir, json_file.stem.replace('_ir', ''))

if __name__ == "__main__":
    main()
