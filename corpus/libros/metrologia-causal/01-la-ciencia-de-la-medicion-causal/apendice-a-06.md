APÉNDICES · Demostraciones formales de propiedades
Apéndice A·6
El análisis de sensibilidad: algoritmo
completo y criterios de cobertura
Del hipercubo de parámetros a la función de robustez y la
Declaración

### I. El algoritmo completo en seis pasos
El algoritmo de análisis de sensibilidad es la transformación
del espacio de parámetros {W(w): w ∈ Π_ij [a_ij, b_ij]} en la
función de robustez ρ: [0,1] → [0,1] que mapea cada umbral
de cobertura del hipercubo en el porcentaje del hipercubo
donde el ranking es estable.
Paso 1 Construir el hipercubo Π = Π_ij [a_ij, b_ij]
desde la hoja de calibración. Identificar la dimensión m
del hipercubo (igual al número de aristas con a_ij < b_ij
— las aristas con incertidumbre en el peso). Las aristas
con a_ij = b_ij tienen peso determinado y no
contribuyen a la dimensión del hipercubo.
Paso 2 Seleccionar los puntos de evaluación.
Obligatorio: todas las 2ᵐ esquinas del hipercubo (cada
arista en su valor mínimo o máximo). Obligatorio: el
punto central (cada arista en su midpoint (a_ij + b_ij)

Metrología Causal
/2). Opcional pero recomendado: muestreo uniforme
aleatorio del interior del hipercubo, con 200 puntos
para la Declaración B, 500 para la Declaración A. Si m
> 15, usar solo el muestreo aleatorio (las esquinas son
2¹⁵ = 32,768 puntos, computacionalmente tratable pero
lento para análisis en tiempo real).
Paso 3 Para cada punto w ∈ Π seleccionado: construir
la matriz W(w) con w_ij = el valor del punto en la
dimensión (i, j). Verificar que W(w) satisface las
condiciones de Perron-Frobenius (irreducibilidad y
aperiodicidad — que son independientes de los valores
específicos de los pesos si el grafo tiene la estructura
topológica correcta). Calcular el eigenvector principal
normalizado v*(w) = R*(w) usando el método de
potencias. Registrar el ranking σ(w) = orden de los
nodos por R*(w) decreciente.
Paso 4 Identificar los puntos de quiebre: los puntos w
donde σ(w) ≠ σ(w_central). Para cada punto de quiebre,
registrar: qué aristas tienen valores que difieren del
punto central (las aristas «críticas» para ese punto de
quiebre), en qué dirección difieren (hacia el mínimo o el
máximo), y cuánto difieren del midpoint.
Paso 5 Calcular la función de robustez. Para cada par
de nodos (i, j) con i ≠ j: ρ_{ij}(θ) = fracción de puntos
evaluados donde R*_i > R*_j. Si ρ_{ij} (1) ≥ θ, el
ranking de i sobre j es robusto al nivel θ. La función de
robustez global del ranking completo es ρ(θ) =
min_{ij} ρ_{ij}(θ) — el porcentaje de puntos donde
todo el ranking es estable.
Paso 6 Producir la Declaración según el criterio de la
función de robustez. Declaración A: ρ (1.00) = 1.00 (el
ranking es estable en todos los puntos evaluados,
incluyendo todas las esquinas). Declaración B: ρ (0.90)

Metrología Causal
≥ 1.00 (el ranking es estable en al menos el 90% de los
puntos evaluados). Declaración C: ρ (0.70) ≥ 1.00 (al
menos el 70% de los puntos). Declaración D: ρ (0.70)
< 1.00 (el ranking no es estable ni en el 70% de los
puntos evaluados).

### II. Los criterios de cobertura del espacio de
parámetros
La cobertura del espacio de parámetros determina la validez
de la Declaración. Una Declaración A sobre cobertura
insuficiente del hipercubo puede ser incorrecta: el ranking
puede ser inestable en puntos no evaluados. El criterio de
cobertura establece cuántos puntos evaluar para que la
Declaración sea válida con alta probabilidad.
Para la Declaración A: la cobertura mínima es la evaluación de
todas las esquinas del hipercubo más el punto central. Si m ≤
20 (grafos de hasta 20 aristas con incertidumbre), las 2²⁰ =
1,048,576 esquinas son computacionalmente tratables en
cómputo moderno (menos de un minuto). Si m > 20, la
evaluación de todas las esquinas no es práctica; usar muestreo
estratificado de esquinas (evaluación de todas las
combinaciones de los dos extremos para las m/2 aristas más
sensibles, más muestreo aleatorio para las demás).
Para la Declaración B: la cobertura estándar es las esquinas
más 200 puntos uniformes aleatorios del interior. Esta
cobertura es suficiente para detectar inestabilidad en el interior
del hipercubo con alta probabilidad. La probabilidad de no
detectar una zona de inestabilidad de volumen superior al 5%
del hipercubo con 200 puntos aleatorios es menor de (0.95) ²⁰⁰
≈ 0.00035 — menos de un punto por mil.

Metrología Causal
Para la Declaración C: la cobertura estándar es las esquinas
más 500 puntos uniformes aleatorios. Esta cobertura permite
estimar la función de robustez ρ(θ) con error estándar menor
de 0.02 para cualquier θ (por la ley de los grandes números con
n = 500).

### III. La función de robustez y su relación con los
puntos de quiebre
La función de robustez ρ(θ) y la distribución de puntos de
quiebre son dos representaciones de la misma información
sobre la estabilidad del ranking. La función ρ(θ) describe cuán
robusto es el ranking en términos de cobertura del hipercubo.
Los puntos de quiebre describen dónde en el hipercubo se
produce la inestabilidad.
La relación entre las dos representaciones: si todos los puntos
de quiebre están en las esquinas extremas del hipercubo (en
los valores de peso que están a más de 0.8 de amplitud del
midpoint), la función ρ es alta para θ ≤ 0.8 y cae solo para θ
cercano a 1. Eso corresponde a la Declaración B: el ranking es
estable en la gran mayoría del hipercubo, pero no en los
extremos más alejados del midpoint. Si los puntos de quiebre
están distribuidos uniformemente por el hipercubo, la función
ρ decrece linealmente desde 1 en θ = 0 hacia valores bajos para
θ alto. Eso corresponde a la Declaración C o D.
La geometría de los puntos de quiebre es la información
estratégica más valiosa para el adversario y para el analista. El
adversario que identifica que los puntos de quiebre se
concentran en la región donde w_FRO→ECP es bajo (la
arista tiene valor en el extremo mínimo de su rango) sabe que
su argumento más fuerte es demostrar que la influencia de
FRO sobre ECP era menor de lo que el midpoint sugiere. El

Metrología Causal
analista que identifica esa misma geometría sabe que la
evidencia sobre esa arista específica es el punto más vulnerable
de su análisis y debe ser reforzada antes de la presentación
adversarial.
Los dos usos estratégicos del análisis de sensibilidad
Uso analítico (antes de la presentación): identificar qué aristas
tienen puntos de quiebre en el interior del hipercubo para
obtener evidencia adicional que estreche esos rangos antes de
presentar el análisis. El objetivo es elevar la Declaración de C
a B, o de B a A, con evidencia real — no ajustando los rangos
artificialmente.
Uso adversarial (durante la presentación): el reporte de
sensibilidad declara los puntos de quiebre y la evidencia que
el adversario necesitaría para que esos puntos sean relevantes.
El objetivo es transformar la disputa de 'tu número vs. el mío'
a 'qué dice la evidencia sobre la intensidad de la influencia
causal entre i y j' — que es el debate correcto.
Notas al apéndice A·6
1 El muestreo uniforme aleatorio del hipercubo para la cobertura del
análisis de sensibilidad es una instancia de la técnica de Monte Carlo para
la evaluación de funciones sobre espacios de alta dimensión. La garantía
probabilística de cobertura (que la probabilidad de no detectar una zona
de inestabilidad de volumen V es (1−V) ⁿ para n puntos aleatorios) es
una propiedad estándar del muestreo aleatorio. Para aplicaciones
forenses donde la certeza es especialmente importante, la cobertura
mínima recomendada es n = 1,000 puntos aleatorios más las esquinas,
lo que garantiza que zonas de inestabilidad de volumen ≥ 1% sean
detectadas con probabilidad ≥ 0.9999.
2 La función de robustez ρ(θ) definida en este apéndice es una función
monótonamente decreciente en θ: ρ (0) = 1 (el 100% del hipercubo tiene
un ranking) y ρ (1) ≤ 1 (el porcentaje del hipercubo con el ranking del
punto central). La Declaración A corresponde a ρ (1) = 1; la Declaración
B a ρ (1) ≥ 0.90; la Declaración C a ρ (1) ≥ 0.70; la Declaración D a ρ
(1) < 0.70. La función ρ puede graficarse para mostrar exactamente

Metrología Causal
cómo varía la robustez con el umbral, lo que provee información más
rica que las cuatro categorías discretas de la Declaración.

Metrología Causal

