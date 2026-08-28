APÉNDICES · Demostraciones formales de propiedades
Apéndice A·5
Demostración de la dualidad daño-
beneficio: R* y R*_B
Identidad formal del operador y condiciones de dualidad
simultánea

### I. Los dos grafos y el mismo operador
La dualidad daño-beneficio establece que R* y R*_B son el
mismo operador aplicado a dos grafos distintos: el grafo de
daño G_D = (N_D, E_D, W_D) y el grafo de beneficio G_B
= (N_B, E_B, W_B). El operador es idéntico: el eigenvector
principal normalizado de la matriz de adyacencia ponderada.
Lo que difiere es el objeto sobre el que el operador actúa — la
matriz W_D vs. la matriz W_B.
Proposición de identidad del operador: R*_D =
eigenvector_normalizado(W_D) y R*_B =
eigenvector_normalizado(W_B). Las dos expresiones son
instancias del mismo funcional matemático F(W) =
eigenvector_principal_normalizado(W) aplicado a distintos
argumentos.
La demostración de la identidad es inmediata: F(W_D)
produce R*_D y F(W_B) produce R*_B. Las propiedades

Metrología Causal
formales de F son las mismas en los dos casos (por Perron-
Frobenius, aplicable cuando ambas matrices son no negativas
e irreducibles). Las propiedades del resultado — positividad
estricta de todos los componentes, unicidad, suma igual a 1 —
son idénticas en los dos grafos.
La consecuencia ontológica: el colapso es el colapso con
independencia del signo del resultado. R* no tiene un sesgo
intrínseco hacia el daño; mide centralidad causal con la misma
matemática con independencia de si el resultado que fluye a
través de esa centralidad es positivo o negativo. La distinción
entre daño y beneficio está en los grafos W_D y W_B, no en
el operador.

### II. Condiciones para dualidad simultánea alta
Un nodo i tiene dualidad simultánea alta cuando R*_D_i es
alto Y R*_B_i es alto — cuando fue factor causal central tanto
del daño como del beneficio. Esta condición no es
contradictoria; es la condición del actor con alta centralidad
causal en ambas direcciones del resultado del sistema.
Las condiciones para dualidad simultánea alta son: primero,
que el nodo i esté en ambos grafos — que tenga aristas tanto
en el grafo de daño como en el grafo de beneficio. Esto ocurre
cuando el actor produjo efectos en ambas direcciones:
contribuyó causalmente al daño D y también contribuyó
causalmente al beneficio B. El directivo que diseñó el sistema
de incentivos que produjo el fraude y que también diseñó el
sistema de formación que produjo profesionales competentes
puede tener R*_D alto y R*_B alto.
Segundo: que la posición del nodo i en ambos grafos sea
central — que en el grafo de daño tenga influencia sobre los
nodos que más contribuyeron al daño, y en el grafo de

Metrología Causal
beneficio tenga influencia sobre los nodos que más
contribuyeron al beneficio. Un nodo puede tener muchas
aristas en ambos grafos, pero con pesos bajos, lo que produce
R* bajo en los dos. La dualidad simultánea alta requiere no
solo presencia en ambos grafos sino centralidad genuina en
ambos.

### III. La interpretación ontológica de la dualidad
La dualidad daño-beneficio tiene una interpretación
ontológica en el sistema del paradigma que la matemática
captura, pero no agota. El colapso ontológico — el acto
producido por φ₁ y asumido por φ₂ — tiene efectos en el
mundo que pueden ser positivos, negativos o ambos
simultáneamente. R* y R*_B son las dos caras de la misma
moneda ontológica: describen la centralidad del nodo en los
efectos del sistema con independencia del signo de esos
efectos.
La diferencia filosófica entre R*_D y R*_B no está en el
operador sino en la pregunta que se le hace al sistema. «¿Quién
causó el daño?» y «¿quién generó el beneficio?» son preguntas
distintas sobre el mismo tipo de objeto — la estructura causal
del sistema. El sistema de Prometeo puede responder ambas
con el mismo grado de rigor y el mismo tipo de Declaración
porque el operador es el mismo.
La consecuencia práctica más importante: los sistemas de
justicia que solo tienen instrumentos para la imputación del
daño (R*_D) sin instrumentos para la atribución del mérito
(R*_B) producen una asimetría sistemática que el paradigma
puede corregir. Un directivo que tiene alta R*_D por los
efectos negativos de su gestión y alta R*_B por los efectos
positivos merece una evaluación que considere ambas

Metrología Causal
dimensiones. La dualidad matemática es la condición de
posibilidad de esa evaluación equitativa.

Metrología Causal
