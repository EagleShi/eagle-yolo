#!/usr/bin/env python3
"""YOLO 数据集质量检查：标签完整性、坐标范围、类别合法性。"""

import argparse
import sys
from pathlib import Path


def check_dataset(dataset_dir, class_names=None):
    ds = Path(dataset_dir)
    images_dir = ds / 'images'
    labels_dir = ds / 'labels'
    data_yaml = ds / 'data.yaml'

    errors = []
    warnings = []

    # 检查目录结构
    if not images_dir.exists():
        errors.append("images/ 目录不存在")
    if not labels_dir.exists():
        errors.append("labels/ 目录不存在")
    if errors:
        for e in errors: print(f"ERROR: {e}")
        return False

    # 收集所有图片和标签
    img_exts = {'.jpg', '.jpeg', '.png', '.bmp', '.webp', '.tiff'}
    all_imgs = {}
    all_labels = {}

    for split in ['train', 'val', 'test']:
        split_img_dir = images_dir / split
        split_lbl_dir = labels_dir / split
        if not split_img_dir.exists():
            warnings.append(f"images/{split}/ 不存在，跳过")
            continue
        for f in split_img_dir.rglob('*'):
            if f.suffix.lower() in img_exts:
                all_imgs[f.stem] = f
        if split_lbl_dir.exists():
            for f in split_lbl_dir.rglob('*.txt'):
                all_labels[f.stem] = f

    print(f"图片数: {len(all_imgs)}, 标签数: {len(all_labels)}")

    # 检查匹配
    no_label = set(all_imgs.keys()) - set(all_labels.keys())
    no_img = set(all_labels.keys()) - set(all_imgs.keys())
    if no_label:
        warnings.append(f"{len(no_label)} 张图片无对应标签: {list(no_label)[:5]}...")
    if no_img:
        warnings.append(f"{len(no_img)} 个标签无对应图片: {list(no_img)[:5]}...")

    # 检查标签内容
    bad_labels = 0
    class_ids = set()
    for stem, lbl_path in all_labels.items():
        try:
            lines = lbl_path.read_text(encoding='utf-8').strip().splitlines()
        except Exception as e:
            errors.append(f"读取失败 {lbl_path}: {e}")
            bad_labels += 1
            continue
        for i, line in enumerate(lines):
            parts = line.split()
            if len(parts) < 5:
                errors.append(f"{lbl_path.name}:{i+1} 字段不足5个: {line}")
                bad_labels += 1
                continue
            try:
                cid = int(parts[0])
                coords = list(map(float, parts[1:5]))
                class_ids.add(cid)
                for j, c in enumerate(coords):
                    if j < 2:  # x_center, y_center
                        if c < 0 or c > 1:
                            errors.append(f"{lbl_path.name}:{i+1} 坐标越界 [{c}]")
                            bad_labels += 1
                    else:  # width, height
                        if c <= 0 or c > 1:
                            errors.append(f"{lbl_path.name}:{i+1} 尺寸异常 [{c}]")
                            bad_labels += 1
            except ValueError:
                errors.append(f"{lbl_path.name}:{i+1} 格式错误: {line}")
                bad_labels += 1

    # 类别检查
    if class_names and class_ids:
        max_id = max(class_ids)
        if max_id >= len(class_names):
            errors.append(f"类别 ID {max_id} 超出 data.yaml 定义的 {len(class_names)} 类")
        print(f"类别 ID 范围: {min(class_ids)}-{max_id}")

    # 汇总
    print(f"\n检查完成:")
    print(f"  错误: {len(errors)}")
    print(f"  警告: {len(warnings)}")
    for w in warnings: print(f"  WARN: {w}")
    for e in errors[:20]: print(f"  ERROR: {e}")
    if len(errors) > 20: print(f"  ... 还有 {len(errors)-20} 个错误")

    return len(errors) == 0


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='YOLO 数据集质量检查')
    p.add_argument('--dataset', required=True, help='数据集根目录')
    p.add_argument('--classes', nargs='+', help='类别名列表（可选）')
    a = p.parse_args()
    ok = check_dataset(a.dataset, a.classes)
    sys.exit(0 if ok else 1)
