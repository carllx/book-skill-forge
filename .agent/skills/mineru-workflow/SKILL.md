---
name: mineru-workflow
description: Automates PDF to Markdown/EPUB conversions using MinerU, manages batch processing, handles Imgur link replacements, and provides a custom Fixed-Layout (FXL) EPUB translation workflow using LLM sub-agents. Use this skill when the user asks to process PDFs, extract text/images via MinerU, translate MinerU output into Fixed-Layout Chinese EPUBs, or manage OCR tasks.
---

# Mineru Workflow

## Overview

This skill provides comprehensive workflows for processing PDFs and images into Markdown using the MinerU system. It handles batch conversion tasks, automated Imgur uploads for local images, environment management for `magic-pdf`, and Pandoc conversions from Markdown to EPUB.

## Pre-Requisite Check & OS Detection

**IMPORTANT:** Before proceeding with ANY Mineru OCR task, you MUST execute these checks:

1. **Book Naming Standardization (Academic Convention)**:
   - All input PDF files MUST follow the academic naming convention: `Author - Year - Title.pdf`.
   - The files are stored in the Task folder at `E:\MinerU\Tasks\<TaskName>`.
   - Run `python scripts/rename_books.py --task <TaskName>` to scan the folder.
   - If files are not compliant, you MUST pause and use your abilities (web search, LLM analysis of the filename/content) to deduce the correct Author, Year, and Title. Rename the files to the correct format BEFORE proceeding.
2. **OS & Environment Check**: 
   - Detect the user's Operating System (macOS vs Windows).
   - **If Windows**: MinerU runs exponentially faster with Nvidia GPU/CUDA. 
     - ⚠️ **CRITICAL Windows Setup**: The user's Python and MinerU environment is hardcoded at `E:\MinerU\Env`. You do **NOT** need to run `conda activate`. The executable is at `E:\MinerU\Env\Scripts\magic-pdf.exe`.
   - **If macOS**: MinerU uses MPS/CPU and is much slower. For large files (>100MB), warn the user about potential OOM/slowness, and strongly suggest extracting a small page range (`-s 0 -e 20`) or switching to their Windows GPU machine.
3. **Imgur Check**: 
   - Explicitly ask the user: **"是否需要生成图床 (Imgur) 版本？(默认为否，保留本地图片路径)"**
   - Wait for the user's confirmation before executing any local or API conversions.

## 1. Quick Start / Single File Processing

If using the local Mineru API (FastAPI backend):
1. **Health Check:** Always `curl http://localhost:8000` to check if the server is alive. If the connection is refused, inform the user they need to start the server (e.g. via `start_mac.command`).
2. Trigger the processing via the API Endpoint (see `references/mineru_api_docs.md`). The backend will automatically handle Imgur uploading if configured.

If using local command line (Windows PC):
1. Execute the absolute path directly: `E:\MinerU\Env\Scripts\magic-pdf.exe -p <input.pdf> -o <output_dir> -m auto`

## 2. Batch Processing & Task Architecture (SOP)

MinerU processing is organized using a **Task-based architecture**.
Input files are placed in `E:\MinerU\Tasks\<TaskName>` and outputs will be generated in `E:\MinerU\Tasks\<TaskName>_output`.

### ⚠️ Network Resilience Best Practice
**DO NOT** run batch conversions directly on remote Network/SMB shares. MinerU is highly I/O intensive and network interruptions during long GPU tasks will cause the entire queue to fail.
**Standard Operating Procedure (SOP):**
1. If the user requests processing on a network drive, **PROACTIVELY SUGGEST** copying the files to a local Task folder (e.g., `E:\MinerU\Tasks\<TaskName>`).
2. Write a script to securely copy all PDF files to the local target folder.
3. Run the local batch script providing the Task Name.
4. (Optional) Sync the output folder back to the network drive upon completion.

### Windows Batch Script
- Use the custom batch script `E:\MinerU\batch_convert.ps1`. 
- Execute it by passing the Task Name: `E:\MinerU\batch_convert.ps1 -TaskName "<TaskName>"`
- This script automatically routes to `E:\MinerU\Tasks\<TaskName>` and inherently handles resuming skipped files automatically.

### Python Batch Script (Alternative)
- Use `E:\MinerU\Scripts\batch_convert.py --task "<TaskName>"`
- Operates under the exact same Task folder logic.

### macOS/Linux Batch Script
- Use `scripts/batch_process_mac.sh <input_dir> <output_dir>`.

## 3. Troubleshooting & GPU Patches (Critical for Windows)

When running `magic-pdf` locally on Windows with older GPUs (like Maxwell/Quadro M4000), you may encounter runtime crashes due to hardware-software mismatches. If a run fails, ALWAYS check the task logs and apply the following patches if these specific errors occur:

1. **CUBLAS_STATUS_NOT_SUPPORTED in LayoutLMv3**:
   - *Cause*: PyTorch incorrectly returns `True` for `torch.cuda.is_bf16_supported()` on unsupported older GPUs, causing CUBLAS to crash when performing bfloat16 convolutions.
   - *Fix*: Edit `E:\MinerU\Env\lib\site-packages\magic_pdf\pdf_parse_union_core_v2.py`. Find `bf_16_support = torch.cuda.is_bf16_supported()` and hardcode it to `bf_16_support = False`.
2. **TypeError: expected Tensor as element 0 in argument 0, but got NoneType in Unimernet**:
   - *Cause*: Incompatibilities between new `transformers` cache objects (`EncoderDecoderCache`) and old MinerU extraction logic assuming simple tuple caches during Math Formula Recognition (MFR).
   - *Fix*: Edit `E:\MinerU\Env\lib\site-packages\magic_pdf\model\sub_modules\mfr\unimernet\unimernet_hf\modeling_unimernet.py`. In the `super().generate` call (around line 477), explicitly inject `use_cache=False` to bypass the cache entirely and avoid the unpack crash.
3. **Queue Interrupted (Network Disconnects)**:
   - *Fix*: If a batch queue fails midway, write a script to differentiate completion status by checking if the `.md` file exists inside the `<pdf_name>\auto\` output directory. Move unstarted and partially started PDFs (without `.md`) to a local drive and restart the queue.

## 4. Image Hosting Replacement (Imgur)

If the user requested the Imgur (图床) version, and you are using the local command line (not the API), you MUST run the provided Python script to convert local image links to Imgur links AFTER the OCR process completes:
- `python scripts/convert_local_images.py <path_to_generated_markdown_file>`
This script will parse the Markdown, upload local images to Imgur, and update the links inline.

## 5. Markdown to EPUB Conversion

To convert the generated Markdown files to EPUB format, use the Pandoc workflow:
- Execute `scripts/convert_markdown_to_epub.sh <input.md> <output.epub> [cover_image] [title]`
- This leverages `pandoc` with `--epub3` and the `pandoc-crossref` filter.

## Resources

- **`references/mineru_api_docs.md`**: Contains the full architectural overview, API endpoints, and configuration details for the Mineru Scan System and Imgur integrations.
- **`scripts/rename_books.py`**: Python script to audit and enforce the "Author - Year - Title.pdf" naming convention within a Task folder.
- **`scripts/convert_local_images.py`**: Python script for parsing a Markdown file, uploading local images to Imgur, and replacing the links.
- **`scripts/convert_markdown_to_epub.sh`**: Helper script to convert the OCR'd Markdown into EPUB using Pandoc.
- **`scripts/extract_by_paragraph.py`**: Extracts text blocks from MinerU JSON into plain text paragraph chunks for high-density, context-aware translation.
- **`scripts/merge_by_block_container.py`**: Merges translated paragraphs back into the MinerU JSON using Block-Level Container Consolidation (overwriting span fragments).
- **`scripts/generate_fxl_epub.py`**: Generates a Fixed-Layout EPUB directly from the merged JSON, utilizing native CSS text wrapping for unified block containers.

## 6. Fixed-Layout (FXL) Translation Workflow (Block-Level Consolidation)

If the user wants to translate a MinerU-processed PDF into Chinese while **strictly preserving the original layout and image positions**, use the advanced Block-Level Container Consolidation workflow:

1. **Paragraph Aggregation Extraction**: 
   Run `python scripts/extract_by_paragraph.py <input_middle.json> <output_dir>`. 
   This parses the MinerU `_middle.json` and extracts full paragraphs (`para_blocks`) into pure `.txt` files (e.g., 500 paragraphs per chunk). This reduces fragmentation overhead by 95% and provides full context for accurate translation.
2. **High-Density Line-by-Line Translation (Looping Engineer & Debate Panel)**: 
   Do NOT use external API scripts unless explicitly requested. Orchestrate IDE Sub-agents:
   - **Batch Dispatch**: Dispatch the `.txt` chunks in batches.
   - **Debate Panel QA**: Invoke a **Translator** sub-agent to translate the text files line-by-line (each line is a full paragraph).
   - **Validation**: Ensure the output Chinese `.txt` file has the exact same line count as the input file.
3. **Block-Level Container Consolidation**: 
   Run `python scripts/merge_by_block_container.py <input_middle.json> <translated_txt_dir> <output_middle_zh.json>`.
   This script reads the translated paragraphs and injects them back into the JSON. Crucially, it deletes the fragmented `lines` and `spans` inside the original `para_block`, replacing them with a single unified text container bound to the parent block's bounding box.
4. **FXL EPUB Generation (V2 Engine)**: 
   Once the JSON is merged, run `python scripts/generate_fxl_epub.py <output_middle_zh.json> <output.epub>`.
   This script utilizes native HTML/CSS word wrapping (`text-align: justify`) inside the unified block containers, entirely eliminating fragmented visual artifacts and rendering a flawless Fixed-Layout EPUB.
