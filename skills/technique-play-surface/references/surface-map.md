# Technique Play Surface Map

Use this file as the first routing layer for final play-surface work.

## Primary workflow docs

- `docs/workflows/workflow-execution.md`
  - run ownership, checkpoints, routing, and closure
- `docs/workflows/technique-play-surface-workflow.md`
  - main workflow for converting authority into core/card play surfaces

## Supporting docs

- `Transcendence-design/docs/system/technique-play-surface.md`
  - the canonical final play-facing structure and compression rules
- `docs/workflows/technique-workflow.md`
  - when authority itself still needs work
- `docs/workflows/core-sync-workflow.md`
  - when the issue is publication drift rather than first-time surface creation
- `docs/workflows/authority-revision-workflow.md`
  - when authority is too unstable to surface safely
- `docs/workflows/dependency-review-workflow.md`
  - when the Technique depends on another unresolved subsystem

## Authority sources required before surfacing

- `Transcendence-design/docs/system/specialization-technique-domains.md`
  - Defines the authoring boundary for each specialization's derived Techniques. A surface run must verify the technique's effect fits its specialization's valid domain before finalizing. Techniques transfer underlying capabilities — they do not upgrade the base skill, and they do not give bonuses to other specializations without domain justification.

## Surface targets

- `Transcendence-publications/core-books/transcendence-techniques/es/`
- `Transcendence-publications/technique-cards/transcendence-technique-cards/`

## Common routing patterns

- authority stable, no final surfaces yet -> stay in `technique-play-surface`
- authority stable, core and card need revision -> stay in `technique-play-surface`
- authority unstable -> route to `technique-workflow` or `authority-revision-workflow`
- final play surface exists but publication drift appeared later -> consider `core-sync-workflow`
