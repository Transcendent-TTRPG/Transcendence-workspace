# Technique Work Run

## Header

- `work_id`: `2026-05-17-naghii-recuperar-la-distancia`
- `owner_workflow`: `technique-workflow`
- `linked_workflows`:
  - `technique-play-surface-workflow`
  - `simulation-port-workflow`
  - `authority-revision-workflow`
- `artifact_type`: `technique`
- `status`: `closed_partial`

## Scope

- `species`: `naghii`
- `technique_id`: `recuperar_la_distancia`
- `goal`: `Run one real Naghii Technique through authority cleanup, final play surface, and simulator porting.`
- `current_state`: `Authored in authority, not yet present in final core/card surface, not yet defined in simulator.`
- `out_of_scope`:
  - `question-ready experiment coverage`
  - `new Naghii policy support`
  - `retroactive cleanup of older Cerrar la Línea pilot mismatches`

## Mandatory sources

- authority docs:
  - `Transcendence-design/docs/system/techniques.md`
- authority data:
  - `Transcendence-design/data/system/techniques.yaml`
- seeds/canon:
  - `Transcendence-design/docs/system/weapon-technique-profiles.md`
- knowledge references:
  - `docs/workflows/technique-workflow.md`
  - `docs/workflows/technique-play-surface-workflow.md`
  - `docs/workflows/simulation-port-workflow.md`
- simulation references if relevant:
  - `Transcendence-design/sim/ARCHITECTURE.md`
  - `Transcendence-design/sim/DATA-SCHEMAS.md`
  - `Transcendence-design/sim/TECHNIQUE-PORTING-PLAN.md`
- publication references if relevant:
  - `Transcendence-design/docs/system/technique-play-surface.md`
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/`
  - `Transcendence-publications/technique-cards/transcendence-technique-cards/`

## Phase checkpoints

### Phase 0. Intake
- `scope_recorded`: `yes`
- `main_question`: `Can one Naghii Technique now move cleanly from authority into final play surfaces and simulator coverage without ad hoc interpretation?`

### Phase 1. Species Framing
- `fantasy`: `Drive the point forward to reclaim safe spear distance before close pressure settles.`
- `world_origin`: `Naghii archive guard range discipline treats correct distance as interpretive authority rather than mere reach advantage.`
- `why_not_base_action`: `The Technique does not merely strike; it bundles the thrust with a committed distance-recovery step.`
- `interaction_surfaces`:
  - `position`
  - `lane state`
  - `pressure reset`

### Phase 2. Mechanical Framing
- `category`: `attack`
- `roll_model`: `A.R. leading into standard weapon exchange and I.R. payload on success`
- `competency_source`: `Spear`
- `effect_model`: `successful weapon exchange plus one-meter post-hit reposition away from close pressure`
- `duration_model`: `instant`
- `restrictions`:
  - `requires a weapon with Perforation access`
  - `requires credible room to recover the line`
  - `does not create broad lane denial by itself`

### Phase 3. Dependency Framing
- `upstream_dependencies`:
  - `Spear / Perforation authority`
  - `weapon exchange runtime`
  - `post-hit reposition effect support`
- `downstream_dependencies`:
  - `core technique entry`
  - `tarot card entry`
  - `sim technique definition`
- `blockers`: `none after authority cost cleanup`
- `linked_files`:
  - `Transcendence-design/docs/system/techniques.md`
  - `Transcendence-design/data/system/techniques.yaml`
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/03-recuperar-la-distancia.md`
  - `Transcendence-publications/technique-cards/transcendence-technique-cards/cards/es/naghii/recuperar-la-distancia.html`
  - `Transcendence-design/sim/data/techniques/naghii.yaml`
  - `Transcendence-design/sim/engine/activations.py`

### Phase 4. Balance Framing
- `cost_sanity_note`: `Authority drift existed: prose and md anchor at Rhythm 5 / Attrition 1, yaml data had Rhythm 4 / Attrition 1. Corrected to 5 / 1.`
- `sibling_comparison_note`: `The Technique must remain broader and costlier in tempo than Cerrar la Línea because it is active reclaiming rather than a narrow reaction window.`
- `pressure_note`: `The value is geometry recovery, not raw damage spike.`
- `counterplay_note`: `If the exchange fails, the user does not recover clean line and the target continues pressure normally.`

### Phase 5. Simulation Framing
- `runtime_gap_classification`: `small_runtime_extension`
- `porting_state_target`: `runtime_supported`
- `scenario_seed_note`: `Validated through a focused activation test with a minimal Naghii profile, not yet through a saved Naghii scenario file.`
- `question_seed_note`: `No saved Naghii question yet.`

### Phase 6. Editorial Framing
- `authority_cleanup_note`: `Authority kept the full explanatory payload; final play surface keeps only player-facing fields.`
- `terminology_note`: `Final surface uses Perforación, not improvised line-control language, for this Technique.`
- `core_sync_note`: `Core entry and tarot card created together from the same semantic payload.`

## Integration

- `files_changed`:
  - `Transcendence-design/docs/system/techniques.md`
  - `Transcendence-design/data/system/techniques.yaml`
  - `Transcendence-design/sim/data/techniques/naghii.yaml`
  - `Transcendence-design/sim/data/species/naghii_profiles.yaml`
  - `Transcendence-design/sim/loaders/definitions.py`
  - `Transcendence-design/sim/engine/activations.py`
  - `Transcendence-design/sim/tests/test_definition_loaders.py`
  - `Transcendence-design/sim/tests/test_activations_runtime.py`
  - `Transcendence-design/sim/TECHNIQUE-PORTING-PLAN.md`
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/README.md`
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/03-recuperar-la-distancia.md`
  - `Transcendence-publications/technique-cards/transcendence-technique-cards/cards/es/naghii/recuperar-la-distancia.html`
  - `Transcendence-publications/technique-cards/transcendence-technique-cards/index.html`
- `sim_updated`: `yes`
- `core_updated`: `yes`
- `knowledge_updated`: `coverage plan updated`

## Validation

- `doctrinal_review_done`: `yes`
- `loader_validation_done`: `yes`
- `runtime_validation_done`: `yes`
- `scenario_test_done`: `focused activation test only`
- `question_test_done`: `no`

## Acceptance closure

- `authority_updated`: `yes`
- `yaml_updated`: `yes`
- `sim_defined_or_gap_classified`: `yes`
- `runtime_supported_or_gap_classified`: `runtime_supported after small extension`
- `coverage_updated`: `yes`
- `core_sync_done_or_not_needed`: `done through play-surface run`
- `pending_items_explicit`: `yes`

## Pending items

- `pending`:
  - `No Naghii-specific policy exercises Recuperar la Distancia yet.`
  - `No saved Naghii scenario or question exists yet for repeatable analysis.`
  - `Cerrar la Línea still has an older pilot surface mismatch that should be reviewed in a separate run.`

## Change impact

- `concepts_touched`:
  - `Perforation final play surface`
  - `active distance recovery`
  - `post-hit reposition`
  - `multi-file technique loading`
- `decisions_reinforced_or_created`:
  - `Naghii play surface should preserve weapon-profile truth from authority.`
  - `Technique play surface and simulator port can be run together under one owned technique pass when authority is stable.`
- `coverage_movement`:
  - `Naghii: sim_defined 0 -> 1`
  - `Naghii: runtime_supported 0 -> 1`
- `follow_up_work`:
  - `create first Naghii question/scenario pair`
  - `add Naghii policy support`
  - `review earlier Cerrar la Línea pilot surface for authority alignment`
