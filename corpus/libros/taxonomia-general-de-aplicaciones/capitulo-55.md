PARTE VIII · Deporte y Rendimiento

## Capítulo 55

### Valoración de jugadores y distribución

### del éxito deportivo

Organ.  Estru.  Model.  Educa.  Crisi.

Para el mediador que busca precisión · Cómo usar este capítulo

Este capítulo es Compilación directa del capítulo 17 de El cálculo de la responsabilidad (Deportes y valor de contribución). Aplica los instrumentos del sistema — R*_B, S_B, Δ_B — al dominio del análisis deportivo: la valoración de jugadores individuales, la distribución del éxito colectivo entre los contribuyentes, y la negociación salarial basada en la contribución causal idiosincrática. El dominio deportivo es el único de la Taxonomía donde el sistema puede calibrarse con datos estadísticos ricos y con el experimento natural de las ausencias del jugador.

La idea más contraintuitiva del capítulo: los jugadores más famosos de la historia tienden a tener S_B más alta de lo que la narrativa popular sugiere. La razón: un equipo genuinamente excelente tiene cierta capacidad de generar el resultado independientemente del individuo específico. La contribución idiosincrática — la fracción del resultado que ese jugador específico y ningún otro en su posición habría producido — es lo que el sistema mide como CI (Contribución Idiosincrática) = R*_B × (1 − S_B).

### §1  Descripción del subcampo: R*_B en el dominio deportivo

### En el dominio deportivo, el evento final es positivo: el triunfo, el campeonato, el resultado que el equipo y sus patrocinadores

Taxonomía General de Aplicaciones

buscaban. R*_B invierte la dirección respecto a R*_D: en lugar de distribuir la responsabilidad sobre el daño, distribuye el mérito sobre el triunfo. La matemática es idéntica — iteración de potencia sobre el grafo de contribución — pero el nodo final (Nf) es el éxito colectivo, y todos los nodos que contribuyen positivamente a él tienen R*_B > 0.

La singularidad del dominio deportivo respecto a los demás dominios de la Taxonomía es que tiene acceso a dos tipos de evidencia que en los otros dominios no existen. La evidencia estadística avanzada — Expected Goals (xG), VAEP, Win Shares, PER, Defensive Impact — permite estimar la contribución de cada jugador al resultado con relativa precisión desde los datos observables del partido. Y el experimento natural de las ausencias — los períodos en que el jugador no estuvo disponible por lesión, suspensión o convocatoria a la selección — provee el contrafáctico que establece S_B con evidencia histórica directa: ¿cómo rindió el equipo sin este jugador específico?

Los tres instrumentos centrales del dominio deportivo R*_B(jugador_i): la fracción del triunfo causalmente atribuible al jugador i. Se calcula como el eigenvector dominante del grafo de contribución, donde los nodos son los jugadores, el sistema de juego, el cuerpo técnico y las condiciones del contexto. S_B(jugador_i): la fungibilidad deportiva del jugador. ¿Habría ganado el equipo sin este jugador? S_B alto significa que el equipo tenía la capacidad de ganar con un reemplazante de nivel equivalente. S_B bajo significa que ese jugador específico era condición necesaria del resultado. S_B_hist = 1 − |P(victoria|jugador) − P(victoria|sin_jugador) |. CI (Contribución Idiosincrática) = R*_B × (1 − S_B): la fracción del resultado que ese jugador específico y ningún otro en su posición habría producido. Es el instrumento más relevante para la negociación salarial y la valoración de transferencias — no el R*_B total, sino la CI que mide la indispensabilidad real. Δ_B del club = B_total × CI − salario_actual. Δ_B > 0 significa que el club extrae valor no compensado del jugador — argumento para el aumento

Taxonomía General de Aplicaciones

salarial. Δ_B < 0 significa que el club paga más de lo que la CI justifica — año de inversión del contrato.

### §2  Escala de evidencia Dep0–Dep8

Tipo de evidencia en

Descripción Rango

Nivel

w

el dominio

deportivo

Dep1 Métricas estadísticas avanzadas de evento (xG, VAEP, pases progresivos, defensive actions) con tracking data de precisión + análisis de ausencias con muestra ≥ 30 partidos

Las métricas de evento calculadas desde los datos de tracking (posición de todos los jugadores a 25 fps) que capturan la contribución física de cada jugador en cada segundo del juego. El análisis de ausencias con muestra de al menos 30 partidos produce estimadores robustos de S_B con intervalos de confianza aceptables.

[0.72, 0.90]

Dep2 Métricas estadísticas estándar verificadas (goles, asistencias, pases clave, xG) + análisis de ausencias con muestra de 15–30 partidos + análisis de rendimiento del equipo en períodos comparables

Las métricas estadísticas estándar verificadas independientemente, con análisis de ausencias y análisis de rendimiento del equipo en períodos comparables (misma fase de la temporada, rival equivalente).

[0.60, 0.78]

Taxonomía General de Aplicaciones

Tipo de evidencia en

Descripción Rango

Nivel

w

el dominio

deportivo

Dep3 Análisis estadístico de dos o más analistas independientes con metodologías distintas que convergen en la estimación de R*_B y S_B

La convergencia de dos análisis estadísticos independientes con metodologías distintas aumenta el peso de la evidencia respecto al análisis único.

[0.50, 0.68]

Dep4 Métricas estadísticas estándar sin análisis de ausencias + evaluación cualitativa de scouting

Las estadísticas estándar sin el análisis de ausencias que establece S_B, combinadas con la evaluación cualitativa del scouting del club.

[0.36, 0.54]

Dep5 Análisis de scouting cualitativo sin métricas estadísticas avanzadas

La evaluación del rendimiento del jugador basada en la observación experta sin métricas estadísticas que la respalden.

[0.18, 0.36]

Dep6 Valoración de mercado y comparación con jugadores equivalentes

La valoración del jugador basada en la comparación con el precio de mercado de jugadores en posiciones y perfiles similares, sin análisis estadístico específico de su contribución.

[0.08, 0.22]

Dep0 Análisis Dep1/Dep2 que establece que el jugador no tuvo R*_B positivo verificable sobre el

El análisis estadístico que establece que la contribución causal del jugador no fue positiva sobre el resultado analizado — el equipo rendía igual o mejor en su ausencia.

w = 0.00

Taxonomía General de Aplicaciones

Tipo de evidencia en

Descripción Rango

Nivel

w

el dominio

deportivo

resultado analizado

### §3  Las herramientas del análisis de contribución deportiva

### §3.1  El grafo de contribución causal al resultado deportivo

El grafo de contribución al resultado deportivo tiene una estructura diferente a los grafos de daño de los capítulos anteriores. Todos los nodos que contribuyen positivamente al triunfo tienen R*_B > 0. Los nodos que contribuyeron negativamente — los errores, las lesiones, las expulsiones — tienen R*_B < 0 en esa acción específica, que se incorpora al cálculo global del jugador.

R*_B típico

Nodo del

en campeonatos

S_B típico Fuente de evidencia para w

grafo deportivo

de largo

plazo

Jugadores individuales

Distribución variable. El jugador de mayor CI en un equipo élite suele tener CI entre 8–18% del triunfo colectivo — porque el deporte es colectivo y la varianza es alta. Los

Alta [0.45– 0.75] para la mayoría. Baja-moderada [0.20–0.45] solo para jugadores únicos en su posición en el equipo.

xG, VAEP, pases progresivos, acciones defensivas. Métricas de impacto en P(victoria). Análisis de ausencias.

Taxonomía General de Aplicaciones

R*_B típico

Nodo del

en campeonatos

S_B típico Fuente de evidencia para w

grafo deportivo

de largo

plazo

jugadores «estrella» raramente superan el 20% de CI genuina.

Sistema de juego / táctica

8–18% en campeonatos donde la táctica fue diferenciadora. La táctica determina el contexto en el que las contribuciones individuales son posibles.

Moderada [0.40–0.65]: sistemas similares son replicables por otros entrenadores, aunque el diseño específico puede ser idiosincrático.

Análisis de rendimiento con distintas alineaciones. Comparación de rendimiento antes/después de cambios tácticos.

Cuerpo técnico (entrenador)

8–15% en campeonatos de largo plazo. En partidos individuales, las decisiones del entrenador (sustituciones, ajustes tácticos en el descanso) pueden ser determinantes.

Moderada [0.35–0.60]: la calidad del entrenador tiene componentes idiosincráticos (el diseñador del sistema táctico específico) y genéricos (los entrenadores de nivel equivalente producirían resultados similares con ese plantel).

Historial de resultados con y sin el entrenador. Eficacia documentada de las sustituciones. Análisis de los ajustes tácticos en partidos.

Taxonomía General de Aplicaciones

R*_B típico

Nodo del

en campeonatos

S_B típico Fuente de evidencia para w

grafo deportivo

de largo

plazo

Condiciones del contexto (localía, árbitro, condiciones climáticas, cansancio del rival)

5–15% según el contexto específico.

Muy alta [0.75–0.95]: las condiciones del contexto son independientes de los actores del equipo.

Análisis estadístico de la ventaja de localía del equipo. Análisis de rendimiento en distintas condiciones.

### §3.2  Los tres métodos de estimación de S_B

El índice S_B puede estimarse con tres métodos distintos que el análisis debe combinar para producir un estimador robusto. Los tres métodos producen rangos que se ponderan según la calidad y la cantidad de la evidencia disponible.

Método Descripción

operativa Limitación S_B resultante

Método 1: Compara ción histórica de ausencia s

Se comparan los resultados del equipo cuando el jugador estuvo disponible versus cuando no (por lesión, suspensión o selección). S_B_hist = 1 − |P(victoria|jug ador) − P(victoria|sin_j ugador) |. Si la diferencia en la tasa de victorias es pequeña, S_B es alta. Si la diferencia es

Las ausencias pueden no ser una muestra representativa: el jugador puede haberse lesionado en partidos contra rivales difíciles o en períodos de fatiga del equipo. Se necesita una muestra de al menos 15 partidos sin el jugador para que el

S_B ∈ [0, 1]. Es el método más directo y de mayor peso cuando la muestra es suficiente.

Taxonomía General de Aplicaciones

Método Descripción

operativa Limitación S_B resultante

grande, S_B es baja.

estimador sea robusto.

Método 2: Shapley deportiv o

El valor de Shapley distribuye la contribución al triunfo entre los jugadores considerando todas las posibles composiciones del equipo. φ_B_i = contribución marginal promedio de i sobre todas las posibles coaliciones del equipo. Captura si la contribución del jugador es mayor cuando sus compañeros son más fuertes o más débiles (complementari edad).

Computaciona lmente intensivo para planteles grandes. Requiere estimar v(S) para cada coalición posible, lo que para un equipo de 11 jugadores implica 2^11 = 2048 coaliciones posibles. Se aproxima con métodos de Monte Carlo.

φ_B_i ∈ [0, 1] con Σ_i φ_B_i = R*_B_total. El Shapley captura complementariedade s que el eigenvector ordinario no capta.

Método 3: Métricas estadístic as avanzada s (VAEP, xG, Win Shares)

Las métricas de contribución avanzadas estiman la contribución de cada acción del jugador al resultado final. S_B estadístico se estima desde la comparación del nivel de las métricas del jugador con el

Las métricas estadísticas capturan muchas, pero no todas las contribucione s: el líder del vestuario, el defensa que intimida a los delanteros rivales sin hacer más recuperacione

S_B estadístico = 1 − (métricas_jugador − métricas_mejor_ree mplazante) / métricas_jugador.

Taxonomía General de Aplicaciones

Método Descripción

operativa Limitación S_B resultante

de sus posibles reemplazantes: si los reemplazantes de nivel equivalente están fácilmente disponibles en el mercado, S_B es alta.

s, el jugador que libera a un compañero. Estas contribucione s no estadísticas pueden ser relevantes.

§3.3  Δ_B como herramienta de negociación salarial

El Δ_B del jugador en relación con el club es la diferencia entre la fracción del B_total del triunfo que el jugador causó y la fracción que recibe. El argumento de negociación tiene tres componentes que el analista debe calcular y el agente debe presentar.

B_total del club = premios competitivos + ingresos de taquilla + contratos de televisión + derechos de imagen +

valorización del plantel salario_justo_jugador = B_total × CI_jugador = B_total ×

R*_B × (1 − S_B) Δ_B_club = B_total × CI_jugador − salario_actual Δ_B_club > 0: el club extrae valor no compensado del jugador — argumento para el aumento salarial. Δ_B_club = 0: la compensación es proporcional a la contribución causal idiosincrática. Δ_B_club < 0: el club paga más de lo que la CI justifica en ese año — año de inversión del contrato que se compensará en los años de peak del jugador. El argumento de negociación basado en Δ_B es más poderoso que el argumento basado solo en comparación de mercado porque conecta el salario específicamente con el beneficio causal que ese jugador produce para ese club. Un club puede replicar el argumento de mercado señalando que el jugador podría ser reemplazado por otro con igual sueldo. No puede replicar el

Taxonomía General de Aplicaciones

argumento de Δ_B cuando el análisis de ausencias documenta que el equipo rinde significativamente peor sin él.

### §3.4  Los cuatro predictores de rendimiento prospectivo

El análisis de R*_B tiene su mayor valor operativo en la predicción prospectiva: estimar la contribución futura de un jugador antes de negociar su contrato de renovación o su transferencia. Los cuatro predictores son instrumentos derivados de R*_B y S_B que el analista puede calcular con los datos de las dos o tres temporadas previas del jugador.

Predictor Descripción operativa Aplicación

principal

P1: Mapa de fragilidad del equipo

Para cada jugador del plantel: ΔP(victoria|ausencia_i) = −CI_i × (1 − calidad_reemplazante_disponible). El mapa de fragilidad muestra qué posición del plantel produce la mayor caída esperada en P(victoria) ante una ausencia. El jugador de mayor fragilidad puede no ser el de mayor R*_B: si tiene un reemplazante de calidad equivalente (S_B alta), su ausencia no es crítica.

Planificación de plantilla antes del mercado de transferencias. Identificación de las posiciones de mayor prioridad para refuerzo. Análisis de riesgo para el seguro de lesiones.

P2: Arbitraje de transferencias (Valor CI)

Valor_arbitraje = (CI_proyectada × B_total_esperado) − precio_mercado − coste_salarial. Un jugador con Valor_arbitraje > 0 está infravalorado por el mercado respecto a su contribución causal proyectada en ese equipo específico. El análisis de CI calibra la contribución para el equipo comprador específico: un mediocampista creativo puede tener CI alta en un equipo de posesión y CI baja en un equipo de contraataque.

Decisiones de fichaje en el mercado de transferencias. Identificación de ineficiencias del mercado.

Taxonomía General de Aplicaciones

Predictor Descripción operativa Aplicación

principal

P3: Curva de valor del jugador en el tiempo

R*_B(t) = R*_B_peak × f (t − t_peak), donde f modela el ciclo de vida del rendimiento. El peak ocurre entre los 25 y 29 años para la mayoría de los jugadores de campo (el portero tiene un peak más tardío y un declive más lento). La CI decrece en el declive porque los reemplazantes se hacen comparables. El año de inversión del contrato ocurre cuando CI × B_total < salario_contratado.

Diseño de los contratos plurianuales. Identificación del año de inversión. Planificación de la renovación óptima.

P4: Composición óptima del plantel dado el presupuesto

max Σ_i CI_i × w_i sujeto a Σ_i (precio_mercado_i + salario_i) ≤ presupuesto, donde w_i es el factor de complementariedad del jugador con los titulares actuales. El problema de optimización puede resolverse con algoritmos greedy o con búsqueda estocástica cuando el espacio de posibilidades es grande.

Optimización del presupuesto de fichajes. Identificación de las combinaciones de jugadores que maximizan la CI total por euro invertido.

### §4  Casos resueltos

### Caso A — Brasil en el Mundial de México 1970: R*_B de Pelé vs. el equipo

El Brasil de 1970 es considerado por muchos historiadores del fútbol el mejor equipo de la historia. Su convocatoria incluía a Pelé, Gerson, Jairzinho, Tostão y Rivelino. El Brasil de 1962 — sin Pelé desde el segundo partido por lesión — también fue campeón del mundo. Esa comparación produce la pregunta más directa del capítulo en términos del sistema: ¿cuál era el R*_B de Pelé en el triunfo de Brasil 1970? La evidencia de 1962 sugiere que Brasil tenía un equipo capaz de ganar el campeonato sin él.

Taxonomía General de Aplicaciones

Nodo Jugador/Factor R*_B S_B Análisis

N1 Pelé (número 10, figura global)

~18% 0.45 S_B moderada documentada por el experimento natural de 1962: Amarildo reemplazó a Pelé con eficacia y Brasil fue campeón. La S_B de Pelé en 1970 era mayor que la de Gerson porque había más jugadores en el mundo capaces de replicar parte de su función que la de Gerson. CI = 18% × (1 − 0.45) = 9.9%. Pelé era el más famoso pero no el más indispensable en el sentido causal.

N2 Gerson (mediocampo, creador)

~14% 0.35 S_B baja: pocos jugadores del mundo tenían su visión de juego y su capacidad de conducir el tempo del Brasil de 1970 desde el mediocampo. CI = 14% × 0.65 = 9.1% — comparable a la de Pelé en CI aunque menor en R*_B.

N3 Jairzinho (extremo goleador)

~13% 0.40 7 goles en 6 partidos incluyendo la final. CI = 13% × 0.60 = 7.8%.

N4 Tostão (falso nueve)

~11% 0.42 Su capacidad de crear espacios para Pelé y Jairzinho era idiosincrática. CI = 11% × 0.58 = 6.4%.

N5 Rivelino (extremo zurdo / mediocampo)

~9% 0.48 Zurdo de calidad técnica excepcional. CI = 9% × 0.52 = 4.7%.

Taxonomía General de Aplicaciones

Nodo Jugador/Factor R*_B S_B Análisis

N6 Sistema táctico / entrenador Zagallo

~14% 0.45 El sistema 4-2-2-2 de Zagallo, que permitía la libertad de movimiento de los atacantes manteniendo la solidez defensiva, fue una innovación táctica del período. CI = 14% × 0.55 = 7.7%.

N7 Calidad del plantel de reserva

~8% 0.85 S alto: la profundidad del plantel era sistémica, no idiosincrática.

N8 Condiciones del contexto

~13% 0.88 Localía relativa en México, altitude del estadio, organización de la FIFA. S muy alta.

El resultado central del análisis: la CI de Pelé (9.9%) es comparable a la de Gerson (9.1%) y algo superior a la del sistema táctico de Zagallo (7.7%). Pelé no era el nodo dominante del grafo — era el más famoso, pero la distribución de la CI era relativamente homogénea entre los tres o cuatro jugadores principales y el entrenador. La proposición del sistema: la grandeza de ese Brasil era colectiva en un sentido técnicamente preciso — ningún nodo individual dominaba la distribución de CI.

Valores de Shapley deportivo para los cinco atacantes principales (estimación Monte Carlo con 10.000 iteraciones): Pelé 18.2%, Gerson 16.4%, Jairzinho 14.8%, Tostão 12.1%, Rivelino 10.9%. La distribución Shapley es más homogénea que la narrativa popular — que tiende a concentrar el mérito en Pelé — porque capta la complementariedad entre los jugadores: cada uno de ellos contribuye más cuando los demás están presentes.

Taxonomía General de Aplicaciones

### Caso B — Negociación salarial con Δ_B: el mediocampista subpagado

Mediocampista central de 26 años en un club de primera división europea. Tres temporadas en el club: dos títulos de liga, tres clasificaciones a fase de grupos de Champions League, dos semifinales de Copa. El club le ofrece 3.5M€/año en la renovación. El análisis establece si es justo.

Componente

del análisis Estimación Fuente de evidencia

B_total del club en las tres temporadas

Premio por ganar la liga: 8M. Premios de Champions (tres clasificaciones + avances): 45M. Incremento en derechos de televisión: 12M. Incremento en contratos de patrocinio atribuible al éxito: 18M. Valorización del valor de mercado del club: 35M estimado. Total: ~118M€ en tres temporadas.

Reportes financieros del club. Datos de la UEFA sobre distribución de premios. Comparación de contratos de patrocinio pre/post período.

R*_B del jugador

Método estadístico: VAEP del jugador / VAEP_total_equipo = 14%. Método contrafáctico: [P (clasif. Champions|con) − P (clasif. |sin)] / P (clasif. |con) = (0.90 − 0.65) / 0.90 ≈ 28%. Promedio ponderado con mayor peso al método contrafáctico: R*_B ≈ 20%.

Datos de VAEP de las tres temporadas. Análisis de las 8 semanas de baja por lesión en la segunda temporada.

Taxonomía General de Aplicaciones

Componente

del análisis Estimación Fuente de evidencia

S_B del jugador

8 semanas de ausencia por lesión: tasa de victorias del equipo cayó del 74% al 51%. S_B_hist = 1 − |0.74 − 0.51| = 0.77. El equipo rendía significativamente peor sin él, pero no de manera catastrófica — S_B moderada-alta.

Base de datos de resultados del equipo. Partidos de las 8 semanas de ausencia.

CI y salario justo

CI = R*_B × (1 − S_B) = 0.20 × (1 − 0.77) = 0.046. Pero con el método contrafáctico calibrado por la caída en P(victoria): CI_ajustada ≈ 0.036 (36 × 10^-3). Salario_justo = B_total_por_año × CI_ajustada = (118M/3) × CI. Con B_total/año ≈ 39.3M€: salario_justo ≈ 39.3M × 0.109 ≈ 4.25M€/año.

Combinación de métodos estadístico y contrafáctico.

Δ_B del club bajo distintos escenarios

Salario actual (2.8M): Δ_B_club = 4.25M − 2.8M = +1.45M/año (el club extrae valor no compensado). Oferta del club (3.5M): Δ_B_club = 4.25M − 3.5M = +0.75M/año (reduce el Δ pero no lo elimina). Salario

Calculado a partir del B_total estimado y la CI_ajustada.

Taxonomía General de Aplicaciones

Componente

del análisis Estimación Fuente de evidencia

justo (4.25M): Δ_B_club ≈ 0.

Estrategia de negociación del agente: presentar el B_total calculado (118M€ en tres temporadas), el R*_B estimado (20%, documentado con las estadísticas de las 8 semanas de ausencia), y el salario justo resultante (4.25M€). Si el club no acepta el marco analítico, el agente puede señalar que el propio período de lesión del jugador prueba su contribución con evidencia interna del club: la caída del 23 puntos porcentuales en la tasa de victorias durante las 8 semanas de baja es el experimento natural más limpio disponible. La contrapropuesta del agente en 4.5M€ — ligeramente superior al salario justo — deja margen de negociación hacia 4.0– 4.25M€.

### §5  Preguntas que responde este capítulo

Pregunta

del caso Instrumento que la responde Nivel de

certeza

¿Cuál es la CI del jugador — su contribución idiosincrática real al resultado?

CI = R*_B × (1 − S_B). Se calcula combinando las métricas estadísticas avanzadas (R*_B) con el análisis de ausencias (S_B). El método contrafáctico de las ausencias tiene mayor peso cuando la muestra es suficiente.

Declaración A con datos Dep1 (tracking + métricas avanzadas + ausencias ≥ 30 partidos). Declaración B con datos Dep2 (métricas estándar + ausencias 15–30 partidos).

Taxonomía General de Aplicaciones

Pregunta

del caso Instrumento que la responde Nivel de

certeza

¿El jugador está subpagado o sobrepagado — cuál es el Δ_B del club?

Δ_B_club = B_total × CI − salario_actual. Requiere estimar el B_total del club en el período analizado (premios, derechos de televisión, patrocinio, valorización del plantel).

Declaración B cuando el B_total puede estimarse con datos disponibles públicamente más los datos internos del club.

¿Cuál es el mapa de fragilidad del equipo — qué posición es más crítica?

ΔP(victoria|ausencia_i) = −CI_i × (1 − calidad_reemplazante_disponible) para cada jugador del plantel. La posición de mayor fragilidad no es necesariamente la de mayor R*_B.

Declaración B con datos Dep2/Dep3 del plantel y de los reemplazantes disponibles.

¿Un fichaje específico produce valor de arbitraje — está infravalorado por el mercado?

Valor_arbitraje = (CI_proyectada × B_total_esperado) − precio_mercado − coste_salarial. Un valor positivo indica que el mercado no ha valorado correctamente la CI del jugador en ese equipo específico.

Declaración B con proyección de CI desde datos Dep2 + estimación del B_total del equipo comprador.

### §6  Límites del método en el análisis deportivo

Límite 1 — Las contribuciones no estadísticas no son capturadas por las métricas avanzadas. Un defensa que intimida a los delanteros rivales sin necesariamente hacer más recuperaciones, un capitán que cambia la dinámica emocional del vestuario, un jugador que libera a otro compañero para que rinda mejor — estas contribuciones no tienen métrica directa. El análisis de ausencias puede capturar su efecto agregado, pero no puede atribuirlo individualmente.

Taxonomía General de Aplicaciones

Límite 2 — La varianza de resultado en el deporte es alta. El fútbol tiene una varianza de resultado excepcionalmente alta comparada con otros deportes. Un equipo superior puede perder con un equipo inferior en un porcentaje significativo de los partidos. R*_B × (1 − S_B) de cualquier jugador individual tiene una componente de azar que es difícil de separar de la contribución genuina. El análisis a largo plazo (tres temporadas) reduce ese ruido, pero no lo elimina.

Límite 3 — La muestra de ausencias puede no ser representativa. El jugador puede haberse lesionado en partidos contra rivales difíciles, produciendo una S_B artificialmente baja. O puede haberse lesionado en períodos de fatiga del equipo, produciendo una S_B artificialmente alta. La robustez del análisis de ausencias requiere verificar que las ausencias son una muestra representativa de la distribución de rivales y condiciones.

Límite 4 — La CI está calibrada para el equipo específico. La CI de un jugador en el equipo A puede ser muy distinta de su CI en el equipo B, porque su contribución idiosincrática depende de las características de sus compañeros. Un jugador que complementa perfectamente al sistema de un equipo puede ser redundante en otro.

— Fin del Capítulo 55 —

Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

