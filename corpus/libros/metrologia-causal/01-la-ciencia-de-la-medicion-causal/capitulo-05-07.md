PARTE V · Validez y límites de la medición causal

### Capítulo V·7

### Los límites estructurales I: causalidad

### acumulativa

Cuando ningún nodo es condición suficiente y el daño es el

resultado de contribuciones marginales

### I.  El problema de la causalidad acumulativa

El sistema de Prometeo está diseñado para la causalidad necesaria: el nodo sin el cual D no se habría producido de esa forma específica. Esta definición funciona bien cuando hay un conjunto relativamente pequeño de nodos y cada uno tiene una contribución causal distinguible. Pero hay una clase de sistemas donde la causalidad necesaria individual no existe: los sistemas donde D es el resultado de la contribución marginal de muchos actores, cada uno de los cuales contribuyó en una fracción tan pequeña que ninguno por sí solo es condición necesaria del resultado.

El ejemplo canónico es el daño ambiental acumulativo. Cien empresas vierten contaminantes en un río durante décadas; el nivel de contaminación produce daño al ecosistema y a la salud de las comunidades ribereñas. Ninguna empresa individual es condición necesaria del daño: si la empresa X hubiera dejado de contaminar, el daño habría ocurrido igualmente — las otras

Metrología Causal

noventa y nueve empresas habrían producido un nivel de contaminación suficiente. El criterio de la condición sine qua non no puede aplicarse directamente: R*_X = 0 para todas las X, lo que implica que nadie es responsable de un daño que evidentemente alguien causó.

Este es el límite estructural más importante del sistema: la causalidad acumulativa sin condición necesaria individual es un tipo de sistema donde R* en su formulación estándar no produce resultados interpretables como distribución de responsabilidad. La suma Σᵢ R*_i = 1 se satisface, pero cada R*_i es tan pequeño que la distribución no distingue entre actores con contribuciones distintas de manera significativa.

### II.  La extensión por valores de Shapley

La extensión natural del sistema para el caso de causalidad acumulativa es la utilización de los valores de Shapley de la teoría de juegos cooperativos. El valor de Shapley de un nodo i es la contribución marginal esperada de i al resultado, promediada sobre todos los posibles órdenes en que los nodos pueden unirse al grafo. Formalmente: φ_i = Σ_ {S ⊆ N\{i}} [|S|! (|N|−|S|−1)! /|N|!] × [v (S ∪ {i}) − v(S)], donde v(S) es el «valor» del subconjunto S de nodos (la fracción del daño D que S puede producir por sí solo).

El valor de Shapley tiene la propiedad de eficiencia que el sistema requiere: Σᵢ φ_i = v(N) = 1. La distribución de Shapley distribuye la totalidad del daño entre todos los nodos. Y tiene la propiedad de que φ_i > 0 para todo nodo que tiene contribución marginal positiva — incluso si ese nodo no es condición necesaria individual, su contribución marginal promediada sobre todos los órdenes posibles es positiva y mensurable.

Metrología Causal

El valor de Shapley resuelve el problema de la causalidad acumulativa porque reemplaza la pregunta «¿es i condición necesaria de D?» (cuya respuesta es no para todos los actores en la causalidad acumulativa) con la pregunta «¿cuál es la contribución marginal esperada de i al daño?» (cuya respuesta es positiva y diferenciada para actores con contribuciones distintas). Esta sustitución de la pregunta es filosóficamente legítima en el caso de la causalidad acumulativa: cuando ningún actor es condición necesaria individual, la distribución proporcional de la responsabilidad sobre la base de las contribuciones marginales es la aproximación más cercana a la justicia proporcional que el sistema puede producir.

### III.  Los límites de la extensión por Shapley

La extensión por Shapley tiene sus propios límites que deben declararse explícitamente. El primer límite: la función v(S) — el daño que el subconjunto S puede producir por sí solo — es difícil de estimar empíricamente para sistemas con muchos actores y daño acumulativo. Para el caso del río contaminado con cien empresas, se necesitarían datos sobre cuánto daño produciría cada posible subconjunto de empresas, lo que requiere cien experimentos contrafácticos que en general no son realizables.

El segundo límite: el valor de Shapley presupone que los subconjuntos de actores son comparables — que la contribución marginal de i con el subconjunto S presente tiene el mismo tipo de sentido que la contribución marginal de i con cualquier otro subconjunto. Esta presunción puede fallar cuando los actores tienen roles cualitativamente distintos: la contribución marginal del diseñador del campo con respecto a la contribución de los ejecutores no es del mismo tipo, y promediarlas sobre todos los subconjuntos posibles puede

Metrología Causal

producir una distribución que no refleja la estructura jerárquica de la responsabilidad.

El tercer límite: el valor de Shapley es computacionalmente tratable solo para sistemas de hasta veinte actores aproximadamente. Para el caso de las cien empresas, el cálculo exacto requiere 2^100 términos — computacionalmente inviable. Las aproximaciones estocásticas (muestreo de subconjuntos) son posibles, pero introducen una fuente adicional de incertidumbre en los resultados. El sistema declara este límite como estructural: para sistemas con causalidad acumulativa y más de veinte actores, la distribución exacta de Shapley no está disponible y la distribución aproximada debe declarar explícitamente la incertidumbre de la aproximación.

Notas al capítulo V·7

1 El valor de Shapley fue introducido por Lloyd Shapley en 1953 en el contexto de la teoría de juegos cooperativos (Shapley, L.S. «A Value for n-Person Games», en H.W. Kuhn y A.W. Tucker, eds., Contributions to the Theory of Games, vol. II, Princeton University Press, 1953). Su aplicación a la distribución de responsabilidad ambiental ha sido desarrollada en la literatura de economía ambiental, especialmente en el contexto del análisis de responsabilidad por daños ecológicos colectivos. La referencia central es Ruiz-Aliseda (2004) sobre la responsabilidad proporcional en daños ambientales acumulativos.

Metrología Causal

