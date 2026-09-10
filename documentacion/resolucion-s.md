# RES-S-001 — Resolución MANT del constructo de sustituibilidad `S`

> **Documento derivado de resolución.** No modifica fuentes canónicas ni introduce una fórmula nueva. Adjudica el núcleo conceptual de `S` y separa ese constructo de sus estimadores, proxies y calibraciones históricas para preparar la normalización formal de segunda edición.

- **ID:** `RES-S-001`
- **Estado:** **RESUELTA EN NÚCLEO CONCEPTUAL / ESTIMADOR FORMAL Y CALIBRACIÓN PENDIENTES**
- **Familia:** `S`, `S_prob`, `S_op`, `S_est`, `S_app`, `R*_neta`
- **Auditoría de origen:** `AUD-S-001`
- **Entrada editorial:** `2E-S-001`
- **Dependencia formal principal:** `RES-RSTAR-001`

## 1. Problema adjudicado

`AUD-S-001` confirmó que el corpus conserva un objeto doctrinal estable de sustituibilidad, pero lo representa mediante fórmulas y procedimientos que no son matemáticamente idénticos y que en algunos casos contienen errores formales.

La tensión no se resuelve eligiendo una de las fórmulas históricas como definición universal. Se resuelve distinguiendo:

1. el **constructo** que `S` pretende medir;
2. los **estimadores formales** propuestos para aproximarlo;
3. los **proxies/operacionalizaciones aplicadas** usados cuando el estimador formal no está disponible;
4. las **calibraciones numéricas** asociadas a dominios concretos.

## 2. Núcleo conceptual vigente

Se conserva como objeto de `S` la pregunta contrafáctica:

> **¿en qué grado el resultado `D`, en su forma relevante, pertenece al campo o estructura y habría ocurrido sin la singularidad causal del actor `i`?**

Por tanto:

- `S → 1`: alta sustituibilidad; el campo explica la mayor parte de la forma relevante de `D` y la singularidad de `i` es poco determinante para esa forma;
- `S → 0`: baja sustituibilidad; la singularidad causal de `i` es necesaria o altamente determinante para explicar esa forma de `D`.

`S` no mide dolo, culpa, moralidad, intención ni responsabilidad jurídica.

Esta adjudicación es consistente con la formulación probabilística de *Metrología Causal*, con la intuición estructural de *Axiomatización* y con los usos aplicados de *El cálculo de la responsabilidad* y Prometeo.

## 3. `S_prob` no es todavía una definición operacional cerrada

La formulación contrafáctica probabilística funciona como el ancla semántica más directa del constructo, pero el corpus distingue al menos:

`S_actor = P(D | c, otro actor en la posición de i)`

y
`S_campo = P(D | c, sin actor en la posición de i)`.

La regla histórica posterior entre `max(...)` y una combinación ponderada no constituye una única operación demostrada.

Por tanto, la segunda edición deberá decidir explícitamente qué intervención contrafáctica representa el símbolo simple `S` y si `S_actor` y `S_campo` se conservan como objetos separados.

Esta resolución no inventa esa regla.

## 4. `S_op` queda tipado como proxy local

La expresión histórica:

`S_op(t)=||c||/(||c||+||a_t||)`

puede conservar intuición sobre predominio relativo del campo frente a la activación singular, pero no es por identidad matemática la probabilidad contrafáctica de sustituibilidad.

Además, `||c||` y `||a_t||` pertenecen históricamente a espacios distintos y sólo pueden combinarse si existe una normalización que los haga comparables.

Por tanto:

> **`S_op` es un proxy local de predominio estructural sujeto a conmensurabilidad y calibración; no es `S` por definición.**

`review.axiom.Sop_units` permanece abierto como problema metrológico, no doctrinal.

## 5. `S_est` histórico no puede ser el estimador vigente

La fórmula histórica:

`S_est(i)=1−D_KL(R* || R*^(i))/log(m)`

no puede trasladarse intacta porque:

- `D_KL(P||Q)≤log(m)` es falso en general;
- la expresión no garantiza pertenencia a `[0,1]`;
- la construcción de `R*^(i)` dependía del aparato histórico de `R*` por eigenvector de `W/Wᵀ`;
- `RES-RSTAR-001` sustituyó ese aparato por la arquitectura `Q_D,b_D → r_D → M_R(D) → R*(D)`.

Por tanto:

> **la intuición de medir sustituibilidad mediante una intervención de reemplazo/ablación puede conservarse; la fórmula histórica de `S_est` no.**

Cualquier nuevo estimador estructural deberá reconstruirse y demostrarse sobre el operador causal vigente.

## 6. No existe un puente demostrado `S_op ↔ S_est`

La correspondencia histórica que pretende una función monótona entre `S_op` y `S_est` no queda demostrada por Pinsker ni por las cotas publicadas.

Los dos objetos responden a niveles distintos:

- `S_op`: predominio local campo/activación;
- `S_est`: sensibilidad global de una distribución causal bajo una regla de sustitución.

Puede conservarse la hipótesis ordinal:

`mayor predominio estructural → mayor sustituibilidad esperada`,

pero no una función universal de traducción sin nueva prueba o calibración.

`review.axiom.S_bridge` permanece como deuda formal.

## 7. `S_app` — scores de El cálculo y Prometeo

Los scores documentales de *El cálculo de la responsabilidad* y Prometeo conservan el mismo referente conceptual de sustituibilidad, pero no son fórmulas universales de `S`.

Sus criterios —formalización, reemplazabilidad, costo de desobedecer, presión/incentivos, conducta de pares u otros— son observables que intentan estimar el constructo en un expediente concreto.

Por tanto:

> **`S_app` es una operacionalización aplicada del constructo, cuya comparabilidad con el estimador formal deberá demostrarse o calibrarse.**

La igualdad de pesos entre criterios es una decisión de modelo, no una consecuencia ontológica.

## 8. Rangos por Hijos de Afrodita

La orientación cualitativa puede conservarse como hipótesis doctrinal:

- mayor determinación por el campo → `S` esperablemente mayor;
- mayor idiosincrasia del eje propio → `S` esperablemente menor.

Los intervalos numéricos concretos no se siguen deductivamente de esa relación.

Por tanto:

- la correspondencia ordinal puede conservarse como hipótesis;
- las bandas numéricas son calibraciones revisables;
- ninguna tabla por Hijos debe presentarse como teorema sin una derivación o validación independiente.

## 9. Nodo de diseño

Ser nodo de diseño no implica por definición `S≈0`.

Un diseño puede ser idiosincrático, pero también estandarizado, regulado, fungible o prácticamente inevitable para diferentes actores.

`review.mci.s_designer_conflict` queda adjudicada en su núcleo: se trata de una generalización contingente, no de una propiedad necesaria del concepto.

## 10. `R*_neta`

La operación histórica:

`R*_neta = R*(1−S)`

puede conservarse únicamente como **modelo aplicado candidato de componente idiosincrático** hasta que `S` esté formalmente normalizada.

No se considera teorema derivado del constructo de sustituibilidad por el solo hecho de que `S∈[0,1]`.

La segunda edición deberá demostrar qué objeto produce el producto y qué relación mantiene con `R*` total antes de presentarlo como magnitud metrológica consolidada.

## 11. Arquitectura obligatoria para segunda edición

La normalización de `S` deberá dejar una ruta explícita:

`constructo de sustituibilidad → intervención contrafáctica → estimador formal → observables/proxy → aplicación`.

Como mínimo, el estimador futuro deberá:

- depender explícitamente del resultado `D`;
- definir sin ambigüedad la operación de sustitución/ablación;
- ser compatible con `RES-RSTAR-001`;
- justificar `S∈[0,1]` por construcción o teorema válido;
- especificar qué ocurre si retirar/reemplazar `i` altera conectividad o posibilidad de `D`;
- distinguir estimación formal de calibración aplicada;
- demostrar o calibrar cualquier puente hacia `S_app` o `S_op`.

## 12. Qué queda resuelto

Queda adjudicado que:

- el constructo doctrinal de `S` se conserva;
- las formulaciones históricas no son identidades entre sí;
- `S_op` es proxy, no definición universal;
- `S_est` histórico es formalmente defectuoso y debe reconstruirse;
- el puente `S_op–S_est` no está demostrado;
- `S_app` es un estimador documental/aplicado;
- los rangos numéricos por Hijos son calibración, no deducción ontológica;
- `S≈0` no es propiedad necesaria de un nodo de diseño;
- `R*_neta` requiere revalidación independiente.

## 13. Qué permanece abierto

Permanecen para trabajo formal/metrológico de segunda edición:

- definición exacta de la intervención contrafáctica;
- relación entre `S_actor` y `S_campo`;
- estimador formal de `S` sobre el operador vigente de `R*`;
- sustitución de la normalización KL;
- conmensurabilidad de `S_op`;
- calibración de `S_app`;
- calibración de rangos por dominio/Hijos;
- revalidación de `R*_neta`;
- recálculo de ejemplos y tablas dependientes.

No se inventan fórmulas ni números para cerrar esas deudas durante MANT.
