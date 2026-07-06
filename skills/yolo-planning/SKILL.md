---
name: yolo-planning
description: >
  YOLO 目标检测项目的实现计划生成。接收设计文档，生成带 TDD 规约的执行计划。
  由 yolo-brainstorming 交接触发，或用户直接指定"规划"。
---

# YOLO Planning — 计划生成

接收明确需求，生成经过审查的实现计划文档。

## 触发条件

- `yolo-brainstorming` 交接后
- 用户直接提供明确需求并说"规划"
- 用户指定对已有设计文档生成计划

## 流程

```
Phase 1: 读取设计文档
Phase 2: 自动检测（工程信息）
Phase 3: 研究（相关代码 + 子技能浅读）
Phase 4a: Write 骨架文件（< 100 行）
Phase 4b: 并行派发 plan-writer 填充 task
Phase 4c: 验证占位符已替换
Phase 5: 闸门检查
Phase 6: plan-reviewer 对抗审查
Phase 7: 呈现用户确认
Phase 8: 交接 yolo-executing
```

---

## Phase 1: 读取设计文档

提取：类型、必须有/没有、验收标准、影响范围、关键决策、环境事实。

---

## Phase 2: 自动检测

| 检测项 | 方式 |
|--------|------|
| Python 版本 | `python --version` |
| Ultralytics | `pip show ultralytics` |
| GPU | `nvidia-smi` |
| 数据集 | `ls dataset/` / `cat data.yaml` |
| 已有模型 | `find . -name "*.pt" -o -name "*.onnx"` |
| 导出工具 | `pip list \| grep -E "onnx\|tensorrt\|openvino"` |

---

## Phase 3: 研究

读取将要修改的文件，理解现有接口。按设计文档的领域路由读取对应子技能 SKILL.md。

---

## Phase 4: 生成计划

### Phase 4a: Write 骨架

保存到 `docs/plans/YYYY-MM-DD-<name>.md`

骨架包含：元信息、约束、文件结构、task 列表（仅标题+意图+占位符）

### Phase 4b: 并行派发 plan-writer

每个 `<!-- TASK-N-PLACEHOLDER -->` 派发一个 plan-writer 子代理填充完整规约。

### Phase 4c: 验证

```bash
grep -c '<!-- TASK-.*-PLACEHOLDER -->' docs/plans/<filename>.md
# 必须为 0
```

---

## Phase 5: 闸门检查

```bash
grep -nE 'TBD|TODO|后续补充' docs/plans/<filename>.md
# 空则通过
```

---

## Phase 6: plan-reviewer 审查

派发 plan-reviewer 子代理检查：覆盖度、一致性、可执行性、测试规约、护栏合规。

最多 2 轮修复。

---

## Phase 7: 呈现确认

展示计划摘要、审查结果、文档路径。等待用户确认。

---

## Phase 8: 交接

用户确认 → 调用 `yolo-executing`。
