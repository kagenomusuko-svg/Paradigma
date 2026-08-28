## PARTE VI · Los documentos del análisis: producción e interpretación

### Capítulo VI·10
La Declaración de robustez: cómo leerla
e interpretarla
Lo que cada Declaración dice sobre el caso — y lo que nunca dice
sobre el analista

### I. La Declaración describe el caso, no al analista
El error de interpretación más frecuente de la Declaración es
confundir su objeto: la Declaración describe el estado de la
evidencia del caso, no la calidad del trabajo del analista. Una
Declaración C no dice que el analista hizo un análisis débil —
dice que la evidencia disponible sobre el caso es insuficiente
para producir una conclusión robusta. Un analista excelente
trabajando con evidencia insuficiente produce una
Declaración C. Un analista mediocre trabajando con evidencia
abundante y clara puede producir una Declaración A.
La misma lógica aplica a la Declaración A: no dice que el
analista es brillante — dice que el caso tiene una estructura
causal suficientemente clara para que la conclusión sea robusta
ante cualquier interpretación razonable de la evidencia. Los
casos con estructuras causales simples (pocos nodos, evidencia
abundante, influencias claramente documentadas) tienden a
producir Declaraciones A, aunque el análisis sea básico. Los

Metrología Causal
casos con estructuras causales complejas (muchos nodos,
evidencia escasa, influencias a través de mecanismos
informales) tienden a producir Declaraciones B o C, aunque el
análisis sea sofisticado.

### II. Lo que cada Declaración dice sobre la
estructura del caso
La Declaración A dice que la estructura causal del caso es clara
y que la distribución de responsabilidad que el análisis produce
es robusta. Estructuralmente: hay un nodo de clara mayor
centralidad que los demás, y esa mayor centralidad es estable
ante cualquier variación razonable en la intensidad de las
influencias. El caso Altamirano tiene Declaración A: FRO
tiene mayor R*_neta que cualquier otro nodo en todos los
escenarios explorados, incluyendo el escenario donde la arista
ECP→BM tiene su peso mínimo plausible.
La Declaración B dice que la estructura causal del caso tiene
un candidato claro al primer lugar en el ranking pero que la
margen de dominancia no es suficiente para ser robusta en
todos los extremos. Estructuralmente: hay un nodo
probablemente más central que los demás, pero existe alguna
combinación de supuestos extremos bajo la cual otro nodo lo
desplaza. La Declaración B es el diagnóstico de un caso donde
el nodo de mayor R* es el correcto con alta probabilidad, pero
no con certeza absoluta.
La Declaración C dice que la estructura causal del caso es
ambigua en la distribución de R*: hay varios candidatos
plausibles para el primer lugar y la evidencia disponible no es
suficiente para discriminar entre ellos. Estructuralmente: los
nodos tienen rangos de R* que se solapan significativamente.
La Declaración D dice que la ambigüedad es tan alta que el

Metrología Causal
análisis no puede discriminar en absoluto — los rangos de R*
de los distintos candidatos se solapan en toda su extensión.

### III. La Declaración como instrumento de
comunicación de la incertidumbre
La Declaración es el instrumento más eficiente que el sistema
produce para comunicar la incertidumbre del análisis en forma
que sea procesable por actores no técnicos. Un tribunal no
puede procesar «R*_FRO ∈ [0.35, 0.41] con intervalo de
confianza del 95%». Puede procesar «con cualquier
interpretación razonable de la evidencia, FRO tiene mayor
responsabilidad causal que cualquier otro actor en el sistema»
— que es exactamente lo que la Declaración A dice.
El principio de equivalencia semántica: la Declaración A es
semánticamente equivalente al enunciado «el ranking es
robusto en el 100% del espacio de parámetros razonables»
pero lo formula en el lenguaje que el foro puede usar
directamente. Esta equivalencia es la razón por la que la
Declaración es el producto final del análisis — no el rango
numérico de R*, no el porcentaje de estabilidad del reporte de
sensibilidad. La Declaración traduce la información técnica del
reporte al lenguaje de la conclusión procesable.

Metrología Causal

