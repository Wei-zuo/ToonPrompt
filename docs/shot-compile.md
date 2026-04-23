# Shot Compile

`compile_shot` 是 Slate 把前期资料接到模型执行层的关键一步。

输入：

- `Shot`
- `AssetLibrary`
- `ModelProfile`
- `ProjectBrief`

输出：

- `ShotRenderRequest`

## 三个子步骤

### 1. 名字解析与共指消解

先用 `AssetLibrary.resolve_name(shot.description)` 找显式提到的资产。

然后做最小共指处理：

- `他 / 她` 优先回指最近提到的 `character`
- `它` 优先回指最近提到的非角色资产
- 若当前镜头没有显式 antecedent，则回退到 `shot.involved_asset_ids`

示例：

- `张果老走上桥，他低头看桥腹`
  - `他` 回指 `张果老`
- `纸鹤掠过城门，它突然发光`
  - `它` 回指 `纸鹤`

### 2. 参考图槽位绑定

根据 `ModelProfile.max_ref_images` 和 `role_binding_supported` 决定：

- 哪些资产进 `ref_images`
- 哪些资产降级成文字描述

如果模型不支持 role binding：

- 仍然可以给图片
- 但要在 `positive_text` 里把 reference subject 说明清楚

### 3. 渲染

`positive_text` 由三部分组成：

- style pack 描述
- asset text notes
- shot.description + camera phrase

`negative_text` 不在业务逻辑里硬编码 quirks，而是直接拼 `ModelProfile.required_negative_fragments`。

## `ModelProfile` 渲染案例

当 profile 是：

- `max_ref_images = 1`
- `role_binding_supported = False`
- `required_negative_fragments = ["no subtitles", "no watermark", "no logo"]`

则编译出来的请求会：

- 最多绑定 1 张参考图
- 其余资产降级成文字
- negative text 自动带上 3 条碎片

## 为什么这层重要

Slate 的上游全在说“名字”和“结构”，下游模型只能吃“参考图 + 可执行提示词”。

`compile_shot` 就是把这两种语言对齐的那一层。
