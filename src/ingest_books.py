import os
import shutil
import re
import subprocess
import hashlib
import json
from pathlib import Path

# ==============================================================================
# BSF Data Pipeline (Semantic Chunking & Integrity Checks)
# 职责：将 Markdown 转入 staging area，并进行语义树状切块，随后调用防丢守护神校验。
# ==============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
GUARDS_DIR = PROJECT_ROOT / "src" / "guards"

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_')

def generate_static_hash_tree(chunked_content: str, clean_id: str, dest_dir: Path) -> Path:
    """
    Reverse Assertion Network & Hash Trees (Tier 1~3 static hash tree)
    通过纯静态文件后置对比，实现零状态追踪下的全局语义衰减测试。
    """
    lines = chunked_content.split('\n')
    
    # Tier 1: 全局防篡改 Hash
    tier1_hash = hashlib.sha256(chunked_content.encode('utf-8')).hexdigest()
    
    tier2_blocks = {}
    tier3_locks = {}
    
    current_h1_key = "0_Root"
    current_block = []
    h1_counter = 0
    
    for line in lines:
        if line.startswith("# "):
            if current_block:
                block_text = "\n".join(current_block)
                tier2_blocks[current_h1_key] = hashlib.md5(block_text.encode('utf-8')).hexdigest()
                
            current_h1 = line[2:].strip()
            h1_counter += 1
            current_h1_key = f"{h1_counter}_{current_h1}"
            current_block = []
            
            # 为每个 H1 节点分配反向断言布尔锁 (false_thesis/true_synthesis)
            h1_hash = hashlib.md5(current_h1.encode('utf-8')).hexdigest()
            tier3_locks[current_h1_key] = {
                "false_thesis": f"FLS_{h1_hash[:8]}",
                "true_synthesis": f"TRU_{h1_hash[:8]}"
            }
        current_block.append(line)
        
    if current_block:
        tier2_blocks[current_h1_key] = hashlib.md5("\n".join(current_block).encode('utf-8')).hexdigest()

    hash_tree = {
        "tier1_global_hash": tier1_hash,
        "tier2_volume_hashes": tier2_blocks,
        "tier3_boolean_locks": tier3_locks
    }

    hash_tree_path = dest_dir / f"{clean_id}_hash_tree.json"
    with open(hash_tree_path, 'w', encoding='utf-8') as f:
        json.dump(hash_tree, f, indent=4, ensure_ascii=False)
        
    return hash_tree_path

def semantic_chunk_markdown(content: str, book_name: str) -> str:
    """
    抛弃 350 token 物理切块，改为基于 H1/H2 的树状切块并注入面包屑。
    【新增】为大模型在 Markdown 文本中硬编码植入 false_thesis/true_synthesis 布尔锁。
    """
    lines = content.split('\n')
    chunked_lines = []
    
    current_h1 = ""
    current_h2 = ""
    
    for line in lines:
        if line.startswith("# "):
            current_h1 = line[2:].strip()
            current_h2 = ""
            h1_hash = hashlib.md5(current_h1.encode('utf-8')).hexdigest()
            
            chunked_lines.append(f"\n[BREADCRUMB_CTX: 《{book_name}》 > {current_h1}]\n")
            # 预埋布尔锁断言
            chunked_lines.append(f"[ASSERTION_LOCK: TRUE_SYNTHESIS=TRU_{h1_hash[:8]} | FALSE_THESIS=FLS_{h1_hash[:8]}]\n")
            chunked_lines.append(line)
            
        elif line.startswith("## "):
            current_h2 = line[3:].strip()
            chunked_lines.append(f"\n[BREADCRUMB_CTX: 《{book_name}》 > {current_h1} > {current_h2}]\n")
            chunked_lines.append(line)
        else:
            chunked_lines.append(line)
            
    return '\n'.join(chunked_lines)

def ingest():
    source_root = Path(r"E:\MinerU\Tasks\gafa-1-future-book_output")
    dest_dir = PROJECT_ROOT / "data" / "books"
    
    if not source_root.exists():
        print(f"Source dir {source_root} not found.")
        return
        
    dest_dir.mkdir(parents=True, exist_ok=True)
    GUARDS_DIR.mkdir(parents=True, exist_ok=True)
    
    validator_script = GUARDS_DIR / "ingestion_validator.py"
    
    count = 0
    for book_dir in source_root.iterdir():
        if book_dir.is_dir():
            auto_dir = book_dir / "auto"
            if auto_dir.exists():
                md_files = list(auto_dir.glob("*.md"))
                if md_files:
                    largest_md = max(md_files, key=lambda f: f.stat().st_size)
                    clean_id = slugify(book_dir.name)
                    
                    raw_dest = dest_dir / f"{clean_id}_raw.md"
                    chunked_dest = dest_dir / f"{clean_id}.md"
                    
                    # 1. 复制原文件作为基准
                    shutil.copy2(largest_md, raw_dest)
                    
                    # 2. 读取并执行语义切块
                    with open(raw_dest, 'r', encoding='utf-8') as f:
                        raw_content = f.read()
                        
                    chunked_content = semantic_chunk_markdown(raw_content, book_dir.name)
                    
                    with open(chunked_dest, 'w', encoding='utf-8') as f:
                        f.write(chunked_content)
                        
                    # 预埋静态 Hash Tree 以防多 Agent 并发时的状态踩踏隐患
                    generate_static_hash_tree(chunked_content, clean_id, dest_dir)
                        
                    print(f"[*] Ingested & Chunked: {book_dir.name} -> {clean_id}.md")
                    
                    # 3. 核心功能保护：调用漏洞校验器
                    if validator_script.exists():
                        try:
                            subprocess.run(
                                ["python", str(validator_script), str(raw_dest), str(chunked_dest)],
                                check=True
                            )
                        except subprocess.CalledProcessError:
                            print(f"[!] 校验失败，清空不合格的转换结果。")
                            if chunked_dest.exists(): chunked_dest.unlink()
                            continue
                            
                    # 清理中间文件
                    if raw_dest.exists(): raw_dest.unlink()
                    count += 1
                else:
                    print(f"[-] No Markdown found in {auto_dir}")
            else:
                print(f"[-] No 'auto' dir in {book_dir}")
                
    print(f"\n[OK] Successfully ingested, semantically chunked, and validated {count} books.")

if __name__ == "__main__":
    ingest()
