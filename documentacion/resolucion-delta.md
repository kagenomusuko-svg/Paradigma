# Resolución MANT — Δ, déficit de asunción e inversión causal

> **Documento analítico derivado, no fuente canónica.** Esta resolución conserva las formulaciones históricas del corpus y registra una adjudicación autoral posterior sobre cuál representa correctamente el objeto Δ. No modifica retrospectivamente las primeras ediciones ni convierte la adjudicación en validación matemática o empírica de los demás componentes del sistema.

## 1. Identificación

- **ID de resolución:** `RES-DELTA-001`
- **Concepto:** Δ / déficit de asunción / inversión causal
- **Estado:** **RESUELTA — error formal adjudicado por el autor**
- **Fórmula válida adjudicada:** `Δ = R* − α`
- **Fórmula histórica errónea para este objeto:** `Δ = R*(1 − α)`
- **Fecha de resolución:** 2026-09-04

### Revisiones históricas vinculadas

La resolución afecta directamente la discrepancia histórica conservada en:

- `review.mci.delta_crosswork`;
- `review.mci.delta_impossible_cases`;
- `review.mcii.delta_sign`;
- `review.calc.delta_history`.

También debe consultarse al trabajar con:

- `review.mcii.delta_magnitude`;
- `review.mcii.delta_appendix`;
- `review.calc.deltaB_type`;
- `review.prometeo.delta_comparability`.

Estas últimas **no quedan cerradas automáticamente**: pueden contener problemas de conmensurabilidad, conversión, tipado o calibración distintos de la fórmula y del signo de Δ.

Relaciones históricas relevantes:

- `rel.mci.delta.differs_axiom`;
- `rel.mci.delta.reuses_tf`.

### Regla de recuperación

Si una consulta sobre Δ recupera la variante `R*(1−α)`, una revisión de signo o la incompatibilidad entre Metrología Causal y la versión sustractiva, debe leerse este documento antes de presentar ambas expresiones como alternativas doctrinales vigentes.

El hecho histórico permanece: las fuentes publicadas contienen ambas formulaciones. La adjudicación actual establece cuál representa el objeto que el autor pretendía medir.

---

## 2. Las dos expresiones conservadas por el corpus

El corpus contiene:

`Δ = R* − α`

y también:

`Δ = R*(1 − α)`.

No son algebraicamente equivalentes:

`R*(1 − α) = R* − R*α`,

mientras la versión sustractiva compara directamente:

`R* − α`.

La diferencia no es notacional. Cada expresión presupone un tipo distinto para α y produce propiedades distintas para Δ.

---

## 3. El objeto que Δ debe medir

Tras la revisión de α, la arquitectura consolidada distingue:

- `R*_i`: magnitud de la posición o participación causal del nodo `i`;
- `α_i`: magnitud de asunción efectiva del nodo `i`.

Δ tiene por objeto medir la brecha entre esas dos magnitudes:

`Δ_i = R*_i − α_i`.

Su lectura descriptiva es:

- `Δ > 0`: el nodo causó más de lo que asumió;
- `Δ = 0`: la magnitud causada y la magnitud asumida coinciden;
- `Δ < 0`: el nodo asumió más de lo que causó.

El tercer caso es indispensable para representar **sobreimputación, chivo expiatorio e inversión causal**.

La medición no prescribe qué debería suceder. Legalidad, legitimidad, justicia, proporcionalidad o merecimiento son predicados posteriores de otras epístemes.

---

## 4. Por qué `R*(1−α)` representa otro objeto

La expresión:

`R*(1 − α)`

sería coherente si α significara:

> fracción de la propia `R*` del nodo que ya fue asumida.

Bajo ese tipado, si:

`R* = 0.20`

y
`α = 0.70`,

entonces:

`R*(1−α) = 0.20 × 0.30 = 0.06`

significaría que queda sin cubrir el 30% de la cuota causal de 0.20.

Ese cálculo es matemáticamente inteligible, pero **no corresponde al α consolidado del Paradigma**. α no es una tasa relativa interna a la propia `R*`; registra una magnitud de asunción efectiva que puede ser comparada directamente con `R*` y, en casos de sobreimputación, puede satisfacer:

`α > R*`.

Por ello la multiplicación introduce implícitamente un tipado de α que no corresponde al objeto utilizado por la arquitectura aplicada.

---

## 5. El problema del signo

Si:

`R* ∈ [0,1]`

y
`α ∈ [0,1]`,

entonces:

`R*(1−α) ≥ 0`.

Por construcción, esa expresión nunca puede producir un Δ negativo.

Metrología Causal I, capítulo II·14, hace explícita esa propiedad al derivar la fórmula multiplicativa y afirmar que `Δ_i ≥ 0 siempre`.

Ésa es precisamente la propiedad que vuelve la fórmula incompatible con el objeto de inversión causal: un sistema que sólo permite `Δ ≥ 0` no puede distinguir matemáticamente entre déficit de asunción y sobreasunción.

La fórmula sustractiva, en cambio, permite:

`Δ ∈ [-1,1]`

cuando `R*, α ∈ [0,1]`, y conserva los tres estados descriptivos necesarios.

---

## 6. Caso de prueba: chivo expiatorio

Considérese el caso aplicado que después utiliza Método Prometeo:

`R* = 0.191`

`α = 0.60`.

Con la fórmula válida:

`Δ = 0.191 − 0.60 = −0.409`.

El resultado expresa que el nodo asumió 40.9 puntos porcentuales más de lo que causó.

Con la fórmula multiplicativa:

`Δ = 0.191(1−0.60) = 0.0764`.

El resultado no sólo tiene otra magnitud: cambia de signo y transforma un caso de sobreimputación en un supuesto déficit positivo.

Por ello, para el objeto `déficit de asunción / inversión causal`, la fórmula multiplicativa no es una variante equivalente: representa incorrectamente el fenómeno que Δ pretende medir.

---

## 7. Cronología y adjudicación autoral

La cronología debe preservarse correctamente.

La formulación sustractiva:

`Δ = R* − α`

ya aparece en *El cálculo de la responsabilidad* y es la que permite medir inversión causal.

Posteriormente, durante la matematización desarrollada en *Metrología Causal*, se introdujo la formulación:

`Δ = R*(1−α)`.

Metrología Causal I la deriva expresamente en II·14 y Metrología Causal II la conserva en su lenguaje operativo.

El autor adjudica ahora que esa sustitución **no fue una evolución doctrinal deliberada**, sino un error de formalización producido durante el esfuerzo de matematización del sistema.

La secuencia histórica correcta es, por tanto:

`formulación sustractiva correcta → error formal posterior en Metrología Causal → adjudicación autoral → corrección pendiente de segunda edición`.

No debe describirse como una fórmula temprana corregida por una fórmula posterior.

---

## 8. Qué se conserva de la intuición metrológica

El error afecta la formalización matemática, no el objeto que la arquitectura pretendía representar.

La intuición metrológica permanece:

`Δ = causado − asumido`.

En ese sentido, el problema puede describirse con precisión como **un error de tipado/formalización de α dentro de la fórmula de Δ**: la versión multiplicativa trató α implícitamente como proporción de `R*`, cuando el sistema aplicado la usa como magnitud de asunción comparable directamente con `R*`.

Esto no convierte automáticamente en correctas todas las escalas, calibraciones o procedimientos con los que se estiman `R*` y α. La resolución fija el objeto y la operación algebraica que lo relaciona.

---

## 9. Consecuencia para la lectura del corpus vigente

Hasta que existan segundas ediciones, las fuentes canónicas deben conservar las dos formulaciones porque documentan las ediciones históricas.

Para consultas doctrinales, editoriales o nuevas implementaciones del déficit de asunción y la inversión causal:

`Δ = R* − α`

debe tratarse como la fórmula autoral adjudicada.

`Δ = R*(1−α)`

debe tratarse como un error formal histórico cuando pretende nombrar el mismo Δ.

No debe armonizarse silenciosamente la fuente histórica. Debe indicarse la existencia del error y la resolución posterior.

---

## 10. Qué queda resuelto

`RES-DELTA-001` resuelve:

1. cuál de las dos fórmulas representa el Δ del Paradigma;
2. el signo permitido de Δ;
3. la necesidad formal de `Δ < 0` para inversión causal;
4. el estatus de `R*(1−α)` como error formal cuando se usa para ese objeto;
5. la cronología de la discrepancia.

---

## 11. Qué NO queda resuelto

Esta adjudicación no resuelve automáticamente:

- calibración de `R*`;
- calibración de α;
- conmensurabilidad empírica entre `R*` y α;
- comparabilidad entre dominios;
- escalas observacionales de Δ;
- `Δ_B` y su conflicto de tipado;
- conversiones o tablas de Metrología Causal II;
- `Δ_sesión` u otras variables que puedan representar objetos diferentes;
- validez empírica o matemática de otros teoremas del corpus.

Si alguna aparición de `R*(1−α)` resulta estar calculando legítimamente un objeto diferente —por ejemplo, «fracción de la propia `R*` aún no cubierta»— podrá conservarse sólo como objeto distinto, con nombre, símbolo y tipo propios. No debe seguir llamándose Δ si se pretende preservar la definición sustractiva.

---

## 12. Regla para segunda edición

La corrección de segunda edición no puede consistir únicamente en buscar y reemplazar una fórmula.

Debe localizarse toda definición, teorema, corolario, tabla, rango, demostración, ejemplo, pseudocódigo, cálculo y conclusión que dependa de:

`Δ = R*(1−α)`.

Cada dependencia debe recalcularse o reformularse con:

`Δ = R* − α`.

Como prueba mínima, cualquier formalización corregida debe poder representar el caso:

`R* = 0.191`, `α = 0.60`, `Δ = −0.409`.

Si no puede producir un valor negativo en ese caso, todavía conserva implícitamente el tipado erróneo.