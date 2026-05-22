# Technique Work Run

## Header

- `work_id`: `2026-05-18-naghii-anudar-el-paso`
- `owner_workflow`: `technique-workflow`
- `linked_workflows`:
  - `technique-play-surface-workflow`
  - `simulation-port-workflow`
- `artifact_type`: `technique`
- `status`: `closed_partial`

## Scope

- `species`: `naghii`
- `technique_id`: `anudar_el_paso`
- `goal`: `Run the fourth early Naghii Technique through final play surface and simulator definition.`
- `current_state`: `Authored in authority, not yet surfaced in core/card, not yet present in simulator.`
- `out_of_scope`:
  - `full runtime support for reactive anti-disengagement denial`
  - `question-ready experiment coverage`
  - `policy support`

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

## Phase checkpoints

### Phase 0. Intake
- `scope_recorded`: `yes`
- `main_question`: `Can Anudar el Paso be closed in final play surface now while being represented honestly in simulator coverage without pretending anti-disengagement runtime already exists?`

### Phase 1. Species Framing
- `fantasy`: `Stored curved threat catches a clean exit before separation completes.`
- `world_origin`: `Naghii temple guard torsion drills punish premature withdrawal or angle improvement from contested contact.`
- `why_not_base_action`: `The Technique is not generic flexible-weapon offense; it exists to deny clean separation once the target is already inside profile-bearing reach.`
- `interaction_surfaces`:
  - `counter_positioning`
  - `anti_disengagement`
  - `setup_denial`

### Phase 2. Mechanical Framing
- `category`: `utility`
- `roll_model`: `reactive specialization check through Flexible Weapons`
- `competency_source`: `Flexible Weapons`
- `effect_model`: `deny clean withdrawal, clean flank, or superior angle on a successful catch`
- `duration_model`: `instant`
- `restrictions`:
  - `requires Torsion access`
  - `only applies after target is already inside profile-bearing reach`
  - `does not create full immobilization by itself`

### Phase 3. Dependency Framing
- `upstream_dependencies`:
  - `Flexible Weapons / Torsion authority`
  - `reactive contested-position logic`
  - `clean-separation denial semantics`
- `downstream_dependencies`:
  - `core technique entry`
  - `tarot card entry`
  - `sim technique definition`
  - `seed Naghii torsion profile`
- `blockers`: `runtime does not yet model anti-disengagement reaction windows or contested-position denial as a resolved surface`

### Phase 4. Balance Framing
- `cost_sanity_note`: `Rhythm 4 / Attrition 1 stays coherent because the Technique is narrow, reactive, and utility-oriented rather than damage-bearing.`
- `sibling_comparison_note`: `Unlike Cerrar la Línea, this does not stop entry; it denies clean withdrawal or angle improvement after entry.`
- `pressure_note`: `Its payoff is positional denial, not impact.`
- `counterplay_note`: `If the reactive check fails, the enemy completes the movement normally.`

### Phase 5. Simulation Framing
- `runtime_gap_classification`: `new_state_family`
- `porting_state_target`: `sim_defined`
- `scenario_seed_note`: `No runtime scenario yet because the anti-disengagement window is not implemented.`
- `question_seed_note`: `No saved Naghii question yet.`

### Phase 6. Editorial Framing
- `authority_cleanup_note`: `Authority remained stable; final surface compresses to player-facing wording and keeps only real game gates.`
- `terminology_note`: `Final surface uses Torsion and treats the check as S.R. on the player-facing side.`
- `core_sync_note`: `Core and card were created together from the same semantic payload.`

## Integration

- `files_changed`:
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/05-anudar-el-paso.md`
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/README.md`
  - `Transcendence-publications/technique-cards/transcendence-technique-cards/cards/es/naghii/anudar-el-paso.html`
  - `Transcendence-publications/technique-cards/transcendence-technique-cards/index.html`
  - `Transcendence-design/sim/data/techniques/naghii.yaml`
  - `Transcendence-design/sim/data/species/naghii_profiles.yaml`
  - `Transcendence-design/sim/tests/test_definition_loaders.py`
  - `Transcendence-design/sim/TECHNIQUE-PORTING-PLAN.md`
- `sim_updated`: `yes`
- `core_updated`: `yes`
- `knowledge_updated`: `coverage plan updated`

## Validation

- `roll_integrity`: `pass`
- `surface_integrity`: `pass`
- `exchange_integrity`: `not_applicable`
- `ailment_integrity`: `not_applicable`
- `critical_break_integrity`: `not_applicable`
- `atb_integrity`: `blocked`
- `dependency_integrity`: `pass`
- `simulation_integrity`: `blocked`
- `balance_sanity`: `pass`
- `loader_validation`: `pending`
- `scenario_validation`: `blocked`
- `question_validation`: `not_applicable`
- `publication_consistency`: `pass`

## Acceptance closure

- `authority_updated`: `not_needed`
- `yaml_updated`: `not_needed`
- `sim_defined_or_gap_classified`: `yes`
- `runtime_supported_or_gap_classified`: `gap classified`
- `coverage_updated`: `yes`
- `core_sync_done_or_not_needed`: `done through play-surface run`
- `pending_items_explicit`: `yes`

## Pending items

- `pending`:
  - `Add a real anti-disengagement reactive window to runtime.`
  - `Model contested-position / clean-separation denial explicitly.`
  - `Add Naghii policy, scenario, and question coverage for torsion play.`

## Change impact

- `concepts_touched`:
  - `Torsion play surface`
  - `reactive utility final surface`
  - `anti_disengagement simulator backlog`
- `decisions_reinforced_or_created`:
  - `Utility techniques can surface an S.R.-style specialization check without inventing attack payload.`
  - `Simulator coverage may stop honestly at sim_defined when runtime support is not yet real.`
- `coverage_movement`:
  - `Naghii: sim_defined 3 -> 4`
  - `Naghii: runtime_supported 2 -> 2`
- `follow_up_work`:
  - `Implement anti-disengagement reactive window support`
