# Capítulo 8. Score crediticio

## El impago no es un hecho del deudor: índice de causalidad y el nodo de diseño del incumplimiento

## §1.  El problema

En la década de 1930, el gobierno federal de los Estados Unidos creó la Administración Federal de Vivienda (FHA) con el objetivo de hacer accesible el crédito hipotecario a millones de familias. Para evaluar el riesgo de los préstamos, la FHA encargó a la Corporación de Préstamos para Propietarios de Hogares (HOLC) que clasificara cada vecindario del país según su "seguridad" crediticia. Los mapas que produjo la HOLC codificaban los vecindarios en colores: verde (primer grado, "más deseable"), azul, amarillo, y rojo. Los vecindarios marcados en rojo —con población predominantemente afroamericana— eran clasificados como "peligrosos" y se les negaba sistemáticamente el acceso al crédito hipotecario federal.

Ese proceso se llamó redlining. Durante cuatro décadas, hasta que la Fair Housing Act de 1968 lo prohibió formalmente, la política federal diseñó y ejecutó un sistema que impedía a las familias negras acumular patrimonio a través de la vivienda propia —el principal vehículo de acumulación de riqueza de la clase media estadounidense en

el siglo XX. El resultado cuantificable: la brecha de riqueza mediana entre familias blancas y negras en los Estados Unidos en 2023 es de aproximadamente 1:7 según el Federal Reserve. Los economistas que han intentado modelar qué fracción de esa brecha es atribuible al redlining estiman que entre el 25% y el 40% del diferencial actual tiene causalidad directa en esas políticas.

La pregunta que el sistema de imputación causal puede responder con precisión es: ¿quién causó el impago que el redlining "predijo"? No el deudor que no pudo pagar el crédito que nunca le dieron. No el vecindario que se depreció porque el sistema crediticio lo dejó sin inversión. El nodo de diseño que creó el sistema que hizo inevitable ese resultado.

Noventa años después, los algoritmos de score crediticio usan variables como el código postal, el historial de compras y los patrones de comportamiento digital. Algunos de esos algoritmos han sido documentados como reproductores del sesgo racial del redlining —no porque tengan "raza" como variable explícita, sino porque sus proxis capturan la misma geografía que los mapas de la HOLC, con la diferencia de que el nodo de diseño ahora no es el Estado federal sino el dataset y el ejecutivo que lo aprobó.

### 1.1 El impago como evento causalmente distribuido

El score crediticio tradicional trata el impago como un hecho del deudor: una propiedad de la persona que solicita el crédito, medida mediante su historial de pagos, deudas vigentes, antigüedad crediticia, tipos de crédito y nuevas solicitudes. Este es el modelo FICO, que desde 1989 determina el acceso al crédito de la mayoría de los

estadounidenses y que, con variantes, se usa en los sistemas crediticios de todo el mundo.

El problema de este modelo no es que sea incorrecto —el historial de pagos de una persona tiene correlación real con su comportamiento futuro— sino que es incompleto. Atribuye toda la causalidad del impago a los factores del deudor, ignorando los factores del sistema crediticio, del entorno macroeconómico, y de las condiciones institucionales que determinan si la persona tenía acceso real a las condiciones que habrían permitido el pago.

El cálculo de la responsabilidad introduce una herramienta diferente: el índice de causalidad del impago (R*), que distribuye la responsabilidad causal del impago entre todos los nodos del sistema crediticio —el diseñador de la política, el algoritmo, el contexto macroeconómico, y el deudor— en proporción a cuánto dependía el impago de cada uno de ellos específicamente.

Índice de causalidad del impago (R*):  La fracción del impago causalmente atribuible a cada nodo del sistema crediticio. R*_deudor mide la responsabilidad causal del deudor en el impago. R*_diseñador mide la responsabilidad causal del nodo que diseñó las condiciones del crédito —la política, el algoritmo, los términos— en el resultado. Cuando R*_diseñador > R*_deudor, el impago era más probable por el diseño del sistema que por la conducta del deudor.

### 1.2 La diferencia entre correlación crediticia y causalidad crediticia

El score FICO predice el impago con correlación estadística real. Una persona con FICO 500 tiene más probabilidad estadística de impago que una con FICO 800. Pero esa correlación no implica causalidad en el sentido del sistema: no dice que el FICO 500 causó el impago. Puede decir que

las condiciones que produjeron un FICO 500 (ingresos inestables, falta de historial crediticio formal, acceso solo a productos de alto costo) son las mismas condiciones que producen el impago. Y esas condiciones pueden tener un nodo de diseño con R* mucho mayor que el del deudor.

Analogía: El termómetro y la fiebre Un FICO bajo es como la temperatura alta: mide el estado del sistema, pero no causa la enfermedad. El sistema FICO mide el resultado acumulado de condiciones que incluyen las del deudor, pero también las del sistema financiero al que tiene acceso, las del entorno macroeconómico, y las de las políticas históricas que determinaron su punto de partida. Usar el FICO como causa del impago es confundir el termómetro con la infección.

### 1.3 El dataset como nodo causal autónomo

El caso contemporáneo de los algoritmos de crédito con sesgo racial introduce un concepto nuevo en el sistema que ninguno de los capítulos anteriores había necesitado con esta precisión: el dataset como nodo causal con R* propio, separado del directivo que lo aprobó.

Un algoritmo de machine learning no tiene voluntad, no tiene dolo, no tiene hijos. Pero tiene posición causal en el grafo de decisiones crediticias: su output determina quién recibe crédito y a qué costo. Si ese output reproduce el sesgo racial del redlining porque fue entrenado con datos históricos generados bajo esa política, el dataset es el nodo que transmite causalmente el daño histórico al sistema presente.

La pregunta de responsabilidad se desdobla entonces en tres niveles: ¿cuánto del impago es causalmente atribuible al deudor? ¿Cuánto al algoritmo (y por tanto al dataset que lo entrenó)? ¿Y cuánto al directivo que aprobó el uso de ese dataset sabiendo —o debiendo saber— que reproducía el sesgo?

R*_impago = R*_deudor + R*_dataset +

R*_directivo + R*_entorno_macro + ...

Esta descomposición es la contribución central del capítulo a la práctica financiera: transforma la evaluación del riesgo crediticio de un ejercicio de predicción estadística sobre el deudor en un análisis causal del sistema completo que produce el impago.

## §2. Página puente — Traducción al lenguaje del crédito y las finanzas

Esta página resume cómo se renombran las herramientas en el contexto del score crediticio y la evaluación del riesgo de impago. El lector con formación en finanzas, banca, o análisis de riesgo puede comenzar aquí.

Herramienta En score crediticio se llama

Qué significa en la práctica financiera

Grafo causal G

Red causal del impago

El mapa de todos los factores (del deudor, del sistema crediticio, del entorno macro, del diseño de la política) que contribuyen causalmente a la probabilidad de impago. Es más amplio que el scorecard tradicional.

R* (vector) Índice de causalidad del impago

La fracción del impago causalmente atribuible a cada nodo. R*_deudor es la fracción atribuible al deudor. R*_sistema es la fracción atribuible al diseño del sistema crediticio. Cuando R*_sistema > R*_deudor, el sistema tiene mayor responsabilidad causal en el impago que el deudor.

Nodo de diseño

Diseñador de la política crediticia

Quien diseñó las condiciones bajo las cuales se otorga o niega el crédito: 

/ aprobador del algoritmo

el regulador que definió la política, el directivo que aprobó el algoritmo, la empresa que diseñó el producto financiero.

Nodo dataset Algoritmo de scoring entrenado con datos históricos

Nodo causal sin voluntad propia pero con posición real en el grafo. Su R* mide cuánto del impago es causalmente atribuible al sesgo incorporado en el dataset histórico. Es el nodo que transmite la discriminación histórica al sistema presente.

S (índice) Fungibilidad del factor crediticio

S alto del deudor: cualquier persona en sus mismas condiciones estructurales (ingreso, código postal, acceso al sistema financiero formal) habría tenido el mismo resultado. El impago es estructural, no idiosincrático. S bajo: el impago dependió de características específicas del comportamiento de este deudor.

α (coeficiente)

Grado de responsabilidad crediticia asumida

Para el deudor: lo que hizo para reducir el riesgo de impago (renegociación, comunicación con el acreedor, búsqueda de refinanciamiento). Para el diseñador: en qué medida reconoció el sesgo del sistema y lo corrigió.

Δ = R* − α Déficit de responsabilidad causal no asumida

Δ alto del diseñador: diseñó condiciones que causaban el impago y no las corrigió. Δ alto del deudor: el

impago era causalmente atribuible a él y no tomó medidas. Δ negativo: la responsabilidad que se le atribuye es mayor que la que causó (deudor como chivo expiatorio del sistema).

D_total Daño crediticio total

T_invertido (la pérdida del acreedor en el impago), T_impedido (el desarrollo financiero truncado del deudor durante el período de exclusión crediticia), ΔT_trayectoria (el diferencial de acumulación de patrimonio entre quien tuvo acceso al crédito justo y quien no lo tuvo).

D_vital Daño en tiempo de vida de trabajo cristalizado

Usando τ(M) = M / w_ref: el daño crediticio expresado en horas de vida que el deudor o la comunidad afectada dedicó a trabajar y que no se tradujeron en patrimonio acumulado por el sesgo del sistema.

B_total Beneficio del diseñador del sesgo

Lo que el nodo de diseño obtuvo del sesgo: menor exposición al riesgo (real o percibida), mayor rentabilidad de la cartera, preservación de la estructura de poder en el mercado inmobiliario. Base para la acción de enriquecimiento sin causa.

Fraude annona

Incumplimiento del Estado en

Cuando el Estado diseñó un sistema que excluía a grupos específicos del

condiciones de acceso al crédito

acceso al crédito (redlining), recibió el capital fiscal de esas comunidades y no generó las condiciones materiales de posibilidad para su acumulación de patrimonio. Δ del Estado > 0.

No aplican al algoritmo ni al dataset. Aplican al directivo que aprobó el algoritmo sesgado: ¿actuó desde Potós (persistencia en el sistema heredado sin revisarlo), desde Anteros (defensa deliberada de una práctica que sabía sesgada), o desde Deimos (ignorancia genuina del sesgo)?

Hijos de Afrodita

Solo para directivos y reguladores humanos

Para el lector que viene del núcleo universal:  Este dominio introduce un tipo de nodo que no había aparecido en los dominios anteriores: el nodo algorítmico / dataset, que tiene posición causal real en el grafo pero carece de voluntad, dolo e hijos. Su R* no implica culpabilidad del algoritmo sino posición causal que apunta hacia el directivo que lo aprobó y hacia el diseñador de la política que generó los datos con los que fue entrenado.

## §3. Las herramientas en el contexto crediticio

### 3.1 Cómo construir el grafo causal del impago

El grafo causal del impago difiere del scorecard tradicional en su alcance: incluye no solo los factores del deudor sino también los del sistema crediticio que determinó las condiciones del préstamo. La construcción procede en cuatro niveles:

Nivel Tipo de nodo Función causal

Fuente de evidencia

Del deudor

Ingreso, estabilidad laboral, historial de pagos, capacidad de servicio de la deuda, conocimiento financiero.

Determina si el deudor, dado el contexto, podía cumplir el pago. R* del deudor mide la fracción del impago atribuible a sus condiciones y conducta específicas.

Historial crediticio, declaraciones de ingreso, documentación laboral, patrones de pago histórico.

Del producto

Tasa de interés, plazo, estructura de pagos, penalizaciones, términos de renegociación.

Las condiciones del producto determinan si el pago

Términos contractuales, comparación con productos equivalentes del mercado, análisis

era factible dado el ingreso del deudor. Un producto de alta tasa sobre un ingreso bajo tiene R* propio en el impago.

de capacidad de pago.

Del sistema

Política crediticia del acreedor, algoritmo de scoring, criterios de aprobación, acceso a refinanciamiento.

Determina las condiciones bajo las cuales se otorgó el crédito. Si el sistema aprobó un crédito que sus propios modelos indicaban como de alto riesgo de impago, ese riesgo tiene R* en el sistema, no solo en el deudor.

Documentación de política interna, modelos de riesgo, auditorías del algoritmo, estudios de disparate impact.

Del entorno

Ciclo económico, tasa de desempleo, inflación, crisis sistémicas, políticas de vivienda.

Los choques exógenos (una crisis financiera, una pandemia) tienen R* real en los impagos que

Series macroeconómicas, estudios de impacto de crisis en carteras de crédito, comparación de tasas de impago antes y durante el choque.

producen. El deudor que no pagó durante el COVID puede haber tenido R* bajo.

### 3.2 R* del deudor versus R* del sistema: cuándo el impago era estructural

La distinción entre R*_deudor y R*_sistema es la aportación operativa más directa del capítulo a la práctica financiera. Tiene consecuencias sobre quién asume el costo del impago, qué reclamaciones son procedentes, y cómo se diseña la regulación del crédito.

Perfil del impago

R* dominante

Consecuencia jurídica y de política pública

Impago idiosincrático

R*_deudor alto (>50%)

El impago fue causado principalmente por condiciones o conductas específicas del deudor. El riesgo estaba correctamente evaluado. La pérdida del acreedor era previsible y proporcional al perfil del deudor. La reclamación del acreedor tiene base.

Impago estructural

R*_sistema > R*_deudor

El impago fue causado principalmente por el diseño del sistema: producto inadecuado para el perfil del deudor, tasa excesiva, condiciones inalcanzables. El acreedor diseñó las condiciones

del impago. La reclamación íntegra al deudor es inverosímil jurídicamente.

Impago sesgado

R*_dataset alto, R*_deudor bajo

El algoritmo de scoring negó crédito o lo encareció para un deudor que, dado su perfil real, habría podido pagar. El impago es consecuencia de las condiciones de exclusión, no de la conducta del deudor. Base para acción de disparate impact.

El impago fue causado por un choque externo (crisis, pandemia, desastre) que el deudor no podía prever ni controlar. La imputación íntegra al deudor es injusta. Base para políticas de moratoria y reestructuración.

Impago exógeno

R*_entorno alto

### 3.3 El índice de sustituibilidad S en el crédito

### En el dominio crediticio, S tiene una interpretación especialmente importante para distinguir el impago estructural del idiosincrático:

•  S alto del deudor: cualquier persona con las mismas condiciones estructurales (mismo código postal, mismo nivel de ingreso, mismo acceso al sistema financiero formal) habría tenido el mismo resultado crediticio. El impago es una propiedad del entorno, no de la persona. La política de crédito correcta trabaja sobre el entorno, no sobre el comportamiento individual. •  S bajo del deudor: las condiciones específicas de este deudor —su gestión financiera, sus decisiones, su comportamiento— fueron determinantes para el

impago. Otro deudor con condiciones estructurales similares habría podido pagar. En este caso, la responsabilidad causal del deudor es genuinamente alta. •  S del dataset: cuánto del sesgo del algoritmo es genérico (cualquier dataset histórico entrenado con datos del redlining habría producido el mismo sesgo) versus idiosincrático (este dataset específico, con estas variables específicas, amplificó el sesgo más allá de lo que otros datasets habrían hecho).

La combinación R*_deudor × (1 − S_deudor) produce la responsabilidad causal neta del deudor en el impago: la fracción del impago que es genuinamente atribuible a sus características idiosincráticas. Esa es la base correcta para cualquier acción de cobro:

AD_deudor = [R*_deudor × (1 − S_deudor)] ×

D_total

Si este producto es significativamente menor que el monto total reclamado al deudor, hay inversión causal en el sistema de cobro: el deudor está asumiendo más de lo que causó.

### 3.4 α y Δ en el sistema crediticio

En el sistema crediticio, α tiene interpretaciones distintas según el tipo de nodo:

Nodo α en este dominio Conducta que sube α

Deudor Grado de responsabilidad crediticia asumida.

Comunicó con el acreedor ante la primera señal de dificultad. Buscó refinanciamiento activamente. Realizó pagos parciales cuando el pago total no era posible.

Cooperó con el proceso de reestructuración.

Acreedor / banco

Grado en que proveyó condiciones que hacían factible el pago.

Ofreció productos adecuados al perfil del deudor. Proveyó educación financiera. Tuvo mecanismos accesibles de renegociación. Ajustó las condiciones ante choques exógenos.

Directivo / aprobador del algoritmo

Grado en que reconoció y corrigió el sesgo del sistema.

Auditó el algoritmo para detectar disparate impact. Corrigió las variables proxy que reproducían el sesgo. Compensó a los deudores excluidos incorrectamente.

Reguló contra el redlining (Fair Housing Act). Exigió auditorías de equidad en los algoritmos de crédito. Diseñó programas de inclusión financiera proporcionales al déficit histórico.

Estado / regulador

Grado en que generó las condiciones materiales de posibilidad para el acceso al crédito justo.

### 3.5 El daño crediticio y su expresión en tiempo de vida

$$D_crédito = T_invertido + T_impedido +$$

Componente En crédito equivale a

Descripción

T_invertido Pérdida directa en el impago

Para el acreedor: el capital prestado no recuperado. Para el deudor (en crédito

predatorio): los pagos realizados que excedían el costo real del capital, el capital consumido en intereses abusivos.

T_impedido Patrimonio no acumulado durante el período de exclusión

Lo que el deudor o la comunidad dejó de acumular mientras el sistema crediticio sesgado lo excluyó: la vivienda que no pudo comprar, el negocio que no pudo capitalizar, la educación que no pudo financiar.

ΔT_trayectoria El diferencial persistente de acumulación de patrimonio

La brecha de riqueza que persiste hoy como consecuencia del sistema de exclusión histórica. En el caso del redlining, la diferencia de 1:7 en riqueza mediana entre familias blancas y negras tiene en este componente su principal expresión.

$$Expresado en tiempo de vida con τ(M) = M / w_ref:$$

$$D_vital_crédito = D_crédito / w_ref   [horas de vida$$

### cristalizadas en trabajo no recompensado]

Esta conversión hace visible la dimensión ontológica del daño crediticio: los recursos que el sistema sesgado extrajo de las comunidades excluidas representan horas de trabajo de personas que no se tradujeron en patrimonio acumulado porque el acceso al instrumento de acumulación les fue negado por diseño.

### 3.6 Los hijos en el dominio crediticio: solo en nodos humanos con voluntad

Los hijos aplican solo a los directivos y reguladores con poder de decisión sobre el sistema crediticio. No aplican al algoritmo, al dataset, ni a los productos financieros como nodos sin voluntad.

Hijo En el directivo / regulador

Evidencia Implicación

Potós Persistencia en el sistema heredado sin cuestionarlo. "Siempre hemos usado este modelo." "Los datos son los datos."

Uso sin auditoría de modelos heredados. Resistencia pasiva a la revisión. "No sabíamos que había sesgo."

Culpa habitual. Compatible con acuerdo de remediación si actúa una vez informado.

Anteros Defensa deliberada de un sistema que sabe sesgado. "El modelo predice correctament e el riesgo." Resistencia activa a la auditoría.

Comunicacione s internas que desestiman advertencias de equidad. Presión sobre el equipo de cumplimiento.

Dolo eventual o directo. Mayor responsabilidad . Menor probabilidad de acuerdo.

Deimos Ignorancia genuina del sesgo. No comprendía las implicaciones de las variables proxy.

Ausencia de documentación de análisis de equidad. No hubo advertencias internas que pudiera haber ignorado.

Negligencia simple. Compatible con remediation sin sanción penal.

Harmoní a

Auditó activamente el algoritmo, identificó el sesgo y lo corrigió antes de que produjera daño a escala.

Documentación del proceso de auditoría, de la corrección, y de la comunicación transparente.

α alto. No hay Δ. Modelo de buenas prácticas regulatorias.

## §4. Casos resueltos

Caso A — Redlining en los Estados Unidos (1930s– 1970s)

El Estado federal como nodo de diseño del impago sistemático de comunidades negras

A.1  El contexto histórico

Entre 1933 y 1940, la HOLC (Home Owners' Loan Corporation) completó los mapas de seguridad residencial para 239 ciudades de los Estados Unidos. Esos mapas clasificaban cada vecindario en cuatro grados de inversión: A (verde), B (azul), C (amarillo) y D (rojo). La clasificación D —el redlining— se aplicaba sistemáticamente a los vecindarios con población negra significativa, independientemente de las condiciones económicas objetivas de sus residentes.

Las consecuencias eran directas y documentadas: los vecindarios marcados en rojo no podían recibir hipotecas aseguradas por la FHA. Sin acceso a hipotecas federales, las familias de esos vecindarios no podían comprar vivienda propia. Sin vivienda propia, no acumulaban el patrimonio que la explosión inmobiliaria de las décadas siguientes generó para las familias blancas. El resultado cuantificable es la brecha de riqueza que persiste hoy.

La investigación académica sobre los mapas de la HOLC — que fueron desclasificados y digitalizados en décadas recientes— ha permitido establecer correlaciones notablemente precisas entre los vecindarios marcados en rojo en los años 1930 y los indicadores actuales de segregación residencial, riqueza media, acceso a servicios, y esperanza de vida. Esa correlación no prueba por sí sola la

### causalidad (confounding factors), pero combinada con el análisis del grafo causal del sistema, sí puede sustentar un R* del nodo de diseño estatal significativamente alto.

### A.2  Construcción del grafo histórico

Nodo Actor/Factor Tipo Función causal

N1 FHA + HOLC: política federal de clasificación

Diseño central

Diseñó e implementó el sistema de clasificación. Sin este diseño, el redlining sistematizado a escala nacional no habría ocurrido. R* más alto del grafo, S bajo (el sistema era idiosincrático en su aplicación racial).

N2 Bancos e instituciones hipotecarias privadas

Ejecución / amplificación

Adoptaron y ampliaron el sistema de clasificación de la HOLC, incluso para préstamos no asegurados federalmente. La clasificación federal se convirtió en norma de facto para toda la industria.

N3 Agentes y corredores inmobiliarios

Ejecución local

Aplicaron el steering (dirigir a compradores negros fuera de vecindarios blancos) y blockbusting (inducir el pánico inmobiliario). Alta visibilidad, S alto.

N4 Legisladores y tribunales que no intervinieron

Omisión sistémica

La ausencia de regulación contra el redlining durante cuatro décadas fue

parte del diseño: el Congreso no legisló contra la práctica hasta 1968 a pesar de documentación extensiva de sus efectos.

N5 Sistema de tasación de propiedades

Técnico / instrumental

Las tasaciones de propiedades en vecindarios marcados en rojo eran sistemáticamente bajas porque el redlining reducía la demanda. El sistema de tasación amplificó el efecto original.

Nodo final Millones de familias que no pudieron acumular patrimonio a través de la vivienda propia durante el período de mayor crecimiento inmobiliario de la historia estadounidense.

Nf Familias negras excluidas del crédito hipotecario

### A.3  R* y la distribución de la causalidad del impago sistemático

En el redlining, el "impago" que el sistema "predijo" para los vecindarios rojos fue en gran medida una profecía autocumplida: los vecindarios no recibieron inversión porque fueron clasificados como peligrosos; la falta de inversión los depreció; la depreciación confirmó la clasificación inicial. El grafo causal del ciclo tiene la siguiente distribución de R*: 

Nodo R* S α 1934-68

Interpretación

~44% 0.28 0.00 Nodo de diseño dominante. S moderado-bajo: la aplicación racial sistemática era idiosincrática. Un sistema diseñado sin el criterio racial habría producido clasificaciones diferentes.

N1 — FHA/HOLC

~28% 0.65 0.02 Alta responsabilidad causal con S moderado. Adoptaron y amplificaron el sistema, pero cualquier banco en el mismo marco regulatorio y de incentivos habría actuado similarmente.

N2 — Bancos privados

~14% 0.85 0.03 Alta sustituibilidad. El steering era una práctica cultural generalizada en la industria.

N3 — Agentes inmobiliarios

~10% 0.70 0.02 La inacción durante cuatro décadas fue parte del diseño del sistema, aunque con S moderado.

N4 — Omisión legislativa

~4% 0.90 0.05 Amplificador estructural con S muy alto.

N5 — Sistema de tasación

### El vector de R* confirma la lectura del cálculo: el 72% de la responsabilidad causal del ciclo de exclusión residía en los

nodos de diseño institucional (N1 y N2), y el α de todos esos nodos en el período activo del sistema estaba en el rango 0.00-0.05. El Índice de Justicia Estructural del sistema crediticio estadounidense durante este período:

J_redlining = 1 − Σ|Δᵢ| ≈ 1 − (0.44 + 0.28 + 0.12 +

$$0.08 + ...) ≈ 0.04$$

J = 0.04: injusticia estructural casi máxima. Los nodos de mayor R* asumieron prácticamente cero. El sistema de imputación crediticia atribuía el impago al deudor cuando el 96% del déficit de asunción estaba en los nodos de diseño.

A.4  El daño del redlining: cálculo de la brecha de riqueza acumulada

Parámetros documentados para el cálculo:

•  Familias negras potencialmente excluidas del crédito hipotecario federal: estimadas en 2.5-3.5 millones entre 1934 y 1968. •  Apreciación promedio de viviendas en áreas clasificadas como A y B entre 1940 y 1970: 300-400% en términos reales. •  Valor promedio de una vivienda en 1940 en dólares de 2024: ~$85,000 USD. •  Generaciones afectadas calculadas al 2024: 2.5 generaciones (nietos de quienes no pudieron comprar en 1950). •  Fracción de la brecha de riqueza actual atribuible al redlining según estimaciones económicas: 25-40%. •  Brecha de riqueza mediana actual entre familias blancas y negras (Federal Reserve, 2023): $171,000 USD. •  Número de familias negras actualmente en los EE.UU.: ~16.4 millones de hogares.

Cálculo del T_impedido (patrimonio no acumulado):

T_imp = 3,000,000 familias × $85,000 × (350%

apreciación) = ~$8.9 billones USD (2024)

ΔT_trayectoria (transmisión intergeneracional):

ΔT = $171,000 × 16,400,000 hogares × 0.325 (fracción

atribuible) = ~$914,000 M USD

D_vital expresado en tiempo de trabajo cristalizado:

D_vital = ($8.9B + $0.914B) / $8 por hora = 1.227 ×

10¹² horas de vida

Más de un billón de horas de vida. Ese es el tiempo de trabajo cristalizado en salarios que las comunidades afectadas no pudieron convertir en patrimonio acumulado porque el sistema crediticio les negó el instrumento de conversión por razón de raza. No es una metáfora: es la expresión exacta del principio ontológico del capítulo —el dinero es tiempo de vida cristalizado— aplicado al daño del redlining.

A.5  El estado actual del α diferido: ¿qué ha asumido el Estado?

La Fair Housing Act de 1968 prohibió el redlining formal (α_N1 ≈ 0.12: prohibición sin compensación). La Community Reinvestment Act de 1977 obligó a los bancos a servir a las comunidades donde operan, incluyendo las históricamente excluidas (α_N2 ≈ 0.20). Algunos programas locales de reparación (Evanston, Illinois en 2021) han comenzado a establecer compensaciones directas a familias afectadas por el redlining, aunque su escala es mínima respecto al D_total.

El α_diferido actual del sistema federal estadounidense respecto al redlining se estima en el rango 0.08-0.15: mucho menor que la Posición_heredada calculable. El Δ_diferido del Estado es positivo y sustancial. Eso es el fraude annona intergeneracional en el dominio crediticio: el Estado recibió los impuestos de las comunidades afectadas durante las décadas del redlining y no generó las condiciones materiales de posibilidad para su acumulación de patrimonio. La deuda sigue vigente.

Caso B — Algoritmos de crédito con sesgo racial (2019–2024)

R* del dataset vs. R* del directivo: el redlining invisible en los modelos de machine learning

B.1  El contexto: del redlining de papel al redlining algorítmico

En 2019, un estudio del Markup analizó 31 millones de solicitudes hipotecarias procesadas por los mayores prestamistas de los Estados Unidos usando datos del Home Mortgage Disclosure Act. Los resultados fueron publicados bajo el título "Secret Discrimination": los algoritmos de préstamo negaban hipotecas a solicitantes negros a tasas 80% más altas que a solicitantes blancos comparables en ingreso y deuda. El diferencial era más alto que el observado durante el período de aplicación formal del redlining en algunos estados.

Los algoritmos no tenían "raza" como variable explícita. Usaban código postal, historial de pagos, tipo de trabajo, antigüedad laboral, y en algunos casos comportamiento digital. Pero esas variables son proxis de la geografía de la segregación residencial histórica: los códigos postales de los vecindarios con alta concentración de familias negras son precisamente los que fueron marcados en rojo por la HOLC en los años 1930. El dataset entrenado con datos históricos de préstamos hipotecarios reproduce el mapa de la HOLC sin conocer su existencia.

El caso plantea la pregunta más técnicamente difícil del capítulo: ¿quién es causalmente responsable del sesgo —el algoritmo, el dataset, el directivo que aprobó el modelo, la empresa que lo diseñó, o el Estado que generó los datos históricos sesgados sobre los que fue entrenado?

### B.2  El grafo causal del sesgo algorítmico

Nodo Actor/Factor Tipo Función causal en el sesgo

N1 HOLC / sistema de redlining histórico (1934-1968)

Diseño histórico

Generó los datos con sesgo racial que estructuran la geografía actual de la segregación. Es el nodo de diseño original del sesgo que el algoritmo hereda.

N2 Dataset de entrenamiento (hipotecas históricas 1970-2015)

Nodo algorítmico

Contiene el sesgo histórico codificado como patrón estadístico. No tiene voluntad. Su R* apunta hacia N1 (que generó el sesgo) y hacia N3 (que lo aprobó sin auditar).

N3 Directivo que aprobó el modelo sin auditoría de equidad

Decisión humana

La persona con poder de aprobación que no realizó (o no exigió) una auditoría de disparate impact antes del despliegue. Este es el nodo humano con voluntad y el mayor Δ en el sistema contemporáneo.

N4 Empresa de tecnología financiera / prestamista

Institución Diseñó y comercializó el modelo. Tenía incentivos para maximizar la precisión estadística sin exigir equidad.

N5 Regulador financiero (CFPB, OCC)

Omisión regulatoria

La ausencia de estándares vinculantes de auditoría de equidad algorítmica hasta 2023 fue parte del entorno que permitió el sesgo.

Nodo final Personas que no accedieron al crédito o lo recibieron a mayor costo por el sesgo del modelo, no por su perfil crediticio real.

Nf Solicitantes de crédito con perfil de riesgo comparable pero código postal sesgado

### B.3  R* del dataset vs. R* del directivo

La pregunta más difícil del caso es: cuando el impago (o la denegación injusta del crédito) es causalmente producido por el sesgo del dataset, ¿quién tiene mayor R*: el dataset o el directivo que lo aprobó?

La respuesta del sistema es precisa: el dataset no tiene voluntad, por lo tanto no tiene α, no tiene hijos, y no puede ser sancionado. Pero sí tiene R* como posición causal en el grafo. El R* del dataset apunta estructuralmente hacia el directivo: si el directivo hubiera realizado la auditoría de equidad, el sesgo del dataset habría sido detectado antes del despliegue, y el daño no habría ocurrido o habría sido menor. El R* del directivo incluye su responsabilidad tanto por lo que hizo (aprobar el modelo) como por lo que no hizo (no exigir la auditoría).

Nodo R* est.

Δ y consecuencia

S est.

α est.

~32% 0.30 0.08 Δ = +0.24. Nodo histórico con α_diferido bajo. La Posición_heredada del Estado federal se extiende al dominio algorítmico.

N1 — Redlining histórico

~25% 0.55 N/A R* alto pero sin α (no tiene voluntad). Su R* se imputa al directivo que lo aprobó sin auditar. Δ del directivo incorpora el R* del dataset.

N2 — Dataset

~22% 0.35 0.05 Δ = +0.17 (propio) + fracción del R*_dataset = ~+0.30 total. Este es el nodo de mayor urgencia para la imputación contemporánea.

N3 — Directivo aprobador

~14% 0.50 0.10 Δ = +0.04. Responsabilidad moderada. Cualquier empresa con los mismos incentivos habría actuado similarmente (S moderado).

N4 — Empresa fintech

~7% 0.75 0.12 Δ = -0.05. El regulador no fijó estándares (Δ positivo histórico), pero S es alto: cualquier regulador en el mismo marco de incentivos habría actuado igual.

N5 — Regulador

### La fórmula de imputación del R* del dataset al directivo:

$$R*_efectivo_directivo = R*_directivo + R*_dataset ×$$

### P(detección | auditoría)

### donde P(detección | auditoría) es la probabilidad de que una auditoría de disparate impact estándar habría detectado

$$el sesgo. Para sesgos de la magnitud documentada por el Markup (80% mayor tasa de denegación), P(detección | auditoría) ≈ 0.90. Entonces:$$

$$R*_efectivo_directivo ≈ 0.22 + 0.25 × 0.90 = 0.445$$

Esto significa que el directivo que aprobó el modelo sin auditoría tiene una responsabilidad causal efectiva del ~44% del sesgo del sistema: su propia posición causal más la fracción del dataset que habría podido detectar y corregir. Ese es el número correcto para cualquier acción de responsabilidad.

### B.4  Los hijos del directivo: Potós como diagnóstico dominante

La investigación sobre los ejecutivos de las empresas fintech y los prestamistas que usaron modelos sesgados entre 2019 y 2024 produce un perfil de hijos que el sistema puede nombrar con precisión:

Evidencia

Perfil del directivo

Hijo dominante

La gran mayoría: uso del modelo estándar de la industria sin auditoría específica

Potós + Deimos

"Usamos el mejor modelo estadístico disponible." "No sabíamos que había sesgo." El directivo persiste en el paradigma de la eficiencia estadística sin cuestionarse la equidad. Potós hacia el modelo técnico establecido.

Minoría: directivos que recibieron advertencias internas y no actuaron

Potós + Anteros

Correos internos que documentan alertas de equidad ignoradas o minimizadas. "Nuestro modelo predice bien; la equidad no es nuestro problema regulatorio."

Harmonía Documentación de auditorías de disparate impact, de iteraciones del modelo hasta alcanzar equidad, de comunicación transparente con el regulador.

Casos aislados: directivos que auditaron y corrigieron proactivamente

El Potós dominante tiene una implicación regulatoria directa: la solución no es sancionar penalmente a los directivos (que genuinamente creían que estaban usando el mejor modelo técnico disponible) sino crear la obligación regulatoria de la auditoría de equidad antes del despliegue. El Potós se transforma con la estructura, no con la amenaza de sanción.

B.5 La solución sistémica: auditoría de equidad como α institucional obligatorio

El análisis del caso contemporáneo produce una recomendación de política directa que el sistema formaliza: la auditoría de equidad algorítmica antes del despliegue es la intervención que más eficientemente reduce el R*_efectivo del directivo y el Δ institucional.

Si la auditoría de equidad es obligatoria y el directivo la realiza, P (detección | auditoría) ≈ 0.90 implica que el R*_efectivo del directivo cae de ~44% a ~22% (su propio R* sin el R* del dataset que habría detectado). Ese es el impacto regulatorio calculable de hacer obligatoria la auditoría.

Δ_directivo_con_auditoría ≈ R*_directivo −

α_post_auditoría ≈ 0.22 − 0.60 = −0.38

Un Δ negativo después de la auditoría indica que el directivo asumió más de lo que causó: realizó la auditoría, corrigió el modelo, e implementó medidas de reparación para los afectados previos. Ese es exactamente el α institucional que

### el sistema requiere para que el Δ_diferido del redlining histórico comience a reducirse.

La paradoja del redlining algorítmico:  El algoritmo no discrimina con intención. Discrimina con precisión estadística. Esa es la forma más eficiente de discriminación que ha existido en la historia del crédito: produce resultados racialmente sesgados sin que ningún actor individual pueda ser señalado como racista en el sentido tradicional. El sistema de imputación causal es el único instrumento analítico que puede distribuir la responsabilidad en ese escenario porque no necesita intención: necesita posición causal. Y la posición del directivo que aprobó el modelo sin auditar es causalmente determinante.

## §5. Alcance y parámetros del método en score crediticio

### 5.1 El problema de la causalidad reversa en el crédito

En el análisis crediticio, la causalidad puede ir en ambas direcciones: el bajo FICO puede ser causado por condiciones estructurales (que producen el impago), pero el bajo FICO también puede causar condiciones estructurales (acceso a crédito de mayor costo, que produce mayor probabilidad de impago). Esta retroalimentación hace que la construcción del grafo causal sea más compleja que en los dominios anteriores, y que el R* del deudor pueda tanto sobrestimarse como subestimarse dependiendo de qué parte del ciclo se captura.

### 5.2 El problema de las variables proxy y la causalidad mediada

Cuando el sesgo opera a través de proxis (el código postal como proxy de la raza), la causalidad es mediada: el algoritmo no causa directamente discriminación racial — causa discriminación geográfica que es estadísticamente equivalente a la racial dado el patrón de segregación histórica. La construcción del grafo causal debe explicitar esa mediación: el R* del código postal como variable no es el R* de la raza como causa, pero está causalmente vinculado a ella a través del historial de segregación.

### 5.3 El R* del entorno macroeconómico en impagos masivos

En crisis sistémicas (la crisis hipotecaria de 2008, la pandemia de 2020), el R*_entorno puede dominar el grafo de impagos. En esos casos, imputar el impago principalmente al deudor produce la inversión causal más visible del sistema financiero: el deudor que no pudo pagar su hipoteca en 2009 porque perdió el empleo en la crisis diseñada por los instrumentos financieros de los que no participó. El sistema permite calcular ese R*_entorno con precisión, pero los datos macroeconómicos necesarios para estimarlo con rigor requieren acceso a series de tiempo que no siempre están disponibles a nivel de caso individual.

### 5.4 El límite de la acción individual cuando el nodo de diseño es estructural

Cuando el nodo con mayor R* es estructural y sistémico (el sistema de redlining, la arquitectura del sistema financiero que produce crisis recurrentes), el análisis causal identifica el problema con precisión, pero la solución no puede ser individual. Un deudor afectado por el redlining algorítmico no puede demandar al dataset. Puede demandar al directivo y a la empresa, pero la reparación proporcional al daño total requiere acción sistémica: cambio regulatorio, auditorías obligatorias, programas de compensación colectiva. El sistema identifica los nodos de mayor R* y Δ, pero la política que actúa sobre ellos trasciende el litigio individual.

### 5.5 El uso predictivo del índice de causalidad del impago

Los cuatro apartados anteriores aplicaron R* al impago ya ocurrido. Pero el índice de causalidad tiene una dimensión predictiva natural que ningún modelo correlacional convencional replica: puede identificar, antes de que el impago ocurra, qué fracción de la probabilidad de impago es causalmente atribuible al sistema crediticio (R*_sistema)

y qué fracción es causalmente atribuible al deudor (R*_deudor). Y puede estimar cuándo el regulador detectará el sesgo de un algoritmo dado el ritmo de acumulación del disparate impact.

### Predictor 1: probabilidad de impago causal pre-evento

El modelo FICO predice P(impago) sobre la clase de riesgo. El análisis causal lo descompone antes de que ocurra:

P(impago_causal_sistema) ᵢ = R*_sistema ×

P(impago_total) ᵢ

P(impago_causal_deudor) ᵢ = R*_deudor ×

P(impago_total) ᵢ

Esta descomposición, aplicada sobre la cartera antes de que los impagos ocurran, produce el mapa de riesgo sistémico de la cartera: la fracción de la pérdida esperada que es estructural (atribuible al sistema de crédito) y la fracción que es idiosincrática (atribuible al comportamiento del deudor).

Perfil de deudor P(impago) FICO

R*_sistema estimado

Pérdida esperada causal del sistema

12% 0.42 5.0% — el 42% del 12%

Código postal de vecindario históricamente redlineado

10% 0.08 0.8% — solo el 8% del 10%

Código postal sin historia de exclusión

18% 0.12 2.2% — el 12% del 18%

Deudor con historial de impago personal

La diferencia entre las dos primeras filas —5.0% vs. 0.8% de pérdida esperada atribuible al sistema— es la huella del redlining algorítmico en la cartera antes de que produzca ningún impago real. Un regulador que solo mira la tasa de impago realizada llega tarde; este predictor llega antes.

Predictor:  Si R*_sistema × P(impago) supera un umbral θ_equidad en un segmento de la cartera, el algoritmo es predictivamente sesgado con independencia de si los impagos ya han ocurrido. La auditoría de equidad debe actuar sobre este predictor, no esperar la evidencia post-hoc.

### Predictor 2: tiempo hasta la detección regulatoria del sesgo algorítmico

El disparate impact (DI) de un algoritmo sesgado se acumula en la cartera con cada ciclo de crédito. El regulador lo detecta cuando el DI observado supera el umbral de evidencia estadística. El tiempo hasta esa detección es predictible:

t_detección ≈ log (θ_DI / DI₀) / log (1 +

r_acumulación × n_ciclos)

donde DI₀ es el disparate impact inicial del algoritmo, θ_DI es el umbral estadístico de detección regulatoria (habitualmente DI ≥ 1.25, es decir 25% mayor tasa de denegación para el grupo protegido), r_acumulación es la tasa a la que el DI crece por ciclo de crédito (función del crecimiento de la cartera en el segmento sesgado), y n_ciclos es el número de ciclos por año.

Aplicación numérica — Algoritmo con sesgo inicial:

•  DI₀ = 1.18 (18% mayor tasa de denegación al inicio, bajo el umbral de detección de 1.25).

•  r_acumulación = 0.04 por año (la cartera en el segmento sesgado crece al 4% anual). •  θ_DI = 1.25 (umbral regulatorio estándar).

t_detección ≈ log (1.25 / 1.18) / log (1.04) ≈ 0.0566 /

$$0.0392 ≈ 1.4 años$$

El algoritmo cruzará el umbral de detección regulatoria en aproximadamente diecisiete meses si la cartera sigue creciendo al ritmo actual. El beneficio predatorio que la aseguradora obtiene antes de la detección es:

B_antes_detección = Δ_B_ciclo × t_detección =

($8M / año) × 1.4 = $11.2M USD

Ese es el incentivo a actuar antes que el regulador: si el diseñador del algoritmo audita y corrige antes de los diecisiete meses, evita la multa regulatoria (estimada en $47.5M en §4.3). El ROI de la auditoría anticipada es positivo por un margen de más de cuatro a uno.

### Predictor 3: ROI de la auditoría de equidad como intervención preventiva

ROI_auditoría = (Multa_evitada × P_detección −

Costo_auditoría) / Costo_auditoría

Con P_detección = 0.30, multa = $47.5M, costo típico de auditoría de equidad = $0.8M:

ROI = (0.30 × $47.5M − $0.8M) / $0.8M = ($14.25M

− $0.8M) / $0.8M ≈ 1,681%

El ROI de la auditoría de equidad supera el 1,600% cuando se incluye la probabilidad de detección. Este es el argumento cuantitativo que convierte la regulación basada en Δ_B en herramienta de gestión de riesgo para las propias instituciones financieras, no solo para los reguladores.

⚠ La predicción del tiempo de detección asume que el regulador aplica el umbral DI ≥ 1.25 de manera consistente. Si la supervisión es irregular, t_detección puede ser muy superior al estimado, lo que aumenta el beneficio predatorio, pero también aumenta el daño acumulado. El argumento para la supervisión algorítmica continua en tiempo real es precisamente reducir la incertidumbre sobre t_detección.

### Código de referencia: predictor de impago causal y tiempo de detección

import numpy as np  def predictor_sesgo_crediticio(DI_inicial, r_acumulacion,                                 theta_DI=1.25, n_ciclos_anio=12, delta_B_anual=8e6,                                 P_deteccion=0.30, costo_auditoria=800_000, multa_base=47_500_000):     """     Predicción de tiempo hasta detección regulatoria del sesgo algorítmico     y ROI de la auditoría preventiva.     """     import math     # Tiempo hasta cruzar el umbral DI if DI_inicial >= theta_DI:         t_det = 0.0  # ya cruzó el umbral     else: t_det = math.log(theta_DI / DI_inicial) / math.log(1 + r_acumulacion) B_antes = delta_B_anual * t_det     multa_esperada = multa_base * P_deteccion     ROI_auditoria = (multa_esperada - costo_auditoria) / costo_auditoria      return {         't_deteccion_anios': round(t_det, 2), 't_deteccion_meses': round(t_det * 12, 1), 'B_acumulado_antes_deteccion': B_antes,         'multa_esperada': multa_esperada,         'ROI_auditoria_preventiva': ROI_auditoria, 'conviene_auditar': ROI_auditoria > 0,     }  def descomposicion_causal_cartera(R_star_sistema, P_impago_FICO, monto_credito_promedio, n_deudores):     """     Descompone la pérdida esperada de la cartera entre     componente causal del sistema y del deudor.     """     P_impago_causal_sistema = R_star_sistema * P_impago_FICO     P_impago_causal_deudor  = (1 - R_star_sistema) * P_impago_FICO     perdida_sistema  = P_impago_causal_sistema * monto_credito_promedio * n_deudores     perdida_deudores = P_impago_causal_deudor  * monto_credito_promedio * n_deudores return {         'P_causal_sistema':  P_impago_causal_sistema, 'P_causal_deudor':   P_impago_causal_deudor, 'perdida_esp_sistema': perdida_sistema,         'perdida_esp_deudor': perdida_deudores,         'fraccion_recuperable_via_auditoria': R_star_sistema,     }  # ── Ejemplo: algoritmo con sesgo docum. (DI_0 = 1.18) ── res_t = predictor_sesgo_crediticio(     DI_inicial=1.18, r_acumulacion=0.04,     delta_B_anual=8e6, P_deteccion=0.30, costo_auditoria=800_000, multa_base=47_500_000) print("=== Predictor de detección regulatoria ===") for k, v in res_t.items(): print(f"  {k}: {v}")  # ── Ejemplo: descomposición causal de cartera ── res_c = descomposicion_causal_cartera(     R_star_sistema=0.42, P_impago_FICO=0.12,     monto_credito_promedio=250_000,

n_deudores=5_000) print("\n=== Descomposición causal de cartera (seg. redlineado) ===") for k, v in res_c.items():     print(f"  {k}: {v:,.0f}" if isinstance(v, float) and v > 1 else f"  {k}: {v:.4f}")

## §6. Profundización formal

### 6.1 El grafo del ciclo de exclusión crediticia: la profecía autocumplida

El redlining y el sesgo algorítmico no son simplemente discriminación en un punto del tiempo: son sistemas de retroalimentación que se auto-perpetúan. La formalización de ese ciclo es:

ψ(t+1) = f (W_crédito × ψ(t))

donde ψ(t) es el vector de estado del sistema crediticio en el período t (que incluye la distribución de acceso al crédito, la distribución de patrimonio, y la distribución geográfica del riesgo percibido). Si W_crédito incorpora el sesgo, la iteración produce un sistema donde el estado de t+1 es más sesgado que el de t porque el impago en t (parcialmente causado por la denegación del crédito) se incorpora al dataset de entrenamiento del período t+1.

La condición de estabilidad del ciclo sin sesgo creciente requiere que el eigenvector dominante de W_crédito no tenga componentes con correlación racial significativa. Si la tiene, el sistema está en un punto fijo sesgado y el R* del dataset crece con cada iteración.

### 6.2 Disparate impact formalizado: la conexión entre R* y el estándar legal

El estándar legal de disparate impact (Griggs vs. Duke Power, 1971, confirmado para el crédito en el Fair Housing Act) establece que una práctica puede ser ilegal si produce un impacto desproporcionado sobre un grupo protegido, aunque no haya intención discriminatoria. El sistema de imputación causal formaliza ese estándar:

Disparate_impact (algoritmo, grupo) = P (denegación | grupo_A) / P (denegación | grupo_B)

El ratio de 1.8 documentado por el Markup (probabilidad de denegación 80% mayor para solicitantes negros comparables) es el disparate impact medido. El R* del dataset en ese disparate impact es:

R*_dataset = [DI_observado − DI_esperado_sin_sesgo] / DI_observado

donde DI_esperado_sin_sesgo = 1.0 (igual probabilidad de denegación para perfiles comparables). Con DI_observado = 1.80: R*_dataset ≈ (1.80 − 1.0) / 1.80 = 0.44. El 44% del disparate impact observado es causalmente atribuible al sesgo del dataset —consistente con el R* del nodo N2 estimado en el análisis del §4.

### 6.3 La fórmula de equidad crediticia ajustada por causalidad

El score crediticio ajustado por causalidad (SCAC) es la herramienta que el sistema propone como alternativa al score FICO tradicional:

SCAC_i = FICO_i + γ × ΔContext_i − β ×

Sesgo_dataset_i

donde ΔContext_i es la corrección por condiciones estructurales que el FICO no captura (inversión en el vecindario, acceso al sistema financiero formal, historial de exclusión crediticia sistemática) y Sesgo_dataset_i es la

corrección por el sesgo geográfico codificado en el dataset histórico. Los parámetros γ y β se calibran para que SCAC produzca el mismo poder predictivo que FICO para el componente genuinamente idiosincrático del riesgo, sin el componente estructural que produce el disparate impact.

El SCAC no "reduce el umbral" para ciertos grupos: recalcula el score sobre la base de los factores causalmente atribuibles al deudor, excluyendo los causalmente atribuibles al sistema. Es la aplicación directa del principio R*_neta = R*_deudor × (1 − S_deudor) al scorecard.

### 6.4 Código Python de referencia

import numpy as np from scipy.stats import pearsonr  def analisis_credito(W_impago, alpha_nodos,                      D_total, w_ref=8.0,                      DI_observado=None, R_star_dataset_idx=None):     """     Análisis de causalidad del impago en sistemas crediticios.     W_impago:       matriz de pesos del grafo causal del impago     alpha_nodos:    α por nodo     D_total:        daño total monetario     w_ref:          salario de referencia (USD/hora) DI_observado:   disparate impact observado (ratio, e.g. 1.80) R_star_dataset_idx: índice del nodo-dataset (sin voluntad, sin α)     """ n = W_impago.shape[0]     # ── R* via operador de responsabilidad (RES-RSTAR-001) ──     A_D = list(range(n - 1))     Q_D = W_impago[np.ix_(A_D, A_D)]     b_D = W_impago[A_D, n - 1]     r_D = np.linalg.solve(np.eye(n - 1) - Q_D, b_D)     R_full = np.zeros(n)     R_full[A_D] = r_D / r_D.sum()     R_star = R_full      # ── S: fungibilidad del factor ──     S = np.zeros(n)     for i in range(n): max_c = 0         for j in range(n):             if j == i: continue             Wm = W_impago.copy()             Wm[i,:] = np.mean(W_impago, axis=0) Rm = np.ones(n)/n             for _ in range(200):                 Rm2 = Wm @ Rm; sm = np.sum(Rm2)                 if sm < 1e-12: break Rm2 /= sm                 if np.max(np.abs(Rm2-Rm)) < 1e-6: break Rm = Rm2             c, _ = pearsonr(R_star, Rm2)             max_c = max(max_c, abs(c))         S[i] = 1 - max_c      # α del dataset = 0 siempre (no tiene voluntad)     if R_star_dataset_idx is not None: alpha_nodos = alpha_nodos.copy() alpha_nodos[R_star_dataset_idx] = 0.0      Delta = R_star - alpha_nodos R_neta = R_star * (1 - S)      # ── Responsabilidad neta del deudor (si está en el grafo) ──     # Convención: el deudor es el primer nodo (índice 0)     AD_deudor = R_neta[0] * D_total  # ajuste debitor correcto      # ── R* efectivo del directivo (incorpora R* del dataset) ──     R_efectivo_directivo = None     if R_star_dataset_idx is not None:         P_deteccion = 0.90  # prob. de detección con auditoría estándar         # Asumimos que el directivo es el nodo que sigue al dataset         dir_idx = R_star_dataset_idx + 1         if dir_idx < n: 

R_efectivo_directivo = (R_star[dir_idx] + R_star[R_star_dataset_idx] * P_deteccion)      # ── Disparate impact y R* del sesgo ──     R_star_sesgo = None     if DI_observado and R_star_dataset_idx is not None:         DI_sin_sesgo = 1.0 R_star_sesgo = (DI_observado - DI_sin_sesgo) / DI_observado      # ── Daño en tiempo de vida ──     D_vital = D_total / w_ref      result = {         'R_star': R_star,         'S': S,         'Delta': Delta,         'R_neta': R_neta,         'AD_deudor_correcto': AD_deudor,         'D_vital_horas': D_vital,         'J_sistema': float(1 - np.sum(np.abs(Delta))),     }     if R_efectivo_directivo: result['R_efectivo_directivo'] = R_efectivo_directivo     if R_star_sesgo: result['R_star_dataset_sesgo'] = R_star_sesgo      return result  # ── Ejemplo: algoritmo con sesgo racial ── # Nodos: N0=Redlining_hist, N1=Dataset, N2=Directivo, N3=Empresa, N4=Regulador, N5=Nf W = np.zeros((6, 6)) W[0,1]=0.90; W[0,5]=0.70   # redlining → dataset, → Nf W[1,2]=0.85; W[1,5]=0.80   # dataset → directivo, → Nf W[2,3]=0.70; W[2,5]=0.75 # directivo → empresa, → Nf W[3,5]=0.65; W[4,5]=0.35   # empresa, regulador → Nf  alpha = np.array([0.08, 0.0, 0.05, 0.10, 0.12, 0.0]) D_total = 50_000_000  # USD daño en cartera analizada  res = analisis_credito(W, alpha, D_total,                        w_ref=8.0, DI_observado=1.80,                        R_star_dataset_idx=1)  nodos = ['N0-Redlining','N1-Dataset','N2-Directivo','N3-Empresa','N4-Regulador','Nf'] print("=== Score crediticio — Sesgo algorítmico ===") for i, (nm, rs, si, di) in enumerate(zip(     nodos, res['R_star'], res['S'], res['Delta'])):     nota = ' ← NO tiene voluntad' if i == 1 else ''     print(f" {nm:18s} R*={rs:.3f} S={si:.2f} Δ={di:+.3f}{nota}")  if 'R_efectivo_directivo' in res:     red = res['R_efectivo_directivo'] print(f"\nR*_efectivo_directivo:  {red:.3f} (incluyendo R*_dataset × P_detección)") if 'R_star_dataset_sesgo' in res:     rds = res['R_star_dataset_sesgo']     print(f"R*_dataset_en_DI:       {rds:.3f} (DI observado = {1.80})") J = res['J_sistema'] dv = res['D_vital_horas'] print(f"J (justicia estructural): {J:.3f}") print(f"D_vital: {dv:,.0f} horas de vida") print(f"AD_deudor_correcto:       USD {res['AD_deudor_correcto']:,.0f}")

Miguel Hilario Olvera Aguilar Centro Multidisciplinario Meriadock Formación y Asesoría A.C., 2026
