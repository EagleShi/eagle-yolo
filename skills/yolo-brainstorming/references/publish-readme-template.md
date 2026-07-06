# YOLO CodeG Skills

YOLO 目标检测全栈开发插件系统，覆盖从数据准备到跨平台部署的完整流程。

## 包含技能

| 技能 | 说明 |
|------|------|
| yolo-workflow-entry | 流程路由入口 |
| yolo-brainstorming | 需求澄清 → 设计文档 |
| yolo-planning | 设计文档 → 执行计划 |
| yolo-executing | 按计划逐步执行 |
| yolo-data-prep | 数据标注转换/增强/划分 |
| yolo-training | YOLOv5/v8/v11 训练 |
| yolo-export | ONNX/TensorRT/CoreML/TFLite/NCNN/OpenVINO |
| yolo-quantize | FP16/INT8 PTQ/QAT/剪枝 |
| yolo-evaluate | mAP/速度基准/混淆矩阵 |
| yolo-deploy | 7 大平台部署 |
| yolo-troubleshoot | 运行时故障排查 |

## 安装

### 安装全部技能

```bash
# 使用 skill-installer 脚本
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo <your-username>/yolo-codeg-skills \
  --path skills/yolo-workflow-entry skills/yolo-brainstorming skills/yolo-planning skills/yolo-executing skills/yolo-data-prep skills/yolo-training skills/yolo-export skills/yolo-quantize skills/yolo-evaluate skills/yolo-deploy skills/yolo-troubleshoot
```

### 安装单个技能

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo <your-username>/yolo-codeg-skills \
  --path skills/yolo-training
```

### 从 URL 安装

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --url https://github.com/<your-username>/yolo-codeg-skills/tree/main/skills/yolo-brainstorming
```

安装后重启 Claude Code 生效。

## 工作流程

```
用户需求 → yolo-workflow-entry（路由）
         → yolo-brainstorming（澄清）
         → yolo-planning（规划）
         → yolo-executing（执行）
            ├── yolo-data-prep
            ├── yolo-training
            ├── yolo-export
            ├── yolo-quantize
            ├── yolo-evaluate
            └── yolo-deploy
```

## 支持平台

NVIDIA GPU / Jetson / iOS / Android / Intel / RKNN / MCU

## 许可证

MIT
