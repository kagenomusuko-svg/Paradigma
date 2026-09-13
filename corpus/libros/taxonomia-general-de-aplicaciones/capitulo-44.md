PARTE VI · Ciencias Sociales y Humanidades

## Capítulo 44

### Ciencia política y procesos electorales

Organ.  Estru.  Model.  Educa.  Crisi.

### Organ.   Estru.  Model.   Educa.   Crisi.

Para el mediador que busca precisión · Cómo usar este capítulo

Este capítulo es Nivel B: deriva y amplía los instrumentos del paradigma para el dominio de la ciencia política y los procesos electorales. El dominio tiene una característica que lo distingue de todos los demás capítulos de la Parte VI: la causalidad opera tanto a nivel del acto individual —el funcionario que alteró el resultado, el algoritmo que suprimió el discurso político de un lado— como a nivel de la estructura sistémica —el diseño de los distritos electorales, las reglas de financiamiento de campaña, el sistema de acceso a los medios. El instrumento central del capítulo es el ILE (Índice de Legitimidad Electoral) — la medida de la brecha entre los procedimientos democráticos declarados de un proceso electoral y los procedimientos realmente implementados.

Los instrumentos de referencia principales de este capítulo son el IIC del cap. 35 (el IIC_político mide la congruencia entre los valores democráticos declarados y el comportamiento observable de las instituciones electorales), el cap. 13 (IA y algoritmos, para la manipulación algorítmica del discurso político) y el cap. 43 (distinción detonadora/estructura, para separar el fraude electoral individual del diseño sistémico que lo habilita).

Si tu caso es de fraude electoral directo (manipulación de actas o votos), ve a §1 sub-variante 1 y §5 configuración 1. Si es de manipulación de la información durante la campaña (desinformación, Cambridge Analytica tipo), ve a §3 y §5 configuración 2. Si es de supresión del voto por barreras estructurales o gerrymandering, ve a §5 configuración 3. Para la jerarquía de evidencia, ve directamente a §2.

Taxonomía General de Aplicaciones

Nota de calibración: rangos Nivel B — derivados por extensión desde los principios del sistema. Pendientes de calibración empírica con litigios electorales documentados.

### §1  Descripción del subcampo

La ciencia política y los procesos electorales son el dominio donde el daño producido por la manipulación del sufragio tiene una propiedad que ningún otro dominio de la Taxonomía comparte: el daño es simultáneamente individual —el votante cuyo voto fue suprimido, el candidato cuya victoria fue robada— y sistémico —la confianza en el proceso democrático como mecanismo de legitimación del poder político, cuya erosión produce daño a todos los miembros de la comunidad política independientemente de su preferencia electoral. El fraude electoral individual produce D_individual; la erosión sistemática de la confianza en el proceso produce D_sistémico, que puede superar al D_individual en varios órdenes de magnitud.

La distinción central del dominio es entre tres tipos de manipulación electoral con grafos causales distintos. La manipulación directa del resultado: la alteración de las actas, el relleno de urnas, la destrucción de votos. La manipulación del proceso: el diseño de los distritos electorales, las reglas de financiamiento de campaña, los requisitos de registro de votantes, el acceso a los medios — el conjunto de reglas que determinan quién puede competir y en qué condiciones. La manipulación del entorno informativo: la desinformación organizada, la supresión algorítmica del discurso político de ciertos grupos, la micro-segmentación de mensajes electorales con datos personales sin consentimiento. Cada tipo tiene un nodo de mayor R* distinto y una distribución distinta del S entre el actor individual y la estructura sistémica.

El ILE (Índice de Legitimidad Electoral) y el IIC_político

Taxonomía General de Aplicaciones

El ILE mide la brecha entre los procedimientos democráticos declarados de un proceso electoral —los establecidos en la constitución, la ley electoral y los estándares internacionales de derechos políticos— y los procedimientos realmente implementados. ILE ∈ [0, 1]: ILE = 1 indica la implementación completa de los procedimientos declarados; ILE = 0 indica la ausencia total de congruencia entre lo declarado y lo implementado.

ILE = corr (procedimientos_electorales_declarados,

procedimientos_electorales_implementados) El ILE es la aplicación del IIC (cap. 35) a las instituciones electorales: el IIC_político de un sistema electoral mide la congruencia entre sus valores democráticos declarados y su comportamiento observable. ILE bajo es la firma del fraude electoral sistémico: la institución electoral declara garantizar el sufragio libre y secreto mientras implementa procedimientos que lo distorsionan. R*_diseñador_del_sistema sobre el D_electoral es positivo proporcional a (1 − ILE).

### Sub-variantes del dominio electoral

Sub-variante Descripción y singularidades del dominio

Fraude electoral directo: manipulación de actas, relleno de urnas, destrucción de votos

La alteración directa del recuento de votos o de los documentos que lo registran. Es la sub-variante con mayor visibilidad mediática y menor R* sistémico en los sistemas democráticos consolidados: el fraude directo a escala suficiente para alterar el resultado de una elección nacional requiere la participación de decenas o cientos de funcionarios, lo que hace que la S de cada funcionario individual sea moderada-alta (cualquier otro funcionario en esa posición bajo las mismas instrucciones habría producido el mismo resultado) y el R* del diseñador del esquema de fraude sea el nodo dominante.

Gerrymandering y manipulación de los distritos electorales

El diseño de los límites de los distritos electorales de manera que concentra o dispersa a los votantes de ciertos grupos para maximizar la ventaja electoral del partido que controla el proceso de redistribución. Es la sub-variante de mayor S sistémica del dominio: el gerrymandering es legal en muchos sistemas y habitual en el sentido de que cualquier partido en la posición del diseñador haría lo mismo. El R* del

Taxonomía General de Aplicaciones

Sub-variante Descripción y singularidades del dominio

diseñador es alto cuando la manipulación produce resultados electorales sistemáticamente distintos de la preferencia popular y cuando el diseño fue idiosincrático respecto a los estándares técnicos disponibles.

Financiamiento ilegal de campañas: el dinero que distorsiona la competencia electoral

El financiamiento de campañas electorales con dinero de origen prohibido, con cantidades superiores a los límites legales, o sin la transparencia requerida. El R* del financiador sobre el daño a la competencia electoral es positivo proporcional a la condición causal del financiamiento sobre el resultado — la pregunta es si el candidato financiado habría ganado sin el financiamiento ilegal. Se conecta con el cap. 2 (PLD) para el análisis del origen de los fondos.

Supresión del voto: barreras estructurales que impiden el ejercicio del sufragio a ciertos grupos

El diseño de requisitos de registro, horarios de votación, accesibilidad de los centros de votación, y procesos de verificación de identidad que producen disparate impact sobre grupos específicos de votantes — que tienen menor tasa de ejercicio del sufragio como consecuencia de esas barreras, no de su preferencia. El análisis del disparate impact (test de los 4/5 del cap. 37) se aplica a las tasas de registro y participación electoral: si la tasa del grupo afectado es inferior al 80% de la del grupo de referencia controlando por las variables de acceso, hay supresión del voto estructural.

Manipulación del entorno informativo: desinformación, micro-segmentación y supresión algorítmica

La desinformación organizada durante la campaña electoral, la micro-segmentación de mensajes electorales con datos personales obtenidos sin consentimiento (Cambridge Analytica tipo), y la supresión algorítmica del discurso político de ciertos grupos o candidatos en las plataformas digitales. Se conecta con el cap. 13 (IA y algoritmos) para el análisis del R* del diseñador de la métrica del algoritmo sobre el sesgo político del contenido promovido. El D_electoral de la desinformación requiere establecer la brecha entre la preferencia informada del votante y la preferencia producida por la desinformación.

Interferencia extranjera en

Un Estado extranjero —o actores con respaldo estatal extranjero— intervino en el proceso electoral

Taxonomía General de Aplicaciones

Sub-variante Descripción y singularidades del dominio

elecciones: el Estado exterior como nodo del grafo electoral

de otro Estado mediante la desinformación, el financiamiento de campañas, la manipulación de la infraestructura tecnológica del proceso electoral, o el uso de sus activos de inteligencia para beneficiar a un candidato o partido. El R* del Estado extranjero sobre el daño a la integridad del proceso electoral es positivo proporcional a la condición causal de la interferencia sobre el resultado o sobre la confianza en el proceso.

Violencia e intimidación electoral: el uso de la fuerza para distorsionar el sufragio

El uso de la violencia física, la amenaza, o la intimidación para impedir el ejercicio del sufragio de ciertos grupos, para obligar a los votantes a votar en un sentido determinado, o para disuadir a candidatos de presentarse. Se conecta con el cap. 1 (derecho penal y civil) para el D_vital de las víctimas de la violencia electoral y con el cap. 43 (geopolítica) para el análisis de la estructura de impunidad que hace posible la violencia electoral sistemática.

### §2  Escala de evidencia Hi0–Hi8 aplicada al dominio electoral

La escala Hi0–Hi8 (Parte VI) se aplica en el dominio electoral con énfasis en los documentos del proceso electoral: las actas de escrutinio, los registros de votantes, los informes de los observadores electorales, los análisis estadísticos de los resultados, y los documentos del financiamiento de campaña. La característica más relevante del dominio es la posición de los análisis estadísticos de los resultados (Hi2): en el dominio electoral, la estadística de los resultados puede ser la fuente más robusta para detectar anomalías en el proceso, especialmente cuando el fraude fue diseñado para no dejar rastro documental directo.

Taxonomía General de Aplicaciones

Tipo de evidencia en

Descripción y ejemplos en

Rango

Nivel

el dominio electoral

w

procesos electorales

Hi1 Documentos primarios del proceso electoral con cadena de custodia verificada: actas de escrutinio, registros de votantes, documentos de financiamiento

Las actas de escrutinio originales firmadas por los representantes de los partidos en cada mesa de votación. Los registros de votantes con las firmas de los electores que ejercieron el sufragio. Los registros contables del financiamiento de campaña con los comprobantes de los ingresos y los gastos. Las grabaciones de las cámaras de los centros de votación donde se produjo la alteración. Son los documentos Hi1 del dominio: su existencia establece el nexo causal con el nivel de certeza más alto disponible.

[0.72, 0.90]

Hi2 Análisis estadístico de los resultados electorales con metodología documentada + informes de observadores electorales internacionales acreditados

El análisis estadístico de los resultados electorales que detecta anomalías inconsistentes con los mecanismos aleatorios del proceso: la prueba de Benford sobre la distribución de los dígitos de los resultados, el análisis de correlación entre los resultados y las características de las mesas de votación, el análisis de las discontinuidades en las series temporales del recuento. Los informes de las misiones de observación electoral de la OEA, la UE o la OSCE, que tienen acceso a los documentos y al proceso durante el día de la elección.

[0.62, 0.80]

Hi3 Testimonios convergentes de funcionarios del proceso electoral

Las declaraciones de funcionarios electorales, representantes de partidos en las mesas de votación, y

[0.52, 0.70]

Taxonomía General de Aplicaciones

Tipo de evidencia en

Descripción y ejemplos en

Rango

Nivel

el dominio electoral

w

procesos electorales

con corroboración documental parcial

personal de los centros de votación que describen consistentemente el mismo patrón de irregularidades, con al menos un documento institucional compatible con el patrón descrito. La convergencia desde múltiples testigos con posiciones distintas en el proceso aumenta el peso de la arista.

Hi4 Análisis del disparate impact en las tasas de participación electoral controlando por variables socioeconómicas

El análisis estadístico de las tasas de registro y participación electoral desagregadas por grupo: si la tasa del grupo afectado por las barreras estructurales es inferior al 80% de la tasa del grupo de referencia controlando por las variables socioeconómicas disponibles, hay supresión del voto estructural documentable (Hi4). El test de los 4/5 aplicado al dominio electoral.

[0.42, 0.60]

Hi5 Análisis comparado de los resultados electorales con el contexto electoral previo y las encuestas de opinión del período

La comparación entre el resultado electoral y las encuestas de opinión del período, las tendencias históricas del voto en ese territorio, y los resultados de elecciones simultáneas en territorios comparables — que establece si el resultado es estadísticamente consistente con el contexto o si presenta anomalías que requieren explicación.

[0.30, 0.50]

Hi6 Denuncias formales de los partidos o

Las denuncias formales presentadas por los partidos o candidatos afectados ante la

[0.16, 0.34]

Taxonomía General de Aplicaciones

Tipo de evidencia en

Descripción y ejemplos en

Rango

Nivel

el dominio electoral

w

procesos electorales

candidatos afectados ante la autoridad electoral

autoridad electoral o judicial, con la descripción de las irregularidades observadas y sin corroboración documental independiente todavía disponible.

Hi7 Testimonios de votantes sobre presión, intimidación o irregularidades sin corroboración documental

Los testimonios de votantes sobre la presión recibida, la intimidación, o las irregularidades observadas en el centro de votación, sin corroboración documental ni testimonial independiente.

[0.06, 0.20]

Hi8 Alegaciones de fraude o manipulación sin evidencia documental ni estadística

Las afirmaciones sobre fraude o manipulación electoral sin ningún respaldo documental, estadístico o testimonial verificable.

[0.02, 0.12]

Hi0 Análisis Hi2 que establece positivamente la ausencia de anomalías en el proceso

Análisis estadístico Hi2 que establece que los resultados electorales son consistentes con el contexto electoral previo y las distribuciones esperadas, y análisis Hi1 que establece que los documentos del proceso son coherentes y completos.

w = 0.00

La prueba de Benford y el análisis estadístico como Hi2 en el dominio electoral

La distribución de Benford establece que, en conjuntos de datos de origen natural, los primeros dígitos no tienen distribución uniforme: el dígito 1 aparece como primer dígito el 30% de las veces, el 2 el 17%, y así sucesivamente de forma logarítmica. Los resultados electorales legítimos tienden a seguir la distribución de Benford; las alteraciones sistemáticas del recuento producen desviaciones estadísticamente significativas de esa

Taxonomía General de Aplicaciones

distribución. Cuando el análisis estadístico detecta una desviación significativa (p < 0.05), establece un patrón de anomalía que requiere explicación — no prueba el fraude, pero desplaza la carga de la prueba hacia quien debe explicar la anomalía.

La posición del análisis estadístico en la escala Hi2 refleja que es el instrumento más potente disponible en muchos contextos electorales donde el acceso a los documentos primarios es limitado — pero que requiere el análisis metodológico riguroso por experto en estadística electoral para alcanzar ese nivel de certeza. Una aplicación incorrecta de la prueba de Benford (en elecciones con distritos pequeños donde la distribución no aplica) produce resultados Hi6 o Hi7, no Hi2.

### §3  El ILE, el IIC_político y los Hijos del actor electoral

El IIC_político de un sistema electoral o de una institución electoral es la aplicación del IIC del cap. 35 a la dimensión política: mide la congruencia entre los valores democráticos declarados de la institución —la garantía del sufragio libre, secreto, universal e igualitario— y su comportamiento observable en el diseño y la administración del proceso electoral. El IIC_político bajo produce el mismo daño que el IIC bajo en cualquier otra dimensión: erosiona la confianza en la institución, produce selección adversa de los candidatos y los participantes, y genera el ciclo de deslegitimación que debilita el sistema democrático como mecanismo de resolución pacífica de los conflictos políticos.

Hijo

Firma documenta

del actor electo

Qué informa

Fuente

R* resultante

l en el dominio electoral

típica

para S

ral

Antero s

S bajo [0.05– 0.28]. El actor diseñó deliberadam ente el

Correos y comunicacio nes internas que muestran el

Correos internos del equipo de campaña o del partido.

R*_actor pleno sobre el D_electoral . El Anteros

Taxonomía General de Aplicaciones

Hijo

Firma documenta

del actor electo

Qué informa

Fuente

R* resultante

l en el dominio electoral

típica

para S

ral

esquema de manipulació n electoral — el diseño de los distritos para maximizar la ventaja electoral, el sistema de requisitos de registro que excluye sistemáticam ente al grupo protegido, el esquema de financiamien to ilegal, la campaña de desinformaci ón. El resultado dependía de ese actor específico porque el diseño tenía rasgos idiosincrátic os que cualquier otro actor en esa posición no habría necesariame nte replicado.

propósito deliberado de la manipulació n. Datos que muestran el conocimient o del efecto discriminato rio antes de la implementa ción del diseño. Decisiones que rechazan alternativas menos manipulador as disponibles sin justificación documentad a.

Documento s del proceso de diseño de los distritos o los requisitos de registro. Análisis del efecto discriminato rio disponible en el período.

electoral es la base para la responsabili dad civil y potencialm ente penal por el daño a la integridad del proceso.

Potós S moderado-alto [0.40– 0.68]. El actor siguió

Diseño de los distritos o los requisitos de

Comparació n con los sistemas de otros

R*_actor moderado con S moderado-

Taxonomía General de Aplicaciones

Hijo

Firma documenta

del actor electo

Qué informa

Fuente

R* resultante

l en el dominio electoral

típica

para S

ral

las prácticas del sistema político del período — el gerrymander ing que todos los partidos practican cuando tienen la oportunidad, los requisitos de registro que son el estándar histórico del sistema, las prácticas de financiamien to que son habituales en el sector — sin que sus decisiones específicas fueran idiosincrática s respecto al estándar del período. El daño fue producido por prácticas habituales del sistema.

registro coherente con el estándar del sistema político del período. Ausencia de señales de propósito discriminato rio idiosincrátic o. Comparació n con las prácticas de otros actores en posiciones equivalentes que muestran el mismo patrón.

estados o jurisdiccione s del mismo período. Análisis del estándar del sistema político para el tipo de decisión analizada.

alto. El Potós establece que la reforma debe ser sistémica — cambiar las reglas que hacen racional el gerrymande ring — más que individual.

Fobos S moderado [0.30–0.55]. El actor adoptó prácticas de manipulació

Comunicaci ones internas donde el actor expresa

Comunicaci ones internas del equipo de campaña o del partido.

R*_actor moderado. El Fobos desplaza parte del R* hacia el

Taxonomía General de Aplicaciones

Hijo

Firma documenta

del actor electo

Qué informa

Fuente

R* resultante

l en el dominio electoral

típica

para S

ral

n electoral motivado por el miedo: el miedo a perder la elección, el miedo a que el partido oponente usara las mismas herramientas , el miedo a las consecuenci as de revelar la desinformaci ón que el equipo de campaña había diseñado. El Fobos produce la manipulació n electoral deshonesta-racional: el actor sabe que la práctica es éticamente cuestionable pero la adopta igualmente porque el sistema político hace que el costo de no hacerlo sea

preocupació n por la práctica que públicament e defiende. Evidencia de que la práctica fue adoptada como respuesta a prácticas equivalentes del oponente. Historial de decisiones que muestran la escalada de la manipulació n en respuesta a la manipulació n del oponente.

Comparació n con las prácticas del oponente en el mismo período.

sistema político que hace racional la escalada de la manipulaci ón — el equivalente de la presión del mercado de capitales en el C-suite corporativo .

Taxonomía General de Aplicaciones

Hijo

Firma documenta

del actor electo

Qué informa

Fuente

R* resultante

l en el dominio electoral

típica

para S

ral

mayor que el de hacerlo.

Deimo s

S alto [0.55– 0.82]. El actor genuinament e no anticipó el efecto discriminato rio de la práctica electoral adoptada, porque el análisis del disparate impact no era el estándar del sistema político del período o porque la tecnología disponible no permitía la detección de ese efecto antes de la implementac ión. El daño fue consecuenci a del riesgo sistémico de la práctica, no de la elección deliberada del actor.

Ausencia de análisis del disparate impact antes de la implementa ción. Respuesta inmediata y proporciona l del actor cuando el efecto discriminato rio fue documentad o. Práctica coherente con el estándar del sistema político del período sin desviación idiosincrátic a.

Análisis del estándar del sistema político del período. Velocidad y calidad de la respuesta del actor ante la primera evidencia del disparate impact.

R*_actor bajo. El Deimos establece que el daño fue consecuenc ia del riesgo sistémico. La reforma del estándar del sistema político es el instrument o correcto.

Taxonomía General de Aplicaciones

### §4  Tipos de nodo, tipos de arista y configuraciones canónicas del dominio

### Tipos de nodo en el grafo de responsabilidad electoral

R* en el grafo

Tipo de nodo Función en el

grafo S típico

de daño electoral

Diseñador del sistema electoral (DSE)

Diseñó las reglas del proceso electoral: los límites de los distritos, los requisitos de registro, las reglas de financiamiento , los procedimiento s de recuento. R* positivo cuando esas reglas produjeron el ILE bajo o el disparate impact documentado.

Moderado-bajo [0.22–0.48] cuando el diseño fue idiosincrático — las reglas específicas producían el efecto discriminatorio que otras reglas disponibles no habrían producido. Moderado-alto [0.48–0.70] cuando el diseño seguía el estándar del sistema político del período.

R*_DSE × D_electoral × (1 − α_DSE). El R*_DSE sobre el ILE bajo incluye el D_sistémico producido por la erosión de la confianza en el proceso electoral, no solo el D a los votantes específicos afectados.

Administració n electoral (AE)

Administró el proceso electoral — el registro de votantes, la organización del día de la elección, el recuento — con la calidad que el ILE requería. R* positivo cuando la administración fue deficiente

Alto [0.58– 0.82] cuando siguió el procedimiento institucional sin desviación idiosincrática, incluyendo los procedimientos deficientes diseñados por el DSE. Moderado [0.30–0.55] cuando las decisiones

Fracción del R*_DSE que corresponde a la ejecución deficiente o a la desviación idiosincrática del administrador respecto al procedimiento declarado.

Taxonomía General de Aplicaciones

R* en el grafo

Tipo de nodo Función en el

grafo S típico

de daño electoral

respecto al estándar que el ILE declarado imponía, o cuando ejecutó con Anteros la manipulación del resultado.

idiosincráticas del administrador fueron condición del fraude.

Candidato o partido beneficiado (CPB)

Fue el beneficiario del fraude o la manipulación electoral. R* positivo cuando diseñó, instruyó o conocía el fraude y no lo denunció. R* nulo cuando genuinamente no conocía el fraude producido por terceros en su beneficio.

Moderado-bajo [0.15–0.40] cuando el candidato o partido diseñó o instruyó el fraude. Alto [0.60–0.85] cuando el fraude fue producido por actores que actuaban «en su beneficio» sin su conocimiento ni instrucción.

Proporcional al conocimiento y la instrucción del fraude. El candidato que genuinamente no conocía el fraude de sus seguidores puede tener R* próximo a cero sobre el D_electoral — aunque tenga un deber de denuncia cuando lo descubra.

Plataforma digital (PD)

Gestionó el algoritmo que determinó qué contenido político fue promovido o suprimido durante la campaña electoral. R* positivo cuando el diseño de la métrica del algoritmo produjo sesgo político

Moderado [0.35–0.60] cuando la métrica del algoritmo era el estándar de la plataforma para todo el contenido, con el sesgo político como consecuencia no buscada del diseño. Moderado-bajo [0.20–0.38] cuando la

Fracción del D_electoral atribuible a la supresión o amplificación algorítmica del discurso político, calculada desde la diferencia entre el alcance real del discurso y el alcance que habría tenido con un

Taxonomía General de Aplicaciones

R* en el grafo

Tipo de nodo Función en el

grafo S típico

de daño electoral

sistemático — cuando la definición de «contenido relevante» o «contenido seguro» producía disparate impact sobre el discurso de ciertos partidos o candidatos.

métrica fue diseñada con conocimiento del sesgo político que producía.

algoritmo neutral.

Actor extranjero (AEX)

Un Estado o actor con respaldo estatal extranjero intervino en el proceso electoral. R* positivo proporcional a la condición causal de la interferencia sobre el resultado o sobre la confianza en el proceso.

Moderado-bajo [0.20–0.45] cuando la interferencia fue idiosincrática de ese actor extranjero específico (campañas de desinformación diseñadas específicamente , hackeo de la infraestructura electoral). Alto [0.55–0.78] cuando la interferencia aprovechó vulnerabilidade s estructurales del sistema de información electoral que cualquier actor extranjero bien equipado podría haber explotado.

R*_AEX × D_electoral × (1 − α_AEX). El α del actor extranjero en el dominio electoral es próximo a cero en la mayoría de los casos: la interferencia electoral es una acción que rara vez produce reconocimient o de la responsabilidad .

Taxonomía General de Aplicaciones

Configuraciones canónicas del dominio

Configuración 1 — Fraude electoral directo: el diseñador del esquema de fraude como nodo dominante

DSE / CPB (actor con Anteros documentado que diseñó el esquema de fraude: la instrucción de alterar las actas, el relleno de urnas en los centros de votación controlados por el partido, la destrucción de votos del oponente — S bajo [0.05–0.22] porque el diseño fue idiosincrático de ese actor) + AE (administradores electorales que ejecutaron el esquema con S moderado-alto [0.50–0.72]: cualquier funcionario bajo las mismas instrucciones y consecuencias habría producido el mismo resultado — Fobos dominante en la mayoría de los casos) → ILE bajo documentado con análisis Hi1/Hi2 → D_electoral_directo = diferencial de votos alterados × w_democrático El D_electoral_directo del fraude tiene dos componentes: el D a los candidatos y partidos afectados (el diferencial de resultado atribuible al fraude) y el D_sistémico a la confianza en el proceso (que puede superar al D_directo). AD_DSE = R*_DSE × D_total × (1 − α_DSE). El análisis del J del proceso post-fraude: cuando el sistema de consecuencias del fraude electoral tiene J bajo, la señal es que el fraude seguirá produciéndose.

Configuración 2 — Manipulación del entorno informativo: Cambridge Analytica (tipo)

Diseñador de la métrica del sistema de micro-segmentación (con Anteros documentado: definió «perfil psicográfico objetivo» usando datos personales obtenidos sin consentimiento para maximizar el impacto electoral del mensaje — S bajo [0.10–0.28] porque el uso específico de los datos sin consentimiento para la segmentación electoral era idiosincrático) + Plataforma que cedió los datos sin el consentimiento de los usuarios (con Potós: siguió las prácticas del sector del período sin verificar el uso final — S moderado-alto [0.45–0.65]) + Campaña que contrató el servicio (con Fobos: sabía que los métodos eran éticamente cuestionables pero los usó porque el oponente podría usarlos igualmente — S moderado [0.32–0.52]) → Micro-segmentación de mensajes electorales a ~87 millones de perfiles → D_electoral = diferencial en las preferencias de los votantes afectados atribuible a la desinformación

Taxonomía General de Aplicaciones

La aplicación del cap. 13 (IA y algoritmos) al dominio electoral: el diseñador de la métrica tiene R* dominante porque la decisión de definir «objetivo del mensaje» usando los perfiles psicográficos obtenidos sin consentimiento fue la condición normativa del sistema. S del equipo técnico ≈ 1.0: cualquier equipo técnico competente habría producido el mismo resultado con la misma métrica y el mismo dataset. Cambiar el equipo técnico no habría cambiado el sesgo. La reforma correcta: la regulación de la métrica (qué datos pueden usarse para la segmentación electoral y con qué consentimiento), no la sustitución del equipo técnico.

### Configuración 3 — Supresión del voto y gerrymandering: el diseño estructural como nodo dominante

DSE (partido que controlaba el proceso de redistribución de distritos, con Anteros documentado: el análisis racial de la distribución de votantes fue usado explícitamente para diseñar los distritos de manera que diluyera el poder electoral del grupo protegido — S moderado-bajo [0.22–0.40] cuando el diseño produjo un disparate impact idiosincrático respecto a los estándares técnicos alternativos disponibles) + DSE (legislatura que aprobó los requisitos de registro o identificación que producen disparate impact sobre el grupo protegido, con Potós en muchos casos: siguió el estándar del sistema político del período — S moderado-alto [0.48–0.68]) → Tasa de participación electoral del grupo protegido inferior al 80% de la tasa del grupo de referencia (test de los 4/5) → D_electoral = valor del sufragio suprimido × número de votantes afectados El análisis de la supresión del voto requiere distinguir la supresión idiosincrática (S bajo, Anteros dominante, reforma individual posible) de la supresión estructural (S alto, Potós dominante, reforma sistémica necesaria). Cuando el gerrymandering o los requisitos de registro eran el estándar del sistema político, la reforma individual del actor específico no resuelve el problema — la reforma de las reglas del juego es el instrumento correcto. El IAS_electoral mide en qué medida las reformas post-escándalo actuaron sobre el nodo estructural de mayor R*.

Taxonomía General de Aplicaciones

### §5  Preguntas que responde este capítulo

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

¿Hay ILE bajo — cuál es la brecha entre el proceso declarado y el implementado?

Análisis comparativo del proceso declarado (constitución, ley electoral, estándares internacionales) versus el proceso implementado (análisis estadístico Hi2 de los resultados, informes de observadores electorales Hi2, análisis del disparate impact Hi4). El ILE = corr(procedimientos declarados, procedimientos implementados) establece la base del R*_DSE sobre el D_electoral.

Declaración A con análisis estadístico Hi2 convergente + documentos Hi1 del proceso. Declaración B con análisis Hi3 de observadores + análisis estadístico Hi4. Declaración C cuando el ILE debe estimarse desde Hi5/Hi6 sin acceso directo al proceso.

¿El Hijo del actor electoral es Anteros, Fobos o Deimos — cuál es la idiosincrasia del daño?

Análisis de las comunicaciones internas del actor, la comparación con las prácticas de actores en posiciones equivalentes del mismo período, y la velocidad de respuesta ante las primeras evidencias del efecto discriminatorio. El Anteros produce S bajo; el Potós o el Fobos produce S moderado-alto; el Deimos produce S alto.

Declaración A con documentos Hi1 que muestran el conocimiento del efecto y la decisión de proceder. Declaración B con análisis Hi3 comparado con el estándar del sistema político del período. Declaración C cuando el Hijo debe inferirse sin acceso a las comunicaciones internas.

¿Hay disparate impact — el diseño produce supresión del voto de un grupo protegido?

Test de los 4/5 aplicado a las tasas de registro y participación: si la tasa del grupo protegido es inferior al 80% de la tasa del grupo de referencia controlando por las variables socioeconómicas disponibles, hay disparate

Declaración A con análisis Hi2 del disparate impact con las variables de control adecuadas. Declaración B con análisis Hi4 del disparate impact desde los datos

Taxonomía General de Aplicaciones

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

impact prima facie. El análisis de regresión logística con las variables de control establece si el disparate impact persiste después de controlar por los factores legítimos.

disponibles sin el conjunto completo de controles.

¿La interferencia extranjera fue condición necesaria del resultado — cuál es su R*?

Análisis del mecanismo causal de la interferencia: ¿la campaña de desinformación o el hackeo de la infraestructura electoral fue condición necesaria del resultado observado o del deterioro de la confianza en el proceso? La comparación con elecciones equivalentes sin la interferencia establece el contrafáctico.

Declaración B con análisis Hi3/Hi4 del mecanismo de la interferencia y su relación causal con el resultado. Declaración A con documentos Hi1/Hi2 desclasificados sobre las operaciones del actor extranjero.

¿Cuál es el D_electoral total — incluyendo el D_sistémico a la confianza en el proceso?

D_electoral = D_directo (diferencial de votos o de participación atribuible a la manipulación) + D_sistémico (daño a la confianza en el proceso electoral como mecanismo de legitimación). El D_sistémico se estima desde el análisis del impacto del escándalo sobre la participación electoral y la confianza institucional en el período posterior.

Declaración B con análisis Hi4/Hi5 del D_directo desde los datos electorales + análisis del D_sistémico desde las encuestas de confianza institucional del período posterior.

### §6  Traducción de D_total al dominio electoral

Taxonomía General de Aplicaciones

### D_electoral = D_sufragio + D_representación +

D_sistémico_democrático El daño en el dominio electoral tiene tres componentes con nodos causales distintos. El D_sufragio es el daño al votante individual cuyo voto fue suprimido, alterado, o coaccionado: el valor del sufragio individual en términos del derecho político suprimido, calculado desde el impacto del voto suprimido sobre el resultado final. El D_representación es el daño a la colectividad cuya representación política fue distorsionada por el fraude o la manipulación estructural: el diferencial entre la representación que el resultado legítimo habría producido y la representación real. El D_sistémico_democrático es el daño a la confianza en el sistema democrático como mecanismo de legitimación del poder político: el costo de la erosión de la confianza institucional medido desde el impacto sobre la participación política y la estabilidad democrática.

Fuente

En el dominio electoral

de evidenc

Componente

Cómo se cuantifica

ia

D_sufragio (daño al derecho político del votante individual)

El daño al votante cuyo voto fue suprimid o, alterado o coaccion ado: el ejercicio del derecho fundame ntal al sufragio libre y secreto, cuya privación constituy e un daño al votante individual con

El valor del sufragio individual no tiene precio de mercado — es un derecho fundamental. El D_sufragio se cuantifica desde el impacto del voto suprimido sobre el resultado: si N votos fueron suprimidos en un distrito que se decidió por M votos (M < N), la supresión fue condición necesaria del resultado en ese distrito.

Análisis estadísti co Hi2 del número de votos suprimid os por las barreras estructur ales o el fraude. Compar ación con la participa ción esperada sin la manipul ación desde el análisis

Taxonomía General de Aplicaciones

Fuente

En el dominio electoral

de evidenc

Componente

Cómo se cuantifica

ia

independ encia del resultado final de la elección.

del disparat e impact.

D_representaci ón (daño colectivo a la representación política distorsionada)

El daño a la colectivid ad cuya represent ación política fue distorsio nada por el fraude o el gerryman dering: el diferencia l entre la distribuci ón de escaños o cargos que el resultado legítimo habría producid o y la distribuci ón real.

D_representación = diferencial de escaños × período de distorsión × costo estimado de la política adoptada con la representación distorsionada versus la política que habría adoptado la representación legítima. Para el gerrymandering: el diferencial de escaños entre el plan de redistribución manipulado y el plan neutral técnicamente optimizado.

Análisis Hi2 de los planes de redistrib ución alternati vos técnica mente neutrale s. Análisis del resultad o electoral bajo los distintos planes. Historial de votacion es del período para estimar el D de la represen tación distorsio nada.

D_sistémico_d emocrático (daño a la

El daño a la confianza

D_sistémico = caída_en_la_participación _electoral × período ×

Encuest as de confianz

Taxonomía General de Aplicaciones

Fuente

En el dominio electoral

de evidenc

Componente

Cómo se cuantifica

ia

confianza en el sistema democrático)

institucio nal en el sistema democrát ico como mecanis mo de legitimaci ón del poder político, producid o por la percepció n de que el proceso electoral está manipula do. La erosión de la confianza reduce la participac ión electoral y aumenta la polarizaci ón política, producie ndo un ciclo de deslegiti mación con efectos de largo plazo.

costo_unitario_de_la_part icipación_perdida + aumento_en_la_polarizaci ón × período × costo_estimado_de_la_po larización. Estimable desde el análisis del impacto de escándalos electorales documentados sobre la participación electoral y las encuestas de confianza institucional.

a instituci onal del período anterior y posterio r al escándal o electoral . Datos de participa ción electoral del período. Análisis compara do del impacto de escándal os electoral es similares en contexto s compara bles.

Taxonomía General de Aplicaciones

### §7  Límites del método y errores frecuentes de aplicación

Límite 1 — El contrafáctico del resultado electoral «legítimo» tiene incertidumbre alta. El D_electoral requiere estimar cuál habría sido el resultado sin la manipulación — un contrafáctico que requiere supuestos sobre el comportamiento del votante que rara vez tienen el nivel de certeza de Hi2. El análisis debe declarar explícitamente la incertidumbre del contrafáctico y presentar el D_electoral como un rango.

Límite 2 — La prueba de Benford tiene limitaciones específicas en elecciones con distritos pequeños. La distribución de Benford aplica a conjuntos de datos suficientemente grandes: en elecciones con distritos de pocos cientos de votantes, la distribución esperada no es benfordiana y el análisis puede producir falsos positivos. La aplicación de la prueba de Benford como Hi2 requiere verificar que el tamaño del conjunto de datos cumple los requisitos estadísticos del test.

Límite 3 — La manipulación del entorno informativo tiene causalidad difusa. La relación entre la desinformación o la micro-segmentación y la preferencia electoral del votante no es directamente observable: el votante afectado por la desinformación puede haber llegado a la misma preferencia por otras vías. El D_electoral de la manipulación informativa debe presentarse con incertidumbre alta — Hi5 en la mayoría de los casos — excepto cuando los experimentos controlados del período establecen el efecto causal de la técnica específica usada.

Errores frecuentes de aplicación

Taxonomía General de Aplicaciones

Error Por qué

Consecue

ncia Corrección

ocurre

Concentrar el R* en el ejecutor visible del fraude ignorando al diseñador del esquema

El funcionario que alteró las actas o el que intimidó a los votantes es el actor más visible del proceso. El analista le atribuye el 100% del R* sin analizar quién diseñó el esquema.

R*_DSE subestimad o. El diseñador del esquema evade la responsabil idad mientras el ejecutor visible asume el R* completo — la inversión causal clásica.

La primera pregunta del análisis electoral: ¿quién diseñó el esquema? ¿El ejecutor actuó bajo instrucciones (S alto) o tomó la iniciativa de manera idiosincrática (S bajo)?

Usar alegaciones de fraude (Hi8) como base del análisis sin evidencia estadística o documental

Las alegaciones de fraude electoral son políticament e frecuentes. El analista las usa como base del grafo sin verificar con análisis estadístico Hi2 o documentos Hi1.

El análisis reproduce las alegaciones del actor afectado sin verificació n. R* asignado sin respaldo evidencial adecuado.

El análisis electoral debe comenzar por el nivel Hi2 — el análisis estadístico de los resultados — antes de usar los testimonios o las alegaciones de las partes. Sin Hi2 disponible, declarar Declaración C con incertidumbre alta.

No incluir el D_sistémico_dem ocrático en el D_electoral

El análisis calcula el D_sufragio y el D_represent ación sin considerar el daño a la

D_electora l subestimad o. El fraude que erosiona la confianza en el

El D_sistémico_dem ocrático debe incluirse siempre en el análisis electoral, aunque su cuantificación tenga mayor

Taxonomía General de Aplicaciones

Error Por qué

Consecue

ncia Corrección

ocurre

confianza institucional en el sistema democrático .

proceso tiene consecuen cias de largo plazo que superan el D del episodio específico.

incertidumbre. La erosión de la confianza en el proceso es el D más importante de los escándalos electorales de gran escala.

Ignorar el S del sistema político al analizar el gerrymandering como acto individual

El análisis atribuye el gerrymander ing al partido específico que controló el proceso de redistribució n sin considerar que cualquier otro partido en esa posición habría hecho lo mismo.

R*_DSE sobreestim ado. La reforma propuesta se dirige a sustituir al partido diseñador en lugar de a cambiar las reglas que hacen racional el gerrymand ering.

El S del gerrymandering es el instrumento que distingue la manipulación idiosincrática (S bajo → reforma individual posible) de la manipulación sistémica (S alto → reforma de las reglas del sistema es el instrumento correcto).

### §8  Guía de prioridades de recolección de evidencia en ciencia política y procesos electorales

Taxonomía General de Aplicaciones

La evidencia

Si tu incertidumbre

Por qué funcion

Qué rango reduce

Qué buscar

que más la reduce

/ qué preguntar

principal es...

a

es...

### 1. ¿Hay ILE bajo — existe la brecha entre el proceso declarado y el implementado?

Análisis estadístico Hi2 de los resultados electorales + informes de observado res electorales Hi2. Test de Benford sobre la distribuci ón de los resultados si el conjunto de datos es suficiente mente grande.

El ILE bajo es la base de toda la responsa bilidad del dominio. Sin establece rlo primero, el análisis no puede distribuir el R* entre los actores.

Establec e el ILE y el R*_DS E (incertid umbre estructur al central).

¿Los resultados son consistentes con el contexto electoral previo y las encuestas del período? ¿La distribución de los resultados sigue los patrones estadísticos esperados? ¿Los informes de observadores identificaron irregularidad es documentad as?

### 2. ¿El diseño produce disparate impact — hay supresión del voto de un grupo protegido?

Test de los 4/5 en las tasas de registro y participaci ón electoral desagrega das por grupo + análisis de regresión con variables de control

El disparate impact establece la base del R*_DSE sobre la supresió n del voto. Sin él, el análisis no puede distingui r la baja participa

Establec e el disparat e impact y el tipo de supresió n (idiosinc rática vs. estructur al).

¿Las tasas de registro y participación del grupo protegido son inferiores al 80% de las del grupo de referencia? ¿La diferencia persiste después de controlar por las variables socioeconóm

Taxonomía General de Aplicaciones

La evidencia

Si tu incertidumbre

Por qué funcion

Qué rango reduce

Qué buscar

que más la reduce

/ qué preguntar

principal es...

a

es...

socioecon ómicas.

ción por elección del votante de la baja participa ción por barreras estructur ales.

icas? ¿Las barreras afectan desproporcio nalmente al grupo protegido?

### 3. ¿El Hijo del actor electoral es Anteros o Deimos — cuál es el S del diseño?

Análisis comparad o del diseño con el estándar del sistema político del período + document os internos del proceso de diseño si están disponible s.

El Hijo determin a el S y el instrume nto correcto de reforma (individu al vs. sistémica ). Anteros → reforma individua l posible y necesaria . Potós/D eimos → reforma sistémica de las reglas del juego.

Establec e el S del actor y la distribuc ión entre reforma individu al y sistémic a.

¿Hay alternativas técnicas al diseño que producen menor disparate impact y que estaban disponibles en el período? ¿El actor rechazó esas alternativas sin justificación documentad a? ¿Las prácticas de actores equivalentes del período son similares al diseño analizado?

### 4. ¿La plataforma digital tiene R* por sesgo

Análisis de la métrica del

El R* de la platafor ma sobre

Establec e el R*_PD sobre la

¿La definición de «contenido seguro» o

Taxonomía General de Aplicaciones

La evidencia

Si tu incertidumbre

Por qué funcion

Qué rango reduce

Qué buscar

que más la reduce

/ qué preguntar

principal es...

a

es...

algorítmico político — cuál fue la métrica?

algoritmo de la plataform a: ¿cuál era la definición de «contenid o relevante» o «contenid o seguro» aplicada al discurso político? ¿Esa definición producía disparate impact sobre el discurso de ciertos grupos?

el sesgo político es proporci onal al diseño de la métrica, no al modelo técnico. El modelo es S ≈ 1.0 (cualquie r modelo con la misma métrica y el mismo dataset habría producid o el mismo sesgo).

supresió n algorítm ica del discurso político.

«contenido relevante» de la plataforma era neutral respecto al contenido político? ¿El análisis del disparate impact sobre el alcance del contenido electoral de distintos grupos está documentad o?

### 5. ¿Cuál es el D_sistémico_d emocrático — la confianza en el proceso fue erosionada?

Encuestas de confianza institucion al del período anterior y posterior al escándalo. Datos de participaci ón electoral del

El D_sisté mico puede dominar el D_electo ral total en los escándal os de gran escala. Sin él, el AD del

Establec e la escala del D_sisté mico y el AD total del DSE.

¿Las encuestas de confianza institucional cayeron después del escándalo? ¿La participación electoral en la siguiente elección fue inferior a la esperada? ¿Los datos de

Taxonomía General de Aplicaciones

La evidencia

Si tu incertidumbre

Por qué funcion

Qué rango reduce

Qué buscar

que más la reduce

/ qué preguntar

principal es...

a

es...

período posterior. Análisis comparad o del impacto de escándalo s electorales similares.

DSE es menor del que le correspo nde.

confianza en el proceso electoral del período posterior son comparables con los de jurisdiccione s sin escándalo?

### Árbol de decisión en ciencia política y procesos electorales

¿El caso es de fraude directo, manipulación informativa o supresión estructural del voto? │

├─ ANÁLISIS A: FRAUDE ELECTORAL DIRECTO

│  └─  PRIORIDAD 1: Análisis estadístico Hi2 + documentos Hi1 → ILE bajo documentado

│         · Anomalía en la distribución de los resultados → ILE positivo → R*_DSE dominante. │  └─  PRIORIDAD 2: ¿El ejecutor actuó bajo instrucciones (S alto) o por iniciativa (S bajo)?

│         · S alto del ejecutor → R* migra al DSE. Fraude annona electoral. │  └─  PRIORIDAD 3: D_electoral = D_sufragio + D_representación + D_sistémico

├─ ANÁLISIS B: MANIPULACIÓN INFORMATIVA

│  └─  PRIORIDAD 1: ¿Cuál fue la métrica del sistema de segmentación o desinformación?

│         · Métrica idiosincrática (S bajo) → R*_diseñador dominante. Cap. 13 para el análisis.

Taxonomía General de Aplicaciones

│  └─  PRIORIDAD 2: ¿La plataforma cedió datos sin consentimiento informado?

│         · Cesión de datos con Potós → R*_plataforma moderado. │  └─  PRIORIDAD 3: D_electoral = diferencial de preferencias atribuible a la desinformación (Hi5/C)

└─ ANÁLISIS C: SUPRESIÓN ESTRUCTURAL DEL VOTO

└─  PRIORIDAD 1: Test de los 4/5 en las tasas de participación del grupo protegido

· Tasa_grupo / Tasa_referencia < 0.80 → disparate impact prima facie. └─  PRIORIDAD 2: ¿El diseño fue idiosincrático (Anteros, S bajo) o el estándar del período (Potós, S alto)?

· S alto → reforma de las reglas del sistema. S bajo → reforma del actor y del diseño. └─  PRIORIDAD 3: D_electoral = D_sufragio_suprimido + D_representación_distorsionada

└─ Paso 2: ¿El D_sistémico_democrático es significativo — la confianza fue erosionada?

├─ SÍ → D_total incluye D_sistémico → AD_DSE aumenta significativamente

│  └─  AD_DSE = R*_DSE × (D_sufragio + D_representación + D_sistémico) × (1 − α_DSE). └─ NO (fraude local sin impacto en la confianza general) → D_total = D_directo

└─  AD_DSE = R*_DSE × D_directo × (1 − α_DSE).

### — Fin del Capítulo 44 —

Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

