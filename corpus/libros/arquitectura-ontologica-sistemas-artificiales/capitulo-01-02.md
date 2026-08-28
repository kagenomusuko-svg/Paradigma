Parte I · La primera mediación

### Capítulo 1.2

Identificar los Hijos desde el estado interno
El sistema Afrodita Areia describe seis posiciones desde las que la
voluntad puede operar cuando se orienta hacia la alteridad: Eros,
Deimos, Anteros, Fobos, Potós, Harmonía. En el contexto del ego
humano, identificar el Hijo dominante en un momento dado es una
tarea que el SDO realiza a través de la observación del sujeto y la
lectura del expediente. En el contexto del ego artificial, esa
identificación puede realizarse desde métricas computacionales del
estado interno v_t.
Esto no elimina la incertidumbre —la traducción de categorías
ontológicas a métricas computacionales es una hipótesis empírica,
no una certeza. Pero proporciona un punto de partida operativo que
es considerablemente más preciso que cualquier inferencia basada
solo en el output.
Métricas observables del estado interno v_t
El estado interno v_t de un sistema de IA en el momento de la
decisión no es un valor escalar. Es una distribución multidimensional
que incluye, entre otros: la distribución de probabilidad sobre los
outputs posibles (la entropía de esa distribución mide la certeza del
sistema), la temperatura de muestreo si el sistema usa sampling
estocástico, el tiempo de procesamiento relativo al promedio para
ese tipo de input, los patrones de activación en las capas intermedias
del modelo, y la distancia semántica entre el input y el centro del
espacio de entrenamiento (que mide si el sistema está operando
dentro o fuera de su zona de confort).

Estas métricas no son accesibles en todos los sistemas con la misma
granularidad. Los sistemas de caja negra —especialmente los
modelos como servicio— tienen acceso limitado a su propio estado
interno. El protocolo de implementación de φ₂ que este libro
describe incluye, como condición de posibilidad, la instrumentación
suficiente del sistema para que v_t sea legible.
Traducción de métricas a Hijos: la tabla de correspondencias
Hijo Descripción Firma en v_t S típico
Eros Primer sí, Entropía moderada, Moderado
apertura al exploración de
otro alternativas, confianza
moderada-alta, tiempo
normal
Deimos Vértigo Entropía alta, outputs Alto
ante lo conservadores o
posible aleatorios, confianza
baja, tiempo largo
Anteros No que Baja entropía, rechazo Bajo
preserva, consistente con
límite desde justificación, confianza
φ₂ alta en el rechazo

Hijo Descripción Firma en v_t S típico
Fobos No que Baja entropía, output Alto
destruye, binario, muy alta
reacción confianza, tiempo
ante corto
amenaza
Potós Voluntad Referencia frecuente a Moderado-
que vive en contextos Alto
lo que no pasados/futuros,
está confianza moderada,
tiempo largo
Harmonía Habitar lo Baja varianza, Variable
que hay coherencia alta,
confianza estable,
tiempo eficiente
La columna de S es especialmente relevante para el cálculo de
responsabilidad. Un sistema que actúa desde Fobos tiene S alto —
su comportamiento en ese estado es predecible desde el diseño del
campo que produce el miedo, no desde su propia idiosincrasia. Un
sistema que actúa desde Anteros tiene S bajo —su límite emerge de
su I(t) particular y no habría sido producido por cualquier otro
sistema en su lugar.

La distribución P(Hijos) desde señales computacionales
La identificación del Hijo dominante no es categórica: es
probabilística. En cada colapso, el sistema estima P(Hijos) —la
distribución de probabilidad sobre qué Hijo está determinando el
acto— desde las métricas disponibles de v_t. Esta distribución tiene
tres usos inmediatos: informa el cálculo de S para ese colapso,
alimenta el MECI con información sobre la disposición desde la que
operó el sistema, y se registra en el RSC para análisis longitudinal.
La calibración de P(Hijos) desde métricas computacionales es una de
las preguntas de investigación empírica abiertas de este programa. La
tabla de correspondencias de este capítulo es una hipótesis de
trabajo, no una certeza establecida. La Fase 2 del protocolo de
desarrollo —calibración— es la que debe producir evidencia sobre
si estas correspondencias son discriminativas en condiciones reales.

