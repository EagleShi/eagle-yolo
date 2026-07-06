---
name: yolo-data-prep
description: >
  YOLO 数据准备全流程：多格式标注转换（COCO/VOC/LabelStudio/Roboflow → YOLO）、
  数据集划分、数据增强策略、数据质量检查。触发词：数据标注、格式转换、COCO、VOC、
  LabelStudio、Roboflow、数据增强、数据集划分、标注工具。
---

# YOLO Data Prep — 数据准备

## 目录结构（YOLO 标准）

```
dataset/
├── data.yaml
├── images/{train,val,test}/
└── labels/{train,val,test}/
```

## data.yaml 模板

```yaml
path: /absolute/path/to/dataset
train: images/train
val: images/val
test: images/test
nc: 80
names: ['person', 'car', ...]
```

## 标签格式

每图一个 `.txt`：`<class_id> <x_center> <y_center> <width> <height>`（归一化 0-1）

## 格式转换

```bash
# COCO → YOLO
python scripts/convert_annotations.py --from coco --input annotations.json --output labels/ --classes person car

# VOC → YOLO
python scripts/convert_annotations.py --from voc --input annotations/ --output labels/

# LabelStudio → YOLO
python scripts/convert_annotations.py --from labelstudio --input export.json --output labels/ --classes person car

# YOLO → COCO（反向）
python scripts/convert_annotations.py --to coco --input labels/ --output coco.json --images-dir images/train/ --classes person car
```

## 数据集划分

```bash
python scripts/split_dataset.py --input dataset/ --output split/ --ratios 0.85 0.10 0.05
```

## 数据增强

Ultralytics 内置已够用。小数据集建议用 Roboflow/Albumentations 离线扩充。

关键参数在 data.yaml 或训练时设置：
- `mosaic: 1.0`（马赛克）
- `mixup: 0.15`（MixUp）
- `fliplr: 0.5`（左右翻转）
- `hsv_h/s/v`（色彩增强）

## 数据质量检查

```bash
python scripts/check_dataset.py --dataset dataset/
```

检查项：标签与图片一一对应、坐标范围 [0,1]、类别 ID 合法、无空标签文件。
