APÉNDICES · Demostraciones formales de propiedades
Apéndice A·2
Convergencia del método de potencias
para el cálculo de R*
Tasa de convergencia, condiciones de lentitud y protocolos de
aceleración

### I. El método de potencias: formulación y
convergencia
El método de potencias calcula el eigenvector principal de W
iterativamente. Sea v⁽⁰⁾ un vector inicial con v⁽⁰⁾ > 0 (todos los
componentes positivos). La iteración es:
v⁽ᵏ⁺¹⁾ = W · v⁽ᵏ⁾ / ||W · v⁽ᵏ⁾||₁
Teorema de convergencia: bajo las condiciones de Perron-
Frobenius (W no negativa, irreducible, aperiódica), la
secuencia {v⁽ᵏ⁾} converge al eigenvector principal normalizado
v* = R* con independencia de la elección de v⁽⁰⁾ > 0.
La demostración de convergencia se basa en la
descomposición espectral. Cualquier vector inicial v⁽⁰⁾ puede
escribirse como combinación lineal de los eigenvectores de W:
v⁽⁰⁾ = c₁v₁ + c₂v₂ + ... + cₙvₙ, donde v₁ = v* (el eigenvector
principal con eigenvalor ρ₁ = ρ(W)) y vₖ son los eigenvectores

Metrología Causal
con eigenvalores ρₖ, ordenados por |ρₖ| decreciente. Dado
que v⁽⁰⁾ > 0 y v* > 0, se tiene c₁ > 0.
Después de k iteraciones sin normalización: Wᵏ v⁽⁰⁾ = c₁ρ₁ᵏv₁
+ c₂ρ₂ᵏv₂ + ... + cₙρₙᵏvₙ. Dividiendo por ρ₁ᵏ: Wᵏv⁽⁰⁾/ρ₁ᵏ = c₁v₁
+ c₂(ρ₂/ρ₁) ᵏv₂ + ... + cₙ(ρₙ/ρ₁) ᵏvₙ. Por Perron-Frobenius,
|ρₖ| < ρ₁ para k ≥ 2, por tanto |ρₖ/ρ₁| < 1 y (ρₖ/ρ₁) ᵏ → 0
para todo k ≥ 2. En el límite, Wᵏv⁽⁰⁾/ρ₁ᵏ → c₁v₁ = c₁v*.
Normalizando: v⁽∞⁾ = v*.

### II. La tasa de convergencia y el cociente
espectral
La tasa de convergencia del método de potencias está
gobernada por el cociente espectral r = |ρ₂|/ρ₁, donde ρ₂ es
el segundo eigenvalor (en módulo) de W. Específicamente, el
error en la iteración k satisface:
||v⁽ᵏ⁾ − v*|| ≤ C · rᵏ
para alguna constante C > 0. La convergencia es geométrica
con razón r. Cuando r es pequeño (ρ₂ << ρ₁), la convergencia
es rápida: el error decrece por un factor r en cada iteración.
Cuando r se aproxima a 1 (ρ₂ ≈ ρ₁), la convergencia es lenta:
muchas iteraciones son necesarias para reducir el error en un
orden de magnitud.
Los grafos causales de sistemas institucionales complejos
típicamente tienen r pequeño porque el eigenvector
dominante concentra la masa en pocos nodos (los nodos de
diseño con alta centralidad), lo que produce dominancia
espectral pronunciada. Los grafos que producen convergencia
lenta son los grafos con estructura casi-bipartita — donde los
nodos se dividen en dos grupos de influencia

Metrología Causal
aproximadamente igual, produciendo un segundo eigenvalor
casi igual al primero en módulo.

### III. Condiciones de convergencia lenta y
protocolos
Los tres tipos de grafos causales donde la convergencia puede
ser lenta en la práctica:
Primero: los grafos con estructura casi simétrica — donde
todos los nodos tienen peso de arista similar y ningún nodo
domina claramente. En el análisis de responsabilidad, esto
corresponde a sistemas con distribución de poder muy
uniforme. El protocolo: verificar r después de 10 iteraciones;
si el cambio en el vector es mayor de 0.01, continuar hasta
convergencia con criterio de parada ||v⁽ᵏ⁺¹⁾ − v⁽ᵏ⁾||₁ < 10⁻⁶.
Segundo: los grafos casi-bipartitos — donde hay dos
subgrupos de nodos con poca conexión entre ellos (el sistema
tiene dos «clusters» causales casi independientes). El
protocolo: descomponer el grafo en sus componentes
fuertemente conexas, analizar cada componente por separado,
y combinar los resultados con los pesos de las aristas que
conectan las componentes.
Tercero: los grafos con ciclos de longitud dominante — donde
la mayoría de los ciclos del grafo tienen la misma longitud,
produciendo periodicidad que ralentiza la convergencia. El
protocolo: añadir una pequeña perturbación ε en la diagonal
de W (W' = W + εI para ε ∈ (0.001, 0.01)) para romper la
periodicidad, calcular el eigenvector de W', y verificar que la
perturbación no cambia el ranking de R*. Si el ranking cambia
con ε > 0.001, el grafo tiene periodicidad que afecta la
interpretación del resultado y debe declararse.

Metrología Causal
Criterio de convergencia estándar para el caso de Prometeo
Condición de parada: ||v⁽ᵏ⁺¹⁾ − v⁽ᵏ⁾||₁ < 10⁻⁶ (todos los
componentes del vector cambiaron menos de 10⁻⁶ en la
última iteración).
Número máximo de iteraciones: 1,000. Si no se alcanza la
condición de parada en 1,000 iteraciones, declarar
convergencia lenta y aplicar los protocolos de diagnóstico.
Vector inicial: v⁽⁰⁾ = (1/n, 1/n, ..., 1/n) — distribución
uniforme. Este vector garantiza que c₁ > 0 en la
descomposición espectral para cualquier W no negativa
irreducible.
Para grafos de hasta 20 nodos: la convergencia con los
midpoints de los pesos ocurre típicamente en menos de 50
iteraciones.
Notas al apéndice A·2
1 La convergencia del método de potencias es equivalente a la
convergencia de la cadena de Markov con matriz de transición W/ρ(W)
a su distribución estacionaria. El cociente espectral r = |ρ₂|/ρ₁ es
exactamente el factor de mezcla de la cadena: determina cuántas
iteraciones son necesarias para que la distribución de la cadena se
aproxime a la distribución estacionaria. Esta equivalencia conecta el
análisis de sensibilidad de Prometeo con la teoría de cadenas de Markov
y sus resultados sobre velocidad de mezcla.

Metrología Causal
