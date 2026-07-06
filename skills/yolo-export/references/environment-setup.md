# 环境配置参考

## Python 环境

```bash
# 推荐 Python 3.10-3.12
conda create -n yolo python=3.11
conda activate yolo

# 基础
pip install ultralytics>=8.3.0 opencv-python-headless numpy

# 导出（按需）
pip install onnx onnxsim onnxruntime-gpu   # GPU 版
pip install openvino                        # Intel
pip install coremltools                     # Apple
```

## CUDA / cuDNN / TensorRT 版本对应

| PyTorch | CUDA | cuDNN | TensorRT |
|---------|------|-------|----------|
| 2.1+ | 12.1 | 8.9 | 8.6+ |
| 2.0 | 11.8 | 8.7 | 8.5+ |
| 1.13 | 11.7 | 8.5 | 8.4+ |

验证：
```bash
python -c "import torch; print(f'PyTorch {torch.__version__}, CUDA {torch.version.cuda}')"
python -c "import tensorrt; print(f'TensorRT {tensorrt.__version__}')"
```

## Jetson JetPack 对应

| JetPack | Jetson | CUDA | TensorRT | Python |
|---------|--------|------|----------|--------|
| 6.0 | Orin | 12.2 | 8.6 | 3.10 |
| 5.1 | Xavier | 11.4 | 8.5 | 3.8 |
| 4.6 | Nano | 10.2 | 8.2 | 3.6 |

## RKNN 工具链

```bash
git clone https://github.com/airockchip/rknn-toolkit2
cd rknn-toolkit2
pip install -r rknn-toolkit2/packages/requirements_cp311-2.3.0.txt
pip install rknn-toolkit2/packages/rknn_toolkit2-2.3.0-cp311-cp311-win_amd64.whl
```
