---
work_id: 2026-05-20-naghii-calcular-el-vano
date: 2026-05-20
species: Naghii
technique: Calcular el Vano
owner_workflow: technique-workflow
linked_workflows: []
status: closed
---

# Work Run: Calcular el Vano

## Scope

New Novice Astronomía technique for Naghii. Replaces the deleted Leer el Arco
(which incorrectly expressed trajectory-reading of creatures — outside Astronomy
domain bounds). Authority, YAML, seeds, publication core, and card are written.
Simulation gap classified.

## Phase 0 — Intake

- Run type: fantasy-led new authoring
- Main question: What concrete moment does Naghii formal celestial knowledge
  produce that no base Astronomía roll and no other technique already covers?
- Mandatory sources: `specialization-technique-domains.md §Astronomy`,
  `data/system/techniques.yaml`, `docs/system/techniques.md`,
  `naghii-technique-seeds.md`

## Phase 1 — Species Framing

- Fantasy: The Naghii applies formal celestial calculation to a timing-dependent
  scene — forcing the Narrator to declare one precise temporal truth (window
  of change, or timing impossibility in a record) that the scene cannot otherwise
  resolve.
- Irreducible fantasy: The sky runs on cycles. The Naghii calculates the window.
  The calculation is precise, not intuitive.
- World origin: Outer archive celestial calculation training — positional
  mathematics taught as prerequisite before deeper sky doctrine.
- Why not base roll: A base Astronomía roll answers whether the character knows
  enough. This Technique forces a specific Narrator declaration — a named timing
  truth, not a success/fail at estimation.
- Interaction surfaces: utility (timing information), setup (declared window
  becomes operational basis for subsequent decisions).

## Phase 2 — Mechanical Framing

- Category: utility / active
- Roll: T.E. (Astronomía)
- Target: phenomenon or record/plan (not a creature)
- Range: visual range or access to a record
- Area: one timing window or one record
- Duration: immediate
- Rhythm: 3 / Attrition: 1 (ATB-only)
- Saving roll: contextual — only if timing was deliberately falsified
- Tags: utility, setup, pattern_exploitation

## Phase 3 — Dependency Framing

- Upstream: Astronomía specialization (stable). No new ailment. No new subsystem.
- Downstream: techniques.md, techniques.yaml, naghii-technique-seeds.md,
  pending.md, core entry, card.
- Blockers: none.
- Bounded expansion: none needed.

## Phase 4 — Balance Framing

- Cost sanity: R=3/D=1 matches all Novice Naghii specialization information
  techniques (Leer el Calor del Paso, Leer la Línea Ausente, Pesar el Umbral,
  Leer el Propósito). Output is comparable: one structured truth per use.
- Pressure: low — pure information, no attack surface, no ailment.
- Counterplay: falsified records resolve against forger's method. Enclosed
  scenes without sky visibility limit use.

## Phase 5 — Simulation Framing

- Runtime gap: data_only — produces Narrator-side timing information; no
  mechanical state change on scene actors.
- Porting state: sim_defined (pending — sim infrastructure not present in
  current workspace; classify and document only)
- Scenario seed: naghii_celestial_timing_read — scene with a timing-dependent
  phenomenon or record, no active combat pressure
- Question seed: cost question comparing Calcular el Vano vs Leer el Calor
  del Paso on rhythm efficiency in information-gathering scenes

## Validation

- roll_integrity: pass — T.E. (Astronomía), no saving roll at novice (contextual
  only for falsified timing), no impact field
- surface_integrity: pass — core and card match; requirements are real game
  mechanisms
- exchange_integrity: not_applicable
- ailment_integrity: not_applicable
- critical_break_integrity: not_applicable
- atb_integrity: pass — active timing correct; Desgaste ATB-only clause present
- dependency_integrity: pass — no unresolved upstream
- simulation_integrity: pass — data_only gap correctly classified; no runtime
  support claimed
- balance_sanity: pass — R=3/D=1 matches sibling pattern
- loader_validation: pass — 74 canonical techniques, 0 errors, 0 warnings
- scenario_validation: not_applicable (sim not present)
- question_validation: not_applicable (sim not present)
- publication_consistency: pass — core entry and card reflect same payload

## Acceptance Closure

- authority_updated: yes (techniques.md)
- yaml_updated: yes (techniques.yaml — 74 canonical techniques)
- sim_defined_or_gap_classified: gap classified — data_only; sim infrastructure
  not present in workspace
- runtime_supported_or_gap_classified: gap classified
- coverage_updated: yes (pending.md: 8/4+4, naghii-technique-seeds.md row added)
- core_sync_done_or_not_needed: done (17-calcular-el-vano.md created)
- pending_items_explicit: sim profile and scenario files deferred

## Change Impact

- concepts_touched: Astronomía technique domain for Naghii; celestial-order
  as a timing/verification tool distinct from trajectory reading
- decisions_reinforced: domain boundary (Astronomy = formal cycle logic, NOT
  creature trajectory); R=3/D=1 is the standard Novice specialization cost
- coverage_movement: Naghii specialization techniques 7→8 (Astronomía gap closed)
- follow_up_work: sim profile naghii_novice_celestial_reader, scenario
  naghii_celestial_timing_read, minimum cost question
