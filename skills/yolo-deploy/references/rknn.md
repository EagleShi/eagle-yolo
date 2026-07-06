# RKNN 部署（瑞芯微）

## 芯片支持

| 芯片 | NPU | 推荐模型 |
|------|-----|----------|
| RK3588 | 6 TOPS | YOLOv8s/m |
| RK3576 | 3 TOPS | YOLOv8n/s |
| RK3568 | 1 TOPS | YOLOv8n |

## 转换流程

```python
from rknn.api import RKNN
rknn = RKNN()
rknn.config(mean_values=[[0,0,0]], std_values=[[255,255,255]], target_platform='rk3588')
rknn.load_onnx(model='best.onnx')
rknn.build(do_quantization=True, dataset='calibration.txt')
rknn.export_rknn('best.rknn')
```

## 校准数据

```bash
find dataset/images/val -name "*.jpg" | head -200 > calibration.txt
```

## 推理

```python
rknn = RKNN()
rknn.load_rknn('best.rknn')
rknn.init_runtime(core_mask=RKNN.NPU_CORE_0)
outputs = rknn.inference(inputs=[img])
```

## 性能参考

| 芯片 | FP16 | INT8 |
|------|------|------|
| RK3588 | 15ms | 8ms |
| RK3576 | 25ms | 15ms |

## 常见问题

**算子不支持**：检查 rknn-toolkit2 支持列表，必要时修改 ONNX 结构。
**精度下降大**：增加校准图片，尝试仅 FP16。
