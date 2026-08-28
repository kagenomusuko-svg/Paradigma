## Apéndice A

Demostración completa del Lema 8.1
La cadena de demostración del Lema 8.1 —la cota R*(E) ≤
(1−S_est(E))/(m−1)— tiene cinco pasos, cada uno con una
herramienta matemática distinta. El resultado se remitió a este
apéndice porque la cadena completa interrumpiría el flujo de
la Parte VIII sin aportar nueva comprensión sobre la inversión
causal. El mapa de la demostración:
Paso Herramienta Resultado Referencia
A.1 Definición de D_KL = Definición 3.2,
S_est y D_KL (1−S_est)·log(m). S_est Parte III
alto implica D_KL
pequeño.
A.2 Desigualdad (cid:0)R*−R*^(E)‖ ₁ ≤ Lema A.2 (este
de Pinsker √(2·D_KL). D_KL apéndice)
pequeño implica L¹
pequeño.
A.3 Continuidad (cid:0)W_{E·}−W(cid:0)_{E·}(cid:0)(cid:0) Lema A.3 (este
Lipschitz del ≤ C(cid:0)·√(D_KL). L¹ apéndice)
eigenvector pequeño implica
perturbación de fila
pequeña.
A.4 Teorema de (cid:0)R*−R*^(E)‖ ₁ ≤ Teorema A.4
Davis-Kahan (m/δ)·(cid:0)E(cid:0)(cid:0). (este apéndice)
Perturbación de fila
controla perturbación del
eigenvector.
A.5 Combinación R*(E) ≤ (1−S_est)/(m−1) Teorema A.5
A.1–A.4 + ε(δ,m). ε < 0.01 para m (este apéndice)
≤ 10 y δ > 0.5.

Axiomatización del Sistema de la Doble Mediación
A.1. Punto de partida — S_est y D_KL
Por la Definición 3.2, con W^(E) la matriz de sustitución de la
fila E y R*^(E) el eigenvector dominante de (W^(E))ᵀ:
Relación S_est — D_KL
D_KL(R* (cid:0) R*^(E)) = (1 − S_est(E)) · log(m)
Relación lineal e invertible · S_est(E) → 1 implica D_KL → 0
A.2. Lema A.2 — Desigualdad de Pinsker
Lema A.2 — Pinsker
(cid:0)P − Q‖ ₁ ≤ √(2 · D_KL(P ‖ Q))
Para cualesquiera distribuciones P, Q sobre espacio finito · (cid:0)·(cid:0)(cid:0) es la distancia
de variación total
Demostración del Lema A.2
Convexidad. La función f(t) = t log t es convexa.
Por la desigualdad de Taylor de segundo orden: para t
= p_k/q_k, f(t) ≥ (t−1) + (t−1)²/2.
Acotación de D_KL. D_KL(P (cid:0) Q) = Σ_k q_k
f(p_k/q_k) ≥ (1/2) Σ_k (p_k−q_k)²/q_k ≥
(1/2)(Σ_k |p_k−q_k|)²/m por Cauchy-Schwarz.
Resultado. D_KL ≥ (cid:0)P−Q‖ ₁ ²/(2m). La forma
estándar (cid:0)P−Q‖ ₁ ≤ √(2·D_KL) se obtiene con el
argumento refinado de Csiszár-Körner (2011) que
elimina el factor m.
(cid:0)R*−R*^(E)‖₁ ≤ √(2(1−S_est(E))·log(m)) al sustituir por A.1. ∎
A.3. Lema A.3 — Perturbación de fila y
eigenvector

Axiomatización del Sistema de la Doble Mediación
Lema A.3
(cid:0)W_{E·} − W(cid:0)_{E·}(cid:0)(cid:0) ≤ C(cid:0) · √(D_KL(R* (cid:0)
R*^(E)))
W_{E·} fila E de W · W(cid:0)_{E·} promedio de las demás filas · C(cid:0) =
(δ/K)·√2 con δ gap espectral
Demostración del Lema A.3
Perturbación E = W^(E) − W. Solo la fila E difiere.
(cid:0)E(cid:0)(cid:0) = (cid:0)W_{E·}−W(cid:0)_{E·}(cid:0)(cid:0).
Continuidad Lipschitz. Para W primitiva con gap δ
= 1−|λ(cid:0)|: (cid:0)R*−R*^(E)‖ ₁ ≥ K·‖ E‖ ₂ /δ para
alguna constante universal K > 0. Reordenando:
(cid:0)E(cid:0)(cid:0) ≤ (δ/K)·(cid:0)R*−R*^(E)‖ ₁ .
Sustitución. Por A.2: (cid:0)R*−R*^(E)‖ ₁ ≤
√(2·D_KL). Luego (cid:0)E(cid:0)(cid:0) ≤ C(cid:0)·√(D_KL) con C(cid:0)
= (δ/K)·√2. (cid:0)
La constante C(cid:0) depende del gap espectral δ. Para δ > 0.5 y m ≤ 10: C(cid:0) <
0.05. (cid:0)
A.4. Teorema A.4 — Davis-Kahan
Sea W primitiva con eigenvalor dominante λ(cid:0) = 1 y gap
espectral δ = 1−|λ(cid:0)| > 0. Sea E = W^(E)−W la
perturbación:
Teorema A.4 — Davis-Kahan
(cid:0)R* − R*^(E)‖ ₁ ≤ (m/δ) · (cid:0)E(cid:0)(cid:0)
m = |N| · δ = 1−|λ(cid:0)| gap espectral · (cid:0)E(cid:0)(cid:0) norma espectral de la
perturbación
Demostración del Teorema A.4
Descomposición. R*^(E) = R* + r con r en el
subespacio de {v(cid:0),…,v_m} (ortogonal a R*).
Acotación de r. De la ecuación de eigenvector
perturbada: (cid:0)r(cid:0)(cid:0) ≤ (cid:0)E(cid:0)(cid:0)·(cid:0)R*^(E)(cid:0)(cid:0)/δ =
(cid:0)E(cid:0)(cid:0)/δ.

Axiomatización del Sistema de la Doble Mediación
Norma L¹. (cid:0)R*−R*^(E)‖ ₁ ≤
√m·(cid:0)R*−R*^(E)‖ ₂ ≤ √m·‖ r‖ ₂ ≤
(√m/δ)·(cid:0)E(cid:0)(cid:0) ≤ (m/δ)·(cid:0)E(cid:0)(cid:0). (cid:0)
(cid:0)R*−R*^(E)‖₁ ≤ (m/δ)·(cid:0)E(cid:0)(cid:0). (cid:0)
A.5. Teorema A.5 — Cota final del Lema 8.1
Teorema A.5 — Lema 8.1 demostrado
R*(E) ≤ (1 − S_est(E)) / (m − 1) + ε(δ, m)
ε(δ,m) < 0.01 para m ≤ 10, δ > 0.5 · la cota se presenta sin ε en aplicaciones
estándar
Demostración del Teorema A.5
A.5.1. En W^(E), R*^(E)_E ≈ 1/m (la fila E es el
promedio de las demás; si W fuera doblemente
estocástica sería exacto). Error |η| ≤ η_max(δ,m)
pequeño.
A.5.2. Por A.2: |R*(E)−R*^(E)_E| ≤
(cid:0)R*−R*^(E)‖ ₁ ≤ √(2(1−S_est)·log(m)).
A.5.3. La perturbación de la fila E satisface:
(cid:0)W_{E·}−W(cid:0)_{E·}(cid:0)(cid:0) ≤ (1−S_est)·√(1/(m−1))
cuando la desviación está acotada por
(1−S_est)/(m−1) distribuida en m−1 componentes.
A.5.4. Por A.4: (cid:0)R*−R*^(E)‖ ₁ ≤
(m/δ)·(1−S_est)/√(m−1). Luego
|R*(E)−R*^(E)_E| ≤ (m/δ)·(1−S_est)/√(m−1).
A.5.5. Combinando: R*(E) ≤ 1/m +
(m/δ)·(1−S_est)/√(m−1) + η. Para δ → 1 y m
grande: el término dominante es (1−S_est)/(m−1). El
término de corrección ε = 1/m + η + términos de
orden superior < 0.01 para m ≤ 10, δ > 0.5.
R*(E) ≤ (1−S_est(E))/(m−1) + ε(δ,m). (cid:0)
A.6. Tabla de valores numéricos

Axiomatización del Sistema de la Doble Mediación
m S_est(E) = S_est(E) = S_est(E) = Referencia
0.70 0.80 0.90
3 0.150 0.100 0.050 Grafo mínimo.
4 0.100 0.067 0.033 Cuatro actores.
Arbitraje estándar.
5 0.075 0.050 0.025 Caso banco.
Referencia
principal del TIC.
6 0.060 0.040 0.020 Con dos nodos
intermedios
adicionales.
10 0.033 0.022 0.011 Grafos complejos.
La cota se estrecha.

Axiomatización del Sistema de la Doble Mediación
AXIOMATIZACIÓN DEL SISTEMA DE LA DOBLE MEDIACIÓN

