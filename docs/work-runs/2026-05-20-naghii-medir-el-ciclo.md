---
work_id: 2026-05-20-naghii-medir-el-ciclo
date: 2026-05-20
species: Naghii
technique: Medir el Ciclo
owner_workflow: technique-workflow
linked_workflows: []
status: closed
supersedes: 2026-05-20-naghii-calcular-el-vano
---

# Work Run: Medir el Ciclo

## Scope

New Novice Astronomía technique for Naghii. Replaces Calcular el Vano (which
was redesigned twice from Leer el Arco). Final design anchors Astronomía to
the ciclo autónomo mechanic — independent ATB pieces belonging to Elite
creatures, body parts, or environmental effects. The technique reads the Rhythm
of a cycle before it fires. Number of steps revealed scales with Astronomía rank.

New subsystem created alongside the technique: `creature-cycles.md` defines the
ciclo autónomo as a formal mechanic. Authority, YAML, seeds, pending, publication
core, and card are all written.

## Phase 0 — Intake

- Run type: fantasy-led new authoring (third iteration; prior designs discarded)
- Main question: What does Naghii formal celestial knowledge produce in ATB
  that no other technique, no other species, and no base Astronomía roll can?
- Prior iteration (Calcular el Vano): targeted shadow/light/tide windows in
  scene — valid but too environment-dependent and too close to exploration
- Key insight: Astronomy = reading cycles. ATB bosses have independent cycles.
  The astronomer reads the cycle before it fires.
- New dependency identified: ciclo autónomo subsystem (not yet in design docs)
- Decision: document the subsystem minimally, anchor technique to it

## Phase 1 — Species Framing

- Fantasy: The Naghii astronomer does not wait to see what the cycle does.
  They measure it. Every cycle has a Rhythm, and the discipline of reading
  return intervals from observable patterns applies to anything that fires
  on a schedule.
- Irreducible fantasy: The group knows exactly when the next pulse arrives.
  No one else does.
- World origin: Outer archive cycle-reading training — extracting return
  intervals from pattern data before deeper celestial study is permitted.
  Same cognitive tool as tracking lunar returns and tidal cycles.
- Why not base roll: A base Astronomía roll estimates. Medir el Ciclo forces
  the Narrator to declare a specific Rhythm value — not "soon" but "in 2
  Rhythm" — with enough precision to act on.
- Combat utility: direct and primary — in ATB, knowing when a cycle fires
  changes every subsequent decision in that window.
- Interaction surfaces: utility (timing information), setup (group acts into
  the declared window with precision others cannot match).
- Rank scaling: steps revealed = Astronomía rank. This is the natural
  expression of "more experience = read further into the cycle."

## Phase 2 — Mechanical Framing

- Category: utility / active
- Roll: T.E. (Astronomía)
- Target: ciclo autónomo (ATB entity — not a creature, not a zone)
- Range: visual range
- Area: one ciclo autónomo
- Duration: immediate
- Rhythm: 3 / Attrition: 1 (ATB-only)
- Saving roll: none
- Tags: utility, setup, pattern_exploitation

## Phase 3 — Dependency Framing

- New subsystem: ciclo autónomo — created in creature-cycles.md
- Upstream: Astronomía specialization (stable). No ailment. No existing
  subsystem extension.
- Downstream: techniques.md, techniques.yaml, naghii-technique-seeds.md,
  pending.md, core entry, card.
- Blockers: none — subsystem defined in this run.
- Bounded expansion: creature-cycles.md is the bounded expansion. Minimal,
  focused, directly supports the technique.

## Phase 4 — Balance Framing

- Cost: R=3/D=1 matches all Novice Naghii specialization information
  techniques. Justified: output is immediate and combat-decisive.
- Scaling is through rank (not a new technique tier) — clean and bounded.
- Pressure: low baseline at Novice (1 step ahead). Pressure grows with
  investment in Astronomía rank, which is the correct scaling surface.
- Counterplay: if the creature's cycle Rhythm is randomized or varies
  between steps, the declared value is still accurate for the next N steps
  (Narrator declares honestly). No counterplay to the technique itself —
  consistent with how other Naghii information techniques work.

## Phase 5 — Simulation Framing

- Runtime gap: data_only — produces Narrator-side timing information; no
  mechanical state change in sim actors.
- Porting state: sim_defined (pending — sim infrastructure not present in
  current workspace)
- Scenario seed: naghii_cycle_read — ATB scene with at least one ciclo
  autónomo present; Narrator declares Rhythm values; user times actions around
  the declared window
- Question seed: cost question comparing Medir el Ciclo vs passive waiting;
  does knowing N steps ahead change action selection rate?

## Validation

- roll_integrity: pass — T.E. (Astronomía), no saving roll, no impact field
- surface_integrity: pass — core and card match; requirements reference ciclo
  autónomo correctly
- exchange_integrity: not_applicable
- ailment_integrity: not_applicable
- critical_break_integrity: not_applicable
- atb_integrity: pass — active timing correct; Desgaste ATB-only clause present;
  rank scaling is explicit
- dependency_integrity: pass — ciclo autónomo subsystem created in this run;
  no unresolved upstream
- simulation_integrity: pass — data_only gap correctly classified; no runtime
  support claimed
- balance_sanity: pass — R=3/D=1 matches sibling pattern; rank scaling is
  naturally bounded
- loader_validation: pass — 74 canonical techniques, 0 errors, 0 warnings
- scenario_validation: not_applicable (sim not present)
- question_validation: not_applicable (sim not present)
- publication_consistency: pass — core entry and card reflect same payload

## Acceptance Closure

- authority_updated: yes (techniques.md — Medir el Ciclo section)
- yaml_updated: yes (techniques.yaml — 74 canonical techniques)
- new_subsystem_created: yes (creature-cycles.md — ciclo autónomo)
- sim_defined_or_gap_classified: gap classified — data_only; sim not present
- runtime_supported_or_gap_classified: gap classified
- coverage_updated: yes (pending.md: Medir el Ciclo; seeds: row updated)
- core_sync_done_or_not_needed: done (17-medir-el-ciclo.md)
- pending_items_explicit: sim profile, scenario, minimum cost question

## Change Impact

- concepts_touched: Astronomía technique domain for Naghii; ciclo autónomo
  as a new formal subsystem for Elite creatures and environmental effects
- decisions_reinforced: combat-first directive (Astronomy = cycle reading,
  not trajectory reading, not record verification); rank as scaling surface
  for information depth
- coverage_movement: Naghii Astronomía technique — now closed with a combat-
  first design anchored to a new mechanic
- follow_up_work: broader creature system documentation (categories, natures,
  battle roles, stats); ciclo autónomo YAML schema; sim profile
  naghii_novice_cycle_reader; scenario naghii_cycle_read; minimum cost question
