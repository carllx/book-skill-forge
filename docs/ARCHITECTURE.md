# Book-Skill-Forge (BSF) 架构指南

## 1. 项目定位与 V6 升级概览
Book-Skill-Forge (BSF) 现已全面升级至 **V6 Native IDE Architecture**。
所有的逻辑调度、规则校验和技能执行，全部下沉至 Antigravity IDE 原生扩展体系。系统通过解耦的 `.agent/` 目录集完成多模态、多相复合管线（Multi-phase Composite Pipeline）的运行，极大降低了传统 Python 胶水代码的维护成本。

## 2. 核心目录规范 (V6 Native)
本节为 V6 目录结构的**单一事实来源 (SSOT)**，严禁在其他文档重复解释。
- **`src/ast_engine/`**: 基于 `markdown-it-py` 的 AST Runtime 引擎。采用访问者模式（包含 `BookToSkillVisitor`、`CangjieVisitor`、`GraphifyVisitor` 等），精准解析带有物理页码（如 `**[Page X]**`）的单文件 Markdown，实现结构化语义流的分离解析。
- **`.agent/rules/`**: 沙盒隔离防线与反作弊约束规则库。强制锁定每个任务的访问边界。
- **`.agent/workflows/`**: 声明式 LLM 驱动工作流目录，采用 `// turbo` 语法驱动并行和串行流水线，如 BSF 的主控调度器。
- **`.agent/skills/`**: 存放所有按需懒加载 (Lazy Loading) 的专职智能体技能，包含：
  - `graphify-agent`: 提取微观实体。
  - `cangjie-agent`: 提炼宏观心法。
  - `judge-agent`: 负责双向盲测映射 (Dual-blind Mapping) 的语义审计员。
- **`data/evaluation_runs/`**: 严格的动态分配 I/O 沙盒，杜绝高并发写的踩踏碰撞。通过变量注入工作流。
- **`~/.gemini/antigravity/knowledge/`**: 全局知识持久化核心。
  - **Atomic KIs**: Graphify 产出的微观实体知识点。
  - **Strategy KIs**: Cangjie 产出的宏观框架心法。
  - **Anchor KIs**: 评测使用的 Ground Truth 锚点。

## 3. 架构模式：Native Subagent-Driven Execution
不再使用 Python 介入调度。所有的路由分发、大乱斗对决，由 `.agent/workflows/` 原生驱动。
- **复合多相测试**：支持 Graphify 与 Cangjie 的懒加载与组合。
- **全局消解与存储**：所有 Worker 生成的片段直接入库 `~/.gemini/antigravity/knowledge/` 作为 KI，后续操作通过原生命令提取、去重、融合，无需外挂复杂 Python 聚类算法。
- **Arena Battle Royale (大乱斗)**：利用 `// turbo` 并发执行纯图谱流、纯心法流和复合管线流，各自在 `data/evaluation_runs/` 内拥有独立沙盒，绝不互扰。

## 4. 沙盒与防踩踏引擎
本节为沙盒机制的 **SSOT**，具体的规则执行代码遵循 [沙盒隔离规则](../.agent/rules/rule_sandbox_isolation.md)。
- 每次触发流水线，通过 Rule 强制生成诸如 `data/evaluation_runs/run_<id>/` 的沙盒，并剥夺在其余目录的写权限。
- Judge Agent 生成的评价报告 (`matches.json`) 被强制写入专属沙盒，最后再基于沙盒内文件做算分处理。

## 5. 评测引擎钩子
关于具体的脱水评测红线、双向证据映射以及 Judge Agent 的审计纪律，请移步至唯一的权威评测手册：[评测标准与 SOP 手册](EVALUATION_GUIDELINE.md#2-脱水计分红线与双向证据映射-ssot)。
