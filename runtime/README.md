# Slate Runtime

Slate `runtime/` 是给 OpenClaw 或测试环境运行的 Python 层，不是给人手动“切 skill”用的。

它负责三件事：

- 把 `制片 -> 编剧 -> 美术设计 -> 图片生产 -> 副导演 -> 视频生产` 变成真实状态图
- 把每阶段输出约束成 `Pydantic` schema
- 把 `AssetLibrary`、`ShotRenderRequest` 编译、反馈回退和队列消费变成程序可执行流程

建议阅读顺序：

1. `../docs/agent-runtime-architecture.md`
2. `../docs/asset-library.md`
3. `video_agents/graph.py`
4. `video_agents/stubs.py`

## 目录

- `video_agents/assets.py`：`Asset` / `AssetLibrary`
- `video_agents/schemas.py`：全部结构化合同
- `video_agents/state.py`：LangGraph 状态与 revision budget
- `video_agents/services.py`：6 个 agent 的 Protocol
- `video_agents/image_production.py`：图片生产队列节点
- `video_agents/video_production.py`：视频生产队列节点
- `video_agents/compile.py`：`Shot -> ShotRenderRequest` 提示词编译器
- `video_agents/model_profile.py`：`ModelProfile` 和 `EXAMPLE_PROFILE`
- `video_agents/segment.py`：beat-aware `SegmentPacker`
- `video_agents/feedback.py`：关键词版 `FeedbackParser`
- `video_agents/stubs.py`：最小可跑 stub agents
- `video_agents/graph.py`：六角色状态图
- `video_agents/export_schemas.py`：导出单文件 `schemas.json`
