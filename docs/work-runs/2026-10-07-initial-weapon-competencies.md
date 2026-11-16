# Dos competencias iniciales de arma

## Header

- `work_id`: initial-weapon-competencies-2026-10-07
- `owner_workflow`: authority-revision-workflow
- `linked_workflows`: core-sync-workflow
- `artifact_type`: mechanical_revision
- `status`: completed_with_preexisting_editorial_debt

## Scope

- Objetivo: registrar la decisión del creador de conceder dos competencias de arma distintas a nivel 1 a todos los personajes, independientemente de especie y trasfondo.
- Fuera de alcance: balance global de especies, creación completa del Panin, Técnicas iniciales, equipo inicial, armaduras y progresión posterior.
- Prioridad de fuentes: decisión explícita del creador y manual ES de Publications; Design recibe la misma decisión estructurada, sin restaurar supuestos antiguos.

## Mandatory sources

- Datos y referencia: `Transcendence-design/data/system/competencies.yaml`, `Transcendence-design/docs/system/competencies.md`.
- Decisión previa: `Transcendence-design/docs/adr/system-specialization-rank-restructure.md` (nivel 1 = Novato; Sinapsis solo por especializaciones).
- Publicaciones: capítulos 5 y 3, `character-creation.md` y `02-rolling-system-and-competencies.md`, ES/EN.
- Dependencias narrativas: `Transcendence-narrative-engine/rosters/contenedores-vacios/formix-01.yaml` y `loxod-01.yaml`.
- Memoria de decisión: `Transcendence-design/data/knowledge/decision-registry.yaml`.

## Phase checkpoints

1. Intake / baseline: completados. Capítulo 5 solo autorizaba sustituciones; capítulo 3 atribuía todas las competencias iniciales al trasfondo; los rosters asumían una competencia por arma natural.
2. Dependencias: capítulos 3/5 ES/EN, datos/referencia de competencias, índice numérico, resumen mecánico, ADR, registro de decisiones, explicaciones de ambos rosters y hojas generadas.
3. Clasificación: `mechanical_revision` + `multi_section_mechanical_sync`.
4. Propuesta: aprobada por el creador. Dos competencias distintas, nivel 1 / Novato, naturales o fabricadas justificadas por experiencia; ninguna elección repetida; anatomía no elegida a nivel 0; competencia no concede posesión; ninguna Sinapsis por arma.
5. Riesgo: aumenta la dotación de especies con una sola arma natural; no implica demostrar equilibrio global. No cambia los niveles actuales de Kairu y Nerum.
6. Integración: completada en datos de competencias, referencia, índice, resumen mecánico, ADR nuevo, registro de decisiones, capítulos 3/5 ES/EN y explicación de ambos rosters. No se modificaron valores ni biografías de protagonistas.
7. Validación: 15 pruebas de continuidad correctas, incluida regresión contra la dotación estructurada y las elecciones actuales de Kairu/Nerum. YAML válidos y registro sin IDs duplicados. Comprobación específica ES/EN de niveles 0/1/2, ejemplo, referencias de autoridad y enlace entre capítulos correcta. `diff --check` sin incidencias en los tres repositorios. Hojas regeneradas; el renderer no imprime la explicación de la regla y no se modificó su diseño.
8. Knowledge / downstream: ADR y registro de decisiones; sincronización editorial en este mismo pase. No se ha identificado un constructor de personajes que asigne estas competencias en el simulador; no se crea un runtime nuevo.

## Acceptance closure

- [x] Baseline y alcance registrados.
- [x] Decisión del creador explícita; invariantes y consecuencias delimitados.
- [x] Datos, referencia y decisión actualizados.
- [x] ES/EN de los dos pasajes sincronizados.
- [x] Ejemplos y restricciones comprobados.
- [x] Rosters alineados sin alterar entrenamiento, amnesia o pertenencias.
- [x] Hojas regeneradas y pruebas de continuidad ejecutadas.
- [x] Validación editorial ejecutada y pendientes registrados; no se afirma limpieza editorial global.

## Pending items

- Hay deriva ES/EN previa fuera del alcance: Aguante por tamaño en capítulo 5 ES frente a fórmula fija en EN; capítulo 3 ES incluye apartados sin par EN (armas naturales, Umbral Pasivo e interpretación de resultados). Este cambio no los resuelve.
- `pipeline/scripts/editorial-check.sh` conserva exactamente los 604 errores y 221 advertencias previos en Publications. Su informe no señala los cuatro archivos modificados. La revisión global sigue pendiente; la nueva regla pasó sus comprobaciones específicas.
- Panin: pendiente elegir sus dos competencias desde su biografía, no por conveniencia de las primeras escenas.

## Change impact

- La cantidad de armas naturales deja de determinar la dotación inicial de entrenamiento.
- No se añaden términos, bonificaciones de características, Técnicas ni objetos.
- Kairu: Expulsión Corrosiva 1 + Dolabra 1; Mordisco 0. Nerum: Colmillos 1 + Hasta 1; Trompa 0. Valores preservados.
