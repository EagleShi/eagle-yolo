---
name: yolo-deploy
description: >
  YOLO 跨平台部署：NVIDIA GPU/TensorRT、Jetson 全系列、iOS CoreML、Android TFLite/NCNN、
  Intel OpenVINO、RKNN 瑞芯微、MCU STM32。触发词：部署、deploy、Jetson、OpenVINO、
  RKNN、MCU、移动端、推理、inference、边缘设备。
---

# YOLO Deploy — 平台部署

按目标平台选择对应参考文档。

## 平台选择

| 平台 | 参考文档 | 关键命令 |
|------|---------|---------|
| NVIDIA GPU | `references/nvidia-gpu.md` | TensorRT engine |
| Jetson | `references/jetson.md` | JetPack + TRT |
| iOS | `references/ios-mobile.md` | CoreML |
| Android | `references/android-mobile.md` | TFLite / NCNN |
| Intel | `references/intel-openvino.md` | OpenVINO |
| RKNN | `references/rknn.md` | rknn-toolkit2 |
| MCU | `references/mcu.md` | STM32Cube.AI |

## NVIDIA GPU 快速部署

```python
from ultralytics import YOLO
model = YOLO('best.engine')
results = model.predict(source='test.mp4', conf=0.25)
```

## Jetson 必须在设备上构建 engine

```bash
yolo export model=best.pt format=engine half=True device=0
```

## RKNN 转换流程

```python
from rknn.api import RKNN
rknn = RKNN()
rknn.config(mean_values=[[0,0,0]], std_values=[[255,255,255]], target_platform='rk3588')
rknn.load_onnx(model='best.onnx')
rknn.build(do_quantization=True, dataset='calibration.txt')
rknn.export_rknn('best.rknn')
```

## 详细部署指南

每个平台的完整流程、性能数据、常见问题见对应 `references/*.md`。
