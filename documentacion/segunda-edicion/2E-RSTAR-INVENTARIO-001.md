# 2E-RSTAR-INVENTARIO-001 — Inventario transversal de dependencias de R*

> **Documento operativo de campaña de segunda edición.** Deriva de `RES-RSTAR-001`, `2E-RSTAR-001` y `AUD-MANT-TRANS-001`. No modifica fuentes canónicas, no recalcula valores y no convierte deudas formales o empíricas en resultados validados. Su función es determinar qué tratamiento requiere cada aparición de `R*` antes de cualquier incorporación editorial.

- **Estado:** EN CURSO — TRAMO 1 COMPLETADO: AXIOMATIZACIÓN
- **Fase:** MANT — campaña de segunda edición habilitada
- **Objeto rector:** `RES-RSTAR-001`
- **Entrada editorial:** `2E-RSTAR-001`
- **Regla de campaña:** **PREPARADO ≠ INCORPORADO**

---

## 1. Regla de clasificación en dos ejes

El inventario no debe confundir **qué clase de aparición existe** con **qué trabajo editorial exige**.

### Eje A — tipo de aparición

Se conserva el inventario mínimo fijado por `AUD-MANT-TRANS-001`:

1. definición directa;
2. axioma, lema, teorema o prueba;
3. fórmula dependiente;
4. vector o valor numérico publicado;
5. ejemplo o caso calculado;
6. código o pseudocódigo;
7. interfaz con otro objeto (`S`, `α`, `Δ`, `Δ_B`, IIC, REC u otros).

### Eje B — tratamiento requerido

Cada aparición se clasifica además por uno de los siguientes tratamientos principales:

- **SD — Sustitución directa.** Reescritura de definición, notación u orientación que no exige demostrar de nuevo una cadena dependiente. Incluye la nota histórica cuando una formulación anterior debe conservarse como proveniencia.
- **RO — Redemostración obligatoria.** La conclusión o la prueba usa propiedades específicas del operador histórico (`eig(W)`, `eig(Wᵀ)`, Markov sobre `W`, perturbación espectral del operador antiguo, etc.). No basta sustituir símbolos: debe verificarse si el resultado sobrevive bajo `Q_D,b_D,r_D,M_R(D)` y, si procede, reconstruir la demostración.
- **RC — Recálculo con posible cambio de resultado.** Hay porcentajes, vectores, tablas, casos o análisis de sensibilidad cuyo valor depende del aparato causal anterior. No se recalculan hasta disponer de un mínimo operacional de `ŵ/U(ŵ)` coherente con `RES-EVID-001`.
- **IR — Interfaz a retipar.** La adjudicación conceptual ya existe, pero la fórmula debe declarar correctamente su dependencia del operador vigente y de los objetos upstream reconstruidos. Puede corregirse el tipo sin publicar todavía nuevos números.

Los códigos no son mutuamente excluyentes en dependencias complejas. Un teorema puede requerir `RO` y contener además una tabla `RC`; una interfaz puede requerir `IR` y quedar bloqueada por una redemostración upstream.

---

## 2. Regla de dependencia de campaña

El carril causal se mantiene en este orden:

`EVID / estimación de w → ŵ/U(ŵ) → R* vigente y recálculos → S formal → Δ/Δ_B → IIC → ejemplos`.

El carril de integración puede avanzar en paralelo:

`RSC → I(t) → α formal → comparabilidad → Δ`,

pero con una barrera explícita:

> **el carril RSC→I(t)→α no puede usar ni normalizar objetos que dependan de `R*_neta`, `S` reconstruida o cualquier otra función cuyo upstream sea `R*`.**

Sí puede avanzar en el nivel conceptual y en el crosswalk entre `α_H`/`α_P`, así como en la distinción voluntaria/forzada/impuesta, mientras conserve esa independencia.

---

## 3. Tramo 1 — Axiomatización del Sistema de la Doble Mediación

Fuente canónica: `corpus/fuentes/Axiomatizacion_Sistema_Doble_Mediacion.md`.

### 3.1 Prólogo, mapa del libro y glosario

| Localizador | Aparición | Tipo A | Tratamiento | Motivo |
|---|---|---|---|---|
| Prólogo II–III; mapa de Partes V–VI | `Δ=R*−α`; `R*` presentado como eigenvector dominante de `Wᵀ` | definición / interfaz | `SD` + `IR` | La semántica causal adjudicada se conserva; debe sustituirse la formulación vigente y conservarse la del eigenvector de `Wᵀ` como historia de primera edición. |
| VI. Audiencia y notación | `R*∈Δⁿ` | tipado | `SD` | El tipado como distribución normalizada puede conservarse; cambia el mecanismo de construcción. |
| Apéndice C, glosario | “Imputación causal = eigenvector dominante de `Wᵀ`” | definición resumida | `SD` | Requiere crosswalk histórico, no un cálculo nuevo. |

### 3.2 Parte III — S y su dependencia de R*

| Localizador | Aparición | Tipo A | Tratamiento | Motivo / bloqueo |
|---|---|---|---|---|
| Def. 3.2 | `S_est(i)=1−D_KL(R* || R*^(i))/log(m)`; `R*^(i)` construido desde `(W^(i))ᵀ` | fórmula dependiente / interfaz | `RO` | El estimador formal de `S` depende del operador histórico. `2E-S-001` exige reconstruirlo sobre el aparato causal vigente; no es sustitución textual. |
| Prop. 3.3 | puente `S_op↔S_est` y preservación de orden | teorema/prueba | `RO` | La demostración mezcla KL, perturbación de `R*`, desviación de fila y normas de estados sin una cadena demostrada suficiente. Debe rehacerse después de fijar el nuevo estimador formal de `S`. |
| Lema 3.4 | rangos de `S_op/S_est` por modo dominante | calibración / fórmula dependiente | `RO` + deuda empírica | Los rangos dependen del puente y de `S_est`; su estatus sigue siendo calibración revisable. No se promueven a teorema por edición. |

**Resultado del tramo:** `S_est` y el puente `S_op↔S_est` quedan en **redemostración obligatoria**, no en sustitución directa.

### 3.3 Parte V — Δ

| Localizador | Aparición | Tipo A | Tratamiento | Motivo / bloqueo |
|---|---|---|---|---|
| Def. 5 | `Δ_i=R*_i−α_i` y referencia al “eigenvector principal de Wᵀ” | interfaz | `IR` + `SD` | `RES-DELTA-001` ya adjudica el núcleo de Δ. Debe retiparse la procedencia de `R*`; la fórmula de diferencia no exige por sí sola recalcular. |
| Teorema 5 | cota `Δ_i∈[-1,1]` | teorema | `SD` condicionado | La prueba sólo necesita `R*_i,α_i∈[0,1]`; puede conservarse si el operador vigente mantiene `R*` normalizado en el simplex. Debe eliminarse la justificación específica por Perron–Frobenius sobre `Wᵀ`. |
| Teorema 5.1 | `dΔ/dt=dR*/dt−dα/dt` | fórmula dependiente | `IR` | Requiere declarar qué significa `R*(t)` cuando cambia `D`/grafo/pesos y no usar derivabilidad sin hipótesis. No necesita todavía nuevos números. |
| Prop. 5.2 y diagnósticos | inferencias desde `Δ_i<0` y completitud de `G` | prueba / interfaz | `RO` | Debe revisarse separadamente de la definición de Δ; no puede heredarse como consecuencia automática del cambio de operador. |

### 3.4 Parte VI — definición, existencia y algoritmo de R*

| Localizador | Aparición | Tipo A | Tratamiento | Motivo / bloqueo |
|---|---|---|---|---|
| Def. 6 | `G=(N,A,w)`, `W` estocástica por filas con sumidero de fila nula | definición | `SD` estructural | Segunda edición debe separar `W` como red local de `Q_D,b_D` y del operador espectral `M_R(D)`. |
| Def. 6.1 | `WᵀR*=λ₁R*` | definición directa | `SD` + nota histórica | Sustituir por `r_D=(I−Q_D)^{-1}b_D`, `R*=r_D/(1ᵀr_D)` y, como representación espectral derivada, `M_R(D)R*=R*`. |
| Teorema 6 | existencia/unicidad por Perron–Frobenius sobre `Wᵀ`; irreducibilidad, aperiodicidad, perturbación `W(ε)` | teorema/prueba | `RO` | La cadena de existencia cambia. La condición primaria vigente es `ρ(Q_D)<1`; Perron–Frobenius, cuando corresponda, se formula sobre `M_R(D)`, no sobre la matriz causal cruda. |
| Lema 6.1, método de potencias | pseudocódigo `R*_{k+1}←WᵀR*_k` y prueba de convergencia | pseudocódigo / prueba | `RO` | Debe reemplazarse el algoritmo operativo y demostrar la convergencia del procedimiento que efectivamente se conserve. |
| Lema 6.1, `R*(min/mid/max)` | bandas E→w usadas como extremos numéricos de `R*` | estimación / incertidumbre | `RC` bloqueado | `RES-EVID-001` impide usar clase E como posición intrínseca de `w`. No recalcular hasta disponer de `ŵ/U(ŵ)`. |

### 3.5 Cierre de Fundamentos — consistencia S–R*

| Localizador | Aparición | Tipo A | Tratamiento | Motivo |
|---|---|---|---|---|
| Ítem (i) de Consistencia Interna | `S_est→1 ⇒ ||R*−R*^(i)||→0` y coherencia con `S_op` | prueba / interfaz | `RO` | Depende exactamente del estimador histórico de `S_est`, del `R*^(i)` histórico y del puente no establecido. Debe redemostrarse después de reconstruir S. |
| Ítem (iv) | compatibilidad algebraica de `Δ` con TIC | prueba | `IR` / verificación posterior | La no vacuidad algebraica puede sobrevivir, pero no valida el TIC ni sus cotas. |

### 3.6 Parte VIII — TIC, Davis–Kahan y fraude annona

| Localizador | Aparición | Tipo A | Tratamiento | Motivo / bloqueo |
|---|---|---|---|---|
| Defs. 8.2–8.3 | `R*(D),R*(E)` y `S_est(E)` | interfaz | `IR` + `RO` upstream | R* se retipa directamente; `S_est` no puede conservarse hasta su reconstrucción formal. |
| Lema 8.1 | cota `R*(E)≤(1−S_est)/(m−1)` por cadena Pinsker/Davis–Kahan | teorema/prueba | `RO` | Es una de las redemostraciones prioritarias: usa perturbación del eigenvector de `W` y no se transfiere automáticamente a `M_R(D)`. |
| Lema 8.2 | cota `R*(D)>1/m` | teorema/prueba | `RO` | Deben explicitarse las hipótesis necesarias sobre dominancia de D frente al resto; no basta cambiar el operador. |
| Teoremas 8.1–8.3 | TIC y monotonicidad ligados a cotas de `R*`, `S_est` y visibilidad | teorema/prueba | `RO` | La cadena de prueba depende de Lemas 8.1–8.2 y del aparato de S. Debe verificarse completa. |
| Def. 8.7 / Teorema 8.4 | fraude annona | interfaz | `IR` + `RO` upstream | La adjudicación conceptual se conserva, pero su fórmula/cota depende del R* vigente y de resultados TIC reconstruidos. No publicar números nuevos todavía. |
| §8.5 caso banco | `R*(E)≤0.0375`, `R*(D)>0.20`, Δ e `I_inv` numéricos | caso calculado | `RC` | Requiere `ŵ/U(ŵ)`, R* vigente y S reconstruida. El resultado puede cambiar. |

### 3.7 Apéndice A — cadena Davis–Kahan

Toda la cadena A.1–A.6 queda clasificada **RO**, con sus tablas numéricas en **RC**.

Razón: los pasos de perturbación y las cotas están escritos para el eigenvector del operador histórico. Debe determinarse primero cuál es el objeto perturbado bajo la arquitectura `Q_D,b_D → r_D → R* → M_R(D)` y qué teorema de sensibilidad es aplicable. No se presume que Davis–Kahan sea transferible por mera renotación.

### 3.8 Apéndice B — casos, sensibilidad y verificación del TIC

| Localizador | Aparición | Tipo A | Tratamiento | Motivo / bloqueo |
|---|---|---|---|---|
| B.1.4 | sensibilidad del caso banco con cotas R* históricas | tabla / caso | `RC` | Recalcular sólo después de `ŵ/U(ŵ)` y de redemostrar las cotas del TIC. |
| B.2 | 18 casos con porcentajes `R*(D)/R*(E)` y mecanismos de verificación | valores publicados / evidencia | `RC` + revisión de proveniencia | Debe distinguirse valor causal estimado de evidencia independiente que sólo establece orden o mecanismo. No convertir resoluciones/historiografía en porcentajes R* sin estimador trazable. |
| B.2, mecanismos 4–5 | “lógica del grafo sin eigenvector” y cota vía `S_est` | prueba auxiliar | `RO` | Ambas rutas dependen de propiedades del formalismo antiguo o de `S_est`; requieren reconstrucción. |

### 3.9 Apéndice D — R*_neta, contrafactuales y dinámica

| Localizador | Aparición | Tipo A | Tratamiento | Motivo / bloqueo |
|---|---|---|---|---|
| Defs. D.3–D.4 | `R*_struct`, `R*_net`, `Δ_net` | interfaz | `IR` | No recalcular todavía. Su sentido debe reexpresarse sobre un contrafactual compatible con el operador vigente y con la futura S formal. |
| Prop. D.2 | identificabilidad por métodos de potencias y bandas E→w | prueba / estimación | `RO` + `RC` bloqueado | El algoritmo y la incertidumbre cambian upstream. |
| Def. D.5; Teorema D.2; Cor. D.3 | operador contrafactual y cotas Davis–Kahan | teorema/prueba | `RO` | Debe reconstruirse la perturbación sobre el aparato vigente; no asumir estabilidad espectral del `W` histórico. |
| D.4, Teoremas D.3–D.5 | dominancia, estabilidad, bifurcación mediante `R*_net` | interfaz / teorema | `IR` + `RO` upstream | No se recalculan mientras `R*_net` y S no estén reconstruidos. |

---

## 4. Resumen del tramo Axiomatización

La obra concentra los cuatro tratamientos y confirma que el inventario no puede reducirse a búsqueda y reemplazo:

- **SD:** definición vigente de `R*`, `W/Wᵀ`, glosario y referencias históricas, siempre conservando proveniencia;
- **RO:** `S_est`, puente `S_op↔S_est`, existencia/convergencia del antiguo eigenvector, Davis–Kahan, cotas y cadena TIC, contrafactuales dependientes del operador;
- **RC:** caso banco, tablas de sensibilidad, porcentajes de casos y cualquier `R*(min/mid/max)` construido con las bandas históricas E→w;
- **IR:** Δ y su dinámica, fraude annona, `R*_net/Δ_net` y demás objetos cuya semántica ya está adjudicada pero cuyo upstream formal cambia.

La consecuencia operativa es estricta:

> **Axiomatización no puede incorporarse en segunda edición por una única corrección de la Parte VI.** Parte III, Parte VIII y los Apéndices A–D contienen dependencias que deben resolverse antes de publicar una versión internamente coherente.

---

## 5. Bloqueos vigentes

1. **Recálculo numérico:** bloqueado hasta fijar un mínimo operacional de `ŵ/U(ŵ)` conforme a `RES-EVID-001`.
2. **S formal:** bloqueado hasta reconstruir su estimador sobre el aparato causal vigente; el concepto ya está adjudicado.
3. **Davis–Kahan/TIC:** bloqueado hasta decidir y demostrar la sensibilidad pertinente del operador vigente; no se presume equivalencia con la cadena histórica.
4. **`R*_net` y derivados:** pueden retiparse conceptualmente, pero no normalizarse ni recalcularse antes de cerrar `R*` y `S` upstream.
5. **Carril α:** habilitado en paralelo sólo en su formalización propia y crosswalk; bloqueado si entra por `R*_net`, `S` o cualquier dependencia de `R*`.

---

## 6. Siguiente tramo

Continuar el mismo inventario, sin modificar todavía las fuentes canónicas, en este orden operativo:

`Metrología Causal I → Metrología Causal II → La transformación formal → El cálculo de la responsabilidad → Método Prometeo → restantes apariciones transversales`.

Al cerrar esos tramos se consolidará una matriz transversal por obra, localizador, tipo de aparición, tratamiento, bloqueo y dependencia aguas abajo. Sólo entonces `2E-RSTAR-001` podrá pasar de **PREPARADO** hacia incorporación efectiva.