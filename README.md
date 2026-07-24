# 🎨 欢迎来到 BSF：无缝感应的数字艺术工坊 (Book-Skill-Forge)

亲爱的媒体艺术老师，欢迎步入这座专为您打造的**数字艺术工坊**！
在这里，我们将蕴藏在浩瀚书海中的智慧骨架与心法，淬炼成属于未来的数字艺术素材（人工智能技能）。没有晦涩的技术代码，只有自动化运作的策展空间。

---

## 🗺️ 艺术工坊展览空间全景图

```mermaid
flowchart TD
    %% Define Styles
    classDef stage fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef output fill:#e1f5fe,stroke:#0277bd,stroke-width:1px;
    classDef vault fill:#fff3e0,stroke:#e65100,stroke-width:1px;
    classDef review fill:#f3e5f5,stroke:#4a148c,stroke-width:2px;

    Book[📚 原著典籍] --> Stage(🎭 全自动无导演剧团<br/>分镜剧本库调度)
    
    subgraph Stage[🌟 多重平行宇宙舞台 (并发创作)]
        direction LR
        S1[写实素描师] --> O1[知识原石]
        S2[抽象派大师] --> O2[空间构图律动]
    end
    class Stage stage
    
    Stage --> Eval{⚖️ 无偏见脱水试金石}
    
    subgraph Eval[⚖️ 试金石与双向探照灯 (客观审计)]
        direction TB
        E1(博物馆标杆印记) -.双向探照灯.- E2(印象派神似意会)
    end
    class Eval review

    Eval -->|通过甄别| Vault[(🏛️ 永久地下珍宝库)]
    Eval -->|落选废弃| Capsule[💊 历届展出胶囊盒]

    class O1,O2 output
    class Vault vault
```

---

## 🏛️ 工坊五大核心展区与设施

### 1. 🎭 舞台与剧团：全自动无导演剧团 (The Ensembles)
- **分镜剧本库** (`.agent/workflows/`)：这是我们的后台总指挥。它负责按照您指定的配方，调度各个艺术流派登场。
- **大师专属画笔箱** (`.agent/skills/`)：存放了专门提取具象元素的“写实素描师 (Graphify)”与提炼宏大思维的“抽象派大师 (Cangjie)”。
- **多重平行宇宙舞台** (`// turbo`)：不同的艺术大师可以在相互平行的舞台上同时泼墨挥毫，互不干扰，极速产出复合流派的惊世杰作。

### 2. 🌈 光影折射的数字三棱镜 (AST Runtime 引擎)
- 我们新引入了名为 **AST 引擎 (`src/ast_engine/`)** 的精密光学仪器。当同一束光（承载着 `**[Page X]**` 等物理坐标的 Markdown 原石文本）穿透这颗三棱镜时，它能凭借内部精巧的折射镜面（Visitor 访问者模式），瞬间将其完美折射成三种交相辉映的光谱：
  - **光谱一：清晰透亮的坐标射线**，生成提取物理速查表的刻度锚点（BookToSkill）。
  - **光谱二：纯净深邃的苍颉语义流**，提炼出抽象宏大的知识架构与心法（Cangjie）。
  - **光谱三：璀璨交织的星系全息图**，投影出概念相互连接的知识图谱星系（Graphify）。

### 3. 🎨 创作与隔离：专属定格动画操作台
- **防颜料沾染隔离板** (`.agent/rules/`): **工坊戒律册**。它如同无菌罩和隔离板，确保每次创作都在专属的工作台上进行，绝不把上一位艺术家的颜料蹭到新作品上。
- **历届展出胶囊盒** (`data/evaluation_runs/`)：每一场竞演的初稿、废案与最终成片，都会被仔细封存在这里，供您随时溯源查阅。

### 4. ⚖️ 鉴定与审计：无偏见脱水试金石
这是我们最引以为傲的鉴定中心。摒弃了“主观凭感觉打分”，一切只依靠确凿的证据：
- **博物馆标杆印记 (Anchor KIs)**：作为核验真伪的黄金参照物。
- **双向探照灯寻踪 (Bi-directional Mapping)**：一盏灯照向创作产物，一盏灯照向原著。只有两灯光束交汇照亮同一段落时，才算有效提取。
- **印象派神似意会 (Semantic Soft-Mapping)**：对于高级艺术抽象心法，我们绝不死板核对字面。只要意境、神韵与原著同频，试金石即可亮起绿灯。

### 5. 🏛️ 收藏与传承：永久地下珍宝库
- 经过试金石淬炼后的**知识原石 (Atomic KIs)** 与 **空间构图律动 (Strategy KIs)**，最终将被存入 `~/.gemini/antigravity/knowledge/`，化作永不褪色的数字素材库，为您的下一次策展提供无尽灵感。

---

> [!TIP]
> **🎨 艺术老师极简导览速查卡**
> - **启动策展**：在系统主控台输入 `/run-eval`，系统会主动为您推荐今日的舞台配方供您挑选。
> - **人机共创**：当创作质量不佳或需要同步远端画笔时，系统会亮起红灯并弹出提示卡（**Proceed**），等待您的最终艺术裁定，绝不私自越权涂改！
