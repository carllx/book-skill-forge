---
description: 所有的评测指标计算，必须纯粹依赖于 Python 脚本对布尔矩阵的算术计算。
globs:
  - "data/evaluation_runs/**"
  - "src/**/*.py"
  - ".agent/skills/judge-agent/**"
---

# 规则：客观计分纪律 (Objective Scoring)

## 1. 核心红线
- ❌ 禁止在任何 Python 脚本中调用 LLM 接口来让其给出 "0-100" 的定性分数。
- ❌ Judge Agent 只能作为输出 True/False 布尔矩阵的审计员，最终成绩由 Python 算数生成。

关于具体的打分公式和语义容错边界，请严格遵循 [评测标准与 SOP 手册](../../docs/EVALUATION_GUIDELINE.md#2-脱水计分红线与双向证据映射-ssot)。
