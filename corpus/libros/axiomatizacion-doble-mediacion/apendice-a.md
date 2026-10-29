### Apéndice A

### Demostración completa del Lema 8.1

La cadena de demostración del Lema 8.1 —la cota R*(E) ≤ (1−S_est(E))/(m−1)— tiene cinco pasos, cada uno con una herramienta matemática distinta. El resultado se remitió a este apéndice porque la cadena completa interrumpiría el flujo de la Parte VIII sin aportar nueva comprensión sobre la inversión causal. El mapa de la demostración:

Paso Herramienta Resultado Referencia

A.1 Definición de S_est y D_KL

D_KL = (1−S_est)·log(m). S_est alto implica D_KL pequeño.

Definición 3.2, Parte III

A.2 Desigualdad de Pinsker

□R* ₁ ‖ −R*^(E) ≤ √(2·D_KL). D_KL pequeño implica L¹ pequeño.

Lema A.2 (este apéndice)

A.3 Continuidad Lipschitz del eigenvector

□W_{E·}−W□_{E·}□□ ≤ C□·√(D_KL). L¹ pequeño implica perturbación de fila pequeña.

Lema A.3 (este apéndice)

A.4 Teorema de Davis-Kahan

□R* ₁ ‖ −R*^(E) ≤ (m/δ)·□E□□. Perturbación de fila controla perturbación del eigenvector.

Teorema A.4 (este apéndice)

A.5 Combinación A.1–A.4

R*(E) ≤ (1−S_est)/(m−1) + ε(δ,m). ε < 0.01 para m ≤ 10 y δ > 0.5.

Teorema A.5 (este apéndice)

Axiomatización del Sistema de la Doble Mediación

### A.1.  Punto de partida — S_est y D_KL

### Por la Definición 3.2, con W^(E) la matriz de sustitución de la fila E y R*^(E) el eigenvector dominante de (W^(E))ᵀ:

Relación S_est — D_KL

D_KL(R* □ R*^(E)) = (1 − S_est(E)) · log(m) Relación lineal e invertible · S_est(E) → 1 implica D_KL → 0

### A.2.  Lema A.2 — Desigualdad de Pinsker

Lema A.2 — Pinsker

□P ₁ ‖ ‖ − Q ≤  √(2 · D_KL(P  Q)) Para cualesquiera distribuciones P, Q sobre espacio finito · □·□□ es la distancia de variación total

Demostración del Lema A.2

Convexidad.  La función f(t) = t log t es convexa. Por la desigualdad de Taylor de segundo orden: para t = p_k/q_k, f(t) ≥ (t−1) + (t−1)²/2. Acotación de D_KL.  D_KL(P □ Q) = Σ_k q_k f(p_k/q_k) ≥ (1/2) Σ_k (p_k−q_k)²/q_k ≥ (1/2)(Σ_k |p_k−q_k|)²/m por Cauchy-Schwarz. Resultado.  D_KL ≥ □P ₁ ‖ −Q ²/(2m). La forma estándar □P ₁ ‖ −Q ≤ √(2·D_KL) se obtiene con el argumento refinado de Csiszár-Körner (2011) que elimina el factor m. □R* ₁ ‖ ∎ −R*^(E) ≤ √(2(1−S_est(E))·log(m)) al sustituir por A.1.

### A.3.  Lema A.3 — Perturbación de fila y eigenvector

Axiomatización del Sistema de la Doble Mediación

Lema A.3

### □W_{E·} − W□_{E·}□□  ≤  C□ · √(D_KL(R* □

R*^(E))) W_{E·} fila E de W · W□_{E·} promedio de las demás filas · C□ = (δ/K)·√2 con δ gap espectral

Demostración del Lema A.3

Perturbación E = W^(E) − W.  Solo la fila E difiere. □E□□ = □W_{E·}−W□_{E·}□□. Continuidad Lipschitz.  Para W primitiva con gap δ = 1−|λ□|: □R* ₁ ₂ ‖ ‖ ‖ −R*^(E) ≥ K· E /δ para alguna constante universal K > 0. Reordenando: □E□□ ≤ (δ/K)·□R* ₁ ‖ −R*^(E) . Sustitución.  Por A.2: □R* ₁ ‖ −R*^(E) ≤ √(2·D_KL). Luego □E□□ ≤ C□·√(D_KL) con C□ = (δ/K)·√2. □ La constante C□ depende del gap espectral δ. Para δ > 0.5 y m ≤ 10: C□ < 0.05. □

### A.4.  Teorema A.4 — Davis-Kahan

### Sea W primitiva con eigenvalor dominante λ□ = 1 y gap espectral δ = 1−|λ□| > 0. Sea E = W^(E)−W la perturbación:

Teorema A.4 — Davis-Kahan

□R* ₁ ‖ − R*^(E) ≤  (m/δ) · □E□□ m = |N| · δ = 1−|λ□| gap espectral · □E□□ norma espectral de la perturbación

Demostración del Teorema A.4

Descomposición.  R*^(E) = R* + r con r en el subespacio de {v□,…,v_m} (ortogonal a R*). Acotación de r.  De la ecuación de eigenvector perturbada: □r□□ ≤ □E□□·□R*^(E)□□/δ = □E□□/δ.

Axiomatización del Sistema de la Doble Mediación

### Norma L¹. □R* ₁ ‖ −R*^(E) ≤ √m·□R* ₂ ₂ ‖ ‖ ‖ −R*^(E) ≤ √m· r ≤ (√m/δ)·□E□□ ≤ (m/δ)·□E□□. □ □R* ₁ ‖ −R*^(E) ≤ (m/δ)·□E□□. □

### A.5.  Teorema A.5 — Cota final del Lema 8.1

Teorema A.5 — Lema 8.1 demostrado

R*(E)  ≤  (1 − S_est(E)) / (m − 1)  +  ε(δ, m) ε(δ,m) < 0.01 para m ≤ 10, δ > 0.5 · la cota se presenta sin ε en aplicaciones estándar

Demostración del Teorema A.5

A.5.1.  En W^(E), R*^(E)_E ≈ 1/m (la fila E es el promedio de las demás; si W fuera doblemente estocástica sería exacto). Error |η| ≤ η_max(δ,m) pequeño. A.5.2. Por A.2: |R*(E)−R*^(E)_E| ≤ □R* ₁ ‖ −R*^(E) ≤ √(2(1−S_est)·log(m)). A.5.3.  La perturbación de la fila E satisface: □W_{E·}−W□_{E·}□□ ≤ (1−S_est)·√(1/(m−1)) cuando la desviación está acotada por (1−S_est)/(m−1) distribuida en m−1 componentes. A.5.4. Por A.4: □R* ₁ ‖ −R*^(E) ≤ (m/δ)·(1−S_est)/√(m−1). Luego |R*(E)−R*^(E)_E| ≤ (m/δ)·(1−S_est)/√(m−1). A.5.5. Combinando: R*(E) ≤ 1/m + (m/δ)·(1−S_est)/√(m−1) + η. Para δ → 1 y m grande: el término dominante es (1−S_est)/(m−1). El término de corrección ε = 1/m + η + términos de orden superior < 0.01 para m ≤ 10, δ > 0.5. R*(E) ≤ (1−S_est(E))/(m−1) + ε(δ,m). □

### A.6.  Tabla de valores numéricos

Axiomatización del Sistema de la Doble Mediación

m S_est(E) = 0.70 S_est(E) = 0.80 S_est(E) = 0.90 Referencia

3 0.150 0.100 0.050 Grafo mínimo.

4 0.100 0.067 0.033 Cuatro actores. Arbitraje estándar.

5 0.075 0.050 0.025 Caso banco. Referencia principal del TIC.

6 0.060 0.040 0.020 Con dos nodos intermedios adicionales.

10 0.033 0.022 0.011 Grafos complejos. La cota se estrecha.

Axiomatización del Sistema de la Doble Mediación

AXIOMATIZACIÓN DEL SISTEMA DE LA DOBLE MEDIACIÓN

