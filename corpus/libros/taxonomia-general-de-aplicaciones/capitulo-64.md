## PARTE X · Ciencias Naturales y Medioambiente

### Capítulo 64
Cambio climático — responsabilidad
histórica en emisiones globales
Organ. Estru. Model. Educa. Crisi.
Para el mediador que busca precisión · Cómo usar este
capítulo
Este capítulo es Nivel B: aplica el cap. 14 de El cálculo de la responsabilidad
(Medio ambiente y ecología) al dominio del cambio climático y las emisiones
históricas. El instrumento central es el valor de Shapley aplicado a la distribución
de la responsabilidad climática: cuando ningún Estado, empresa o sector
individual es condición necesaria del cambio climático global, el Shapley
distribuye la responsabilidad proporcional a la contribución marginal promedio
de cada emisor sobre todas las posibles coaliciones.
La singularidad del dominio climático es que produce la forma más pura del
problema de causalidad acumulativa: el calentamiento global no es el resultado
de ningún actor individual sino de la suma de las contribuciones de miles de
emisores durante más de un siglo. R* convencional asigna cero a todos los actores
porque ninguno es condición necesaria del daño global. El Shapley produce
valores positivos para todos proporcionales a su contribución marginal real. Esos
valores son la base técnica para el diseño de compromisos climáticos equitativos.
§1 El problema de la causalidad climática: por qué
R* convencional falla
El cambio climático es el caso de causalidad acumulativa más
complejo de la Taxonomía: la desestabilización del sistema climático
es el resultado de las emisiones de miles de actores durante más de

Taxonomía General de Aplicaciones
un siglo. Las emisiones de CO₂ y otros gases de efecto invernadero
tienen la propiedad de que cada tonelada contribuye marginalmente
al calentamiento global, pero ninguna tonelada individual es
condición necesaria del daño en el sentido del postulado I5 del
sistema — porque sin las emisiones de cualquier actor individual, el
sistema climático habría sido desestabilizado de todas formas por la
suma de los demás actores.
El fallo de R* convencional en este dominio es técnico y preciso: R*
convencional requiere que P (daño_a_esa_escala | sin el actor_i) <
P (daño | con el actor_i). Para el cambio climático global, sin las
emisiones de ningún actor individual el sistema habría alcanzado
prácticamente el mismo nivel de desestabilización — porque la
cantidad de emisiones de cualquier actor individual (incluso los
mayores emisores históricos) no es necesaria para producir el umbral
de calentamiento que constituye el daño global. R* convencional =
0 para todos. El resultado es evidentemente incorrecto: los grandes
emisores históricos son causalmente responsables del daño, aunque
no sean causalmente necesarios individualmente.
El valor de Shapley climático: la solución al problema de
causalidad acumulativa
φᵢ (Shapley) = Σ_{S⊆N\{i}} [|S|! (n−|S|−1) /n!] × [v(S∪{i}) −
v(S)]
Donde v(S) es la función de valor de la coalición: el daño climático producido por la
coalición S de actores operando juntos. El Shapley del actor i es su contribución
marginal promedio a todas las coaliciones posibles que incluyen a ese actor. Para el
cambio climático, v(S) = f(emisiones_acumuladas_S) — una función del total de
emisiones de la coalición S. El Shapley produce valores positivos para todos los
emisores proporcionales a su contribución marginal: los grandes emisores históricos
tienen mayor Shapley que los pequeños emisores, aunque ninguno sea condición
necesaria individualmente.
Para grupos grandes de emisores (los 200+ países del sistema climático), el Shapley
se aproxima con métodos de Monte Carlo: se generan K ordenamientos aleatorios del
conjunto de actores, se calcula la contribución marginal de cada actor en cada
ordenamiento, y se promedia. Con K ≥ 10,000 iteraciones, el estimador converge al
Shapley exacto con error < 1%.

Taxonomía General de Aplicaciones
§2 Escala de evidencia Am0–Am8
Tipo de
evidencia en Rango
Nivel Descripción
el dominio w
climático
Am1 Inventarios Los inventarios de emisiones [0.72,
nacionales de verificados por el IPCC o por 0.90]
emisiones organismos de verificación
verificados + independiente, combinados con
estudios de estudios de atribución climática que
atribución establecen la contribución de las
climática con emisiones acumuladas al calentamiento
modelos de observado con metodología
circulación documentada e intervalo de confianza
general + estadístico.
análisis de
detección y
atribución con
intervalo de
confianza
documentado
Am2 Inventarios de Los inventarios de emisiones de [0.60,
emisiones de organismos internacionales 0.78]
organismos reconocidos con metodología
internacionales documentada, combinados con los
(IEA, estudios de atribución disponibles en la
EDGAR, literatura científica revisada.
GCP) con
metodología
documentada
+ estudios de
atribución de
segundo nivel
Am3 Análisis La convergencia de dos o más [0.50,
convergente inventarios de emisiones 0.68]
de múltiples independientes sobre el mismo período
inventarios de y actor, que establecen un rango de
emisiones emisiones acumuladas consistente.
sobre el

Taxonomía General de Aplicaciones
Tipo de
evidencia en Rango
Nivel Descripción
el dominio w
climático
mismo
período y actor
Am4 Estimaciones Las estimaciones de emisiones [0.36,
de emisiones históricas calculadas desde proxies 0.52]
desde proxies cuando los inventarios directos no están
históricos disponibles para el período analizado.
(consumo de
combustibles,
producción
industrial,
datos de
satélite) sin
verificación
directa
Am5 Análisis de El análisis de las emisiones de un sector [0.18,
emisiones económico sin la capacidad de 0.36]
sectoriales sin atribuirlas a actores individuales dentro
desglose por del sector.
actor
específico
Am0 Análisis El análisis de inventario verificado que w =
Am1/Am2 establece que las emisiones del actor en 0.00
que establece el período analizado son negligibles
que el actor no respecto al total o que el actor no operó
produjo como emisor en ese período.
emisiones
atribuibles en
el período
analizado
§3 El protocolo Shapley para emisiones históricas
§3.1 La distinción entre responsabilidad histórica y
responsabilidad prospectiva

Taxonomía General de Aplicaciones
La responsabilidad climática tiene dos dimensiones que el análisis
debe tratar separadamente. La responsabilidad histórica: la fracción
del daño climático acumulado hasta la fecha atribuible a las
emisiones históricas del actor. Esta es la dimensión del Shapley
climático histórico — la distribución de la responsabilidad sobre el
stock de emisiones acumuladas desde la Revolución Industrial. La
responsabilidad prospectiva: la fracción del daño climático futuro
que las emisiones actuales del actor producirán bajo los escenarios
de trayectoria disponibles. Esta es la dimensión del Shapley climático
prospectivo — la distribución de la responsabilidad sobre las
emisiones proyectadas bajo distintos escenarios de mitigación.
Dimensión de
la Instrumento del
Resultado del análisis
responsabilidad sistema
climática
Responsabilidad Shapley histórico: φᵢ_hist La distribución de la
histórica (stock = contribución marginal responsabilidad histórica
de emisiones promedio de las establece quién tiene mayor
1850–hoy) emisiones acumuladas del AD sobre los daños ya
actor i sobre todas las producidos por el cambio
posibles coaliciones de climático: los eventos de calor
emisores históricos. Las extremo, las inundaciones
emisiones históricas se costeras, los desplazamientos
calculan con los de comunidades. El Shapley
inventarios de la base de histórico es la base de los
datos Carbon Dioxide reclamos de «pérdidas y
Information Analysis daños» de los países
Center (CDIAC) y el vulnerables al cambio
Global Carbon Project climático.
(GCP).
Responsabilidad Shapley prospectivo: La distribución de la
prospectiva φᵢ_prosp(S) = responsabilidad prospectiva
(emisiones contribución marginal de establece los compromisos de
proyectadas bajo las emisiones proyectadas reducción de emisiones
distintos del actor i en el escenario equitativos: la fracción del
escenarios) S sobre las emisiones presupuesto de carbono
totales necesarias para restante que corresponde a
mantener el cada actor dado su Shapley
calentamiento por debajo prospectivo. Es la base
del umbral establecido técnica para los Nationally
(1.5°C o 2°C). El Determined Contributions
presupuesto de carbono (NDCs) del Acuerdo de París.
restante es el total de

Taxonomía General de Aplicaciones
Dimensión de
la Instrumento del
Resultado del análisis
responsabilidad sistema
climática
emisiones permitidas; el
Shapley distribuye ese
presupuesto entre los
actores.
§3.2 La responsabilidad diferenciada por época: el problema de
las emisiones pre-industriales
El Shapley histórico tiene una dimensión temporal que el análisis
debe incorporar: la responsabilidad de las emisiones históricas
depende del conocimiento científico disponible en el período en que
se produjeron. Las emisiones previas al Primer Informe del IPCC
(1990) se produjeron en un contexto donde el conocimiento
científico sobre el vínculo entre las emisiones de GEI y el
calentamiento global no estaba consolidado en el consenso científico
internacional. Las emisiones posteriores a 1990 — especialmente las
posteriores a la Convención Marco de las Naciones Unidas sobre el
Cambio Climático (UNFCCC, 1992) — se produjeron con
conocimiento pleno del riesgo.
El operador H climático: la responsabilidad diferenciada por
conocimiento
φᵢ_ajustado = φᵢ_pre1990 × K_pre + φᵢ_post1990 × K_post +
φᵢ_post2015 × K_2015
Donde K_pre es el coeficiente de conocimiento del período pre-1990 (menor
responsabilidad atribuible por ausencia del consenso científico internacional
consolidado), K_post es el coeficiente del período 1990–2015 (conocimiento
establecido, pero compromisos voluntarios), y K_2015 es el coeficiente del período post-
Acuerdo de París (responsabilidad plena con compromisos legalmente vinculantes).
Los valores calibrados de los coeficientes son objeto de debate normativo — no son
valores técnicos sino políticos. El análisis establece el rango: K_pre ∈ [0.30, 0.60],
K_post ∈ [0.65, 0.85], K_2015 ∈ [0.90, 1.00].

Taxonomía General de Aplicaciones
§4 Aplicación del Shapley climático: distribución de
la responsabilidad histórica
La aplicación del Shapley histórico a las emisiones acumuladas de los
principales actores climáticos produce una distribución que difiere
significativamente de la distribución de las emisiones anuales
actuales — porque incorpora la responsabilidad histórica que los
grandes emisores del pasado acumularon durante el siglo XX. Los
datos del Carbon Dioxide Information Analysis Center (CDIAC)
establecen que los países industrializados producen
aproximadamente el 75% de las emisiones acumuladas históricas a
pesar de representar menos del 20% de la población mundial actual.
Emisiones
φᵢ Shapley Implicación
Actor / acumuladas
histórico para la
Grupo históricas
(estimación) responsabilidad
(aprox.)
Estados ~25% del total ~22–28% según el AD_EEUU
Unidos histórico período de inicio y el sobre el
(1850–hoy) acumulado método de D_climático
estimación de v(S). acumulado es el
La contribución más alto de
marginal de EEUU cualquier actor
es alta porque era el individual. La
mayor emisor base del reclamo
individual hasta hace de «pérdidas y
relativamente poco. daños» de los
países
vulnerables
apunta en mayor
proporción a
EEUU.
Unión ~22% del total ~18–24% del La
Europea (28 histórico Shapley histórico responsabilidad
países, acumulado colectivo de la UE. histórica
histórico) colectiva de la
UE es
comparable a la
de EEUU

Taxonomía General de Aplicaciones
Emisiones
φᵢ Shapley Implicación
Actor / acumuladas
histórico para la
Grupo históricas
(estimación) responsabilidad
(aprox.)
aunque sus
emisiones per
cápita actuales
son menores.
China ~12% del total ~10–14% del El Shapley
histórico Shapley histórico. La histórico de
acumulado contribución China es
(mayor emisor marginal de China es significativo pero
anual desde creciente en el menor que el de
~2007) período reciente. EEUU y la UE
dados sus
menores
emisiones
históricas
acumuladas hasta
fines del s. XX.
Resto del ~25% del total ~20–26% del La
mundo histórico Shapley histórico responsabilidad
desarrollado acumulado colectivo. histórica de los
(Canadá, países
Australia, desarrollados
Japón, Rusia) excede con
creces su peso en
la población
mundial.
Países en ~16% del total ~12–18% del Los países en
desarrollo histórico Shapley histórico desarrollo — que
(resto del acumulado colectivo. incluyen a los
mundo) más vulnerables
al cambio
climático — son
los que menos
han contribuido
al stock de
emisiones que
produce el daño
que sufren.

Taxonomía General de Aplicaciones
El resultado más relevante del Shapley climático para la
política pública: la inversión entre responsabilidad y
vulnerabilidad
El Shapley histórico establece con precisión la inversión que hace que el cambio
climático sea el caso más extremo de injusticia distributiva global: los países que
menos han contribuido al stock de emisiones históricas (Shapley histórico bajo)
son los que sufren los mayores daños climáticos (exposición alta a inundaciones,
sequías, eventos de calor extremo y desplazamiento). Los países insulares del
Pacífico, las naciones del Sahel africano, los países de los Andes con glaciares en
retroceso — tienen Shapley histórico < 1% y sufren daños climáticos
desproporcionados al 1% de las emisiones que produjeron.
§4.1 La responsabilidad de las empresas de combustibles
fósiles: el Shapley de emisiones de producto
Un análisis complementario del Shapley climático aplica el
instrumento a las empresas de combustibles fósiles cuyos productos
— el petróleo, el carbón, el gas natural extraídos y vendidos — son
la fuente de las emisiones. El Carbon Disclosure Project (CDP)
estableció en 2017 que 100 empresas de combustibles fósiles son
responsables del 71% de las emisiones globales desde 1988. El
análisis de Shapley de esas empresas distribuye la responsabilidad de
esas emisiones proporcional a la producción de cada empresa.
Fracción de las
Empresa / emisiones φᵢ Shapley de
Implicación
Grupo globales (1988– producto
hoy)
Saudi ~4.4% de las φ Aramco ≈ 4.0– La empresa de
Aramco emisiones 4.8% mayor φ individual
globales del entre las empresas
período privadas y estatales
de combustibles
fósiles.
Chevron ~3.5% de las φ Chevron ≈ 3.0– Mayor φ individual
emisiones 4.0% entre las empresas
globales del privadas
período occidentales
cotizadas.

Taxonomía General de Aplicaciones
Fracción de las
Empresa / emisiones φᵢ Shapley de
Implicación
Grupo globales (1988– producto
hoy)
ExxonMobil ~3.2% φ ExxonMobil ≈ ExxonMobil
2.8–3.5% conocía el vínculo
entre sus emisiones y
el cambio climático
desde los años 1970–
1980 según
documentos
internos publicados
posteriormente — el
K_conocimiento de
sus emisiones post-
1990 es máximo.
Las 5 ~21% colectivo φ ≈ 18–23% El Shapley de las
mayores colectivo grandes empresas
estatales estatales incluye la
(Saudi responsabilidad del
Aramco, Estado propietario.
Gazprom,
NIOC,
NNPC,
KPC)
§5 El D_climático y la inconmensurabilidad del
daño sistémico
El D_climático tiene la misma estructura de tres componentes que
todos los dominios de la Taxonomía — pero su dimensión es sin
precedentes en ningún otro dominio. El T_invertido climático son
las pérdidas directas ya producidas: los muertos y los daños
materiales de los eventos de calor extremo, las inundaciones, los
huracanes más intensos que el sistema climático desestabilizado
produce con mayor frecuencia e intensidad. El T_impedido son los
servicios ecosistémicos perdidos durante el período de la
desestabilización: la productividad agrícola reducida, el agua perdida
por el retroceso de los glaciares, los recursos pesqueros diezmados
por la acidificación del océano. El ΔT_trayectoria es el componente

Taxonomía General de Aplicaciones
más grande y el más difícil de cuantificar: la diferencia entre el
potencial de desarrollo de las regiones y comunidades afectadas bajo
el sistema climático estable y el potencial bajo el sistema
desestabilizado.
D_climático_total = T_invertido + T_impedido + ΔT_trayectoria
El D_monetary_equiv del cambio climático bajo el escenario de calentamiento de 2°C
(el objetivo del Acuerdo de París): entre 2 y 10 billones de dólares anuales en pérdidas
económicas globales según los distintos estudios de daños (Stern, 2006; Burke et al.,
2015; IPCC, 2022). Para el escenario de 4°C (el escenario actual sin acción
climática suficiente): entre 10 y 50 billones de dólares anuales en pérdidas — el 10–
25% del PIB global por año en el extremo superior del rango. Esas cifras son el
D_monetary_equiv calculable del cambio climático. Lo que no es calculable con
equivalente monetario — y que el sistema reconoce honestamente — es el valor
intrínseco del Amazonas, del Gran Arrecife de Coral, de los sistemas culturales de
las comunidades que el desplazamiento destruirá. Para esos componentes, el
Δ_permanente del daño climático es inconmensurable.
§5.1 El mecanismo de pérdidas y daños (Loss and Damage)
como α_diferido climático
El mecanismo de pérdidas y daños del Acuerdo de París (COP27,
2022) es la formalización institucional del α_diferido climático: el
reconocimiento de que los grandes emisores históricos tienen la
obligación de contribuir a las pérdidas y daños de los países
vulnerables proporcional a su Shapley histórico. El fondo de
pérdidas y daños establecido en COP27 tiene compromisos iniciales
de menos de 800 millones de dólares — una fracción minúscula del
D_total que el Shapley establece como responsabilidad proporcional
de los grandes emisores.
Instrumento
del sistema Equivalente en el paradigma Escala actual
climático
Fondo de α_diferido climático de los ~800M USD en
pérdidas y grandes emisores sobre el compromisos iniciales
daños (COP27) D_climático de los países vs. D_climático anual
vulnerables. AD = estimado de los países

Taxonomía General de Aplicaciones
Instrumento
del sistema Equivalente en el paradigma Escala actual
climático
Shapley_histórico × más vulnerables de
D_climático_atribuible al actor. ~400B USD. El AD /
D_total ≈ 0.2% —
valor de α_diferido muy
bajo para la magnitud
del Shapley histórico.
Compromisos α_anticipado climático: la Los NDCs actuales
de reducción fracción del daño futuro que el producen un
de emisiones actor se compromete a prevenir calentamiento
(NDCs del mediante la reducción de sus proyectado de ~2.4–
Acuerdo de emisiones prospectivas. 2.7°C para 2100 —
París) significativamente por
encima del objetivo de
1.5°C del Acuerdo de
París. El α_anticipado
colectivo es insuficiente
para el D_climático
prospectivo que las
emisiones actuales
producirán.
Financiamiento α_diferido sobre la fracción del El compromiso de
climático para T_impedido atribuible a la falta 100B USD anuales del
países en de acceso a tecnologías de Acuerdo de
desarrollo mitigación y adaptación. Copenhague no fue
cumplido hasta 2022.
La brecha de
financiamiento
climático para países en
desarrollo se estima en
6–10 veces el
financiamiento actual.
§6 Preguntas que responde este capítulo
Pregunta Instrumento Nivel de certeza
¿Cuál es el Shapley histórico aplicado a Declaración B con
Shapley histórico los inventarios de emisiones inventarios Am1/Am2

Taxonomía General de Aplicaciones
Pregunta Instrumento Nivel de certeza
del actor — qué verificados del actor en el del actor + modelo de
fracción del daño período 1850–actual. La atribución climática
climático función de valor v(S) se documentado. El rango
acumulado es construye desde la relación del Shapley tiene
causalmente entre las emisiones incertidumbre
atribuible a sus acumuladas de la coalición S y proporcional a la
emisiones? la temperatura observada del incertidumbre del
sistema climático. modelo de atribución.
¿Qué Operador H climático: Declaración B para los
responsabilidad φᵢ_ajustado = φᵢ_pre1990 × períodos con inventarios
diferenciada K_pre + φᵢ_post1990 × Am2/Am3 verificados.
corresponde al K_post + φᵢ_post2015 × La calibración de K es
período post- K_2015. El coeficiente K normativa y requiere
1990 vs. pre- depende del estado del consenso político.
1990? conocimiento científico en
cada período.
¿Cuál es el AD AD_i = Shapley_histórico_i Declaración C: el AD
del actor sobre el × del actor individual
D_climático de D_climático_total_atribuible. sobre el D de un país
los países El D_climático de los países específico requiere la
vulnerables? más vulnerables puede cadena de atribución
estimarse desde los estudios completa desde las
de daños climáticos por país emisiones hasta el
del IPCC. evento de daño, que
tiene incertidumbre alta.
§7 Límites del método en el dominio climático
Límite 1 — El Shapley climático tiene incertidumbre en la función
de valor. La función de valor v(S) = f(emisiones_acumuladas_S)
requiere el modelo de atribución climática que establece la relación
entre las emisiones acumuladas de una coalición y el nivel de
calentamiento producido. Esa relación tiene incertidumbre científica
que el IPCC cuantifica con intervalos de confianza. El Shapley
hereda esa incertidumbre — los rangos del análisis reflejan los
rangos del modelo de atribución.

Taxonomía General de Aplicaciones
Límite 2 — La inconmensurabilidad del D_climático irreversible. El
D_monetary_equiv del cambio climático es calculable en principio,
pero los componentes irreversibles — la extinción de ecosistemas
únicos, el desplazamiento permanente de comunidades, la pérdida
de la identidad cultural de los pueblos costeros que desaparecerán
bajo el agua — son inconmensurables con cualquier compensación
monetaria finita. El Δ_permanente del cambio climático es el mayor
de cualquier dominio de la Taxonomía.
Límite 3 — El Shapley es un instrumento técnico pero los
coeficientes de responsabilidad diferenciada son normativos. La
calibración de K_pre, K_post y K_2015 no es una decisión técnica
sino política: refleja el acuerdo de la comunidad internacional sobre
qué peso asignar al conocimiento histórico en la distribución de la
responsabilidad. El sistema establece los rangos posibles, pero no
puede determinar el valor justo sin ese acuerdo normativo.
— Fin del Capítulo 64 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

