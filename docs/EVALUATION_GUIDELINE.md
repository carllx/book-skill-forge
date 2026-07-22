# 评测标准与 SOP 手册 (Evaluation SOP & Methodology)

## 1. 评测目标与 Ground Truth
BSF 评测体系的核心目标是验证选手生成的结构化知识是否在深度和精度上战胜基准线。
- 测试前必须建立 Ground Truth，即 **Anchor KIs**。关于 KIs 的存储与架构定义，请[参见 V6 核心目录规范](ARCHITECTURE.md#2-核心目录规范-v6-native)。

## 2. 脱水计分红线与双向证据映射 (SSOT)
本节为计分与映射的绝对标准，严禁在其他规则中复制粘贴。

### 2.1 Judge Agent 的审计员职责 (True/False 矩阵)
Judge Agent **绝不输出定性分值 (0-100)**。其唯一职责是执行**双向证据映射 (Bi-directional Mapping)**：
验证选手提取的 KI 是否能命中 Anchor KIs 中的原文证据。输出结果必须为严格的 True/False 布尔矩阵（记录于 `<run_id>/matches.json`）。

### 2.2 语义等价容错 (Semantic Soft-Mapping)
针对艺术与哲学等人文学科，死板的“字面找词”会扼杀抽象心法。
**容错准则**：只要 Judge Agent 认为其隐喻、同义词替换在语境上与原文核心段落高度一致，即在 `matches.json` 中记为 True（命中）。这不是主观打分，而是基于语义容忍度的客观审计。

### 2.3 底层 Python 算术红线
最终的脱水成绩（知识召回率、去重准确率、伪影可用性等），**必须且只能由底层 Python 脚本**读取 `matches.json` 进行纯算数计算得出。

## 3. 标准评测 SOP (人机交互控制流)
评测全流程必须严格遵守以下执行流与门禁（HCI Guardrails）：

1. **入口配置**：触发评测前，若用户未携带参数，系统**必须挂起**，向用户推荐评测管线选项，等待用户确认 (Proceed)。
2. **环境检查**：检查 `scripts/sync_vendors.py`，若需同步，**必须向用户申请权限**后执行。
3. **隔离沙盒执行**：Worker Agent 开始并发提取。所有文件读写必须遵守 [沙盒隔离规则](../.agent/rules/rule_sandbox_isolation.md)。
4. **质量门禁与重试**：
   - 提取完成后，Python 脚本进行公式结算。
   - 若可用性得分低于 80%，Agent 可自主调整 Prompt 并重试。
   - **自动重试上限为 2 次**。若仍失败，必须立即上报人工请求干预。
5. **战报终审与入库**：
   - Judge Agent 生成布尔矩阵并输出成绩至战报。
   - 战报末尾必须展示“终审裁定卡”，系统**挂起等待人类艺术总监的最终裁定意见**。
   - 人类批准后，才可将沙盒内的提取产物提升写入全局持久化知识库。
