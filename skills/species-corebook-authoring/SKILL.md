---
name: "species-corebook-authoring"
description: "Use when a species design document must be converted into a reader-facing corebook prose entry with mechanical stats. This is a UNIFIED, single-pass authoring skill that inherently applies cosmicist compression, fluid prose without subtitles, and strict inside-out perspective."
---

# Species Corebook Authoring (Unified Pass)

Use this skill to write the reader-facing corebook entry for a species. 

This is a **highly compressed, single-pass authoring workflow**. It replaces the old multi-stage pipeline. Do not attempt to run a separate "cosmology localization" pass after this; this skill requires you to write localized, inside-out lore from the very first letter.

## Required Context

Load in this order before writing anything:
1. **Species design doc:** `Transcendence-design/docs/canon/species/<species>.md`
2. **Editorial rules:** `Transcendence-publications/CLAUDE.md`
3. **Reference files (Recent standard):** `Transcendence-publications/core-books/transcendence-corebook/06-species/es/14-bufoni.md` or `15-vesper.md`

---

## 🛑 THE 4 IRON RULES OF SPECIES AUTHORING

### 1. Prosa Fluida y Compresión Extrema (CERO SUBTÍTULOS)
- **NO uses subtítulos** (como "El Cuerpo", "La Cultura", "Teología", etc.) en la sección de lore.
- La historia, cultura, biología y creencias de la especie deben estar entrelazadas en **3 a 5 párrafos densos, evocativos y continuos**. Menos es más. Un párrafo potente vale más que una enciclopedia aburrida.
- La única sección que lleva formato y subtítulos es el **Bloque de Estadísticas Mecánicas** al final del archivo.

### 2. Perspectiva Interna Absoluta (Inside-Out)
- **PROHIBIDO usar términos del Capítulo 12 en el Lore.** No menciones jamás las palabras: *Tauma*, *Limbo*, *Vestigios*, *Vínculos*, *Aflicciones* o *Entidades Primordiales*.
- La especie no conoce la metafísica objetiva del universo. Solo conoce sus rituales, su entorno, sus miedos y su biología.
- Describe los objetos mágicos o fuerzas místicas usando el vocabulario cotidiano o teológico de la especie (ej: "las aguas responden", "las reliquias cerradas", "el pulso del mundo").

### 3. Tragedia Sistémica (El Horror Cósmico)
- Cada especie debe escribirse alrededor de su ansiedad civilizacional o su ironía trágica.
- **NO declares el miedo directamente.** No escribas "Su mayor miedo es...". Muéstralo. 
- Ejemplo: Los Vesper creen firmemente que están torturando cuerpos para revelar "dioses" (consagrados); la tragedia es la certeza con la que manufacturan monstruos. El horror debe surgir orgánicamente de sus prácticas institucionales y creencias.

### 4. Human Scale (Baja a la Tierra)
- No escribas todo desde una altitud sociológica omnisciente. 
- Incluye detalles sensoriales, escenas implícitas, o la perspectiva de un individuo (un guerrero esperando en el barro, un archivista cerrando una línea de sangre). Haz que el lector sienta que está parado frente a ellos.

---

## Execution Pattern

### Phase 1: Synthesize the Design Doc
Read the species design document. Identify the core Tragedy/Horror, the biological reality, and the cultural response. Mentally map how you will weave these into 3-5 paragraphs without explicitly naming system mechanics.

### Phase 2: Write the Lore (3-5 Paragraphs)
Write the narrative lore following the **4 Iron Rules**. 
- **Paragraph 1:** Hook the reader. Place them in the world with the species. Establish the physical/sensory reality.
- **Paragraph 2-3:** Weave their biology, culture, and daily practices. Show how their civilization works.
- **Paragraph 4:** Establish the systemic tragedy/cosmology (without Chapter 12 terms).
- **Paragraph 5 (Optional):** Wrap up with how they interact with outsiders or why one would leave their home (Player Character hooks).

### Phase 3: Mechanical Stats Block
Append the standard mechanical stats block after the lore. **This is the only place where subtitles and system terms (T.A., T.E., NR) are allowed.**

The block MUST follow this exact markdown structure and inherit values directly from the design doc:

```markdown
---

## Estadísticas de Especie

### Datos Generales

| Longevidad | Tamaño | Estatura | Peso | Velocidad |
| --- | --- | --- | --- | --- |
| [Valor] | [Valor] | [Valor] | [Valor] | [Valor] |

**Idiomas:** [Idioma Nativo] · Común

### Características

Los [Species] obtienen `+1` en **[Stat 1]**, **[Stat 2]** y **[Stat 3]**.

### Herencia

**[Nombre de la Herencia]** — [Descripción biológica y mecánica. Ej: Penalización de -3 a ciertas T.E.]

### Legado

**[Nombre del Legado 1]** — [Descripción mecánica. Ej: +1 por cada cuatro Niveles de Referencia a X]
**[Nombre del Legado 2]** — [Descripción mecánica]

### Armas Naturales

Todos los [Species] tienen acceso a [Arma 1] y [Arma 2] desde el inicio.

#### [Arma 1]
*Todos los [Species] · Principal/Auxiliar*

| T.A. | T.I. | Alcance | Daño | Durabilidad | Potencia |
| --- | --- | --- | --- | --- | --- |
| [Stat] | [Stat] | [X m] | [Dado] | [Escala] | [Escala] |

**Perfiles:** [Perfil 1] · [Perfil 2]

**Efecto:** [Condición y severidad si supera T.D. por 3 o más]
```

### Phase 4: File Creation
Write the output to `Transcendence-publications/core-books/transcendence-corebook/06-species/es/<nn>-<species-slug>.md`. (Determine `<nn>` by checking the existing files in the directory).

Include the standard YAML frontmatter:
```yaml
---
title: "<Species Name>"
type: corebook
content_kind: lore
writing_mode: prose
language: es
chapter: 6
status: draft
canonical: false
tags: [species, <species-slug>, lore, <tags>]
authority_refs:
  - Transcendence-design/docs/canon/species/<species>.md
related:
  - core-books/transcendence-corebook/06-species/es/00-las-especies.md
---
```
