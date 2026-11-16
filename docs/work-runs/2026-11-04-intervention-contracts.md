# Contratos ejecutables de intervención

Fecha: 2026-11-04. Trabajo autorizado para formalizar mensajes, estados pendientes
y confirmaciones del circuito diseñado. Cambios en Narrative Engine y este registro;
no se modifican protagonistas, módulo, canon o fuentes de reglas.

- Se añade `InterventionController` y validación estricta de mensajes versión 1
  sobre ejecuciones con semilla de diario versión 2. El contenedor SQLite conserva
  sus tablas y las ejecuciones antiguas no se migran automáticamente.
- Contextos autorizados persistidos por intervención; respuesta ligada al actor,
  manifestación y nota separadas; solicitud y evidencia T.C. congeladas antes de
  interpretar; propuestas y confirmaciones atómicas.
- Reacciones habilitadas por el GM, revisión explícita del alcance de evidencia
  después de cambios del mundo, cancelación solo previa a respuesta y pausa/reanudación
  para revisión sin perder lo ya aceptado. No se implementa un planificador narrativo.
- Versión 2 impide que una nota privada avance el reloj público o cambie las vistas
  del GM y otros actores. La vista de pendientes del GM excluye contexto, hashes,
  cuaderno, presencia de notas y revisiones globales.
- Ensayo fijo en `examples/intervention-flow` y reproductor que reabre el diario.
  Verifica reacción, comunicación parcial y resultado sin generar historia de campaña.

Validación: 32 pruebas nuevas de intervención, 27 del Broker y 13 del ejemplo
aprobado, correctas. Las ocho vistas originales también se reproducen con semilla
versión 2. Se prueban errores de destinatario/versión, reloj privado, pausa,
evidencia inmutable, propuestas obsoletas, fallo de escritura y reanudación.

Pendientes: ejecución de modelos y aislamiento de herramientas, dados aleatorios,
otros tipos y secuencias de pruebas, contratos de cambios personales y adaptador
de perfiles reales. La evidencia nueva del ensayo usa un dado fijo identificado;
no es aleatoriedad real. Los objetos Python siguen perteneciendo al controlador
de confianza. S0/S1/S4 no se declaran cerradas.
