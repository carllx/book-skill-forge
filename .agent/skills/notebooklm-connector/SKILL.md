---
name: notebooklm-connector
description: Connects to and interacts with Google NotebookLM via the local `notebooklm-py` CLI.
---

# NotebookLM Connector Skill

## 1. 技能说明
本技能用于指导 Agent 如何调用本地的 `notebooklm-py` 命令行工具，实现与 Google NotebookLM 云端笔记本的无缝交互。
主要场景包括：列出笔记本资源、查询特定文档状态、以及基于笔记本内容发起对话（RAG 检索）。

## 2. 身份验证与上下文
- CLI 工具名: `notebooklm`
- 鉴权信息: 用户已在本地完成登录，无需您操心 Cookie。
- 目标笔记本名称: `造物与创格`
- 目标笔记本 ID: `c7f9c10a-10db-454d-ab7a-ba307cb4612d`

## 3. 核心命令范例
使用 `run_command` 工具执行以下命令：

### 获取帮助
```bash
notebooklm --help
notebooklm chat --help
```

### 列出资源
列出“造物与创格”笔记本中目前加载的所有书籍资源：
```bash
notebooklm source list -n c7f9c10a-10db-454d-ab7a-ba307cb4612d
```

### 发起对话 (RAG 检索)
直接向该笔记本发起提问，获取 AI 基于库中书籍生成的回答。
*注意：遇到长文本输出，建议先重定向到临时文件再读取。*

**全局检索（查询所有书籍）:**
```bash
notebooklm ask "在这里输入你想问的关于书籍或艺术的问题" -n c7f9c10a-10db-454d-ab7a-ba307cb4612d
```

**限定单本/特定书籍检索（推荐在擂台赛中使用）:**
使用 `-s` 或 `--source` 参数，并跟上前面 `source list` 命令获取到的资源 ID，可以将检索范围严格限定在指定的图书中：
```bash
notebooklm ask -s 49dbfd25-1ce5-4e47-93eb-1da130eab3e4 "基于建构文化理论分析某物..." -n c7f9c10a-10db-454d-ab7a-ba307cb4612d
```

## 4. 最佳实践
- 提问时尽可能指明对应的书籍名称（如：“根据《建构文化研究》的观点……”），以提高 NotebookLM 的检索命中率。
- NotebookLM 可能会以 Markdown 格式返回带引用的文本，请直接提取并原汁原味地展示。
