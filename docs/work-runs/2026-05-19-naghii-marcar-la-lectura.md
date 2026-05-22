# Technique Work Run

## Header

- `work_id`: `2026-05-19-naghii-marcar-la-lectura`
- `owner_workflow`: `technique-workflow`
- `linked_workflows`:
  - `technique-play-surface-workflow`
  - `simulation-port-workflow`
- `artifact_type`: `technique`
- `status`: `closed_partial`

## Scope

- `species`: `naghii`
- `technique_id`: `marcar_la_lectura`
- `goal`: `Run the next early Naghii weapon Technique through final play surface and simulator definition.`
- `current_state`: `Authored in authority, not yet surfaced in core/card, not yet present in simulator.`
- `out_of_scope`:
  - `full runtime support for marked-route tracking`
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
- `main_question`: `Can Marcar la Lectura be surfaced honestly now while classifying its simulator gap as marked-route readability instead of pretending the current concealment runtime already covers it?`

### Phase 1. Species Framing
- `fantasy`: `A precise mark turns the target's next disappearance into a readable route instead of a clean loss.`
- `world_origin`: `Saa-Naghii projection practice treats distance as a place where interpretation must be made consequential through trace and pursuit.`
- `why_not_base_action`: `The Technique is not generic ranged damage; it preserves immediate route readability after contact.`
- `interaction_surfaces`:
  - `ranged precision`
  - `marking`
  - `counter_concealment`

### Phase 2. Mechanical Framing
- `category`: `attack`
- `roll_model`: `T.A. with T.D. negating contact`
- `competency_source`: `Ranged Weapons`
- `effect_model`: `apply a short-lived readable mark rather than direct impact payload`
- `duration_model`: `until next movement or concealment attempt, mark clear, sealed barrier, or lost relevance`
- `restrictions`:
  - `requires Precision access`
  - `requires a delivery capable of leaving a readable mark`
  - `does not grant attack bonus or cover ignore`

### Phase 3. Dependency Framing
- `upstream_dependencies`:
  - `Ranged Weapons / Precision authority`
  - `player-facing marking language`
  - `counter-concealment semantics`
- `downstream_dependencies`:
  - `core technique entry`
  - `tarot card entry`
  - `sim technique definition`
  - `seed Naghii projection profile`
- `blockers`: `runtime does not yet support a real read-marked route state or immediate-route preservation through concealment pressure`

### Phase 4. Balance Framing
- `cost_sanity_note`: `Rhythm 4 / Attrition 1 stays coherent because the Technique spends a precise ranged hit on bounded information control instead of direct damage payoff.`
- `sibling_comparison_note`: `Unlike Robar el Ángulo, this wins by preserving the target's route as readable information rather than stealing angle or spoiling response through melee pressure.`
- `pressure_note`: `Its payoff is one immediate readable route, not full tracking or broad reveal.`
- `counterplay_note`: `A defended contact prevents the mark, and clearing the mark or crossing a sealed barrier ends the benefit.`

### Phase 5. Simulation Framing
- `runtime_gap_classification`: `new_state_family`
- `porting_state_target`: `sim_defined`
- `scenario_seed_note`: `No runtime scenario yet because marked-route readability is not implemented as a real state family.`
- `question_seed_note`: `No saved Naghii projection question yet.`

### Phase 6. Editorial Framing
- `authority_cleanup_note`: `Authority cost note in md was corrected to Rhythm 4 / Attrition 1 to match yaml.`
- `terminology_note`: `Final surface localizes the profile as Precisión and uses the existing Spanish publication roll notation T.A. / T.D.`
- `core_sync_note`: `Core and card were created together from the same semantic payload.`

## Integration

- `files_changed`:
  - `Transcendence-design/docs/system/techniques.md`
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/07-marcar-la-lectura.md`
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/README.md`
  - `Transcendence-publications/technique-cards/transcendence-technique-cards/cards/es/naghii/marcar-la-lectura.html`
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
- `yaml_updated`: `not_needed`
- `sim_defined_or_gap_classified`: `yes`
- `runtime_supported_or_gap_classified`: `gap classified`
- `coverage_updated`: `yes`
- `core_sync_done_or_not_needed`: `done through play-surface run`
- `pending_items_explicit`: `yes`

## Pending items

- `pending`:
  - `Implement a real read-marked / route-readable procedural state family.`
  - `Connect marked-route readability to concealment and movement logic honestly.`
  - `Add Naghii projection policy, scenario, and question coverage.`

## Change impact

- `concepts_touched`:
  - `Precision play surface`
  - `marking-based counter-concealment`
  - `read-marked simulator backlog`
- `decisions_reinforced_or_created`:
  - `Spanish play surfaces can include Salvación explicitly when a distinct T.D. negates the effect.`
  - `A marking technique may omit Impact when its payoff is route readability rather than direct damage.`
  - `Final publication surfaces should preserve exact bounded scope instead of inflating a tracking effect into broad reveal.`
- `coverage_movement`:
  - `Naghii: sim_defined 5 -> 6`
  - `Naghii: runtime_supported 2 -> 2`
- `follow_up_work`:
  - `Implement marked-route readability runtime support`
