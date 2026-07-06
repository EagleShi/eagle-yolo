---
name: yolo-export
description: >
  YOLO 模型导出：ONNX/TensorRT/CoreML/TFLite/NCNN/OpenVINO/TorchScript。
  支持 FP16/INT8 导出。触发词：导出、export、ONNX、TensorRT、CoreML、TFLite、
  NCNN、OpenVINO、TorchScript、模型转换。
---

# YOLO Export — 模型导出

## 导出命令速查

```bash
# ONNX（通用中间格式，必导）
yolo export model=best.pt format=onnx imgsz=640 simplify=True opset=17

# TensorRT
yolo export model=best.pt format=engine imgsz=640 half=True

# TensorRT INT8
yolo export model=best.pt format=engine int8=True data=data.yaml

# CoreML（iOS）
yolo export model=best.pt format=coreml imgsz=640

# TFLite
yolo export model=best.pt format=tflite imgsz=640 int8=True data=data.yaml

# NCNN
yolo export model=best.pt format=ncnn imgsz=640

# OpenVINO
yolo export model=best.pt format=openvino imgsz=640 int8=True data=data.yaml
```

## 导出矩阵

| 格式 | 后缀 | INT8 | FP16 | 命令 |
|------|------|------|------|------|
| ONNX | .onnx | ✅ | ✅ | format=onnx |
| TensorRT | .engine | ✅ | ✅ | format=engine |
| CoreML | .mlpackage | ✅ | ✅ | format=coreml |
| TFLite | .tflite | ✅ | ✅ | format=tflite |
| NCNN | ncnn/ | - | ✅ | format=ncnn |
| OpenVINO | openvino/ | ✅ | ✅ | format=openvino |

## ONNX 后处理

```bash
python -c "
import onnx, onnxsim
model = onnx.load('best.onnx')
model_simp, check = onnxsim.simplify(model)
assert check
onnx.save(model_simp, 'best_sim.onnx')
"
```

## Python API

```python
from ultralytics import YOLO
model = YOLO('best.pt')
model.export(format='onnx', imgsz=640, simplify=True)
```

## 详细参考

- 各平台导出细节见 `references/export-matrix.md`
- ONNX opset 选择见 `references/environment-setup.md`
