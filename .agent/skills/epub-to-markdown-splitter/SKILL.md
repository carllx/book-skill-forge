---
name: epub-to-markdown-splitter
description: 将 EPUB 电子书转换为 Agent 友好的独立 Markdown 知识库。当用户要求拆分电子书、提取 EPUB 文本、或要求 Agent 读取大型 EPUB 文件以避免上下文溢出时触发。
---

# EPUB to Markdown Splitter

本技能提供了一个基于 Python 和 `uv` 执行环境的强大脚本，可以将 EPUB 电子书依据其内部的逻辑目录（TOC/NavMap）精准拆分为多个结构化的独立 Markdown 文件。

## 前置条件

1. **环境依赖**：必须在包含该技能的 Antigravity 终端中安装有 `uv`（极速 Python 包管理器）。
2. **输入文件**：用户需提供或指定一个存在的 `.epub` 文件路径。

## 核心脚本用法

该技能的核心脚本位于 `scripts/epub_splitter.py`。该脚本已包含 PEP 723 内联依赖声明，因此请务必使用 `uv run` 执行，它会自动处理依赖：

```bash
uv run .agent/skills/epub-to-markdown-splitter/scripts/epub_splitter.py -i <输入文件.epub> -o <输出目录> [--max-chars 8000] [--full]
```

### 参数说明

- `-i, --input`  (必填): 输入的 EPUB 文件绝对或相对路径。
- `-o, --output` (必填): 输出 Markdown 文件的目标目录。脚本会自动创建该目录。
- `--max-chars`  (可选): 单个 Markdown 文件的最大字符数，默认 `8000`。为防止大模型因上下文过长而导致注意力丢失，超过此长度的章节会被智能切割为多个部分（`part1`, `part2`...）。
- `--full`       (可选): 如果带有此标志，脚本在拆分输出的同时，还会额外生成一个合并全量文本的 `full.md` 文件，方便整体阅读（但需注意上下文限制）。

## 输出结构预期

执行成功后，`<输出目录>` 内应包含：

- `index.md`: **智能路由面板 (Smart Routing Panel)**。包含书籍的元数据（书名、作者）、带有缩进层级的树状目录结构，以及面向 Agent 的检索和阅读指南。
- `chapter_01_前言.md`, `chapter_02_第一章.md` ...: 按照目录和 max-chars 智能拆分的独立 Markdown 文件。
- `images/`: 若原书含有图片，将被统一提取至此文件夹，且 Markdown 文件内的引用路径会被正确重写。
- `full.md` (若使用了 `--full` 参数): 合并了所有拆分章节的全集。

## 代理执行工作流 (Agent Workflow)

当决定使用此技能满足用户拆分 EPUB 的需求时，遵循以下步骤：

1. **确认目标参数**：向用户确认或从上下文中提取出输入 `.epub` 文件的路径，以及期望的输出目录路径。询问用户是否需要附加的 `full.md`（如果尚未指明）。
2. **执行转换**：在终端中使用 `run_command` 调用上述 `uv run` 命令。
3. **验证结果**：通过 `list_dir` 或类似工具，检查输出目录中是否成功生成了 `index.md` 和带有章节序号的 `.md` 文件。
4. **汇报与后续操作**：结束任务并通知用户转换已完成。如果是为了让后续 Agent 提取书中的特定知识，**必须引导接手的 Agent 第一时间读取 `index.md` 中的检索指令 (Search Heuristics)**，再进行内容搜索或阅读。
