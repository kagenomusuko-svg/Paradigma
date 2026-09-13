PARTE X · Ciencias Naturales y Medioambiente

## Capítulo 64

### Cambio climático — responsabilidad

### histórica en emisiones globales

Organ.  Estru.  Model.  Educa.  Crisi.

Para el mediador que busca precisión · Cómo usar este capítulo

Este capítulo es Nivel B: aplica el cap. 14 de El cálculo de la responsabilidad (Medio ambiente y ecología) al dominio del cambio climático y las emisiones históricas. El instrumento central es el valor de Shapley aplicado a la distribución de la responsabilidad climática: cuando ningún Estado, empresa o sector individual es condición necesaria del cambio climático global, el Shapley distribuye la responsabilidad proporcional a la contribución marginal promedio de cada emisor sobre todas las posibles coaliciones.

La singularidad del dominio climático es que produce la forma más pura del problema de causalidad acumulativa: el calentamiento global no es el resultado de ningún actor individual sino de la suma de las contribuciones de miles de emisores durante más de un siglo. R* convencional asigna cero a todos los actores porque ninguno es condición necesaria del daño global. El Shapley produce valores positivos para todos proporcionales a su contribución marginal real. Esos valores son la base técnica para el diseño de compromisos climáticos equitativos.

### §1  El problema de la causalidad climática: por qué R* convencional falla

El cambio climático es el caso de causalidad acumulativa más complejo de la Taxonomía: la desestabilización del sistema climático es el resultado de las emisiones de miles de actores durante más de

Taxonomía General de Aplicaciones

un siglo. Las emisiones de CO₂ y otros gases de efecto invernadero tienen la propiedad de que cada tonelada contribuye marginalmente al calentamiento global, pero ninguna tonelada individual es condición necesaria del daño en el sentido del postulado I5 del sistema — porque sin las emisiones de cualquier actor individual, el sistema climático habría sido desestabilizado de todas formas por la suma de los demás actores.

El fallo de R* convencional en este dominio es técnico y preciso: R* convencional requiere que P (daño_a_esa_escala | sin el actor_i) < P (daño | con el actor_i). Para el cambio climático global, sin las emisiones de ningún actor individual el sistema habría alcanzado prácticamente el mismo nivel de desestabilización — porque la cantidad de emisiones de cualquier actor individual (incluso los mayores emisores históricos) no es necesaria para producir el umbral de calentamiento que constituye el daño global. R* convencional = 0 para todos. El resultado es evidentemente incorrecto: los grandes emisores históricos son causalmente responsables del daño, aunque no sean causalmente necesarios individualmente.

El valor de Shapley climático: la solución al problema de causalidad acumulativa

φᵢ (Shapley) = Σ_{S⊆N\{i}} [|S|! (n−|S|−1) /n!] × [v(S∪{i}) −

v(S)] Donde v(S) es la función de valor de la coalición: el daño climático producido por la coalición S de actores operando juntos. El Shapley del actor i es su contribución marginal promedio a todas las coaliciones posibles que incluyen a ese actor. Para el cambio climático, v(S) = f(emisiones_acumuladas_S) — una función del total de emisiones de la coalición S. El Shapley produce valores positivos para todos los emisores proporcionales a su contribución marginal: los grandes emisores históricos tienen mayor Shapley que los pequeños emisores, aunque ninguno sea condición necesaria individualmente. Para grupos grandes de emisores (los 200+ países del sistema climático), el Shapley se aproxima con métodos de Monte Carlo: se generan K ordenamientos aleatorios del conjunto de actores, se calcula la contribución marginal de cada actor en cada ordenamiento, y se promedia. Con K ≥ 10,000 iteraciones, el estimador converge al Shapley exacto con error < 1%.

Taxonomía General de Aplicaciones

### §2  Escala de evidencia Am0–Am8

Tipo de evidencia en

Descripción Rango

Nivel

w

el dominio

climático

Am1 Inventarios nacionales de emisiones verificados + estudios de atribución climática con modelos de circulación general + análisis de detección y atribución con intervalo de confianza documentado

Los inventarios de emisiones verificados por el IPCC o por organismos de verificación independiente, combinados con estudios de atribución climática que establecen la contribución de las emisiones acumuladas al calentamiento observado con metodología documentada e intervalo de confianza estadístico.

[0.72, 0.90]

Am2 Inventarios de emisiones de organismos internacionales (IEA, EDGAR, GCP) con metodología documentada + estudios de atribución de segundo nivel

Los inventarios de emisiones de organismos internacionales reconocidos con metodología documentada, combinados con los estudios de atribución disponibles en la literatura científica revisada.

[0.60, 0.78]

Am3 Análisis convergente de múltiples inventarios de emisiones sobre el

La convergencia de dos o más inventarios de emisiones independientes sobre el mismo período y actor, que establecen un rango de emisiones acumuladas consistente.

[0.50, 0.68]

Taxonomía General de Aplicaciones

Tipo de evidencia en

Descripción Rango

Nivel

w

el dominio

climático

mismo período y actor

Am4 Estimaciones de emisiones desde proxies históricos (consumo de combustibles, producción industrial, datos de satélite) sin verificación directa

Las estimaciones de emisiones históricas calculadas desde proxies cuando los inventarios directos no están disponibles para el período analizado.

[0.36, 0.52]

Am5 Análisis de emisiones sectoriales sin desglose por actor específico

El análisis de las emisiones de un sector económico sin la capacidad de atribuirlas a actores individuales dentro del sector.

[0.18, 0.36]

Am0 Análisis Am1/Am2 que establece que el actor no produjo emisiones atribuibles en el período analizado

El análisis de inventario verificado que establece que las emisiones del actor en el período analizado son negligibles respecto al total o que el actor no operó como emisor en ese período.

w = 0.00

### §3  El protocolo Shapley para emisiones históricas

### §3.1  La distinción entre responsabilidad histórica y responsabilidad prospectiva

Taxonomía General de Aplicaciones

La responsabilidad climática tiene dos dimensiones que el análisis debe tratar separadamente. La responsabilidad histórica: la fracción del daño climático acumulado hasta la fecha atribuible a las emisiones históricas del actor. Esta es la dimensión del Shapley climático histórico — la distribución de la responsabilidad sobre el stock de emisiones acumuladas desde la Revolución Industrial. La responsabilidad prospectiva: la fracción del daño climático futuro que las emisiones actuales del actor producirán bajo los escenarios de trayectoria disponibles. Esta es la dimensión del Shapley climático prospectivo — la distribución de la responsabilidad sobre las emisiones proyectadas bajo distintos escenarios de mitigación.

Dimensión de

la responsabilidad

Instrumento del

sistema Resultado del análisis

climática

Responsabilidad histórica (stock de emisiones 1850–hoy)

La distribución de la responsabilidad histórica establece quién tiene mayor AD sobre los daños ya producidos por el cambio climático: los eventos de calor extremo, las inundaciones costeras, los desplazamientos de comunidades. El Shapley histórico es la base de los reclamos de «pérdidas y daños» de los países vulnerables al cambio climático.

Shapley histórico: φᵢ_hist = contribución marginal promedio de las emisiones acumuladas del actor i sobre todas las posibles coaliciones de emisores históricos. Las emisiones históricas se calculan con los inventarios de la base de datos Carbon Dioxide Information Analysis Center (CDIAC) y el Global Carbon Project (GCP).

Responsabilidad prospectiva (emisiones proyectadas bajo distintos escenarios)

Shapley prospectivo: φᵢ_prosp(S) = contribución marginal de las emisiones proyectadas del actor i en el escenario S sobre las emisiones totales necesarias para mantener el calentamiento por debajo del umbral establecido (1.5°C o 2°C). El presupuesto de carbono restante es el total de

La distribución de la responsabilidad prospectiva establece los compromisos de reducción de emisiones equitativos: la fracción del presupuesto de carbono restante que corresponde a cada actor dado su Shapley prospectivo. Es la base técnica para los Nationally Determined Contributions (NDCs) del Acuerdo de París.

Taxonomía General de Aplicaciones

Dimensión de

la responsabilidad

Instrumento del

sistema Resultado del análisis

climática

emisiones permitidas; el Shapley distribuye ese presupuesto entre los actores.

### §3.2  La responsabilidad diferenciada por época: el problema de las emisiones pre-industriales

El Shapley histórico tiene una dimensión temporal que el análisis debe incorporar: la responsabilidad de las emisiones históricas depende del conocimiento científico disponible en el período en que se produjeron. Las emisiones previas al Primer Informe del IPCC (1990) se produjeron en un contexto donde el conocimiento científico sobre el vínculo entre las emisiones de GEI y el calentamiento global no estaba consolidado en el consenso científico internacional. Las emisiones posteriores a 1990 — especialmente las posteriores a la Convención Marco de las Naciones Unidas sobre el Cambio Climático (UNFCCC, 1992) — se produjeron con conocimiento pleno del riesgo.

El operador H climático: la responsabilidad diferenciada por conocimiento

φᵢ_ajustado = φᵢ_pre1990 × K_pre + φᵢ_post1990 × K_post +

φᵢ_post2015 × K_2015 Donde K_pre es el coeficiente de conocimiento del período pre-1990 (menor responsabilidad atribuible por ausencia del consenso científico internacional consolidado), K_post es el coeficiente del período 1990–2015 (conocimiento establecido, pero compromisos voluntarios), y K_2015 es el coeficiente del período post-Acuerdo de París (responsabilidad plena con compromisos legalmente vinculantes). Los valores calibrados de los coeficientes son objeto de debate normativo — no son valores técnicos sino políticos. El análisis establece el rango: K_pre ∈ [0.30, 0.60], K_post ∈ [0.65, 0.85], K_2015 ∈ [0.90, 1.00].

Taxonomía General de Aplicaciones

### §4  Aplicación del Shapley climático: distribución de la responsabilidad histórica

La aplicación del Shapley histórico a las emisiones acumuladas de los principales actores climáticos produce una distribución que difiere significativamente de la distribución de las emisiones anuales actuales — porque incorpora la responsabilidad histórica que los grandes emisores del pasado acumularon durante el siglo XX. Los datos del Carbon Dioxide Information Analysis Center (CDIAC) establecen que los países industrializados producen aproximadamente el 75% de las emisiones acumuladas históricas a pesar de representar menos del 20% de la población mundial actual.

Emisiones acumuladas

φᵢ Shapley

Implicación

Actor /

para la responsabilidad

histórico (estimación)

Grupo

históricas

(aprox.)

Estados Unidos (1850–hoy)

~25% del total histórico acumulado

~22–28% según el período de inicio y el método de estimación de v(S). La contribución marginal de EEUU es alta porque era el mayor emisor individual hasta hace relativamente poco.

AD_EEUU sobre el D_climático acumulado es el más alto de cualquier actor individual. La base del reclamo de «pérdidas y daños» de los países vulnerables apunta en mayor proporción a EEUU.

Unión Europea (28 países, histórico)

~22% del total histórico acumulado

~18–24% del Shapley histórico colectivo de la UE.

La responsabilidad histórica colectiva de la UE es comparable a la de EEUU

Taxonomía General de Aplicaciones

Emisiones acumuladas

φᵢ Shapley

Implicación

Actor /

para la responsabilidad

histórico (estimación)

Grupo

históricas

(aprox.)

aunque sus emisiones per cápita actuales son menores.

China ~12% del total histórico acumulado (mayor emisor anual desde ~2007)

~10–14% del Shapley histórico. La contribución marginal de China es creciente en el período reciente.

El Shapley histórico de China es significativo pero menor que el de EEUU y la UE dados sus menores emisiones históricas acumuladas hasta fines del s. XX.

Resto del mundo desarrollado (Canadá, Australia, Japón, Rusia)

~25% del total histórico acumulado

~20–26% del Shapley histórico colectivo.

La responsabilidad histórica de los países desarrollados excede con creces su peso en la población mundial.

Países en desarrollo (resto del mundo)

~16% del total histórico acumulado

~12–18% del Shapley histórico colectivo.

Los países en desarrollo — que incluyen a los más vulnerables al cambio climático — son los que menos han contribuido al stock de emisiones que produce el daño que sufren.

Taxonomía General de Aplicaciones

El resultado más relevante del Shapley climático para la política pública: la inversión entre responsabilidad y vulnerabilidad

El Shapley histórico establece con precisión la inversión que hace que el cambio climático sea el caso más extremo de injusticia distributiva global: los países que menos han contribuido al stock de emisiones históricas (Shapley histórico bajo) son los que sufren los mayores daños climáticos (exposición alta a inundaciones, sequías, eventos de calor extremo y desplazamiento). Los países insulares del Pacífico, las naciones del Sahel africano, los países de los Andes con glaciares en retroceso — tienen Shapley histórico < 1% y sufren daños climáticos desproporcionados al 1% de las emisiones que produjeron.

### §4.1  La responsabilidad de las empresas de combustibles fósiles: el Shapley de emisiones de producto

Un análisis complementario del Shapley climático aplica el instrumento a las empresas de combustibles fósiles cuyos productos — el petróleo, el carbón, el gas natural extraídos y vendidos — son la fuente de las emisiones. El Carbon Disclosure Project (CDP) estableció en 2017 que 100 empresas de combustibles fósiles son responsables del 71% de las emisiones globales desde 1988. El análisis de Shapley de esas empresas distribuye la responsabilidad de esas emisiones proporcional a la producción de cada empresa.

Fracción de las

φᵢ Shapley de

Empresa /

emisiones globales (1988–

producto Implicación

Grupo

hoy)

Saudi Aramco

~4.4% de las emisiones globales del período

φ Aramco ≈ 4.0– 4.8% La empresa de mayor φ individual entre las empresas privadas y estatales de combustibles fósiles.

Chevron ~3.5% de las emisiones globales del período

φ Chevron ≈ 3.0– 4.0% Mayor φ individual entre las empresas privadas occidentales cotizadas.

Taxonomía General de Aplicaciones

Fracción de las

φᵢ Shapley de

Empresa /

emisiones globales (1988–

producto Implicación

Grupo

hoy)

ExxonMobil ~3.2% φ ExxonMobil ≈ 2.8–3.5% ExxonMobil conocía el vínculo entre sus emisiones y el cambio climático desde los años 1970– 1980 según documentos internos publicados posteriormente — el K_conocimiento de sus emisiones post-1990 es máximo.

~21% colectivo φ ≈ 18–23% colectivo

Las 5 mayores estatales (Saudi Aramco, Gazprom, NIOC, NNPC, KPC)

El Shapley de las grandes empresas estatales incluye la responsabilidad del Estado propietario.

### §5  El D_climático y la inconmensurabilidad del daño sistémico

El D_climático tiene la misma estructura de tres componentes que todos los dominios de la Taxonomía — pero su dimensión es sin precedentes en ningún otro dominio. El T_invertido climático son las pérdidas directas ya producidas: los muertos y los daños materiales de los eventos de calor extremo, las inundaciones, los huracanes más intensos que el sistema climático desestabilizado produce con mayor frecuencia e intensidad. El T_impedido son los servicios ecosistémicos perdidos durante el período de la desestabilización: la productividad agrícola reducida, el agua perdida por el retroceso de los glaciares, los recursos pesqueros diezmados por la acidificación del océano. El ΔT_trayectoria es el componente

Taxonomía General de Aplicaciones

más grande y el más difícil de cuantificar: la diferencia entre el potencial de desarrollo de las regiones y comunidades afectadas bajo el sistema climático estable y el potencial bajo el sistema desestabilizado.

D_climático_total = T_invertido + T_impedido + ΔT_trayectoria El D_monetary_equiv del cambio climático bajo el escenario de calentamiento de 2°C (el objetivo del Acuerdo de París): entre 2 y 10 billones de dólares anuales en pérdidas económicas globales según los distintos estudios de daños (Stern, 2006; Burke et al., 2015; IPCC, 2022). Para el escenario de 4°C (el escenario actual sin acción climática suficiente): entre 10 y 50 billones de dólares anuales en pérdidas — el 10– 25% del PIB global por año en el extremo superior del rango. Esas cifras son el D_monetary_equiv calculable del cambio climático. Lo que no es calculable con equivalente monetario — y que el sistema reconoce honestamente — es el valor intrínseco del Amazonas, del Gran Arrecife de Coral, de los sistemas culturales de las comunidades que el desplazamiento destruirá. Para esos componentes, el Δ_permanente del daño climático es inconmensurable.

§5.1  El mecanismo de pérdidas y daños (Loss and Damage) como α_diferido climático

El mecanismo de pérdidas y daños del Acuerdo de París (COP27, 2022) es la formalización institucional del α_diferido climático: el reconocimiento de que los grandes emisores históricos tienen la obligación de contribuir a las pérdidas y daños de los países vulnerables proporcional a su Shapley histórico. El fondo de pérdidas y daños establecido en COP27 tiene compromisos iniciales de menos de 800 millones de dólares — una fracción minúscula del D_total que el Shapley establece como responsabilidad proporcional de los grandes emisores.

Instrumento

Equivalente en el paradigma Escala actual

del sistema

climático

Fondo de pérdidas y daños (COP27)

α_diferido climático de los grandes emisores sobre el D_climático de los países vulnerables. AD =

~800M USD en compromisos iniciales vs. D_climático anual estimado de los países

Taxonomía General de Aplicaciones

Instrumento

Equivalente en el paradigma Escala actual

del sistema

climático

Shapley_histórico × D_climático_atribuible al actor.

más vulnerables de ~400B USD. El AD / D_total ≈ 0.2% — valor de α_diferido muy bajo para la magnitud del Shapley histórico.

Compromisos de reducción de emisiones (NDCs del Acuerdo de París)

α_anticipado climático: la fracción del daño futuro que el actor se compromete a prevenir mediante la reducción de sus emisiones prospectivas.

Los NDCs actuales producen un calentamiento proyectado de ~2.4– 2.7°C para 2100 — significativamente por encima del objetivo de 1.5°C del Acuerdo de París. El α_anticipado colectivo es insuficiente para el D_climático prospectivo que las emisiones actuales producirán.

Financiamiento climático para países en desarrollo

α_diferido sobre la fracción del T_impedido atribuible a la falta de acceso a tecnologías de mitigación y adaptación.

El compromiso de 100B USD anuales del Acuerdo de Copenhague no fue cumplido hasta 2022. La brecha de financiamiento climático para países en desarrollo se estima en 6–10 veces el financiamiento actual.

### §6  Preguntas que responde este capítulo

Pregunta Instrumento Nivel de certeza

¿Cuál es el Shapley histórico

Shapley histórico aplicado a los inventarios de emisiones

Declaración B con inventarios Am1/Am2

Taxonomía General de Aplicaciones

Pregunta Instrumento Nivel de certeza

del actor — qué fracción del daño climático acumulado es causalmente atribuible a sus emisiones?

verificados del actor en el período 1850–actual. La función de valor v(S) se construye desde la relación entre las emisiones acumuladas de la coalición S y la temperatura observada del sistema climático.

del actor + modelo de atribución climática documentado. El rango del Shapley tiene incertidumbre proporcional a la incertidumbre del modelo de atribución.

¿Qué responsabilidad diferenciada corresponde al período post-1990 vs. pre-1990?

Operador H climático: φᵢ_ajustado = φᵢ_pre1990 × K_pre + φᵢ_post1990 × K_post + φᵢ_post2015 × K_2015. El coeficiente K depende del estado del conocimiento científico en cada período.

Declaración B para los períodos con inventarios Am2/Am3 verificados. La calibración de K es normativa y requiere consenso político.

¿Cuál es el AD del actor sobre el D_climático de los países vulnerables?

AD_i = Shapley_histórico_i × D_climático_total_atribuible. El D_climático de los países más vulnerables puede estimarse desde los estudios de daños climáticos por país del IPCC.

Declaración C: el AD del actor individual sobre el D de un país específico requiere la cadena de atribución completa desde las emisiones hasta el evento de daño, que tiene incertidumbre alta.

### §7  Límites del método en el dominio climático

Límite 1 — El Shapley climático tiene incertidumbre en la función de valor. La función de valor v(S) = f(emisiones_acumuladas_S) requiere el modelo de atribución climática que establece la relación entre las emisiones acumuladas de una coalición y el nivel de calentamiento producido. Esa relación tiene incertidumbre científica que el IPCC cuantifica con intervalos de confianza. El Shapley hereda esa incertidumbre — los rangos del análisis reflejan los rangos del modelo de atribución.

Taxonomía General de Aplicaciones

Límite 2 — La inconmensurabilidad del D_climático irreversible. El D_monetary_equiv del cambio climático es calculable en principio, pero los componentes irreversibles — la extinción de ecosistemas únicos, el desplazamiento permanente de comunidades, la pérdida de la identidad cultural de los pueblos costeros que desaparecerán bajo el agua — son inconmensurables con cualquier compensación monetaria finita. El Δ_permanente del cambio climático es el mayor de cualquier dominio de la Taxonomía.

Límite 3 — El Shapley es un instrumento técnico pero los coeficientes de responsabilidad diferenciada son normativos. La calibración de K_pre, K_post y K_2015 no es una decisión técnica sino política: refleja el acuerdo de la comunidad internacional sobre qué peso asignar al conocimiento histórico en la distribución de la responsabilidad. El sistema establece los rangos posibles, pero no puede determinar el valor justo sin ese acuerdo normativo.

— Fin del Capítulo 64 —

Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

