# APÉNDICE C
## Fundamentos matemáticos y demostraciones

*Banach · Perron-Frobenius · Itô · Shapley · Contrafáctico histórico*

---

Este apéndice contiene las demostraciones de los resultados matemáticos que sustentan el sistema de imputación causal. Cada sección puede leerse de manera independiente. El lector sin formación matemática formal puede saltarse este apéndice sin perder el argumento del libro: todos los resultados se enuncian en lenguaje natural en los capítulos correspondientes.

#### A.1 El Teorema de Banach y la convergencia de R*

El vector R* se calcula como el eigenvector dominante de la matriz de pesos W mediante iteración de potencia. La convergencia de este algoritmo requiere que el proceso iterativo sea una contracción en el espacio de distribuciones de probabilidad. El Teorema del Punto Fijo de Banach garantiza esa convergencia bajo las condiciones del grafo causal.


Teorema A.1 (Banach — Punto Fijo):  Sea (X, d) un espacio métrico completo y f: X → X una contracción, es decir, ∃ c ∈ [0,1) tal que d(f(x), f(y)) ≤ c·d (x, y) para todo x, y ∈ X. Entonces f tiene un único punto fijo x* ∈ X tal que f(x*) = x*.

Aplicación al cálculo de R*:

Sea X = {v ∈ ℝⁿ: vᵢ ≥ 0, Σvᵢ = 1} el símplex de probabilidad (espacio de distribuciones de R* candidatas) con la métrica de variación total d (v, w) = Σᵢ|vᵢ − wᵢ|/2. El operador de iteración T definido por:

T(v) = Wv / ‖Wv‖₁

es una contracción sobre X cuando W es una matriz primitiva (irreducible y aperiódica). La condición de primitividad se traduce en el grafo causal como:

1. Irreductibilidad: desde cualquier nodo del grafo se puede alcanzar cualquier otro nodo siguiendo las aristas. Equivalente a que el grafo sea fuertemente conexo. 2. Aperiodicidad: el grafo no tiene ciclos de longitud fija que produjera oscilaciones en la iteración. Se garantiza añadiendo un pequeño peso ε de auto-referencia en los nodos hojas.

Demostración de la contracción:

Sea v, w ∈ X. Entonces:

d(T(v), T(w)) = ‖Wv/‖Wv‖₁ − Ww/‖Ww‖₁‖₁ ≤ c · ‖v −

w‖₁


donde c = 1 − δ(W) < 1, siendo δ(W) el coeficiente de ergodicidad de Dobrushin. Para matrices W no negativas con al menos una columna estrictamente positiva (condición que los grafos causales bien construidos satisfacen), δ(W) > 0 y por tanto c < 1. Por el Teorema de Banach, la iteración T^k(v₀) converge a un único punto fijo R* independientemente del valor inicial v₀. Eso justifica que el algoritmo de iteración de potencia produce siempre el mismo R* independientemente del vector inicial con que se arranque.

Corolario:  Si el grafo causal es irreducible y aperiódico (condiciones generalmente satisfechas en los grafos de los capítulos del libro), la iteración de potencia converge al único R* en a lo más log(ε/2) /log(c) iteraciones para alcanzar precisión ε.

#### A.2 El Teorema de Perron-Frobenius y las propiedades de R*

El Teorema de Perron-Frobenius garantiza que la matriz W de un grafo causal bien construido tiene un eigenvector dominante único con todas las componentes positivas, que es precisamente R*.

Teorema A.2 (Perron-Frobenius):  Sea W una matriz cuadrada n×n con todas las entradas no negativas e irreducible. Entonces: (i) W tiene un eigenvalor positivo dominante ρ(W) > 0 (radio espectral). (ii) El eigenvector asociado a ρ(W) tiene todas sus componentes estrictamente


positivas. (iii) Este eigenvector es único salvo normalización. (iv) Todos los demás eigenvalores λ satisfacen |λ| < ρ(W).

Implicaciones para el análisis de R*:

- R*ᵢ > 0 para todo nodo i: ningún nodo del grafo tiene peso causal exactamente cero si el grafo es irreducible. Todo nodo contribuye algo al resultado, aunque sea mínimamente.
- R* es único: para un grafo causal dado, hay un único vector de distribución de responsabilidad. El análisis no produce ambigüedad en el resultado final.
- La velocidad de convergencia de la iteración de potencia es proporcional a |λ₂/ρ(W)|, la razón entre el segundo eigenvalor más grande y el dominante. Cuando este ratio es pequeño, la convergencia es rápida (típicamente < 100 iteraciones para los grafos del libro).


Caso de grafos reducibles (cuando I5 falla):

Cuando el postulado I5 no se cumple para ningún nodo (causalidad acumulativa, Capítulo 14), el grafo puede ser reducible: existen nodos que no tienen aristas hacia el nodo final. En ese caso, R* convencional asigna cero a esos nodos. La extensión mediante valores de Shapley es la respuesta correcta porque no requiere la irreductibilidad del grafo.

#### A.3 El Cálculo de Itô y la evolución dinámica del ego


El ego como proceso estocástico es la base de la formulación matemática de la Responsabilidad como EU(t) = E [dX/dt | F_t] que aparece en las referencias del libro. El Cálculo de Itô provee el marco para la evolución de los egos en tiempo continuo.

Teorema A.3 (Fórmula de Itô):  Sea X_t un proceso de Itô que satisface la ecuación diferencial estocástica dX_t = u (t, X_t) dt + s (t, X_t) dW_t, donde W_t es el movimiento browniano estándar. Sea f (t, x) una función C (1,2). Entonces:

df (t, X_t) = ∂f/∂t dt + ∂f/∂x dX_t + ½ σ² (t, X_t)

∂²f/∂x² dt

Aplicación a la evolución del ego:

El ego Ego(t) puede modelarse como un proceso de Itô donde:

- μ (t, Ego) = tasa de asunción de colapsos = φ₂(t) representa el proceso de integración.
- σ (t, Ego) dW_t representa la aleatoriedad de los eventos que afectan al ego (los "colapsos" que pueden o no ser asumidos).


La condición de muerte (cierre de la integral del ego) corresponde formalmente al tiempo de parada:

τ_muerte = inf {t > 0: Ego(t) alcanza su límite de

posibilidades}

El ego final es la integral estocástica:

Ego_final = Ego (0) + ∫₀^τ φ₂(s)dμ(s) + ∫₀^τ σ(s)dW_s


El término ∫φ₂dμ captura la asunción consciente (determinista); el término ∫σdW captura los eventos aleatorios que el ego también debe integrar. La diferencia entre dos egos no es solo el camino determinista sino también cómo cada sujeto integró los eventos aleatorios que encontró.

Corolario:  El D_total en tiempo de vida D_vital = D/w_ref puede entenderse como la diferencia entre las integrales de dos procesos de ego: el ego que habría podido desarrollarse sin el daño y el ego que se desarrolló con él. Esa diferencia es el tiempo de vida cristalizado en trabajo que el daño impidió acumular.

#### A.4 La derivación axiomática del valor de Shapley

Los valores de Shapley son la única solución que satisface simultáneamente cuatro axiomas de equidad en la distribución de responsabilidad acumulativa. Esa caracterización axiomática es lo que los distingue de cualquier otra distribución ad hoc.

Teorema A.4 (Shapley — Axiomático):  Sea v: 2^N → ℝ una función de valor con v (∅) = 0. La solución φ: v → ℝⁿ que satisface simultáneamente (i) Eficiencia: Σᵢφᵢ = v(N); (ii) Simetría: si v(S∪{i}) = v(S∪{j}) para todo S, entonces φᵢ = φⱼ; (iii) Nulo: si v(S∪{i}) = v(S) para todo S, entonces φᵢ = 0; (iv) Aditividad: φᵢ(v+w) = φᵢ(v) + φᵢ(w), está determinada de manera única por la fórmula: El Cálculo de la Responsabilidad · Apéndices

φᵢ(v) = Σ_{S⊆N\{i}} |S|! (n-|S|-1)! /n! × [v(S∪{i}) −

v(S)]

Por qué los axiomas son condiciones de equidad para la distribución del daño:

- Eficiencia: la suma de las responsabilidades individuales iguala exactamente el daño total. No queda "daño no atribuido" ni hay "sobreatribución". Aplicado al daño ambiental: la suma de las cuotas de Texaco + Petroecuador + otros = 100% del daño observado.
- Simetría: actores con la misma contribución marginal en todas las coaliciones reciben la misma cuota. No hay discriminación por nombre o tamaño.
- Nulo: un actor que no añade nada a ninguna coalición recibe responsabilidad cero. Evita imputar daño a actores que no contribuyeron causalmente en ninguna combinación.
- Aditividad: si hay dos daños independientes, la responsabilidad total es la suma de las responsabilidades en cada daño por separado. Permite descomponer los casos complejos.


Relación entre R* y φ cuando el grafo es aditivo:

Cuando la función de valor es aditiva (v(S) = Σᵢ∈S v({i})), el valor de Shapley colapsa a R*:

Si v(S) = Σᵢ∈S R*ᵢ × D_total → φᵢ = R*ᵢ × D_total

La extensión Shapley generaliza R* al caso no aditivo (superaditividad por efectos de interacción entre contaminantes, o subaditivos por efectos de sustitución), que es exactamente el caso de la causalidad acumulativa del Capítulo 14.


#### A.5 Formalización del contrafáctico histórico calibrado

El contrafáctico histórico —¿qué habría ocurrido sin este nodo? — es el fundamento del R* histórico del Capítulo 16. Su formalización permite distinguir la incertidumbre del contrafáctico de la imprecisión del análisis.

Definición formal del R* histórico:

R*_hist(Nᵢ) = [P(E|G) − P(E|G\Nᵢ)] / P(E|G)

donde P(E|G) es la probabilidad del evento E dado el sistema completo G, y P(E|G\Nᵢ) es la probabilidad del evento sin el nodo Nᵢ. El R* histórico es el diferencial normalizado de probabilidad.

Calibración del contrafáctico con los tres métodos:

3. Comparación de casos análogos: estima P(E|G\Nᵢ) a partir de episodios históricos similares donde ese nodo específico estaba ausente. Para Princip: las crisis de 1905, 1908 y 1911 sin asesinato de ningún archiduque, pero con el mismo sistema de alianzas. 4. Análisis de mecanismos: P(E|G\Nᵢ) ≈ P(E|G) si el mecanismo de transmisión entre el detonador y el resultado habría operado con otro detonador. P(E|G\Nᵢ) << P(E|G) si ese mecanismo era específico de Nᵢ. 5. Estimación de tasa base: el límite inferior de P(E|G\Nᵢ) es la tasa base del tipo de evento en ese sistema durante ese período, independientemente de cualquier detonador.


Intervalo de confianza del R* histórico:

El R* histórico no es un valor puntual sino un intervalo [R*_min, R*_max] calibrado por la incertidumbre del contrafáctico:

[R*_min, R*_max] = [(P(E|G) − P_max) / P(E|G),

(P(E|G) − P_min) / P(E|G)]

Para el sistema de alianzas de 1914: R*_alianzas ∈ [0.35, 0.55]. Para Gavrilo Princip: R*_Princip ∈ [0.00, 0.10]. La presentación correcta del análisis histórico siempre incluye estos rangos.


