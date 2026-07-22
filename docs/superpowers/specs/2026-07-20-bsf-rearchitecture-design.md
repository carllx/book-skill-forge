# BSF 纯智能体架构重构设计规范 (Design Spec)
日期: 2026-07-20

> [!NOTE] 
> **历史归档 (Historical Spec)**: 本文档为早期 (2026-07-20) 架构设计草案，现已由 [V6 Native 架构指南](../../ARCHITECTURE.md) 全面替代。其中涉及的 `data/evaluation_out/` 等旧路径规范已作废，请以 V6 指南为准。

## 1. 核心概述
Book-Skill-Forge (BSF) 项目正在全面转向**纯智能体驱动 (Pure Agentic-Driven)** 架构。该架构的目的是为了更好地评估和整合多种开源提取框架（如 Graphify、Cangjie、Book-to-Skill）。
核心红线：Python 代码严格限制在纯粹的数据搬运（I/O）和简单的数学计算；所有涉及语义理解、信息抽取和主观评判的任务，全权交由子智能体（Subagents）完成。

## 2. 核心架构角色划分
- **艺术总监 (Orchestrator)**：一个中央主控智能体（`bsf-eval-orchestrator`），负责根据配方调度整个工作流。
- **专职艺术家 (Subagents)**：
  - **Graphify Agent（解剖学画师）**：负责提取结构化的知识图谱，并输出 `graph.json`。
  - **Cangjie Agent（抽象派大师）**：负责蒸馏书籍中的抽象心法和思维模型。
  - **Book-to-Skill Agent（策展人）**：将提取出的各个组件完美拼装，生成最终可用的 `SKILL.md`。
- **Python 的“苦力”职责**：只允许负责打开和保存文件、利用 Pydantic 等工具进行 JSON 结构校验，以及进行最后的算数打分。绝不允许在 Python 脚本中直接发送 LLM API 请求。

## 3. 策展配方薄：灵活的调度配置
为了让 BSF 成为一个名副其实的“策展实验室”，能够对不同的框架进行跑分对比，以及测试各种融合技术，我们的总监将由一本**“策展配方薄 (Config File)”**驱动。
- **配置文件格式**：推荐使用 YAML 或 JSON。
- **工作机制**：配方薄中定义了子智能体的出场顺序（例如：`[Graphify, Cangjie]`）。这意味着未来我们如果想引入一个新的开源框架，只需要写一张新配方，而完全不需要修改总监（Orchestrator）的代码逻辑。

## 4. 评测打分引擎的解耦
为了客观公正地给生成的 Skill 打分，我们将“裁判”与“计分板”彻底拆分：
- **满分范本 (Ground Truth)**：采用严谨的 JSON 模板（`concepts.json`），明确列出必须提炼的核心方法论及其重要性权重。
- **艺术评论家 (Judge Subagent)**：这是负责阅读和对比的智能体。他会对比我们生成的 Skill 和满分范本，出具一份纯粹的布尔值（True/False）打勾清单单，即 `matches.json`。
- **计分器 (Python)**：Python 脚本读取 `matches.json`，并做以下死板的数学运算：
  - **知识召回率 (Knowledge Recall)**：匹配成功的概念权重总和 ÷ 标准答案中的概念权重总和。
  - **去重准确率 (Dedup Precision)**：提取出的有效且不重复的概念数量 ÷ 总提取的概念数量。
  - **伪影可用性 (Artifact Usability)**：根据评论家给出的排版、逻辑等主观分数，进行加权平均。

## 5. 整体数据流水线 (Data Flow)
1. **源头备料**：Python 脚本将清洗后的纯 Markdown 文件存入 `data/books/`。
2. **流水线生产**：Python 加载文本 -> 艺术总监读取“配方薄” -> 唤醒对应的专职艺术家进行提取 -> 生成的中间产物统一保存在 `data/evaluation_out/`。
3. **评委打分**：评论家（Judge Agent）拿着生成的作品与 `data/ground_truth/concepts.json` 逐一核对 -> 填写并输出 `matches.json`。
4. **成绩出榜**：Python 拿到 `matches.json`，算出各项指标 -> 输出最终的 `scores_table.md` 成绩单。

## 6. 开源项目同步机制 (Vendor Synchronization)
作为集成测试实验室，我们需要时刻保持各种开源框架（Graphify, Cangjie 等）与上游的同步，以测试它们在最新版本下的表现。
- **依赖隔离目录**：所有的外部开源框架将被统一拉取并放置在 `lib/vendors/` 目录下。
- **一键更新脚本**：将提供专门的同步脚本（如 `scripts/sync_vendors.py`）。在每次评测或实验开始前，总监（用户或自动化系统）可以运行该脚本一键拉取所有开源组件的最新代码更新。
