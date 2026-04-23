from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import TypedDict

from pydantic import Field

from .schemas import AdFeedback, ArtPackage, ProductionPacket, ProjectBrief, RevisionRequest, StoryboardPackage, StoryPackage, StrictModel


class WorkflowPhase(str, Enum):
    PRODUCER_INTAKE = "producer_intake"
    SCREENWRITER = "screenwriter"
    ART_DESIGN = "art_design"
    ASSISTANT_DIRECTOR = "assistant_director"
    PRODUCER_INTEGRATION = "producer_integration"
    PRODUCTION = "production"
    DONE = "done"
    FAILED = "failed"


class RevisionCounter(StrictModel):
    screenwriter: int = 0
    art_design: int = 0
    assistant_director: int = 0

    def total(self) -> int:
        return self.screenwriter + self.art_design + self.assistant_director


class RevisionLimits(StrictModel):
    screenwriter: int = 2
    art_design: int = 2
    assistant_director: int = 1
    total: int = 5


class AuditEntry(StrictModel):
    phase: WorkflowPhase
    event: str
    detail: str
    timestamp: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class VideoAgentState(TypedDict, total=False):
    phase: WorkflowPhase
    should_run_production: bool
    brief: ProjectBrief
    story_package: StoryPackage
    art_package: ArtPackage
    storyboard: StoryboardPackage
    ad_feedback: AdFeedback
    production_packet: ProductionPacket
    active_revision: RevisionRequest | None
    revision_counts: RevisionCounter
    revision_limits: RevisionLimits
    stop_reason: str | None
    audit_log: list[AuditEntry]
