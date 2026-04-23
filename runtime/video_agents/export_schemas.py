from __future__ import annotations

import json
from pathlib import Path

from .schemas import AdFeedback, ArtPackage, ProductionPacket, ProjectBrief, StoryPackage, StoryboardPackage


SCHEMA_MODELS = {
    "project_brief.schema.json": ProjectBrief,
    "story_package.schema.json": StoryPackage,
    "art_package.schema.json": ArtPackage,
    "storyboard_package.schema.json": StoryboardPackage,
    "ad_feedback.schema.json": AdFeedback,
    "production_packet.schema.json": ProductionPacket,
}


def export_schemas(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for filename, model in SCHEMA_MODELS.items():
        schema = model.model_json_schema()
        (output_dir / filename).write_text(
            json.dumps(schema, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )


def main() -> None:
    export_schemas(Path("schemas"))


if __name__ == "__main__":
    main()
