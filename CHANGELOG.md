# Changelog

## 0.3.0 - 2026-04-23

- Reframed Slate as a full OpenClaw plugin with a six-agent architecture: producer, screenwriter, art design, image production, assistant director, and video production.
- Rewrote `README.md` to make `ShotRenderRequest[]` the end-state and document OpenClaw installation plus the new runtime relationship.
- Rewrote all three `SKILL.md` files to align with the six-agent flow and the v0.3 runtime contracts.
- Rewrote `runtime/video_agents/` around `AssetLibrary`, `ArtGenerationPlan`, `Shot`, `ShotRenderRequest`, queue-driven production nodes, `compile_shot`, `SegmentPacker`, and stub agents.
- Added new runtime modules: `assets.py`, `image_production.py`, `video_production.py`, `compile.py`, `model_profile.py`, `segment.py`, `feedback.py`, and `stubs.py`.
- Upgraded `graph.py` to a six-stage LangGraph with image-production reentry, AD cut/review split, revision routing, and queued video production.
- Switched schema export to a single `runtime/video_agents/schemas.json` target.
- Added new documentation for `AssetLibrary`, `compile_shot`, production agents, and OpenClaw plugin usage.
- Upgraded the Zhaozhou example target from markdown-only packet output toward structured assets, storyboard JSON, and compiled render requests.
- Bumped runtime packaging metadata and repository version to `0.3.0`.

## 0.2.0 - 2026-04-22

- Added `video-agent-orchestration`, a producer-led video pipeline skill that coordinates brief, story package, art package, storyboard, AD feedback, schedule, production todo, and production packet.
- Added `examples/zhaozhouqiao-2d-adaptation/` as a full adaptation and producer-integration example for a 2D folklore animation workflow.
- Added four art test images for the Zhaozhou Bridge example to show visual direction and character exploration.
- Introduced a simple repository version file: `VERSION`.

## 0.1.0 - Initial Release

- Released `screenplay-development`.
- Released `character-prompt-engine`.
