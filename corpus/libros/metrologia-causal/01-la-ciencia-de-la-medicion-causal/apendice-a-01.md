APÉNDICES · Demostraciones formales de propiedades

### Apéndice A·1

### Demostración del teorema de Perron-Frobenius para matrices no negativas

Existencia, unicidad y positividad del eigenvector principal — y

su aplicación a R*

### I.  Enunciado del teorema y notación

Sea A una matriz real n×n con entradas no negativas (A_ij ≥ 0 para todo i, j). Se dice que A es irreducible si el grafo dirigido G(A) — donde existe una arista de j a i si y solo si A_ij > 0 — es fuertemente conexo: para todo par (i, j) existe un camino dirigido de i a j en G(A). El teorema de Perron-Frobenius para matrices no negativas irreducibles establece:

Teorema de Perron-Frobenius (versión para matrices no negativas irreducibles)

(1) Existe un eigenvalor real positivo ρ(A) — el radio espectral — tal que |λ| ≤ ρ(A) para todo eigenvalor λ de A.

(2) ρ(A) es un eigenvalor simple (no repetido) de A. (3) El eigenvector v correspondiente a ρ(A) tiene todos sus componentes estrictamente positivos: v_i > 0 para todo i.

Metrología Causal

(4) Para cualquier otro eigenvalor λ ≠ ρ(A): |λ| < ρ(A) (dominancia estricta del radio espectral).

(5) El eigenvector v es único (salvo reescalado positivo): no existe ningún otro eigenvector con todos los componentes no negativos.

### II.  Demostración de la existencia y positividad del eigenvector

Paso 1 — Construcción del conjunto admisible

Definimos el conjunto S = {x ∈ ℝⁿ: x ≥ 0, ||x||₁ = 1}, el simplex estándar en ℝⁿ. Para cada x ∈ S definimos la función f: S → S por f(x) = Ax / ||Ax||₁. Esta función está bien definida porque A es no negativa e irreducible: para cualquier x ∈ S con x ≥ 0 y x ≠ 0, el vector Ax tiene al menos un componente positivo (por irreducibilidad), de modo que ||Ax||₁ > 0.

Por el teorema de punto fijo de Brouwer: S es un compacto convexo no vacío, f es continua (como cociente de funciones continuas con denominador positivo en S). Por tanto, existe al menos un punto fijo x* ∈ S tal que f(x*) = x*, es decir, Ax* = ρ x* donde ρ = ||Ax*||₁ > 0. Este x* es un eigenvector con eigenvalor positivo ρ y componentes no negativos.

Paso 2 — Positividad estricta del eigenvector

Supongamos que x* tiene algún componente cero: existe i₀ tal que x*_{i₀} = 0. Como Ax* = ρ x*, el componente i₀ satisface: Σⱼ A_{i₀j} x*_j = ρ x*_{i₀} = 0. Dado que A_{i₀j} ≥ 0 y x*_j

Metrología Causal

≥ 0, esto requiere A_{i₀j} x*_j = 0 para todo j. Para los j con A_{i₀j} > 0 (las aristas salientes del nodo i₀ en G(A)), se necesita x*_j = 0.

Aplicando este argumento iterativamente: el conjunto Z = {i: x*_i = 0} satisface que para todo i ∈ Z y todo j tal que A_ij > 0, se tiene j ∈ Z. Equivalentemente, no existe arista dirigida de ningún nodo de Z hacia ningún nodo fuera de Z en G(A). Esto contradice la irreducibilidad de A (que requiere que desde cualquier nodo exista un camino a cualquier otro nodo). Por tanto, Z debe ser vacío: x*_i > 0 para todo i.

Paso 3 — Unicidad del eigenvector positivo

Supongamos que existen dos eigenvectores con eigenvalor positivo y componentes positivos: u y v con Au = ρu y Av = ρv, u > 0, v > 0. Definimos t* = min {u_i / v_i: i = 1, ..., n}. Por positividad de u y v, t* > 0. El vector w = u − t*v satisface: w_i ≥ 0 para todo i (por definición de t*) y w_{i*} = 0 para algún i* donde el mínimo se alcanza. Dado que Aw = ρw y w ≥ 0, si w ≠ 0 el argumento del Paso 2 produciría contradicción. Por tanto, w = 0, es decir u = t*v. El eigenvector positivo es único salvo escala.

### III.  Aplicación al grafo causal de R*

La matriz de adyacencia ponderada W del grafo causal de Prometeo satisface las hipótesis del teorema bajo las condiciones de la Parte II (II·3): W_ij = w_ij ≥ 0 para todo (i,j), y el grafo es irreducible (existe camino dirigido entre cualquier par de nodos). Por tanto, el teorema garantiza que el eigenvector principal v* existe, es único (salvo reescalado), y tiene todos sus componentes estrictamente positivos.

Metrología Causal

El vector R* del sistema es precisamente este eigenvector principal normalizado para que la suma sea 1: R* = v* / ||v*||₁. La positividad estricta garantiza que R*_i > 0 para todo nodo i del grafo irreducible — ningún nodo causalmente conectado tiene responsabilidad cero. La unicidad garantiza que no existe otra distribución de responsabilidad con las mismas propiedades formales que produce el eigenvector.

La condición adicional de aperiodicidad (que el grafo no tenga ciclos de longitud fija) garantiza que ρ(W) es el único eigenvalor con valor absoluto ρ — es decir, no hay otros eigenvalores de módulo igual al radio espectral. Esta condición fortalece la Propiedad (4) del teorema a: para todo λ ≠ ρ(W), |λ| < ρ(W), sin excepciones sobre el círculo de radio ρ(W). Esta garantía adicional es la que asegura la convergencia del método de potencias al único eigenvector dominante (A·2).

Notas al apéndice A·1

1 La demostración presentada sigue la línea del argumento de punto fijo de Brouwer. La demostración original de Perron (1907) usó análisis real; la extensión de Frobenius (1912) a matrices no negativas usó argumentos de álgebra matricial. La versión con punto fijo de Brouwer es más moderna y más directa para las hipótesis que el sistema requiere. Una demostración alternativa usa la teoría de la dominancia espectral y la técnica de la matriz primitiva; ambas producen el mismo resultado.

2 El radio espectral ρ(A) de una matriz no negativa irreducible tiene la caracterización variacional: ρ(A) = max_{x>0} min_i (Ax)_i / x_i = min_{x>0} max_i (Ax)_i / x_i. Esta caracterización permite calcular cotas sobre ρ(A) desde los pesos del grafo sin calcular el eigenvector exacto, lo que es útil para estimar el orden de magnitud de R* antes del cálculo completo.

Metrología Causal

