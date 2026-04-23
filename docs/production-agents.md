# Production Agents

Slate v0.3 有两个执行型 agent：

- 图片生产 Agent
- 视频生产 Agent

它们都是**队列驱动**的，不参与故事、美术、分镜的创意判断。

## 图片生产 Agent

消费：

- `pending_image_jobs`

支持三种 `job_kind`：

- `asset_image`
- `first_frame`
- `last_frame`

成功回写：

- `asset_image` -> `Asset.reference_image_paths`
- `first_frame` -> `Shot.first_frame_ref.image_path`
- `last_frame` -> `Shot.last_frame_ref.image_path`

重试策略：

- 最多到 `retry_count >= 2`
- 达到上限即记为 `failed`

失败冒泡规则：

- 资产图失败 -> 默认 `revise_art`
- 首尾帧失败 -> 默认 `revise_storyboard`

## 视频生产 Agent

消费：

- `pending_video_jobs`

输入就是已经编译完成的 `ShotRenderRequest`。

重试策略：

- 最多重试 1 次

失败冒泡规则：

- 任一 job 失败且超重试上限 -> workflow `FAILED`

## 设计边界

两个生产 agent 都**不负责**：

- 改故事
- 改风格
- 改镜头
- 改资产命名

它们的唯一任务是：消费队列，回写结果，报告失败。
