# YOLO 常见错误码

## 训练错误

| 错误 | 原因 | 解决 |
|------|------|------|
| CUDA out of memory | 显存不足 | 减 batch / 降 imgsz / 用更小模型 |
| loss = nan | 学习率过高或数据异常 | 降 lr / 检查标签 / 检查数据 |
| 0 labels found | 标签路径错误或格式错 | 检查 labels/ 目录和 txt 格式 |
| ValueError: No images | 数据集路径错 | 检查 data.yaml 的 path 字段 |

## 导出错误

| 错误 | 原因 | 解决 |
|------|------|------|
| OpsetNotSupported | opset 版本过高 | 降低 opset 到 13/11 |
| TensorRT build failed | TRT 版本不兼容 | 检查 CUDA-TRT 版本对应 |
| ONNX simplify failed | 模型含不支持算子 | 关闭 simplify / 手动修复 |

## 推理错误

| 错误 | 原因 | 解决 |
|------|------|------|
| 推理结果全 0 | 预处理不一致 | 检查归一化、channel 顺序 |
| 推理极慢 | 未用 GPU/INT8 | 检查 device 参数和量化状态 |
| RKNN init failed | NPU 被占用 | 检查 core_mask 配置 |

## 环境错误

| 错误 | 原因 | 解决 |
|------|------|------|
| No module 'ultralytics' | 未安装 | pip install ultralytics |
| torch.cuda.is_available()=False | CUDA 未安装 | 安装 CUDA 版 PyTorch |
| libcuda.so not found | 驱动问题 | 安装/更新 NVIDIA 驱动 |
