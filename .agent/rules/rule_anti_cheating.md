---
description: 强制从内容中分离线索以防 LLM 抄袭，禁止 prompt 中带入标准答案。
globs:
  - "data/evaluation_runs/**"
  - "src/**/*.py"
  - ".agent/workflows/**/*.md"
---

# 规则：反作弊纪律 (Anti-Cheating)

## 1. 核心红线
绝不允许在 Prompt 中将标准答案（Ground Truth/Anchor KIs）与原文本混合，诱导 LLM 产生匹配错觉。所有的上下文线索（Breadcrumbs）与待测内容必须严格隔离。

关于如何执行客观双向映射，请严格遵循 [评测标准与 SOP 手册](../../docs/EVALUATION_GUIDELINE.md#2-脱水计分红线与双向证据映射-ssot)。
