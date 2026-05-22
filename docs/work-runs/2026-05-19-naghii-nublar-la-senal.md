# Technique Work Run

## Header

- `work_id`: `2026-05-19-naghii-nublar-la-senal`
- `owner_workflow`: `technique-workflow`
- `linked_workflows`:
  - `technique-play-surface-workflow`
  - `simulation-port-workflow`
- `artifact_type`: `technique`
- `status`: `closed_partial`

## Scope

- `species`: `naghii`
- `technique_id`: `nublar_la_senal`
- `goal`: `Run the next early Naghii ranged Technique through final play surface and simulator definition.`
- `current_state`: `Authored in authority, not yet surfaced in core/card, not yet present in simulator.`
- `out_of_scope`:
  - `full runtime support for sensory-channel residue`
  - `policy support`
  - `saved scenario or question coverage`

## Mandatory sources

- authority docs:
  - `Transcendence-design/docs/system/techniques.md`
- authority data:
  - `Transcendence-design/data/system/techniques.yaml`
- seeds/canon:
  - `Transcendence-design/docs/system/weapon-technique-profiles.md`
  - `Transcendence-design/docs/system/materials-and-fabrication.md`
  - `Transcendence-publications/core-books/transcendence-corebook/08-conflict-and-combat/es/01-acciones.md`
- knowledge references:
  - `docs/workflows/technique-workflow.md`
  - `docs/workflows/technique-play-surface-workflow.md`
  - `docs/workflows/simulation-port-workflow.md`

## Phase checkpoints

### Phase 0. Intake
- `scope_recorded`: `yes`
- `main_question`: `Can Nublar la Señal be surfaced honestly now while classifying the missing runtime around bounded sensory residue instead of pretending current ailment or concealment logic already resolves it?`

### Phase 1. Species Framing
- `fantasy`: `A ranged residue does not blind the enemy fully; it fouls the one channel their next clean decision needs.`
- `world_origin`: `Saa-Naghii suppression practice projects venom logic outward so contact matters because it degrades the next decision rather than simply causing damage.`
- `why_not_base_action`: `The Technique is not generic ranged harm or poison damage; it creates a bounded sensory-pressure choice around one declared read channel.`
- `interaction_surfaces`:
  - `ranged residue`
  - `sensory pressure`
  - `one-roll disruption`

### Phase 2. Mechanical Framing
- `category`: `utility`
- `roll_model`: `T.A. with T.D. negating contact`
- `competency_source`: `Ranged Weapons`
- `effect_model`: `one declared sensory channel becomes costly to rely on until cleaned or spent`
- `duration_model`: `until cleanup, one affected action, or environmental loss of residue`
- `restrictions`:
  - `requires Desgaste access`
  - `requires Munition Kit for non-natural users`
  - `requires an exposed sensory channel`
  - `does not become full blindness`

### Phase 3. Dependency Framing
- `upstream_dependencies`:
  - `Ranged Weapons / Corrosion authority`
  - `Kit rules`
  - `Interactuar as quick cleanup path`
- `downstream_dependencies`:
  - `core technique entry`
  - `tarot card entry`
  - `sim technique definition`
  - `seed Naghii ranged projection profile`
- `blockers`: `runtime does not yet model a true signal-blurred residue state with one-roll burden and cleanup resolution`

### Phase 4. Balance Framing
- `cost_sanity_note`: `Rhythm 4 / Attrition 1 stays coherent because the Technique asks for a precise called sensory shot and pays off with one bounded disrupted read rather than damage.`
- `sibling_comparison_note`: `Unlike Marcar la Lectura, this does not preserve route readability; it pressures the target's next clean sensory action through one fouled channel.`
- `pressure_note`: `Its value is one forced cleanup-or-act-badly choice, not broad blindness or scene-wide debuffing.`
- `counterplay_note`: `The target can spend Interactuar to clear the residue before the affected action.`

### Phase 5. Simulation Framing
- `runtime_gap_classification`: `new_state_family`
- `porting_state_target`: `sim_defined`
- `scenario_seed_note`: `No runtime scenario yet because signal-blurred residue is not implemented as a real state family.`
- `question_seed_note`: `No saved Naghii suppression question yet.`

### Phase 6. Editorial Framing
- `authority_cleanup_note`: `Authority was aligned to Munition Kit dependency and Interactuar as the base cleanup path.`
- `terminology_note`: `Final surface localizes Corrosion to Desgaste and keeps Spanish roll notation T.A. / T.D.`
- `core_sync_note`: `Core and card were created together from the same semantic payload.`

## Integration

- `files_changed`:
  - `Transcendence-design/docs/system/techniques.md`
  - `Transcendence-design/data/system/techniques.yaml`
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/08-nublar-la-senal.md`
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/README.md`
  - `Transcendence-publications/technique-cards/transcendence-technique-cards/cards/es/naghii/nublar-la-senal.html`
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

- `authority_updated`: `yes`
- `yaml_updated`: `yes`
- `sim_defined_or_gap_classified`: `yes`
- `runtime_supported_or_gap_classified`: `gap classified`
- `coverage_updated`: `yes`
- `core_sync_done_or_not_needed`: `done through play-surface run`
- `pending_items_explicit`: `yes`

## Pending items

- `pending`:
  - `Implement a real signal-blurred sensory residue state family.`
  - `Connect cleanup and one-roll burden resolution to runtime honestly.`
  - `Add Naghii suppression policy, scenario, and question coverage.`

## Change impact

- `concepts_touched`:
  - `Desgaste play surface`
  - `munition-kit dependency on ranged residue techniques`
  - `bounded sensory-pressure simulator backlog`
- `decisions_reinforced_or_created`:
  - `A utility technique may use T.A. and T.D. without carrying direct impact payload.`
  - `If a residue technique has a base cleanup path, that path should appear explicitly on the final play surface.`
  - `Non-natural residue delivery should name Kit de Munición directly when that is the real gate.`
- `coverage_movement`:
  - `Naghii: sim_defined 6 -> 7`
  - `Naghii: runtime_supported 2 -> 2`
- `follow_up_work`:
  - `Implement bounded sensory-residue runtime support`
