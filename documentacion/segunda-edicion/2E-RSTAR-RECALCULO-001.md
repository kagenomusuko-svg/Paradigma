# 2E-RSTAR-RECALCULO-001 — Inventario y recálculo de R* diferido

> **Entrada editorial derivada para segunda edición.** No modifica fuentes canónicas ni altera `RES-RSTAR-001`. Registra una decisión de secuencia de trabajo: el recálculo transversal de `R*` sigue siendo obligatorio, pero se difiere hasta terminar la auditoría de tensiones relevantes del corpus.

- **Estado:** PENDIENTE / DIFERIDO
- **Prioridad:** ALTA, NO INMEDIATA
- **Resolución de referencia:** `RES-RSTAR-001`
- **Entrada matriz:** `2E-RSTAR-001`
- **Motivo del diferimiento:** evitar rehacer ejemplos, tablas y código antes de estabilizar otras tensiones doctrinales o formales que puedan afectar la segunda edición.

## Trabajo pendiente

Antes de incorporar `2E-RSTAR-001` en segunda edición deberá levantarse un inventario completo de:

- apariciones de `R*`;
- `W R*=λR*` y `W^T R*=λR*`;
- iteración de potencia;
- Perron–Frobenius y Banach aplicados a `R*`;
- matrices estocásticas/Markov tratadas como equivalentes;
- rondas de Prometeo;
- aristas acumuladas;
- `w/Σw`;
- tablas y porcentajes `R*`;
- código y pseudocódigo;
- teoremas, corolarios y resultados aguas abajo.

Para cada ocurrencia deberá registrarse si requiere:

1. recálculo numérico;
2. reescritura conceptual;
3. corrección formal;
4. nota histórica solamente;
5. revisión de dependencias aguas abajo.

## Alcance del diferimiento

Este diferimiento **no**:

- reabre `RES-RSTAR-001`;
- vuelve provisional el operador `M_R(D)`;
- restaura `R*=eig(W)` o `R*=eig(W^T)`;
- elimina la obligación de recalcular los casos históricos incompatibles;
- modifica `corpus/fuentes/` ni el mapa histórico.

Sólo cambia el orden de ejecución editorial.

## Condición de reanudación

El inventario y recálculo se retomará cuando la auditoría de tensiones doctrinales/formales prioritarias haya quedado suficientemente estabilizada para evitar correcciones repetidas.

Hasta entonces, la continuidad MANT vuelve a la búsqueda y adjudicación de tensiones reales del corpus.
