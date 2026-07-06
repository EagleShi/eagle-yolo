#!/usr/bin/env python3
"""标注格式转换：COCO/VOC/LabelStudio → YOLO，及反向。"""

import argparse
import json
import os
import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict


def coco_to_yolo(input_json, output_dir, classes):
    with open(input_json) as f:
        coco = json.load(f)
    cat_map = {}
    for i, cat in enumerate(coco['categories']):
        cat_map[cat['id']] = classes.index(cat['name']) if classes else i
    img_info = {img['id']: img for img in coco['images']}
    ann_by_img = defaultdict(list)
    for ann in coco['annotations']:
        ann_by_img[ann['image_id']].append(ann)
    os.makedirs(output_dir, exist_ok=True)
    for img_id, anns in ann_by_img.items():
        img = img_info[img_id]
        w, h = img['width'], img['height']
        lines = []
        for ann in anns:
            ci = cat_map.get(ann['category_id'])
            if ci is None: continue
            bx, by, bw, bh = ann['bbox']
            lines.append(f"{ci} {(bx+bw/2)/w:.6f} {(by+bh/2)/h:.6f} {bw/w:.6f} {bh/h:.6f}")
        Path(output_dir, Path(img['file_name']).stem + '.txt').write_text('\n'.join(lines))


def voc_to_yolo(input_dir, output_dir, classes):
    os.makedirs(output_dir, exist_ok=True)
    for xml_file in Path(input_dir).glob('*.xml'):
        root = ET.parse(xml_file).getroot()
        w = int(root.find('size').find('width').text)
        h = int(root.find('size').find('height').text)
        lines = []
        for obj in root.findall('object'):
            name = obj.find('name').text
            if classes and name not in classes: continue
            ci = classes.index(name) if classes else 0
            bb = obj.find('bndbox')
            xmin, ymin = float(bb.find('xmin').text), float(bb.find('ymin').text)
            xmax, ymax = float(bb.find('xmax').text), float(bb.find('ymax').text)
            lines.append(f"{ci} {((xmin+xmax)/2)/w:.6f} {((ymin+ymax)/2)/h:.6f} {(xmax-xmin)/w:.6f} {(ymax-ymin)/h:.6f}")
        Path(output_dir, xml_file.stem + '.txt').write_text('\n'.join(lines))


def labelstudio_to_yolo(input_json, output_dir, classes):
    with open(input_json) as f:
        data = json.load(f)
    os.makedirs(output_dir, exist_ok=True)
    for item in data:
        if not item.get('annotations'): continue
        for ann in item['annotations']:
            if ann.get('was_cancelled'): continue
            img_name = Path(item['data']['image']).stem
            lines = []
            for r in ann.get('result', []):
                if r['type'] != 'rectanglelabels': continue
                v = r['value']
                label = v['rectanglelabels'][0]
                if classes and label not in classes: continue
                ci = classes.index(label) if classes else 0
                cx = (v['x'] + v['width']/2) / 100
                cy = (v['y'] + v['height']/2) / 100
                bw, bh = v['width']/100, v['height']/100
                lines.append(f"{ci} {cx:.6f} {cy:.6f} {bw:.6f} {bh:.6f}")
            Path(output_dir, f"{img_name}.txt").write_text('\n'.join(lines))


def yolo_to_coco(input_dir, output_json, images_dir, classes):
    coco = {'images': [], 'annotations': [], 'categories': [{'id': i, 'name': n} for i, n in enumerate(classes)]}
    ann_id = 0
    for img_id, txt in enumerate(sorted(Path(input_dir).glob('*.txt')), 1):
        img_name = txt.stem + '.jpg'
        img_path = Path(images_dir) / img_name
        if img_path.exists():
            try:
                import cv2
                img = cv2.imread(str(img_path))
                h, w = img.shape[:2]
            except ImportError:
                print("WARNING: opencv-python not installed, using default 640x640")
                w, h = 640, 640
        else: w, h = 640, 640
        coco['images'].append({'id': img_id, 'file_name': img_name, 'width': w, 'height': h})
        for line in txt.read_text().strip().splitlines():
            parts = line.split()
            if len(parts) < 5: continue
            ci, cx, cy, bw, bh = int(parts[0]), *map(float, parts[1:5])
            x, y = (cx-bw/2)*w, (cy-bh/2)*h
            aw, ah = bw*w, bh*h
            coco['annotations'].append({'id': ann_id, 'image_id': img_id, 'category_id': ci,
                'bbox': [round(x,2), round(y,2), round(aw,2), round(ah,2)], 'area': round(aw*ah,2), 'iscrowd': 0})
            ann_id += 1
    Path(output_json).write_text(json.dumps(coco, indent=2))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='YOLO 标注格式转换')
    p.add_argument('--from', dest='from_fmt', choices=['coco','voc','labelstudio'])
    p.add_argument('--to', dest='to_fmt', choices=['coco'])
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--classes', nargs='+')
    p.add_argument('--images-dir')
    args = p.parse_args()
    if args.from_fmt:
        {'coco': lambda: coco_to_yolo(args.input, args.output, args.classes),
         'voc': lambda: voc_to_yolo(args.input, args.output, args.classes),
         'labelstudio': lambda: labelstudio_to_yolo(args.input, args.output, args.classes)}[args.from_fmt]()
        print(f"Converted {args.from_fmt} → YOLO: {args.output}")
    elif args.to_fmt == 'coco':
        yolo_to_coco(args.input, args.output, args.images_dir, args.classes)
        print(f"Converted YOLO → COCO: {args.output}")
