---
name: yolo-training
description: >
  YOLO 模型训练全流程：多版本支持（YOLOv5/v8/v11）、训练参数配置、恢复训练、
  模型选择、训练监控。触发词：训练、train、微调、fine-tune、超参、epoch、
  模型选择、预训练、训练精度。
---

# YOLO Training — 模型训练

## 快速训练

```bash
# YOLOv8 检测
yolo detect train data=data.yaml model=yolov8n.pt epochs=100 imgsz=640 batch=16

# YOLOv11
yolo detect train data=data.yaml model=yolo11n.pt epochs=100 imgsz=640

# 分割任务
yolo segment train data=data.yaml model=yolov8n-seg.pt epochs=100

# 分类任务
yolo classify train data=dataset_path model=yolov8n-cls.pt epochs=100

# YOLOv5
python train.py --data data.yaml --cfg yolov5n.yaml --weights yolov5n.pt --epochs 100
```

## 模型选择

| 模型 | 参数量 | mAP | 适用场景 |
|------|--------|-----|----------|
| YOLOv8n | 3.2M | 37.3 | 移动端/MCU |
| YOLOv8s | 11.2M | 44.9 | 边缘设备 |
| YOLOv8m | 25.9M | 50.2 | Jetson/嵌入式 |
| YOLO11n | 2.6M | 39.0 | 最新轻量 |
| YOLO11s | 9.4M | 47.0 | 新一代边缘 |

**经验法则**：从 n 开始验证 pipeline，再换大模型。

## 训练参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| epochs | 100 | 训练轮数 |
| imgsz | 640 | 输入分辨率 |
| batch | 16 | 批大小（-1 自动） |
| lr0 | 0.01 | 初始学习率 |
| patience | 100 | 早停耐心 |
| device | '' | 0 / 0,1 / cpu |
| amp | True | 混合精度 |
| cos_lr | False | 余弦退火 |

## Python API

```python
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
results = model.train(
    data='data.yaml', epochs=100, imgsz=640,
    batch=16, device='0', patience=20,
    project='runs/train', name='my_model',
)
```

## 恢复训练

```bash
yolo detect train data=data.yaml model=runs/train/my_model/weights/last.pt epochs=200 resume=True
```

## 训练后

最佳权重保存在 `runs/train/<name>/weights/best.pt`。
