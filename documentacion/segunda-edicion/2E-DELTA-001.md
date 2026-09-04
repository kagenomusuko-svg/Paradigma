# 2E-DELTA-001 — Corrección formal de Δ

> **Entrada editorial derivada para segunda edición.** Pertenece al registro abierto en `documentacion/segunda-edicion.md` y se apoya en `documentacion/resolucion-delta.md`. No modifica las fuentes canónicas de primera edición.

- **Estado:** PREPARADO PARA SEGUNDA EDICIÓN
- **Prioridad:** ALTA
- **Resolución analítica de referencia:** `documentacion/resolucion-delta.md` (`RES-DELTA-001`)
- **Tipo de problema:** error formal, no evolución doctrinal
- **Obras principalmente afectadas:** *Metrología Causal* I y II
- **Fórmula válida:** `Δ = R* − α`
- **Fórmula a corregir cuando representa el mismo objeto:** `Δ = R*(1 − α)`

## 1. Diagnóstico editorial

El corpus conserva dos fórmulas distintas para Δ. La adjudicación autoral determina que el objeto `déficit de asunción / inversión causal` debe calcularse mediante:

`Δ = R* − α`.

La expresión:

`Δ = R*(1−α)`

aparece posteriormente en *Metrología Causal* y trata implícitamente α como una tasa relativa de la propia `R*` del nodo. Ese tipado no corresponde al α consolidado del sistema y elimina por construcción la posibilidad de `Δ < 0`.

La corrección de segunda edición es necesaria porque un lector puede implementar correctamente la fórmula publicada y obtener un resultado que contradice el fenómeno que Δ fue diseñado para representar.

---

## 2. Qué debe quedar inequívoco

La segunda edición debe expresar sin ambigüedad:

- `R*` = magnitud de la posición causal;
- α = magnitud de asunción efectiva;
- `Δ = R* − α` = diferencia entre lo causado y lo asumido.

Interpretación:

- `Δ > 0`: causó más de lo que asumió;
- `Δ = 0`: causalidad y asunción coinciden en magnitud;
- `Δ < 0`: asumió más de lo que causó; sobreimputación / inversión causal.

Estas descripciones son metrológicas. No implican por sí mismas que la distribución sea justa, injusta, legal, ilegal, legítima o ilegítima.

---

## 3. Metrología Causal I — capítulo II·14

### Problema

El capítulo deriva expresamente:

`Δ_i = R*_i − α_iR*_i = R*_i(1−α_i)`

y de ella concluye:

`Δ_i ≥ 0 siempre`.

También construye `Δ_total` como suma de esos déficits no negativos.

Ese desarrollo impide representar un nodo que asumió más de lo que causó.

### Corrección necesaria

Cuando el capítulo quiera medir déficit de asunción e inversión causal, sustituir la definición por:

`Δ_i = R*_i − α_i`.

Si `R*, α ∈ [0,1]`, explicitar:

`Δ_i ∈ [-1,1]`.

Revisar todas las propiedades derivadas. En particular, dejar de sostener como propiedad general del objeto que:

`Δ_i ≥ 0 siempre`.

La segunda edición deberá construir por separado cualquier agregado sistémico `Δ_total`, porque la simple suma de valores con signo tiene una interpretación distinta de la suma de déficits sólo positivos.

### No hacer

No sustituir mecánicamente la fórmula y conservar intactas demostraciones que dependían de no negatividad. Toda consecuencia algebraica debe revisarse.

---

## 4. Metrología Causal II

### Problema

Vol. II arrastra la versión multiplicativa dentro de su glosario y formalizaciones operativas:

`Δ_i = R*(i)(1−α_i)`.

Por ello, la segunda edición debe considerarse afectada aunque parte del desarrollo remita a Vol. I.

### Corrección necesaria

Toda aparición donde Δ signifique la brecha entre causalidad y asunción debe utilizar:

`Δ_i = R*_i − α_i`.

Revisar especialmente:

- glosario operativo;
- tablas de equivalencia por dominio;
- corolarios que dependan del signo;
- rangos declarados;
- formularios del Apéndice A;
- tabla de conversión;
- ejemplos y productos de salida.

`review.mcii.delta_magnitude` y `review.mcii.delta_appendix` no quedan resueltas sólo por sustituir la fórmula: sus problemas de magnitud, conversión o conmensurabilidad deben auditarse por separado.

---

## 5. El cálculo de la responsabilidad

### Estado

La formulación que debe preservarse es:

`Δ_i = R*_i − α_i`.

El libro ya permite la interpretación:

- `Δ > 0`: causó más de lo asumido;
- `Δ < 0`: cargó más de lo causado.

### Mejora propuesta

En segunda edición, usar esta formulación como ancla transversal para corregir Metrología Causal.

Añadir, si procede editorialmente, una nota que explicite que α no es «porcentaje interno de R* ya cubierto», sino magnitud de asunción comparable con `R*`.

### No cambiar

No sustituir la resta por la fórmula multiplicativa.

---

## 6. Método Prometeo

### Estado

El caso del asesor sobreimputado funciona como prueba aplicada del signo negativo:

`R* = 0.191`

`α ≈ 0.60`

`Δ = −0.409`.

### Mejora propuesta

Conservar el caso como prueba pedagógica y de implementación.

Añadir una nota de referencia a la definición formal corregida de segunda edición de Metrología Causal, de modo que el lector no encuentre dos mecanismos incompatibles para el mismo Δ.

### No cambiar

No perder la posibilidad de `Δ < 0`, porque es la que hace visible la inversión causal.

---

## 7. Prueba obligatoria de validación editorial y de software

Toda segunda edición, hoja de cálculo, implementación o motor que use Δ deberá superar como mínimo:

`R* = 0.191`

`α = 0.60`

Resultado esperado:

`Δ = −0.409`.

Si devuelve un resultado no negativo, sigue utilizando directa o implícitamente la fórmula o el tipado erróneos.

Debe incluirse además un caso por cada régimen:

1. `R* > α` → `Δ > 0`;
2. `R* = α` → `Δ = 0`;
3. `R* < α` → `Δ < 0`.

---

## 8. Búsqueda sistemática obligatoria antes de cerrar la segunda edición

Antes de marcar esta entrada como INCORPORADA deben localizarse en todo el corpus:

- `Δ`;
- `R*(1−α)` y variantes tipográficas;
- `R*−α` y variantes tipográficas;
- `Δ_total`;
- rangos del tipo `[0,1]` atribuidos a Δ;
- afirmaciones de no negatividad;
- tablas o escalas derivadas del signo;
- ejemplos numéricos;
- pseudocódigo y plantillas;
- `Δ_B`;
- `Δ_sesión` u otras variables homónimas.

Cada aparición deberá clasificarse como:

- uso correcto del déficit de asunción;
- uso histórico erróneo;
- consecuencia dependiente del error;
- objeto distinto que accidentalmente comparte símbolo;
- revisión independiente que no queda resuelta por `RES-DELTA-001`.

---

## 9. Si `R*(1−α)` resulta útil para otro objeto

La expresión multiplicativa no es algebraicamente absurda. Puede representar legítimamente:

> la porción de una cuota causal `R*` que permanece sin cubrir cuando α es definida como proporción interna de esa cuota.

Pero ése sería **otro objeto formal**, con otro tipo de α o con otra variable de cobertura.

Si la segunda edición decide conservar ese cálculo por utilidad propia, deberá:

1. darle otro símbolo;
2. darle otro nombre;
3. definir expresamente su tipo;
4. impedir que se confunda con `Δ = R* − α`;
5. no usarlo para inversión causal.

No debe conservarse bajo el mismo símbolo por mera inercia editorial.

---

## 10. Revisiones vinculadas

### Adjudicadas en cuanto a fórmula y signo

- `review.mci.delta_crosswork`;
- `review.mci.delta_impossible_cases`;
- `review.mcii.delta_sign`;
- `review.calc.delta_history`.

### Permanecen abiertas por problemas propios

- `review.mcii.delta_magnitude`;
- `review.mcii.delta_appendix`;
- `review.calc.deltaB_type`;
- `review.prometeo.delta_comparability`.

La segunda edición no debe usar la corrección de Δ para cerrar estas últimas por arrastre.

---

## 11. Criterio de cierre de 2E-DELTA-001

La entrada podrá pasar de **PREPARADO** a **INCORPORADO** únicamente cuando:

1. se hayan localizado todas las dependencias de la fórmula multiplicativa;
2. las definiciones de Δ usadas para inversión causal sean sustractivas;
3. los rangos y propiedades de signo hayan sido corregidos;
4. los ejemplos hayan sido recalculados;
5. las tablas, formularios y pseudocódigo dependientes hayan sido revisados;
6. el caso `0.191 − 0.60 = −0.409` sea reproducible;
7. los objetos distintos que usen Δ tengan tipado y símbolo separados;
8. las revisiones independientes permanezcan visibles.

La corrección editorial debe reparar el error sin borrar que existió en la primera edición.