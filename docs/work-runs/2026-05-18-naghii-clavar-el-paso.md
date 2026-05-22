# Technique Work Run

## Header

- `work_id`: `2026-05-18-naghii-clavar-el-paso`
- `owner_workflow`: `technique-workflow`
- `linked_workflows`:
  - `technique-play-surface-workflow`
  - `simulation-port-workflow`
- `artifact_type`: `technique`
- `status`: `closed_partial`

## Scope

- `species`: `naghii`
- `technique_id`: `clavar_el_paso`
- `goal`: `Run the third early Naghii spear Technique through final play surface and simulator support.`
- `current_state`: `Authored in authority, not yet surfaced in core/card, not yet present in simulator.`
- `out_of_scope`:
  - `question-ready experiment coverage`
  - `full Naghii policy exercise`

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
- `main_question`: `Can the simulator support a committed 2-meter close-and-strike spear action without inventing fuzzy timing or fake requirements in the final surface?`

### Phase 1. Species Framing
- `fantasy`: `When waiting becomes more dangerous than commitment, the step and the thrust arrive as one decision.`
- `world_origin`: `Naghii Kha enforcement and breach-response drills collapse interval into committed forward pressure.`
- `why_not_base_action`: `The Technique is not a standard spear attack because it compresses up to 2 meters of close plus the attack into one action.`
- `interaction_surfaces`:
  - `range`
  - `position`
  - `timing`

### Phase 2. Mechanical Framing
- `category`: `attack`
- `roll_model`: `A.R. into standard weapon exchange and I.R. payload`
- `competency_source`: `Spear`
- `effect_model`: `advance up to 2 meters before exchange, then strike from the new position`
- `duration_model`: `instant`
- `restrictions`:
  - `requires Perforation access`
  - `should leave the user committed forward`
  - `does not become broad zone control`

### Phase 3. Dependency Framing
- `upstream_dependencies`:
  - `Spear / Perforation authority`
  - `weapon exchange runtime`
  - `pre-exchange advance effect support`
- `downstream_dependencies`:
  - `core technique entry`
  - `tarot card entry`
  - `sim technique definition`
- `blockers`: `none`
- `linked_files`:
  - `Transcendence-design/sim/data/techniques/naghii.yaml`
  - `Transcendence-design/sim/engine/activations.py`
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/04-clavar-el-paso.md`
  - `Transcendence-publications/technique-cards/transcendence-technique-cards/cards/es/naghii/clavar-el-paso.html`

### Phase 4. Balance Framing
- `cost_sanity_note`: `Rhythm 5 / Attrition 2 remains coherent because the Technique compresses range closing and attack into one committed forward action.`
- `sibling_comparison_note`: `Recuperar la Distancia spends less strain to restore line after contact; Clavar el Paso spends more strain to seize line by closing before contact.`
- `pressure_note`: `Its value is disguised reach and compressed timing, not a different damage payload.`
- `counterplay_note`: `If the exchange fails, the forward commitment was still spent.`

### Phase 5. Simulation Framing
- `runtime_gap_classification`: `small_runtime_extension`
- `porting_state_target`: `runtime_supported`
- `scenario_seed_note`: `Validated through a focused Naghii activation test.`
- `question_seed_note`: `No saved Naghii question yet.`

### Phase 6. Editorial Framing
- `authority_cleanup_note`: `No authority rewrite was needed; final play surface removed contextual pseudo-requirements and kept exact quantities.`
- `terminology_note`: `Final surface preserves Perforación as the real gate.`
- `core_sync_note`: `Core and card were created together from the same payload.`

## Integration

- `files_changed`:
  - `Transcendence-design/sim/data/species/naghii_profiles.yaml`
  - `Transcendence-design/sim/data/techniques/naghii.yaml`
  - `Transcendence-design/sim/engine/activations.py`
  - `Transcendence-design/sim/tests/test_definition_loaders.py`
  - `Transcendence-design/sim/tests/test_activations_runtime.py`
  - `Transcendence-design/sim/TECHNIQUE-PORTING-PLAN.md`
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/README.md`
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/04-clavar-el-paso.md`
  - `Transcendence-publications/technique-cards/transcendence-technique-cards/cards/es/naghii/clavar-el-paso.html`
  - `Transcendence-publications/technique-cards/transcendence-technique-cards/index.html`
- `sim_updated`: `yes`
- `core_updated`: `yes`
- `knowledge_updated`: `coverage plan updated`

## Validation

- `roll_integrity`: `pass`
- `surface_integrity`: `pass`
- `exchange_integrity`: `pass`
- `ailment_integrity`: `not_applicable`
- `critical_break_integrity`: `not_applicable`
- `atb_integrity`: `pass`
- `dependency_integrity`: `pass`
- `simulation_integrity`: `pass`
- `balance_sanity`: `pass`
- `loader_validation`: `pass`
- `scenario_validation`: `pass`
- `question_validation`: `not_applicable`
- `publication_consistency`: `pass`

## Acceptance closure

- `authority_updated`: `not_needed`
- `yaml_updated`: `not_needed`
- `sim_defined_or_gap_classified`: `yes`
- `runtime_supported_or_gap_classified`: `runtime_supported after small extension`
- `coverage_updated`: `yes`
- `core_sync_done_or_not_needed`: `done through play-surface run`
- `pending_items_explicit`: `yes`

## Pending items

- `pending`:
  - `No Naghii policy selects Clavar el Paso yet.`
  - `No saved Naghii question exists yet for repeatable analysis.`

## Change impact

- `concepts_touched`:
  - `Perforation play surface`
  - `pre-exchange committed advance`
  - `compressed close-and-strike timing`
- `decisions_reinforced_or_created`:
  - `Exact movement quantities survive unchanged in the final surface.`
  - `Active-technique requirements stay limited to real game gates.`
- `coverage_movement`:
  - `Naghii: sim_defined 1 -> 2`
  - `Naghii: runtime_supported 1 -> 2`
- `follow_up_work`:
  - `Add first Naghii policy/scenario/question coverage`
