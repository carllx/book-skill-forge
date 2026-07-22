#!/usr/bin/env python3
import sys
import json
import os
import subprocess
from pathlib import Path
import re

def print_usage():
    print("Usage: python ingestion_pipeline.py <input_file> <output_ir_dir>")
    sys.exit(1)

def extract_with_pandoc(input_path: Path) -> str:
    """Uses pandoc to convert docx/pdf/html/md to plain markdown."""
    # Based on user global rules, Pandoc 3.5 is available.
    try:
        # Convert everything to markdown as the universal text base
        result = subprocess.run(
            ['pandoc', str(input_path), '-t', 'markdown'],
            capture_output=True, text=True, check=True
        )
        return result.stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Pandoc extraction failed or pandoc not found: {e}", file=sys.stderr)
        # Fallback for simple text files
        try:
            return input_path.read_text(encoding='utf-8')
        except Exception:
            return ""

def assign_semantic_type(block_text: str) -> str:
    """Heuristic / Regex based semantic typing."""
    block_lower = block_text.lower()
    
    # 1. Procedure/Step
    if re.search(r'^(步骤|step|1\.|first|首先|接着|然后|点击|navigate|click|run|execute)', block_lower, re.IGNORECASE):
        return 'Procedure'
    if re.search(r'^(-\s*\[[x\s]\]|\*\s*\[[x\s]\])', block_lower):
        return 'Procedure'
        
    # 2. Rule/Constraint
    if re.search(r'(必须|必须不|禁止|注意|警告|warning|caution|must|never|always|确保|ensure)', block_lower):
        return 'Rule'
        
    # 3. Trigger
    if re.search(r'^(当|什么时候|如果|条件|触发|when|if|in case of|use this when)', block_lower):
        return 'Trigger'
        
    # 4. Principle/Heuristic (Interaction Design Specific)
    if re.search(r'(principle|heuristic|pattern|rule of thumb|启发式|设计原则|guideline)', block_lower):
        return 'Heuristic'
        
    # 5. Case Study/Example (Interaction Design Specific)
    if re.search(r'(case study|example|dilemma|trade-off|tradeoff|案例|权衡|dilemmas)', block_lower):
        return 'Case_Study'
        
    # Default to Concept
    return 'Concept'

def parse_markdown_to_ir(markdown_text: str, source_name: str) -> list:
    """Parses markdown into hierarchical blocks."""
    lines = markdown_text.split('\n')
    blocks = []
    current_block = []
    current_level = 0
    
    def flush_block():
        if current_block:
            text = '\n'.join(current_block).strip()
            if text:
                sem_type = assign_semantic_type(text)
                blocks.append({
                    "content": text,
                    "hierarchy_level": current_level,
                    "semantic_type": sem_type,
                    "source_metadata": {
                        "source_file": source_name
                    }
                })
            current_block.clear()

    for line in lines:
        header_match = re.match(r'^(#{1,6})\s+(.*)', line)
        if header_match:
            flush_block()
            current_level = len(header_match.group(1))
            current_block.append(line)
            flush_block()
        elif line.strip() == '':
            flush_block()
        else:
            current_block.append(line)
            
    flush_block()
    return blocks

def main():
    if len(sys.argv) != 3:
        print_usage()
        
    input_path = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    
    if not input_path.exists():
        print(f"Error: {input_path} not found.")
        sys.exit(1)
        
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if input_path.is_dir():
        print(f"[*] Ingesting directory (Passthrough Mode): {input_path.name}")
        md_files = list(input_path.glob('*.md'))
        if len(md_files) > 1:
            print(f"[+] Detected structured directory with {len(md_files)} markdown files.")
            output_file = output_dir / f"{input_path.name}_ir.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "passthrough": True,
                    "source_dir": str(input_path.absolute()),
                    "blocks": []
                }, f, ensure_ascii=False, indent=2)
            print(f"[+] Saved Passthrough IR to {output_file}")
            sys.exit(0)
        else:
            print("[-] Directory does not contain multiple markdown files. Cannot passthrough.")
            sys.exit(1)
            
    print(f"[*] Ingesting document: {input_path.name}")
    md_content = extract_with_pandoc(input_path)
    
    if not md_content:
        print("[-] Failed to extract content.")
        sys.exit(1)
        
    ir_blocks = parse_markdown_to_ir(md_content, input_path.name)
    
    print(f"[*] Normalization complete. Extracted {len(ir_blocks)} semantic blocks.")
    
    # Save the Universal Multi-format Data Model (UMDM) IR
    output_file = output_dir / f"{input_path.stem}_ir.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            "passthrough": False,
            "blocks": ir_blocks
        }, f, ensure_ascii=False, indent=2)
        
    print(f"[+] Saved Intermediate Representation to {output_file}")

if __name__ == "__main__":
    main()
