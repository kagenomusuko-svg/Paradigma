PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·2

### Teorema de la Responsabilidad Causal

### Proporcional

Existencia, unicidad y demostración

### I.  El enunciado del teorema

Teorema de la Responsabilidad Causal Proporcional

Sea G = (N, E, W) un grafo causal dirigido con matriz de adyacencia ponderada W ≥ 0 e irreducible sobre N□{Nf}, donde Nf es el nodo sumidero que representa el resultado D.

Existe una única distribución R*: N → [0,1] con Σᵢ R*(i) = 1 que satisface simultáneamente los axiomas A1, A2, A3 y A4.

Esa distribución es el eigenvector principal normalizado de W: el único vector positivo v tal que W·v = λ_max·v, normalizado para que ||v||□ = 1.

### II.  Lema previo: el Teorema de Perron-Frobenius

Metrología Causal · Vol. II

La demostración del teorema descansa sobre el Teorema de Perron-Frobenius para matrices no negativas e irreducibles. El lema que este capítulo usa en su forma operativa es el siguiente.

Lema PF (Perron-Frobenius, forma operativa)

Sea W una matriz cuadrada n×n con entradas no negativas (W ≥ 0) e irreducible. Entonces:

(i) W tiene un eigenvalor real positivo λ_max > 0, estrictamente mayor que el módulo de cualquier otro eigenvalor: λ_max > |λᵢ| para todo i ≠ max.

(ii) El eigenvector correspondiente a λ_max es único (salvo escala) y tiene todas sus entradas estrictamente positivas: v_i > 0 para todo i.

(iii) El método de potencias converge a v desde cualquier vector inicial positivo: W^k·u / ||W^k·u||₁ → v cuando k → ∞.

La irreducibilidad de W es la condición que garantiza las tres propiedades del lema. Un grafo es irreducible si y solo si su matriz de adyacencia es irreducible — es decir, si desde cualquier nodo existe un camino dirigido al nodo sumidero Nf. Esta es exactamente la condición de completitud del grafo verificada en el Paso 2 del protocolo.

### III.  Demostración: el eigenvector satisface los cuatro axiomas

La primera parte muestra que la distribución eigenvectorial satisface A1, A2, A3 y A4.

A1 — Eficiencia: el eigenvector v está normalizado por construcción: ||v||□ = Σᵢ v_i = 1. La normalización en la norma ℓ¹ asegura exactamente que la suma de todas las entradas es uno.

Metrología Causal · Vol. II

R*(i) = v_i / ||v||□ satisface A1 por definición del procedimiento de normalización.

A2 — Causalidad necesaria: por el lema PF(ii), todas las entradas del eigenvector son estrictamente positivas: v_i > 0 para todo i. Esto significa que todo nodo del grafo tiene R* > 0. La dirección '→' (si R* > 0 entonces condición necesaria) se garantiza porque el grafo por construcción contiene solo nodos causalmente relevantes para D. La dirección '←' (si es condición necesaria entonces R* > 0) se satisface por PF(ii).

A3 — Centralidad recursiva: la ecuación eigenvectorial W·v = λ_max·v dice exactamente que v_i = (1/λ_max) · Σ□ w_ij · v_j. Es decir: el valor de v_i es proporcional a la suma ponderada de los valores v_j de los nodos sobre los que i ejerce influencia. Esto es exactamente A3. La ecuación eigenvectorial es la forma matricial de A3.

A4 — Monotonicidad: si el peso w_ji aumenta, la entrada (W)_ji de la matriz W aumenta. Por el teorema de Perron para matrices con entradas no negativas, el eigenvalor principal λ_max es una función creciente de cada entrada de W. Y la entrada v_i del eigenvector principal es proporcional a la suma de los pesos de las aristas que entran a i, ponderados por los valores eigenvectoriales de sus fuentes — por lo tanto, v_i no puede decrecer cuando w_ji aumenta.

### IV.  Demostración: unicidad por relajación de axiomas

La segunda parte demuestra que relajar cualquier axioma permite distribuciones distintas del eigenvector que satisfacen los tres axiomas restantes.

Si se relaja A1: la distribución v' = 2·v satisface A2, A3 y A4 pero tiene Σ v'_i = 2 ≠ 1. Cualquier múltiplo escalar positivo del

Metrología Causal · Vol. II

eigenvector satisface A2–A4, pero no A1. La normalización ℓ¹ selecciona el único representante que satisface A1.

Si se relaja A2: la distribución que asigna R* = 0 al nodo de mayor eigenvector y distribuye su peso uniformemente entre los demás satisface A1, A3 (modificada) y A4, pero viola A2 porque un nodo causalmente necesario tiene R* = 0.

Si se relaja A3: cualquier distribución proporcional al grado de salida (número de aristas salientes de cada nodo, sin ponderación recursiva) satisface A1, A2 y A4, pero viola A3 porque ignora la propagación recursiva de la influencia.

Si se relaja A4: la distribución que invierte el ranking del eigenvector satisface A1 y A2, pero viola A4 porque los nodos con mayor influencia recibida tienen menor responsabilidad. Los cuatro casos muestran que cada axioma excluye una familia de distribuciones distintas del eigenvector. Juntos, los cuatro no dejan lugar para ninguna otra distribución.

La demostración por unicidad desde la relajación de axiomas no solo prueba que el eigenvector es la respuesta correcta: muestra con precisión por qué cada axioma es necesario. Un sistema que propone una distribución de responsabilidad distinta del eigenvector está, explícitamente, violando al menos uno de los cuatro axiomas. Identificar cuál axioma viola una distribución alternativa permite al mediador articular exactamente en qué sentido esa alternativa es metodológicamente inadecuada.

Función de la demostración por unicidad en el contexto adversarial

### V.  La condición de irreducibilidad: qué pasa si no se cumple

El teorema requiere que W sea irreducible. Si el grafo tiene nodos desde los que no existe camino al sumidero, W es reducible

Metrología Causal · Vol. II

y el eigenvector principal puede no ser único o puede no tener todas sus entradas positivas.

El protocolo maneja esta situación en el Paso 2 del análisis: cualquier nodo sin camino al sumidero se elimina del grafo antes del cálculo. Con esa eliminación, la submatriz resultante es irreducible y el teorema aplica. Los nodos eliminados tienen R* = 0 por A2 — no son condición necesaria de D.

Producto de salida · Capítulo IV·2

Demostración completa del Teorema de la Responsabilidad Causal Proporcional: el eigenvector principal normalizado de W es la única distribución que satisface A1–A4 simultáneamente. La demostración tiene dos partes: satisfacción directa de los cuatro axiomas (por verificación con el lema PF) y unicidad (por demostración desde relajación de axiomas).

Notas al Capítulo IV·2

1  La demostración de A2 presenta una sutileza técnica: el lema PF garantiza que todas las entradas del eigenvector son positivas cuando la matriz es irreducible. Pero la condición A2 exige que las entradas sean positivas exactamente para los nodos sine qua non, y cero para los que no lo son. La reconciliación es que el protocolo elimina del grafo los nodos no-sine-qua-non antes del cálculo. Con esa eliminación, todos los nodos presentes son sine qua non y el eigenvector les asigna entradas positivas.

Metrología Causal · Vol. II

