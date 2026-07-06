# NVIDIA GPU 部署

## TensorRT 推理

```python
from ultralytics import YOLO
model = YOLO('best.engine')
results = model.predict(source='test.mp4', conf=0.25)
```

## 性能参考（YOLOv8s, 640x640）

| 精度 | 延迟 | FPS |
|------|------|-----|
| FP32 | 12ms | 83 |
| FP16 | 7ms | 143 |
| INT8 | 4ms | 250 |

## 常见问题

**TensorRT 构建慢**：首次构建需数分钟，后续缓存复用。

**CUDA 版本不匹配**：TRT 版本需与 CUDA 版本对应。
