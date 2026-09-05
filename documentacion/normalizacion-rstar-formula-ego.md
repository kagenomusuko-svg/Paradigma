# NORM-RSTAR-EGO-001 — Normalización conceptual de R* desde la fórmula del ego

> **Documento derivado de mantenimiento, no fuente canónica.** Normaliza la genealogía conceptual y el tipado que conectan la fórmula del ego con la imputación causal y R*. La construcción matemática de `M_R(D)` fue adjudicada posteriormente en `RES-RSTAR-001`, que gobierna esta normalización.

- **ID:** `NORM-RSTAR-EGO-001`
- **Estado:** NORMALIZACIÓN CONCEPTUAL VIGENTE / FORMALIZACIÓN ADJUDICADA EN `RES-RSTAR-001`
- **Ámbito:** fórmula del ego, φ₁, φ₂, W, δ_ext, R*, α y Δ
- **Decisión autoral MANT:** `R*` es el **eigenvector de responsabilidad**.
- **Precisión vigente:** `R*` no es el eigenvector de la matriz causal cruda `W`; es el Perron-eigenvector del operador de responsabilidad `M_R(D)` definido en `RES-RSTAR-001`.

---

## 1. Punto de partida: la fórmula individual del ego

La forma compacta del ciclo individual es:

`Ego_i(t) = φ₂,i( φ₁,i(v_i(t), c_i(t)), I_i(t) )`.

Defínase el acto o colapso producido por la primera mediación:

`a_i(t) = φ₁,i(v_i(t), c_i(t))`.

La segunda mediación retorna ese acto al ego y modifica su integral:

`I_i(t+1) = φ₂,i(a_i(t), I_i(t))`.

Esquemáticamente:

`v_i, c_i → φ₁,i → a_i → φ₂,i → I_i(t+1)`.

Esta fórmula contiene dos direcciones que originan familias metrológicas distintas:

1. **producción causal hacia el mundo**, asociada a `φ₁`;
2. **retorno/asunción hacia el ego**, asociada a `φ₂`.

---

## 2. Del ego individual al campo causal

El acto producido por un ego puede entrar como condición del campo de otro ego:

`a_i → c_j`.

Como representación auxiliar:

`c_j(t) = c_j^0(t) + Σ_i Γ_ij(a_i(t))`,

donde `Γ_ij` representa la contribución causal del acto de `i` a las condiciones bajo las cuales colapsa `j`.

Entonces:

`a_j = φ₁,j(v_j, c_j^0 + Σ_i Γ_ij(a_i))`.

La estructura encadenada es:

`a_i → c_j → φ₁,j → a_j → c_k → φ₁,k → ... → D`,

donde `D` es el resultado respecto del cual se reconstruye responsabilidad.

El grafo causal es la representación metrológica externa de esas dependencias; no su fundamento ontológico.

---

## 3. W: matriz de determinaciones locales

Bajo la convención:

`W_ij = w(i→j)`,

`W_ij` representa el grado en que `i` determinó causalmente el colapso o comportamiento de `j`.

Por tanto:

`W`

representa **dependencias locales entre primeras mediaciones**.

No debe identificarse por definición con:

- responsabilidad total;
- atribución global respecto de `D`;
- `R*`;
- el operador espectral de responsabilidad.

La relación correcta es:

`φ₁ → relaciones locales → W`.

---

## 4. Composición causal por rutas

Si existe:

`A → B → C`,

la influencia de `A` sobre `C` puede transmitirse por mediación de `B`.

Bajo la aproximación multiplicativa adoptada:

`peso(A→B→C)=w_AB·w_BC`.

Si existen múltiples rutas causalmente distintas, sus contribuciones se agregan antes de normalizar, evitando contabilizar dos veces un mismo mecanismo.

La estructura vigente es:

`influencia total de i sobre D = contribución directa + contribuciones mediadas por rutas hacia D`.

---

## 5. δ_ext: exteriorización atributiva

Areópago distingue:

`δ_int(t) = Ego(t) − I(t)`

como retorno interno del acto al sujeto, y:

`δ_ext(t) = atribución(φ₁(v_t,c_t), Sujeto)`

como atribución exterior del acto al nodo cuya cadena causal es reconstruible.

Regla de normalización:

> **La imputación exterior tiene forma atributiva análoga a φ₂, pero su material causal es la cadena de φ₁.**

Por tanto:

- `δ_int` requiere `φ₂` interna;
- `δ_ext` opera sobre colapsos de `φ₁` y cadenas causales reconstruibles;
- la semejanza estructural no convierte `δ_ext` en medición de `φ₂` interna.

---

## 6. Corrección del crosswalk de Transformación formal

La formulación histórica que presenta `R*` como «lectura exterior de la distribución de φ₂» debe precisarse.

La formulación vigente es:

`R* = distribución exterior de atribución causal de los colapsos de φ₁ respecto de un resultado D`.

No:

`R* = medida de cuánto operó la φ₂ interna de cada ego`.

Ese segundo objeto pertenece a la genealogía de α.

---

## 7. R*(D): distribución global y convergencia causal

Para un resultado `D`:

`R*_i(D) = proporción estable de convergencia causal del nodo i respecto de D`.

Con:

`Σ_i R*_i(D)=1`.

`R*` no mide intención, dolo, culpabilidad, arrepentimiento, reconocimiento subjetivo ni sanción.

Mide la posición causal relativa que resulta estable bajo el operador de responsabilidad.

---

## 8. M_R(D): operador espectral de responsabilidad

`RES-RSTAR-001` adjudica:

`Q_D` = matriz de determinaciones primitivas entre ancestros causales de `D`;

`b_D` = vector de determinaciones primitivas directas sobre `D`.

Para:

`ρ(Q_D)<1`,

se define:

`r_D=(I−Q_D)^−1b_D`.

La distribución normalizada es:

`R*(D)=r_D/[1^T r_D]`.

Con:

`η_D=[1^T r_D]^−1`,

se define:

`M_R(D)=Q_D+η_D b_D1^T`.

Y:

`M_R(D)R*(D)=R*(D)`.

La iteración:

`x^(t+1)=M_R(D)x^(t)`

representa rondas de propagación/atribución causal que, bajo las condiciones espectrales vigentes, convergen a `R*(D)`.

Así, `R*` es el **Perron-eigenvector normalizado del operador de responsabilidad**.

---

## 9. El nodo final D

`D` es el objeto respecto del cual se distribuye causalidad.

No recibe automáticamente responsabilidad por ser el sumidero del grafo.

Su separación en `b_D` permite que los nodos causales formen el espacio de responsabilidad sin exigir que el resultado sea homogéneo a sus causas.

---

## 10. Rama interna: φ₂ → α

La otra dirección de la fórmula del ego es:

`a_i → φ₂,i → I_i(t+1)`.

De esta rama deriva la genealogía de la asunción.

Conforme a `RES-ALPHA-001`:

`α_i = grado de asunción efectiva de la posición causal del nodo i`.

Su operacionalización aplicada puede registrar acciones, reparaciones y consecuencias efectivamente soportadas, incluidas modalidades voluntarias, forzadas o impuestas.

---

## 11. R* y α como dos lecturas de la fórmula del ego

### Rama causal/exterior

`v,c → φ₁ → acto → W → Q_D,b_D → r_D → M_R(D) → R*(D)`.

### Rama de retorno/asunción

`acto → φ₂ → I(t+1) → α`.

Por tanto:

- `R*` cuantifica cuánto causalmente converge hacia cada nodo respecto del resultado;
- `α` cuantifica cuánto de esa posición fue efectivamente asumido o soportado.

---

## 12. Δ como comparación entre ambas ramas

Con `RES-DELTA-001`:

`Δ_i = R*_i − α_i`.

Genealogía:

`φ₁ → W → Q_D,b_D → M_R(D) → R*`

frente a:

`φ₂ → α`.

Y:

`R*−α → Δ`.

La comparación sigue siendo descriptiva; no introduce por sí sola una predicación normativa.

---

## 13. Esquema maestro vigente

```text
v_i,c_i
   │
   ▼
 φ₁,i
   │
   ▼
 a_i ───────────────────────────────┐
   │                                │
   │ entra en el campo de j         │ retorno/asunción
   ▼                                ▼
 c_j                               φ₂,i
   │                                │
   ▼                                ▼
 φ₁,j                            I_i(t+1)
   │                                │
   ▼                                ▼
 ...                               α_i
   │
   ▼
 D

φ₁ encadenadas
      │
      ▼
      W
      │
      ▼
   Q_D,b_D
      │
      ▼
     r_D
      │
      ▼
   M_R(D)
      │
      ▼
    R*(D)
      │
      ├──────────────┐
      │              ▼
      │             α_i
      │              │
      └───────┬──────┘
              ▼
        Δ_i=R*_i−α_i
```

Forma compacta:

`φ₁ → W → Q_D,b_D → r_D → M_R(D) → R*`

`φ₂ → α`

`R*−α=Δ`.

---

## 14. Qué queda fijado

1. `W` representa determinaciones locales de `φ₁`.
2. `W` no es responsabilidad global por definición.
3. `δ_ext` atribuye exteriormente colapsos de `φ₁` y conserva una estructura atributiva análoga a `φ₂`.
4. `D` se separa del espacio de causas.
5. `Q_D` y `b_D` reconstruyen la red pertinente respecto de `D`.
6. `r_D=(I−Q_D)^−1b_D` calcula atribución total por rutas para `ρ(Q_D)<1`.
7. La normalización se realiza una sola vez al final.
8. `M_R(D)=Q_D+η_D b_D1^T` es el operador espectral de responsabilidad vigente.
9. `R*_i` es la proporción estable de convergencia causal del nodo `i`.
10. La velocidad de convergencia es distinta y depende del espectro secundario.
11. α pertenece a la rama de asunción/retorno.
12. Δ compara ambas ramas mediante `R*−α`.

---

## 15. Problemas que permanecen abiertos

`RES-RSTAR-001` no resuelve:

- calibración empírica de `w`;
- validación externa de rangos;
- interacción no aditiva entre rutas;
- rutas solapadas;
- condiciones conjuntas e hiperaristas;
- causalidad acumulativa;
- Shapley;
- feedback con `ρ(Q_D)≥1`;
- temporalización de ciclos fuera del dominio del operador;
- reasignación de nodos instrumentales a diseñadores;
- validación científica o jurídica universal del modelo.

---

## 16. Revisiones formalmente adjudicadas por RES-RSTAR-001

Quedan resueltas respecto de su problema histórico:

- `review.prometeo.rstar_algorithm_equivalence` — no equivalencia;
- `review.prometeo.design_node_presumption` — no universalidad;
- `review.calc.published_vectors_reproduction` — no reproducibilidad del operador declarado;
- `review.calc.orientation`;
- `review.calc.sinks`;
- `review.rstar.sink_irreducibility`;
- `review.tf.rstar_orientation`;
- `review.axiom.rstar_sink`;
- `review.mci.rstar_orientation`;
- `review.mcii.sink_normalization`.

Las formulaciones históricas permanecen visibles como proveniencia.

---

## 17. Criterios para implementación

Toda implementación de R* deberá:

1. preservar `W_ij=i→j`;
2. distinguir aristas primitivas de acumuladas;
3. separar `D` del espacio causal activo;
4. construir `Q_D` y `b_D`;
5. verificar `ρ(Q_D)<1` antes de aplicar el operador vigente;
6. calcular la atribución total antes de normalizar;
7. normalizar una sola vez;
8. verificar `M_RR*=R*`;
9. distinguir porcentajes `R*_i` de velocidad de convergencia;
10. mantener independencia respecto de α;
11. rechazar o modelar separadamente feedback fuera de dominio;
12. reportar calibraciones y supuestos sin presentarlos como teoremas.

---

## 18. Proveniencia

La normalización se apoya en lectura transversal de:

- *Caos: El abismo del ego y la doble mediación*, cap. VI;
- *Afrodita Areia: Areópago*, apéndice II;
- *La transformación formal*, cap. 2.1;
- *El cálculo de la responsabilidad*;
- *El método Prometeo*.

La construcción exacta de `M_R(D)` y la interpretación de `R*_i` como proporción estable de convergencia causal fueron adjudicadas autoralmente en MANT mediante `RES-RSTAR-001` después de la primera edición. No deben retroproyectarse como si todas las obras históricas hubieran usado ya esta formulación.
