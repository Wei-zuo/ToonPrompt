"""Build the Slate v0.3 Zhaozhou example outputs.

Run from the repository root:

    python3 examples/zhaozhouqiao-2d-adaptation/scripts/build_demo.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from runtime.video_agents.assets import AssetLibrary
from runtime.video_agents.compile import compile_all_shots
from runtime.video_agents.model_profile import EXAMPLE_PROFILE
from runtime.video_agents.schemas import CameraSpec, FrameRef, InputRoute, ProjectBrief, Shot, StoryboardPackage


EXAMPLE_ROOT = REPO_ROOT / "examples" / "zhaozhouqiao-2d-adaptation"
ASSET_ROOT = EXAMPLE_ROOT / "assets"


def build_brief() -> ProjectBrief:
    """Return the example brief."""

    return ProjectBrief(
        project_id="zhaozhouqiao-001",
        route=InputRoute.ADAPTATION,
        title="赵州桥·八仙试桥",
        goal="把赵州桥传说推进到结构化 ShotRenderRequest 列表",
        platform="OpenClaw",
        format="2D Chinese folklore animation",
        target_duration_seconds=180,
        language="zh-CN",
        aspect_ratio="16:9",
        target_audience=["文旅内容受众", "学生家庭向观众", "动画短片观众"],
        source_materials=["story_package.md", "art_package.md", "storyboard.md"],
        required_elements=["鲁班", "张果老", "柴王爷", "赵州桥", "日月五岳", "仙迹留桥"],
        forbidden_drift=["photoreal 3D", "idol xianxia styling", "tourism-ad kitsch"],
        delivery_scope="storyboard and shot render requests",
    )


def build_storyboard() -> StoryboardPackage:
    """Return the structured 12-shot storyboard."""

    shots = [
        Shot(
            shot_id="shot-01",
            beat_id="beat-01",
            duration_seconds=10,
            description="洨河横亘两岸，赵州桥尚未出现，百姓和车马被水阻断。",
            involved_asset_ids=[],
            camera=CameraSpec(movement="侧移", shot_size="extreme wide", position="high", speed="slow"),
            first_frame_ref=FrameRef(source="to_generate", generation_hint="河岸被阻的起始大全景"),
            last_frame_ref=FrameRef(source="to_generate", generation_hint="停在尚未建桥的河面"),
            style_pack_id="2d-guofeng",
            risk_level="low",
            notes="Establish the problem before the bridge exists.",
        ),
        Shot(
            shot_id="shot-02",
            beat_id="beat-02",
            duration_seconds=14,
            description="鲁班夜里凿石起拱，火星与月色交替，他为百姓造桥。",
            involved_asset_ids=["luban"],
            camera=CameraSpec(movement="跟随", shot_size="medium", position="front", speed="medium"),
            first_frame_ref=FrameRef(source="to_generate", generation_hint="鲁班挥锤起手"),
            last_frame_ref=FrameRef(source="to_generate", generation_hint="桥拱初现"),
            style_pack_id="2d-guofeng",
            risk_level="medium",
            notes="Character-introduction shot for Luban.",
        ),
        Shot(
            shot_id="shot-03",
            beat_id="beat-03",
            duration_seconds=12,
            description="天明后赵州桥完整亮相，百姓试走过桥，鲁班抚桥看着通途。",
            involved_asset_ids=["luban", "zhaozhou-bridge"],
            camera=CameraSpec(movement="缓推", shot_size="wide", position="front", speed="slow"),
            first_frame_ref=FrameRef(source="asset", asset_id="zhaozhou-bridge"),
            last_frame_ref=FrameRef(source="to_generate", generation_hint="桥成通途的喜悦定格"),
            style_pack_id="2d-guofeng",
            risk_level="medium",
            notes="First full reveal of the bridge asset.",
        ),
        Shot(
            shot_id="shot-04",
            beat_id="beat-04",
            duration_seconds=12,
            description="云层裂开，张果老倒骑白驴现身，从高处俯看赵州桥。",
            involved_asset_ids=["zhangguolao", "zhaozhou-bridge"],
            camera=CameraSpec(movement="缓推", shot_size="wide", position="high", speed="slow"),
            first_frame_ref=FrameRef(source="asset", asset_id="zhangguolao"),
            last_frame_ref=FrameRef(source="to_generate", generation_hint="张果老落桥前的云端末帧"),
            style_pack_id="2d-guofeng",
            risk_level="medium",
            notes="Cloud reveal with a readable Zhang Guolao anchor.",
        ),
        Shot(
            shot_id="shot-05",
            beat_id="beat-05",
            duration_seconds=16,
            description="柴王爷推独轮车同张果老一起落在桥头，鲁班拱手相迎，赵州桥承接两股神力。",
            involved_asset_ids=["luban", "zhangguolao", "chaiwangye", "zhaozhou-bridge"],
            camera=CameraSpec(movement="缓推", shot_size="medium", position="front", speed="slow"),
            first_frame_ref=FrameRef(source="asset", asset_id="chaiwangye"),
            last_frame_ref=FrameRef(source="to_generate", generation_hint="桥头对峙的压迫感收帧"),
            style_pack_id="2d-guofeng",
            risk_level="medium",
            notes="Bridge all key characters into one shot.",
        ),
        Shot(
            shot_id="shot-06",
            beat_id="beat-06",
            duration_seconds=16,
            description="张果老倒骑白驴踏上赵州桥，驴蹄落处桥板微沉，褡裢金光渗出。",
            involved_asset_ids=["zhangguolao", "zhaozhou-bridge"],
            camera=CameraSpec(movement="跟随", shot_size="medium", position="low", speed="medium"),
            first_frame_ref=FrameRef(source="asset", asset_id="zhangguolao"),
            last_frame_ref=FrameRef(source="to_generate", generation_hint="白驴踏桥后桥面受压的末帧"),
            style_pack_id="2d-guofeng",
            risk_level="medium",
            notes="Pressure begins.",
        ),
        Shot(
            shot_id="shot-07",
            beat_id="beat-07",
            duration_seconds=16,
            description="柴王爷推独轮车上桥，车轮碾石发出闷响，赵州桥开始吃力，百姓神色由喜转忧。",
            involved_asset_ids=["chaiwangye", "zhaozhou-bridge"],
            camera=CameraSpec(movement="跟随", shot_size="medium", position="side", speed="medium"),
            first_frame_ref=FrameRef(source="asset", asset_id="chaiwangye"),
            last_frame_ref=FrameRef(source="to_generate", generation_hint="车轮压桥后的忧色定格"),
            style_pack_id="2d-guofeng",
            risk_level="medium",
            notes="Escalate pressure with the wheelbarrow weight.",
        ),
        Shot(
            shot_id="shot-08",
            beat_id="beat-08",
            duration_seconds=14,
            description="桥心下沉，石缝开裂，赵州桥栏板震动，河水翻涌，百姓惊呼后退。",
            involved_asset_ids=["zhaozhou-bridge"],
            camera=CameraSpec(movement="俯冲", shot_size="wide", position="high", speed="fast"),
            first_frame_ref=FrameRef(source="asset", asset_id="zhaozhou-bridge"),
            last_frame_ref=FrameRef(source="to_generate", generation_hint="桥心惊变后的混乱末帧"),
            style_pack_id="2d-guofeng",
            risk_level="high",
            notes="The bridge must look unstable but not fully broken.",
        ),
        Shot(
            shot_id="shot-09",
            beat_id="beat-09",
            duration_seconds=22,
            description="鲁班跃入河中，以双臂托住赵州桥桥腹，他的身躯和石桥正面相抗。",
            involved_asset_ids=["luban", "zhaozhou-bridge"],
            camera=CameraSpec(movement="俯冲", shot_size="wide", position="low", speed="fast"),
            first_frame_ref=FrameRef(source="asset", asset_id="luban"),
            last_frame_ref=FrameRef(source="to_generate", generation_hint="鲁班托桥定住下坠的英雄末帧"),
            style_pack_id="2d-guofeng",
            risk_level="high",
            notes="Core climax shot.",
        ),
        Shot(
            shot_id="shot-10",
            beat_id="beat-10",
            duration_seconds=16,
            description="掌印、膝痕、车沟、圆坑与蹄印烙进赵州桥石面，仙迹被瞬间定格。",
            involved_asset_ids=["zhangguolao", "chaiwangye", "zhaozhou-bridge"],
            camera=CameraSpec(movement="定镜", shot_size="close", position="front", speed="slow"),
            first_frame_ref=FrameRef(source="asset", asset_id="zhaozhou-bridge"),
            last_frame_ref=FrameRef(source="to_generate", generation_hint="仙迹连成镜头链的末帧"),
            style_pack_id="2d-guofeng",
            risk_level="high",
            notes="Detail montage of bridge marks.",
        ),
        Shot(
            shot_id="shot-11",
            beat_id="beat-11",
            duration_seconds=16,
            description="赵州桥重新稳住，张果老与柴王爷下桥拱手，百姓在桥头欢腾。",
            involved_asset_ids=["zhangguolao", "chaiwangye", "zhaozhou-bridge"],
            camera=CameraSpec(movement="拉远", shot_size="wide", position="front", speed="slow"),
            first_frame_ref=FrameRef(source="asset", asset_id="zhaozhou-bridge"),
            last_frame_ref=FrameRef(source="to_generate", generation_hint="二仙行礼与群像欢腾的末帧"),
            style_pack_id="2d-guofeng",
            risk_level="medium",
            notes="Release after the climax.",
        ),
        Shot(
            shot_id="shot-12",
            beat_id="beat-12",
            duration_seconds=16,
            description="鲁班湿衣上岸，回望赵州桥浅笑，镜头最后停在桥上仙迹与长虹卧波。",
            involved_asset_ids=["luban", "zhaozhou-bridge"],
            camera=CameraSpec(movement="拉远", shot_size="wide", position="front", speed="slow"),
            first_frame_ref=FrameRef(source="asset", asset_id="luban"),
            last_frame_ref=FrameRef(source="asset", asset_id="zhaozhou-bridge"),
            style_pack_id="2d-guofeng",
            risk_level="medium",
            notes="Closing hero image.",
        ),
    ]
    return StoryboardPackage(
        total_duration_seconds=sum(shot.duration_seconds for shot in shots),
        shots=shots,
        continuity_notes=[
            "赵州桥桥拱与桥腹比例不可漂移。",
            "鲁班、张果老、柴王爷的识别锚点必须跨镜稳定。",
        ],
        first_test_shot_ids=["shot-03", "shot-09", "shot-10", "shot-12"],
    )


def write_json(path: Path, payload) -> None:
    """Write a JSON file with UTF-8 and indentation."""

    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    """Build the example storyboard and compiled render requests."""

    brief = build_brief()
    storyboard = build_storyboard()
    library = AssetLibrary(ASSET_ROOT).load()
    render_requests = compile_all_shots(storyboard, library, EXAMPLE_PROFILE, brief)

    write_json(EXAMPLE_ROOT / "storyboard.json", storyboard.model_dump(mode="json"))
    write_json(
        EXAMPLE_ROOT / "shot-render-requests.json",
        [request.model_dump(mode="json") for request in render_requests],
    )
    print("Generated storyboard.json and shot-render-requests.json")


if __name__ == "__main__":
    main()
