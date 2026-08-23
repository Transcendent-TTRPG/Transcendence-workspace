---
name: "novel-authoring"
description: "Use when translating a Transcendence campaign module and party of characters into a long-form novel or serialized narrative chapters. Enforces constrained 3rd-person POV, bio-tactical consistency, and sensory-driven prose without repo-wide over-fetching."
---

# Novel Authoring (Module-to-Prose Pipeline)

Use this skill when converting a **Campaign Module** into a **Novel / Serialized Fiction** within the Transcendence universe.

---

## 1. Scope & Role

- **Input:** A structured campaign module (scenes, locations, adversaries, puzzles) + A party of protagonist character sheets.
- **Output:** Serialized novel chapters written in visceral, third-person constrained POV.
- **Discipline:** Mechanical design of the module (encounters, stats, maps) is decided prior to or during authoring discussion. This skill governs the **dramatization and literary translation** of those game elements.

---

## 2. Minimal Context Loading (Anti-Overfetch Guardrail)

Do **NOT** scan or load the entire workspace. Load strictly what is needed for the current task:

| Phase | Files to Load |
| :--- | :--- |
| **Character Creation / Party Dossier** | 1. The specific species canon doc: `Transcendence-design/docs/canon/species/<species>.md`<br>2. The technique seeds/profile if applicable |
| **Scene Preparation** | 1. The target module act/scene (e.g. `contenedores-vacios/01-acto-1-el-despertar.md`)<br>2. The character profiles of the party |
| **Chapter Prose Drafting** | 1. `Transcendence-publications/canon/fiction-guide.md`<br>2. `Transcendence-publications/canon/style-guide.md`<br>3. The POV character profile for the chapter/scene |

---

## 3. Core Narrative Guardrails

1. **Constrained Third-Person POV (No Omniscient Lore-Dumps):**
   - Each chapter/scene is anchored to one protagonist's perspective.
   - Describe only what that character's sensory anatomy and cultural background can register.
   - Never explain world history or mechanics as an outside narrator. If a character doesn't understand ancient human machinery, describe the cold, humming black alloy and the smell of ozone, not "an ancient magnetic capacitor".

2. **Sensory Biology as Narrative Filter:**
   - Every playable species experiences the world through distinct biological organs:
     - **Rokhart:** Feather tension, spatial/vertical calculations, bone lightness, clinical detachment.
     - **Formix:** Chemical gradients, antennal taste, mandible torque, caste/order urgency.
     - **Naghii:** Infrared thermal traces, Jacobson's organ, vibration, serpentine balance.
     - **Luphran:** Scent trails, pack proximity, hunting drive, predatory instinct.
     - **Drak'kai:** Internal geomagnetic orientation, carapace weight, bone density.
     - *(Apply equivalent biological anchors for any of the 20 species)*.

3. **Physics-Grounded Action & Tauma:**
   - The Tauma is an equalizer of physical gradients (pressure, sound, heat, kinetic force), not abstract magic.
   - Combat adheres to the tactical reality of *Transcendence*: ATB timing/windows, reaction delays, weapon profiles, cover, wounds, and fatigue.
   - Playable species are fragile. Every encounter has real stakes and physical cost.

4. **Bio-Organic Technology Constraints:**
   - Equipment and tools made of living/inert symbiosis suffer from cold, starvation, exhaustion, and environmental degradation.

---

## 4. The 4-Step Authoring Workflow

```
[1. Party Dossier] ──▶ [2. Scene Tactical Staging] ──▶ [3. Dramatic Discussion] ──▶ [4. Chapter Prose]
```

1. **Party Dossier:** Maintain a character sheet for each protagonist (Attributes, Species Heritage, Techniques, Sensory Channels, Trauma/Motivation, Interpersonal Friction).
2. **Scene Tactical Staging:** Frame the current module beat (objective, environment, active threats, time pressure).
3. **Dramatic Discussion:** Align with the Director/User on tactical choices and party decisions as if playing the session.
4. **Chapter Prose Drafting:** Write the scene adhering to `fiction-guide.md` and the designated POV voice.
