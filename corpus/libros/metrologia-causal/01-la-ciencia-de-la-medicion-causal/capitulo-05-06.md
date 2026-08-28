## PARTE V · Validez y límites de la medición causal

### Capítulo V·6
Protocolos de detección y corrección de
errores
Para cada tipo: señales de presencia, protocolo de corrección y
condición de invalidación total

### I. Principio de detección: coherencia interna del
análisis
Los cuatro tipos de error tienen en común una propiedad que
el protocolo de detección explota: producen incoherencias
internas en el análisis. Un análisis sin errores tiene coherencia
entre sus componentes: la distribución P(Hijos) es consistente
con los valores de S, los valores de S son consistentes con los
rangos de w_ij, los valores de R* son consistentes con el
análisis narrativo del caso, la Declaración es consistente con el
análisis de sensibilidad. Cuando alguno de los cuatro tipos de
error está presente, alguna de esas coherencias se rompe.
El protocolo de detección es por tanto un protocolo de
verificación de coherencia: el analista verifica
sistemáticamente si cada par de componentes del análisis es
coherente entre sí. La verificación de coherencia P(Hijos) —
S detecta el Error Tipo I. La verificación de coherencia S —
R* detecta el Error Tipo II cuando el S alto de un nodo no se

Metrología Causal
refleja en R*_neta bajo, o viceversa. La verificación de
coherencia análisis narrativo — R* detecta el Error Tipo III
cuando el nodo que la evidencia narrativa señala como más
central no tiene el R* más alto. La verificación de coherencia
rangos de peso — escala temporal detecta el Error Tipo IV.

### II. Protocolos de corrección por tipo
La corrección del Error Tipo I requiere relocalizar el Hijo
dominante del nodo afectado usando el protocolo de la
Taxonomía (III·3–III·5), recalibrar S usando la tabla de S por
Hijo (II·10), y recalcular R* con el S corregido. Si la
relocalización requiere ECO porque la localización desde el
expediente es ambigua (III·2), el análisis debe suspenderse
hasta que ECO produzca la localización, o producir la
Declaración con el rango amplio de S que refleja la
incertidumbre en la localización.
La corrección del Error Tipo II requiere revisar la evidencia
que fundamenta el peso de la arista afectada, identificar si el
peso está fuera del rango consistente con esa evidencia, y
ajustarlo al rango correcto. Si el Error Tipo II fue el resultado
de usar el punto central del rango en lugar del rango completo,
la corrección es simplemente expandir el rango y volver a
producir el análisis de sensibilidad. Si el error fue el resultado
de un supuesto erróneo sobre la naturaleza de la influencia
causal (por ejemplo, confundir correlación con causalidad en
la calibración de w_ij), la corrección requiere revisar el
supuesto y reconstruir la arista.
La corrección del Error Tipo III requiere identificar qué nodos
relevantes están fuera de N, añadirlos al grafo con sus aristas
correspondientes, y recalcular todo el análisis. Esta corrección
es la más costosa porque afecta al análisis completo, no solo a
un parámetro. En el análisis forense, la corrección del Error

Metrología Causal
Tipo III puede requerir buscar evidencia adicional sobre el
nodo excluido, lo que a su vez puede requerir acceso a
documentos que no estaban en el expediente original.
La corrección del Error Tipo IV requiere descomponer el
grafo en capas temporales, calcular R* separadamente para
cada capa y declarar los supuestos de conversión entre capas.
Si la corrección no es posible por falta de evidencia sobre la
separación temporal de las influencias, el análisis debe
producir la Declaración C o D, declarando explícitamente que
la escala temporal incorrecta es la condición de validez que no
está satisfecha.

### III. Los errores que invalidan el análisis
completo
Los cuatro tipos de error son corregibles en principio, pero
hay condiciones bajo las cuales la corrección no es posible y el
análisis debe declararse inválido. El Error Tipo III invalida el
análisis completo cuando el nodo excluido tiene R* que,
estimado conservadoramente, sería mayor que el R* del nodo
que el análisis identificó como el de mayor responsabilidad —
y no existe evidencia disponible para incluirlo en el grafo con
la precisión que el estándar de validez del análisis requiere. En
ese caso, el analista no puede producir una Declaración sobre
el nodo de mayor R* porque la información disponible es
insuficiente para determinar si ese nodo es realmente el
primero en el ranking.
El Error Tipo IV invalida el análisis completo cuando las
escalas temporales mezcladas son tan distintas que ningún
supuesto de conversión razonable puede hacerlas comparables
— por ejemplo, cuando el análisis mezcla influencias de siglos
(el diseño colonial de instituciones) con influencias de horas

Metrología Causal
(el acto del ejecutor contemporáneo). En ese caso, el análisis
debe separarse en dos análisis independientes — uno para el
nivel histórico y otro para el nivel contemporáneo — con la
declaración explícita de que los R* de los dos niveles no son
directamente comparables.

Metrología Causal

