# ToonPrompt

Version: `0.2.0`

Open-source Codex skills for screenplay development, character prompt design, and producer-led video agent orchestration.

This repository now includes:

- `screenplay-development` for story development
- `character-prompt-engine` for prompt-only character design and key art generation
- `video-agent-orchestration` for turning a brief or existing script into a producer-led video production packet

## 中文简介

`ToonPrompt` 目前开源了三个可直接放进 Codex 的技能：

- `screenplay-development`：把灵感、梗概和草稿打磨成更可拍、更可卖的剧本
- `character-prompt-engine`：把角色设定、服化道、镜头与气质需求压缩成可直接出图的人设/定妆照提示词
- `video-agent-orchestration`：把 brief、现成剧本或改编任务，组织成制片驱动的视频 agent 流程，并整理出可交给生产层的 production packet

其中，`screenplay-development` 不是单纯的“剧本生成器”，而是一个更接近编剧室开发流程的工作流：

- 先把灵感打磨成可卖、可讲、可继续开发的“一句话故事”
- 再用 `Save the Cat / 救猫咪` 做结构压力测试
- 然后才往角色、beat、scene list、treatment、screenplay 逐层展开

这个 skill 适合处理四类输入：

- `spark`：一个词、一种情绪、一张画面、一个设定
- `premise`：一句话故事、logline、简短梗概
- `draft`：大纲、分场、对白页、初稿
- `industrialize`：希望把故事做得更可拍、更可卖、更适合系列化

`character-prompt-engine` 则更像一个“角色设计师 + 提示词编译器”：

- 默认只输出提示词本身，不写说明文档
- 适合角色定妆照、人设图、服装变化版、同角色多镜头一致性出图
- 强调脸型、发型、轮廓、服装结构、材质、色彩和道具锚点的稳定性

`video-agent-orchestration` 则负责把前两个 skill 串成真实的视频生产链：

- 制片先冻结 brief
- 编剧阶段调用 `screenplay-development`
- 美术阶段调用 `character-prompt-engine`
- 副导演产出 `storyboard.md` 和 `ad_feedback.md`
- 制片整合成 `schedule.md`、`production_todo.md`、`production_packet.md`

## 当前收录

- `skills/screenplay-development/`
  - 以一句话故事为前置闸门
  - 内置 `Save the Cat` 节拍和 logline 工作法
  - 支持短片、长片、剧集、微短剧的开发
  - 可用于前期立项、剧本医生、商业化重构
- `skills/character-prompt-engine/`
  - 面向角色设定、人设图、定妆照和视觉变体
  - 默认输出可直接复制到图像模型的 prompt
  - 支持 2D、写实、海报感、棚拍纯背景等常见模式
  - 适合和剧作 skill 串联使用，先做故事，再锁角色视觉
- `skills/video-agent-orchestration/`
  - 面向制片驱动的视频 agent 工作流
  - 产出 `brief`、`story package`、`art package`、`storyboard`、`AD feedback`、`schedule`、`production todo`、`production packet`
  - 适合改编已有剧本、民间传说、IP 设定和短片策划
  - 默认把 `screenplay-development` 和 `character-prompt-engine` 融入编剧与美术阶段

## 安装方式

将本仓库里的 skill 目录复制到本地 Codex skills 目录，例如：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/screenplay-development "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/character-prompt-engine "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/video-agent-orchestration "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装后，直接在 Codex 中调用：

```text
Use $screenplay-development 把这个灵感先打磨成 3 条一句话故事，等我选中再继续扩写。
```

```text
Use $character-prompt-engine 把这个角色设定整理成一条可直接出图的人设提示词，只输出提示词本身。
```

```text
Use $video-agent-orchestration 把这个剧本改编成 2D 动画前期生产包，并在编剧阶段调用 $screenplay-development、在美术阶段调用 $character-prompt-engine。
```

## OpenClaw 拉取

仓库拉取链接：

```text
https://github.com/Wei-zuo/ToonPrompt.git
```

如果你使用 OpenClaw，可以把这两个 skill 拉到共享 skills 目录：

```bash
git clone https://github.com/Wei-zuo/ToonPrompt.git
mkdir -p ~/.openclaw/skills
cp -R ToonPrompt/skills/character-prompt-engine ~/.openclaw/skills/
cp -R ToonPrompt/skills/screenplay-development ~/.openclaw/skills/
cp -R ToonPrompt/skills/video-agent-orchestration ~/.openclaw/skills/
```

如果你只想装到当前 workspace：

```bash
git clone https://github.com/Wei-zuo/ToonPrompt.git
mkdir -p ./skills
cp -R ToonPrompt/skills/character-prompt-engine ./skills/
cp -R ToonPrompt/skills/screenplay-development ./skills/
cp -R ToonPrompt/skills/video-agent-orchestration ./skills/
```

重开一个新的 OpenClaw session 后，skill 就会被加载。

## 目录结构

```text
skills/
  character-prompt-engine/
    SKILL.md
    agents/
      openai.yaml
  screenplay-development/
    SKILL.md
    agents/
      openai.yaml
    references/
      commercial-evaluation.md
      development-frameworks.md
      logline-and-save-the-cat.md
  video-agent-orchestration/
    SKILL.md
    agents/
      openai.yaml
    references/
      handoff-rules.md
      pipeline-files.md
examples/
  zhaozhouqiao-2d-adaptation/
    README.md
    art-tests/
      luban-test.png
      zhangguolao-test.png
      chaiwangye-test.png
      bridge-test.png
```

## 示例案例

仓库现在附带一个完整案例：

- `examples/zhaozhouqiao-2d-adaptation/`

这个案例展示了如何把《赵州桥·八仙试桥》从已有剧本改编成 `2D 国风动画` 的前期生产包，并附上 4 张测试美术图，方便对照 `art_package.md` 和后续 production packet。

### 案例设计逻辑

这个测试案例不是为了证明“模型能不能直接一键出片”，而是为了验证 `ToonPrompt` 的三层能力能不能串起来：

1. 先把已有民间故事剧本改编成 `更适合动画生产` 的叙事结构
2. 再把故事里的角色、桥体、服化道和神迹压缩成 `可重复出图` 的视觉约束
3. 最后把剧本材料、美术材料和分镜材料整理成 `生产层可以直接执行` 的 packet

换句话说，这个案例重点验证的是：

- 现成剧本能不能被接管，而不是被重写得面目全非
- 美术提示词能不能和故事节奏、分镜需求对齐
- 制片能不能把上游零散材料收束成下游可执行代办

### 这个案例为什么选《赵州桥》

选《赵州桥·八仙试桥》有三个原因：

- 它天然同时具备 `民间传奇`、`视觉奇观`、`文化传播` 三种属性，适合测试编剧、美术、制片三条链是否能协同
- 它既有人间动机，也有神话压迫，适合测试 `screenplay-development` 对“可拍性”和“高潮集中”的处理能力
- 它有明确的桥体、角色和仙迹，适合测试 `character-prompt-engine` 在结构锚点、一致性和测试图回写方面的能力

### 按步骤看，这一套能干什么

#### 1. Producer / 制片阶段

输入：

- 用户 brief
- 现成剧本
- 改编要求
- 风格要求

可以做什么：

- 冻结项目目标、时长、平台、轮次范围
- 判断这是 `new-brief`、`existing-script`、`adaptation` 还是 `production-rescue`
- 决定本轮只做到前期整合，还是继续进入生产

产出：

- `brief.md`
- `adaptation_notes.md`
- `producer_log.md`

#### 2. Screenwriter / 编剧阶段

调用：

- `screenplay-development`

可以做什么：

- 把原始剧本改成更适合动画的结构
- 压缩解释性对白，强化画面表达和旁白节奏
- 把故事整理成能继续交给美术和副导演的 `story_package.md`

在赵州桥案例里，这一步重点做了：

- 保留鲁班造桥、二仙试桥、桥上留痕的核心传奇
- 把结构改成 `12 镜头 / 180 秒`
- 把高潮集中到 `桥心惊变 -> 鲁班托桥 -> 仙迹留桥`

产出：

- `story_package.md`

#### 3. Art Design / 美术设计阶段

调用：

- `character-prompt-engine`

可以做什么：

- 锁定角色身份锚点
- 锁定桥体、服化道、道具、色板、光线
- 把视觉要求压成可直接测试的 prompt block
- 把测试图回写进案例，验证美术方向是否成立

在赵州桥案例里，这一步重点做了：

- 锁定鲁班、张果老、柴王爷、白驴、赵州桥的结构锚点
- 明确 `2D 国风手绘动画`，避免漂成写实 3D 或泛仙侠风
- 产出 4 张测试美术图，用来对照 `art_package.md`

产出：

- `art_package.md`
- `art-tests/*.png`

#### 4. Assistant Director / 副导演阶段

可以做什么：

- 把故事包和美术包拆成可执行镜头
- 判断哪些镜头风险最高
- 反馈哪些问题必须打回编剧或美术阶段

在赵州桥案例里，这一步重点做了：

- 把全片拆成 `12` 个镜头并校到 `180 秒`
- 标出 `09` 和 `10` 为最高风险镜头
- 明确要求补 `桥体结构图`、`仙迹定位图`、`桥下托桥 key art`

产出：

- `storyboard.md`
- `ad_feedback.md`

#### 5. Producer Integration / 制片整合阶段

可以做什么：

- 汇总剧本、美术、分镜、反馈
- 决定先试跑哪些镜头，哪些后做
- 把抽象方向翻成生产代办

在赵州桥案例里，这一步重点做了：

- 先锁 `03、09、10、12` 四个测试镜头
- 把全片拆成 `P0 / P1 / P2`
- 形成可交给生产 agent 的执行说明

产出：

- `schedule.md`
- `production_todo.md`
- `production_packet.md`
- `project-state.yaml`

### 什么时候该用这个案例

如果你想验证下面这些事情，这个案例有参考价值：

- 现成剧本怎么进入 agent 工作流
- 2D 动画项目怎么先做前期包，而不是直接盲跑模型
- 美术测试图怎么回写到文档体系里
- 制片 agent 如何把“剧本、美术、分镜”收束成生产 packet

如果你要测试的是：

- 真实视频模型调用
- 配音、音乐、剪辑
- 完整成片流水线

那这个案例只覆盖到 `生产前整合`，还没有覆盖最终生产执行。

## License

MIT
