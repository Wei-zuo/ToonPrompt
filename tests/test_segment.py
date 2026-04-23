from __future__ import annotations

import pytest

from runtime.video_agents.schemas import SceneSpec, Shot, StoryBeat
from runtime.video_agents.segment import SingleBeatTooLongError, pack_segments


def _make_scene() -> list[SceneSpec]:
    return [
        SceneSpec(
            scene_id="scene-1",
            order=1,
            title="Scene",
            location="Bridge",
            time_of_day="day",
            summary="summary",
            target_shot_count=3,
        )
    ]


def _make_beats(durations: list[float]) -> list[StoryBeat]:
    return [
        StoryBeat(
            beat_id=f"beat-{index + 1}",
            scene_id="scene-1",
            order=index + 1,
            label=f"Beat {index + 1}",
            purpose="test",
            summary="summary",
            duration_seconds=duration,
        )
        for index, duration in enumerate(durations)
    ]


def test_pack_segments_raises_for_single_beat_too_long() -> None:
    beats = _make_beats([6, 18, 8])
    with pytest.raises(SingleBeatTooLongError):
        pack_segments(_make_scene(), beats, [], 15)


def test_pack_segments_returns_two_segments() -> None:
    beats = _make_beats([6, 5, 8])
    shots = [
        Shot(
            shot_id="shot-01",
            beat_id="beat-1",
            duration_seconds=6,
            description="a",
            involved_asset_ids=[],
            camera={"movement": "缓推", "shot_size": "medium", "position": "front"},
            style_pack_id="style-pack",
            risk_level="low",
            notes="",
        ),
        Shot(
            shot_id="shot-02",
            beat_id="beat-2",
            duration_seconds=5,
            description="b",
            involved_asset_ids=[],
            camera={"movement": "缓推", "shot_size": "medium", "position": "front"},
            style_pack_id="style-pack",
            risk_level="low",
            notes="",
        ),
        Shot(
            shot_id="shot-03",
            beat_id="beat-3",
            duration_seconds=8,
            description="c",
            involved_asset_ids=[],
            camera={"movement": "缓推", "shot_size": "medium", "position": "front"},
            style_pack_id="style-pack",
            risk_level="low",
            notes="",
        ),
    ]
    segments = pack_segments(_make_scene(), beats, shots, 15)
    assert len(segments) == 2
    assert segments[0].beat_ids == ["beat-1", "beat-2"]
    assert segments[1].beat_ids == ["beat-3"]
