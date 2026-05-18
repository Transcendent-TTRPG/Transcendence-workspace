# Species Audit Map

Use this file as the short navigation layer for species pass audits.

## Primary workflow docs

- `docs/workflows/workflow-execution.md`
  - run ownership, checkpointing, routing, and closure
- `docs/workflows/species-audit-workflow.md`
  - the main workflow for species-wide audit work
- `docs/workcards/species-audit-workcard-template.md`
  - the structure for a species audit run

## Secondary workflow docs

- `docs/workflows/technique-workflow.md`
  - when an audit routes into one Technique fix
- `docs/workflows/simulation-port-workflow.md`
  - when an audit routes into simulator coverage work
- `docs/workflows/balance-review-workflow.md`
  - when the audit exposes cost or pressure concerns
- `docs/workflows/dependency-review-workflow.md`
  - when repeated blockers cross subsystem boundaries
- `docs/workflows/core-sync-workflow.md`
  - when publication drift is part of the audit
- `docs/workflows/authority-revision-workflow.md`
  - when a species-local issue is actually upstream doctrine

## Common source clusters

- `Transcendence-design/docs/system/`
- `Transcendence-design/data/system/`
- `Transcendence-design/docs/knowledge/`
- `Transcendence-design/data/knowledge/`
- `Transcendence-design/sim/`
- `Transcendence-publications/`

## Common routing patterns

- inventory + identity only -> stay in species-audit
- local Technique issue -> route to `technique-workflow`
- local sim gap -> route to `simulation-port-workflow`
- repeated cost concern -> route to `balance-review-workflow`
- upstream subsystem ambiguity -> route to `dependency-review-workflow` or `authority-revision-workflow`
- publication drift -> route to `core-sync-workflow`
