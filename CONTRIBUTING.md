# 🤝 Contributing to Book-Skill-Forge (BSF)

欢迎加入这座“无缝感应的数字艺术工坊”！在提交 PR 或 Issue 前，请仔细阅读以下贡献守则。我们采取严格的“单一数据源 (SSOT)”与“双轨制规则”，以保持工坊纯粹的艺术张力与脱水评测红线。

## 1. 提交新代码与新配方的红线
任何核心逻辑与评测引擎的改动，**必须绝对服从脱水计分信仰**。
- 绝不允许通过 Python 调用 LLM 来绕过评测逻辑进行主观打分。
- 所有评测输出必须落实在 `matches.json` 布尔矩阵上。
- **详见**：[V6 核心目录规范](docs/ARCHITECTURE.md) 与 [脱水计分红线](docs/EVALUATION_GUIDELINE.md)。

## 2. 参与双轨制文档重塑
我们为本项目设定了**双轨制交互视角 (Dual-Track Persona)**：
- 向技术人员传递逻辑时，使用严谨的软件工程术语。
- 向项目的主控群体（媒体艺术老师）传达更新时，必须在 `README.md` 中使用感性的“艺术工坊”隐喻。
- 请在提交大型 Feature PR 时，同步更新对应的底层 Markdown 协议以及 `README.md` 展厅，切勿产生孤儿文档！

## 3. Pull Request 流程
1. **Fork 本仓库** 并创建您的特性分支 (`git checkout -b feature/AmazingFeature`)。
2. 确保在本地进行了相应的沙盒隔离测试 (`data/evaluation_runs/`)。
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)。
4. 推送到分支 (`git push origin feature/AmazingFeature`)。
5. 打开一个 Pull Request，并清楚地阐述您的艺术理念与算法实现。
