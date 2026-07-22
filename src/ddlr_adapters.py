import argparse
import os
import re

def get_book_name(filepath):
    filename = os.path.basename(filepath)
    name, _ = os.path.splitext(filename)
    return name.replace('_', ' ').title()

def unified_logical_chunk(text, book_name, max_chars=80000):
    """
    Large granularity logical chunking based on H1/H2.
    Targets around 30k-50k tokens (roughly 80,000 characters) per chunk to prevent OOM
    while providing the model with a wide context for accurate entity relations and extraction.
    """
    # Split text by H1 or H2, keeping the delimiter
    sections = re.split(r'(?m)^(#{1,2}\s+.*$)', text)
    
    chunks = []
    current_chunk = []
    current_len = 0
    current_h1 = ""
    current_h2 = ""
    current_breadcrumb = ""
    
    # Handle text before the first header if any
    if sections and not re.match(r'^#{1,2}\s+', sections[0]):
        current_chunk.append(sections[0])
        current_len += len(sections[0])
        sections = sections[1:]
        current_breadcrumb = f"[BREADCRUMB_CTX: 《{book_name}》]\n\n"

    i = 0
    while i < len(sections):
        header = sections[i]
        content = sections[i+1] if i + 1 < len(sections) else ""
        i += 2
        
        # Track current logical position
        if header.startswith('## '):
            current_h2 = header[3:].strip()
        elif header.startswith('# '):
            current_h1 = header[2:].strip()
            current_h2 = ""

        part = header + "\n" + content
        part_len = len(part)

        # Set breadcrumb for the new chunk if we just started one
        if current_len == 0:
            current_breadcrumb = f"[BREADCRUMB_CTX: 《{book_name}》"
            if current_h1: current_breadcrumb += f" > {current_h1}"
            if current_h2: current_breadcrumb += f" > {current_h2}"
            current_breadcrumb += "]\n\n"

        # If adding this part exceeds max_chars and we already have content, yield the chunk
        if current_len + part_len > max_chars and current_chunk:
            chunks.append(current_breadcrumb + ''.join(current_chunk))
            current_chunk = []
            current_len = 0
            
            # Setup breadcrumb for the NEXT chunk
            current_breadcrumb = f"[BREADCRUMB_CTX: 《{book_name}》"
            if current_h1: current_breadcrumb += f" > {current_h1}"
            if current_h2: current_breadcrumb += f" > {current_h2}"
            current_breadcrumb += "]\n\n"

        current_chunk.append(part)
        current_len += part_len

    if current_chunk:
        chunks.append(current_breadcrumb + ''.join(current_chunk))
        
    # Filter out empty or too small chunks
    return [c for c in chunks if len(c.strip()) > 50]

def chunk_for_graphify(text, book_name):
    return unified_logical_chunk(text, book_name)

def chunk_for_cangjie(text, book_name):
    return unified_logical_chunk(text, book_name)

def main():
    parser = argparse.ArgumentParser(description="DDLR Text Pulling and Breadcrumb Injection Adapter (V2 Large Granularity)")
    parser.add_argument("--mode", choices=["graphify", "cangjie"], required=True, help="Chunking mode")
    parser.add_argument("--input", required=True, help="Input markdown file")
    parser.add_argument("--output-dir", required=True, help="Output directory for chunks")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} does not exist.")
        return

    with open(args.input, 'r', encoding='utf-8') as f:
        text = f.read()
        
    book_name = get_book_name(args.input)
    os.makedirs(args.output_dir, exist_ok=True)
    
    if args.mode == 'graphify':
        chunks = chunk_for_graphify(text, book_name)
    else:
        chunks = chunk_for_cangjie(text, book_name)
        
    for i, chunk in enumerate(chunks):
        out_path = os.path.join(args.output_dir, f"chunk_{i:04d}.md")
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(chunk)
            
    print(f"Generated {len(chunks)} chunks in {args.output_dir}")

if __name__ == "__main__":
    main()
