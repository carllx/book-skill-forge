---
name: textbook-to-skill-converter
description: 一套高度灵活的教材转技能 (Textbook-to-Skill) 转换工具集。赋能 Agent 根据具体输入源的形态（单文件、预分块目录等），自主编排归一化、图谱构建、工作流提取及测试流程，将复杂知识库转化为遵循渐进式披露原则的智能 Skill。
---

# Textbook-to-Skill Converter (Meta-Skill)

本技能秉持**“高内聚、低耦合”**与**“赋能而非限制”**的设计理念。以下提供的四个阶段（Phases）是底层的能力模块，**你不必死板地按线性流程执行**。作为主控 Agent，你应该根据输入源的实际形态（例如：是未经处理的单一 PDF 还是已经切分好的高质量 Markdown 目录）以及任务规模，**灵活且开放地裁量、组合甚至跳过特定模块**，以最大化通用性与效率。

对于超大体量的书籍，建议搭配 `/goal` 指令长线运行并充分利用子代理 (Subagents) 进行 Map-Reduce 并发操作。

## Capability Modules (核心能力模块库)

你可以根据当前上下文灵活调用以下模块来组装转换流水线：

### 🔧 模块 1: Ingestion & Denoising (多态自适应归一化与切片)
**用途**：将异构格式统一处理为高质量的 Markdown 切片集群。
**灵活运用提示**：此模块内置形态探针。如果你传入的是自带组织结构的“文件夹”，它会自动开启 `Passthrough` 直通模式，保护原有生态；如果传入单文件，它会基于语义进行深度拆片。你可以只取所需。
* **数据摄取与探测**：`python scripts/ingestion_pipeline.py <目标教材路径/目录> <IR缓存目录>`
* **物理切片生成**：`python scripts/chunking_engine.py <IR缓存目录> <临时切片存放目录>`

### 🕸️ 模块 2: Enhanced Graphify Extraction (零 API 图谱构建)
**用途**：保留教材原始的逻辑拓扑结构，避免大语言模型在总结时过度压缩深度理论。
**灵活运用提示 (Agent-Driven 架构)**：为了彻底解决无 API Key 时无法提取图谱的痛点，此模块已重构为“本地提取 + 无头聚类”模式。你（主控 Agent）只需执行本地 Python 脚本，即可极速完成数百切片的 AST（语法树）提取。
* **第一步：本地极速 AST 图谱提取**：`python scripts/local_graph_extractor.py <切片源目录> <输出文件/graph.json>`
* **第二步：无头聚类 (社区发现)**：在图谱所在目录下执行 `graphify cluster-only . --no-label` 完成网络降维，无需任何 LLM 或 API Key。

### 🧠 模块 3: Dynamic Triage & Assembly (基于渐进式披露的合成与路由)
**用途**：提取网络中的“可操作知识”生成独立的工作流指南，将“深层理论”封装为后置查询脚本，生成最终的 Skill。
**灵活运用提示 (Agent-Driven 架构)**：此模块已升级为**纯本地、零 API Key 依赖**的子代理协同模式。Python 脚本仅负责生成任务队列 (`.agent_tasks/synthesis_tasks.json`)，随后你需要作为主控 Agent 读取队列，并使用 `invoke_subagent` 派遣多个子代理并发完成 markdown 编写。
* **第一步：生成合成队列**：`python scripts/triage_router.py <最终合并_graph.json> <输出_Skill_目标目录> [可选:源切片目录]`
* **第二步：指派 Subagents 执行合成**：主控 Agent 需读取生成的 JSON 队列，并将合并任务分配给子代理执行，覆盖占位符并完成最终工作流文件。

### ⚖️ 模块 4: QA Verification (多智能体协同质检与反馈闭环)
**用途**：严格检验转换成果的健壮性，确保无知识遗漏并强制落实渐进式披露。
**灵活运用提示 (Agent-Driven 架构)**：此模块同样移除了对外部 API 的依赖。脚本会生成测试用例并下发任务队列 (`.agent_tasks/qa_tasks.json`)。你（主控 Agent）需调度 QA 子代理来执行实际的盲测比对。
* **第一步：生成质检队列**：`python scripts/multi_agent_qa.py <最终合并_graph.json> <输出_Skill_目标目录> <源切片目录>`
* **第二步：指派 QA Subagents 盲测**：主控 Agent 读取 JSON 队列，派遣子代理执行 Graph QA 与 Script QA。如果发现缺陷，由主控 Agent 直接调用对应社区的重试逻辑修复问题。
* **(向下兼容) 基础数据覆盖率校验**：`python scripts/quantitative_qa.py <最终合并_graph.json> <输出_Skill_目标目录>`
* **自主 AI 盲测指南**：参考 [references/quiz_judge_prompt.md](references/quiz_judge_prompt.md) 生成实战问题，检验新生成 Skill 的鲁棒性。
