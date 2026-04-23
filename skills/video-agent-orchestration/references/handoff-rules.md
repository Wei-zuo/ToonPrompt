# Handoff Rules

## Producer -> Screenwriter

- Freeze the brief first.
- If premise is loose, use one-line development before treatment.
- If source material already exists, adapt it instead of replacing it.

## Screenwriter -> Producer

- `StoryPackage.characters` must be complete enough for the producer to bootstrap stub `character` assets.
- If a location, prop, or style pack is structurally required, call it out explicitly instead of leaving art to guess.

## Screenwriter -> Art Design

- Story package must reveal what needs to be seen, not only what needs to be said.
- Character goals and visual motifs must be clear enough for art direction.
- If the story promise depends on a literal visual gag, recognition reveal, or strong contrast, art design cannot silently downgrade it into abstract texture, soft mood, or vague atmosphere.

## Producer -> Art Design

- Producer owns stub asset creation.
- Art design should receive a readable `AssetLibrary` baseline before planning prompts.

## Art Design -> Image Production

- Art design hands off `ArtGenerationPlan.asset_jobs`.
- Each job must already contain prompt, negative prompt, target id, aspect ratio, and style-pack context.

## Image Production -> Assistant Director

- Pending asset-image jobs must be empty before AD cuts shots.
- Generated images must already be written back to `AssetLibrary.reference_image_paths`.

## Art Design -> Assistant Director

- Main character anchors, costume structure, set structure, and palette must be readable.
- Prompt blocks are helpful, but the art package must also function as a visual rules document.
- Assistant director must explicitly check whether the promised hook still reads on first watch.
- If the brief says `好笑`, `反差`, or `一眼识别`, and the art package weakens that readability, AD should reject or send back with blocker notes instead of approving with soft notes.

## Assistant Director -> Image Production

- Storyboard is not enough by itself.
- AD must also hand off first / last frame generation specs as `ImageJob[]`.

## Assistant Director -> Producer

- AD must say what is risky, what is missing, what should be tested first, and which upstream owner must revise.

## Producer -> Video Production

- Video production only receives the packet after `ShotRenderRequest[]` are compiled.
- If `production_packet` or `pending_video_jobs` are incomplete, production does not start.

## Rework Routing

- story issue -> screenwriter
- visual identity issue -> art design
- asset-image generation failure -> art design, with producer copied
- first / last frame generation failure -> assistant director, with producer copied
- execution readability issue -> assistant director
- model or run instability -> video production
- hook readability or joke-strength mismatch -> art design, with producer copied
- model or run instability -> video production
- story promise versus visual execution mismatch -> producer routes jointly to screenwriter and art design
