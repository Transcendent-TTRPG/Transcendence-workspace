# Neutralizadores alquímicos — soporte compartido

## Header

- `work_id`: `2026-10-14-neutralizadores-alquimicos`
- `owner_workflow`: `status-family-workflow`, countermeasures de venenos mediante poison-authoring.
- `linked_workflows`: dependency-review; técnica Bufoni 06 La dosis perdida; core-sync para sincronización ES y registro explícito de traducción pendiente.
- `status`: `authored`, 2026-10-15; reglas compartidas y tres fórmulas registradas en autoridad y publicación ES. Sin port runtime ni validación experimental de equilibrio.
- `family_outcome`: `family_defined`, alcance acotado: gramática compartida y un tipo compatible con tres calidades. No catálogo completo de antídotos.

## Scope

- Definir productos preparados de Alquimia antes de registrar La dosis perdida.
- Heredar el acuerdo existente: compatibilidad por tipo de veneno; calidades Común/Rara/Excepcional; cubrir calidad igual o inferior del tipo compatible; capacidad externa de una dosis por una dosis.
- No reconstruir todo el catálogo antiguo ni imponer equivalencias entre calidad, Índice Alquímico y severidad.
- No conceder antídoto universal, fabricación instantánea, curación automática, inmunidad ni neutralización de Tauma.

## Sources and baseline

- Capítulo 10 ES 05-alquimia: fórmula, reactivos de criatura y botánicos, índice mínimo, fabricación en instalación fija; tres rarezas con 12/24/36 horas y 1d4/1d3/1d2 dosis.
- Capítulo 11 ES 04-venenos: identificación, vías, manipulación y tratamiento; Kit de Medicina y excepciones de cada veneno.
- Baseline de Materials-and-fabrication, docs y YAML: fórmulas aceptaban other_alchemical_compounds y requerían salida, rareza, reactivos, plantas, índice y dosis. Este pase integra el catálogo acotado de neutralizadores.
- Ailments, docs/YAML: toxic life cycle y neutralización como countermeasure propia de Veneno.
- Fuentes ES de fórmulas y agravios no están plenamente alineadas: no equiparar automáticamente un nombre de agravio a una receta química concreta.
- Workflow-execution, status-family-workflow y dependency-review; poison-map/poison-checks.

## Phase checkpoints

### 0. Intake

- El creador propone definir primero los productos y luego asentar la técnica.
- Técnica mantiene nombre, ejecución y coste aceptados; borrador completo pendiente de revisión y registro.

### 1. Family boundary — corrección aceptada el 2026-10-15

- Familia específica de productos químicos preparados para neutralizar un tipo de veneno, no para borrar cualquier agravio de igual severidad.
- El creador rechaza ofrecer un modo externo ordinario en la entrada del producto: ese permiso es precisamente lo que aporta La dosis perdida. Se descarta la propuesta anterior de dos modos autónomos de uso.
- La entrada del producto describe capacidad química por tipo/calidad y su empleo como recurso de tratamiento. La fórmula describe fabricación. La técnica concede la aplicación excepcional sobre una dosis externa durante el ataque.
- Disponer del compuesto no sustituye Medicina, kit, acceso al paciente, procedimiento ni requisitos particulares del veneno. No cura heridas ni revierte automáticamente lesiones causadas.
- El permiso externo 1:1 se conserva en la técnica; no se publica como una acción gratuita o genérica del producto ni como prevención sostenida frente a dosis nuevas.

### 2. Grammar — base parcial

- Tipo de veneno compatible, calidad, reactivos, plantas, índice mínimo, fórmula, tiempo, rendimiento, presentación, dosis y usos permitidos.
- Compatibilidad/tres calidades y consumo clínico de una dosis por intento aceptados; relación externa 1:1 propiedad de la técnica. Ingredientes, índice y presentación todavía no aprobados.
- Distinguir nombre del compuesto, efecto tóxico y vía; la vía sola no determina compatibilidad.

### 3–7. Resolution, dependencies, balance, simulation and editorial

- Producto sin modo externo ordinario propio; tratamiento clínico hereda Medicina, que sí puede utilizarse bajo presión. No declarar que toda neutralización ordinaria sea imposible en combate.
- La técnica compra la reacción anterior a la defensa, no la existencia exclusiva del producto.
- Conservación, manipulación y consumo deberán heredar las reglas que correspondan sin inventar inmunidad al manipular venenos.
- El consumo clínico 1 dosis por intento fue propuesto por separado y aceptado por el creador; no se dedujo de la capacidad externa. No equivale a un éxito automático ni a curar simultáneamente todos los venenos.
- Kits de tratamiento y excepciones publicadas deben preservarse. Calidad/dosis ausentes de fuentes viejas requieren puente explícito, no conversión tácita desde severidad.
- `runtime_gap_classification`: `new_subsystem`: inventario tipado de compuestos, compatibilidad, consumo de dosis y resolución clínica no portados. La autoridad ya está formalizada; no mantener authority_blocked ni confundir registro con runtime. Revisión acotada de modelos/engine sin interfaz de neutralizadores encontrada.
- Equilibrio experimental y precios todavía pendientes; no fijar costes de fórmula/mercado sin revisar su familia de salida. Los precios no son requisito para fabricar y usar las fórmulas registradas.
- Destinos posteriores: Alquimia y tratamiento en ES, autoridad de materiales/afecciones y datos, con alcance de sincronización explícito.

## Regla compartida — registrada

### Neutralizador específico

Compuesto alquímico preparado para neutralizar un tipo concreto de veneno. Cada producto identifica el veneno compatible y su calidad. No actúa sobre otros venenos solo porque compartan vía de administración, síntomas o severidad.

| Calidad del neutralizador | Calidad de la preparación compatible que puede neutralizar |
| --- | --- |
| Común | Común |
| Rara | Común o Rara |
| Excepcional | Común, Rara o Excepcional |

Para emplearlo en un organismo envenenado, necesitas el Kit de Medicina y el procedimiento que requiera ese veneno. Realiza la T.E. de Medicina correspondiente. Con éxito, neutralizas el veneno compatible y cesan sus efectos activos. No recuperas automáticamente heridas ni otros daños que haya causado. Una calidad superior no sustituye un kit ni rebaja por sí sola la dificultad.

Consumo clínico aceptado por el creador: una dosis administrada permite un intento de tratamiento de un veneno compatible en una criatura, y se consume aunque la T.E. falle. Un fallo no elimina parcialmente el veneno ni autoriza repetir la tirada sin cumplir las reglas de reintento de Medicina. Si faltan compatibilidad, calidad o recursos de tratamiento, no hay un intento válido; no asumir gasto automático por comprobar esos requisitos.

Este producto no concede una aplicación reactiva sobre armas. Ese uso debe proceder de la técnica que lo autorice. Tampoco reemplaza otros tratamientos expresamente autorizados ni convierte su compra en un requisito nuevo para todos los métodos de neutralización existentes.

Nota editorial: no convertir esta tabla en Común = Leve, Rara = Moderada y Excepcional = Grave. Calidad describe la preparación; severidad describe el agravio. Cada veneno conserva sus excepciones de recuperación.

## Primera fórmula — aceptada en discusión

### Neutralizador del Veneno de Confusión — Común

Se elige como primera prueba una preparación tóxica ya publicada con identidad y rareza explícitas: Veneno de Confusión, capítulo 10, fórmula Común. No crear un neutralizador universal de Desorientado ni equiparar esta fórmula antigua a un veneno del capítulo 11 sin revisión.

| Campo | Acuerdo / origen |
| --- | --- |
| Tipo compatible | Solo Veneno de Confusión, preparación Común publicada |
| Calidad / rareza de fórmula | Común; aceptada para este neutralizador |
| Vía clínica | Ingestión; aceptada, no establece modo externo ordinario |
| Reactivo de criatura | Fluido (1); aceptado |
| Reactivos botánicos | 2 unidades de plantas; aceptadas |
| Índice botánico mínimo total | 8; aceptado, no valor heredado del veneno ni de su identificación |
| Fabricación | 12 horas de progreso; rendimiento 1d4 dosis, heredados de fórmula Común |
| Instalación | Alambique u horno fijo, según capítulo 10; no fabricación instantánea |
| Prueba de fabricación | Alquimia, Desafiante por reactivo principal Fluido; proceso publicado |

Los insumos son unidades abstractas del sistema, no una receta química real. Se usa el esquema de Fluido (1), 2 plantas e índice 8 ya presente en la Cataplasma Estabilizadora como referencia de carga material; que coincidan no hace intercambiables las fórmulas ni demuestra balance. La fórmula documenta la preparación específica del neutralizador.

Efecto de producto aceptado: permite intentar neutralizar el Veneno de Confusión compatible mediante Medicina y el Kit de Medicina correspondiente. Con éxito, termina ese envenenamiento y cesa la desorientación que produzca; no elimina Desorientado procedente de otras causas. Una dosis se consume por intento, aunque falle. No reduce por sí sola el umbral de Medicina ni reemplaza recursos/procedimientos.

No se deduce un grado de kit o dificultad clínica universal de este índice botánico. El creador aprobó después un perfil local para la preparación Común publicada: kit Básico, Medicina Desafiante y tratamiento activo 6/1. Se registra sin reformar los demás venenos ni deducir calidad de su severidad.

Conservación del producto terminado aceptada y registrada abajo. Precio de producto no establecido; no tomar el coste de comprar una fórmula como precio por dosis.

## Variantes de calidad — progresión aceptada

Mismo tipo de veneno compatible y vía clínica de ingestión. Cada variante exige su propia fórmula; disponer de la fórmula Común no concede automáticamente acceso a las otras. Se registra capacidad de producto, no nuevas versiones del Veneno de Confusión: la única preparación tóxica de ese nombre verificada en el catálogo actual es Común. No inventar raridades adicionales de la fuente tóxica ni compatibilidad con otros compuestos para darles uso.

| Campo | Común aceptada | Rara aceptada | Excepcional aceptada |
| --- | --- | --- | --- |
| Reactivo de criatura | Fluido (1) | Glándula (1) | Sistema nervioso (1) |
| Unidades botánicas | 2 | 3 | 4 |
| Índice botánico mínimo total | 8 | 15 | 24 |
| Horas de progreso | 12 | 24 | 36 |
| Dosis por lote | 1d4 | 1d3 | 1d2 |
| Dificultad de fabricación | Desafiante | Exigente | Extrema |

Horas/rendimiento heredan rareza. Las dificultades corresponden también a las categorías de reactivo principal de capítulo 10, evitando inventar una excepción entre tabla de reactivos y rarezas. Reactivos, cantidades botánicas e índices de las variantes fueron aceptados por el creador; no son un escalado heredado ni balance experimentalmente validado.

La progresión exige materias menos accesibles y mayor carga botánica por dosis; no suma resultados de Medicina, no sustituye kits ni cura varios venenos. No se añade una regla de combinación automática de dosis entre calidades. Cada fabricación conserva su requisito de fórmula.

## Últimos detalles — aceptados y registrados

- Presentación: preparado líquido por dosis, en recipiente sellado. La vía de tratamiento sigue siendo ingestión; no añadir un modo externo propio al producto.
- Conservación: producto terminado Estable mientras se conserve en recipiente sellado, sin contaminación y en condiciones normales de almacenamiento. No hereda automáticamente la caducidad/volatilidad de sus insumos crudos ni añade un contador de días. Propiedad aceptada para estas fórmulas, no regla global de todos los compuestos. Exposición destructiva sigue las reglas generales; no implica inmunidad al entorno.
- Tratamiento de la preparación Común publicada del Veneno de Confusión: Kit de Medicina Básico y T.E. de Medicina a dificultad Desafiante, con los modificadores de escena de Medicina. Concreción local aceptada; no deducida del índice botánico 8.
- Bajo presión ATB: procedimiento activo de tratamiento asistido/técnico a 6 Ritmo / 1 Desgaste, aprobado para este método. No reacción; no sustituye la defensa ni neutraliza una dosis en el arma. Se consume una dosis administrada incluso si falla la T.E.
- Una calidad superior de neutralizador usada sobre el mismo veneno Común no aumenta el kit, no rebaja el umbral ni cambia el coste del procedimiento. No se definen aquí tratamientos de variantes tóxicas Raras/Excepcionales aún inexistentes.
- Fuera del ATB, conservar Medicina y sus requisitos de acceso/tiempo de intervención en ficción; no inventar estrés ni Desgaste por una escena de tratamiento tranquila.
- Tres productos y gramática compartida registrados. La técnica sigue sin registro final, sujeto además a revisión de su borrador completo.

## Integración realizada

- Datos: `Transcendence-design/data/system/materials-and-fabrication.yaml`, `alchemy.poison_neutralizers`.
- Referencias: `docs/system/materials-and-fabrication.md`, enlace de propiedad en `ailments.md`, índice y superficies en `mechanics-overview.md`.
- Decisión: `Transcendence-design/docs/adr/alchemy-poison-neutralizers.md`.
- Recuperación compacta: concepto, decisión y dominio de consulta en los tres registros de `data/knowledge/`.
- Glosario ES/EN de Neutralizador específico y Neutralizador del Veneno de Confusión.
- Publicación ES: capítulo 10 Alquimia, tabla, procedimiento y ejemplo; capítulo 11 Venenos enlaza ese recurso sin cambiar sus entradas.
- `sync_outcome`: `multi_section_mechanical_sync`, ES completado; EN diferido expresamente. Capítulo 10 EN solo tiene README; capítulo 11 EN conserva una versión previa con catálogo pendiente. No fabricar una traducción parcial que parezca un capítulo completo.
- No se modificó `techniques.yaml`, no se creó tarjeta/ID nuevo y no se asignó aprendizaje a Seku.

## Pendientes tras el registro

- Traducción EN de los pasajes integrados, dentro de la traducción pendiente del capítulo y de la paridad de Venenos.
- Portar a simulación y ejecutar escenarios/preguntas de equilibrio si se requiere; no parte del registro actual.
- Precios comerciales, nuevos tipos compatibles o versiones más potentes de fuentes tóxicas solo cuando se diseñen. Una fuente sin calidad debe definirla; no se admite deducirla de severidad.
- Retomar revisión del borrador completo de La dosis perdida antes de su integración Core → Card → YAML.

## Validation and acceptance

- Taxonomía, dosis, fórmulas, tratamiento local, conservación, permisos y enlaces: pass, 14 pruebas específicas de registro/publicación (`pipeline/tests/test_poison_neutralizers.py`). No pruebas de motor.
- Loader: pass, YAML sin claves duplicadas en datos y registros editados. Runtime/escenarios: no implementados/no ejecutados; gap `new_subsystem`.
- Preservación: pass, huellas semánticas de los datos/registros previos intactas al excluir las adiciones; ambos manuscritos previos intactos al retirar las secciones/metadatos añadidos; `techniques.yaml` y `pipeline/manifest.json` sin cambios en este pase.
- Editorial: escaneo de solo lectura, 305 archivos, 611 errores previos y 220 advertencias (antes 221). Persiste el error preexistente de falta de par EN de Alquimia; no se marca final/review ni se regenera manifest.
- `git diff --check`: pass en ambos repos y workspace.
- `authority_updated`: sí; `publication_updated`: ES sí, EN diferido; `yaml_updated`: sí; `sim_updated`: no.
- `pending_items_explicit`: sí.
- Familia registrada en autoría para el alcance aprobado; no declarar cerrada la traducción, la simulación o el equilibrio. La técnica no se marca authored por tener ya disponible este soporte.

## Change impact

- Corrección del creador conservada: el producto no ofrece dos modos de uso autónomos. Regla de tratamiento y tres fórmulas aprobadas registradas en datos, referencias, glosario y publicación ES.
- Datos previos, fórmulas ajenas, agravios, manifest, técnica y material narrativo preservados.
- Pruebas específicas añadidas; runtime/traducción y precios comerciales no completados ni fingidos.
- Próximo paso: revisión del texto completo de La dosis perdida con el soporte ya registrado.
