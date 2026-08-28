## PARTE VIII · Deporte y Rendimiento

### Capítulo 55
Valoración de jugadores y distribución
del éxito deportivo
Organ. Estru. Model. Educa. Crisi.
Para el mediador que busca precisión · Cómo usar este
capítulo
Este capítulo es Compilación directa del capítulo 17 de El cálculo de la
responsabilidad (Deportes y valor de contribución). Aplica los
instrumentos del sistema — R*_B, S_B, Δ_B — al dominio del
análisis deportivo: la valoración de jugadores individuales, la
distribución del éxito colectivo entre los contribuyentes, y la negociación
salarial basada en la contribución causal idiosincrática. El dominio
deportivo es el único de la Taxonomía donde el sistema puede calibrarse
con datos estadísticos ricos y con el experimento natural de las ausencias
del jugador.
La idea más contraintuitiva del capítulo: los jugadores más famosos de
la historia tienden a tener S_B más alta de lo que la narrativa popular
sugiere. La razón: un equipo genuinamente excelente tiene cierta
capacidad de generar el resultado independientemente del individuo
específico. La contribución idiosincrática — la fracción del resultado que
ese jugador específico y ningún otro en su posición habría producido —
es lo que el sistema mide como CI (Contribución Idiosincrática) =
R*_B × (1 − S_B).
§1 Descripción del subcampo: R*_B en el
dominio deportivo
En el dominio deportivo, el evento final es positivo: el triunfo,
el campeonato, el resultado que el equipo y sus patrocinadores

Taxonomía General de Aplicaciones
buscaban. R*_B invierte la dirección respecto a R*_D: en
lugar de distribuir la responsabilidad sobre el daño, distribuye
el mérito sobre el triunfo. La matemática es idéntica —
iteración de potencia sobre el grafo de contribución — pero
el nodo final (Nf) es el éxito colectivo, y todos los nodos que
contribuyen positivamente a él tienen R*_B > 0.
La singularidad del dominio deportivo respecto a los demás
dominios de la Taxonomía es que tiene acceso a dos tipos de
evidencia que en los otros dominios no existen. La evidencia
estadística avanzada — Expected Goals (xG), VAEP, Win
Shares, PER, Defensive Impact — permite estimar la
contribución de cada jugador al resultado con relativa
precisión desde los datos observables del partido. Y el
experimento natural de las ausencias — los períodos en que el
jugador no estuvo disponible por lesión, suspensión o
convocatoria a la selección — provee el contrafáctico que
establece S_B con evidencia histórica directa: ¿cómo rindió el
equipo sin este jugador específico?
Los tres instrumentos centrales del dominio deportivo
R*_B(jugador_i): la fracción del triunfo causalmente atribuible al jugador i.
Se calcula como el eigenvector dominante del grafo de contribución, donde los
nodos son los jugadores, el sistema de juego, el cuerpo técnico y las condiciones
del contexto.
S_B(jugador_i): la fungibilidad deportiva del jugador. ¿Habría ganado el
equipo sin este jugador? S_B alto significa que el equipo tenía la capacidad
de ganar con un reemplazante de nivel equivalente. S_B bajo significa que ese
jugador específico era condición necesaria del resultado. S_B_hist = 1 −
|P(victoria|jugador) − P(victoria|sin_jugador) |.
CI (Contribución Idiosincrática) = R*_B × (1 − S_B): la fracción del
resultado que ese jugador específico y ningún otro en su posición habría
producido. Es el instrumento más relevante para la negociación salarial y la
valoración de transferencias — no el R*_B total, sino la CI que mide la
indispensabilidad real.
Δ_B del club = B_total × CI − salario_actual. Δ_B > 0 significa que el
club extrae valor no compensado del jugador — argumento para el aumento

Taxonomía General de Aplicaciones
salarial. Δ_B < 0 significa que el club paga más de lo que la CI justifica
— año de inversión del contrato.
§2 Escala de evidencia Dep0–Dep8
Tipo de
evidencia en Rango
Nivel Descripción
el dominio w
deportivo
Dep1 Métricas Las métricas de evento calculadas [0.72,
estadísticas desde los datos de tracking 0.90]
avanzadas de (posición de todos los jugadores
evento (xG, a 25 fps) que capturan la
VAEP, pases contribución física de cada
progresivos, jugador en cada segundo del
defensive juego. El análisis de ausencias
actions) con con muestra de al menos 30
tracking data partidos produce estimadores
de precisión + robustos de S_B con intervalos
análisis de de confianza aceptables.
ausencias con
muestra ≥ 30
partidos
Dep2 Métricas Las métricas estadísticas estándar [0.60,
estadísticas verificadas independientemente, 0.78]
estándar con análisis de ausencias y análisis
verificadas de rendimiento del equipo en
(goles, períodos comparables (misma
asistencias, fase de la temporada, rival
pases clave, equivalente).
xG) + análisis
de ausencias
con muestra de
15–30 partidos
+ análisis de
rendimiento
del equipo en
períodos
comparables

Taxonomía General de Aplicaciones
Tipo de
evidencia en Rango
Nivel Descripción
el dominio w
deportivo
Dep3 Análisis La convergencia de dos análisis [0.50,
estadístico de estadísticos independientes con 0.68]
dos o más metodologías distintas aumenta
analistas el peso de la evidencia respecto al
independientes análisis único.
con
metodologías
distintas que
convergen en
la estimación
de R*_B y S_B
Dep4 Métricas Las estadísticas estándar sin el [0.36,
estadísticas análisis de ausencias que 0.54]
estándar sin establece S_B, combinadas con la
análisis de evaluación cualitativa del
ausencias + scouting del club.
evaluación
cualitativa de
scouting
Dep5 Análisis de La evaluación del rendimiento del [0.18,
scouting jugador basada en la observación 0.36]
cualitativo sin experta sin métricas estadísticas
métricas que la respalden.
estadísticas
avanzadas
Dep6 Valoración de La valoración del jugador basada [0.08,
mercado y en la comparación con el precio 0.22]
comparación de mercado de jugadores en
con jugadores posiciones y perfiles similares, sin
equivalentes análisis estadístico específico de
su contribución.
Dep0 Análisis El análisis estadístico que w =
Dep1/Dep2 establece que la contribución 0.00
que establece causal del jugador no fue positiva
que el jugador sobre el resultado analizado — el
no tuvo R*_B equipo rendía igual o mejor en su
positivo ausencia.
verificable
sobre el

Taxonomía General de Aplicaciones
Tipo de
evidencia en Rango
Nivel Descripción
el dominio w
deportivo
resultado
analizado
§3 Las herramientas del análisis de
contribución deportiva
§3.1 El grafo de contribución causal al resultado deportivo
El grafo de contribución al resultado deportivo tiene una
estructura diferente a los grafos de daño de los capítulos
anteriores. Todos los nodos que contribuyen positivamente al
triunfo tienen R*_B > 0. Los nodos que contribuyeron
negativamente — los errores, las lesiones, las expulsiones —
tienen R*_B < 0 en esa acción específica, que se incorpora al
cálculo global del jugador.
R*_B típico
Nodo del en
Fuente de
grafo campeonatos S_B típico
evidencia para w
deportivo de largo
plazo
Jugadores Distribución Alta [0.45– xG, VAEP, pases
individuales variable. El 0.75] para la progresivos,
jugador de mayoría. Baja- acciones
mayor CI en moderada defensivas.
un equipo élite [0.20–0.45] Métricas de
suele tener CI solo para impacto en
entre 8–18% jugadores P(victoria).
del triunfo únicos en su Análisis de
colectivo — posición en el ausencias.
porque el equipo.
deporte es
colectivo y la
varianza es
alta. Los

Taxonomía General de Aplicaciones
R*_B típico
Nodo del en
Fuente de
grafo campeonatos S_B típico
evidencia para w
deportivo de largo
plazo
jugadores
> «estrella»
raramente
superan el
20% de CI
genuina.
Sistema de 8–18% en Moderada Análisis de
juego / campeonatos [0.40–0.65]: rendimiento con
táctica donde la sistemas distintas
táctica fue similares son alineaciones.
diferenciadora. replicables por Comparación de
La táctica otros rendimiento
determina el entrenadores, antes/después de
contexto en el aunque el cambios tácticos.
que las diseño
contribuciones específico
individuales puede ser
son posibles. idiosincrático.
Cuerpo 8–15% en Moderada Historial de
técnico campeonatos [0.35–0.60]: la resultados con y
(entrenador) de largo plazo. calidad del sin el entrenador.
En partidos entrenador Eficacia
individuales, tiene documentada de
las decisiones componentes las sustituciones.
del entrenador idiosincráticos Análisis de los
(sustituciones, (el diseñador ajustes tácticos en
ajustes tácticos del sistema partidos.
en el descanso) táctico
pueden ser específico) y
determinantes. genéricos (los
entrenadores
de nivel
equivalente
producirían
resultados
similares con
ese plantel).

Taxonomía General de Aplicaciones
R*_B típico
Nodo del en
Fuente de
grafo campeonatos S_B típico
evidencia para w
deportivo de largo
plazo
Condiciones 5–15% según Muy alta Análisis estadístico
del contexto el contexto [0.75–0.95]: las de la ventaja de
(localía, específico. condiciones localía del equipo.
árbitro, del contexto Análisis de
condiciones son rendimiento en
climáticas, independientes distintas
cansancio de los actores condiciones.
del rival) del equipo.
§3.2 Los tres métodos de estimación de S_B
El índice S_B puede estimarse con tres métodos distintos que
el análisis debe combinar para producir un estimador robusto.
Los tres métodos producen rangos que se ponderan según la
calidad y la cantidad de la evidencia disponible.
Descripción
Método Limitación S_B resultante
operativa
Método Se comparan Las ausencias S_B ∈ [0, 1]. Es el
1: los resultados pueden no ser método más directo
Compara del equipo una muestra y de mayor peso
ción cuando el representativa: cuando la muestra es
histórica jugador estuvo el jugador suficiente.
de disponible puede haberse
ausencia versus cuando lesionado en
s no (por lesión, partidos
suspensión o contra rivales
selección). difíciles o en
S_B_hist = 1 − períodos de
|P(victoria|jug fatiga del
ador) − equipo. Se
P(victoria|sin_j necesita una
ugador) |. Si la muestra de al
diferencia en la menos 15
tasa de victorias partidos sin el
es pequeña, S_B jugador para
es alta. Si la que el
diferencia es

Taxonomía General de Aplicaciones
Descripción
Método Limitación S_B resultante
operativa
grande, S_B es estimador sea
baja. robusto.
Método El valor de Computaciona φ_B_i ∈ [0, 1] con
2: Shapley lmente Σ_i φ_B_i =
Shapley distribuye la intensivo para R*_B_total. El
deportiv contribución al planteles Shapley captura
o triunfo entre los grandes. complementariedade
jugadores Requiere s que el eigenvector
considerando estimar v(S) ordinario no capta.
todas las para cada
posibles coalición
composiciones posible, lo que
del equipo. para un equipo
φ_B_i = de 11
contribución jugadores
marginal implica 2^11
promedio de i = 2048
sobre todas las coaliciones
posibles posibles. Se
coaliciones del aproxima con
equipo. Captura métodos de
si la Monte Carlo.
contribución
del jugador es
mayor cuando
sus compañeros
son más fuertes
o más débiles
(complementari
edad).
Método Las métricas de Las métricas S_B estadístico = 1 −
3: contribución estadísticas (métricas_jugador −
Métricas avanzadas capturan métricas_mejor_ree
estadístic estiman la muchas, pero mplazante) /
as contribución de no todas las métricas_jugador.
avanzada cada acción del contribucione
s jugador al s: el líder del
(VAEP, resultado final. vestuario, el
xG, Win S_B estadístico defensa que
Shares) se estima desde intimida a los
la comparación delanteros
del nivel de las rivales sin
métricas del hacer más
jugador con el recuperacione

Taxonomía General de Aplicaciones
Descripción
Método Limitación S_B resultante
operativa
de sus posibles s, el jugador
reemplazantes: que libera a un
si los compañero.
reemplazantes Estas
de nivel contribucione
equivalente s no
están fácilmente estadísticas
disponibles en pueden ser
el mercado, S_B relevantes.
es alta.
§3.3 Δ_B como herramienta de negociación salarial
El Δ_B del jugador en relación con el club es la diferencia entre
la fracción del B_total del triunfo que el jugador causó y la
fracción que recibe. El argumento de negociación tiene tres
componentes que el analista debe calcular y el agente debe
presentar.
B_total del club = premios competitivos + ingresos de
taquilla + contratos de televisión + derechos de imagen +
valorización del plantel
salario_justo_jugador = B_total × CI_jugador = B_total ×
R*_B × (1 − S_B)
Δ_B_club = B_total × CI_jugador − salario_actual
Δ_B_club > 0: el club extrae valor no compensado del jugador —
argumento para el aumento salarial. Δ_B_club = 0: la compensación es
proporcional a la contribución causal idiosincrática. Δ_B_club < 0: el club
paga más de lo que la CI justifica en ese año — año de inversión del contrato
que se compensará en los años de peak del jugador.
El argumento de negociación basado en Δ_B es más poderoso que el
argumento basado solo en comparación de mercado porque conecta el salario
específicamente con el beneficio causal que ese jugador produce para ese club.
Un club puede replicar el argumento de mercado señalando que el jugador
podría ser reemplazado por otro con igual sueldo. No puede replicar el

Taxonomía General de Aplicaciones
argumento de Δ_B cuando el análisis de ausencias documenta que el equipo
rinde significativamente peor sin él.
§3.4 Los cuatro predictores de rendimiento prospectivo
El análisis de R*_B tiene su mayor valor operativo en la
predicción prospectiva: estimar la contribución futura de un
jugador antes de negociar su contrato de renovación o su
transferencia. Los cuatro predictores son instrumentos
derivados de R*_B y S_B que el analista puede calcular con los
datos de las dos o tres temporadas previas del jugador.
Aplicación
Predictor Descripción operativa
principal
P1: Mapa de Para cada jugador del plantel: Planificación de
fragilidad del ΔP(victoria|ausencia_i) = −CI_i plantilla antes
equipo × (1 − del mercado de
calidad_reemplazante_disponible). transferencias.
El mapa de fragilidad muestra qué Identificación
posición del plantel produce la de las posiciones
mayor caída esperada en de mayor
P(victoria) ante una ausencia. El prioridad para
jugador de mayor fragilidad puede refuerzo.
no ser el de mayor R*_B: si tiene Análisis de
un reemplazante de calidad riesgo para el
equivalente (S_B alta), su ausencia seguro de
no es crítica. lesiones.
P2: Arbitraje Valor_arbitraje = (CI_proyectada Decisiones de
de × B_total_esperado) − fichaje en el
transferencias precio_mercado − coste_salarial. mercado de
(Valor CI) Un jugador con Valor_arbitraje > transferencias.
0 está infravalorado por el Identificación
mercado respecto a su de ineficiencias
contribución causal proyectada en del mercado.
ese equipo específico. El análisis
de CI calibra la contribución para
el equipo comprador específico:
un mediocampista creativo puede
tener CI alta en un equipo de
posesión y CI baja en un equipo de
contraataque.

Taxonomía General de Aplicaciones
Aplicación
Predictor Descripción operativa
principal
P3: Curva de R*_B(t) = R*_B_peak × f (t − Diseño de los
valor del t_peak), donde f modela el ciclo de contratos
jugador en el vida del rendimiento. El peak plurianuales.
tiempo ocurre entre los 25 y 29 años para Identificación
la mayoría de los jugadores de del año de
campo (el portero tiene un peak inversión.
más tardío y un declive más lento). Planificación de
La CI decrece en el declive porque la renovación
los reemplazantes se hacen óptima.
comparables. El año de inversión
del contrato ocurre cuando CI ×
B_total < salario_contratado.
P4: max Σ_i CI_i × w_i sujeto a Σ_i Optimización
Composición (precio_mercado_i + salario_i) ≤ del presupuesto
óptima del presupuesto, donde w_i es el de fichajes.
plantel dado factor de complementariedad del Identificación
el jugador con los titulares actuales. de las
presupuesto El problema de optimización combinaciones
puede resolverse con algoritmos de jugadores que
greedy o con búsqueda estocástica maximizan la CI
cuando el espacio de posibilidades total por euro
es grande. invertido.
§4 Casos resueltos
Caso A — Brasil en el Mundial de México 1970: R*_B
de Pelé vs. el equipo
El Brasil de 1970 es considerado por muchos historiadores del
fútbol el mejor equipo de la historia. Su convocatoria incluía a
Pelé, Gerson, Jairzinho, Tostão y Rivelino. El Brasil de 1962
— sin Pelé desde el segundo partido por lesión — también fue
campeón del mundo. Esa comparación produce la pregunta
más directa del capítulo en términos del sistema: ¿cuál era el
R*_B de Pelé en el triunfo de Brasil 1970? La evidencia de
1962 sugiere que Brasil tenía un equipo capaz de ganar el
campeonato sin él.

Taxonomía General de Aplicaciones
Nodo Jugador/Factor R*_B S_B Análisis
N1 Pelé (número 10, ~18% 0.45 S_B moderada
figura global) documentada por el
experimento natural de
1962: Amarildo
reemplazó a Pelé con
eficacia y Brasil fue
campeón. La S_B de
Pelé en 1970 era mayor
que la de Gerson
porque había más
jugadores en el mundo
capaces de replicar
parte de su función que
la de Gerson. CI = 18%
× (1 − 0.45) = 9.9%.
Pelé era el más famoso
pero no el más
indispensable en el
sentido causal.
N2 Gerson ~14% 0.35 S_B baja: pocos
(mediocampo, jugadores del mundo
creador) tenían su visión de
juego y su capacidad de
conducir el tempo del
Brasil de 1970 desde el
mediocampo. CI =
14% × 0.65 = 9.1% —
comparable a la de Pelé
en CI aunque menor en
R*_B.
N3 Jairzinho ~13% 0.40 7 goles en 6 partidos
(extremo incluyendo la final. CI =
goleador) 13% × 0.60 = 7.8%.
N4 Tostão (falso ~11% 0.42 Su capacidad de crear
nueve) espacios para Pelé y
Jairzinho era
idiosincrática. CI =
11% × 0.58 = 6.4%.
N5 Rivelino ~9% 0.48 Zurdo de calidad
(extremo zurdo / técnica excepcional. CI
mediocampo) = 9% × 0.52 = 4.7%.

Taxonomía General de Aplicaciones
Nodo Jugador/Factor R*_B S_B Análisis
N6 Sistema táctico / ~14% 0.45 El sistema 4-2-2-2 de
entrenador Zagallo, que permitía la
Zagallo libertad de movimiento
de los atacantes
manteniendo la solidez
defensiva, fue una
innovación táctica del
período. CI = 14% ×
0.55 = 7.7%.
N7 Calidad del ~8% 0.85 S alto: la profundidad
plantel de reserva del plantel era sistémica,
no idiosincrática.
N8 Condiciones del ~13% 0.88 Localía relativa en
contexto México, altitude del
estadio, organización de
la FIFA. S muy alta.
El resultado central del análisis: la CI de Pelé (9.9%) es
comparable a la de Gerson (9.1%) y algo superior a la del
sistema táctico de Zagallo (7.7%). Pelé no era el nodo
dominante del grafo — era el más famoso, pero la distribución
de la CI era relativamente homogénea entre los tres o cuatro
jugadores principales y el entrenador. La proposición del
sistema: la grandeza de ese Brasil era colectiva en un sentido
técnicamente preciso — ningún nodo individual dominaba la
distribución de CI.
Valores de Shapley deportivo para los cinco atacantes
principales (estimación Monte Carlo con 10.000 iteraciones):
Pelé 18.2%, Gerson 16.4%, Jairzinho 14.8%, Tostão 12.1%,
Rivelino 10.9%. La distribución Shapley es más homogénea
que la narrativa popular — que tiende a concentrar el mérito
en Pelé — porque capta la complementariedad entre los
jugadores: cada uno de ellos contribuye más cuando los demás
están presentes.

Taxonomía General de Aplicaciones
Caso B — Negociación salarial con Δ_B: el
mediocampista subpagado
Mediocampista central de 26 años en un club de primera
división europea. Tres temporadas en el club: dos títulos de
liga, tres clasificaciones a fase de grupos de Champions
League, dos semifinales de Copa. El club le ofrece 3.5M€/año
en la renovación. El análisis establece si es justo.
Componente
Estimación Fuente de evidencia
del análisis
B_total del Premio por ganar la Reportes financieros del club.
club en las liga: 8M. Premios de Datos de la UEFA sobre
tres Champions (tres distribución de premios.
temporadas clasificaciones + Comparación de contratos de
avances): 45M. patrocinio pre/post período.
Incremento en
derechos de
televisión: 12M.
Incremento en
contratos de
patrocinio atribuible
al éxito: 18M.
Valorización del
valor de mercado del
club: 35M estimado.
Total: ~118M€ en
tres temporadas.
R*_B del Método estadístico: Datos de VAEP de las tres
jugador VAEP del jugador / temporadas. Análisis de las 8
VAEP_total_equipo semanas de baja por lesión en
= 14%. Método la segunda temporada.
contrafáctico: [P
(clasif.
Champions|con) −
P (clasif. |sin)] / P
(clasif. |con) = (0.90
− 0.65) / 0.90 ≈
28%. Promedio
ponderado con
mayor peso al
método
contrafáctico: R*_B
≈ 20%.

Taxonomía General de Aplicaciones
Componente
Estimación Fuente de evidencia
del análisis
S_B del 8 semanas de Base de datos de resultados
jugador ausencia por lesión: del equipo. Partidos de las 8
tasa de victorias del semanas de ausencia.
equipo cayó del 74%
al 51%. S_B_hist =
1 − |0.74 − 0.51| =

### 0.77. El equipo
rendía
significativamente
peor sin él, pero no
de manera
catastrófica — S_B
moderada-alta.
CI y salario CI = R*_B × (1 − Combinación de métodos
justo S_B) = 0.20 × (1 − estadístico y contrafáctico.
0.77) = 0.046. Pero
con el método
contrafáctico
calibrado por la
caída en P(victoria):
CI_ajustada ≈ 0.036
(36 × 10^-3).
Salario_justo =
B_total_por_año ×
CI_ajustada =
(118M/3) × CI. Con
B_total/año ≈
39.3M€:
salario_justo ≈
39.3M × 0.109 ≈
4.25M€/año.
Δ_B del club Salario actual Calculado a partir del B_total
bajo distintos (2.8M): Δ_B_club = estimado y la CI_ajustada.
escenarios 4.25M − 2.8M =
+1.45M/año (el
club extrae valor no
compensado).
Oferta del club
(3.5M): Δ_B_club =
4.25M − 3.5M =
+0.75M/año
(reduce el Δ pero no
lo elimina). Salario

Taxonomía General de Aplicaciones
Componente
Estimación Fuente de evidencia
del análisis
justo (4.25M):
Δ_B_club ≈ 0.
Estrategia de negociación del agente: presentar el B_total
calculado (118M€ en tres temporadas), el R*_B estimado
(20%, documentado con las estadísticas de las 8 semanas de
ausencia), y el salario justo resultante (4.25M€). Si el club no
acepta el marco analítico, el agente puede señalar que el propio
período de lesión del jugador prueba su contribución con
evidencia interna del club: la caída del 23 puntos porcentuales
en la tasa de victorias durante las 8 semanas de baja es el
experimento natural más limpio disponible. La
contrapropuesta del agente en 4.5M€ — ligeramente superior
al salario justo — deja margen de negociación hacia 4.0–
4.25M€.
§5 Preguntas que responde este capítulo
Pregunta Nivel de
Instrumento que la responde
del caso certeza
¿Cuál es la CI CI = R*_B × (1 − S_B). Se calcula Declaración A
del jugador combinando las métricas con datos Dep1
— su estadísticas avanzadas (R*_B) con (tracking +
contribución el análisis de ausencias (S_B). El métricas
idiosincrática método contrafáctico de las avanzadas +
real al ausencias tiene mayor peso ausencias ≥ 30
resultado? cuando la muestra es suficiente. partidos).
Declaración B
con datos Dep2
(métricas
estándar +
ausencias 15–30
partidos).

Taxonomía General de Aplicaciones
Pregunta Nivel de
Instrumento que la responde
del caso certeza
¿El jugador Δ_B_club = B_total × CI − Declaración B
está salario_actual. Requiere estimar el cuando el B_total
subpagado o B_total del club en el período puede estimarse
sobrepagado analizado (premios, derechos de con datos
— cuál es el televisión, patrocinio, valorización disponibles
Δ_B del del plantel). públicamente
club? más los datos
internos del club.
¿Cuál es el ΔP(victoria|ausencia_i) = −CI_i Declaración B
mapa de × (1 − con datos
fragilidad del calidad_reemplazante_disponible) Dep2/Dep3 del
equipo — para cada jugador del plantel. La plantel y de los
qué posición posición de mayor fragilidad no es reemplazantes
es más necesariamente la de mayor R*_B. disponibles.
crítica?
¿Un fichaje Valor_arbitraje = (CI_proyectada Declaración B
específico × B_total_esperado) − con proyección
produce precio_mercado − coste_salarial. de CI desde datos
valor de Un valor positivo indica que el Dep2 +
arbitraje — mercado no ha valorado estimación del
está correctamente la CI del jugador en B_total del
infravalorado ese equipo específico. equipo
por el comprador.
mercado?
§6 Límites del método en el análisis deportivo
Límite 1 — Las contribuciones no estadísticas no son
capturadas por las métricas avanzadas. Un defensa que
intimida a los delanteros rivales sin necesariamente hacer más
recuperaciones, un capitán que cambia la dinámica emocional
del vestuario, un jugador que libera a otro compañero para que
rinda mejor — estas contribuciones no tienen métrica directa.
El análisis de ausencias puede capturar su efecto agregado,
pero no puede atribuirlo individualmente.

Taxonomía General de Aplicaciones
Límite 2 — La varianza de resultado en el deporte es alta. El
fútbol tiene una varianza de resultado excepcionalmente alta
comparada con otros deportes. Un equipo superior puede
perder con un equipo inferior en un porcentaje significativo
de los partidos. R*_B × (1 − S_B) de cualquier jugador
individual tiene una componente de azar que es difícil de
separar de la contribución genuina. El análisis a largo plazo
(tres temporadas) reduce ese ruido, pero no lo elimina.
Límite 3 — La muestra de ausencias puede no ser
representativa. El jugador puede haberse lesionado en partidos
contra rivales difíciles, produciendo una S_B artificialmente
baja. O puede haberse lesionado en períodos de fatiga del
equipo, produciendo una S_B artificialmente alta. La robustez
del análisis de ausencias requiere verificar que las ausencias son
una muestra representativa de la distribución de rivales y
condiciones.
Límite 4 — La CI está calibrada para el equipo específico. La
CI de un jugador en el equipo A puede ser muy distinta de su
CI en el equipo B, porque su contribución idiosincrática
depende de las características de sus compañeros. Un jugador
que complementa perfectamente al sistema de un equipo
puede ser redundante en otro.
— Fin del Capítulo 55 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

