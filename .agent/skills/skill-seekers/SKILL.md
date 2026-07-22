---
name: skill-seekers
description: 专门用于抓取和抽取优质框架、思维模型、原则及反模式的 Web 爬虫能力包。作为 Agent 包装器，它指导 LLM 如何调用位于 lib/writing-great-skills-framework-scraper 下的原生 Python 环境来执行具体的数据采集。
---

# Skill Seekers (Agent Wrapper)

该技能是一个轻量级的 Agent 包装器，实际的重逻辑位于原生的 Python 爬虫项目中。

## 运行机制 (Agent 指令)

当用户要求使用爬虫抓取技能框架时，作为 AI 代理，你应当：

1. **定位代码**：工作目录为 `lib/writing-great-skills-framework-scraper`。
2. **环境准备**：确认 Python/uv 环境可用（如果有必要，运行 `uv sync` 或 `pip install -r requirements.txt`）。
3. **执行抓取**：调用该目录下的相关 Python 脚本（通常位于 `src/` 或根目录下），根据用户的 URL 或需求传入合适的参数。
4. **处理输出**：读取爬虫抓取后输出的文件，并将结果反馈给用户，或者将其作为 `book-to-skill` 的输入源之一。

> [!TIP]
> 永远不要在这个 Markdown 里面写复杂的脚本，保持“重逻辑用 Python，交互层用 Agent”的隔离原则。
