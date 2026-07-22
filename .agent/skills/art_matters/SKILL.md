---
name: art_matters
description: Provide comprehensive workflows and heuristics derived from art_matters. Use when executing domain-specific tasks, evaluating patterns, or needing deep structural checklists.
---

# art_matters Workflows & Guides

This skill provides a structured, progressive disclosure architecture. 
Please route to the specific workflow below based on your current goal.

## Quick Start
如果你是第一次调用此技能，或者不知道该用哪个具体的工作流，请仔细梳理你的目标，然后查阅下面的核心工作流：

## Core Workflows (工作流体系)

- **Art Matters**
  ➡️ [Art Matters Guide](references/workflows/art_matters_ctheory.md)


## 渐进式知识检索 (Progressive Knowledge Retrieval)

> [!WARNING]  
> 原书核心概念已编译为高密度的知识图谱。**切勿使用 `view_file` 或 `read_file` 等工具尝试读取原始的大型文本块**，否则会导致严重的上下文溢出（Context Bloat）与截断。本技能严格遵循渐进式披露（Progressive Disclosure）原则。

当你在工作流中遇到未知的专属术语，或需要深挖某个模式的理论依据时，请强制使用 `graphify-mcp` MCP server 提供的 `graphify_query` 工具。

1. **深度理论推演 (Deep Theory Query)** (首选)：
   当你需要理解 "Why" 或更深层次的理论推演时使用。请调用 `graphify_query` MCP 工具，并将 `query` 参数设置为你的问题（例如："为什么我们需要采用这种设计模式？"），`graph` 参数指向当前 skill 目录下的 `graphify-out/graph.json` 的绝对路径。该工具内置 Token 限制，避免上下文爆炸。

2. **Fallback (无 MCP 时)**：
   如果因为环境限制无法使用 MCP 工具，请运行生成的 `scripts/query_graph_fallback.py` 脚本来查询 `graphify-out/graph.json`：
   `python scripts/query_graph_fallback.py graphify-out/graph.json "<你的查询>"`

3. **用户引导**：当你需要用户确认深奥的设计概念时，请建议用户在交互中直接提问，由你代为通过 MCP 工具检索，或者建议用户输入 `/graphify query "<在此处替换你的概念>"`。
