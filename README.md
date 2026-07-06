# Eagle YOLO — Claude Code 插件

YOLO 目标检测全栈开发插件，覆盖从数据准备到跨平台部署的完整流程。

## 安装

### 方式 1：通过市场安装（推荐）

```bash
# 在 Claude Code 中执行
/plugins install eagle-yolo
```

### 方式 2：从 GitHub 安装

```bash
# 克隆仓库
git clone https://github.com/Eagle-0718/eagle-yolo.git ~/.claude/plugins/cache/eaglecode/eagle-yolo/1.0.0

# 重启 Claude Code
```

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
| yolo-deploy | 7 大平台部署（GPU/Jetson/iOS/Android/Intel/RKNN/MCU） |
| yolo-troubleshoot | 运行时故障排查 |

## 工作流程

```
用户需求 → yolo-workflow-entry（路由）
         → yolo-brainstorming（澄清 + 设计文档）
         → yolo-planning（执行计划 + 对抗审查）
         → yolo-executing（逐步执行）
            ├── yolo-data-prep
            ├── yolo-training
            ├── yolo-export
            ├── yolo-quantize
            ├── yolo-evaluate
            └── yolo-deploy
```

## 子代理

| 代理 | 用途 |
|------|------|
| yolo-plan-writer | 计划文档内容生成 |
| yolo-plan-reviewer | 计划对抗性审查 |
| yolo-code-writer | 代码实现（TDD） |
| yolo-code-reviewer | 代码对抗性审查 |

## 支持平台

NVIDIA GPU / Jetson / iOS / Android / Intel / RKNN / MCU

## 许可证

MIT
