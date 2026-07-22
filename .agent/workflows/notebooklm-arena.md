# NotebookLM Arena Battle Royale Workflow (沙盒级大乱斗主控)

## 目标
执行 BSF 3.0 的终极评测：以“脱水客观、沙盒隔离、极简输出”为准则的多管线大乱斗。

## 执行步骤 (Looping Engineer 模式)

### 阶段 0：创建隔离沙盒 (Sandbox Initialization)
1. 每次启动前，必须在 `data/evaluation_runs/` 下生成当前对局的专属沙盒（如 `run_<book>_<timestamp>/`）。
2. 本次对局的所有通信日志、选手输出、裁判打分表，**必须全部落盘于此沙盒内**。

### 阶段 1：挑战者与基准派发 (Challengers Dispatch)
- **获取 Baseline**: 使用 `notebooklm ask -s <source_id>`，提示词附加【极简协议】。
- **派发挑战者**: 唤起纯图谱、纯心法、以及 **卫冕冠军(Hybrid)** 的 Subagent。
- **【极简输出协议死命令】**：在派发所有选手（包括查询 NotebookLM）时，必须附加以下命令：“字数限制 150 字，仅输出最高度浓缩的骨架点（3个核心实体+2条深度心法），强制使用 Bullet Points，严禁任何废话，违规直接零分。”

### 阶段 2：证据审计 (Evidence Auditing)
1. 收集齐所有沙盒极简答卷后，唤醒 **Judge Agent (证据审计员)**。
2. 裁判不再进行主观量化打分。它的任务是：扫描选手的骨架点，在带面包屑的原书数据中寻找**“证据锚点”**。
3. 裁判在沙盒中输出纯布尔值的 `matches.json` (记录是否命中证据)。

### 阶段 3：脱水算分与人工裁定
1. 调用底层 Python 脚本读取 `matches.json`，算出真实的脱水成绩。
2. 聚合所有的极简骨架答卷、脱水得分，生成排版极其紧凑的战报 `ARENA_ROYALE_REPORT_XXX.md`。
3. 必须在战报最末尾保留一块高度显眼的 **👨‍🎨 艺术总监（用户）人工最终裁定区**，供人类总监在秒级阅读后做出终审！
