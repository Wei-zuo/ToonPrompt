# Producer Log

## 阶段 1

- Stage：`intake`
- Decision：`APPROVED`
- Owner：`producer-agent`
- Artifact Path：`projects/zhaozhouqiao-001/brief.md`
- Acceptance Criteria：
  - 已读取用户原始剧本
  - 已明确目标为 `2D 动画风格`
  - 已确认本轮范围到 `制片整合`
- Risks：
  - 平台、预算、最终用途尚未明确
- Next Action：
  - 交给 `screenwriter-agent` 做 2D 动画适配改编

## 阶段 2

- Stage：`adaptation-story`
- Decision：`APPROVED`
- Owner：`screenwriter-agent`
- Artifact Path：`projects/zhaozhouqiao-001/story_package.md`
- Acceptance Criteria：
  - 保留原故事核心
  - 改成适合 180 秒 2D 动画的结构
  - 已形成明确叙事节奏和关键台词
- Risks：
  - 旁白过多会压缩画面呼吸
- Next Action：
  - 交给 `art-design-agent` 锁定 2D 国风美术方案

## 阶段 3

- Stage：`art-design`
- Decision：`APPROVED`
- Owner：`art-design-agent`
- Artifact Path：`projects/zhaozhouqiao-001/art_package.md`
- Acceptance Criteria：
  - 风格统一为 `2D 国风手绘动画`
  - 角色与桥体已有明确一致性锚点
  - 提示词和视觉母题可直接下放生产层
- Risks：
  - 如果桥体结构图不补，长片段镜头可能漂移
- Next Action：
  - 交给 `assistant-director-agent` 出分镜和执行反馈

## 阶段 4

- Stage：`assistant-director`
- Decision：`APPROVED_WITH_NOTES`
- Owner：`assistant-director-agent`
- Artifact Path：`projects/zhaozhouqiao-001/storyboard.md`
- Acceptance Criteria：
  - 已拆成 12 个镜头，总时长 180 秒
  - 已明确高潮镜头和风险镜头
  - 已给出反馈，当前可进入制片整合
- Risks：
  - 镜头 `09` 和 `10` 是成本与风格风险最高点
- Next Action：
  - 制片整合排期、代办和生产包

## 阶段 5

- Stage：`producer-integration`
- Decision：`READY_FOR_PRODUCTION`
- Owner：`producer-agent`
- Artifact Path：`projects/zhaozhouqiao-001/production_packet.md`
- Acceptance Criteria：
  - 已完成 `schedule.md`
  - 已完成 `production_todo.md`
  - 已完成 `production_packet.md`
  - 已明确先试跑后全量生产的策略
- Risks：
  - 尚未执行真实模型，最终动势和风格稳定性仍待验证
- Next Action：
  - 等待你确认这版改编和前期整合方向，再决定是否进入真实生产试跑
