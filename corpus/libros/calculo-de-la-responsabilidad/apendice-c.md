### APÉNDICE C Fundamentos matemáticos

### y demostraciones

Banach · Perron-Frobenius · Itô · Shapley · Contrafáctico

histórico

Este apéndice contiene las demostraciones de los resultados matemáticos que sustentan el sistema de imputación causal. Cada sección puede leerse de manera independiente. El lector sin formación matemática formal puede saltarse este apéndice sin perder el argumento del libro: todos los resultados se enuncian en lenguaje natural en los capítulos correspondientes.

### A.1 El Teorema de Banach y la convergencia de R*

El vector R* es la distribución estacionaria del operador de responsabilidad M_R(D) inducido por la reconstrucción causal completa de las cadenas φ₁ que terminan en D. El Teorema del Punto Fijo de Banach garantiza la unicidad de esa distribución cuando el operador es una contracción en el espacio de distribuciones de probabilidad.

El Cálculo de la Responsabilidad · Apéndices

Teorema A.1 (Banach — Punto Fijo):  Sea (X, d) un espacio métrico completo y f: X → X una contracción, es decir, ∃ c ∈ [0,1) tal que d(f(x), f(y)) ≤ c·d (x, y) para todo x, y ∈ X. Entonces f tiene un único punto fijo x* ∈ X tal que f(x*) = x*.

Construcción del operador y aplicación al cálculo de R*:

Sea A_D = {i : existe un camino i→⋯→D} el conjunto de ancestros causales de D. Se define Q_D como la submatriz de determinaciones causales primitivas entre nodos de A_D, y b_D el vector de determinaciones primitivas directas sobre D (b_i = w(i→D)). Para ρ(Q_D) < 1:

r_D = (I − Q_D)⁻¹ b_D = Σ_{k≥0} Q_D^k b_D

Cada potencia Q_D^k b_D agrega la contribución de rutas con k intermediarios. Definiendo Z_D = 1ᵀ r_D y η_D = 1/Z_D, el operador de responsabilidad es:

M_R(D) = Q_D + η_D b_D 1ᵀ

y el vector de responsabilidad queda R*(D) = r_D / Z_D = η_D r_D, que satisface M_R(D) R*(D) = R*(D).

Sea X = {v ∈ ℝ^|A_D|: vᵢ ≥ 0, Σvᵢ = 1} con la métrica de variación total d(v,w) = Σᵢ|vᵢ − wᵢ|/2. El operador de iteración T(v) = M_R(D) v / ‖M_R(D) v‖₁ es una contracción sobre X cuando M_R(D) es primitiva sobre A_D.

El Cálculo de la Responsabilidad · Apéndices

Para los grafos causales del libro, que son DAGs (grafos acíclicos dirigidos), Q_D es nilpotente: Q_D^m = 0 para algún m ≤ |A_D|. La serie converge en un número finito de términos, el coeficiente de ergodicidad δ(M_R(D)) > 0, y por el Teorema de Banach la solución R*(D) es única e independiente del vector inicial.

Corolario:  Cuando M_R(D) es primitiva sobre A_D, la iteración T^k(v₀) converge al único R* en a lo más log(ε/2)/log(c) pasos para precisión ε, donde c = 1 − δ(M_R(D)) < 1.

### A.2 El Teorema de Perron-Frobenius y las propiedades de R*

El Teorema de Perron-Frobenius garantiza que el operador de responsabilidad M_R(D), cuando es no negativo e irreducible sobre A_D, tiene un eigenvector dominante único con todas las componentes positivas, que es precisamente R*.

Teorema A.2 (Perron-Frobenius):  Sea M una matriz cuadrada n×n con todas las entradas no negativas e irreducible. Entonces: (i) M tiene un eigenvalor positivo dominante ρ(M) > 0 (radio espectral). (ii) El eigenvector asociado a ρ(M) tiene todas sus componentes estrictamente

El Cálculo de la Responsabilidad · Apéndices

positivas. (iii) Este eigenvector es único salvo normalización. (iv) Todos los demás eigenvalores λ satisfacen |λ| < ρ(M).

Aplicación a M_R(D):  Bajo las condiciones de la sección A.1 — Q_D ≥ 0, b_D > 0, todo nodo de A_D con camino positivo hacia D, ρ(Q_D) < 1 — el operador M_R(D) = Q_D + η_D b_D 1ᵀ es no negativo, irreducible y aperiódico sobre A_D, con eigenvalor dominante λ₁ = 1. Perron-Frobenius garantiza entonces M_R(D) R*(D) = R*(D) con R*(D) > 0 en todo componente.

Implicaciones para el análisis de R*:

• R*ᵢ > 0 para todo nodo i ∈ A_D: ningún ancestro causal de D tiene peso de responsabilidad exactamente cero. Todo nodo con camino hacia D contribuye en alguna proporción. • R* es único: para un grafo causal dado respecto de D, hay un único vector de distribución de responsabilidad. El análisis no produce ambigüedad en el resultado final. • La velocidad de convergencia al eigenvector dominante depende de |λ₂|, el segundo eigenvalor en módulo de M_R(D). Esta velocidad no debe confundirse con las proporciones R*ᵢ: el porcentaje estable de cada nodo es una propiedad de la distribución, no de la rapidez de aproximación a ella.

Caso de grafos con nodos sin camino a D (cuando I5 falla):

Cuando el postulado I5 no se cumple para ningún nodo individualmente (causalidad acumulativa, Capítulo 14), existen nodos que no pertenecen a A_D. Esos nodos tienen R*ᵢ = 0 por construcción. La extensión mediante valores de Shapley es la respuesta correcta porque mide contribuciones marginales en coaliciones y no requiere conectividad individual hacia D.

### A.3 El Cálculo de Itô y la evolución dinámica del ego

El Cálculo de la Responsabilidad · Apéndices

El ego como proceso estocástico es la base de la formulación matemática de la Responsabilidad como EU(t) = E [dX/dt | F_t] que aparece en las referencias del libro. El Cálculo de Itô provee el marco para la evolución de los egos en tiempo continuo.

Teorema A.3 (Fórmula de Itô):  Sea X_t un proceso de Itô que satisface la ecuación diferencial estocástica dX_t = u (t, X_t) dt + s (t, X_t) dW_t, donde W_t es el movimiento browniano estándar. Sea f (t, x) una función C (1,2). Entonces:

df (t, X_t) = ∂f/∂t dt + ∂f/∂x dX_t + ½ σ² (t, X_t)

∂²f/∂x² dt

Aplicación a la evolución del ego:

El ego Ego(t) puede modelarse como un proceso de Itô donde:

• μ (t, Ego) = tasa de asunción de colapsos = φ₂(t) representa el proceso de integración. • σ (t, Ego) dW_t representa la aleatoriedad de los eventos que afectan al ego (los "colapsos" que pueden o no ser asumidos).

La condición de muerte (cierre de la integral del ego) corresponde formalmente al tiempo de parada:

τ_muerte = inf {t > 0: Ego(t) alcanza su límite de

posibilidades}

El ego final es la integral estocástica:

Ego_final = Ego (0) + ∫₀^τ φ₂(s)dμ(s) + ∫₀^τ σ(s)dW_s

El Cálculo de la Responsabilidad · Apéndices

El término ∫φ₂dμ captura la asunción consciente (determinista); el término ∫σdW captura los eventos aleatorios que el ego también debe integrar. La diferencia entre dos egos no es solo el camino determinista sino también cómo cada sujeto integró los eventos aleatorios que encontró.

Corolario:  El D_total en tiempo de vida D_vital = D/w_ref puede entenderse como la diferencia entre las integrales de dos procesos de ego: el ego que habría podido desarrollarse sin el daño y el ego que se desarrolló con él. Esa diferencia es el tiempo de vida cristalizado en trabajo que el daño impidió acumular.

### A.4 La derivación axiomática del valor de Shapley

Los valores de Shapley son la única solución que satisface simultáneamente cuatro axiomas de equidad en la distribución de responsabilidad acumulativa. Esa caracterización axiomática es lo que los distingue de cualquier otra distribución ad hoc.

Teorema A.4 (Shapley — Axiomático):  Sea v: 2^N → ℝ una función de valor con v (∅) = 0. La solución φ: v → ℝⁿ que satisface simultáneamente (i) Eficiencia: Σᵢφᵢ = v(N); (ii) Simetría: si v(S∪{i}) = v(S∪{j}) para todo S, entonces φᵢ = φⱼ; (iii) Nulo: si v(S∪{i}) = v(S) para todo S, entonces φᵢ = 0; (iv) Aditividad: φᵢ(v+w) = φᵢ(v) + φᵢ(w), está determinada de manera única por la fórmula: El Cálculo de la Responsabilidad · Apéndices

φᵢ(v) = Σ_{S⊆N\{i}} |S|! (n-|S|-1)! /n! × [v(S∪{i}) −

v(S)]

Por qué los axiomas son condiciones de equidad para la distribución del daño:

• Eficiencia: la suma de las responsabilidades individuales iguala exactamente el daño total. No queda "daño no atribuido" ni hay "sobreatribución". Aplicado al daño ambiental: la suma de las cuotas de Texaco + Petroecuador + otros = 100% del daño observado. • Simetría: actores con la misma contribución marginal en todas las coaliciones reciben la misma cuota. No hay discriminación por nombre o tamaño. • Nulo: un actor que no añade nada a ninguna coalición recibe responsabilidad cero. Evita imputar daño a actores que no contribuyeron causalmente en ninguna combinación. • Aditividad: si hay dos daños independientes, la responsabilidad total es la suma de las responsabilidades en cada daño por separado. Permite descomponer los casos complejos.

Relación entre R* y φ cuando el grafo es aditivo:

Cuando la función de valor es aditiva (v(S) = Σᵢ∈S v({i})), el valor de Shapley colapsa a R*:

Si v(S) = Σᵢ∈S R*ᵢ × D_total → φᵢ = R*ᵢ × D_total

La extensión Shapley generaliza R* al caso no aditivo (superaditividad por efectos de interacción entre contaminantes, o subaditivos por efectos de sustitución), que es exactamente el caso de la causalidad acumulativa del Capítulo 14.

El Cálculo de la Responsabilidad · Apéndices

### A.5 Formalización del contrafáctico histórico calibrado

El contrafáctico histórico —¿qué habría ocurrido sin este nodo? — es el fundamento del R* histórico del Capítulo 16. Su formalización permite distinguir la incertidumbre del contrafáctico de la imprecisión del análisis.

Definición formal del R* histórico:

R*_hist(Nᵢ) = [P(E|G) − P(E|G\Nᵢ)] / P(E|G)

donde P(E|G) es la probabilidad del evento E dado el sistema completo G, y P(E|G\Nᵢ) es la probabilidad del evento sin el nodo Nᵢ. El R* histórico es el diferencial normalizado de probabilidad.

Calibración del contrafáctico con los tres métodos:

3. Comparación de casos análogos: estima P(E|G\Nᵢ) a partir de episodios históricos similares donde ese nodo específico estaba ausente. Para Princip: las crisis de 1905, 1908 y 1911 sin asesinato de ningún archiduque, pero con el mismo sistema de alianzas. 4. Análisis de mecanismos: P(E|G\Nᵢ) ≈ P(E|G) si el mecanismo de transmisión entre el detonador y el resultado habría operado con otro detonador. P(E|G\Nᵢ) << P(E|G) si ese mecanismo era específico de Nᵢ. 5. Estimación de tasa base: el límite inferior de P(E|G\Nᵢ) es la tasa base del tipo de evento en ese sistema durante ese período, independientemente de cualquier detonador.

El Cálculo de la Responsabilidad · Apéndices

Intervalo de confianza del R* histórico:

El R* histórico no es un valor puntual sino un intervalo [R*_min, R*_max] calibrado por la incertidumbre del contrafáctico:

[R*_min, R*_max] = [(P(E|G) − P_max) / P(E|G),

(P(E|G) − P_min) / P(E|G)]

Para el sistema de alianzas de 1914: R*_alianzas ∈ [0.35, 0.55]. Para Gavrilo Princip: R*_Princip ∈ [0.00, 0.10]. La presentación correcta del análisis histórico siempre incluye estos rangos.

El Cálculo de la Responsabilidad · Apéndices

