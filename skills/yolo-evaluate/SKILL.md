---
name: yolo-evaluate
description: >
  YOLO 模型评估：mAP/Precision/Recall 验证、可视化预测、速度基准测试、混淆矩阵。
  触发词：评估、eval、mAP、val、混淆矩阵、benchmark、速度测试、精度验证。
---

# YOLO Evaluate — 模型评估

## 模型验证

```bash
yolo detect val model=best.pt data=data.yaml
```

关键指标：
- **mAP50**：IoU=0.5 平均精度
- **mAP50-95**：IoU 0.5-0.95 平均精度（主指标）
- **Precision / Recall**

## Python API 评估

```python
from ultralytics import YOLO
model = YOLO('best.pt')
metrics = model.val(data='data.yaml')
print(f"mAP50: {metrics.box.map50}")
print(f"mAP50-95: {metrics.box.map}")
```

## 可视化预测

```python
results = model.predict(source='test_images/', save=True, conf=0.25)
# 结果保存在 runs/detect/predict/
```

## 速度基准

```python
import time
model = YOLO('best.pt')
img = np.random.randint(0, 255, (640, 640, 3), dtype=np.uint8)

# 预热
for _ in range(10):
    model.predict(img, verbose=False)

# 测速
start = time.time()
for _ in range(100):
    model.predict(img, verbose=False)
fps = 100 / (time.time() - start)
print(f"FPS: {fps:.1f}")
```

## 混淆矩阵

训练时启用 `plots=True` 自动生成：
```bash
yolo detect train data=data.yaml model=yolov8n.pt plots=True
```

或使用 `confusion_matrix.png` 在 `runs/detect/train/`。
