# /// script
# requires-python = ">=3.9"
# ///

import argparse
import os
import logging
from pathlib import Path

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def split_markdown_content(md_text, max_chars):
    chunks = []
    paragraphs = md_text.split('\n\n')
    current_chunk = ""
    for p in paragraphs:
        if len(current_chunk) + len(p) + 2 > max_chars:
            if current_chunk:
                chunks.append(current_chunk.strip())
                current_chunk = p
            else:
                chunks.append(p[:max_chars])
                current_chunk = p[max_chars:]
        else:
            if current_chunk:
                current_chunk += "\n\n" + p
            else:
                current_chunk = p
    
    if current_chunk:
        chunks.append(current_chunk.strip())
        
    return chunks

def main():
    parser = argparse.ArgumentParser(description="将单体 Markdown 文件切分为带面包屑的多个文件")
    parser.add_argument("-i", "--input", required=True, help="输入 Markdown 文件路径")
    parser.add_argument("-o", "--output", required=True, help="输出目录")
    parser.add_argument("--title", required=True, help="书名（用于生成面包屑）")
    parser.add_argument("--max-chars", type=int, default=8000, help="单片段最大字符数")
    args = parser.parse_args()

    input_file = Path(args.input)
    output_dir = Path(args.output)
    book_title = args.title

    if not input_file.exists():
        logging.error(f"输入文件不存在: {input_file}")
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    logging.info(f"开始读取文件: {input_file}")
    
    try:
        md_text = input_file.read_text(encoding='utf-8')
    except Exception as e:
        logging.error(f"读取文件失败: {e}")
        return

    chunks = split_markdown_content(md_text, args.max_chars)
    
    index_content = [
        f"# {book_title}",
        "## 目录导航\n"
    ]

    for part_idx, chunk in enumerate(chunks, 1):
        part_filename = f"part_{part_idx:03d}.md"
        part_filepath = output_dir / part_filename
        
        breadcrumb = f"> [BREADCRUMB_CTX: 《{book_title}》 > Part {part_idx}]\n\n"
        
        # 确保包含标题，避免只有零碎文本
        if not chunk.startswith('#'):
            chunk = f"## Part {part_idx}\n\n{breadcrumb}{chunk}"
        else:
            chunk = f"{breadcrumb}{chunk}"
            
        part_filepath.write_text(chunk, encoding='utf-8')
        logging.info(f"生成片段: {part_filename}")
        index_content.append(f"- [Part {part_idx}]({part_filename})")

    index_filepath = output_dir / "index.md"
    index_filepath.write_text("\n".join(index_content), encoding='utf-8')
    logging.info("生成索引文件: index.md")
    logging.info("转换完成！")

if __name__ == "__main__":
    main()
