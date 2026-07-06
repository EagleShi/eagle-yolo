---
name: yolo-troubleshoot
description: >
  YOLO 项目运行时诊断。遇到任何运行时问题——崩溃、超时、无结果、精度异常、
  导出失败、部署异常——必须先加载本 skill 再尝试修复。适用于所有 YOLO 项目。
---

# YOLO Troubleshoot — 运行时诊断

## 诊断流程

```
1. 收集症状（错误信息、日志、环境）
2. 分类问题类型
3. 按类型执行排查
4. 验证修复
```

## 常见问题分类

### 训练问题

| 症状 | 排查方向 |
|------|---------|
| CUDA OOM | 减 batch、降 imgsz、启用 AMP、检查 GPU 内存 |
| mAP 不收敛 | 检查标签质量、学习率、数据增强、类别平衡 |
| 训练极慢 | 检查 DataLoader workers、数据加载瓶颈、GPU 利用率 |
| loss 为 nan | 学习率过高、数据有异常值、标签格式错误 |

### 导出问题

| 症状 | 排查方向 |
|------|---------|
| ONNX 导出失败 | 检查 opset、简化模型、关闭动态轴 |
| TensorRT 构建慢 | 首次正常，检查 TRT 版本兼容 |
| 精度下降大 | INT8 校准数据不足、量化参数需调整 |

### 部署问题

| 症状 | 排查方向 |
|------|---------|
| 推理速度慢 | 确认使用 GPU/INT8、检查预处理耗时 |
| 结果异常 | 检查预处理是否一致（归一化、channel 顺序） |
| RKNN 转换失败 | 检查 op 支持列表、ONNX opset |
| 移动端崩溃 | 检查模型大小、内存限制、输入格式 |

## 诊断命令

```bash
# 环境检查
nvidia-smi
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}, Device: {torch.cuda.get_device_name(0)}')"
pip show ultralytics onnx tensorrt

# 模型检查
python -c "from ultralytics import YOLO; m = YOLO('best.pt'); print(m.info())"

# ONNX 检查
python -c "import onnx; m = onnx.load('best.onnx'); print(f'Opset: {m.opset_import[0].version}, IR: {m.ir_version}')"
```

## 详细参考

- 常见错误码见 `references/error-codes.md`
- 平台特定问题见 `references/platform-issues.md`
