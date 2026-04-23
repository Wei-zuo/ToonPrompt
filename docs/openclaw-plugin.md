# Slate as an OpenClaw Plugin

Slate v0.3 的目标形态是：**三个 skill + 一个 Python runtime**，作为完整的 OpenClaw 插件工作。

## 安装哪些 skill

把这三个目录装进 `~/.openclaw/skills/`：

- `skills/screenplay-development/`
- `skills/character-prompt-engine/`
- `skills/video-agent-orchestration/`

## Python runtime 怎么装

在仓库根目录执行：

```bash
pip install ./runtime
```

这会安装：

- `video_agents` Python package
- `langgraph`
- `pydantic`
- `pyyaml`

## 如何与 OpenClaw 的模型配置对接

Slate 本身不带任何模型 SDK。

OpenClaw 侧需要做的是：

1. 提供真实的 `ModelProfile`
2. 提供图片生产 Agent 的实际实现
3. 提供视频生产 Agent 的实际实现
4. 把 `ShotRenderRequest` 送入你自己的模型配置层

Slate 自带的 `EXAMPLE_PROFILE` 和 `stubs.py` 只用于测试与冒烟，不用于真实生产。

## 推荐工作方式

在 OpenClaw 里触发：

```text
Use $video-agent-orchestration
```

然后把具体 brief / 剧本 / 改编任务交给 Slate 主控 skill。

## 当前边界

v0.3 不做：

- 真实模型 SDK 集成
- 数据库
- Web UI
- CLI 包装
- 跨项目资产共享
