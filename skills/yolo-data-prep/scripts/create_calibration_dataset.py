#!/usr/bin/env python3
"""INT8 量化校准数据集生成。"""

import argparse
import random
from pathlib import Path


def create_calibration(images_dir, output_file, num=500, seed=42):
    exts = {'.jpg','.jpeg','.png','.bmp','.webp'}
    all_imgs = [f for ext in exts for f in Path(images_dir).rglob(f'*{ext}')]
    if not all_imgs: raise ValueError(f"No images in {images_dir}")
    random.seed(seed)
    selected = random.sample(all_imgs, min(num, len(all_imgs)))
    Path(output_file).write_text('\n'.join(str(i.resolve()) for i in selected) + '\n')
    print(f"Created: {output_file} ({len(selected)} images from {len(all_imgs)})")


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='校准数据集生成')
    p.add_argument('--images-dir', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--num', type=int, default=500)
    p.add_argument('--seed', type=int, default=42)
    a = p.parse_args()
    create_calibration(a.images_dir, a.output, a.num, a.seed)
