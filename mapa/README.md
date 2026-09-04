# Mapa maestro

> **Documento local no normativo.** Las instrucciones completas de construcción, uso y límites del mapa están en `/INSTRUCCIONES.md`.

Esta carpeta contiene la capa semántica de Paradigma.

Su función es orientar desde una pregunta o tarea hacia los pasajes correctos del corpus, conservando proveniencia, evolución conceptual y correspondencias entre lenguaje ontológico, formal y aplicado.

Flujo esperado:

**mapa → localizador → texto real → respuesta o producto**

El contenido de esta carpeta es derivado y nunca sustituye a `corpus/fuentes/`.

## Resoluciones de mantenimiento

El mapa conserva revisiones, tensiones y relaciones históricas para no borrar el rastro de la auditoría. Una revisión detectada en una fase anterior puede quedar posteriormente resuelta por lectura transversal sin que sea necesario eliminar del mapa el hallazgo que permitió detectarla.

Cuando una revisión del mapa tenga una resolución posterior, ésta se documenta fuera de las fuentes canónicas, en `documentacion/`, conservando el **ID exacto de la revisión** para que pueda recuperarse por búsqueda. Antes de tratar una revisión histórica como contradicción doctrinal vigente, debe comprobarse si existe una resolución de mantenimiento asociada a ese ID.

Una resolución de mantenimiento puede cerrar una cuestión semántica o de crosswalk sin cerrar otras revisiones matemáticas, metrológicas, empíricas, clínicas, jurídicas o técnicas relacionadas con el mismo concepto.

Ejemplo vigente: `review.axiom.alpha_forced` se conserva como hallazgo histórico y su resolución se encuentra en `documentacion/resolucion-alpha.md`.
