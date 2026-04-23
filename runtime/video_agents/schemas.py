from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class InputRoute(str, Enum):
    NEW_BRIEF = "new_brief"
    EXISTING_SCRIPT = "existing_script"
    ADAPTATION = "adaptation"
    PRODUCTION_RESCUE = "production_rescue"


class ProjectBrief(StrictModel):
    project_id: str
    route: InputRoute
    title: str
    goal: str
    format: str
    target_duration_seconds: int = Field(ge=1)
    language: str
    target_audience: list[str] = Field(default_factory=list)
    source_materials: list[str] = Field(default_factory=list)
    required_elements: list[str] = Field(default_factory=list)
    forbidden_drift: list[str] = Field(default_factory=list)
    delivery_scope: str


class CharacterCard(StrictModel):
    character_id: str
    name: str
    dramatic_function: str
    visual_hooks: list[str] = Field(default_factory=list)


class StoryBeat(StrictModel):
    beat_id: str
    label: str
    purpose: str
    duration_seconds: int = Field(ge=1)


class SceneSpec(StrictModel):
    scene_id: str
    title: str
    location: str
    time_of_day: str
    summary: str
    involved_characters: list[str] = Field(default_factory=list)
    target_shot_count: int = Field(ge=1)


class StoryPackage(StrictModel):
    title: str
    logline: str
    adaptation_goal: str
    characters: list[CharacterCard] = Field(default_factory=list)
    scenes: list[SceneSpec] = Field(default_factory=list)
    beats: list[StoryBeat] = Field(default_factory=list)
    total_shots: int = Field(ge=1)
    narration_style: str
    dialogue_constraints: list[str] = Field(default_factory=list)


class VisualAnchor(StrictModel):
    subject_id: str
    silhouette: str
    wardrobe: str
    materials: list[str] = Field(default_factory=list)
    props: list[str] = Field(default_factory=list)
    palette: list[str] = Field(default_factory=list)


class EnvironmentDesign(StrictModel):
    environment_id: str
    summary: str
    structure_constraints: list[str] = Field(default_factory=list)
    lighting_notes: list[str] = Field(default_factory=list)
    palette: list[str] = Field(default_factory=list)


class PromptBlock(StrictModel):
    target: str
    positive_prompt: str
    negative_prompt: list[str] = Field(default_factory=list)
    model_notes: list[str] = Field(default_factory=list)


class ArtPackage(StrictModel):
    style_name: str
    medium: str
    global_constraints: list[str] = Field(default_factory=list)
    character_anchors: list[VisualAnchor] = Field(default_factory=list)
    environments: list[EnvironmentDesign] = Field(default_factory=list)
    prompt_blocks: list[PromptBlock] = Field(default_factory=list)


class ShotFraming(str, Enum):
    ESTABLISHING = "establishing"
    WIDE = "wide"
    MEDIUM = "medium"
    CLOSE_UP = "close_up"
    INSERT = "insert"


class ShotSpec(StrictModel):
    shot_id: str
    scene_id: str
    order: int = Field(ge=1)
    duration_seconds: int = Field(ge=1)
    framing: ShotFraming
    camera_move: str
    action: str
    characters: list[str] = Field(default_factory=list)
    art_dependencies: list[str] = Field(default_factory=list)
    risk_level: int = Field(ge=1, le=3)


class StoryboardPackage(StrictModel):
    total_duration_seconds: int = Field(ge=1)
    shots: list[ShotSpec] = Field(default_factory=list)
    continuity_notes: list[str] = Field(default_factory=list)
    first_test_shots: list[str] = Field(default_factory=list)


class RevisionTarget(str, Enum):
    SCREENWRITER = "screenwriter"
    ART_DESIGN = "art_design"
    ASSISTANT_DIRECTOR = "assistant_director"


class ReviewDecision(str, Enum):
    APPROVED = "approved"
    REVISE_STORY = "revise_story"
    REVISE_ART = "revise_art"
    REVISE_STORYBOARD = "revise_storyboard"
    BLOCKED = "blocked"


class RevisionRequest(StrictModel):
    target: RevisionTarget
    reason: str
    blocking_issues: list[str] = Field(default_factory=list)
    requested_changes: list[str] = Field(default_factory=list)
    retry_budget: int = Field(ge=0, default=0)


class AdFeedback(StrictModel):
    decision: ReviewDecision
    summary: str
    blocking_issues: list[str] = Field(default_factory=list)
    high_risk_shots: list[str] = Field(default_factory=list)
    revision_request: RevisionRequest | None = None


class PriorityLevel(str, Enum):
    P0 = "P0"
    P1 = "P1"
    P2 = "P2"


class ProductionTodoItem(StrictModel):
    item_id: str
    priority: PriorityLevel
    owner_role: str
    description: str
    depends_on: list[str] = Field(default_factory=list)
    success_criteria: list[str] = Field(default_factory=list)


class ProductionPacket(StrictModel):
    brief: ProjectBrief
    story: StoryPackage
    art: ArtPackage
    storyboard: StoryboardPackage
    locked_constraints: list[str] = Field(default_factory=list)
    first_test_shots: list[str] = Field(default_factory=list)
    todo_items: list[ProductionTodoItem] = Field(default_factory=list)
