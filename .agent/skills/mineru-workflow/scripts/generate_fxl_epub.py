import json
import argparse
import sys
import os
import math
import zipfile
import shutil

def generate_fxl_epub(mineru_json_path, output_epub_path):
    """
    Reads a MinerU JSON (typically the merged _middle_zh.json) and builds a 
    Fixed-Layout EPUB3, utilizing native CSS text wrapping for block containers.
    """
    if not os.path.exists(mineru_json_path):
        print("Error: MinerU JSON file not found.")
        sys.exit(1)
        
    with open(mineru_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    pages = data.get("pdf_info", [])
    if not pages:
        if isinstance(data, list): pages = data
        else:
            print("Error: Cannot find pages in MinerU JSON.")
            sys.exit(1)
            
    temp_dir = "temp_epub_build"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    
    oebps_dir = os.path.join(temp_dir, "OEBPS")
    meta_dir = os.path.join(temp_dir, "META-INF")
    os.makedirs(meta_dir)
    os.makedirs(os.path.join(oebps_dir, "css"))
    os.makedirs(os.path.join(oebps_dir, "images"))
    
    # 1. Create META-INF/container.xml
    with open(os.path.join(meta_dir, "container.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0"?>\n<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n  <rootfiles>\n    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>\n  </rootfiles>\n</container>')

    # 2. Create CSS
    with open(os.path.join(oebps_dir, "css", "style.css"), "w", encoding="utf-8") as f:
        f.write("""
        body { margin: 0; padding: 0; background-color: #ffffff; }
        .text-block { 
            position: absolute; 
            box-sizing: border-box; 
            overflow: hidden; 
            font-family: sans-serif;
            text-align: justify;
            line-height: 1.4;
        }
        .img-block { 
            position: absolute; 
        }
        """)

    manifest_items = []
    spine_items = []
    
    for page_index, page in enumerate(pages):
        page_no = page.get("page_no", page_index)
        page_size = page.get("page_size", [800, 1200])
        width, height = page_size[0], page_size[1]
        
        html_content = [
            f'<?xml version="1.0" encoding="utf-8"?>',
            f'<!DOCTYPE html>',
            f'<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">',
            f'<head><title>Page {page_no}</title>',
            f'<meta name="viewport" content="width={width}, height={height}" />',
            f'<link rel="stylesheet" type="text/css" href="css/style.css" />',
            f'</head><body>'
        ]
        
        para_blocks = page.get("para_blocks", [])
        raw_blocks = page.get("preproc_blocks", [])
        
        # 1. Process images from the raw physical blocks
        for block in raw_blocks:
            b_type = block.get("type", "")
            if b_type == "image":
                bbox = block.get("bbox", [0, 0, 0, 0])
                if len(bbox) != 4:
                    bbox = [0, 0, 0, 0]
                x0, y0, x1, y1 = bbox
                bw, bh = x1 - x0, y1 - y0
                img_path = block.get("image_path", "")
                if not img_path:
                    for sub_block in block.get("blocks", []):
                        for line in sub_block.get("lines", []):
                            for span in line.get("spans", []):
                                if span.get("image_path"):
                                    img_path = span.get("image_path")
                                    break
                
                if img_path:
                    img_name = os.path.basename(img_path)
                    src_img = os.path.join(os.path.dirname(mineru_json_path), img_path)
                    if not os.path.exists(src_img):
                        src_img_alt = os.path.join(os.path.dirname(mineru_json_path), "images", img_name)
                        if os.path.exists(src_img_alt):
                            src_img = src_img_alt
                            
                    if os.path.exists(src_img):
                        shutil.copy(src_img, os.path.join(oebps_dir, "images", img_name))
                        html_content.append(f'<img class="img-block" src="images/{img_name}" style="left:{x0}px; top:{y0}px; width:{bw}px; height:{bh}px;" />')
                        if img_name not in [x[0] for x in manifest_items]:
                            manifest_items.append((img_name, f"images/{img_name}", "image/jpeg"))
                            
        # 2. Process text from the consolidated para_blocks
        for block in para_blocks:
            b_type = block.get("type", "")
            
            if b_type in ["text", "title"]:
                # We assume the JSON is already merged using Block Container logic
                # So we just extract the text from the single span inside the block
                zh_text = ""
                lines = block.get("lines", [])
                for line in lines:
                    for span in line.get("spans", []):
                        content = span.get("content", "").strip()
                        if content:
                            zh_text += content
                
                if zh_text.strip():
                    bbox = block.get("bbox", [0, 0, 0, 0])
                    x0, y0, x1, y1 = bbox
                    bw, bh = x1 - x0, y1 - y0
                    
                    # Estimate optimal font size using area distribution for unified blocks
                    char_count = max(1, len(zh_text))
                    area = bw * bh
                    calc_size = math.sqrt(area / char_count) * 0.75
                    font_size = max(8, min(int(calc_size), 72))
                    
                    html_content.append(f'<div class="text-block" style="left:{x0}px; top:{y0}px; width:{bw}px; height:{bh}px; font-size:{font_size}px;">{zh_text}</div>')
        
        html_content.append('</body></html>')
        page_filename = f"page_{page_no}.xhtml"
        with open(os.path.join(oebps_dir, page_filename), "w", encoding="utf-8") as f:
            f.write("\n".join(html_content))
            
        manifest_items.append((f"page_{page_no}", page_filename, "application/xhtml+xml"))
        spine_items.append(f"page_{page_no}")
        
    # 3. Create content.opf
    opf_content = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="BookId">',
        '  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">',
        '    <dc:title>Translated FXL Book</dc:title>',
        '    <dc:language>zh-CN</dc:language>',
        '    <meta property="rendition:layout">pre-paginated</meta>',
        '    <meta property="rendition:orientation">auto</meta>',
        '    <meta property="rendition:spread">none</meta>',
        '  </metadata>',
        '  <manifest>',
        '    <item id="style" href="css/style.css" media-type="text/css"/>'
    ]
    for m_id, href, media_type in manifest_items:
        opf_content.append(f'    <item id="{m_id}" href="{href}" media-type="{media_type}"/>')
    
    opf_content.append('  </manifest>\n  <spine>')
    for s_id in spine_items:
        opf_content.append(f'    <itemref idref="{s_id}"/>')
    opf_content.append('  </spine>\n</package>')
    
    with open(os.path.join(oebps_dir, "content.opf"), "w", encoding="utf-8") as f:
        f.write("\n".join(opf_content))
        
    # 4. Zip into EPUB
    with zipfile.ZipFile(output_epub_path, 'w', zipfile.ZIP_DEFLATED) as epub:
        epub.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        for root, _, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, temp_dir)
                epub.write(file_path, arcname)
                
    shutil.rmtree(temp_dir)
    print(f"Generated Fixed-Layout EPUB successfully: {output_epub_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Fixed-Layout EPUB from merged MinerU JSON using Block Containers.")
    parser.add_argument("mineru_json", help="Path to merged MinerU _middle_zh.json")
    parser.add_argument("output_epub", help="Path for the output .epub file")
    
    args = parser.parse_args()
    generate_fxl_epub(args.mineru_json, args.output_epub)
