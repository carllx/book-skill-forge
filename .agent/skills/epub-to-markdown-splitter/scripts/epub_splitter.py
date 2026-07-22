# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "ebooklib",
#     "beautifulsoup4",
#     "markdownify",
# ]
# ///

import argparse
import os
import re
import logging
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify
import ebooklib
from ebooklib import epub
import posixpath

# 配置日志（使用简体中文）
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ChapterFilter:
    def __init__(self):
        self.noise_patterns = [
            r'^subject index$',
            r'^author index$',
            r'^index$',
            r'^bibliography$',
            r'^references$'
        ]
        self.compiled_patterns = [re.compile(p, re.IGNORECASE) for p in self.noise_patterns]

    def is_noise_chapter(self, title: str) -> bool:
        if not title:
            return False
        clean_title = title.strip()
        return any(pattern.search(clean_title) for pattern in self.compiled_patterns)

def process_internal_links(soup: BeautifulSoup):
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if not href.startswith(('http://', 'https://', 'mailto:')):
            a_tag.unwrap()

def sanitize_and_truncate_filename(index: int, title: str, max_length: int = 40) -> str:
    clean_title = re.sub(r'[<>:"/\\|?*\n\r\t]', '', title)
    clean_title = re.sub(r'\s+', '_', clean_title).strip('_')
    if not clean_title:
        clean_title = "Untitled_Chapter"
    truncated_title = clean_title[:max_length].strip('_')
    return f"{index:03d}_{truncated_title}"

def extract_content_by_id(soup, anchor_id, all_anchors):
    """
    根据锚点 ID 提取 HTML 内容。
    找到包含该锚点且不包含其他 TOC 锚点的最大容器节点，
    然后提取该容器节点及其后续的所有同级节点，直到遇到包含其他 TOC 锚点的节点为止。
    """
    element = soup.find(id=anchor_id)
    if not element:
        # 有些 EPUB 的旧式锚点使用 a 标签的 name 属性
        element = soup.find(attrs={'name': anchor_id})
        
    if not element:
        return ""
    
    # 1. 寻找最大的独立容器（不包含其他的 TOC 锚点）
    curr = element
    best = curr
    while curr.parent and curr.parent.name not in ['body', 'html', '[document]']:
        curr = curr.parent
        found_ids = set()
        for el in curr.find_all(True):
            if el.get('id'): found_ids.add(el.get('id'))
            if el.get('name'): found_ids.add(el.get('name'))
            
        other_ids = found_ids.intersection(all_anchors) - {anchor_id}
        if other_ids:
            # 当前节点包含了其他的 TOC 锚点，说明它太大了，应该使用上一个 best
            break
        best = curr
        
    # 2. 收集 best 及其所有后续兄弟节点，直到遇到下一个包含 TOC 锚点的节点
    content = str(best)
    for sibling in best.find_next_siblings():
        sibling_ids = set()
        if not isinstance(sibling, str):
            if sibling.get('id'): sibling_ids.add(sibling.get('id'))
            if sibling.get('name'): sibling_ids.add(sibling.get('name'))
            for el in sibling.find_all(True):
                if el.get('id'): sibling_ids.add(el.get('id'))
                if el.get('name'): sibling_ids.add(el.get('name'))
                
        if sibling_ids.intersection(all_anchors):
            break
        content += str(sibling)
        
    return content

def process_images(soup, book, epub_href, output_dir):
    """
    处理 HTML 中的图片。
    将 EPUB 中的图片文件提取并保存到输出目录下的 images 文件夹，
    同时将 img 标签的 src 属性重写为相对路径。
    """
    images_dir = output_dir / "images"
    
    for img in soup.find_all('img'):
        src = img.get('src')
        if not src:
            continue
            
        # 计算图片在 EPUB 内部的绝对路径
        base_dir = posixpath.dirname(epub_href)
        img_href = posixpath.normpath(posixpath.join(base_dir, src))
        
        # 尝试通过 href 获取图片对象
        img_item = book.get_item_with_href(img_href)
        if not img_item:
            logging.warning(f"无法在 EPUB 中找到图片: {img_href}")
            continue
            
        images_dir.mkdir(parents=True, exist_ok=True)
        img_filename = posixpath.basename(img_href)
        # 处理可能的文件名冲突（如果有同名图片，这里会覆盖，实际可根据需要加上 UUID）
        img_dest = images_dir / img_filename
        
        # 写入图片文件
        with open(img_dest, 'wb') as f:
            f.write(img_item.get_content())
            
        # 重写 img 标签的 src
        img['src'] = f"images/{img_filename}"

def parse_toc(toc, depth=0):
    """
    解析 EPUB 的目录结构（TOC），将其展平为 (标题, href, 层级) 的列表。
    """
    items = []
    for item in toc:
        if isinstance(item, tuple):
            # 通常是 (Section/Link, [nested_toc])
            section = item[0]
            nested_toc = item[1]
            if hasattr(section, 'title') and hasattr(section, 'href'):
                items.append((section.title, section.href, depth))
            items.extend(parse_toc(nested_toc, depth + 1))
        elif hasattr(item, 'title') and hasattr(item, 'href'):
            # 支持 epub.Link 和 epub.Section 等
            items.append((item.title, item.href, depth))
    return items

def split_markdown_content(md_text, max_chars):
    """
    按尽可能大的粒度（段落级别）将 Markdown 切分为多个片段，每个片段尽量不超过 max_chars。
    """
    chunks = []
    paragraphs = md_text.split('\n\n')
    current_chunk = ""
    for p in paragraphs:
        if len(current_chunk) + len(p) + 2 > max_chars:
            if current_chunk:
                chunks.append(current_chunk.strip())
                current_chunk = p
            else:
                # 极端情况：单个段落超长，强行截断
                chunks.append(p[:max_chars])
                current_chunk = p[max_chars:]
        else:
            if current_chunk:
                current_chunk += "\n\n" + p
            else:
                current_chunk = p
    
    # 追加最后一个 chunk
    if current_chunk:
        chunks.append(current_chunk.strip())
        
    return chunks

def main():
    parser = argparse.ArgumentParser(description="将 EPUB 文件依据其目录拆分为多个独立的 Markdown 文件")
    parser.add_argument("-i", "--input", required=True, help="输入 EPUB 文件路径")
    parser.add_argument("-o", "--output", required=True, help="输出目录")
    parser.add_argument("--max-chars", type=int, default=8000, help="单个输出文件的最大字符数，用于适配大模型上下文 (默认: 8000)")
    parser.add_argument("--full", action="store_true", help="是否同时生成合并的完整版 md")
    args = parser.parse_args()

    input_file = args.input
    output_dir = Path(args.output)
    max_chars = args.max_chars

    if not os.path.exists(input_file):
        logging.error(f"输入文件不存在: {input_file}")
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    logging.info(f"开始读取 EPUB 文件: {input_file}")
    
    try:
        book = epub.read_epub(input_file)
    except Exception as e:
        logging.error(f"解析 EPUB 失败: {e}")
        return

    # 提取书籍元数据
    book_title_meta = book.get_metadata('DC', 'title')
    book_title = book_title_meta[0][0] if book_title_meta else "未知书籍"
    
    book_creator_meta = book.get_metadata('DC', 'creator')
    book_creator = book_creator_meta[0][0] if book_creator_meta else "未知作者"

    # 解析目录
    toc_items = parse_toc(book.toc)
    if not toc_items:
        logging.warning("未能在 EPUB 中提取到有效目录信息。")
        return

    index_content = [
        f"# {book_title}",
        f"\n**作者**: {book_creator}\n",
        "## 🎯 智能路由面板",
        "本文档是针对 Agent 阅读优化的知识索引。为避免上下文超载，请根据下方的树状目录按需读取对应章节的 Markdown 文件。",
        "\n## 🔍 Agent 检索指南",
        "- **精准定位**: 如果寻找特定的领域概念或术语，请优先使用 `grep_search` 工具在当前目录下全文搜索 `*.md`，而非猜测章节。",
        "- **连贯阅读**: 当需要深入理解某个话题时，请沿着目录的嵌套层级（从父章节到子小节）依次阅读；如果是被拆分的子章节（`part1`, `part2`），请按序号顺序连续读取。",
        "\n## 目录导航\n"
    ]
    full_content = []
    
    # 预先收集所有文件中存在的 TOC 锚点（按文件分组）
    file_to_anchors = {}
    for title, href, depth in toc_items:
        if '#' in href:
            f_href, anc = href.split('#', 1)
            file_to_anchors.setdefault(f_href, set()).add(anc)
            
    chapter_filter = ChapterFilter()
    total_extracted_chars = 0
            
    for idx, (title, href, depth) in enumerate(toc_items, 1):
        if chapter_filter.is_noise_chapter(title):
            logging.info(f"跳过索引/噪声章节: {title}")
            continue
            
        if not title:
            title = f"未命名章节_{idx}"
            
        safe_title = sanitize_and_truncate_filename(idx, title)
        
        # 分离 href 中的文件路径和锚点
        if '#' in href:
            file_href, anchor = href.split('#', 1)
        else:
            file_href, anchor = href, None
            
        # 获取对应的 HTML 文件内容
        item = book.get_item_with_href(file_href)
        if not item:
            logging.warning(f"无法在 EPUB 中找到章节文件: {file_href}")
            continue
            
        try:
            html_content = item.get_content().decode('utf-8', errors='ignore')
        except Exception as e:
            logging.warning(f"解码章节文件失败 {file_href}: {e}")
            continue
            
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 剥离失效的内部链接
        process_internal_links(soup)
        
        # 处理并保存图片，重写 src
        process_images(soup, book, file_href, output_dir)
        
        # 获取当前文件所有的 TOC 锚点
        all_anchors = file_to_anchors.get(file_href, set())
        
        # 根据是否带有锚点进行内容切割
        if anchor:
            extracted_html = extract_content_by_id(soup, anchor, all_anchors)
            if not extracted_html:
                logging.warning(f"未找到锚点 '{anchor}'，将回退使用整个文件内容。")
                extracted_html = str(soup.body) if soup.body else str(soup)
        else:
            if not all_anchors:
                extracted_html = str(soup.body) if soup.body else str(soup)
            else:
                # 提取从 body 开始直到遇到第一个 TOC 锚点的内容
                content = ""
                if soup.body:
                    for child in soup.body.children:
                        child_ids = set()
                        if not isinstance(child, str):
                            if child.get('id'): child_ids.add(child.get('id'))
                            if child.get('name'): child_ids.add(child.get('name'))
                            for el in child.find_all(True):
                                if el.get('id'): child_ids.add(el.get('id'))
                                if el.get('name'): child_ids.add(el.get('name'))
                        if child_ids.intersection(all_anchors):
                            break
                        content += str(child)
                extracted_html = content if content else (str(soup.body) if soup.body else str(soup))
            
        # 将提取出的 HTML 片段转为 Markdown
        md_text = markdownify(extracted_html, heading_style="ATX").strip()
        
        # 确保章节文本以标题开头
        if not md_text.startswith('#'):
            md_text = f"# {title}\n\n{md_text}"
            
        total_extracted_chars += len(md_text.strip())
            
        # 根据 max-chars 进行切分
        chunks = split_markdown_content(md_text, max_chars)
        
        indent = "  " * depth
        if len(chunks) == 1:
            # 不需要切分
            md_filename = f"{safe_title}.md"
            md_filepath = output_dir / md_filename
            breadcrumb = f"> [BREADCRUMB_CTX: 《{book_title}》 > {title}]\n\n"
            with open(md_filepath, 'w', encoding='utf-8') as f:
                f.write(breadcrumb + chunks[0])
            logging.info(f"生成章节成功: {md_filename}")
            index_content.append(f"{indent}- [{title}]({md_filename})")
        else:
            # 需要切分
            logging.info(f"章节超长，将被拆分为 {len(chunks)} 个文件: {safe_title}")
            index_content.append(f"{indent}- {title}")
            for part_idx, chunk in enumerate(chunks, 1):
                part_filename = f"{safe_title}_part{part_idx}.md"
                part_filepath = output_dir / part_filename
                
                breadcrumb = f"> [BREADCRUMB_CTX: 《{book_title}》 > {title} (Part {part_idx})]\n\n"
                # 为后续的 part 增加一个引用上下文的标题
                if part_idx > 1 and not chunk.startswith('#'):
                    chunk = f"## {title} (Part {part_idx})\n\n{breadcrumb}{chunk}"
                else:
                    chunk = f"{breadcrumb}{chunk}"
                    
                with open(part_filepath, 'w', encoding='utf-8') as f:
                    f.write(chunk)
                logging.info(f"生成子章节成功: {part_filename}")
                part_indent = indent + "  "
                index_content.append(f"{part_indent}- [Part {part_idx}]({part_filename})")
        
        if args.full:
            full_content.append(md_text)

    if total_extracted_chars < 200:
        logging.error("致命错误: 提取的文本内容过短（不足 200 字）。这通常是因为 EPUB 为空壳或受保护。中止操作以防止下游模型发生幻觉！")
        import sys
        sys.exit(1)

    # 写入总目录文件
    index_filepath = output_dir / "index.md"
    with open(index_filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(index_content))
    logging.info("生成总目录导航文件: index.md")

    # 如果指定了 --full 参数，则生成完整版的 Markdown
    if args.full:
        full_filepath = output_dir / "full.md"
        with open(full_filepath, 'w', encoding='utf-8') as f:
            f.write("\n\n---\n\n".join(full_content))
        logging.info("生成合并的完整版文件: full.md")
        
    logging.info("EPUB 拆分转换任务全部完成！")

if __name__ == "__main__":
    main()
