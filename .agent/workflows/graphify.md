---
description: 执行 Graphify 图谱化提取管线
permissions:
  - restricted_paths: ["**/*"]
---

# Graphify Workflow

## 前置条件
- 目标路径存在，且安装了相应的提取工具

## 步骤
1. 解析用户传入的参数（路径、URL 或模式）
2. 遵循 `.agents/skills/graphify/SKILL.md` 中定义的转换管线进行处理
// turbo
3. 在 `graphify-out/` 目录中输出知识图谱结果
