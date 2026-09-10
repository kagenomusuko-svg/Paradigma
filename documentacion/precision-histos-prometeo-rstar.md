# RES-HISTOS-PROM-001-P1 — Precisión de capas: qué aporta HISTOS y qué necesita Prometeo

> **Precisión vinculada a `RES-HISTOS-PROM-001`; no constituye una nueva tensión ni modifica fuentes canónicas.** Este documento fija una consecuencia arquitectónica que quedó implícita en la resolución general: HISTOS no alimenta la construcción de `R*`; sus aportes se ubican, con estatus secundario, en capas posteriores o auxiliares de `S` y `α`.

- **ID:** `RES-HISTOS-PROM-001-P1`
- **Resolución rectora:** `RES-HISTOS-PROM-001`
- **Estado:** **PRECISIÓN RESUELTA — separación entre motor causal R* y capas S/α/Δ**
- **Fecha:** 2026-09-10
- **Resoluciones relacionadas:** `RES-RSTAR-001`, `RES-ALPHA-001`, `RES-DELTA-001`, `AUD-S-001` / `2E-S-001`, `RES-SDO-PROM-001`

---

## 1. Pregunta precisa

Si HISTOS afirma que su expediente «alimenta» a Prometeo, debe distinguirse qué parte de Prometeo recibe realmente ese aporte.

La pregunta correcta es:

> ¿El expediente HISTOS aporta entradas al motor causal que produce `R*(D)`, o sólo puede informar de manera secundaria capas posteriores o auxiliares de `S_P`, `α_P` y la interpretación de `Δ_P`?

La resolución es inequívoca:

> **HISTOS no alimenta la construcción de `R*`.**

---

## 2. Qué necesita Prometeo para producir R*

Bajo `RES-RSTAR-001`, el cálculo de responsabilidad causal requiere un resultado explícito `D` y una reconstrucción causal independiente del caso.

La secuencia mínima es:

`resultado D`

`→ actores/factores causalmente pertinentes`

`→ aristas primitivas documentadas`

`→ pesos locales w por arista`

`→ Q_D, b_D`

`→ condición ρ(Q_D) < 1`

`→ r_D = (I − Q_D)^−1 b_D`

`→ R*(D) = r_D / (1^T r_D)`.

Por tanto, para el motor causal son constitutivos:

1. un resultado `D` explícito;
2. un grafo causal `G_D` reconstruido respecto de ese resultado;
3. aristas primitivas sustentadas por evidencia;
4. pesos `w` por arista;
5. la construcción de `Q_D` y `b_D`;
6. la condición de convergencia `ρ(Q_D) < 1`.

Ninguno de esos objetos es producido por el expediente longitudinal de HISTOS.

---

## 3. Qué HISTOS no puede aportar al motor R*

El expediente HISTOS no puede, por sí solo:

- definir el resultado `D` de Prometeo;
- validar una arista causal;
- producir el peso `w_ij` de una arista;
- construir `Q_D`;
- construir `b_D`;
- demostrar `ρ(Q_D) < 1`;
- producir `R*(D)`;
- convertir una observación longitudinal del sujeto en evidencia causal contemporánea del hecho analizado.

Una salida de HISTOS puede sugerir qué investigar, qué contraste formular o qué evidencia buscar. Esa función es **heurística/contextual**, no constitutiva del operador causal.

La cadena prohibida es:

`HISTOS → dato del expediente → w/Q_D/b_D → R*`

sin reconstrucción causal independiente.

---

## 4. Capas de Prometeo y ubicación correcta del aporte HISTOS

La interfaz debe separarse por capas.

### Capa A — reconstrucción causal y R*

Entrada:

- `D`;
- evidencia contemporánea y documental pertinente;
- aristas causales;
- `w`;
- `Q_D`, `b_D`.

Salida:

- `R*(D)`.

**Aporte HISTOS:** no constitutivo. Puede generar preguntas o hipótesis, pero no sustituye ninguna entrada del cálculo.

### Capa B — sustituibilidad `S_P`

Prometeo estima la sustituibilidad estructural del actor mediante criterios propios del rol y del sistema: formalización, costo de desobediencia, evidencia de desobediencias, fungibilidad, incentivos, restricciones y demás evidencia pertinente.

**Aporte HISTOS:** `P(Hijos)` y `S_H` pueden orientar hipótesis sobre patrones de actuación o dependencia del campo. No determinan `S_P`.

### Capa C — asunción aplicada `α_P`

Prometeo construye `α_P` desde acciones o consecuencias concretas y verificables posteriores al evento: reparación, pagos, modificaciones del sistema, sanciones u otras formas de asunción efectiva según el dominio.

**Aporte HISTOS:** `α_H` por período y dominio puede aportar contexto de segundo nivel acerca del proceso interno de integración/asunción. No se transfiere numéricamente a `α_P` sin un crosswalk explícito y validado.

### Capa D — brecha `Δ_P`

Prometeo calcula:

`Δ_P = R* − α_P`.

**Aporte HISTOS:** el momento del arco, `Δ_H` y la historia de bloqueos pueden contextualizar la lectura del proceso, pero no entran en la resta formal ni sustituyen `R*` o `α_P`.

---

## 5. Tabla de interfaz consolidada

| Elemento del expediente HISTOS | Capa de Prometeo relacionada | Estatus permitido del aporte |
| --- | --- | --- |
| `P(Hijos)` + `S_H` cualitativa | investigación de `S_P` | Hipótesis de trabajo/contexto; no sustituye criterios estructurales ni documentales de `S_P` |
| `α_H` por período y dominio | investigación de `α_P` | Información secundaria sobre integración interna; no es `α_P` aplicado ni se transfiere numéricamente sin crosswalk validado |
| Momento del arco | contexto de `α_P` / `Δ_P` | Contexto interpretativo; no entra al cálculo |
| `Δ_H` cualitativo | contexto de la brecha de asunción | Genealogía conceptual análoga; no es `Δ_P = R* − α_P` |
| Historia de bloqueos | contexto del actor/proceso | Evidencia secundaria contextual; cualquier efecto causal, jurídico o mitigante exige una regla independiente |
| Observaciones longitudinales | generación de hipótesis | Pueden orientar búsqueda de evidencia; no producen `w`, `Q_D`, `b_D` ni `R*` |

La última precisión evita convertir una observación de acompañamiento en «circunstancia mitigante» por mera inferencia. Cualquier consecuencia normativa requiere fundamento propio del dominio correspondiente.

---

## 6. Sentido correcto de «HISTOS alimenta a Prometeo»

La formulación general debe restringirse.

No debe entenderse:

> «HISTOS aporta los datos con los que Prometeo construye su grafo causal y calcula R*.»

La formulación consolidada es:

> **HISTOS puede informar capas posteriores o auxiliares del análisis Prometeo —especialmente la investigación de `S_P` y `α_P`— mediante información contextual de segundo nivel. No alimenta la reconstrucción causal que produce `R*`, y sus salidas no sustituyen los criterios evidenciales propios de `S_P` ni `α_P`.**

Esto preserva la utilidad de la interfaz sin confundir capas.

---

## 7. Consecuencia para S

La precisión refuerza `RES-HISTOS-PROM-001`:

`P(Hijos) → hipótesis sobre patrón de actuación`

no equivale a:

`P(Hijos) → S_P`.

`S_P` pertenece a la estructura contrafáctica del rol/sistema. Dos actores con el mismo Hijo dominante pueden tener sustituibilidad distinta si las condiciones estructurales difieren.

La información HISTOS puede reducir el espacio de preguntas, nunca sustituir la investigación estructural.

---

## 8. Consecuencia para α

`α_H` y `α_P` pertenecen a la misma familia conceptual de asunción, pero no al mismo estimando ni a la misma evidencia.

Por tanto:

`α_H alto` puede coexistir con `α_P bajo`;

`α_P alto` puede coexistir con `α_H bajo`.

HISTOS puede aportar contexto para investigar `α_P`, pero Prometeo debe construir `α_P` desde sus propios observables aplicados.

---

## 9. Consecuencia para Δ

Como:

`Δ_P = R* − α_P`,

ningún dato HISTOS puede producir `Δ_P` sin que Prometeo haya construido previamente `R*` y `α_P`.

`Δ_H` sólo puede conservarse como lectura cualitativa interna de brecha de asunción.

La frase «HISTOS permite estimar Δ de Prometeo» debe entenderse, como máximo, en sentido de **orientar una investigación** o proporcionar contexto; no como producir el valor formal.

---

## 10. Contaminación temporal

La separación de capas no elimina la asimetría temporal.

Si:

`t0 = hecho que Prometeo reconstruye`

`t1…tn = acompañamiento HISTOS`,

entonces un dato recogido en `tn` después de intervención es un dato post-intervención.

Puede describir el estado en `tn`, cambio longitudinal o una hipótesis retrospectiva. No puede operar como evidencia contemporánea de `t0` sin inferencia explícita y evidencia independiente.

La contaminación temporal es distinta de la contaminación cruzada entre analista y mediador y ambas deben conservarse como controles separados.

---

## 11. Ejecución, transferencia y retroalimentación

La precisión mantiene tres operaciones distintas.

### Ejecución de Prometeo

El análisis documental y el cálculo de `R*` pueden ejecutarse independientemente del momento del arco de HISTOS, siempre que Prometeo disponga de sus propias entradas válidas.

### Transferencia HISTOS → Prometeo

Sólo aporta información contextual de segundo nivel a capas permitidas y debe conservar consentimiento, procedencia, dominio, período, certeza y condición pre/post intervención.

### Retroalimentación Prometeo → HISTOS / sujeto

Puede modificar el proceso interno. Por ello `M·3+` se mantiene como umbral para introducir resultados al acompañamiento en el dominio pertinente, junto con las demás condiciones del protocolo.

La sola presencia del sujeto en `M·1/M·2` no invalida la ejecución externa de Prometeo; limita la retroalimentación susceptible de forzar el proceso.

---

## 12. Firewall informacional

La operación concurrente debe preservar la separación funcional ya fijada en `RES-HISTOS-PROM-001`.

El firewall debe impedir, en particular, que:

- el analista use información post-intervención como si fuera evidencia causal de `t0`;
- el mediador oriente HISTOS hacia los actos que Prometeo intenta atribuir;
- los resultados de Prometeo ingresen prematuramente al acompañamiento;
- un dato generado por HISTOS se convierta en entrada causal y luego la salida de Prometeo se presente como confirmación independiente del mismo dato.

---

## 13. Efecto sobre las revisiones abiertas

Esta precisión **no reabre** la tensión HISTOS→Prometeo.

Queda definitivamente fijado que:

- `review.histos.prometeo_independence` no implica que HISTOS deba ser excluido, sino que su aporte está tipado como secundario y fuera del motor `R*`;
- `review.histos.s_qualitative` conserva abierta la validez/calibración de `S_H`, pero no la inferencia directa a `S_P`;
- `review.histos.alpha_scale` conserva abierta la calibración de `α_H`, pero no la equivalencia numérica con `α_P`;
- `review.histos.delta_semantics` permanece resuelta por separación `Δ_H/Δ_P`;
- `review.histos.change_attribution` continúa abierta y es independiente de esta interfaz.

---

## 14. Obligación editorial derivada

La segunda edición debe decir explícitamente, en VI·2 y en toda referencia equivalente, que:

> **el expediente HISTOS no alimenta `G_D`, `w`, `Q_D`, `b_D` ni `R*`; puede informar, como contexto de segundo nivel, la investigación de `S_P` y `α_P`, y contextualizar `Δ_P`, sin sustituir los procedimientos propios de Prometeo.**

La reparación editorial concreta se registra en `2E-HISTOS-PROM-001-P1`.

---

## 15. Fórmula de cierre

La arquitectura consolidada es:

`D + evidencia causal independiente`

`→ G_D → w → Q_D,b_D → [ρ(Q_D)<1] → R*`

seguida, en capas distintas, por:

`evidencia estructural → S_P`

`evidencia de asunción efectiva → α_P`

`R* + α_P → Δ_P`.

HISTOS puede situarse alrededor de las capas `S_P` y `α_P` como fuente contextual de segundo nivel y alrededor de `Δ_P` como contexto interpretativo; **no como fuente constitutiva de `R*`**.

Esta precisión forma parte de la resolución vigente de HISTOS→Prometeo y no modifica la doctrina canónica de primera edición.