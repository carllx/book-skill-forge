---
name: visual-display-skill
description: "Applies principles from Tufte's The Visual Display of Quantitative Information to design, evaluate, or critique data graphics."
---

# The Visual Display of Quantitative Information (Edward Tufte)

## 触发条件 (Trigger Conditions)
- 当用户要求评估、优化或设计数据可视化图表 (Data Graphics) 时。
- 当图表显得混乱、难以理解，或者用户怀疑图表存在误导性 (Graphical Distortion) 时。
- 当需要在有限空间内展示高密度或多维度数据时。

## 心法原则 (Mental Models & Principles)
1. **Graphical Excellence (图形卓越)**: 
   - 将复杂的数据以最清晰、精确和高效的方式传达。
   - 优秀的图形能在最短的时间、最小的空间内，用最少的墨水为观众提供最多的思想。
2. **Graphical Integrity & Lie Factor (图形完整性与谎言因子)**: 
   - 数据变化与图形变化的比例 (Lie Factor) 必须接近 1.0。严禁在图表中夸大数据的波动。
   - 展示数据的变动 (Data Variation)，而不是设计的变动 (Design Variation)。
3. **Data-Ink Ratio (数据墨水比)**: 
   - 墨水应尽可能多地用于展示非冗余的数据。
   - 消除 Chartjunk (图表垃圾，如无意义的网格线、视觉抖动底纹或过度修饰的“鸭子”装饰)。
4. **Data Density & Small Multiples (数据密度与小多图)**: 
   - 提高单位面积内的数据点密度。
   - 使用 Small Multiples（相同坐标轴的小型并排图表）来比较多个变量或时间序列，鼓励观众的眼睛比较不同部分的数据。

## 执行 Checklist (Execution Checklist)
- [ ] **审查谎言因子 (Lie Factor)**: 测量图形中展示的效应大小，并与数据实际的效应大小对比。是否存在通过 3D 面积或不规范缩放夸大的情况？
- [ ] **消除图表垃圾 (Erase Chartjunk)**: 图形中是否有多余的 3D 效果、无用的网格线或过度装饰？如果有，立刻移除。
- [ ] **最大化数据墨水比 (Maximize Data-Ink)**: 是否有非数据墨水可以被删除？是否有冗余的数据墨水可以被删除？
- [ ] **增加数据维度与上下文 (Provide Context)**: 图表是否断章取义？是否需要引入更多数据点来建立对比基准（如历史数据、对比组）？
- [ ] **考虑小多图 (Small Multiples)**: 对于包含过多重叠信息的复杂图表，是否能拆解为结构一致的小多图排列？
- [ ] **整合文本与图形 (Integrate Text and Graphic)**: 是否已在图形本身提供详尽的标注、数据说明和重要事件标记，而不是让观众在图文之间来回跳跃？
