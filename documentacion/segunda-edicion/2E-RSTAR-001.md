# 2E-RSTAR-001 — Corrección y normalización formal de R* para segunda edición

> **Entrada editorial derivada para segunda edición.** Se rige por `RES-RSTAR-001`, resolución MANT vigente por adjudicación autoral explícita. No modifica las fuentes canónicas de primera edición y conserva las formulaciones históricas como proveniencia.

- **Estado:** PREPARADO PARA SEGUNDA EDICIÓN / RESOLUCIÓN FORMAL ADOPTADA
- **Prioridad:** MUY ALTA
- **Normalización conceptual:** `NORM-RSTAR-EGO-001`
- **Auditoría formal:** `AUD-RSTAR-001`
- **Validación:** `VAL-RSTAR-001`
- **Resolución vigente:** `RES-RSTAR-001`
- **Decisión autoral:** `R*` es el **eigenvector de responsabilidad** y `R*_i(D)` es la **proporción estable de convergencia causal** del nodo `i` respecto de `D`.

---

## 1. Crosswalk obligatorio

La segunda edición deberá presentar la arquitectura:

`φ₁ encadenadas → W → Q_D,b_D → r_D → M_R(D) → R*(D)`

mientras:

`φ₂ → α`

Y:

`Δ=R*−α`.

Los objetos quedan tipados así:

- `φ₁`: primera mediación; produce acto/colapso;
- `W`: determinaciones causales locales con convención `W_ij=w(i→j)`;
- `D`: resultado respecto del cual se distribuye causalidad;
- `Q_D`: determinaciones primitivas entre ancestros causales de `D`;
- `b_D`: determinaciones primitivas directas sobre `D`;
- `r_D`: atribución causal total antes de normalizar;
- `M_R(D)`: operador espectral de propagación/atribución causal;
- `R*(D)`: distribución estable de responsabilidad;
- `φ₂`: retorno/asunción interna;
- `α`: asunción efectiva;
- `Δ`: brecha `R*−α`.

---

## 2. Fórmula vigente

Para:

`ρ(Q_D)<1`,

se define:

`r_D=(I−Q_D)^−1b_D`.

Equivalentemente:

`r_D=Σ_{k=0}^∞Q_D^k b_D`.

La normalización es:

`R*(D)=r_D/[1^T r_D]`.

Defínase:

`η_D=[1^T r_D]^−1`.

Entonces:

`M_R(D)=Q_D+η_D b_D1^T`.

Y:

`M_R(D)R*(D)=R*(D)`.

El eigenvalor dominante asociado es:

`λ_1=1`.

---

## 3. Interpretación de R*

`R*_i(D)` responde:

> ¿a qué proporción estable converge la atribución causal del nodo `i` respecto de `D`?

Si:

`R*=(0.58,0.27,0.15)^T`,

la distribución estable es:

`58% / 27% / 15%`.

La iteración:

`x^(t+1)=M_R(D)x^(t)`

representa rondas de propagación/atribución causal hasta que las proporciones dejan de cambiar.

Debe distinguirse de la **velocidad de convergencia**, que depende del espectro secundario, en particular de `|λ_2|` o de la brecha:

`γ=1−|λ_2|`.

---

## 4. Regla de aristas

La segunda edición deberá distinguir:

- **arista primitiva:** mecanismo causal local documentado;
- **arista acumulada:** resumen de rutas ya representadas.

Una arista acumulada no puede entrar al cálculo junto con las mismas rutas primitivas que resume.

Un mecanismo directo adicional puede coexistir con rutas mediadas sólo si está documentado como mecanismo independiente.

---

## 5. Regla de normalización

La normalización ocurre **una sola vez y al final** de la reconstrucción causal.

No se conservan como regla vigente las rondas que normalizan un estado intermedio y luego lo reutilizan como si mantuviera magnitud causal absoluta.

Prometeo Caso 2 valida esta regla al reproducir exactamente:

`68.7% / 19.9% / 11.4%`.

Prometeo Caso 3 muestra que una normalización intermedia altera la atribución upstream.

---

## 6. Transformación formal

### Conservar

- influencia transitiva;
- múltiples caminos;
- producto de pesos dentro de una ruta;
- necesidad de distribuir el resultado entre múltiples condiciones causales.

### Corregir

No mantener:

`R* = distribución de φ₂`.

Usar:

`R* = distribución exterior de atribución causal de colapsos de φ₁ respecto de D`.

No mantener como fórmula vigente:

`R*=eig(W)`.

Debe sustituirse por la arquitectura adjudicada en `RES-RSTAR-001`.

---

## 7. Axiomatización

La segunda edición deberá corregir conjuntamente:

- `W` frente a `W^T`;
- sumidero con fila nula;
- estocasticidad por filas;
- fuerte conexidad/irreducibilidad;
- Perron–Frobenius aplicado a la matriz causal cruda.

La solución vigente separa:

`W` = red causal local

de:

`M_R(D)` = operador espectral de responsabilidad.

El nodo final `D` se separa del espacio causal activo mediante `b_D`.

---

## 8. Metrología Causal I y II

Conservar el objetivo de medir influencia causal total, no proximidad.

Corregir cualquier afirmación que haga depender la existencia de `R*` de que la matriz causal cruda sea irreducible.

Las condiciones de Perron–Frobenius deben formularse sobre `M_R(D)`.

Los DAG son válidos: `Q_D` puede ser nilpotente y la atribución total se calcula por suma finita de rutas.

---

## 9. El cálculo de la responsabilidad

### Conservar

- `R*` como distribución causal descriptiva;
- `ΣR*_i=1`;
- independencia respecto de dolo y α;
- transitividad y mediación.

### Corregir

Toda identificación:

`R*=eig(W)`

o código equivalente basado en iteración de potencia sobre la matriz causal cruda.

Los grafos impresos revisados son DAG; por tanto, sus matrices `W` son nilpotentes y no producen mediante ese algoritmo los vectores positivos publicados.

Todos los vectores afectados deberán recalcularse con `RES-RSTAR-001`.

Los porcentajes de primera edición se conservarán sólo como registro histórico cuando no sean reproducibles.

---

## 10. Método Prometeo

### Conservar

- composición causal a través de rutas;
- posibilidad de responsabilidad upstream;
- multiplicación de pesos dentro de una ruta;
- contraprueba de que el nodo de diseño no siempre domina.

### Corregir

No tratar como equivalentes:

1. rondas con normalización intermedia;
2. suma de rutas;
3. aristas acumuladas;
4. `w/Σw`;
5. eigenvector de `W`.

`w/Σw` queda únicamente como caso especial cuando:

`Q_D=0`.

---

## 11. Revisiones adjudicadas

Quedan resueltas por `RES-RSTAR-001`:

- `review.prometeo.rstar_algorithm_equivalence` — NO equivalencia;
- `review.prometeo.design_node_presumption` — NO universalidad;
- `review.calc.published_vectors_reproduction` — el algoritmo declarado NO reproduce los vectores impresos;
- `review.calc.orientation`;
- `review.calc.sinks`;
- `review.rstar.sink_irreducibility`;
- `review.tf.rstar_orientation`;
- `review.axiom.rstar_sink`;
- `review.mci.rstar_orientation`;
- `review.mcii.sink_normalization`.

Las revisiones históricas permanecen visibles en el mapa como proveniencia.

---

## 12. Problemas que permanecen abiertos

Esta resolución no resuelve:

- calibración empírica de `w`;
- validación externa de rangos;
- equivalencia entre necesidad contrafáctica y peso escalar;
- interacción no aditiva entre rutas;
- rutas solapadas;
- condiciones conjuntas e hiperaristas;
- causalidad acumulativa;
- Shapley;
- feedback con `ρ(Q_D)≥1`;
- temporalización de ciclos;
- reasignación de nodos instrumentales;
- validación científica o jurídica universal.

---

## 13. Pruebas ya superadas

| Prueba | Estado |
|---|---|
| DAG simple | SUPERADA |
| ruta directa + mediada | SUPERADA |
| múltiples rutas | SUPERADA bajo regla de arista primitiva |
| nodo final/sumidero | SUPERADA mediante `b_D` |
| orientación `i→j` | SUPERADA |
| existencia/unicidad en DAG | SUPERADA |
| feedback atenuado | SUPERADA si `ρ(Q_D)<1` |
| Perron–Frobenius | SUPERADA para `M_R(D)` bajo hipótesis declaradas |
| independencia de α | SUPERADA |
| Prometeo Caso 2 | REPRODUCCIÓN EXACTA |
| reproducción de vectores históricos generales | NO; requiere recálculo editorial |

---

## 14. Inventario de recálculo obligatorio

Antes de pasar `2E-RSTAR-001` a **INCORPORADO**, deberá levantarse un inventario completo de toda aparición de:

- `R*`;
- `W R*=λR*`;
- `W^T R*=λR*`;
- iteración de potencia;
- Perron–Frobenius;
- Banach aplicado a R*;
- matrices estocásticas/Markov usadas como equivalente de R*;
- rondas de Prometeo;
- aristas acumuladas;
- `w/Σw`;
- tablas de porcentajes R*;
- código y pseudocódigo que calcule R*;
- teoremas/corolarios dependientes de la antigua formulación.

Para cada aparición deberá registrarse:

1. obra y localizador;
2. tipo de formulación;
3. si es histórica, formal, operativa o de calibración;
4. si requiere recálculo numérico;
5. si requiere reescritura conceptual;
6. si sólo requiere nota histórica;
7. dependencias aguas abajo.

---

## 15. Criterio de cierre editorial

`2E-RSTAR-001` pasará a **INCORPORADO** sólo cuando:

1. todas las apariciones relevantes hayan sido inventariadas;
2. los casos numéricos afectados hayan sido recalculados;
3. los teoremas de existencia/convergencia hayan sido corregidos;
4. `W` y `M_R(D)` estén tipados por separado en todas las obras;
5. se eliminen normalizaciones intermedias no justificadas;
6. se distingan aristas primitivas y acumuladas;
7. se documente `ρ(Q_D)<1` como condición de dominio;
8. se incorpore la distinción entre proporción y velocidad de convergencia;
9. se preserve la historia de primera edición;
10. ninguna formalización sea presentada como validación empírica por el solo hecho de ser matemática.

---

## 16. Fórmula editorial de referencia

La formulación vigente para segunda edición es:

`φ₁ encadenadas → W → Q_D,b_D → r_D=(I−Q_D)^−1b_D → R*(D)`

con:

`R*(D)=r_D/[1^T r_D]`.

Y:

`M_R(D)=Q_D+η_D b_D1^T`,

`η_D=[1^T r_D]^−1`,

`M_R(D)R*(D)=R*(D)`.

En paralelo:

`φ₂ → α`

`Δ=R*−α`.

La matemática representa la genealogía causal del sistema; no redefine retrospectivamente las fuentes de primera edición.
