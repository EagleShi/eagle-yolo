---
name: yolo-executing
description: >
  YOLO 目标检测项目的计划执行。按计划文档逐步执行，每步完成后标记 checkbox，
  失败时停止等待用户决定。由 yolo-planning 交接触发。
---

# YOLO Executing — 计划执行

## 流程

```
Phase 0: 子代理可用性预检
Phase 1: 资源前置闸门
Phase 2: 逐步执行（或并行派发）
Phase 3: 静态验证（yolo-verification）
Phase 4: 运行时验证
Phase 5: 完成报告
Phase 6: 可选 git 收尾
```

---

## Phase 0: 子代理预检

确认 `code-writer` / `code-reviewer` 等子代理是否可用。缺失时降级为 general-purpose。

---

## Phase 1: 资源前置闸门

执行前检查：数据集、模型文件、SDK 依赖是否就绪。缺失则停止等待。

---

## Phase 2: 逐步执行

按计划依赖图顺序执行。每个 task：

1. 派发 writer 子代理
2. 验证产出
3. 派发 reviewer 子代理（FULL 级别）
4. 标记 checkbox 完成
5. 失败则停止，等待用户决策

---

## Phase 3-5: 验证与报告

执行完成后调用 `yolo-verification` 进行项目级验证。

---

## Phase 6: git 收尾（可选）

按用户要求 commit / 创建 PR。
