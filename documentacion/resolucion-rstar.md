# RES-RSTAR-001 — Propuesta de resolución MANT para R* y el operador de responsabilidad

> **PROPUESTA DE ADJUDICACIÓN, NO RESOLUCIÓN VIGENTE.** Este documento deriva del mantenimiento del corpus y no modifica las fuentes canónicas. Sólo puede pasar a estado **RESUELTA** mediante adjudicación autoral explícita.

- **ID:** `RES-RSTAR-001`
- **Estado:** **PROPUESTA PREPARADA / NO VIGENTE**
- **Normalización conceptual:** `NORM-RSTAR-EGO-001`
- **Auditoría formal:** `AUD-RSTAR-001`
- **Candidato:** `CAND-RSTAR-001`
- **Validación estructural:** `VAL-RSTAR-001`
- **Entrada editorial:** `2E-RSTAR-001`
- **Objeto:** `R*(D)`, `W`, `Q_D`, `b_D`, `M_R(D)`

---

## 1. Problema que la resolución pretende adjudicar

El corpus conserva una tesis doctrinal estable:

`R*` distribuye la participación causal de un resultado entre los nodos que fueron condiciones de su producción.

También conserva una decisión autoral vigente:

`R*` es el **eigenvector de responsabilidad**.

Sin embargo, las formalizaciones históricas identificaron ese eigenvector con la matriz causal local `W` o `W^T`, mientras los casos publicados usan principalmente DAG con nodo final sumidero.

En un DAG, `W` y `W^T` son nilpotentes y no poseen el eigenvector dominante positivo requerido por las obras.

Prometeo, además, utiliza bajo el mismo símbolo:

- rondas;
- productos de rutas;
- aristas acumuladas;
- normalización simple `w/Σw`.

Estas operaciones no son equivalentes.

La resolución busca preservar el objeto doctrinal y la genealogía de la fórmula del ego sin conservar como identidad matemática una formulación que no reproduce los casos.

---

## 2. Genealogía que se propone conservar

Fórmula individual:

`Ego_i(t)=φ₂,i(φ₁,i(v_i,c_i),I_i(t))`.

Producción causal:

`φ₁_i → acto_i → condiciones_j → φ₁_j → ... → D`.

Atribución exterior:

`D → δ_ext → ancestros causales`.

Asunción:

`acto_i → φ₂_i → α_i`.

Comparación:

`Δ_i=R*_i−α_i`.

La relación normalizada queda:

`φ₁ encadenadas → W → atribución total → R*`

mientras:

`φ₂ → α`.

---

## 3. Tipado propuesto de W

`W` no es por definición la matriz de responsabilidad.

Bajo la convención:

`W_ij=w(i→j)`,

representa cuánto determinó localmente el nodo `i` el colapso o comportamiento del nodo `j`.

Es una representación de determinaciones locales de `φ₁`.

No se exige a `W`:

- irreducibilidad;
- fuerte conexidad;
- estocasticidad;
- existencia de un eigenvector dominante positivo.

Esas propiedades, si son necesarias, pertenecen al operador de responsabilidad y no al grafo causal crudo.

---

## 4. Separación del resultado D

Sea:

`A_D={i : existe un camino i→...→D}`.

`D` es el resultado respecto del cual se distribuye causalidad y no un actor homogéneo a sus causas.

Sobre `A_D` se define:

`Q_D=[q_ij]`,

con:

`q_ij=w(i→j)`

para aristas primitivas entre nodos activos.

Se define además:

`b_D=(b_i)`,

con:

`b_i=w(i→D)`

para mecanismos directos primitivos hacia `D`.

Esto elimina la contradicción entre un nodo final de fila nula y la exigencia de que la misma matriz sea irreducible.

---

## 5. Regla de arista primitiva

La entrada del cálculo debe distinguir:

- **arista primitiva:** mecanismo causal local documentado;
- **arista acumulada:** resumen de una o varias rutas ya construidas.

Una arista acumulada no puede introducirse simultáneamente como entrada junto con las rutas que resume.

Si existe un mecanismo directo adicional e independiente, puede coexistir con rutas mediadas, pero debe estar documentado como mecanismo distinto.

---

## 6. Núcleo computacional propuesto

Para cada nodo:

`r_i(D)=b_i+Σ_j q_ij r_j(D)`.

En forma vectorial:

`r_D=b_D+Q_D r_D`.

Si:

`ρ(Q_D)<1`,

entonces:

`r_D=(I−Q_D)^−1 b_D`.

Equivalentemente:

`r_D=Σ_{k=0}^∞ Q_D^k b_D`.

La serie expresa:

- influencia directa;
- rutas con un intermediario;
- rutas con dos intermediarios;
- etc.

Cada ruta se compone multiplicando los pesos de sus aristas; las rutas representadas se agregan antes de normalizar.

---

## 7. Regla de normalización propuesta

Defínase:

`Z_D=1^T r_D`.

Entonces:

`R*(D)=r_D/Z_D`.

La normalización ocurre **una sola vez y al final** de la reconstrucción causal.

No deben normalizarse rondas intermedias y utilizar después esos porcentajes como si conservaran la magnitud causal previa.

Prometeo Caso 2 muestra que la suma de rutas seguida de una única normalización reproduce exactamente los porcentajes publicados; Prometeo Caso 3 muestra que la renormalización intermedia cambia el resultado.

---

## 8. Operador espectral inducido propuesto

Para conservar literalmente que `R*` es eigenvector de responsabilidad, se propone:

`η_D=1/Z_D`.

`M_R(D)=Q_D+η_D b_D 1^T`.

Entonces:

`M_R(D)R*(D)=R*(D)`.

Por tanto, `R*` es eigenvector de `M_R(D)` con eigenvalor `1`.

Bajo:

- `Q_D≥0`;
- `b_D≥0`;
- todo nodo de `A_D` tiene un camino positivo hacia `D`;
- `ρ(Q_D)<1`;

`R*>0` sobre los ancestros causales y el operador inducido es no negativo, irreducible y aperiódico en el espacio causal relevante.

Perron–Frobenius se aplica entonces a `M_R(D)`, no a `W`.

---

## 9. Estatuto conceptual de la spectralización

La resolución propone que la prioridad lógica sea:

`causalidad local → composición de rutas → atribución total → normalización → representación espectral`.

No:

`eigenvector de una matriz elegida → redefinición del objeto causal para que el resultado encaje`.

La spectralización es una propiedad del operador de responsabilidad inducido por la atribución total.

Esto preserva la afirmación autoral `R* = eigenvector de responsabilidad` sin convertir a `W` en algo que ontológicamente no es.

---

## 10. DAG

Si `Q_D` es acíclica:

`Q_D^m=0`

para algún `m`.

Entonces:

`ρ(Q_D)=0`

y:

`r_D=(I+Q_D+Q_D²+...+Q_D^m)b_D`.

El cálculo existe sin añadir ciclos ficticios, autolazos causales o teleportación.

---

## 11. Ciclos

Para feedback real se propone como condición básica:

`ρ(Q_D)<1`.

Si se cumple, la suma de recorridos converge.

Si no se cumple, esta resolución no fuerza una salida numérica. El caso deberá:

- desplegarse temporalmente;
- descomponerse en eventos;
- o recibir un modelo específico de feedback.

No se introduce amortiguación arbitraria para salvar la convergencia.

---

## 12. Qué ocurre con W frente a Wᵀ

Bajo:

`Q_ij=w(i→j)`,

la atribución exterior se escribe:

`r_i=b_i+Σ_j Q_ij r_j`.

Por tanto:

`r=b+Qr`.

No se requiere cambiar la semántica de las aristas mediante una transposición.

La reconstrucción lee hacia atrás la pertenencia causal, pero conserva la dirección ontológica `i→j`.

---

## 13. Algoritmos históricos

### Eigenvector de W o Wᵀ

Se conserva como formulación histórica, pero no como algoritmo vigente si esta resolución se adopta.

### Método de rondas de Prometeo

Se conserva como desarrollo histórico y pedagógico. Sus productos de rutas son recuperables dentro del nuevo operador; sus renormalizaciones intermedias no se conservan como regla de cálculo.

### `w/Σw`

Se conserva como caso especial cuando:

`Q_D=0`.

En un grafo estrella sin mediaciones:

`R*=b_D/(1^T b_D)`.

No se conserva como regla universal.

---

## 14. Adjudicaciones que acompañarían la adopción

### `review.prometeo.rstar_algorithm_equivalence`

**RESUELTA — NO equivalencia.**

Rondas, normalización simple y eigenvector de `W` son algoritmos distintos.

### `review.prometeo.design_node_presumption`

**RESUELTA — NO universalidad.**

La propia obra presenta una contraprueba donde el ejecutor obtiene el mayor `R*`. El nodo de diseño puede dominar frecuentemente, pero no por definición.

### `review.calc.published_vectors_reproduction`

**RESUELTA respecto de reproducibilidad declarada.**

La matriz/algoritmo impresos no producen los vectores publicados. La procedencia histórica exacta de esos porcentajes queda como nota de auditoría, y la segunda edición debe recalcularlos.

### Orientación, sumidero y Perron históricos

Si esta resolución se adopta, las revisiones:

- `review.calc.orientation`;
- `review.calc.sinks`;
- `review.rstar.sink_irreducibility`;
- `review.tf.rstar_orientation`;
- `review.axiom.rstar_sink`;
- `review.mci.rstar_orientation`;
- `review.mcii.sink_normalization`;

se resolverán mediante el nuevo tipado: eran problemas de identificar `W` con el operador de responsabilidad.

---

## 15. Qué NO resolvería RES-RSTAR-001

Incluso si se adopta, permanecerán abiertos:

- `review.calc.rstar_equivalence` en cuanto a equivalencia entre necesidad contrafáctica, pesos escalares y fracción de daño;
- calibración empírica de `w`;
- validación externa de rangos;
- interacción no aditiva entre rutas;
- rutas solapadas;
- condiciones conjuntas/hiperaristas;
- causalidad acumulativa;
- Shapley;
- ciclos con `ρ(Q_D)≥1`;
- temporalización de feedback;
- reglas de reasignación de nodos instrumentales a diseñadores;
- validación científica o jurídica del modelo.

La resolución es formal y de tipado; no es una validación empírica universal.

---

## 16. Consecuencias editoriales si se adopta

La segunda edición deberá:

1. corregir *Transformación formal* donde identifica `R*` con distribución de `φ₂` y con `eig(W)`;
2. corregir *Axiomatización* en la tensión `W/Wᵀ`, sumidero, estocasticidad e irreducibilidad;
3. corregir *Metrología Causal* donde la iteración de potencia sobre `W` se presenta como solución de DAG;
4. corregir *El cálculo de la responsabilidad* en teoremas, código y ejemplos dependientes de `eig(W)`;
5. recalcular todos los vectores publicados que no sean reproducibles;
6. corregir Prometeo para usar suma de rutas con una sola normalización final;
7. conservar `w/Σw` sólo para grafos sin mediación activa;
8. separar aristas primitivas de aristas acumuladas;
9. documentar el dominio `ρ(Q_D)<1`;
10. preservar el historial de primera edición en la auditoría.

---

## 17. Pruebas que sustentan la propuesta

### Sintéticas

- DAG simple: superada;
- ruta directa + mediada: superada;
- rutas paralelas: superada;
- nodo desconectado: superada;
- feedback atenuado: superada;
- feedback con `ρ(Q)>1`: correctamente rechazado como fuera de dominio.

### Corpus

- Prometeo Caso 2: reproducción exacta de `68.7/19.9/11.4`;
- Prometeo Caso 3: divergencia explicada por renormalización intermedia;
- Prometeo banco agregado: divergencia explicada por mezcla de rondas y arista acumulada;
- Prometeo banco descompuesto: divergencia estructural de las rondas;
- El cálculo Caso Eje: la `W` impresa es nilpotente y el algoritmo declarado no reproduce el vector histórico.

---

## 18. Fórmula de resolución propuesta

Si el autor adjudica favorablemente `RES-RSTAR-001`, la formulación vigente será:

`Q_D = matriz de determinaciones causales locales primitivas entre ancestros de D`.

`b_D = vector de determinaciones primitivas directas sobre D`.

`r_D=(I−Q_D)^−1b_D`, para `ρ(Q_D)<1`.

`R*(D)=r_D/[1^T r_D]`.

`η_D=[1^T(I−Q_D)^−1b_D]^−1`.

`M_R(D)=Q_D+η_D b_D1^T`.

`M_R(D)R*(D)=R*(D)`.

Así:

> **R* es el Perron-eigenvector normalizado del operador de responsabilidad inducido por la reconstrucción total de las cadenas de φ₁ que terminan en D.**

---

## 19. Regla de no-adjudicación automática

Hasta que exista decisión autoral explícita:

- `CAND-RSTAR-001` sigue siendo candidato;
- este documento sigue en estado PROPUESTA;
- no se corrigen fuentes canónicas;
- no se declara que el corpus histórico siempre haya usado esta fórmula;
- no se cierran por oficio las revisiones dependientes.

La consistencia matemática de la propuesta no sustituye la decisión autoral sobre si esta spectralización representa exactamente el objeto que el sistema pretende llamar `R*`.
