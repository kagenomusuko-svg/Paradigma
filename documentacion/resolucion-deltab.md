# Resolución MANT — Δ_B, beneficio derivado del daño y reversión

> **Documento analítico derivado, no fuente canónica.** Esta resolución conserva las formulaciones históricas del corpus y registra una adjudicación autoral sobre el objeto que `Δ_B` pretende medir. No modifica retrospectivamente las primeras ediciones ni convierte la adjudicación en validación matemática o empírica de los componentes todavía abiertos.

## 1. Identificación

- **ID de resolución:** `RES-DELTAB-001`
- **Concepto:** `Δ_B` / beneficio derivado del daño / beneficio no revertido
- **Estado:** **RESUELTA — conflicto de tipado y fórmula adjudicado**
- **Revisión histórica principal:** `review.calc.deltaB_type`
- **Naturaleza del problema:** mezcla entre proporciones normalizadas, magnitudes absolutas y coeficientes de asunción
- **Objeto doctrinal adjudicado:** diferencia entre el beneficio causalmente recibido por un nodo y el beneficio efectivamente revertido por ese nodo.
- **Fecha de resolución:** 2026-09-04

### Regla de recuperación

Si una consulta sobre `Δ_B` recupera las variantes `R*_B − β`, `B_total − α_B` o cualquier otra mezcla entre beneficio total, participación causal y reversión, debe leerse este documento antes de presentar esas expresiones como alternativas formales vigentes.

El hecho histórico permanece: *El cálculo de la responsabilidad* contiene formulaciones no equivalentes. La adjudicación actual establece qué objeto debe representar `Δ_B` y cómo tiparlo.

---

## 2. Δ_B no es una variante de Δ

Debe distinguirse:

`Δ_i = R*_i − α_i`

frente a:

`Δ_{B,i}`.

`Δ` compara:

- posición causal en el daño;
- asunción efectiva.

`Δ_B` compara:

- beneficio recibido como consecuencia del evento dañino;
- beneficio efectivamente revertido.

Por tanto:

`Δ_B ≠ Δ`

y:

`β ≠ α`.

La coincidencia de la letra delta expresa que ambos objetos son brechas, no que tengan el mismo tipo ni las mismas variables de entrada.

---

## 3. Daño y beneficio son distribuciones causales distintas

Un mismo evento puede producir simultáneamente:

`D_total`

y:

`B_total`.

El daño y el beneficio no tienen por qué recaer sobre los mismos nodos ni en las mismas proporciones.

Por ello deben distinguirse conceptualmente:

- `G_D`: grafo de producción causal del daño;
- `G_B`: grafo de producción, transmisión o recepción causal del beneficio derivado de ese daño.

Del primero se obtiene `R*`.

Del segundo se obtiene `R*_B`.

Así:

`R*_i` = participación causal del nodo `i` en la producción del daño.

`R*_{B,i}` = participación normalizada del nodo `i` en el beneficio causalmente derivado del evento.

Un nodo puede presentar `R*_i ≈ 0` y, sin embargo, `R*_{B,i} > 0`: puede no haber producido causalmente el daño y aun así haber recibido beneficio derivado de él.

---

## 4. Beneficio total

Defínase:

`B_total` = beneficio total efectivamente producido como consecuencia causal del evento analizado.

El tipo y la unidad de `B_total` dependen del dominio. Puede expresarse, cuando el objeto lo permita, en:

- moneda;
- patrimonio;
- recursos;
- tiempo;
- unidades físicas;
- otra magnitud explícitamente definida.

La metrología debe conservar la unidad del objeto y no introducir predicados jurídicos o morales dentro de la medición.

---

## 5. Beneficio correspondiente a cada nodo

Si `R*_{B,i} ∈ [0,1]` representa la participación normalizada del nodo `i` en el beneficio total, entonces:

`B_i = R*_{B,i} · B_total`.

Donde:

`B_i` = beneficio causalmente atribuible o causalmente recibido por el nodo `i` dentro del evento analizado.

Ejemplo:

`B_total = 100 000 000`

`R*_{B,i} = 0.40`

entonces:

`B_i = 40 000 000`.

El producto no compite con la resta de `Δ_B`: cumple una operación distinta. Convierte una participación normalizada en una magnitud de beneficio atribuible.

---

## 6. Beneficio revertido

Defínase:

`β_i` = magnitud de beneficio efectivamente revertida por el nodo `i`.

La reversión puede adoptar, según el dominio, formas como:

- restitución;
- devolución;
- recuperación;
- confiscación ejecutada;
- transferencia efectiva;
- reversión patrimonial;
- otra operación material verificable.

`β_i` mide un hecho. No presupone:

- consentimiento;
- arrepentimiento;
- reconocimiento moral;
- legalidad;
- justicia;
- legitimidad.

Una reversión impuesta sigue siendo una reversión efectivamente producida.

---

## 7. Fórmula absoluta de Δ_B

Si `B_i` y `β_i` están expresados en la misma unidad:

`Δ_{B,i} = B_i − β_i`.

Sustituyendo la definición de `B_i`:

`Δ_{B,i} = R*_{B,i} · B_total − β_i`.

Ésta es la formulación absoluta adjudicada.

Si `B_total` está expresado en moneda, `B_i`, `β_i` y `Δ_{B,i}` deben estar expresados en esa misma moneda.

---

## 8. Fórmula normalizada

También puede utilizarse una versión normalizada.

Defínase:

`β̂_i = β_i / B_total`.

Entonces:

`Δ̂_{B,i} = R*_{B,i} − β̂_i`.

Todos los términos son ahora adimensionales.

Las dos formulaciones son equivalentes por escala:

`Δ_{B,i} = B_total · Δ̂_{B,i}`.

Por tanto, el corpus puede trabajar tanto con magnitudes absolutas como normalizadas, siempre que no las mezcle dentro de una misma operación.

---

## 9. Interpretación del signo

`Δ_{B,i} > 0` significa que el nodo conserva una magnitud de beneficio causalmente derivado del evento superior a la que ha sido revertida.

`Δ_{B,i} = 0` significa que la magnitud del beneficio recibido y la magnitud revertida coinciden.

`Δ_{B,i} < 0` significa que el nodo revirtió una magnitud superior al beneficio que le fue causalmente atribuido en ese análisis.

Ninguno de estos resultados implica automáticamente un juicio jurídico o moral.

---

## 10. Frontera descriptiva

La metrología puede afirmar:

- el evento produjo `B_total`;
- el nodo `i` recibió `B_i`;
- el nodo revirtió `β_i`;
- permanece `Δ_{B,i}`.

No sigue de ello automáticamente que el beneficio sea:

- ilícito;
- ilegítimo;
- injusto;
- indebido;
- confiscable;
- reclamable;
- sujeto a restitución.

Esas predicaciones pertenecen a las epístemes correspondientes.

---

## 11. Resolución del conflicto histórico

*El cálculo de la responsabilidad* conserva al menos estas formulaciones:

`Δ_B = R*_B − β`

y:

`Δ_B = B_total − α_B`.

### 11.1 La resta `R*_B − β`

Puede ser formalmente válida únicamente si `β` está expresada en la misma escala normalizada que `R*_B`.

Su forma explícita y tipada debe ser:

`Δ̂_{B,i} = R*_{B,i} − β̂_i`.

Si `β_i` es una magnitud absoluta, la expresión correcta es:

`Δ_{B,i} = R*_{B,i} · B_total − β_i`.

### 11.2 La expresión `B_total − α_B`

No representa correctamente el objeto cuando `B_total` es una magnitud absoluta y `α_B` un coeficiente adimensional.

En ese caso existe un conflicto dimensional:

`magnitud − coeficiente`.

Además, la expresión pierde la distribución entre beneficiarios representada por `R*_B` y compara un total sistémico contra una variable de nodo o coeficiente.

Esta formulación queda adjudicada como error de tipado para el objeto `Δ_B`.

---

## 12. Estatuto de α_B

`α_B` no debe introducirse como sinónimo de `β`.

Si alguna sección futura necesita conservar una variable `α_B`, deberá definirla como objeto independiente y tiparla expresamente.

No debe utilizarse para representar beneficio revertido mientras `β` cumple ya esa función.

α conserva su función general como coeficiente de asunción; β representa la reversión efectiva del beneficio.

---

## 13. Polisemia posible de R*_B

El corpus utiliza `R*_B` también para contribución causal a resultados positivos, por ejemplo en dominios deportivos.

En `Δ_B`, el objeto relevante es específicamente la distribución causal del beneficio derivado de un evento entre sus beneficiarios.

Si ambos usos pueden representarse mediante el mismo operador matemático, pueden conservar el símbolo común con semánticas de dominio explícitas.

Si no son el mismo objeto formal, deberán recibir símbolos distintos.

La coincidencia de notación no establece por sí sola identidad formal.

---

## 14. Ejemplo de consistencia

Supóngase:

`B_total = 100 000 000`

`R*_{B,A} = 0.40`

Entonces:

`B_A = 40 000 000`.

Si:

`β_A = 15 000 000`,

entonces:

`Δ_{B,A} = 40 000 000 − 15 000 000 = 25 000 000`.

Normalizando:

`β̂_A = 15 000 000 / 100 000 000 = 0.15`.

Por tanto:

`Δ̂_{B,A} = 0.40 − 0.15 = 0.25`.

Y:

`100 000 000 · 0.25 = 25 000 000`.

Las representaciones absoluta y normalizada son consistentes.

---

## 15. Qué queda resuelto

`RES-DELTAB-001` resuelve:

- qué pretende medir `Δ_B`;
- la diferencia entre `B_total`, `R*_B`, `B_i`, `β_i` y `Δ_B`;
- la diferencia entre fórmula absoluta y normalizada;
- el conflicto resta/producto cuando se trataban como fórmulas rivales;
- la incompatibilidad dimensional de `B_total − α_B` cuando `α_B` es un coeficiente;
- la separación de `Δ_B` respecto de `Δ` y α;
- `review.calc.deltaB_type` en cuanto a la adjudicación del objeto, tipo y fórmula.

---

## 16. Qué NO queda resuelto

Permanecen como problemas metrológicos independientes:

- cómo determinar empíricamente `B_total`;
- cómo construir y validar `G_B`;
- cómo estimar `R*_B`;
- cómo separar beneficio directo, acumulado y derivado;
- cómo evitar doble contabilización;
- cómo valorar beneficio no monetario;
- cómo modelar beneficio heredado;
- cómo modelar depreciación, rendimiento o acumulación temporal;
- cómo tratar beneficio no rastreable;
- cómo distribuir residuos no atribuidos;
- si el operador utilizado para `R*_B` es formalmente idéntico al utilizado para `R*`.

Ninguno de estos problemas queda validado por la adjudicación autoral del tipo de `Δ_B`.

---

## 17. Regla de lectura futura

Cuando el corpus presente `Δ_B`, debe preguntarse primero:

**¿la operación está expresada en escala absoluta o normalizada?**

En escala absoluta:

`Δ_{B,i} = R*_{B,i} · B_total − β_i`.

En escala normalizada:

`Δ̂_{B,i} = R*_{B,i} − β_i/B_total`.

No deben mezclarse ambas escalas dentro de una misma resta.
