# Ejecución de inspección y papel de la IA

El creador pidió ejecutar lo existente para mirarlo y precisó que GM, personajes,
propuestas semánticas de registro y transformación a prosa deben ser interpretados
por IA. Se documenta la frontera con código y se prioriza la primera integración
de llamadas/instrucciones por rol, sobre el soporte existente, antes de completar
todos los subsistemas mecánicos.

Se añade `tools/preview_runtime.py`: ejecuta el intercambio fijo ya existente,
valida y reabre SQLite, y genera una vista HTML y un informe Markdown del creador.
Reúne tres perfiles reales sin escena y cuatro vistas del intercambio sintético.
Se comprueba que la nota privada no aparece en el contexto del GM.

Salidas locales privadas, excluidas de Git mediante `.local-runs/`:
`2026-11-04-inspection-review/index.html`, `inspection.md` y `synthetic.sqlite3`.
No hubo llamadas a modelos, dados aleatorios o decisiones de campaña.

El intento de apertura HTML con Browser Use fue rechazado por su política de
protocolos: no admite archivos locales `file:`. No se elude el bloqueo mediante
servidor local u otro navegador. Se solicita abrir el informe Markdown como archivo
en el panel de Codex; el conector devuelve estado `queued`.
