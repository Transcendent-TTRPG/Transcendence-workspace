# Transcendence Workspace — Claude Context

This file is read automatically at session start. It tells you what this project
is, what files matter, and what to load before doing technique work.

---

## What is this project

**Transcendence** is a bilingual (ES/EN) tabletop RPG with ATB combat, a
post-apocalyptic cosmic setting, and a technique system organized by weapon
profile, species origin, and specialization.

Three repos live as submodules under this workspace:

| Repo | Path | Role |
| --- | --- | --- |
| `Transcendence-design` | `Transcendence-design/` | Source of truth: YAML data, canon docs, world design |
| `Transcendence-publications` | `Transcendence-publications/` | Reader-facing: corebook prose, technique cards |
| workspace root | `/` | Submodule pointers, pipeline, skills, docs |

---

## Current state (as of 2026-06-05)

Drak'kai novice technique pass is in progress. Techniques written so far:

- #74–80 (Drak'kai bite/claw — complete)
- #81 El Tránsito Que No Llega (garras · Intercepción)
- #82 La Costura Que Cede (maza · Ruptura)
- #83 El Peso Que Planta (maza · Bastión)

**Remaining Drak'kai novice techniques to write:**

- #84 La Posición Que Se Hunde (escudo · Bastión · Activo)
- #85 El Margen Que Se Mueve (escudo · Control de Línea · Activo)
- El Golpe Que Cobra (armadura pesada · Reactivo) — defense #1
- El Cuerpo Que Se Calibra (armadura pesada · Activo) — defense #2
- 8 specialization techniques (Orientación, Enfoque, Identificación, Historia,
  Geografía, Lingüística, Percepción, Rastreo)
- 2 resistance hybrids (La Carga Que No Acaba, Lo Que Se Conoce No Sorprende)

---

## Skills to use for technique work

Two skills govern technique production. Read them before any technique run.

- [`skills/technique-authoring/SKILL.md`](skills/technique-authoring/SKILL.md)
  — design workflow: non-overlap analysis, mechanical framing, balance review
- [`skills/technique-play-surface/SKILL.md`](skills/technique-play-surface/SKILL.md)
  — prose rules for corebook entries and HTML cards; canonical language patterns,
  flavor text rules, effect text format

Other skills exist for related work (check `skills/` for the full list).

---

## Production order for each technique

**Core → Card → YAML. Always in this order.** Never write YAML before the core
and card exist and have been reviewed.

1. Write corebook entry:
   `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/<id>-<slug>.md`
2. Write technique card:
   `Transcendence-publications/technique-cards/transcendence-technique-cards/cards/es/<species>/<slug>.html`
3. Append to YAML:
   `Transcendence-design/data/system/techniques.yaml`

---

## Non-overlap analysis — mandatory before designing

Before drafting any technique:

1. Search `techniques.yaml` for **all existing techniques with the same weapon profile** across all species. Map what each one does. Identify the specific gap the new technique fills.
2. Also check **cross-profile functional overlap**: a technique that has the same trigger + same output as an existing one is a duplicate regardless of profile. Example: two techniques that both fire on enemy movement and stop that movement are overlapping even if their profiles differ.

Only after completing this analysis should you propose a design to the user.

---

## Key design rules to remember

- **No stacking:** penalties/bonuses don't stack — strongest value applies.
- **Posture cost doctrine:** stances that require the player to stay still cost Ritmo 3 (the positional lock is part of the price). Add Alcance del arma +1 to area to prevent trivial routing. Stance does NOT lock out attacks or other techniques — that makes player turns useless.
- **T.A. vs T.I. are independent:** T.A. tests if the weapon connects. T.I. is damage. A technique can use T.A. without T.I. when the contact creates no damage payload.
- **Rango vs Área:** Rango = where the effect *starts*. For stances, the effect starts at the user = `Personal`. Área = coverage from that origin.
- **Duración:** only `Instantáneo` or `Permanente`. No round-count or "next action" effects. Permanente effects must have clear fictional end conditions in the effect text.
- **`Salvación` field:** only when the saving roll *completely negates* the effect. A saving roll that only reduces severity does not go in Salvación — it goes in the effect text.

---

## Mechanics reference

The authoritative mechanics source is the corebook chapters, not memory:

```
Transcendence-publications/core-books/transcendence-corebook/
  01-getting-started/
  08-conflict-and-combat/   ← ATB, T.A./T.D./T.I./T.R./T.E., Desgaste, Fatiga
  09-techniques/es/         ← all published techniques (EN source of truth for mechanics)
```

For structured data:

- `Transcendence-design/data/system/techniques.yaml` — all authored techniques
- `Transcendence-design/data/system/weapon-technique-profiles.yaml` — profile definitions
- `Transcendence-design/data/system/specialization-technique-domains.yaml` — which specializations unlock which technique types
- `Transcendence-design/data/system/specializations-catalog.yaml` — full specialization list
- `Transcendence-design/data/system/ailments.yaml` — Alteraciones (Desequilibrado, Lacerado, Agonía, etc.)

---

## Seeds and species docs

Seeds define the thematic "DNA" a species technique must express. Read them
before designing any species-origin technique.

```
Transcendence-design/docs/canon/species/
  drakkai.md                    ← Drak'kai species identity
  drakkai-technique-seeds.md    ← Drak'kai technique seeds (read first for Drak'kai work)
  sauri.md / sauri-technique-seeds.md
  naghii.md / naghii-technique-seeds.md
  zarnag.md / zarnag-technique-seeds.md
  species-technique-coverage.md ← which profiles/specializations each species has used
```

---

## Cost doctrine

Read `docs/work-runs/2026-06-04-technique-cost-stabilization.md` and
`docs/work-runs/2026-06-04-technique-cost-master-table.md` for the current
cost doctrine before reviewing or setting Ritmo/Desgaste values.

Short summary:

- **Ritmo = time**: how much ATB position (ficha advancement) the technique costs. Any value ≥ 0. Ritmo 0 when the effect has no external manifestation, movement, or timing requirement — a purely internal cognitive or reactive snap. Ritmo > 0 when execution requires physical action, timing, or occupies attention on the ATB track.
- **Desgaste = effort**: permanent accumulated strain. Always ≥ 1 for active and reactive techniques — doing anything under simultaneous combat pressure costs something permanently, even when fast or cognitive. Desgaste 0 only for passive hybrid resistance techniques (things the body executes without conscious activation).
- Key question when setting costs: does this technique take **time** (Ritmo > 0), or only **effort** (Ritmo 0)? How much of each?
- Base actions are the inefficient floor — don't benchmark techniques against them.
- Don't surcharge just because a technique has `Permanente` duration.

---

## Workflow docs

For technique design workflow, read:
- `docs/workflows/technique-workflow.md`

---

## Commit convention

Commit all three repos (design, publications, workspace) after each technique
or batch. Commit message format:

```
Add <Technique Name> — <weapon/species> #<id>
```

Workspace commit: `Advance submodules — <Technique Name> #<id>`

Always push all three after committing.

---

## What the publications submodule CLAUDE.md says

The `Transcendence-publications` repo has its own `CLAUDE.md` with canonical
term translations and editorial constraints. Check it before editing any prose.
Key rule: **EN only in YAML, ES in all publication files.**
