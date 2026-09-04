# NORM-RSTAR-EGO-001 — Normalización conceptual de R* desde la fórmula del ego

> **Documento derivado de mantenimiento, no fuente canónica.** Su función es normalizar la genealogía conceptual y el tipado de los objetos que conectan la fórmula del ego con la imputación causal y R*. No modifica retrospectivamente las primeras ediciones ni declara resuelta la construcción matemática del operador de responsabilidad.

- **ID:** `NORM-RSTAR-EGO-001`
- **Estado:** NORMALIZACIÓN CONCEPTUAL VIGENTE / FORMALIZACIÓN MATEMÁTICA ABIERTA
- **Ámbito:** fórmula del ego, φ₁, φ₂, W, δ_ext, R*, α y Δ
- **Decisión autoral MANT:** conservar `R*` como **eigenvector de responsabilidad**.
- **Precisión:** esa decisión no equivale a afirmar que `R*` sea necesariamente el eigenvector de la matriz causal cruda `W`.

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

Esta fórmula contiene dos direcciones distintas que después darán lugar a dos familias metrológicas distintas:

1. **producción causal hacia el mundo**, asociada a `φ₁`;
2. **retorno/asunción hacia el ego**, asociada a `φ₂`.

---

## 2. Del ego individual al campo causal

El acto producido por un ego no queda aislado. Puede entrar como condición del campo de otro ego.

Esquemáticamente:

`a_i → c_j`.

Para hacer visible esa dependencia puede escribirse, como representación auxiliar:

`c_j(t) = c_j^0(t) + Σ_i Γ_ij(a_i(t))`,

donde `Γ_ij` representa la contribución causal del acto de `i` a las condiciones bajo las cuales colapsa `j`.

Entonces:

`a_j = φ₁,j(v_j, c_j^0 + Σ_i Γ_ij(a_i))`.

La estructura encadenada es:

`a_i → c_j → φ₁,j → a_j → c_k → φ₁,k → ... → D`,

donde `D` es el resultado concreto respecto del cual se reconstruye la responsabilidad.

El grafo causal surge como representación externa de esas dependencias encadenadas. No es el fundamento ontológico de la relación; es su representación metrológica.

---

## 3. W: matriz de determinaciones locales, no matriz de responsabilidad por definición

Normalización de significado:

`W_ij = grado en que el nodo i determinó causalmente el colapso/acto del nodo j`.

En lenguaje operativo:

`W_ij = fracción del comportamiento de j determinada por i`,

siempre bajo la convención de arista:

`i → j`.

Por tanto:

`W`

representa **dependencias locales entre primeras mediaciones**.

No debe identificarse por definición con:

- responsabilidad total;
- atribución global respecto de un resultado;
- R*;
- el operador de responsabilidad.

La relación correcta es de precedencia:

`φ₁ → relaciones locales → W`.

---

## 4. Composición causal por rutas

Si existe una cadena:

`A → B → C`,

la influencia de `A` sobre `C` puede transmitirse por mediación de `B`.

Bajo una aproximación multiplicativa local, la contribución de la ruta es:

`w_AB · w_BC`.

Si existen múltiples rutas entre un nodo y el resultado, todas las rutas causalmente distintas relevantes deben ser consideradas sin contabilizar dos veces el mismo flujo causal.

La estructura general que el corpus intenta representar es:

`influencia total de i sobre D = contribuciones directas + contribuciones mediadas por rutas hacia D`.

Esta propiedad —composición/transitividad causal— sí se deriva del encadenamiento de primeras mediaciones.

No se deriva de ella, por sí sola, que el eigenvector de la matriz cruda `W` sea el operador correcto para calcular esa influencia total.

---

## 5. δ_ext: exteriorización atributiva de la segunda mediación

La distinción de Areópago normaliza dos operaciones:

`δ_int(t) = Ego(t) − I(t)`

como retorno interno del acto al sujeto, y:

`δ_ext(t) = atribución(φ₁(v_t,c_t), Sujeto)`

como atribución exterior del acto al nodo cuya cadena causal es reconstruible.

La relación debe leerse con precisión:

- `δ_int` requiere la operación interna de `φ₂`;
- `δ_ext` opera sobre el colapso producido por `φ₁` y una cadena causal reconstruible;
- ambas tienen una **estructura atributiva isomorfa**: retornar/asignar un acto a un sujeto;
- esa semejanza estructural no convierte a `δ_ext` en medición de la `φ₂` interna del sujeto.

Regla de normalización:

> **La imputación exterior tiene forma atributiva análoga a φ₂, pero su material causal es la cadena de φ₁.**

---

## 6. Corrección del crosswalk de Transformación formal

La formulación histórica que presenta `R*` como «lectura exterior de la distribución de φ₂» debe interpretarse y, en segunda edición, precisarse.

La formulación normalizada es:

`R* = distribución exterior de la atribución causal de los colapsos de φ₁ respecto de un resultado D`.

No:

`R* = medida de cuánto operó la φ₂ interna de cada ego`.

Ese segundo objeto pertenece a la genealogía de la asunción y de α.

La normalización preserva la intuición correcta de Transformación formal —la imputación como operación exterior de retorno atributivo— pero separa:

- **estructura de la operación:** análoga a `φ₂`;
- **objeto causal atribuido:** producido por `φ₁`.

---

## 7. R*(D): distribución global de atribución causal respecto de un resultado

Para un resultado concreto `D`, R* debe representar:

`R*_i(D) = participación total del nodo i en la producción causal de D`.

Con normalización:

`Σ_i R*_i(D) = 1`.

La suma unitaria expresa que el objeto distribuido es la totalidad de la participación causal considerada en el modelo para ese resultado.

`R*` no mide:

- intención;
- dolo;
- culpabilidad;
- arrepentimiento;
- reconocimiento subjetivo;
- asunción;
- sanción.

Mide posición causal relativa respecto de un resultado definido.

---

## 8. M_R(D): operador de responsabilidad como objeto intermedio

Para evitar identificar prematuramente `W` con responsabilidad global, esta normalización introduce un símbolo editorial provisional:

`M_R(D)`.

Definición conceptual:

`M_R(D) = operador que transforma la red local de determinaciones W en una atribución causal global respecto del resultado D`.

La decisión autoral vigente conserva a `R*` como **eigenvector de responsabilidad**. Por tanto, la forma objetivo de la formalización futura es:

`M_R(D) · R*(D) = λ_R · R*(D)`.

Esta expresión fija el **tipo de relación buscada**, no la construcción matemática ya validada de `M_R(D)`.

Todavía debe demostrarse:

- cómo se construye `M_R(D)` a partir de `W` y `D`;
- cómo compone rutas;
- cómo evita doble contabilización;
- cómo trata DAG, ciclos y componentes desconectados;
- qué condiciones garantizan existencia/unicidad del eigenvector relevante;
- qué orientación matricial corresponde a la convención causal;
- cómo se excluye o trata el nodo final;
- cómo reproduce los casos publicados.

Por ello:

`R* = eig(M_R(D))`

es la forma normalizada de la tesis autoral,

mientras:

`R* = eig(W)`

permanece como una identificación histórica que requiere revisión formal.

---

## 9. El nodo final D

El resultado o nodo final cumple una función distinta de los nodos causales.

`D`

es el **objeto respecto del cual** se distribuye causalidad.

No debe recibir automáticamente un componente de responsabilidad causal sólo por ser el sumidero del grafo.

Normalización conceptual:

`W` puede representar conexiones que terminan en `D`, pero `R*(D)` distribuye responsabilidad entre nodos causalmente pertinentes, no entre el resultado y sus causas como si fueran homogéneos.

La construcción matemática exacta de esta exclusión pertenece a la revisión formal pendiente.

---

## 10. Rama interna: φ₂ → α

La otra dirección de la fórmula del ego es:

`a_i → φ₂,i → I_i(t+1)`.

De esta rama deriva la genealogía de la asunción.

Normalización:

`α_i = grado de asunción efectiva de la posición causal del nodo i`.

Su genealogía ontológica procede de `φ₂`; su operacionalización aplicada puede registrar acciones, reparaciones y consecuencias efectivamente soportadas, incluidas modalidades voluntarias, forzadas o impuestas, conforme a `RES-ALPHA-001`.

Esta normalización no redefine α ni reabre su resolución.

---

## 11. R* y α como dos lecturas de la fórmula del ego

La arquitectura queda dividida en dos ramas:

### Rama causal/exterior

`v,c → φ₁ → acto → red causal → W → M_R(D) → R*(D)`.

### Rama de retorno/asunción

`acto → φ₂ → I(t+1) → α`.

Por tanto:

- `R*` cuantifica cuánto causalmente pertenece al nodo respecto del resultado;
- `α` cuantifica cuánto de esa posición fue efectivamente asumido/soportado en el dominio aplicado.

---

## 12. Δ como comparación entre ambas ramas

Con las resoluciones MANT ya adoptadas:

`Δ_i = R*_i − α_i`.

Su genealogía puede esquematizarse como:

`φ₁ → W → M_R(D) → R*`

frente a:

`φ₂ → α`.

Y finalmente:

`R* − α → Δ`.

Esta comparación no convierte causalidad en normatividad. Δ describe una brecha entre magnitudes del sistema.

---

## 13. Esquema maestro normalizado

```text
EGO INDIVIDUAL

v_i , c_i
   │
   ▼
 φ₁,i
   │
   ▼
 a_i ──────────────────────────────┐
   │                               │
   │ entra en el campo de j        │ retorno/asunción
   ▼                               ▼
 c_j                              φ₂,i
   │                               │
   ▼                               ▼
 φ₁,j                           I_i(t+1)
   │                               │
   ▼                               ▼
 a_j                              α_i
   │
   ▼
 ...
   │
   ▼
 D

RED EXTERIOR

φ₁ encadenadas
      │
      ▼
      W
      │
      ▼
   M_R(D)
      │
      ▼
    R*(D)
      │
      ├──────────────┐
      │              │
      │              ▼
      │             α_i
      │              │
      └───────┬──────┘
              ▼
        Δ_i = R*_i − α_i
```

Forma compacta:

`v,c → φ₁ → a → W → M_R(D) → R*`

`a → φ₂ → I(t+1) → α`

`R* − α = Δ`.

---

## 14. Qué aporta esta normalización

Queda fijado conceptualmente que:

1. `W` representa determinaciones locales entre primeras mediaciones.
2. `W` no es responsabilidad global por definición.
3. `δ_ext` atribuye exteriormente colapsos de `φ₁` y es estructuralmente análoga al retorno de `φ₂`.
4. `R*(D)` distribuye causalidad global respecto de un resultado.
5. `R*` se conserva autoralmente como eigenvector de responsabilidad.
6. El eigenvector debe pertenecer al operador de responsabilidad `M_R(D)`, cuya construcción aún debe demostrarse.
7. α pertenece a la rama de asunción/retorno y no debe confundirse con causalidad.
8. Δ compara ambas ramas mediante `R* − α`.

---

## 15. Qué NO queda resuelto

Esta normalización no adjudica todavía:

- `W` frente a `Wᵀ` como implementación final;
- fórmula concreta de `M_R(D)`;
- equivalencia entre método de rondas y formulaciones eigenvectoriales;
- normalización simple `w_i/Σw_j` del Apéndice C de Prometeo;
- doble contabilización de rutas;
- tratamiento formal de sumideros;
- irreducibilidad;
- primitividad/aperiodicidad;
- condiciones precisas de Perron–Frobenius;
- regularización de DAG nilpotentes;
- ciclos causales;
- reproducción de los vectores publicados;
- validación empírica de pesos o calibraciones.

Todos estos puntos permanecen como revisiones formales separadas.

---

## 16. Revisiones relacionadas que permanecen abiertas

Entre otras:

- `review.prometeo.rstar_algorithm_equivalence`;
- `review.prometeo.design_node_presumption`;
- `review.calc.rstar_equivalence`;
- `review.calc.orientation`;
- `review.calc.sinks`;
- `review.calc.published_vectors_reproduction`;
- `review.rstar.sink_irreducibility`;
- `review.tf.rstar_orientation`;
- `review.axiom.rstar_sink`;
- `review.mci.rstar_orientation`;
- `review.mcii.sink_normalization`;
- revisiones de periodicidad, conectividad y condiciones espectrales asociadas.

La normalización debe consultarse antes de intentar resolver esas revisiones, porque fija qué objetos deben distinguirse.

---

## 17. Criterio para la formalización futura

Cualquier propuesta matemática futura para `M_R(D)` deberá demostrar, como mínimo, que:

1. preserva la convención causal local de `W`;
2. compone influencia a través de rutas;
3. permite responsabilidad upstream en grafos acíclicos;
4. no requiere inventar causalidad inversa para obtener un espectro útil;
5. distingue nodos causales del resultado `D`;
6. evita doble contabilización;
7. produce una distribución normalizable;
8. ofrece condiciones explícitas de existencia y unicidad;
9. reproduce o explica las diferencias con los casos publicados;
10. mantiene la separación entre causalidad `R*`, asunción `α` y predicación normativa posterior.

Hasta que esas pruebas existan, `M_R(D)` es una **normalización conceptual y un objetivo de formalización**, no un teorema validado.

---

## 18. Proveniencia

La normalización se apoya en lectura transversal de:

- *Caos: El abismo del ego y la doble mediación*, cap. VI — fórmula del ego y doble mediación;
- *Afrodita Areia: Areópago*, apéndice II — `δ_int`, `δ_ext` e imputación exterior sobre `φ₁`;
- *La transformación formal*, cap. 2.1 — derivación histórica de R*, red de caminos y formulación eigenvectorial;
- *El cálculo de la responsabilidad* — R* como vector de distribución causal y formulación espectral;
- *El método Prometeo* — grafo, pesos, método de rondas, composición de caminos, casos calculados y normalización simplificada del Apéndice C.

La decisión de conservar `R*` como **eigenvector de responsabilidad** es una adjudicación autoral MANT posterior a esas primeras ediciones. Esta decisión no adjudica todavía el operador matemático exacto cuyo eigenvector debe ser `R*`.
