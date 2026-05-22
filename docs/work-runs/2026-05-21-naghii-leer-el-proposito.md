---
work_id: 2026-05-21-naghii-leer-el-proposito
date: 2026-05-21
species: Naghii
technique: Leer el Propósito
owner_workflow: technique-workflow
linked_workflows: []
status: closed
supersedes: null
---

# Work Run: Leer el Propósito

## Scope

Full redesign of Leer el Propósito (Architecture — Novato). The prior design
read built spaces for structural intent truths — useful in exploration but
overlapping too heavily with what a base Architecture S.R. already provides
narratively, and anchored to environments rather than ATB combat.

New design applies architectural structural grammar (access hierarchy, load
distribution, vital mass concentration) to living creatures — identifying one
Punto Vital on the target creature. The technique reveals location only, not
function: no cycles, no techniques, no connections. Bonus to T.A and T.E
against that Punto Vital scales with Architecture rank.

## Phase 0 — Intake

- Run type: redesign (prior design discarded)
- Main question: what does Naghii formal architectural knowledge produce in
  ATB that no base Architecture roll can, and that no other technique produces?
- Prior design: structural intent truth about built spaces — too exploration-
  anchored, too close to base S.R. output
- Key insight: Architecture reads structural grammar. Creatures have structural
  grammar. Vital points are the load-bearing nodes of a living system. The
  cognitive tool transfers.
- Decision: target creatures, identify Puntos Vitales, bonus to targeting

## Phase 1 — Species Framing

- Fantasy: a Naghii architect does not wait for the creature to act to
  understand its critical zones. They read the structural organization —
  access hierarchy, vital mass concentration — and identify where the
  critical biology is held. Not what it does. Where it is.
- Irreducible fantasy: the user knows exactly which zone is vital before
  anyone else attacks it
- World origin: outer archive training — structural grammar reading applied
  first to built space, then to any organized system including living ones
- Why not base roll: base Architecture roll gives qualitative impressions.
  Leer el Propósito forces the Narrator to declare one specific Punto Vital
  location — binary, actionable, targetable
- Combat utility: direct — identification enables focused fire; Punto Vital
  destruction interrupts linked cycles and techniques
- Bonus: +[Architecture rank] to T.A and T.E against the identified Punto Vital
  (user only — information vs. competence principle)
- Duration: indefinite — architectural knowledge does not expire; ends only
  when the vital point is destroyed or relocated

## Phase 2 — Mechanical Framing

- Category: utility / active
- Roll: T.E. (Architecture)
- Target: one creature
- Range: visual range
- Area: one Punto Vital
- Duration: indefinite (until Punto Vital destroyed or relocated)
- Rhythm: 3 / Attrition: 1 (ATB-only)
- Saving roll: none (difficulty threshold by creature category)
- Tags: utility, setup, targeting, structural_analysis

## Phase 3 — Dependency Framing

- No new subsystem required
- Upstream: Architecture specialization (stable). No ailment. Puntos Vitales
  subsystem already exists in the design.
- Downstream: techniques.md, techniques.yaml, core entry, card
- Blockers: none

## Phase 4 — Balance Framing

- Cost: R=3/D=1 matches all Novice Naghii specialization information
  techniques. Justified: output is identification + persistent bonus
- Difficulty by creature category: Común=Desafiante, Campeona=Rigurosa,
  Elite=Exigente. Vital point count (~5) is equal across categories and
  is not the determining factor — structural complexity is
- Bonus scales with Architecture rank (+1 per rank), user only
- Duration: indefinite — correct because knowledge is permanent; the only
  invalidation condition is structural change (Punto Vital destroyed or
  relocated), not time

## Phase 5 — Simulation Framing

- Runtime gap: data_only — produces Narrator-side location information and
  user-side roll bonus; no complex state machine required
- Porting state: sim_defined (pending — sim infrastructure not present)
- Scenario seed: naghii_vital_read — ATB scene with champion or elite
  creature; user identifies one Punto Vital; group focuses fire; observes
  whether identification changes action selection rate vs. unguided targeting

## Validation

- roll_integrity: pass — T.E. (Architecture), no saving roll, no impact field
- surface_integrity: pass — core and card match; requirements reference
  Punto Vital correctly
- exchange_integrity: not_applicable
- ailment_integrity: not_applicable
- critical_break_integrity: not_applicable
- atb_integrity: pass — active timing correct; Desgaste ATB-only clause
  present; bonus duration correctly bounded
- dependency_integrity: pass — no new subsystem; Puntos Vitales already
  defined in design
- simulation_integrity: pass — data_only gap correctly classified
- balance_sanity: pass — R=3/D=1 matches sibling pattern; bonus bounded
  to user only and to T.A/T.E only
- loader_validation: pass — 74 canonical techniques, 0 errors, 0 warnings
- publication_consistency: pass — core entry and card reflect same payload

## Acceptance Closure

- authority_updated: yes (techniques.md — Leer el Propósito section rewritten)
- yaml_updated: yes (techniques.yaml — Leer el Propósito entry rewritten)
- new_subsystem_created: no (Puntos Vitales already exists)
- sim_defined_or_gap_classified: gap classified — data_only; sim not present
- core_sync_done_or_not_needed: done (18-leer-el-proposito.md)
- pending_items_explicit: sim profile, scenario naghii_vital_read

## Change Impact

- concepts_touched: Architecture technique domain for Naghii; application of
  structural grammar to living systems (not a new subsystem — an extension
  of architectural reasoning to a new medium)
- decisions_reinforced: combat-first directive; information vs. competence
  principle (bonus user-only, information shared); specialization vs.
  technique distinction (base roll = qualitative, technique = forced
  Narrator declaration)
- follow_up_work: sim profile naghii_novice_vital_reader; scenario
  naghii_vital_read; broader creature category documentation
