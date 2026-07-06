# Intel OpenVINO 部署

## 支持设备

CPU (Core i3/i5/i7/i9)、Intel Arc GPU、Movidius VPU、NPU (Meteor Lake+)

## 推理

```python
from openvino.runtime import Core
import numpy as np

core = Core()
model = core.read_model('best.xml')
compiled = core.compile_model(model, 'AUTO')

input_layer = compiled.input(0)
output_layer = compiled.output(0)

results = compiled({input_layer: input_data})
```

## 性能参考（YOLOv8n, 640x640）

| 设备 | FP32 | FP16 | INT8 |
|------|------|------|------|
| i7-13700K CPU | 45ms | 28ms | 18ms |
| Arc A770 GPU | 12ms | 6ms | 4ms |

## Benchmark

```bash
benchmark_app -m best.xml -d CPU -api sync
```
