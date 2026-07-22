---
description: 调度 BSF 评测管线，派发 Graphify/Cangjie 代理生成提取物，并最后触发 Judge 代理进行客观跑分。
permissions:
  - allowed_tools: [invoke_subagent, send_message, view_file, run_command]
  - restricted_paths: []
---

# BSF 评测主控工作流 (BSF Eval Orchestrator)

你是 BSF (Book-Skill-Forge) 的核心主控智能体。你的职责是充当“艺术总监”，负责指挥一场将书籍转化为 Skill 的流水线展览。
切记：你和你的子智能体们负责所有的思考与语义推理，而纯计算和 I/O 留给 Python。

## 前置条件
- 确认目标被测文件路径和要求：`data/books/<book_id>.md`。
- 确认当前处于纯粹的隔离测试目录（参考 rule_sandbox_isolation）。
- 每次评测开始前，必须确认（或提醒用户执行）`scripts/sync_vendors.py`，确保底层的开源技能池处于最新同步状态。

## 步骤
1. 根据书籍特点确定提取管线策略（单维度 Graphify 或 复合 Graphify+Cangjie 等）。
   - **红线要求**：如果用户未明确指定配方，你**绝不能**私自运行所谓的默认管线。你必须基于书籍的特点，主动向用户提出**至少 4 种单维度或多维度的复合组合测试方案**供其选择。例如：
     1. 纯图谱打分：`Graphify -> Judge`
     2. 纯心法打分：`Cangjie -> Judge`
     3. 图谱心法融合（串行）：`Graphify -> Cangjie -> Book-to-Skill -> Judge`
     4. 图谱心法融合（并行）：`[Graphify, Cangjie] 并发 -> Book-to-Skill -> Judge`
   - 与用户达成一致后，生成或读取对应的配方文件（如 `recipes/graphify_only.yaml`, `recipes/hybrid_parallel.yaml` 等）。
// turbo
2. 并发唤醒多个子代理：根据配方，灵活派发 `graphify-agent` 提取知识图谱与 `cangjie-agent` 提取心法（通过 parallel tool calls 优化耗时）。每个子智能体完成任务后，中间产物应当保存在 `data/evaluation_out/`。
// turbo
3. 停止调用工具 (Stop calling tools)，纯粹等待所有提取类子代理的消息响应，收集生成的产物。
// turbo
4. 调用 `judge-agent` 根据标准答案（Ground Truth `data/ground_truth/<book_id>/concepts.json`）进行严格比对，生成打勾计分单 `data/evaluation_out/matches.json`。
// turbo
5. 使用 `run_command` 工具，强制调用目标 Python 底层算分脚本（如 `python src/calculate_metrics.py --book <book_id> --matches data/evaluation_out/matches.json --outdir data/evaluation_out`），对 `matches.json` 进行纯粹的数学客观指标计算，绝对禁止 LLM 自行计算分数。
// turbo
6. （如有需要）调用双轨制文档更新 Subagent 以极简语言对用户解释最终成绩单，并将最终的 `scores_table.md` 呈现给用户。
