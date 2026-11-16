# #107 Adaptabilidad — sincronización y acceso espontáneo de Seku

- Fecha: 2026-11-02.
- Estado: sincronización de contenido ES completada; cierre visual, balance y motor pendientes.
- Alcance aprobado: conservar competencias reales, transferir apoyo parcial entre especializaciones de la misma característica y representar el legado como asociación espontánea en Seku desde el despertar.
- Flujo principal: technique-authoring / technique-workflow.
- Flujos vinculados: technique-play-surface, core-sync-workflow, mechanic-registrar y rule-clarifier. Simulation-port-workflow queda pendiente.

## Decisión y autoridad

Se registró #107 en `Transcendence-design/data/system/techniques.yaml`, su referencia
`docs/system/technique-adaptabilidad.md`, el ADR `docs/adr/panin-adaptability-transfer.md`
y el glosario de Publications. Se actualizaron índice, catálogo, resumen de sistemas
y documento de especie. La fórmula es `max(nivel de destino + rango de destino,
rango actual de origen)`. Un uso añade o sustituye una pareja, con 1/2/3 espacios
en NR 1–4/5–8/9+, coste 3/1 bajo presión y permanencia hasta sustituirse.

La selección mecánica puede representar una asociación espontánea. No exige que
Seku conozca el nombre o planee usarla. Mantiene sus costes y límites, sin bono
universal ni acceso a información bloqueada. El actor decide sus acciones; el GM
valida y resuelve. No se predetermina una pareja, un uso o una escena inicial.

## Superficies sincronizadas

- Entrada ES #107 y ejemplo separado en `core-books/transcendence-techniques/es/ejemplos/adaptabilidad.md`.
- Resumen de Adaptabilidad en capítulo 06, entrada Panin.
- Tarjeta individual y artículo idéntico en la hoja de impresión Panin.
- Perfil de diseño, perfil de amnesia y roster privado de Seku, copia editorial de consulta y README de hojas.
- Vista generada `Transcendence-narrative-engine/character-sheets/contenedores-vacios/03-seku.html`.

Los tres aprendizajes técnicos y las siete unidades de memoria de Seku continúan
bloqueados; no se registraron eventos de continuidad. No se modificaron habilidades
de otros personajes, decisiones de acción ni reglas generales de aprendizaje.

## Verificación

- 25 pruebas de continuidad: pasan.
- 4 pruebas de sincronización: pasan; comparan autoridad, publicación, artículo de tarjeta/impresión, enlaces y límite de información.
- Validador general: antes 66 errores; después 63. Solo desaparecieron los tres campos faltantes de #107 (`status`, `purpose`, `origin`); no aparecieron errores nuevos. Los otros 63 son anteriores y quedan fuera de alcance.
- Los datos semánticos de las otras 143 técnicas no cambiaron: SHA-256 `c98b69683bd38efa43a9ab9233ab79b5b15da9313a1ce3c4dc64fdfc0bb702d5`.
- El manifiesto global conservó SHA-256 `ef741863600b59b4116e8c011aa7c1e6f33787e64574e7e6edbdb63750225859`; no se regeneró el índice.
- Las vistas de Kairu y Nerum conservaron sus bytes tras ejecutar el generador.
- `git diff --check` pasa en Design, Publications y Narrative Engine.

## Pendientes explícitos

- Balance empírico de frecuencia de cambio, preparación previa y valores por rango.
- Port al motor de simulación: el YAML y las pruebas documentales no implementan ejecución ni evaluación de recuerdos.
- Parejas EN de #107 y capítulo 06 Panin: no se encontraron archivos correspondientes; traducción pendiente.
- Revisión visual e impresa de la tarjeta y hoja de cinco páginas. La igualdad de HTML y los controles estructurales no prueban ajuste, legibilidad o ausencia de recortes. No se declara terminada la producción de impresión.

Se conservaron cambios previos de los repositorios; no se hicieron commits ni push
porque los archivos de autoridad compartían modificaciones anteriores ajenas a esta sincronización.
