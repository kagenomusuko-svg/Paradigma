## PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·6
Extensión al caso acumulativo
El valor de Shapley cuando ningún nodo es condición sine qua non
individual

### I. El límite del Teorema IV·2
El Teorema de la Responsabilidad Causal Proporcional
requiere que al menos un nodo del grafo sea condición sine qua
non individual de D. Hay sistemas causales complejos donde esta
condición no se cumple: el resultado emerge de la intersección de
múltiples contribuciones ninguna de las cuales es individualmente
necesaria. En esos sistemas, el axioma A2 no puede cumplirse en
su formulación original.
En esos sistemas, el eigenvector sigue siendo
matemáticamente calculable, pero su interpretación como
responsabilidad causal proporcional pierde el fundamento que A2
le provee. Este capítulo establece qué distribución aplica en ese
caso.

### II. La función característica del juego cooperativo
asociado

Metrología Causal · Vol. II
Cuando ningún nodo es condición sine qua non individual,
el sistema causal se modela como un juego cooperativo. El juego
tiene como jugadores los nodos de N (excluyendo Nf) y como
función característica v: 2^N → [0,1] donde v(S) mide la fracción
del resultado D que la coalición S puede producir por sí sola.
Función característica v(S)
v(S) = fracción de D que la submatriz W_S (restringida
a nodos en S) produce en Nf
v ((cid:0)) = 0 (la coalición vacía no produce nada) · v(N(cid:0){Nf}) = 1 (todos
los nodos producen todo D). v(S) se calcula como el eigenvector principal de
W_S normalizado sobre Nf.

### III. El valor de Shapley como distribución de
responsabilidad
El valor de Shapley φᵢ de cada nodo i es su contribución
marginal promedio sobre todas las coaliciones posibles. Mide
cuánto agrega cada nodo al resultado cuando se une a una
coalición que ya existía, promediado sobre todos los órdenes
posibles.
Valor de Shapley
φᵢ = Σ_ {¡S ⊆ ¡N∖ {i, Nf}} [|S|! · (n−|S|−1)! / n!] ×
[v(S∪{i}) − v(S)]
n = |N(cid:0){Nf}| es el número de nodos sin el sumidero. El factor
combinatorio es la probabilidad de que S sea exactamente el conjunto de
nodos que precedieron a i en un orden aleatorio.
El valor de Shapley satisface cuatro axiomas propios:
eficiencia (los valores suman v(N)), simetría (nodos con
contribuciones idénticas reciben valores idénticos), nulidad (nodos

Metrología Causal · Vol. II
que no contribuyen a ninguna coalición reciben cero), y aditividad.
En el caso acumulativo, estos axiomas determinan de manera
única la distribución Shapley.

### IV. El Shapley como caso límite del eigenvector
La relación entre el eigenvector y el valor de Shapley no es
de oposición sino de continuidad. El valor de Shapley es el caso
límite del eigenvector cuando la condición sine qua non individual
se debilita hacia cero. Esta continuidad tiene una consecuencia
práctica: en grafos donde la condición se cumple para algunos
nodos, pero no para todos, los dos métodos producen valores
similares.
Característica Eigenvector (caso Valor de Shapley (caso
s.q.n.) acumulativo)
Condición de Al menos un nodo es Ningún nodo es condición
aplicación condición sine qua sine qua non individual
non individual
Axiomas A1 eficiencia, A2 Eficiencia, simetría,
causalidad necesaria, nulidad, aditividad
A3 centralidad
recursiva, A4
monotonicidad
Complejidad O(n²·k) con k O(2ⁿ) exacto. Para n > 20
iteraciones. Eficiente requiere métodos de
para grafos grandes. aproximación.
Corolarios R*_neta, Δ, fraude R*_neta y Δ son válidos
derivados annona — todos con Shapley como base.
válidos Fraude annona requiere
adaptación del IIC.

Metrología Causal · Vol. II
Producto de salida · Capítulo IV·6
Extensión del Teorema IV·2 al caso acumulativo: el valor de
Shapley φᵢ como la distribución de responsabilidad cuando
ningún nodo es condición sine qua non individual. La
función característica v(S) del juego cooperativo asociado al
grafo G. El Shapley como caso límite del eigenvector con sus
axiomas propios.
Notas al Capítulo IV·6
1 La complejidad computacional O(2ⁿ) del valor de Shapley exacto es una
limitación práctica para grafos grandes. Los métodos de aproximación
más eficientes son: (a) muestreo de permutaciones aleatorias — calcular
la contribución marginal de cada nodo en K permutaciones aleatorias y
promediar, con error que decrece como 1/√K; y (b) el algoritmo de
Strömberg (2018) que calcula Shapley en tiempo O(n·2^(n/2)) para
estructuras con independencia condicional.
2 La relación entre el eigenvector y el Shapley tiene un precedente en la
literatura relevante para la Conjetura del Operador Unificador del

### Capítulo IV·7. Teng (2016) demuestra que el PageRank puede
interpretarse como el valor de Shapley de un juego de influencia social
específico. Si esa relación puede generalizarse al grafo causal ponderado
de este sistema, el eigenvector y el Shapley serían instancias del mismo
operador con diferentes funciones características.

Metrología Causal · Vol. II

