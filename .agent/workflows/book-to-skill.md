---
description: 将图书或文档转换为结构化的 Agent Skill
permissions:
  - restricted_paths: ["**/*"]
---

# Book-to-Skill Workflow

## 前置条件
- 目标文档存在（支持 PDF, EPUB, DOCX 等）

## 步骤
1. 解析用户传入的文档路径参数
2. 遵循 `.agent/skills/book-to-skill/SKILL.md` 中定义的转换管线进行处理
// turbo
3. 输出结构化的技能文档和相关资源
