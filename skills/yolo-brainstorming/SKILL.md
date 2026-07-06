---
name: yolo-brainstorming
description: >
  YOLO 目标检测项目的需求澄清。当用户提出模糊的 YOLO 任务（"训练一个检测模型"、
  "部署到边缘设备"）需要先澄清再规划时触发。跳过已明确的需求（用户说"直接规划"或"直接做"）。
---

<HARD-GATE>
**禁止行为（未确认设计文档前）**：
- 禁止调用 `yolo-planning`
- 禁止调用 `yolo-executing`
- 禁止直接写代码、修改配置
- 即使用户说"直接写吧"，也必须先产出设计文档草稿

**唯一豁免**：任务粒度极小（< 5 行改动、单参数调整）。

**流程锁定**：brainstorming → 设计文档 → 用户确认 → planning → executing
</HARD-GATE>

# YOLO Brainstorming — 需求澄清

将模糊需求转化为明确的规划输入。完成后交接给 `yolo-planning`。

## 流程

```
Phase 1: 工程扫描（记录项目现状）
Phase 2: 环境门禁（检测 GPU/CUDA/工具链）
Phase 3: 意图分类（任务类型 + 部署领域）
Phase 4: 访谈（只问必须问的）
Phase 5: 方案选项呈现（2-3 个方案 + tradeoffs + 推荐）
Phase 6: 写设计文档
Phase 7: spec-reviewer 评审
Phase 8: 交接 yolo-planning
```

---

## Phase 1: 工程扫描

**只做机械扫描，不做判定。**

### 扫描清单

1. **项目结构**：根目录布局、技术栈文件（`pyproject.toml`/`requirements.txt`/`CMakeLists.txt`）
2. **数据集**：`dataset/`、`data.yaml` 是否存在，标注格式
3. **模型**：已有 `.pt`/`.onnx`/`.engine` 文件
4. **训练记录**：`runs/` 目录，已有实验结果
5. **部署产物**：`deploy/`、平台特定文件

### 输出"工程现状摘要"

```
project_root: /xxx/yyy
tech_stack: Python 3.11 + ultralytics 8.3
dataset: 存在/缺失，格式，类别数
existing_models: 已有模型列表
deployment_target: 已知目标平台（如有）
gaps: 缺失项一行小结
```

**Phase 1 完成后 → 进入 Phase 2**

---

## Phase 2: 环境门禁

检测开发环境：

```bash
# GPU 可用性
nvidia-smi
python -c "import torch; print(torch.cuda.is_available())"

# Ultralytics 版本
pip show ultralytics

# 已安装导出工具
pip list | grep -E "onnx|tensorrt|openvino|coremltools"
```

记录环境事实，写入设计文档的"已确认事实清单"。

---

## Phase 3: 意图分类

**维度 1 — 任务类型：**

| 类型 | 访谈深度 | 示例 |
|------|---------|------|
| 全新项目 | 完整访谈 | "从零搭建检测系统" |
| 模型训练 | 中等 | "用自己的数据训练" |
| 模型优化 | 轻量 | "量化加速" |
| 平台迁移 | 完整 | "从 GPU 迁移到 RKNN" |
| 问题修复 | 轻量 | "训练精度上不去" |

**维度 2 — 部署领域（叠加层）：**

| 领域 | 关键词 | 叠加子技能 |
|------|--------|-----------|
| NVIDIA GPU | TensorRT, CUDA, 服务器 | `yolo-export` + `yolo-deploy` |
| Jetson | Jetson, Orin, 嵌入式 GPU | `yolo-deploy` |
| 移动端 | iOS, Android, CoreML, TFLite | `yolo-export` + `yolo-deploy` |
| Intel | OpenVINO, CPU, VPU | `yolo-deploy` |
| RKNN | 瑞芯微, RK3588, NPU | `yolo-deploy` |
| MCU | STM32, ESP32, 微控制器 | `yolo-quantize` + `yolo-deploy` |

---

## Phase 4: 访谈

### 最小必问（所有任务）

1. 检测什么目标？（类别）
2. 数据量多大？有标注吗？
3. 目标部署平台？
4. 性能要求？（精度优先 vs 速度优先）

### 按类型补问

**全新项目**：数据从哪来？预算？时间约束？
**模型训练**：预训练模型版本？训练时长限制？
**模型优化**：可接受的精度损失？目标加速比？
**平台迁移**：当前是什么平台？迁移原因？

### 使用 question 工具提问

```python
# 批量独立问题一次提出
question(questions=[
    {"question": "检测什么目标？", "header": "检测目标", "options": [...]},
    {"question": "部署到什么平台？", "header": "部署平台", "options": [...]},
])
```

---

## Phase 5: 方案选项呈现

加载 `references/scheme-catalog.md`，按维度呈现 2-3 个方案：

```markdown
## 方案选项

### 模型选择
- **方案 A（推荐）**：YOLOv8s — 平衡精度与速度
- **方案 B**：YOLO11n — 最新轻量，适合边缘
- **方案 C**：YOLOv8x — 最高精度，需要 GPU

### 导出格式
- **方案 A（推荐）**：ONNX + TensorRT — GPU 最优
- ...
```

---

## Phase 6: 写设计文档

加载 `references/design-doc-template.md`，填充到 `docs/specs/YYYY-MM-DD-<name>-design.md`

---

## Phase 7: spec-reviewer 评审

派发子代理对抗评审设计文档。

---

## Phase 8: 交接

用户确认设计文档后 → 调用 `yolo-planning`。
