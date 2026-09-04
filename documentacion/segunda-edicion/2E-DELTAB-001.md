# 2E-DELTAB-001 — Corrección y tipado de Δ_B

> **Entrada editorial derivada para segunda edición.** Pertenece al registro abierto en `documentacion/segunda-edicion.md` y se apoya en `documentacion/resolucion-deltab.md` (`RES-DELTAB-001`). No modifica las fuentes canónicas de primera edición.

- **Estado:** PREPARADO PARA SEGUNDA EDICIÓN
- **Prioridad:** ALTA
- **Resolución analítica de referencia:** `documentacion/resolucion-deltab.md`
- **Revisión histórica principal:** `review.calc.deltaB_type`
- **Tipo de problema:** conflicto de tipado, unidades y notación
- **Obra principal afectada:** *El cálculo de la responsabilidad*

## 1. Corrección nuclear

La segunda edición deberá distinguir expresamente:

`B_total` = beneficio total derivado del evento.

`R*_{B,i}` = participación normalizada del nodo `i` en ese beneficio.

`B_i = R*_{B,i} · B_total` = beneficio causalmente atribuible o recibido por el nodo `i`.

`β_i` = beneficio efectivamente revertido.

`Δ_{B,i}` = beneficio causalmente recibido menos beneficio revertido.

Por tanto, en escala absoluta:

`Δ_{B,i} = R*_{B,i} · B_total − β_i`.

Y en escala normalizada:

`Δ̂_{B,i} = R*_{B,i} − β_i/B_total`.

Las dos expresiones representan el mismo objeto en escalas distintas.

---

## 2. El producto y la resta no son fórmulas rivales

La segunda edición deberá explicitar que:

`R*_{B,i} · B_total`

convierte una participación normalizada en una magnitud de beneficio atribuible.

La resta:

`B_i − β_i`

mide cuánto de ese beneficio permanece después de la reversión efectiva.

El error histórico consistió en mezclar estos objetos y sus escalas como si fueran expresiones alternativas del mismo nivel formal.

---

## 3. Capítulo 1 — beneficio del daño

### Formulación histórica

El capítulo presenta:

`Δ_B = R*_B − β`,

donde `β` se describe como beneficio efectivamente revertido.

### Riesgo

Si `R*_B` es una proporción adimensional y `β` una magnitud absoluta, la resta mezcla unidades incompatibles.

### Corrección

La segunda edición deberá escoger explícitamente una de dos representaciones:

**Escala absoluta:**

`Δ_{B,i} = R*_{B,i} · B_total − β_i`.

**Escala normalizada:**

`β̂_i = β_i/B_total`

`Δ̂_{B,i} = R*_{B,i} − β̂_i`.

No debe escribirse `R*_B − β` sin declarar previamente que `β` está normalizada.

---

## 4. Apéndice E — glosario unificado

### Formulación histórica

El glosario presenta:

`Δ_B = B_total − α_B`.

### Problema

Esta formulación mezcla un total sistémico con una variable cuya función y unidad no están tipadas de manera compatible. Además elimina `R*_B`, que es precisamente el objeto que distribuye el beneficio entre nodos.

Si `B_total` es magnitud absoluta y `α_B` un coeficiente, la operación es dimensionalmente inválida:

`magnitud − coeficiente`.

### Corrección

El glosario deberá sustituir la entrada por:

`Δ_{B,i} = B_i − β_i = R*_{B,i} · B_total − β_i`.

Y, si se incluye versión normalizada:

`Δ̂_{B,i} = R*_{B,i} − β_i/B_total`.

Debe evitarse usar `α_B` como sinónimo de `β`.

---

## 5. Estatuto de α_B y β

La segunda edición deberá reservar:

- α para el sistema general de asunción;
- β para beneficio efectivamente revertido.

Si alguna sección necesita conservar una variable `α_B`, deberá definirla como objeto independiente y tiparla expresamente. No debe utilizarse como abreviatura de beneficio revertido mientras `β` cumple esa función.

---

## 6. Distinción respecto de Δ

La segunda edición debe impedir la lectura de que `Δ_B` es simplemente “la misma Δ aplicada a un resultado positivo”.

`Δ` compara:

- causalidad del daño;
- asunción efectiva.

`Δ_B` compara:

- beneficio recibido;
- beneficio revertido.

La similitud está en que ambos son operadores de brecha, no en que tengan las mismas entradas ni el mismo tipo.

---

## 7. Distinción entre G_D y G_B

Cuando el dominio lo requiera, la segunda edición deberá distinguir conceptualmente:

- `G_D`: grafo causal del daño;
- `G_B`: grafo causal del beneficio derivado del evento.

Los nodos y pesos pueden diferir.

Un nodo puede tener baja participación causal en el daño y alta participación en el beneficio recibido, o viceversa.

La segunda edición no deberá asumir que `R*` y `R*_B` son el mismo vector calculado sobre el mismo grafo sólo porque compartan estructura matemática.

---

## 8. Frontera descriptiva

La corrección debe conservar el carácter descriptivo de la metrología.

`Δ_{B,i} > 0` significa que permanece una magnitud de beneficio causalmente derivado del evento que no ha sido revertida.

No significa automáticamente:

- enriquecimiento ilícito;
- enriquecimiento injusto;
- obligación de restitución;
- confiscabilidad;
- ilegitimidad;
- responsabilidad jurídica.

Esas calificaciones pertenecen a las epístemes correspondientes.

---

## 9. Prueba obligatoria de consistencia

Toda segunda edición, hoja de cálculo o implementación de `Δ_B` deberá superar como mínimo:

`B_total = 100`

`R*_B = 0.40`

`β = 15`.

Entonces:

`B_i = 0.40 · 100 = 40`

`Δ_B = 40 − 15 = 25`.

En versión normalizada:

`β̂ = 15/100 = 0.15`

`Δ̂_B = 0.40 − 0.15 = 0.25`.

Debe verificarse:

`100 · 0.25 = 25`.

Si la implementación resta `0.40 − 15` o `100 − α_B` sin una conversión explícita y tipada, conserva el error.

---

## 10. Búsqueda transversal obligatoria antes de cerrar la segunda edición

Antes de pasar esta entrada a **INCORPORADO** deberán localizarse en todo el corpus:

- `B_total`;
- `R*_B`;
- `B_i`;
- `β`;
- `α_B`;
- `Δ_B`;
- beneficio recibido;
- beneficio revertido;
- beneficio heredado;
- enriquecimiento;
- restitución;
- recuperación;
- confiscación;
- extinción de dominio;
- cualquier conversión monetaria o temporal aplicada al beneficio.

Cada aparición deberá clasificarse por:

1. objeto;
2. unidad;
3. escala absoluta o normalizada;
4. dominio;
5. procedencia de la medición;
6. relación con `G_B` y `R*_B`.

---

## 11. Problemas que permanecen abiertos

`RES-DELTAB-001` y esta entrada no validan ni resuelven:

- la medición empírica de `B_total`;
- la construcción y validación de `G_B`;
- la estimación de `R*_B`;
- la equivalencia algorítmica entre `R*` y `R*_B`;
- beneficio directo, acumulado o de trayectoria;
- beneficio heredado;
- doble contabilización;
- beneficio no monetario;
- depreciación, rendimiento o acumulación temporal;
- rastreabilidad incompleta del beneficio.

Estas cuestiones requieren revisiones metrológicas propias.

---

## 12. Criterio de cierre editorial

`2E-DELTAB-001` podrá pasar de **PREPARADO** a **INCORPORADO** únicamente cuando:

1. todas las apariciones de `Δ_B` hayan sido localizadas;
2. toda operación declare su unidad;
3. se distinga escala absoluta de escala normalizada;
4. `B_total`, `R*_B`, `B_i`, `β` y `Δ_B` estén tipados por separado;
5. `α_B` no se use como reversión sin definición independiente;
6. las expresiones dimensionalmente inválidas hayan sido corregidas;
7. la prueba `100, 0.40, 15 → 25` sea reproducible;
8. las cuestiones metrológicas independientes permanezcan abiertas y visibles.

La segunda edición debe corregir el error sin borrar que la primera edición contenía formulaciones incompatibles.
