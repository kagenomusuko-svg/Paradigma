# RES-RSTAR-001 — Resolución MANT vigente para R* y el operador de responsabilidad

> **RESOLUCIÓN VIGENTE POR ADJUDICACIÓN AUTORAL EXPLÍCITA.** Documento derivado de mantenimiento. No modifica retrospectivamente las fuentes canónicas de primera edición; fija la lectura y formalización vigentes para segunda edición y productos derivados.

- **ID:** `RES-RSTAR-001`
- **Estado:** **RESUELTA — ADJUDICACIÓN AUTORAL VIGENTE**
- **Normalización conceptual:** `NORM-RSTAR-EGO-001`
- **Auditoría formal:** `AUD-RSTAR-001`
- **Candidato adoptado:** `CAND-RSTAR-001`
- **Validación estructural:** `VAL-RSTAR-001`
- **Entrada editorial:** `2E-RSTAR-001`
- **Objeto:** `R*(D)`, `W`, `Q_D`, `b_D`, `M_R(D)`

---

## 1. Adjudicación nuclear

Se adopta como formalización vigente la siguiente jerarquía:

`causalidad local → composición total de rutas → normalización final → operador espectral de responsabilidad → convergencia estable R*`.

La tesis autoral vigente queda:

> **R* es el eigenvector de responsabilidad: la distribución estable a la que converge la atribución causal entre los nodos respecto de un resultado D.**

Por tanto:

`R*_i(D)`

representa la **proporción estable de convergencia causal** del nodo `i` respecto de `D`.

Si:

`R*(D) = (0.58, 0.27, 0.15)^T`,

la atribución causal estable converge a:

- nodo 1: `58%`;
- nodo 2: `27%`;
- nodo 3: `15%`.

Esto debe distinguirse de la **velocidad de convergencia**, que depende del resto del espectro del operador y no de los componentes de `R*`.

---

## 2. Genealogía desde la fórmula del ego

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

La genealogía normalizada queda:

`φ₁ encadenadas → W → Q_D,b_D → atribución total r_D → M_R(D) → R*(D)`

mientras:

`φ₂ → α`.

Y finalmente:

`R*−α → Δ`.

---

## 3. Tipado de W

Bajo la convención:

`W_ij = w(i→j)`,

`W` representa cuánto determinó localmente el nodo `i` el colapso o comportamiento del nodo `j`.

Es una matriz de **determinaciones causales locales de φ₁**.

`W` no es por definición:

- la matriz de responsabilidad;
- una matriz estocástica;
- una matriz irreducible;
- una matriz fuertemente conexa;
- el operador cuyo eigenvector deba ser R*.

Las propiedades espectrales pertenecen al operador de responsabilidad construido sobre la red causal, no a la matriz causal cruda.

---

## 4. Separación del resultado D

Sea:

`A_D={i : existe un camino i→...→D}`.

`D` es el resultado respecto del cual se distribuye causalidad y no un actor homogéneo a sus causas.

Sobre `A_D` se define:

`Q_D=[q_ij]`,

con:

`q_ij=w(i→j)`

para aristas primitivas entre nodos causales activos.

Se define además:

`b_D=(b_i)`,

con:

`b_i=w(i→D)`

para mecanismos directos primitivos hacia `D`.

El sumidero deja así de tener que pertenecer a la misma matriz a la que se exige irreducibilidad.

---

## 5. Regla de arista primitiva

Debe distinguirse:

- **arista primitiva:** mecanismo causal local documentado;
- **arista acumulada:** resumen de una o varias rutas ya representadas.

Una arista acumulada no puede entrar simultáneamente al cálculo junto con las rutas primitivas que resume.

Si existe además un mecanismo directo independiente entre dos nodos, puede coexistir con las rutas mediadas, pero debe documentarse como mecanismo causal distinto.

Esta regla evita la doble contabilización observada en algunos desarrollos históricos de Prometeo.

---

## 6. Núcleo computacional vigente

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

La serie tiene una lectura causal directa:

- `b_D`: contribución directa;
- `Q_D b_D`: contribución por rutas con un intermediario;
- `Q_D² b_D`: contribución por rutas con dos intermediarios;
- etc.

Cada ruta se compone multiplicando los pesos de sus aristas. Las rutas se agregan antes de normalizar.

---

## 7. Normalización final única

Defínase:

`Z_D=1^T r_D`.

Entonces:

`R*(D)=r_D/Z_D`.

Por construcción:

`Σ_i R*_i(D)=1`.

La normalización ocurre **una sola vez y al final** de la reconstrucción causal.

No se normalizan rondas intermedias para luego tratarlas como si conservaran la magnitud causal previa.

Prometeo Caso 2 demuestra que la suma de rutas seguida de una única normalización reproduce exactamente los porcentajes publicados `68.7/19.9/11.4`; Prometeo Caso 3 muestra que la renormalización intermedia cambia el objeto calculado.

---

## 8. Operador espectral de responsabilidad

Defínase:

`η_D=1/Z_D`.

Y:

`M_R(D)=Q_D+η_D b_D 1^T`.

Entonces:

`M_R(D)R*(D)=R*(D)`.

El eigenvalor asociado a `R*` es:

`λ_1=1`.

Bajo:

- `Q_D≥0`;
- `b_D≥0`;
- todo nodo de `A_D` tiene un camino positivo hacia `D`;
- `ρ(Q_D)<1`;

se obtiene `R*>0` sobre los ancestros causales y el operador es no negativo, irreducible y aperiódico en el espacio causal relevante.

Perron–Frobenius se aplica a `M_R(D)`, no a `W`.

---

## 9. Significado metrológico de la iteración

La iteración:

`x^(t+1)=M_R(D)x^(t)`

no se entiende como un adorno posterior ni como una mera representación algebraica sin contenido.

Se interpreta como una **ronda de propagación/atribución causal** en el espacio de responsabilidad.

Bajo las condiciones espectrales declaradas:

`x^(t) → R*(D)`

tras la normalización que corresponda al algoritmo de implementación.

La convergencia significa que llega un punto en el que una nueva ronda de propagación no altera las proporciones relativas de atribución:

`M_R(D)R*(D)=R*(D)`.

Así:

`R*_i(D)`

es el porcentaje estable al que converge el nodo `i` dentro de la distribución total de responsabilidad.

---

## 10. Porcentaje de convergencia y velocidad de convergencia

Deben mantenerse separados dos objetos.

### Proporción estable

`R*_i(D)` responde:

> ¿a qué proporción de atribución causal converge el nodo `i` respecto de `D`?

### Velocidad de convergencia

La rapidez con que una iteración inicial se aproxima a `R*` depende del espectro secundario.

Con `λ_1=1`, la cantidad relevante es, según el caso, el segundo eigenvalor en módulo:

`|λ_2|`,

o la brecha espectral:

`γ=1−|λ_2|`.

Una brecha mayor implica convergencia más rápida; una brecha menor implica persistencia mayor de la distribución inicial.

La velocidad de convergencia no debe confundirse con los porcentajes de responsabilidad.

---

## 11. Estatuto conceptual de la spectralización

La prioridad lógica y metrológica es:

`causalidad local → composición de rutas → atribución total → operador de propagación → distribución estable`.

No:

`eigenvector de una matriz elegida → redefinición retrospectiva de la causalidad para que encaje`.

El operador espectral tiene contenido metrológico porque su dinámica expresa la propagación de la atribución hasta la estabilidad.

Pero la propiedad espectral no constituye una prueba independiente de que los pesos `w` sean empíricamente correctos. La validez causal de las entradas debe establecerse antes mediante evidencia y calibración del dominio.

---

## 12. DAG

Si `Q_D` es acíclica:

`Q_D^m=0`

para algún `m`.

Entonces:

`ρ(Q_D)=0`

y:

`r_D=(I+Q_D+Q_D²+...+Q_D^m)b_D`.

La atribución total existe sin añadir ciclos ficticios, autolazos causales o teleportación.

La spectralización se produce después sobre `M_R(D)`, que sí puede tener a `R*` como Perron-eigenvector estable.

---

## 13. Ciclos reales

Para feedback causal real se adopta como condición básica de este operador:

`ρ(Q_D)<1`.

Si se cumple, la suma de recorridos converge.

Si no se cumple, RES-RSTAR-001 no fuerza una salida numérica. El caso deberá:

- desplegarse temporalmente;
- descomponerse en eventos;
- o recibir un modelo específico de feedback.

No se introduce amortiguación arbitraria sólo para salvar la convergencia.

---

## 14. W frente a Wᵀ

Bajo:

`Q_ij=w(i→j)`,

la atribución se escribe:

`r_i=b_i+Σ_j Q_ij r_j`.

Por tanto:

`r=b+Qr`.

No se requiere cambiar la semántica de las aristas mediante transposición.

La reconstrucción exterior recorre hacia atrás la pertenencia causal, pero conserva la dirección ontológica de la relación `i→j`.

La antigua disputa `W` frente a `Wᵀ` era consecuencia de intentar usar la matriz causal local como operador global de responsabilidad.

---

## 15. Algoritmos históricos

### Eigenvector de W o Wᵀ

Se conserva como formulación histórica de primera edición, pero no como algoritmo vigente de R*.

### Método de rondas de Prometeo

Se conserva como desarrollo histórico y pedagógico.

Sus productos de rutas son recuperables dentro del operador vigente; sus normalizaciones intermedias no se conservan como regla de cálculo.

### `w/Σw`

Se conserva como caso especial cuando:

`Q_D=0`.

En un grafo estrella sin mediaciones:

`R*=b_D/(1^T b_D)`.

No es una regla universal.

---

## 16. Revisiones adjudicadas

### `review.prometeo.rstar_algorithm_equivalence`

**RESUELTA — NO equivalencia.**

Rondas, normalización simple y eigenvector de `W` son algoritmos distintos.

### `review.prometeo.design_node_presumption`

**RESUELTA — NO universalidad.**

El propio Prometeo presenta una contraprueba donde el ejecutor obtiene el mayor `R*`. El nodo de diseño puede dominar en determinados campos, pero no por definición.

### `review.calc.published_vectors_reproduction`

**RESUELTA respecto de reproducibilidad declarada.**

La matriz y el algoritmo impresos no producen los vectores publicados. La procedencia histórica exacta de esos porcentajes permanece como nota de auditoría y los casos deben recalcularse en segunda edición.

### Orientación, sumidero y Perron aplicados a W cruda

Quedan resueltas por nuevo tipado las familias:

- `review.calc.orientation`;
- `review.calc.sinks`;
- `review.rstar.sink_irreducibility`;
- `review.tf.rstar_orientation`;
- `review.axiom.rstar_sink`;
- `review.mci.rstar_orientation`;
- `review.mcii.sink_normalization`.

El problema histórico era identificar `W` con el operador espectral de responsabilidad.

Las relaciones y revisiones históricas permanecen visibles como proveniencia de primera edición.

---

## 17. Qué NO resuelve RES-RSTAR-001

Permanecen abiertas:

- `review.calc.rstar_equivalence` en cuanto a relación entre necesidad contrafáctica, pesos escalares y fracción de daño;
- calibración empírica de `w`;
- validación externa de rangos;
- interacción no aditiva entre rutas;
- rutas solapadas;
- condiciones conjuntas e hiperaristas;
- causalidad acumulativa;
- Shapley;
- ciclos con `ρ(Q_D)≥1`;
- temporalización de feedback;
- reglas de reasignación de nodos instrumentales a diseñadores;
- validación científica, jurídica o empírica universal del modelo.

La resolución es formal, ontológico-metrológica y de tipado. No convierte la formalización en validación empírica.

---

## 18. Consecuencias editoriales obligatorias

La segunda edición deberá:

1. corregir *Transformación formal* donde identifica `R*` con distribución de `φ₂` y con `eig(W)`;
2. corregir *Axiomatización* en la tensión `W/Wᵀ`, sumidero, estocasticidad e irreducibilidad;
3. corregir *Metrología Causal* donde la iteración de potencia sobre `W` se presenta como solución de DAG;
4. corregir *El cálculo de la responsabilidad* en teoremas, código y ejemplos dependientes de `eig(W)`;
5. recalcular los vectores publicados no reproducibles;
6. corregir Prometeo para usar composición de rutas y normalización final única;
7. conservar `w/Σw` sólo para grafos sin mediación activa;
8. separar aristas primitivas de aristas acumuladas;
9. documentar el dominio `ρ(Q_D)<1`;
10. incorporar la distinción entre porcentaje estable `R*_i` y velocidad de convergencia;
11. preservar el historial de primera edición en la auditoría.

---

## 19. Pruebas que sustentan la resolución

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
- *El cálculo*, Caso Eje: la `W` impresa es nilpotente y el algoritmo declarado no reproduce el vector histórico.

---

## 20. Fórmula vigente de R*

`Q_D` = matriz de determinaciones causales locales primitivas entre ancestros de `D`.

`b_D` = vector de determinaciones primitivas directas sobre `D`.

Para:

`ρ(Q_D)<1`,

se define:

`r_D=(I−Q_D)^−1b_D`.

Luego:

`R*(D)=r_D/[1^T r_D]`.

Defínase:

`η_D=[1^T(I−Q_D)^−1b_D]^−1`.

Entonces:

`M_R(D)=Q_D+η_D b_D1^T`.

Y:

`M_R(D)R*(D)=R*(D)`.

Por tanto:

> **R* es el Perron-eigenvector normalizado del operador de responsabilidad inducido por la reconstrucción total de las cadenas de φ₁ que terminan en D, y sus componentes son las proporciones estables de convergencia causal de los nodos respecto de ese resultado.**

---

## 21. Regla de lectura histórica

Las formulaciones de primera edición:

- `R*=eig(W)`;
- `R*=eig(W^T)`;
- rondas con normalizaciones intermedias;
- `R*=w/Σw` como regla universal;

se conservan como formulaciones históricas y no se reescriben retrospectivamente en las fuentes canónicas.

Cuando un producto derivado, respuesta o segunda edición necesite la formulación vigente deberá consultar `RES-RSTAR-001` antes de presentar esas variantes como alternativas equivalentes.

Donde documentos derivados anteriores a esta adjudicación digan que `M_R(D)` es sólo provisional o que su construcción sigue abierta, **RES-RSTAR-001 supersede ese estado provisional**.
