---
description: 测试任务的读写操作必须严格隔离在动态沙盒目录中，防止读写踩踏。
globs:
  - "data/evaluation_runs/**"
  - "src/**/*.py"
  - ".agent/workflows/**/*.md"
---

# 规则：沙盒隔离原则 (Sandbox Isolation)

## 1. 核心红线
测试任务在启动时必须分配动态唯一的运行标识（run_id），所有的输出结果（如日志、评测报告、中间产物、`matches.json`）必须写入 `data/evaluation_runs/<run_id>/` 目录。

- ❌ 禁止写死固定的全局输出路径（如根目录下的 `matches.json`）。
- ❌ 禁止不同测试任务实例共享临时文件。
- ❌ 测试运行期间，严禁向 `.agent/`、`docs/` 或根目录越权写入任何文件。

关于沙盒在整体架构中的定位，请参见 [V6 核心目录规范](../../docs/ARCHITECTURE.md#4-沙盒与防踩踏引擎)。
