# Technique Work Run

## Header

- `work_id`: `2026-05-18-naghii-robar-el-angulo`
- `owner_workflow`: `technique-workflow`
- `linked_workflows`:
  - `technique-play-surface-workflow`
  - `simulation-port-workflow`
- `artifact_type`: `technique`
- `status`: `closed_partial`

## Scope

- `species`: `naghii`
- `technique_id`: `robar_el_angulo`
- `goal`: `Run the fifth early Naghii Technique through final play surface and simulator definition.`
- `current_state`: `Authored in authority, not yet surfaced in core/card, not yet present in simulator.`
- `out_of_scope`:
  - `full runtime support for false-line choice resolution`
  - `policy support`
  - `saved scenario or question coverage`

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

## Phase checkpoints

### Phase 0. Intake
- `scope_recorded`: `yes`
- `main_question`: `Can Robar el Ángulo be surfaced honestly now while classifying the simulator gap around combined false-line resolution instead of pretending it is already runnable?`

### Phase 1. Species Framing
- `fantasy`: `A visible line draws the answer; the real contact takes the useful angle.`
- `world_origin`: `Naghii flexible-line practice turns controlled misreading into positional theft rather than raw force.`
- `why_not_base_action`: `The Technique is not generic flexible-weapon offense; it wins by making the target answer the wrong line and then cashing that mistake into position or response spoil.`
- `interaction_surfaces`:
  - `false_read`
  - `mobility`
  - `disruption`

### Phase 2. Mechanical Framing
- `category`: `attack`
- `roll_model`: `A.R. with Flexible Weapons-facing false-line consequences`
- `competency_source`: `Flexible Weapons`
- `effect_model`: `on success, steal position and spoil immediate response together`
- `duration_model`: `until the immediate response window closes or the target re-centers`
- `restrictions`:
  - `requires Unpredictability access`
  - `target must be able to read the visible line`

### Phase 3. Dependency Framing
- `upstream_dependencies`:
  - `Flexible Weapons / Unpredictability authority`
  - `false-line choice semantics`
  - `immediate-response spoil support`
- `downstream_dependencies`:
  - `core technique entry`
  - `tarot card entry`
  - `sim technique definition`
  - `seed Naghii false-line profile`
- `blockers`: `runtime does not yet support combined false-line resolution with reposition plus immediate-response spoil`

### Phase 4. Balance Framing
- `cost_sanity_note`: `Rhythm 4 / Attrition 1 remains coherent because the Technique gives up direct damage and converts success into a bounded positional plus disruption package instead.`
- `sibling_comparison_note`: `Unlike Anudar el Paso, this is an active false-line attack rather than a reactive anti-disengagement catch.`
- `pressure_note`: `Its value is angle theft plus response spoil, not broad control or extra damage.`
- `counterplay_note`: `If the target answers the false line successfully, the consequence does not apply.`

### Phase 5. Simulation Framing
- `runtime_gap_classification`: `new_state_family`
- `porting_state_target`: `sim_defined`
- `scenario_seed_note`: `No runtime scenario yet because combined false-line consequence resolution is not implemented.`
- `question_seed_note`: `No saved Naghii question yet.`

### Phase 6. Editorial Framing
- `authority_cleanup_note`: `Authority drift on cost was corrected in docs to match yaml: Rhythm 4 / Attrition 1.`
- `terminology_note`: `Final surface localizes the profile as Impredecible in Spanish publication while preserving the authority-side family identity.`
- `core_sync_note`: `Core and card were created together from the same semantic payload.`

## Integration

- `files_changed`:
  - `Transcendence-design/docs/system/techniques.md`
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/06-robar-el-angulo.md`
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/README.md`
  - `Transcendence-publications/technique-cards/transcendence-technique-cards/cards/es/naghii/robar-el-angulo.html`
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
- `exchange_integrity`: `blocked`
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

- `authority_updated`: `yes`
- `yaml_updated`: `not_needed`
- `sim_defined_or_gap_classified`: `yes`
- `runtime_supported_or_gap_classified`: `gap classified`
- `coverage_updated`: `yes`
- `core_sync_done_or_not_needed`: `done through play-surface run`
- `pending_items_explicit`: `yes`

## Pending items

- `pending`:
  - `Implement a true false-line resolver for combined reposition plus immediate-response spoil.`
  - `Support immediate-response spoil as a real procedural runtime surface.`
  - `Add Naghii policy, scenario, and question coverage for false-line play.`

## Change impact

- `concepts_touched`:
  - `Unpredictability play surface`
  - `combined false-line consequence`
  - `choice-free simulator backlog for this technique`
- `decisions_reinforced_or_created`:
  - `Attack techniques may omit Impact when their guaranteed surface is tactical consequence rather than direct damage payload.`
  - `Profile names should be localized on play-facing Spanish surfaces.`
  - `This technique resolves both false-line consequences because it gives up direct damage.`
- `coverage_movement`:
  - `Naghii: sim_defined 4 -> 5`
  - `Naghii: runtime_supported 2 -> 2`
- `follow_up_work`:
  - `Implement false-line runtime support for combined reposition plus immediate-response spoil`
