# YOLO 方案候选库

按决策维度组织，每个维度 2-3 个方案供选择。

## 模型选择

| 方案 | 参数量 | mAP | 速度 | 适用 |
|------|--------|-----|------|------|
| YOLOv8n | 3.2M | 37.3 | 极快 | 移动端/MCU |
| YOLOv8s | 11.2M | 44.9 | 快 | 边缘设备 |
| YOLOv8m | 25.9M | 50.2 | 中 | Jetson |
| YOLOv8l | 43.7M | 52.9 | 慢 | 服务器 |
| YOLOv8x | 68.2M | 53.9 | 最慢 | 最高精度 |
| YOLO11n | 2.6M | 39.0 | 极快 | 最新轻量 |
| YOLO11s | 9.4M | 47.0 | 快 | 新一代边缘 |
| YOLO11m | 20.1M | 51.5 | 中 | 新一代嵌入式 |

**推荐决策树：**
- 移动端/MCU → YOLOv8n 或 YOLO11n
- 边缘设备 → YOLO11s（新项目）或 YOLOv8s（稳定）
- Jetson → YOLOv8m 或 YOLO11m
- 服务器 → YOLOv8l/x
- 追求最新 → YOLO11 系列

## 导出格式

| 方案 | 优势 | 劣势 | 适用 |
|------|------|------|------|
| ONNX | 通用、生态完善 | 非最快 | 通用中间格式 |
| TensorRT | NVIDIA GPU 最快 | 绑定 NVIDIA | GPU 部署 |
| CoreML | iOS 原生、Apple 优化 | 仅 Apple | iOS |
| TFLite | 跨移动端 | 精度损失略大 | Android/嵌入式 |
| NCNN | 移动端高性能 | 无 INT8 | 移动端 |
| OpenVINO | Intel 全线 | 仅 Intel | Intel 设备 |

## 量化方式

| 方案 | 精度损失 | 加速 | 复杂度 | 适用 |
|------|----------|------|--------|------|
| FP16 | 极小 | 1.5-2x | 低 | GPU 默认 |
| INT8 PTQ | 小 | 2-4x | 中 | 有校准数据 |
| INT8 QAT | 最小 | 2-4x | 高 | 精度敏感 |
| 剪枝 | 中 | 1.5-3x | 高 | 压缩体积 |

## 数据增强

| 方案 | 说明 | 适用 |
|------|------|------|
| Ultralytics 内置 | mosaic/mixup/hsv | 默认够用 |
| Albumentations | 离线增强 | 小数据集扩充 |
| Roboflow | 在线标注+增强 | 标注+增强一站式 |
| Mosaic+MixUp | 组合增强 | 小目标场景 |
