---
name: yolo-quantize
description: >
  YOLO 模型量化：FP16/INT8 PTQ/INT8 QAT/剪枝。含校准数据集生成、自定义量化脚本、
  量化后验证。触发词：量化、quantize、INT8、PTQ、QAT、剪枝、prune、FP16、半精度。
---

# YOLO Quantize — 模型量化

## 量化方式对比

| 方式 | 精度损失 | 加速 | 适用场景 |
|------|----------|------|----------|
| FP16 | 极小 | 1.5-2x | GPU 默认 |
| INT8 PTQ | 小 | 2-4x | 有校准数据 |
| INT8 QAT | 最小 | 2-4x | 精度要求高 |
| 剪枝 | 中 | 1.5-3x | 压缩体积 |

## 快速量化

```bash
# FP16
yolo export model=best.pt format=onnx half=True

# INT8 PTU（需校准数据）
yolo export model=best.pt format=onnx int8=True data=data.yaml

# TensorRT INT8
yolo export model=best.pt format=engine int8=True data=data.yaml
```

## 校准数据集

```bash
# 使用 yolo-data-prep 的脚本生成校准数据集
python ../yolo-data-prep/scripts/create_calibration_dataset.py --images-dir dataset/images/val --output calibration.txt --num 500
```

## 自定义 ONNX INT8 量化

```python
from onnxruntime.quantization import quantize_dynamic, QuantType
quantize_dynamic('best.onnx', 'best_int8.onnx', weight_type=QuantType.QInt8)
```

## 量化后验证

```bash
yolo detect val model=best.onnx data=data.yaml
yolo detect val model=best_int8.onnx data=data.yaml
# 精度下降 < 1% 可接受
```

## 平台特定注意事项

| 平台 | 注意 |
|------|------|
| TensorRT | FP16 几乎无损；INT8 需 calibration cache |
| TFLite | INT8 需 representative_dataset |
| RKNN | rknn-toolkit2 内置量化 |
| OpenVINO | INT8 需 accuracy_control API |
| NCNN | 仅支持 FP16 |
