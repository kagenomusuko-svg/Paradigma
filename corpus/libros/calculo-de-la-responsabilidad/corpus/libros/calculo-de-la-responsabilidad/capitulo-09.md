# Capítulo 9
## Análisis de quiebra y riesgo sistémico

*El índice de concentración de riesgo causal: quién hizo inevitable el colapso*

---

### §1.  El problema

El 15 de septiembre de 2008 a las 1:45 de la madrugada, Lehman Brothers Holdings Inc. presentó su solicitud de quiebra ante el tribunal federal de Manhattan. Era la quiebra corporativa más grande de la historia de los Estados Unidos: 613,000 millones de dólares en activos declarados. En las horas siguientes, los mercados financieros globales entraron en pánico. El crédito interbancario se congeló. Empresas en todo el mundo que no tenían ninguna relación con Lehman no pudieron renovar sus líneas de crédito. En los meses siguientes, la crisis financiera global que el colapso de Lehman desencadenó o aceleró se tradujo en 30 millones de personas desempleadas en el mundo, en el equivalente a una contracción de 22 billones de dólares de riqueza global, y en el mayor programa de rescate de instituciones financieras con fondos públicos de la historia.

La narrativa política dominante sobre la crisis de 2008 atribuyó el colapso principalmente a la codicia de los bancos de inversión, con Lehman como el caso más visible. Esa narrativa no es completamente incorrecta —la codicia de


Lehman existía y tenía posición causal en el grafo. Pero es radicalmente incompleta: pone el 100% del foco narrativo en el nodo que hizo quiebra cuando los nodos que hicieron posible el sistema que produjo la quiebra tenían R* comparable o mayor y casi ningún Δ positivo al final del proceso.

Los CDOs (Collateralized Debt Obligations) que Lehman y otros bancos empaquetaron tenían necesariamente una calificación de las agencias para poder venderse a los inversores institucionales. Las agencias calificadoras — Moody's, S&P, Fitch— asignaban calificaciones AAA a instrumentos que sus propios analistas sabían que no las merecían, porque su modelo de negocio los incentivaba a complacer a los emisores que les pagaban. Los reguladores de la Reserva Federal observaron el crecimiento de la burbuja durante años con instrumentos que habrían permitido intervenir y no los usaron. Los legisladores diseñaron el marco de desregulación financiera de los años 1990 que hizo posible la escala del riesgo sistémico. Lehman fue quien quebró. Pero ninguno de esos actores fue el único que lo hizo posible.

Para la empresa mediana que enfrenta un riesgo de quiebra mucho menos espectacular —un proveedor único que falla, un cliente que concentra el 80% de los ingresos y se pierde, un covenant de deuda que se incumple en la primera crisis de liquidez— el mismo instrumento aplica con la misma precisión: el índice de concentración de riesgo sistémico (R*) identifica qué nodo de la red de dependencias de la empresa es condición necesaria del colapso. No para asignar culpa sino para diseñar la intervención que puede evitarlo.

#### 1.1 La diferencia entre riesgo sistémico y riesgo individual


El riesgo financiero convencional es un cálculo sobre la probabilidad de que un actor individual incumpla sus obligaciones. El riesgo sistémico es algo diferente y más difícil: la probabilidad de que la interconexión entre actores produzca un colapso en cascada que ninguno de ellos habría producido individualmente. Lehman no era el único banco con posiciones de riesgo excesivas en 2008. Pero era el nodo cuya quiebra —dadas las interdependencias del sistema— tenía suficiente R* sobre el conjunto como para desencadenar el colapso en cascada.

Riesgo sistémico causal (R*):  En el análisis de quiebra, R* mide cuánto del colapso sistémico total dependía causalmente de cada nodo específico. R* alto de un nodo significa que ese nodo era condición necesaria del colapso a esa escala. R* bajo significa que el colapso habría ocurrido de manera similar incluso sin ese nodo. Esta distinción no se captura con ninguna medida de riesgo convencional porque las medidas convencionales son por definición individuales.

La distinción entre riesgo sistémico y riesgo individual es también la distinción entre el análisis de quiebra convencional —que pregunta "¿estaba Lehman en quiebra técnica?"— y el análisis causal —que pregunta "¿sin Lehman, habría ocurrido la crisis de 2008 con la misma escala?"—. La primera pregunta tiene respuesta fácil. La segunda es la que importa para el diseño de la regulación futura.

#### 1.2 El índice de concentración de riesgo sistémico

El índice de concentración de riesgo sistémico (ICRS) es la aplicación de R* al grafo de interdependencias financieras de un sistema. Para una empresa, el ICRS identifica qué nodo de su red de proveedores, clientes, acreedores e instrumentos financieros es condición necesaria de su


quiebra. Para un sistema financiero, identifica qué institución, instrumento o política es condición necesaria del colapso sistémico.

ICRS_i = R*ᵢ   sobre el grafo de interdependencias

financieras

Un ICRS alto del nodo i significa que el colapso del sistema dependía causalmente de ese nodo —ya sea porque era un puente necesario en la red de transmisión del riesgo, porque su quiebra activaba cláusulas que producían quiebras en cascada, o porque su existencia era condición para que otros nodos mantuvieran su solvencia.

Concentración de riesgo:  La propiedad más importante del ICRS para el análisis preventivo es que puede calcularse antes del colapso: se construye el grafo de interdependencias de la empresa o del sistema, se estiman los pesos de las dependencias, y se calcula R*. Un ICRS alto en un nodo específico es la señal de que ese nodo es el eslabón más débil — no necesariamente en términos de su propia solvencia, sino en términos de lo que su fallo provocaría en el sistema.

#### 1.3 Por qué los hijos no aplican en este dominio

En el análisis de quiebra y riesgo sistémico, los hijos de Afrodita no aplican en ningún nodo. La razón es la misma que en el caso del dataset del Capítulo 8: los nodos del grafo financiero —los CDOs, las calificaciones crediticias, los covenants de deuda, las líneas de crédito interbancario— son instrumentos financieros sin voluntad propia. Y los nodos humanos (los directivos, los reguladores, los analistas) aparecen en el análisis de quiebra no como individuos con disposiciones de voluntad sino como nodos funcionales en el grafo de interdependencias.

El análisis de los hijos de los directivos de Lehman o de los reguladores de la Fed pertenece al Capítulo 1 (derecho penal


y civil) cuando hay imputación de responsabilidad individual, o al Capítulo 3 (derecho internacional) si hay responsabilidades de política pública. En este capítulo, el análisis es del sistema, no de las personas que operaron dentro de él. Esa es la precisión que el dominio requiere: el colapso de Lehman no fue un fracaso de la voluntad de sus directivos sino de la arquitectura del sistema en el que operaban.


### §2.  Página puente — Traducción al lenguaje del análisis financiero

Esta página resume las herramientas del sistema en el contexto del análisis de quiebra y riesgo sistémico. El lector con formación en finanzas corporativas, gestión de riesgo o regulación financiera puede comenzar aquí.

Herramienta En quiebra y riesgo sistémico se llama

Qué significa

Grafo causal G

Red de interdependencias financieras

El mapa de todas las dependencias que conectan la empresa o la institución con su entorno: proveedores, clientes, acreedores, instrumentos financieros, reguladores. Las aristas son las dependencias causales.

R* (vector) ICRS — Índice de Concentración de Riesgo Sistémico

La fracción del colapso sistémico causalmente atribuible a cada nodo de la red. ICRS alto indica que el colapso del sistema depende causalmente de ese nodo. Es la medida de "too big to fail" formalizada.

Nodo de diseño

Arquitecto del sistema de riesgo

El nodo que diseñó las condiciones bajo las cuales el riesgo sistémico era posible: el regulador que diseñó el marco de


desregulación, el banco que estructuró los CDOs, la agencia calificadora que asignó ratings incorrectos.

Nodo instrumental

Instrumento financiero (CDO, CDS, covenant)

Un instrumento financiero que no tiene voluntad, pero tiene posición causal real: los CDOs eran condición necesaria de la escala de la crisis de 2008. Su ICRS apunta hacia quien los diseñó y calificó.

S (índice) Fungibilidad sistémica del nodo

S alto: cualquier institución equivalente en esa posición habría producido el mismo riesgo sistémico. El colapso era una propiedad del sistema, no de Lehman específicamente. S bajo: las características idiosincráticas de Lehman (su exposición específica, su ratio de apalancamiento) eran determinantes.

α (coeficiente) Provisión y mitigación del riesgo

En quiebra corporativa: las reservas de capital, los colchones de liquidez, las estrategias de cobertura, la diversificación de la cartera. α = 0: sin provisión. α = 1: riesgo completamente mitigado con capital o cobertura.

Δ = R* − α Déficit de provisión: riesgo

La brecha entre el riesgo sistémico que el nodo portaba y la provisión


sistémico no mitigado

que tenía. Δ alto positivo en un nodo de diseño regulatorio significa que el diseño del sistema cargaba más riesgo del que estaba provisionado.

D_total Daño sistémico del colapso

T_invertido (pérdidas directas en el evento de colapso), T_impedido (crédito no otorgado, inversión no realizada, empleo no generado durante la recesión), ΔT_trayectoria (pérdida persistente de potencial de crecimiento de largo plazo).

B_total Beneficio extraído del sistema de riesgo

Lo que los nodos de diseño obtuvieron del sistema: las comisiones por estructuración de CDOs, los ratings fees de las agencias calificadoras, las bonificaciones pagadas antes del colapso. Base para la acción de enriquecimiento sin causa.

El Estado diseñó un marco de desregulación que permitió el riesgo sistémico, recibió el capital fiscal de los ciudadanos, y luego usó fondos públicos para rescatar las instituciones que generaron el riesgo. El Δ del nodo regulatorio es la medida de ese incumplimiento.

Fraude annona

Incumplimiento regulatorio del Estado


Para el lector que viene del núcleo universal:  Este dominio no aplica hijos. Los nodos del grafo son instituciones e instrumentos financieros, no personas con disposición de voluntad. Cuando hay responsabilidad individual de directivos o reguladores, ese análisis pertenece al Capítulo 1. Este capítulo analiza la arquitectura del riesgo, no las intenciones de quienes la diseñaron.


### §3.  Las herramientas en el contexto del análisis de quiebra

#### 3.1 El grafo de interdependencias financieras

El grafo de quiebra y riesgo sistémico tiene una estructura dual: el grafo del riesgo interno (las dependencias dentro de la empresa o institución) y el grafo del riesgo externo (las dependencias con el entorno financiero). Un colapso puede ser causado por factores internos, externos o por la interacción de ambos.

Capa del grafo

Tipo de nodo

Aristas típicas

Fuente de evidencia para w

Ingresos Clientes, contratos, productos. Concentració n de ingresos por cliente o segmento.

Dependencia de ingresos. Si el cliente A representa el 70% de ventas, w(A→empres a) = 0.70.

Segmentación de ingresos, contratos, análisis de concentración de cartera.

Operacione s

Proveedores críticos, infraestructur a, procesos clave. Single points of failure.

Dependencia operativa. Si el proveedor único P es necesario para producir, w(P→empresa ) próximo a 1.

Mapas de cadena de suministro, contratos de provisión, auditorías de continuidad de negocio.


Financiero Acreedores, covenants de deuda, líneas de crédito, instrumentos derivados.

Dependencia de liquidez. Si el covenant C se incumple, se activan vencimientos cruzados. w(C→empres a) depende del porcentaje de deuda acelerada.

Contratos de crédito, calendarios de vencimiento, análisis de covenants.

Sistémico Marco regulatorio, política monetaria, ciclo de crédito, mercados de capital.

Dependencia sistémica. Cuánto depende la solvencia de la empresa del estado del ciclo crediticio en general.

Correlación histórica entre resultados de la empresa y ciclo macroeconómic o, análisis de sensibilidad.

#### 3.2 ICRS como medida del "too big to fail" formalizada

La expresión "too big to fail" (demasiado grande para quebrar) fue el argumento político central para los rescates de 2008. Pero "demasiado grande" es una medida de tamaño, no de riesgo sistémico. Una institución puede ser grande y tener ICRS bajo (si está suficientemente aislada del resto del sistema) o pequeña y tener ICRS alto (si es un nodo de paso necesario en la red de transmisión del riesgo).

#### La formalización correcta del "too big to fail" no es el tamaño sino el ICRS:

#### Too_critical_to_fail_i ⟺ R*ᵢ > θ_sistémico


donde θ_sistémico es el umbral a partir del cual la quiebra de ese nodo produce pérdidas sistémicas que superan el costo del rescate. Esta definición tiene consecuencias regulatorias directas: la decisión de rescatar o no rescatar una institución en quiebra debería depender de su ICRS, no de su tamaño.

En 2008, Lehman tenía ICRS alto no porque fuera el banco más grande (no lo era: Citigroup, JP Morgan y BofA eran mayores) sino porque era el nodo con mayor densidad de conexiones no colateralizadas con otros actores del sistema. Su quiebra activó simultáneamente vencimientos cruzados en un número de contrapartes suficiente para congelar el mercado interbancario global.

#### 3.3 El índice de sustituibilidad S en el riesgo financiero

En el dominio del riesgo sistémico, S tiene una interpretación precisa para la regulación preventiva:

- S alto del nodo de riesgo: el colapso habría ocurrido con cualquier institución equivalente en esa posición. El riesgo era una propiedad del sistema, no de la institución específica. La regulación correcta no es supervisar esa institución sino cambiar las reglas del sistema.
- S bajo del nodo de riesgo: las características idiosincráticas de esa institución —su estructura de pasivos, su exposición específica, sus conexiones particulares— fueron condición necesaria del colapso a esa escala. La regulación puede enfocarse en esa institución.
- S del instrumento financiero (CDO, CDS): cuánto del riesgo sistémico era específico de ese instrumento versus genérico de cualquier instrumento con esas características. Si S es alto, regular ese instrumento



específico es menos eficiente que regular la clase de instrumentos.

El análisis de sensibilidad de R* bajo variaciones de S es especialmente importante en el contexto del riesgo sistémico porque la S de las instituciones financieras cambia rápidamente: una institución con S alto (reemplazable) puede volverse de S bajo (crítica) durante una crisis si el mercado interpreta su quiebra como señal sistémica independientemente de sus condiciones objetivas.

#### 3.4 α y Δ en el análisis de quiebra

En el análisis de quiebra corporativa, α mide el grado de provisión del riesgo que el nodo tenía antes del colapso. Para una empresa, α se descompone en tres instrumentos de mitigación:

Instrumento α que contribuye Descripción

Capital buffer α_capital El capital regulatorio y los colchones de liquidez que absorben pérdidas sin producir default. Para bancos: Tier 1 Capital ratio. Para empresas: ratio deuda/EBITDA.

Diversificación α_diversificación La distribución del riesgo entre múltiples contrapartes, productos y mercados. Reduce S_empresa porque el colapso de cualquier nodo individual tiene menor impacto.

Cobertura α_cobertura Los instrumentos de hedging (derivados,


seguros) que transfieren el riesgo a terceros. Reduce R* del nodo individual pero puede trasladar el riesgo sistémico si la cobertura está concentrada.

α_total = 1 − (1−α_capital) × (1−α_diversificación) ×

(1−α_cobertura)

El Δ de quiebra es la diferencia entre el ICRS del nodo y su α de provisión. Un Δ positivo alto en el período previo al colapso era la señal de que el sistema llevaba más riesgo del que estaba provisionado. En Lehman, el Δ de los nodos de diseño regulatorio (la Reserva Federal, la SEC) era positivo durante años antes de 2008, medible con datos públicos, y nadie actuó sobre él.

#### 3.5 El D_total sistémico: de la quiebra al desempleo

D_sistémico = T_invertido + T_impedido +

ΔT_trayectoria

Componente En quiebra sistémica

Descripción

T_invertido Pérdidas directas en el evento de colapso

Para Lehman: los 613,000 millones en activos declarados y las pérdidas de los acreedores. Para la crisis de 2008: la contracción de riqueza financiera inmediata estimada en 11 billones de dólares solo en los EE.UU.

T_impedido La actividad económica

El crédito no otorgado durante la recesión (empresas que no


que no ocurrió

pudieron financiarse), las inversiones no realizadas, los empleos no generados. Para 2008: 30 millones de empleos perdidos en el mundo y la caída del PIB de múltiples economías.

ΔT_trayectoria Pérdida persistente de potencial económico

La evidencia indica que las crisis financieras profundas reducen permanentemente el PIB potencial de las economías afectadas. Estudios del FMI estiman que la crisis de 2008 redujo el PIB potencial de los EE.UU. en entre 5% y 10% de manera permanente.

La expresión en tiempo de vida del D_sistémico de la crisis de 2008 con w_ref = $8 USD/hora:

D_vital_2008 ≈ $22,000,000,000,000 / $8 = 2.75 × 10¹²

horas de vida

Dos billones setecientos cincuenta mil millones de horas. En términos humanos directos: los 30 millones de desempleados perdieron en promedio 2.5 años de ingresos. La distribución de ese daño entre los nodos del grafo — según sus respectivos R* e ICRS— es la base para cualquier análisis de responsabilidad sobre la crisis de 2008.

#### 3.6 B_total en el análisis de quiebra: quién ganó con el colapso

A diferencia del dominio tanatológico (donde B = 0 por definición), en la quiebra sistémica hay nodos que obtuvieron beneficios causales del colapso. Las agencias calificadoras cobraron sus fees antes del colapso. Los directivos de Lehman recibieron bonificaciones


multimillonarias en los años previos a la quiebra, financiadas con el riesgo que el sistema acumulaba. Los fondos de cobertura que apostaron contra las hipotecas subprime (como los descritos en The Big Short) obtuvieron rentabilidades extraordinarias.

El B_total sistémico tiene dos componentes:

B_sistémico = B_extraído_pre_colapso +

B_extraído_durante_colapso

B_extraído_pre_colapso son los beneficios que los nodos de diseño obtuvieron mientras el sistema se cargaba de riesgo: las comisiones por estructuración de CDOs, los fees de rating, las bonificaciones. B_extraído_durante_colapso son los beneficios obtenidos como consecuencia directa del colapso: las ganancias de los fondos que apostaron en corto, el diferencial de tasas que los bancos supervivientes obtuvieron por el rescate de sus competidores.

En ambos casos, R*_B distribuye ese beneficio entre los nodos que contribuyeron causalmente a generarlo. La base para la acción de enriquecimiento sin causa contra los nodos que se beneficiaron del colapso es la misma fórmula del sistema:

AD_B_i = R*_B_i × B_total_sistémico


### §4.  Casos resueltos

Caso A — Lehman Brothers y la crisis de 2008

ICRS de CDOs y agencias calificadoras vs. la narrativa del banco codicioso

A.1 El contexto histórico

Para comprender el colapso de Lehman Brothers es necesario entender primero la arquitectura del sistema que lo hizo posible. Entre 2001 y 2007, el mercado hipotecario estadounidense experimentó una transformación radical: las hipotecas ya no se mantenían en el balance de los bancos que las originaban, sino que se empaquetaban en instrumentos financieros estructurados (CDOs, Collateralized Debt Obligations) que se vendían a inversores institucionales en todo el mundo.

Este proceso de titulación tenía una lógica aparente: distribuir el riesgo hipotecario entre miles de inversores en lugar de concentrarlo en unos pocos bancos. El problema era que esa distribución solo funcionaba si los CDOs eran valorados correctamente. Y para que los inversores institucionales (fondos de pensión, aseguradoras, bancos centrales) pudieran comprarlos, necesitaban tener una calificación crediticia. Las agencias calificadoras asignaron calificaciones AAA a tranches de CDOs que en muchos casos estaban respaldados por hipotecas subprime de altísimo riesgo.

¿Por qué lo hicieron? El modelo de negocio de las agencias establece que el emisor del instrumento —el banco que crea el CDO— paga a la agencia calificadora por su calificación. Ese conflicto de intereses produjo un incentivo estructural: la agencia que asignara calificaciones más generosas conseguiría más mandatos del banco emisor. El resultado


fue una carrera al fondo en los estándares de calificación que duró años, con analistas de las propias agencias documentando internamente su preocupación por la calidad de los ratings que asignaban.

Cuando los precios de la vivienda comenzaron a caer en 2007 y las hipotecas subprime empezaron a impagar masivamente, el valor de los CDOs colapsó. Los inversores que los habían comprado creyendo que eran instrumentos AAA descubrieron que eran incobrables. Los bancos que los tenían en su balance —Lehman entre ellos— vieron evaporarse su capital. Lehman, más apalancado que sus competidores supervivientes, fue el primero en llegar al umbral de insolvencia sin posibilidad de refinanciarse.

#### A.2 El grafo causal del colapso sistémico

Nodo Actor / Instrumento

Tipo Función causal en el colapso

N1 Marco regulatorio de desregulación (Gramm-Leach-Bliley Act 1999, derogación Glass-Steagall)

Diseño normativo

Eliminó la separación entre banca comercial y banca de inversión que habría limitado el riesgo sistémico. Sin este marco, Lehman no habría podido construir el balance que construyó. R* alto, S moderado (el sistema político de los años 1990 habría desregulado de alguna manera; la forma específica fue idiosincrática).

N2 Agencias calificadoras

Diseño / certificación

Asignaron calificaciones AAA a instrumentos de


(Moody's, S&P, Fitch)

alto riesgo. Sin esas calificaciones, los inversores institucionales no habrían comprado los CDOs y el mercado no habría alcanzado esa escala. R* alto, S moderado-bajo (las tres agencias reprodujeron el mismo comportamiento por incentivos estructurales similares).

N3 CDOs y derivados hipotecarios (instrumentos)

Nodo instrumental

El mecanismo que concentró y ocultó el riesgo. Sin los CDOs como instrumento, el riesgo hipotecario no habría podido distribuirse opacamente. Nodo sin voluntad: su R* apunta hacia N1 (que lo permitió), N2 (que lo certificó) y N4 (que lo diseñó).

N4 Bancos de inversión estructuradores (Goldman, Lehman, Bear Stearns)

Ejecución / amplificación

Diseñaron y vendieron los CDOs. Su S es moderado: el sistema los incentivaba a hacerlo; otros bancos habrían hecho lo mismo. Pero Lehman fue el más agresivamente


apalancado de los supervivientes.

N5 Reserva Federal y SEC (supervisión)

Omisión regulatoria

Tuvieron acceso a información que mostraba la acumulación de riesgo sistémico y no usaron los instrumentos disponibles para intervenir. Posición causal real por omisión.

N6 Originadores de hipotecas subprime (Countrywide, etc.)

Materia prima del riesgo

Generaron las hipotecas de baja calidad que alimentaron el sistema. S muy alto: cualquier originador con los mismos incentivos habría producido lo mismo.

Nodo final El daño sistémico alcanzó a personas que no habían participado en ningún nodo del grafo.

Nf Economía global: desempleados, ahorradores, contribuyentes

#### A.3 R* y el ICRS: la narrativa política vs. el análisis causal

Nodo R* / ICRS

S α pre-200 8

Δ Narrativa política vs. análisis

#### 0.3 8 0.10 +0.12 Narrativa: no mencionado.

N1 — Marco regulatorio

~22 %


Análisis: el nodo de diseño con mayor responsabilida d estructural. Ningún banco fue condenado por el marco que el Congreso creó.

0.3 2 0.05 +0.15 Narrativa: criticadas, pero no procesadas. S&P pagó una multa de $1,375M en 2015. Ninguna calificadora fue condenada por los ratings AAA. Análisis: segundo nodo por R*.

N2 — Calificadoras

~20 %

#### 0.5 5 0.00 N/A * Nodo sin voluntad. Su R* apunta a N1, N2 y N4. No procesable directamente.

N3 — CDOs (instrumento)

~18 %

#### 0.4 5 0.15 +0.0 5 Narrativa: foco principal. "Bancos codiciosos." Análisis: alta visibilidad documental, pero R* similar al del

N4 — Bancos estructuradore s

~20 %


marco regulatorio y las calificadoras. S moderado: cualquier banco con los mismos incentivos habría actuado igual.

#### 0.6 0 0.10 +0.0 4 Narrativa: casi no mencionado. Análisis: R* real por omisión. La Fed tenía la facultad de intervenir y no lo hizo.

N5 — Fed / SEC (omisión)

~14 %

~6% 0.8 8 0.20 -0.14 Alta sustituibilidad. Funcionaron dentro de los incentivos del sistema. Chivos expiatorios parciales de la narrativa.

N6 — Originadores hipotecas

#### * R*_CDOs = 0.18 se imputa mediante la fórmula R*_efectivo de los nodos humanos que los diseñaron y certificaron (N1, N2, N4).

#### La tabla produce la lectura más importante del capítulo: la narrativa política concentró el foco en N4 (los bancos estructuradores, con R* = 20%) y casi ignoró N1 (el marco


regulatorio, R* = 22%) y N2 (las calificadoras, R* = 20%). El Índice de Justicia Estructural del sistema post-crisis de 2008:

J_2008 = 1 − Σ|Δᵢ| ≈ 1 − (0.12 + 0.15 + 0.05 + 0.04 +

...) ≈ 0.60

J = 0.60: moderadamente injusto. Mejor que el redlining (J = 0.04) pero con un Δ positivo significativo en los nodos de mayor R*. El principal beneficiario de esa injusticia fue N1: el marco regulatorio que produjo el sistema nunca fue reformado de manera proporcional a su R*.

A.4 El B_total y quién ganó con la crisis

Beneficios extraídos por los nodos de diseño antes del colapso:

- Agencias calificadoras (N2): ~$2,200 millones en revenues de ratings estructurados entre 2000 y 2007. Moody's obtuvo el 44% de sus ingresos totales de ratings estructurados en el pico.
- Bancos estructuradores (N4): comisiones de estructuración estimadas en $8-12 mil millones durante el período de expansión del mercado CDO.
- Directivos de los bancos (incluidos en N4): bonificaciones totales pagadas por Wall Street entre 2000-2007: estimadas en más de $300,000 millones.


Beneficios obtenidos durante el colapso:

- Fondos de cobertura en corto (Paulson & Co., Magnetar, etc.): ganancias documentadas de más de $20,000 millones apostando contra los CDOs que ayudaron a diseñar.
- JP Morgan Chase, Bank of America, Citigroup (supervivientes del rescate): el programa TARP y los rescates de la Fed les permitieron adquirir



competidores a precios de derribo, aumentando su participación de mercado.

B_total_N2 = ~$2,200M → AD_B_N2 = 0.20 ×

$2,200M = $440M (monto de enriquecimiento

proporcional a R*)

La multa que S&P pagó en 2015 fue de $1,375M —más que su B_total proporcional estimado. Eso significa que, en ese caso específico, el α_diferido de S&P fue mayor que su posición de beneficio, produciendo Δ_B < 0. El problema es que la multa no guardó ninguna relación con el análisis causal: fue el resultado de una negociación, no de un cálculo de R*_B. El sistema produce el cálculo que la negociación no tuvo.

A.5 ¿Habría la crisis de 2008 ocurrido sin Lehman?

La pregunta contrafáctica más importante del caso: si el Tesoro estadounidense hubiera rescatado a Lehman el 14 de septiembre de 2008 (como hizo con Bear Stearns en marzo de 2008 y con Fannie Mae y Freddie Mac días antes), ¿habría ocurrido la crisis con la misma escala?

El análisis de S de Lehman responde esta pregunta con más precisión que cualquier especulación narrativa. S_Lehman se estima en 0.45: moderadamente bajo. Eso significa que las características idiosincráticas de Lehman —su ratio de apalancamiento (31:1 en su momento de mayor expansión), su exposición específica a hipotecas comerciales, su estructura de pasivos de corto plazo— contribuyeron causalmente al colapso en mayor medida que lo que habría ocurrido con cualquier banco equivalente.

Dicho de otro modo: sí, la crisis habría ocurrido de alguna forma sin Lehman (los nodos N1, N2 y N3 seguían activos). Pero sin las características específicas de Lehman (S bajo = 0.45), el colapso habría tenido menor intensidad en el


evento detonante de septiembre de 2008. El Tesoro al dejar caer a Lehman tomó una decisión que, calculada con el ICRS de Lehman en ese momento (~12% del sistema), era una apuesta de alto riesgo que perdió.


Caso B — Empresa mediana hipotética

Proveedor único + cliente concentrado + deuda covenant: el mapa del riesgo de quiebra antes de que ocurra

Este caso es una composición hipotética que integra los factores de riesgo más frecuentes en quiebras de empresas medianas. No corresponde a ninguna empresa específica.

B.1 La situación de la empresa

Empresa manufacturera de componentes metálicos. Facturación de 180 millones de pesos anuales. Tres años de crecimiento sólido. El director general solicita una auditoría de riesgo de continuidad antes de una renegociación de deuda. El análisis de su red de dependencias revela la siguiente estructura:

- Cliente A: representa el 72% de la facturación. Tiene un contrato anual renovable. La empresa construyó su capacidad productiva específicamente para ese cliente.
- Proveedor único P: el único proveedor del material metálico específico que el cliente A requiere. P tiene capacidad limitada y largo lead time. Ningún proveedor alternativo tiene la calificación técnica requerida.
- Deuda bancaria D: 85 millones de pesos al banco B, con un covenant que establece que si el EBITDA cae más del 20% vs. el año anterior, el crédito se vence anticipadamente. La deuda vence en 18 meses.
- Cliente B y C: representan el 28% restante. Fragmentados, sin concentración en ninguno.
- Capital de trabajo: financiado íntegramente con línea de crédito revolvente del banco B.



#### B.2 El grafo de riesgo de la empresa

Factor Tipo Función causal en el riesgo de quiebra

Nod o

N1 Pérdida del cliente A

Concentració n de ingresos

Si A no renueva el contrato, la empresa pierde el 72% de los ingresos. Con la estructura de costos fijos construida para esa escala, la empresa entraría en pérdidas en el mes 3 y violaría el covenant en el mes 6.

N2 Fallo del proveedor único P

Single point of failure

Si P no puede entregar (por su propia crisis, por un incidente operativo, por fuerza mayor), la empresa no puede cumplir sus pedidos. El incumplimiento con A activa penalidades contractuales y puede producir la no renovación del contrato.

N3 Incumplimient o del covenant de deuda

Detonante de vencimiento

Si el EBITDA cae más del 20% (por N1 o N2), el banco B acelera el vencimiento de los 85 millones más la línea revolvente. Eso produce


insolvencia de liquidez inmediata aunque la empresa sea técnicamente solvente en valor de activos.

N4 Ciclo económico sectorial

Una contracción en el sector manufacturero podría reducir los pedidos de A independientement e de la relación comercial. S muy alto: cualquier empresa en ese sector lo experimentaría igual.

Riesgo externo

#### B.3 ICRS y el mapa del riesgo real

#### Los pesos del grafo se estiman con base en la información financiera y contractual de la empresa:

Factor R* / ICRS

S α actual

Interpretación

~48% 0.30 0.05 Factor dominante. S moderado-bajo: el cliente A tiene características específicas (contrato largo, especificaciones técnicas) que hacen que su pérdida sea peor que perder cualquier cliente equivalente en ingresos.

N1 — Pérdida de A


~32% 0.20 0.05 S bajo: el proveedor único con esa calificación técnica no tiene sustituto inmediato. Su fallo es idiosincrático. Es el segundo factor de mayor urgencia.

N2 — Fallo de P

~14% 0.55 0.10 S moderado: cualquier empresa con covenant equivalente y caída de EBITDA similar enfrentaría el mismo vencimiento acelerado. El covenant amplifica N1 y N2 pero no los causa.

N3 — Covenant

~6% 0.92 0.20 S muy alto. Factor exógeno no controlable. La empresa tiene poco poder de mitigación directa.

N4 — Ciclo económico

#### La lectura del ICRS produce el mapa de prioridades de riesgo:

1.  N2 (proveedor único P) es la intervención más urgente, aunque no tiene el R* más alto, porque su S es el más bajo del grafo (0.20): su fallo es el más idiosincrático y el más difícil de absorber. La ecuación de prioridad es R* × (1 − S): N2 tiene 0.32 × 0.80 = 0.256, mayor que N1 con 0.48 × 0.70 = 0.336 en términos de urgencia de intervención no reemplazable. 2.  N1 (concentración en el cliente A) tiene el R* más alto pero su S es más alto que el de N2 porque existen otros clientes potenciales (aunque ninguno con el mismo volumen). La intervención correcta es la diversificación de ingresos, aunque su escala y velocidad están


limitadas por la capacidad productiva que fue diseñada para A. 3.  N3 (el covenant) no es el factor primario: es el amplificador. Renegociar el covenant antes de la próxima auditoría reduce el Δ de N3 sin resolver N1 ni N2. Es la intervención más fácil pero la menos eficiente si no va acompañada de las otras.

#### El plan de mitigación recomendado ordenado por R* × (1 − S):

Prior. Acción Nodo que resuelve

Impacto en ICRS y en α

1 Certificar proveedor alternativo para P

N2 Eleva α_N2 de 0.05 a ~0.60 (reduce R* efectivo de N2 en más del 50%). Mayor impacto por unidad de inversión dado S bajo de N2.

2 Diversificar ingresos: 3 clientes nuevos al 10% cada uno

N1 Reduce R*_N1 de 0.48 a ~0.35 en 18 meses. Requiere inversión comercial pero también reduce la dependencia de renovación del contrato.

3 Renegociar covenant: ampliar el umbral al 35% de caída EBITDA

N3 Elimina el detonante de vencimiento acelerado. No resuelve N1 ni N2 pero compra tiempo.

4 Construir reserva de liquidez

N3 + N1 Aumenta α_capital de la empresa. Reduce


equivalente a 3 meses de EBITDA

Δ_N3 aunque no elimina el riesgo de N1.

B.4 Proyección del ICRS después de las intervenciones

El ICRS total del sistema empresa antes de las intervenciones, medido como la suma de Δ positivos:

ICRS_total_antes = 0.43 + 0.27 + 0.04 + ... ≈ 0.82

(riesgo muy alto)

Después de implementar las cuatro intervenciones en 18 meses:

ICRS_total_después ≈ 0.35 + 0.12 + 0.01 + ... ≈ 0.52

(riesgo moderado)

La reducción de 0.82 a 0.52 en el ICRS total no es una garantía de continuidad: la empresa sigue siendo vulnerable si N1 y N4 se materializan simultáneamente. Pero la probabilidad de quiebra en los 18 meses siguientes se reduce de manera cuantificable por las intervenciones.

El valor del análisis preventivo:  La empresa del caso B no está en quiebra. Está en riesgo de quiebra evitable si no actúa. El ICRS como instrumento de diagnóstico preventivo —aplicado antes del colapso, no como análisis forense post-quiebra— es donde el sistema produce su mayor valor en el dominio empresarial. Identificar que N2 (el proveedor único) tiene S = 0.20 con R* = 0.32 antes de que P falle es la diferencia entre una empresa que tiene tiempo de certificar alternativas y una empresa que colapsa por una contingencia que era calculable.


### §5.  Límites del método en quiebra y riesgo sistémico

#### 5.1 El problema de los pesos dinámicos en crisis

En condiciones normales, los pesos del grafo de interdependencias financieras son relativamente estables. En condiciones de crisis, cambian rápidamente: el pánico convierte nodos de S alto (reemplazables) en nodos de S bajo (críticos) porque el mercado los interpreta como señales sistémicas independientemente de sus condiciones objetivas. El ICRS calculado en tiempo normal puede subestimar el riesgo de un nodo durante la crisis. El análisis debe incluir escenarios de estrés donde los pesos se ajustan para capturar esa dinámica.

#### 5.2 El riesgo de modelos correlacionales usados como causales

El VaR (Value at Risk) y otros modelos de riesgo financiero estándar son correlacionales: estiman la probabilidad de pérdida basándose en la distribución histórica de los retornos. Cuando los retornos están correlacionados durante la crisis (todos los activos caen juntos), el VaR subestima dramáticamente el riesgo. El ICRS es causal y por eso es menos sensible a ese problema: identifica los nodos de necesidad causal en la red, que son críticos independientemente de la distribución estadística de los retornos.

#### 5.3 El problema de la circularidad en el riesgo sistémico


En sistemas financieros altamente interconectados, el riesgo es a veces circular: A depende de B que depende de A. En esos casos, el grafo tiene ciclos y la iteración de potencia para calcular R* puede no converger de manera simple. La solución técnica —añadir un nodo de absorción o usar la factorización PageRank— está desarrollada en el §6. Pero la presencia de ciclos en el grafo es también una señal de riesgo: indica que el sistema tiene retroalimentaciones que pueden amplificar el colapso de manera no lineal.

#### 5.4 El límite político del "too big to fail"

El ICRS produce una medida técnica del riesgo sistémico de cada nodo. La decisión de rescatar o no rescatar una institución con ICRS alto es política, no técnica. El sistema puede decir: "El ICRS de Lehman era 0.12 y su quiebra producirá un colapso sistémico con D_total estimado de X." La decisión de si ese D_total justifica usar fondos públicos para el rescate requiere un juicio sobre la distribución del costo (los contribuyentes versus los accionistas) que el ICRS no puede hacer. El sistema provee los números; la decisión política los usa.

#### 5.5 El ICRS como predictor de quiebra y el ROI de las intervenciones

El §4.3 del capítulo calculó el ICRS antes y después de las intervenciones en la empresa mediana hipotética y mostró la reducción cuantitativa del riesgo sistémico. Lo que este apartado añade es la dimensión temporal: la probabilidad de quiebra en un horizonte de N meses dado el ICRS actual, y el retorno sobre la inversión esperado de cada intervención de mitigación antes de que el colapso ocurra.


#### El modelo de probabilidad de quiebra en función del ICRS

La probabilidad de quiebra en un horizonte T meses no es una función lineal del ICRS: es un proceso de primer paso sobre el grafo de riesgo. Cada nodo con Δ positivo es una "trampa" potencial —si ese nodo falla, activa los nodos que dependen de él. La probabilidad de quiebra tiene la forma:

#### P (quiebra, T) = 1 − exp (−λ × ICRS_total × T)

donde λ es la tasa de materialización del riesgo por período, calibrada con datos históricos de quiebras en el sector. Para empresas medianas manufactureras, λ ≈ 0.018 por mes. Para empresas con proveedor único documentado y concentración en un cliente, λ sube a ≈ 0.028 por mes por la correlación entre los riesgos.

#### Aplicación a la empresa mediana del §4 (ICRS_total = 0.82):

Horizonte ICRS actual (0.82)

ICRS post-intervenciones (0.52)

Reducción en P(quiebra)

6 meses 8.7% 5.4% −3.3 pp

12 meses 16.7% 10.2% −6.5 pp

18 meses 24.0% 14.4% −9.6 pp

24 meses 31.0% 18.3% −12.7 pp

Una reducción de 9.6 puntos porcentuales en la probabilidad de quiebra a 18 meses no es un número abstracto: es la diferencia entre una empresa que tiene una probabilidad de 1 en 4 de colapsar y una que tiene 1 en 7. Para los inversores y los acreedores, esa diferencia tiene un


#### valor actuarial directo que puede calcularse sobre el D_total estimado.

#### ROI de cada intervención: la tabla de prioridades con retorno financiero

#### El ROI de una intervención de mitigación es el valor esperado del daño evitado menos el costo de la intervención, dividido entre el costo de la intervención:

#### ROI_intervención_i = (D_total × ΔP(quiebra)_i −

#### Costo_i) / Costo_i

ROI

Pri .

Intervenció n

Costo est.

ΔP(quiebr a) 18m

D_tota l evitad o (esp.)

1 Certificar proveedor alternativo P

$0.8M −4.8 pp $8.6M 975%

2 Diversificar ingresos (3 clientes nuevos)

$1.5M −3.2 pp $5.8M 283%

3 Renegociar covenant al 35%

$0.3M −1.2 pp $2.2M 627%

4 Reserva de liquidez 3 meses EBITDA

$5.4M * −0.4 pp $0.7M −87%* *

#### * La reserva de liquidez tiene un costo de oportunidad real (capital inmovilizado), no un gasto directo.


** ROI negativo porque el impacto en P(quiebra) es menor que el costo del capital inmovilizado. Esto no significa que la reserva sea mala idea — significa que es la intervención de menor prioridad dentro de este conjunto. Tiene valor como red de seguridad, no como reducción primaria del riesgo.

Predictor:  La intervención con mayor ROI en el corto plazo es certificar el proveedor alternativo (ROI 975%), aunque no tiene el R* más alto del grafo. Eso confirma la regla del §3.2: el criterio correcto de priorización es R* × (1−S), no R* solo. El proveedor único tiene S = 0.20 y por eso su mitigación produce el mayor impacto por unidad de inversión.

#### El análisis contrafáctico: Lehman y la decisión del Tesoro

La misma estructura permite responder la pregunta contrafáctica del §4.5: si el Tesoro hubiera intervenido para rescatar a Lehman el 14 de septiembre de 2008, ¿cuánto habría reducido el ICRS sistémico del sistema financiero global?

Lehman tenía ICRS = 0.12 sobre el sistema. Si se elimina ese nodo del grafo (rescate que evita el default), el ICRS del sistema en esa fecha cae aproximadamente:

ΔICRS_sistémico = −0.12 × (1 −

correlación_otros_nodos)

Con una correlación entre nodos de aproximadamente 0.45 (estimada por la correlación entre los CDS spreads de los principales bancos de inversión en esa semana), ΔICRS ≈ −0.12 × 0.55 ≈ −0.066. El ICRS total del sistema habría pasado de ~0.78 a ~0.71. Todavía en zona de peligro (>0.70), pero con una probabilidad de colapso sistémico a 6 meses que cae del 28% al 22%.

Eso no habría evitado la crisis —el ICRS de 0.71 seguía siendo muy alto por los otros nodos (N1, N2, N3 con R* El Cálculo de la Responsabilidad · Cap. 9 — Quiebra y riesgo sistémico

combinado del 60%)— pero habría comprado tiempo para que las intervenciones sistémicas (los programas TARP, los recortes de tasas coordinados) pudieran operar antes de que el pánico se volviera irreversible.

El valor de la predicción contrafáctica:  No se trata de saber si la crisis habría ocurrido de todas formas (sí, habría ocurrido). Se trata de saber si el tiempo adicional que el rescate de Lehman habría comprado era suficiente para implementar las intervenciones que finalmente detuvieron el colapso. El análisis del ICRS dinámico sugiere que, con seis semanas adicionales antes del pánico máximo, la Reserva Federal habría tenido margen para actuar antes de que el crédito interbancario se congelara completamente.

#### Código de referencia: predictor de quiebra y ROI de intervenciones

import numpy as np import math  def predictor_quiebra(ICRS_total, lam=0.018,                        horizontes_meses=(6,12,18,24)):     """ P(quiebra, T) = 1 - exp(-lambda * ICRS_total * T)     lam: tasa de materialización por mes (sect. manufacturero ~0.018,          con proveedor único y cliente concentrado ~0.028)     """     return {T: 1 -math.exp(-lam * ICRS_total * T)             for T in horizontes_meses}  def roi_intervencion(D_total, delta_P_quiebra, costo, T_meses=18, r_anual=0.12):     """     ROI de una intervención de mitigación.     D_total:          daño total si ocurre la quiebra delta_P_quiebra:  reducción en P(quiebra) en T_meses     costo: costo de la intervención     """     valor_esperado_daño_evitado = D_total * delta_P_quiebra     # descuento al período T     factor = 1 / (1 + r_anual * T_meses / 12)     vp_daño_evitado = valor_esperado_daño_evitado * factor     roi = (vp_daño_evitado -costo) / costo     return {'VP_daño_evitado': vp_daño_evitado, 'costo': costo,             'ROI': roi,             'conviene': roi > 0}  def contraFactual_rescate(ICRS_sistema, ICRS_nodo_rescatado, corr_nodos=0.45, lam=0.025,                            horizontes=(3,6,12)): """     Efecto de rescatar un nodo sobre el ICRS sistémico     y sobre la probabilidad de colapso.     """     delta_ICRS = -ICRS_nodo_rescatado * (1 - corr_nodos)     ICRS_post  = max(0, ICRS_sistema + delta_ICRS) P_antes = {T: 1 - math.exp(-lam*ICRS_sistema*T) for T in horizontes} P_desp  = {T: 1 - math.exp(-lam*ICRS_post*T)    for T in horizontes} return {'ICRS_antes': ICRS_sistema, 'ICRS_despues': ICRS_post, 'delta_ICRS': delta_ICRS,             'P_colapso_antes': P_antes, 'P_colapso_despues': P_desp}  # ── Empresa mediana ── D_empresa = 180_000_000 P_antes = predictor_quiebra(0.82, lam=0.028) P_desp = predictor_quiebra(0.52, lam=0.028) print("=== Empresa mediana — Probabilidad de quiebra ===") for T in (6,12,18,24):     dif = P_desp[T]


- P_antes[T]     print(f"  {T:2d} meses: ANTES={P_antes[T]:.1%} DESPUÉS={P_desp[T]:.1%}  Δ={dif:+.1%}")  # ── ROI de intervenciones ── print("\n=== ROI de intervenciones ===") intervs = [     ("Certificar proveedor alt.",  D_empresa, 0.048, 800_000), ("Diversificar ingresos",      D_empresa, 0.032, 1_500_000), ("Renegociar covenant",        D_empresa, 0.012, 300_000),     ("Reserva liquidez",           D_empresa, 0.004, 5_400_000), ] for nombre, D, dp, costo in intervs:     r = roi_intervencion(D, dp, costo)     print(f" {nombre:30s}  ROI={r['ROI']:+.0%}  {'✓' if r['conviene'] else '✗'}")  # ── Contrafáctico Lehman ── print("\n=== Contrafáctico: rescate de Lehman ===") cf = contraFactual_rescate(0.78, 0.12, corr_nodos=0.45, lam=0.025) print(f"  ICRS sistema antes:    {cf['ICRS_antes']:.3f}") print(f"  ICRS sistema después:  {cf['ICRS_despues']:.3f}") print(f" ΔP(colapso, 6 meses):  {cf['P_colapso_despues'][6]-cf['P_colapso_antes'][6]:+.1%}")


§6.  Profundización formal — Esta sección puede saltarse sin perder el argumento del capítulo

### §6.  Profundización formal

#### 6.1 El grafo de quiebra en cascada: modelado del contagio

Sea G_fin = (N, A, w) el grafo financiero y sea x_i(t) el estado de solvencia del nodo i en el tiempo t (0 = solvente, 1 = en default). La dinámica de contagio puede modelarse como:

x_i(t+1) = I [ Σⱼ w_ji × x_j(t) ≥ θᵢ]

donde θᵢ es el umbral de quiebra del nodo i (la fracción de sus contrapartes que deben quebrar para que i quiebre) y I [·] es la función indicadora. El ICRS de Lehman puede calcularse como la diferencia entre el daño total con el colapso de Lehman (x_Lehman (0) = 1) y sin él (x_Lehman (0) = 0):

ICRS_Lehman = D_total(x_L=1) − D_total(x_L=0)

Normalizado sobre el D_total total, este es exactamente R*_Lehman en el grafo del colapso sistémico. La iteración del modelo de contagio con y sin cada nodo produce el vector R* completo sin necesidad de resolver el eigenvector directamente —es el enfoque de perturbación unitaria.

#### 6.2 La relación entre ICRS y las métricas de centralidad de red


El ICRS tiene una relación directa con la teoría de redes complejas. Específicamente:

- ICRS ≈ eigenvector centrality cuando los pesos son simétricos. En redes financieras los pesos son asimétricos (la dependencia de A en B no es la misma que la de B en A), por lo que el ICRS generaliza la eigenvector centrality al caso asimétrico.
- ICRS > betweenness centrality cuando el nodo es un puente necesario en el flujo del riesgo. La betweenness mide cuántas rutas pasan por el nodo; el ICRS mide cuánto del daño depende de que ese nodo exista.
- ICRS > pagerank en términos de interpretabilidad causal: pagerank mide la probabilidad de que una caminata aleatoria visite un nodo; el ICRS mide la fracción del daño causalmente atribuible a ese nodo.


#### 6.3 Análisis de sensibilidad del ICRS ante cambios de S

El ICRS depende de los pesos del grafo, que pueden ser inciertos o cambiar durante la crisis. El análisis de sensibilidad estándar examina:

∂ICRS_i / ∂S_j   ∀ i, j

Si ∂ICRS_i / ∂S_j > 0, entonces cuando la fungibilidad del nodo j aumenta (se vuelve más reemplazable), el ICRS del nodo i también aumenta —lo que indica que i y j comparten la posición de riesgo idiosincrático. En el caso de Lehman, el análisis de sensibilidad habría mostrado que a medida que Bear Stearns (rescatado en marzo 2008) era absorbido por JP Morgan (aumentando su S porque dejó de ser un nodo independiente), el ICRS de Lehman aumentaba: el sistema perdía un nodo alternativo de absorción.


#### 6.4 Código Python de referencia

import numpy as np from scipy.stats import pearsonr  def analisis_quiebra(W_fin, alpha_provision,                      D_total, w_ref=8.0,                      nombres_nodos=None):     """     Análisis de quiebra y riesgo sistémico.     W_fin:           matriz de pesos del grafo de interdependencias     alpha_provision: α (provisión del riesgo) por nodo D_total:         daño total estimado del colapso     w_ref:           salario de referencia (USD/hora)     """     n = W_fin.shape[0]      # ── ICRS = R*: índice de concentración de riesgo sistémico ──     R = np.ones(n) / n     for _ in range(500):         Rn = W_fin @ R; s = np.sum(Rn)         if s < 1e-12: break         Rn /= s         if np.max(np.abs(Rn - R)) < 1e-9: break         R = Rn     ICRS = Rn  # = R*      # ── S: fungibilidad sistémica del nodo ──     S = np.zeros(n)     for i in range(n): max_c = 0         for j in range(n):             if j == i: continue             Wm = W_fin.copy()             Wm[i,:] = np.mean(W_fin, axis=0)             Rm = np.ones(n)/n             for _ in range(200):                 Rm2 = Wm @ Rm; sm = np.sum(Rm2)                 if sm < 1e-12: break                 Rm2 /= sm                 if np.max(np.abs(Rm2-Rm)) < 1e-6: break                 Rm = Rm2             c, _ = pearsonr(ICRS, Rm2)             max_c = max(max_c, abs(c))         S[i] = 1 - max_c      Delta = ICRS - alpha_provision     # Prioridad: nodos con mayor riesgo causal no mitigado     prioridad = ICRS * (1 - S)  # R_neta: riesgo idiosincrático      # ── Distribución del daño sistémico ──     AD = ICRS * D_total  # ajuste debitor por nodo D_vital = D_total / w_ref      # ── ICRS total: suma de déficits positivos ──     ICRS_total = float(np.sum(Delta[Delta > 0]))      result = {         'ICRS': ICRS,         'S': S,         'Delta_provision': Delta, 'prioridad_intervencion': np.argsort(-prioridad), 'riesgo_idiosincratico': prioridad,         'AD_por_nodo': AD, 'D_vital_horas': D_vital,         'ICRS_total_sistema': ICRS_total, 'J_sistema': float(1 - np.sum(np.abs(Delta))),     }     return result  def proyectar_post_intervencion(W_fin, alpha_antes, mejoras_alpha, D_total):     """     Proyecta el ICRS después de aplicar mejoras de mitigación.     mejoras_alpha: dict {índice_nodo: nuevo_alpha}     """ alpha_despues = alpha_antes.copy()     for idx, nuevo_alpha in mejoras_alpha.items():         alpha_despues[idx] = nuevo_alpha     antes = analisis_quiebra(W_fin, alpha_antes, D_total)     despues = analisis_quiebra(W_fin, alpha_despues, D_total)     return { 'ICRS_total_antes': antes['ICRS_total_sistema'], 'ICRS_total_despues': despues['ICRS_total_sistema'],         'reduccion': antes['ICRS_total_sistema'] - despues['ICRS_total_sistema'], 'J_antes': antes['J_sistema'],         'J_despues': despues['J_sistema'],     }  # ── Ejemplo: empresa mediana hipotética ── W_emp = np.array([     [0, 0,    0,    0,    0],  # N1 (cliente A)     [0.55, 0,    0,    0,    0],  # N2 (proveedor P) → N1 si falla     [0,    0,    0,    0,    0],  # N3 (covenant) [0,    0,    0,    0,    0],  # N4 (ciclo)     [0,    0,    0,    0,    0],  # Nf (empresa: quiebra) ]) # Aristas hacia Nf W_emp[0,4]=0.85; W_emp[1,4]=0.75; W_emp[2,4]=0.60; W_emp[3,4]=0.40 # N1 dispara N3 si cae el EBITDA W_emp[0,2]=0.65; W_emp[1,2]=0.50  alpha_antes = np.array([0.05, 0.05, 0.10, 0.20, 0.0]) D_total_empresa = 180_000_000


# facturación como proxy del D_total  res = analisis_quiebra(W_emp, alpha_antes, D_total_empresa, w_ref=8.0) nombres = ['N1-Cliente A','N2-Proveedor P','N3-Covenant','N4-Ciclo','Nf'] print("=== Empresa mediana — Análisis de riesgo de quiebra ===") for i, (nm, icrs, si, di, pri) in enumerate(zip(     nombres, res['ICRS'], res['S'], res['Delta_provision'], res['riesgo_idiosincratico'])):     flag = ' ← ATENDER PRIMERO' if pri == max(res['riesgo_idiosincratico']) else '' print(f"  {nm:18s} ICRS={icrs:.3f} S={si:.2f} Δ={di:+.3f} Prio={pri:.3f}{flag}")  print(f"\nICRS total del sistema: {res['ICRS_total_sistema']:.3f}") print(f"J (justicia/mitigación): {res['J_sistema']:.3f}")  # Proyección post-intervenciones mejoras = {1: 0.60, 0: 0.20, 2: 0.45}  # cert.P, diversif.A, renegoc.covenant proyeccion = proyectar_post_intervencion(W_emp, alpha_antes, mejoras, D_total_empresa) print(f"\n--- Proyección post-intervenciones ---") print(f"ICRS antes:     {proyeccion['ICRS_total_antes']:.3f}") print(f"ICRS después:   {proyeccion['ICRS_total_despues']:.3f}") print(f"Reducción:      {proyeccion['reduccion']:.3f} ({proyeccion['reduccion']/proyeccion['ICRS_total_antes']*100:.0f}%)")

Miguel Hilario Olvera Aguilar Centro Multidisciplinario Meriadock Formación y Asesoría A.C., 2026

Continúa en el Capítulo 10 — Seguros y actuaría


