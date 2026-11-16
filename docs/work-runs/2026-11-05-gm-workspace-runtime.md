# Vista de trabajo y consultas locales del GM

Fecha: 2026-11-05.

Se implementan `GMPort.context_window()`, `recall()` y `read()` sobre proyecciones
permitidas del mundo, hojas actuales, preparación, manifestaciones recibidas,
entregas, eventos, continuidad y pendientes. No se consultan notas interiores ni
respuestas crudas de actor. Las escrituras privadas y respuestas solo mentales no
cambian las vistas ni consultas del GM. La vista exige semilla 2 o posterior para
conservar el reloj público separado; las ejecuciones antiguas no se migran.

La vista conserva el núcleo seleccionado, todos los pendientes con evidencia y
referencias fijadas; el historial opcional entra bajo presupuesto de caracteres.
Se recuperan elementos enteros, sin resúmenes semánticos o recortes silenciosos.
La selección de relaciones descritas en prosa sigue requiriendo atención del GM.

`gm_sources.py` y el generador de bibliotecas leen los perfiles y registros existentes
de Publications para congelar fuentes españolas, técnicas y decisiones aprobadas.
El paquete se incorpora a los insumos de una ejecución nueva. Las consultas trabajan
con esos snapshots, conservan autoridad/hash/líneas y no leen fuentes vivas o rutas
arbitrarias. Se verificó también un paquete de 15 fuentes con las reglas del roster
real, incluidas Formix, Loxod, Panin y las técnicas del libro separado.

Se actualiza la procedencia del generador de perfiles y se refrescan sus cinco
artefactos conocidos. Las vistas de apertura siguen coincidiendo con los rosters;
no se generan recuerdos, escenas o progreso. No se modifican manuales ni campaña.

La inspección técnica queda en `.local-runs/2026-11-05-gm-workspace/` del motor:
informe Markdown, vista y consultas JSON, SQLite sintético y paquete privado de
fuentes del roster. La prueba conserva una T.C. fija pendiente, preparación distinta
de existencia oculta y ausencia de pensamiento privado. Se verifica reapertura.

Se añaden pruebas del espacio y fuentes y se conservan los comprobadores de perfiles,
continuidad, intervenciones e información. La documentación de implementación
`docs/gm-workspace-runtime.md` distingue estas operaciones locales de su futura
exposición a un agente. No hay modelos, dados aleatorios, integración aislada,
revisión estructurada de intenciones o simulador de procesos fuera de escena.

Validación final: 185 pruebas pasan en siete conjuntos (29 nuevas del espacio
del GM y 156 existentes). El ejemplo estático y la vigencia de los cinco perfiles
generados también pasan. El conjunto previo del Broker emite un `ResourceWarning`
por una conexión no cerrada en una ruta de prueba; no se modifica ese comportamiento
ajeno al incremento. Se revisan además formato, enlaces locales y sintaxis de los
archivos nuevos.
