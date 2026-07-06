# MCU 部署

## 适用芯片

| 芯片 | RAM | 推荐模型 |
|------|-----|----------|
| STM32H7 | 1MB | YOLOv8n INT8 |
| ESP32-S3 | 512KB | 极简模型 |
| K210 | 8MB | YOLOv2 tiny |

## 路线 1: STM32Cube.AI

```bash
yolo export model=yolov8n.pt format=tflite int8=True data=data.yaml imgsz=320
# 然后用 STM32Cube.AI 转换为 C 代码
```

## 路线 2: Edge Impulse

导出 ONNX → 上传 Edge Impulse Studio → 自动转换 EIM 格式

## 优化策略

- 降低分辨率到 320/224
- INT8 量化
- 减少类别数
- 结构化剪枝

## 内存估算

YOLOv8n INT8 @imgsz=320：~1.5MB Flash, ~200KB RAM
