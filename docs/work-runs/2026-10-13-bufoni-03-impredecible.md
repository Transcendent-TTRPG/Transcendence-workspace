# Tercera técnica Bufoni — El rastro ofrecido

## Header

- `work_id`: `2026-10-13-bufoni-03-impredecible`
- `owner_workflow`: `technique-workflow`
- `linked_workflows`: `technique-play-surface-workflow`; simulación pendiente.
- `artifact_type`: `technique`
- `status`: `authored`; nombre, rango Novato, entrada completa y coste 2/1 aprobados por el creador el 2026-10-13. Registro central y superficies incorporados; sin validación empírica ni visual.

## Scope

- `species`: Bufoni como origen cultural; no fijar requisito racial.
- `technique_id`: 164; único, posterior al máximo publicado y central 163.
- `goal`: discutir una sola técnica nueva, después de 162 y 163.
- `current_state`: core ES/EN, tarjeta, impresión, YAML y referencia humana sincronizados con la regla aprobada.
- `out_of_scope`: otras técnicas, implementación de simulación, concesiones a Seku, cambios al módulo o biografías y reparación del pipeline, catálogo histórico o doctrina global de Oculto.

## Mandatory sources

- authority docs/data: definición Unpredictability en `weapon-technique-profiles.md` y `.yaml`; registros centrales que exigen ese perfil, contrastados con publicación.
- seeds/canon: capítulo 6 ES `14-bufoni.md` como identidad principal; `docs/canon/species/bufoni.md` como complemento, sin importar sus discrepancias de longevidad o cosmología como hechos nuevos.
- knowledge references: `docs/knowledge/SOURCE-OF-TRUTH.md`, workflows de ejecución/técnicas/presentación, template de ficha, skills de autoría y presentación y sus referencias de routing/checkpoints. Dominios generales e Intuición/Engaño consultados para separar engaño físico, lectura y control mental; no se adopta un origen de especialización.
- simulation references: `sim/engine/concealment.py`, `effects.py`, `activations.py`, `reactions.py`, `models/concealment_state.py`, `policies/base.py`, `tests/test_concealment.py` y experimento `run_hidden_crossing_iteration`; inspección, no portado ni prueba del nuevo runtime.
- publication references: técnicas 6, 73, 139; comparaciones 8, 89, 111, 114, 121, 130, 132, 148, 152, 155, 157, 162 y 163; capítulo 8 ES, Reacciones y `07-cobertura-visibilidad-y-ocultacion.md`; autoridad `cover-visibility-concealment.md` y datos correspondientes, secciones de Oculto/detección.

## Phase checkpoints

### Phase 0. Intake

- `scope_recorded`: una por vez, primero discusión.
- `main_question`: cómo dirigir una pista de localización equivocada sin anular la detección real ni repetir la supresión de señal de Golpe Sin Eco.
- Acceso del pase ya establecido: lengua con Torsión, Interrupción, Impredecible y Corrosión. Armadura y resistencias entrenadas no fijadas. Saltar/Nadar/Sigilo vinculados al legado, no competencias universales.

### Phase 1. Species Framing

- `fantasy`: dejar una señal física real cuyo origen aparente haga buscar al detector en un punto equivocado, mientras la posición corporal sigue sin localizarse.
- `world_origin`: paciencia, emboscada y control de lo que el intruso alcanza a interpretar; útil tanto para defensores/cazadores como para infiltrados. No fijar dominio, escuela o maestro.
- No confundir Impredecible con azar o conducta caótica: es una ejecución deliberadamente difícil de leer.
- `why_not_base_action`: sustituir, mediante una ejecución entrenada, la posición falsa aleatoria del procedimiento de Ocultación por un punto elegido de antemano y físicamente justificado. No basta con describir una distracción; la regla define qué pista recibe el detector.
- `interaction_surfaces`: ocultación, información de localización y geometría del señuelo en ATB.
- No proyectar Tauma, ilusión, control mental, un veneno propio ni una orden obligatoria al enemigo.

### Phase 2. Mechanical Framing

- `category`: utilidad reactiva de arma, aprobada como parte de la resolución.
- `roll_model`: aprobado: T.A. de Impredecible enfrentada a la Percepción del detector, usando su mismo resultado de Percepción para las comprobaciones. Se mantiene la comparación original Percepción frente al valor activo de Oculto; la técnica no reemplaza ese valor. Empate favorece Oculto en detección, pero no basta para superar Percepción con esta intervención.
- `competency_source`: arma con Impredecible, competencia Novato o superior; accesible con herramienta fabricada compatible.
- `effect_model`: aprobado: controlar una posición falsa, no obligar a reaccionar o moverse. Resolver una localización de un solo detector por uso, sin impacto ni efectos propios del arma.
- `duration_model`: Instantáneo, aprobado con el coste; se resuelve qué información recibe el detector en ese intento, no una condición sostenida de engaño. La pista no lo obliga a creerla para siempre ni limita futuras búsquedas.
- `restrictions`: aprobadas: punto falso alcanzable mediante el arma y una señal físicamente plausible para el sentido usado por el detector; no recrear señales sin soporte, borrar evidencia clara ni bloquear otros sentidos. No alterar la detección previa de una acción ni otorgar automáticamente ventaja de apertura. Declaración antes de conocer el resultado de Percepción.

Resolución aprobada por el creador:

1. Antes de resolver un intento de localizarte mientras estás Oculto respecto a ese detector, declara la técnica y el punto de la señal falsa. No esperar a conocer si su Percepción acertó; se preserva la incertidumbre de las tiradas secretas.
2. Genera la señal mediante el arma con Impredecible y realiza T.A. El detector resuelve su Percepción habitual; no una segunda Percepción por esta técnica.
3. Si Percepción supera el valor activo de Oculto, localiza tu posición real, aunque tu T.A. sea superior. La técnica no revierte una detección exitosa.
4. Si Percepción no supera Oculto y tu T.A. supera Percepción, recibe como pista la posición falsa declarada en vez de la determinada por 1d8.
5. Si Percepción no supera Oculto pero tu T.A. tampoco supera Percepción, se resuelve la posición falsa por el procedimiento ordinario. Fallar esta técnica no revela automáticamente tu cuerpo ni mejora el valor activo de Oculto.

- La criatura decide qué hacer con la información; no ataques, movimiento, gasto de acciones ni pérdida de técnicas impuestos.
- Las condiciones físicas que sostienen Oculto siguen siendo necesarias. Los demás observadores se resuelven normalmente; una señal también puede comprometer el ocultamiento ante ellos según las reglas existentes.
- No rescatar a alguien ya localizado, ignorar detección automática de un sentido específico ni proteger contra un área que cubra el cuerpo real.
- Un intento por esta localización, sin repetir la técnica hasta lograr dirigir la pista; Ritmo 2 / Desgaste 1 aprobados, también si no se consigue dirigir la pista.

### Phase 3. Dependency Framing

- `upstream_dependencies`: Oculto por enemigo, valor activo preservado, Percepción estrictamente superior para localizar, pistas falsas por 1d8, alcance/sentido aplicable y declaración previa a tiradas secretas. Hay una divergencia anterior en YAML que describe volver a tirar Oculto; no importarla sobre la regla ES de conservar el valor activo ni reparar esa autoridad en este pase.
- `downstream_dependencies`: entrada ES/EN, tarjeta, autoridad y referencia humana incorporadas después de aprobación.
- `blockers`: no bloquea autoría; falta el pipeline ejecutable de localización/pista percibida y revisión visual. El nuevo registro preserva el valor activo de Oculto de la regla aprobada, sin reparar la divergencia previa en los datos generales de detección.
- `linked_files`: fuentes anteriores; no modificadas.
- La reacción no debe simplemente cancelarse después de declarada: repetiría la salida de 162 con otra justificación. Tampoco cambiar el destinatario de un golpe real: ya es 163.

### Phase 4. Balance Framing

- `cost_sanity_note`: doctrina y tabla maestra leídas completamente. Ritmo 2 / Desgaste 1 aprobados por el creador, también si la intervención falla o la detección original tiene éxito. Una microconversión informativa inmediata sobre un detector; genera una señal física y exige coordinación temporal, por lo que no corresponde Ritmo 0. Un resultado principal, sin daño, condición, movimiento forzado ni negación de detección; no se justifica Desgaste 2 por tener dos comprobaciones.
- Comparación de coste: 69 Pasar Como Parte del Fondo, 3/1, permite cruzar una línea manteniendo/ganando Oculto frente a observadores; 6 Robar el Ángulo, 4/1, compra movimiento y posible Desequilibrado; 111 Golpe Sin Eco, 0/2, suprime la señal por una capacidad innata, no es benchmark temporal para una manipulación voluntaria; 117 Saturación, 2/1, ilustra una utilidad condicional de efecto inmediato, no una equivalencia funcional. La tabla también usa 2/1 para microconversiones estrechas; su fila 65 no coincide con el coste publicado 0/2 de Tirar la Advertencia, por lo que no se importa ese valor como hecho uniforme.
- 3/1 queda como alternativa a comparar si el control espacial del punto muestra mucha utilidad o repetición. 2/1 está aprobado para autoría, no probado en balance.
- `sibling_comparison_note`:
  - 6 Robar el Ángulo, Naghii: activo; T.A. frente a Intuición, movimiento propio sin reacción del objetivo y posible Desequilibrado.
  - 73 Cobrar con la Otra, Zarnag: activo, dos armas; segundo ataque inmediato tras conectar el primero, posible Desequilibrado si ambos conectan.
  - 139 El Golpe Sin Eco, Vesper: activo; ataque sin señal detectable, elimina el bonificador de competencia de la defensa sensorial.
  - El YAML de Robar el Ángulo y Esconder la Segunda Línea conserva versiones diferentes del conjunto publicado. Se revisaron ambas: no duplicar penalización de respuesta futura o supresión de una defensa preparada bajo un nombre nuevo.
- Comparación funcional cruzada: 152 sustituye defensa por Engaño; 155 reduce T.D. mediante Imitación; 121 altera directamente ficha ATB tras golpear; 130 encarece Reacciones; 148/157/162 cancelan acciones o Reacciones; 111/114 conservan Oculto. Evitar usar cualquiera de esas salidas como novedad sin diferencia mecánica real.
- `pressure_note`: su valor depende de la utilidad espacial del punto elegido y de que el enemigo actúe sobre la pista. No fingir que comprar control de una pista equivale a ganar Oculto o cancelar una acción.
- `counterplay_note`: Percepción que localiza realmente, otro sentido no engañado, observación directa, nueva búsqueda, no seguir la pista y efectos de área. No conceder detección nueva gratuita a todo el entorno.
- Comparación actualizada: 111 suprime la señal y niega Percepción; 114 reposiciona para sostener Oculto; 132 concede Oculto sin cobertura física pero exige ausencia de visión directa; 8 degrada un canal sensorial mediante residuo. Aquí el canal sigue funcionando y se dirige una pista falsa solo si no hubo localización real. 139 elimina bonificador defensivo al detectar un ataque: tampoco equivale a localización incierta.

Precomprobación del conjunto publicado de armas naturales con Impredecible:

| Arma | Disparador y efecto |
| --- | --- |
| Lengua Bufoni | T.A. > T.D.; T.R. Veneno fallida aplica veneno del linaje, severidad por rango. |
| Bilis Yacani | T.A. > T.D.; T.R. Veneno fallida aplica Erosionado, severidad por rango. |
| Garras Lapinni | Impacto ignora Bloqueo por Competencia; no exige margen adicional en la entrada. |

La candidata sin impacto no debe entregar estos efectos. Hereda Efectos se decidirá tras definir categoría e impacto; una utilidad omite la etiqueta y debe indicar que no entrega un golpe propio.

### Phase 5. Simulation Framing

- `runtime_gap_classification`: `new_subsystem`, estimación conservadora para el pipeline faltante de localización/información, no un estado nuevo del juego. `engine/concealment.py` es un stub; el modelo y otorgamiento de Hidden sí existen. El experimento de cruce prueba tasas de detección, no eventos de intento, selección de posición falsa ni información percibida por políticas.
- `porting_state_target`: alcanzado `authored`; no `sim_defined`, `runtime_supported`, `policy_exercisable` ni `question_ready`.
- Soporte requerido: evento de localización con detector/sentido y declaración previa, punto físicamente plausible, Percepción reutilizable, valor activo de Oculto preservado, prioridad de detección real, pista elegida/fallback normal, guardas de intento y costes reactivos incluso sin efecto. Las políticas deben actuar sobre pistas percibidas, no coordenadas omniscientes. El objeto YAML `false_location_control` es un contrato, no un handler implementado.
- `scenario_seed_note`: Percepción > Oculto aun con T.A. mayor; empate de Percepción/Oculto; empate T.A./Percepción; ubicación elegida válida/inalcanzable; sentido no engañado; múltiples observadores; detección de acción sin localización corporal; futuras búsquedas y áreas sobre la posición real. Declaración previa a resultados secretos.
- `question_seed_note`: comparar 2/1 y 3/1 frente al procedimiento aleatorio sin técnica, con posiciones falsas de igual plausibilidad y acceso físico. Medir pistas aprovechadas, localizaciones reales, fallos de intervención, riesgo ante otros observadores, efectos sobre rutas/áreas, repetición y gastos realmente elegidos por el detector. Conservar ambos filtros y no modelar inmunidad a detección. Es una semilla guardada, no una pregunta ejecutable o un resultado.

### Phase 6. Editorial Framing

- `authority_cleanup_note`: registro 164 añadido; no se alteran los 139 registros anteriores ni datos globales de detección.
- `terminology_note`: nombre aprobado registrado en el glosario con The Offered Trail. Oculto y posición aproximada incierta ya existen; no se crea Engañado/Desorientado ni otro estado.
- `core_sync_note`: entrada aprobada ES y traducción EN con ejemplo de las tres ramas. Las guías de autoría/presentación mantuvieron separados el valor activo de Oculto, ambos usos de Percepción y ausencia de impacto propio. `status: draft`, `canonical: false`; no promoción editorial a final.
- Tarjeta condensada, artículo idéntico en la hoja de impresión parcial de cuatro cartas. Tipografía y tamaño compartidos sin cambios; espaciado local como las cartas previas.
- Visual pendiente: hubo denegación de acceso local por el navegador en el pase anterior. No intentar otro navegador, servidor local ni otro mecanismo para sortearla. QA estática no certifica ausencia de desbordamiento, fuentes cargadas ni impresión.

## Integration

- `files_changed`: core ES/EN 164; tarjeta/impresión Bufoni; YAML central; referencia humana y documento central de técnicas; catálogo de superficie; README ES; glosario; esta ficha.
- `sim_updated`: no.
- `core_updated`: sí.
- `knowledge_updated`: glosario y referencias humanas, sin nuevas biografías, escuelas ni estados.

## Validation

- `roll_integrity`, `exchange_integrity`, `atb_integrity`, `dependency_integrity`: `pass` documental de la resolución aprobada: una Percepción, valor de Oculto preservado, empates diferenciados, declaración previa y ausencia de impacto propio. No prueba de runtime.
- `balance_sanity`: `blocked` para cierre empírico; coste 2/1 aprobado para autoría, sin simulación ejecutada.
- `surface_integrity`: `pass` estático: HTML equilibrado, IDs SVG únicos, iconos y CSS existentes, artículo idéntico individual/impresión y tres cartas previas conservadas literalmente. Revisión visual pendiente.
- `ailment_integrity`, `critical_break_integrity`: `not_applicable`; no agravio, impacto ni ruptura propios. No heredar efectos del arma en esta utilidad.
- `loader_validation`: `pass` enfocado: ID único, esquema completo, coste 2/1, rango/tier y contrato concordantes. El validador global sigue fallando con los mismos 66 errores previos y 0 advertencias, sobre 140 registros centrales y 21 de simulación; no hay errores del registro 164.
- `publication_consistency`: `pass` enfocado: efecto ES idéntico al aprobado salvo formato; cabeceras/costes/referencias ES/EN válidos; traducción revisada manualmente. No equivalencia semántica demostrada por un motor.
- Conservación central: al excluir 164, SHA-256 semántico `e41ad76857b609e847662ac5010797e04f6d732333e37801372a9da1e4a370b4`, idéntico al previo: 139 registros y metadatos sin cambios.
- Indexador editorial: ambos archivos tienen pareja real y enlaces válidos. Su comprobación ES solo acepta enlaces bajo `core-books/transcendence-corebook/`, por lo que añade un falso positivo para esta pareja en `transcendence-techniques/`. No se añade una referencia ficticia ni se modifica el indexador. Resto de comprobaciones enfocadas sin errores/advertencias; búsqueda con `--search`, sin escribir el manifiesto.
- `simulation_integrity`, `scenario_validation`, `question_validation`: `blocked`; no portado ni experimentos.
- Revisión de no-solapamiento completada para proponer la dirección; deberá repetirse sobre el efecto concreto antes de aprobarla.

## Acceptance closure

- `authority_updated`, `yaml_updated`, `core_sync_done_or_not_needed`: sí.
- `coverage_updated`: no; no cobertura de runtime ficticia.
- `sim_defined_or_gap_classified`, `runtime_supported_or_gap_classified`: gap clasificado, no soporte implementado.
- `pending_items_explicit`: sí; discusión, no técnica cerrada.

## Pending items

- `pending`: revisión visual permitida, pipeline de localización, escenarios y pregunta de coste ejecutable. No está aprobada una versión que también dispute detecciones exitosas; ampliar a varios detectores o mantener un señuelo requiere nueva discusión. Catálogo histórico, metadatos antiguos, regla general de conservar Oculto y falso positivo del indexador quedan fuera de este alcance.

## Change impact

- `concepts_touched`: control de localización incierta desde la identidad Bufoni, con el estado Oculto existente.
- `decisions_reinforced_or_created`: doble filtro y dirección de pista falsa aprobados; no reversión de detección exitosa, origen no requisito racial, una técnica por vez y no concesión automática a Seku.
- `coverage_movement`: ninguno.
- `follow_up_work`: revisar esta incorporación antes de abrir otra técnica.

## Entrada completa aprobada

Registro del texto aprobado por el creador, no autoridad paralela. La entrada mantenida para lectura es el core ES 164. No se concede la técnica a Seku.

## El rastro ofrecido

### Reactivo - Utilidad

**Rango Novato**

*Las garras encuentran hojas.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | 1 Criatura | Instantáneo | T.A. |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| — | — | 2 | 1 |

### Requisitos

- Competencia Novato o superior con el arma utilizada.
- Arma con perfil Impredecible.
- Estar Oculto respecto al detector.

### Palabras clave

- Impredecible
- Oculto

### Efecto

Cuando un enemigo vaya a resolver un intento de localizarte, puedes declarar esta técnica antes de conocer el resultado de su Percepción.

Elige una posición falsa distinta de la que ocupas, donde tu arma pueda producir una señal físicamente plausible para el sentido que utiliza el detector. El alcance de tu arma limita el punto de la señal, no la distancia al detector; este debe poder percibirla según las reglas normales de detección.

Realiza una T.A. con tu arma de Impredecible, enfrentada a la T.E. de Percepción del detector. Utiliza ese mismo resultado de Percepción para resolver su intento habitual de localizarte frente al valor activo de tu estado Oculto. No vuelves a tirar ni reemplazas ese valor, y el detector no realiza una segunda Percepción por esta técnica.

Si su Percepción supera tu valor de Oculto, localiza tu posición real, aunque tu T.A. sea superior.

Si su Percepción no supera tu valor de Oculto y tu T.A. supera su Percepción, recibe como pista la posición falsa que elegiste, en lugar de la determinada mediante 1d8. Si tu T.A. no supera su Percepción, la posición falsa se determina por el procedimiento normal de Ocultación.

La criatura decide qué hacer con la pista. Esta técnica no la obliga a moverse ni atacar, no modifica tu valor de Oculto y no impide futuras búsquedas. No borra información obtenida por otros sentidos ni anula una detección automática.

Cada uso afecta un solo intento de localización de un detector. Solo puedes intentar esta técnica una vez contra ese intento. Los demás observadores resuelven su detección normalmente; la señal puede comprometer tu ocultamiento frente a ellos según las reglas habituales.

Esta técnica no inflige impacto ni aplica efectos de tu arma, no concede ventaja de apertura y no te protege de áreas que cubran tu posición real.

Pagas Ritmo y Desgaste aunque no consigas dirigir la pista.
