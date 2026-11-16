# Broker local: persistencia y contextos

Fecha: 2026-11-04. Trabajo autorizado tras aprobar el ejemplo y formatos versión 1
de circulación de información. Cambios en `Transcendence-narrative-engine`;
no se cambian los rosters, publicaciones, módulo fuente ni datos del ejemplo.

- Biblioteca Python estándar `narrative_engine`: diario SQLite con transacciones
  atómicas, control de revisión e idempotencia persistente de envíos. Conserva
  también las instantáneas de entrada y el manifiesto del ejemplo con sus hashes.
- Validación previa de fuentes, destinatarios, recepción efectiva, separación de
  acciones/notas, eventos, cambios de estado y evidencia aritmética de T.C.
- Broker con contextos ligados a cada rol, selección explícita de campos y
  reconstrucción por tiempo ficticio o revisión de almacenamiento.
- Puertos de actor y GM separados. El actor envía acción y/o nota privada; el GM
  recibe manifestaciones y no puede escribir el cuaderno mental o las elecciones
  del actor. No hay llamadas a modelos ni aislamiento de sus herramientas todavía.
- Adaptador de reproducción del ejemplo aprobado, sin generar tiradas o historia.
  Compara los ocho contextos guardados antes y después de reabrir la base.

Validación: 27 pruebas nuevas del almacenamiento/Broker y 13 del ejemplo, todas
correctas; comprobador estático correcto (20 registros, 5 eventos, 19 entregas,
8 vistas). Incluye fallo de escritura simulado, reintento tras reabrir, rechazo de
revisión obsoleta, notas privadas, entregas no autorizadas y conservación de tiradas.

SQLite es la fuente persistente de esta versión, en lugar de confirmar varios
JSONL independientes. Los formatos y vistas aprobados se conservan como referencia.
No hay migración de las hojas reales, memoria recobrada, progreso de personajes,
selección de historia ni promoción al canon. Faltan integración GM/actores,
herramientas aisladas, continuidad mutable y gestión del contexto de historias largas.
