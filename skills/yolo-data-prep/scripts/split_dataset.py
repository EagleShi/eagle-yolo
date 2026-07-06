#!/usr/bin/env python3
"""数据集自动划分：train/val/test。"""

import argparse
import random
import shutil
from pathlib import Path


def split_dataset(input_dir, output_dir, ratios=(0.85, 0.10, 0.05), seed=42):
    inp = Path(input_dir); out = Path(output_dir)
    exts = {'.jpg','.jpeg','.png','.bmp','.webp','.tiff'}
    images_dir, labels_dir = inp / 'images', inp / 'labels'

    if images_dir.exists() and labels_dir.exists():
        imgs = sorted(set(f for ext in exts for f in images_dir.rglob(f'*{ext}')))
        has_sep = True
    else:
        imgs = sorted(f for f in inp.iterdir() if f.suffix.lower() in exts)
        has_sep = False

    if not imgs: raise ValueError(f"No images in {input_dir}")
    random.seed(seed); random.shuffle(imgs)

    t = len(imgs); te = int(t*ratios[0]); ve = te + int(t*ratios[1])
    splits = {'train': imgs[:te], 'val': imgs[te:ve], 'test': imgs[ve:]}

    for s in splits:
        (out/'images'/s).mkdir(parents=True, exist_ok=True)
        (out/'labels'/s).mkdir(parents=True, exist_ok=True)

    stats = {}
    for s, files in splits.items():
        for img in files:
            shutil.copy2(img, out/'images'/s/img.name)
            lf = (labels_dir / img.relative_to(images_dir)).with_suffix('.txt') if has_sep else img.with_suffix('.txt')
            if lf.exists(): shutil.copy2(lf, out/'labels'/s/lf.name)
        stats[s] = len(files)

    print(f"Split complete: {output_dir}")
    for n, c in stats.items(): print(f"  {n}: {c} ({c/t*100:.1f}%)")
    return stats


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='数据集划分')
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--ratios', nargs=3, type=float, default=[0.85, 0.10, 0.05])
    p.add_argument('--seed', type=int, default=42)
    a = p.parse_args()
    split_dataset(a.input, a.output, tuple(a.ratios), a.seed)
