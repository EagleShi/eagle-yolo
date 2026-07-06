---
name: yolo-executing
description: >
  YOLO 目标检测项目的计划执行。按计划文档逐步执行，每步完成后标记 checkbox，
  失败时停止等待用户决定。由 yolo-planning 交接触发。
---

<HARD-GATE>
**禁止跳步**：必须按 Phase 顺序执行，不得跳过预检和资源闸门。
**禁止静默失败**：writer 返回错误时必须停止并报告，不得自行修复继续。
</HARD-GATE>

# YOLO Executing — 计划执行

## 流程

```
Phase 0: 子代理可用性预检
Phase 1: 资源前置闸门
Phase 2: 逐步执行（按依赖图）
Phase 3: 静态验证
Phase 4: 运行时验证
Phase 5: 完成报告
Phase 6: 可选 git 收尾
```

---

## Phase 0: 子代理预检

派发任何子代理前，确认所需 agent 是否可用：

```bash
# 检查 agent 是否注册
# 在 Claude Code 中验证 yolo-code-writer / yolo-code-reviewer 是否在可用列表
```

缺失时降级表：

| 缺失的 agent | 降级策略 |
|-------------|---------|
| yolo-code-writer | 用 general-purpose，prompt 首行写"立即执行，不要反问" |
| yolo-code-reviewer | 降级为主代理自审（读测试输出 + 跑验证命令） |
| 两个都缺 | SKIP 主代理直接做；FULL 用 general + 强制执行 |

---

## Phase 1: 资源前置闸门

执行前检查所有依赖是否就绪：

```bash
# 数据集
ls dataset/images/train/ dataset/images/val/ data.yaml

# 预训练模型（如需要）
ls *.pt || echo "需要下载预训练模型"

# 导出工具（如需要导出）
pip list | grep -E "onnx|tensorrt|openvino"
```

缺失 → 停止，报告缺失项，等待用户补充。

---

## Phase 2: 逐步执行

### 执行顺序

读取计划文档的依赖图，按拓扑排序执行：

```
步骤1 → 步骤2 → 步骤4
步骤1 → 步骤3 → 步骤4（2和3可并行）
```

### 每步执行流程

**FULL 级别（业务代码）：**

1. 派发 `yolo-code-writer`，传入 step_id、plan_file、step_content
2. 等待返回：文件列表 + 测试输出 + 验证证据
3. 检查返回状态：成功 → 继续；失败 → 停止
4. 派发 `yolo-code-reviewer`，传入 changed_files
5. 审查通过 → 标记 checkbox；不通过 → 派 writer 修复（最多 2 轮）

**LITE 级别（配置/构建）：**

1. 派发 `yolo-code-writer`，传入 step_id、plan_file、step_content
2. 检查返回状态
3. 主代理验证（格式检查、语法检查）
4. 通过 → 标记 checkbox

**SKIP 级别（目录/文档）：**

1. 主代理直接执行 bash 命令
2. 验证结果
3. 标记 checkbox

### 并行执行

无依赖的步骤可并行派发 writer（最多 5 个同时）：

```python
# 伪代码
parallel([
    dispatch_writer(step_2),
    dispatch_writer(step_3),
])
# 等待两者完成后再执行 step_4
```

### 失败处理

writer 返回错误时：

1. 记录错误信息
2. **停止执行后续步骤**
3. 向用户报告：
   - 失败步骤编号和内容
   - 错误信息
   - 已完成的步骤
   - 建议修复路径
4. 等待用户决策：修复后重试 / 跳过 / 终止

---

## Phase 3: 静态验证

所有步骤完成后，执行项目级静态检查：

```bash
# 代码语法检查
python -m py_compile src/*.py

# 配置文件格式
python -c "import yaml; yaml.safe_load(open('data.yaml'))"

# 文件完整性
ls -la runs/train/*/weights/best.pt
ls -la export/*.onnx
```

---

## Phase 4: 运行时验证

按计划文档的"验证策略"执行：

```bash
# 模型验证
yolo detect val model=best.pt data=data.yaml

# 推理测试
python -c "from ultralytics import YOLO; m=YOLO('best.pt'); m.predict('test.jpg', save=True)"

# 导出验证（如适用）
python -c "import onnx; m=onnx.load('best.onnx'); print('ONNX OK')"
```

---

## Phase 5: 完成报告

向用户展示：

```
执行完成摘要
============
总步骤: N
成功: M
跳过: K
失败: 0

产出文件:
- runs/train/my_model/weights/best.pt
- export/best.onnx
- ...

验证结果:
- mAP50: 0.85
- mAP50-95: 0.62
- 推理速度: 8.2ms (GPU)
```

---

## Phase 6: git 收尾（可选）

用户要求时：

```bash
git add -A
git commit -m "feat: YOLO 模型训练与导出完成"
```
