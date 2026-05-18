# Corebook Sync Map

Use this file as the short navigation layer for publication sync runs.

## Primary workflow docs

- `docs/workflows/workflow-execution.md`
  - run ownership, checkpoints, routing, and closure
- `docs/workflows/core-sync-workflow.md`
  - main workflow for publication synchronization

## Secondary workflow docs

- `docs/workflows/technique-workflow.md`
  - when publication work depends on a Technique still being closed
- `docs/workflows/authority-revision-workflow.md`
  - when the rule itself is not stable enough to publish
- `docs/workflows/dependency-review-workflow.md`
  - when the sync crosses chapter or subsystem boundaries
- `docs/workflows/species-audit-workflow.md`
  - when the sync belongs to a broader species pass

## Core source clusters

- `Transcendence-design/docs/system/`
- `Transcendence-design/data/system/`
- `Transcendence-design/docs/knowledge/`
- `Transcendence-design/data/knowledge/`
- `Transcendence-publications/`

## Common routing patterns

- authority stable + section mapping clear -> stay in core-sync
- authority unstable -> route to `authority-revision-workflow`
- Technique closure incomplete -> route to `technique-workflow`
- cross-chapter dependency ambiguity -> route to `dependency-review-workflow`
- broader species pass -> return to or coordinate with `species-audit-workflow`
