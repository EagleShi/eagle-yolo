---
name: yolo-workflow-entry
description: >
  YOLO 目标检测全流程入口路由。当用户提到 YOLO、目标检测、模型训练、TensorRT、RKNN、
  模型量化、数据标注、边缘部署等关键词，且问题明确具体时，路由到对应子技能。
  跳过模糊需求（使用 yolo-brainstorming）。
---

# YOLO Workflow Entry — 流程路由

## 路由规则

根据用户输入关键词，路由到对应子技能：

| 关键词 | 路由目标 | 说明 |
|--------|---------|------|
| 数据标注、格式转换、COCO、VOC、LabelStudio、Roboflow | `yolo-data-prep` | 数据准备 |
| 训练、train、微调、fine-tune、超参、epoch | `yolo-training` | 模型训练 |
| 导出、export、ONNX、TensorRT、CoreML、TFLite、NCNN | `yolo-export` | 模型导出 |
| 量化、quantize、INT8、PTQ、QAT、剪枝 | `yolo-quantize` | 模型量化 |
| 评估、mAP、val、混淆矩阵、benchmark | `yolo-evaluate` | 模型评估 |
| 部署、deploy、Jetson、OpenVINO、RKNN、MCU、移动端 | `yolo-deploy` | 平台部署 |
| 报错、崩溃、超时、不工作、错误码 | `yolo-troubleshoot` | 故障排查 |
| 新项目、从零开始、全流程、完整项目 | `yolo-brainstorming` | 需求澄清→规划→执行 |

## 路由流程

```
1. 识别用户意图关键词
2. 匹配上表路由目标
3. 调用对应子技能
4. 子技能接管后续流程
```

## 错误码路由

| 错误码/现象 | 路由 |
|------------|------|
| CUDA OOM | `yolo-troubleshoot` |
| 导出失败 | `yolo-troubleshoot` → `yolo-export` |
| 精度下降 | `yolo-troubleshoot` → `yolo-quantize` |
| 推理速度慢 | `yolo-troubleshoot` → `yolo-deploy` |
| mAP 不收敛 | `yolo-troubleshoot` → `yolo-training` |

## 复合任务

用户需求跨越多个子技能时（如"训练一个模型并部署到 Jetson"），按流水线串联调用：

```
yolo-brainstorming → yolo-planning → yolo-executing
```

`yolo-executing` 内部会按计划自动调度 `yolo-data-prep` → `yolo-training` → `yolo-export` → `yolo-deploy`。
