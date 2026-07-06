# 平台特定问题

## NVIDIA GPU

| 问题 | 原因 | 解决 |
|------|------|------|
| CUDA OOM | 显存不足 | 减 batch / 降 imgsz / 用更小模型 |
| driver version is insufficient | CUDA 与驱动不匹配 | 安装匹配的 NVIDIA 驱动 |
| cuDNN error | cuDNN 版本不对 | 重装 cuDNN 或用 conda 安装 |

## Jetson

| 问题 | 原因 | 解决 |
|------|------|------|
| 内存不足 | Nano 4GB 限制 | 关桌面、降 imgsz、用 nvpmodel |
| USB 摄像头延迟 | GStreamer 管道问题 | 改用 V4L2 |
| TRT engine 构建慢 | 首次编译正常 | 后续复用缓存 |

## 移动端

| 问题 | 原因 | 解决 |
|------|------|------|
| CoreML 转换失败 | 不支持的 op | 降低 opset、简化模型 |
| TFLite 推理慢 | 未用 GPU delegate | 启用 GPU/NPU delegate |
| Android NNAPI 报错 | 设备不支持 | fallback 到 CPU |

## Intel OpenVINO

| 问题 | 原因 | 解决 |
|------|------|------|
| 模型加载失败 | XML/BIN 不配对 | 确认两个文件同目录 |
| GPU 推理慢 | 首次编译 kernel | 后续会加速 |
| INT8 精度差 | 校准数据不足 | 增加校准图片 |

## RKNN

| 问题 | 原因 | 解决 |
|------|------|------|
| 算子不支持 | 模型含 RKNN 不支持的 op | 修改 ONNX 结构或换模型 |
| NPU 被占用 | 其他进程占用 | kill 占用进程或换 core_mask |
| 精度下降大 | INT8 量化损失 | 改用 FP16 或增加校准数据 |
| 推理结果全 0 | 预处理不一致 | 检查 mean/std 和 channel 顺序 |

## MCU

| 问题 | 原因 | 解决 |
|------|------|------|
| Flash 不够 | 模型太大 | 降 imgsz 到 320、用更小模型 |
| RAM 不够 | 特征图峰值内存高 | 减少类别、降分辨率 |
| 推理极慢 | 无硬件加速 | 使用 STM32 Chrom-ART |
