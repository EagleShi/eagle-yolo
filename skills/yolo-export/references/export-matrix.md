# 导出格式矩阵

## 完整对比

| 格式 | 后缀 | INT8 | FP16 | GPU | CPU | 移动端 | 命令 |
|------|------|------|------|-----|-----|--------|------|
| ONNX | .onnx | ✅ | ✅ | ✅ | ✅ | ✅ | format=onnx |
| TensorRT | .engine | ✅ | ✅ | ✅ | ❌ | ❌ | format=engine |
| CoreML | .mlpackage | ✅ | ✅ | ❌ | ✅ | iOS | format=coreml |
| TFLite | .tflite | ✅ | ✅ | ✅ | ✅ | Android | format=tflite |
| NCNN | ncnn/ | ❌ | ✅ | ❌ | ✅ | Android/iOS | format=ncnn |
| OpenVINO | openvino/ | ✅ | ✅ | ✅ | ✅ | ❌ | format=openvino |
| TorchScript | .torchscript | ❌ | ✅ | ✅ | ✅ | ❌ | format=torchscript |

## opset 版本建议

| opset | 兼容性 | 推荐用途 |
|-------|--------|----------|
| 11 | 最广 | 旧设备、MCU |
| 13 | 好 | RKNN、通用 |
| 17 | 推荐 | ONNX Runtime、OpenVINO |
| 18 | 最新 | 新特性 |

## 导出后验证

```bash
# ONNX 验证
python -c "import onnx; m=onnx.load('best.onnx'); print(f'Opset: {m.opset_import[0].version}')"

# TensorRT 验证
trtexec --onnx=best.onnx --saveEngine=best.engine --verbose

# 模型信息
python -c "from ultralytics import YOLO; m=YOLO('best.pt'); print(m.info())"
```

## 常见导出问题

| 问题 | 原因 | 解决 |
|------|------|------|
| ONNX simplify 失败 | 不支持的算子 | 降低 opset 或关闭 simplify |
| TRT 构建失败 | CUDA-TRT 版本不匹配 | 检查版本对应表 |
| TFLite INT8 精度差 | 校准数据不足 | 增加校准图片到 500+ |
| NCNN 转换失败 | 模型含不支持 op | 简化模型结构 |
| CoreML 动态形状 | iOS 不支持 | 固定 imgsz |
