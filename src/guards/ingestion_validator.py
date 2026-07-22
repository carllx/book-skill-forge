import sys
import hashlib
import re
from pathlib import Path

# BSF 漏洞检查器 - 摄入数据防丢守护神 (Ingestion Validator)
# 职责：在 Ingest 和切块之后，物理校验字符 Hash 确保没有由于分块逻辑导致的长文本漏块、漏段落，保护开源组件的核心转换结果。

def remove_breadcrumbs_and_whitespace(text: str) -> str:
    """剔除面包屑标签和所有空白字符，提取纯骨架文本"""
    # 移除面包屑标签 [BREADCRUMB_CTX: xxx]
    text = re.sub(r'\[BREADCRUMB_CTX:.*?\]', '', text)
    # 移除所有空白字符 (空格、换行、制表符)
    text = re.sub(r'\s+', '', text)
    return text

def validate_integrity(original_md_path: Path, chunked_md_path: Path):
    if not original_md_path.exists() or not chunked_md_path.exists():
        print(f"[ERROR] 找不到校验文件: {original_md_path} 或 {chunked_md_path}")
        sys.exit(1)
        
    print(f"🔍 [Validator] 正在校验核心数据完整性: {original_md_path.name}")
    
    with open(original_md_path, 'r', encoding='utf-8') as f:
        original_text = f.read()
        
    with open(chunked_md_path, 'r', encoding='utf-8') as f:
        chunked_text = f.read()
        
    pure_original = remove_breadcrumbs_and_whitespace(original_text)
    pure_chunked = remove_breadcrumbs_and_whitespace(chunked_text)
    
    len_orig = len(pure_original)
    len_chunk = len(pure_chunked)
    
    if len_orig != len_chunk:
        print("\n" + "!"*50)
        print("💥 [FATAL VULNERABILITY] 数据转换发现漏洞：长文本漏块！")
        print(f"原文字符数: {len_orig}")
        print(f"切块后字符数: {len_chunk}")
        print(f"差值: {abs(len_orig - len_chunk)} 字符")
        print("这会导致开源核心管线（如 Cangjie / Graphify）因数据遗漏而崩溃。转换中断！")
        print("!"*50 + "\n")
        sys.exit(1)
        
    # Hash 物理级比对
    hash_orig = hashlib.sha256(pure_original.encode('utf-8')).hexdigest()
    hash_chunk = hashlib.sha256(pure_chunked.encode('utf-8')).hexdigest()
    
    if hash_orig != hash_chunk:
        print("\n" + "!"*50)
        print("💥 [FATAL VULNERABILITY] 数据转换发现漏洞：内容被篡改或乱序！")
        print(f"Hash 校验失败！")
        print("!"*50 + "\n")
        sys.exit(1)
        
    print(f"✅ [Validator] 数据转换完美无损 (Length: {len_orig}, Hash Match)。核心能力受到保护！")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python ingestion_validator.py <original.md> <chunked.md>")
        sys.exit(1)
        
    validate_integrity(Path(sys.argv[1]), Path(sys.argv[2]))
