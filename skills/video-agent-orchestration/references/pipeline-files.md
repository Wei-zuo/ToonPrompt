# Pipeline Files

## `brief.md`

定义：

- 项目目标
- 平台 / 画幅 / 时长
- 目标受众
- required elements
- forbidden drift
- 本轮 scope

对应结构化产物：`ProjectBrief`

## `story_package.md`

应包含：

- one-line concept / logline
- adaptation strategy
- synopsis
- emotional rhythm
- `characters: list[CharacterCard]`
- `scenes: list[SceneSpec]`
- `beats: list[StoryBeat]`
- roles and goals
- draft narration or dialogue
- promised hook and recognition requirement when relevant
- notes for art
- notes for assistant director

对应结构化产物：`StoryPackage`

## `art_package.md`

应包含：

- overall visual direction
- color and lighting
- character / location / prop / style-pack anchor blocks
- costume and prop system
- environment and set notes
- literal vs metaphorical reveal decision when the concept depends on a transformation or gag
- prompt strategy
- prompt blocks when needed
- continuity constraints

对应结构化产物：`ArtGenerationPlan`

## `storyboard.md`

必须是可执行分镜，不是诗意说明。

至少包含：

- shot number
- beat id
- duration
- shot size
- camera move
- action
- first / last frame spec
- production requirement

对应结构化产物：`StoryboardPackage`

## `ad_feedback.md`

必须指出：

- what screenwriter must fix
- what art design must fix
- what storyboard must fix
- execution risks
- which shots to test first
- whether the promised hook still reads clearly on first watch

对应结构化产物：`AdFeedback`

## `production_packet.md`

必须总结：

- project
- required reads
- execution requirements
- global constraints
- shot-level notes
- producer go / no-go judgment
- compiled `ShotRenderRequest[]`

对应结构化产物：`ProductionPacket`
