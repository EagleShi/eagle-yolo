# Eagle YOLO 项目指令

本项目是一个 YOLO 目标检测全栈开发插件，支持 Claude Code 平台。

## 目录结构

- `agents/` — Agent 定义（Markdown + YAML frontmatter）
- `skills/` — 工作流和领域知识（唯一工作流表面）
- `config/` — 程序化配置
- `.claude-plugin/` — Claude Code 平台适配

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

## 开发约定

### Agent 格式

```markdown
---
name: agent-name
description: One-sentence description
tools: ["Read", "Bash"]
model: sonnet
---

Agent 的系统提示词内容...
```

### Skill 格式

每个 skill 放在 `skills/<skill-name>/SKILL.md`，包含 frontmatter（name + description）和工作流指令。

## 添加新内容

1. 新 Agent → 在 `agents/` 下创建 `.md` 文件
2. 新 Skill → 在 `skills/<name>/` 下创建 `SKILL.md`
3. 更新 `config/agents.json` 注册表（如有新 agent）
