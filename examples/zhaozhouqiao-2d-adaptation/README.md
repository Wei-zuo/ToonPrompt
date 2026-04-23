# 赵州桥 2D 动画改编案例

这个例子展示 Slate v0.3 升级了什么：

- 保留原有 markdown 前期资料不动
- 新增 `AssetLibrary` 资产目录
- 新增结构化 `storyboard.json`
- 新增编译后的 `shot-render-requests.json`

## 输入与目标

- 输入：`赵州桥故事剧本`
- 风格：`2D 国风手绘动画`
- 目标：从人读材料推进到模型可读的 `ShotRenderRequest[]`

## 目录

- `brief.md` / `story_package.md` / `art_package.md` / `storyboard.md`
  - 给人读的版本
- `assets/`
  - 给 runtime 用的 `AssetLibrary`
- `storyboard.json`
  - 给程序用的 `StoryboardPackage`
- `shot-render-requests.json`
  - 用 `compile_all_shots + EXAMPLE_PROFILE` 生成的请求
- `scripts/build_demo.py`
  - 重新生成 JSON 产物

## 这个例子重点验证什么

1. 角色、桥体和 style pack 能不能先变成资产
2. 分镜能不能用新 `Shot` schema 表达
3. 分镜能不能稳定编译成 `ShotRenderRequest[]`

## 快速重建

在仓库根目录执行：

```bash
python3 examples/zhaozhouqiao-2d-adaptation/scripts/build_demo.py
```

成功后会刷新：

- `storyboard.json`
- `shot-render-requests.json`

## 资产预览

鲁班测试图：

![Luban Test](art-tests/luban-test.png)

赵州桥测试图：

![Bridge Test](art-tests/bridge-test.png)
