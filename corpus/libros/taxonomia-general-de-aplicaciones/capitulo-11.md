PARTE II · Ciencias Económicas y Financieras

## Capítulo 11

### Crédito y sistema financiero —

### fraude y colapso crediticio

Organ.  Estru.  Model.  Educa.  Crisi.

Para el mediador que busca precisión · Cómo usar este capítulo Este capítulo opera con tres análisis que deben distinguirse desde el inicio. El primero es el análisis causal del impago individual: distribución de la responsabilidad del impago entre el deudor, el diseñador del producto crediticio, el algoritmo y el entorno macroeconómico. El segundo es el análisis del sesgo sistémico: cómo el nodo algorítmico transmite el daño histórico al sistema presente, y quién tiene R* sobre ese sesgo. El tercero es el análisis del riesgo sistémico y el colapso financiero: quién tenía mayor posición causal en el diseño del sistema que hizo inevitable el colapso. Si tu prioridad es el análisis del impago individual, lee §1 a §5. Para el análisis del sesgo algorítmico, ve a §4.3. Para el colapso sistémico, ve a §4.4. Para cuantificar D_crédito, ve a §7. Para la prioridad de evidencia, ve a §9.

### §1  Descripción del subcampo

El crédito y el sistema financiero es el dominio donde el sistema de imputación causal introduce un tipo de nodo que no había aparecido en ningún capítulo anterior: el nodo algorítmico / dataset, con posición causal real en el grafo, pero sin voluntad propia, sin dolo y sin Hijos. Su R* no implica culpabilidad del algoritmo sino posición causal que apunta estructuralmente hacia el directivo que lo aprobó y hacia el

Taxonomía General de Aplicaciones

diseñador de la política que generó los datos con los que fue entrenado. Esa distinción — entre el R* del nodo sin voluntad y el R* del actor humano que lo creó o aprobó — es la contribución conceptual central de este capítulo.

La segunda distinción fundamental es entre el impago idiosincrático (causado principalmente por las condiciones y conductas específicas del deudor: R*_deudor alto) y el impago estructural (causado principalmente por el diseño del sistema crediticio: R*_sistema > R*_deudor). Esa distinción transforma la evaluación del riesgo crediticio de un ejercicio de predicción estadística sobre el deudor en un análisis causal del sistema completo que produce el impago.

El índice de causalidad del impago: R* en el sistema crediticio R*_impago = R*_deudor + R*_dataset + R*_directivo + R*_producto + R*_entorno_macro + ... Esta descomposición transforma la evaluación del riesgo crediticio. R*_deudor es la fracción del impago causalmente atribuible a las condiciones y conducta específicas del deudor. R*_sistema es la fracción atribuible al diseño del producto, al sesgo del algoritmo, a la política crediticia del acreedor y al entorno macroeconómico. Cuando R*_sistema > R*_deudor, el sistema tiene mayor responsabilidad causal en el impago que el deudor. La acción de cobro integral contra el deudor en ese escenario es la inversión causal clásica del sistema financiero. La distinción entre correlación crediticia y causalidad crediticia: el score FICO predice el impago con correlación estadística real. Pero esa correlación no implica causalidad en el sentido del sistema: no dice que el FICO bajo causó el impago. Puede decir que las condiciones que produjeron un FICO bajo — ingresos inestables, falta de historial crediticio formal, acceso solo a productos de alto costo — son las mismas condiciones que producen el impago. Y esas condiciones pueden tener un nodo de diseño con R* mucho mayor que el del deudor.

Sub-variantes del dominio

Impago individual y responsabilidad crediticia: la distribución de R* entre el deudor y el sistema en un impago específico. El

Taxonomía General de Aplicaciones

análisis determina qué fracción del impago era causalmente atribuible al deudor (su gestión financiera, su capacidad de servicio de la deuda, sus decisiones) y qué fracción era atribuible al producto (tasa excesiva para el perfil del deudor, términos irrazonables, condiciones de renegociación inexistentes), al algoritmo de scoring (sesgo que excluyó crédito justo), y al entorno macroeconómico.

Sesgo algorítmico y discriminación crediticia sistémica: el algoritmo de scoring produce resultados sistemáticamente desfavorables para grupos que, dado su perfil crediticio real, deberían recibir condiciones equivalentes a otros grupos. El sesgo opera a través de variables proxy que no son discriminatorias en sí mismas pero que capturan patrones de segregación histórica. R* del dataset y R* del directivo que aprobó el modelo sin auditoría de equidad son los instrumentos de imputación.

Crédito predatorio: el diseñador del producto financiero diseñó deliberadamente condiciones que hacían inevitable el impago para capturar el activo o generar ingresos por comisiones y penalizaciones que superaban el costo del capital. S_bajo del diseñador: la estructura específica del producto era idiosincrática y deliberada. Anteros dominante. R*_sistema alto, R*_deudor bajo.

Fraude financiero corporativo: el directivo de la institución financiera diseñó un esquema de falsificación de información, de ventas de productos que sabía inadecuados para el perfil del cliente, o de ocultación de riesgos a los accionistas y reguladores. La estructura del grafo es idéntica al fraude corporativo del cap. 6 (competencia), aplicada al dominio financiero.

Riesgo sistémico y colapso financiero: el diseño del sistema financiero — los instrumentos de seguridad, las calificaciones crediticias que no reflejaban el riesgo real, el marco de desregulación que permitió la escala del riesgo — creó las condiciones de un colapso que ningún actor individual podría haber producido solo. El índice de concentración de riesgo

Taxonomía General de Aplicaciones

### sistémico (ICRS) establece qué nodo del sistema tenía mayor posición causal en el colapso.

Fraude annona crediticio estatal: el Estado diseñó un sistema crediticio que excluía a grupos específicos del acceso al crédito (redlining) o que no reguló la discriminación algorítmica sistémica (inacción regulatoria), recibiendo los impuestos de las comunidades afectadas sin generar las condiciones materiales de posibilidad para su acumulación de patrimonio.

### §2  Escala de evidencia CF0–CF8 · Dominio crediticio y financiero

La escala CF0–CF8 traduce la jerarquía general E0–E8 al vocabulario del crédito y el sistema financiero. Su característica más relevante es la posición del peritaje financiero-cuantitativo (CF2) como instrumento central del dominio — incluyendo el análisis de disparate impact algorítmico, que transforma el sesgo estadístico en evidencia causal. Compilación directa desde El cálculo de la responsabilidad cap. 8 y cap. 9.

Descripción y ejemplos en el dominio crediticio

Nivel Tipo de evidencia

Rango

w

y financiero

CF1 Documento financiero o institucional directo

Expediente crediticio con los términos del producto y el perfil del deudor al momento de la aprobación; política interna de crédito del acreedor; correo o acta donde se tomó la decisión de diseño del producto o del algoritmo; estados financieros de la institución con los datos relevantes del período; registro de comunicaciones entre el directivo aprobador y el equipo que presentó advertencias de sesgo;

[0.74, 0.92]

Taxonomía General de Aplicaciones

Descripción y ejemplos en el dominio crediticio

Nivel Tipo de evidencia

Rango

w

y financiero

documentación de auditoría interna del sistema de scoring.

CF2 Peritaje financiero-cuantitativo especializado

Análisis de capacidad de servicio de la deuda que establece si el producto era razonablemente pagable dado el perfil del deudor; análisis de disparate impact que establece si el algoritmo producía diferencias estadísticamente significativas entre grupos comparables en ingresos y deudas; análisis de concentración de riesgo sistémico (ICRS) que establece la posición causal de cada nodo en el colapso; valoración del D_crédito mediante análisis de la brecha patrimonial generada por el sesgo o el colapso.

[0.65, 0.85]

CF3 Testimonios convergentes con corroboración documental

Declaraciones de deudores afectados cuyas versiones son compatibles entre sí y con al menos un registro documental consistente; testimonios de empleados de la institución que describen las prácticas de diseño del producto o del algoritmo; testigos del programa de clemencia en fraudes financieros corporativos.

[0.48, 0.66]

CF4 Análisis estadístico del comportamiento

Análisis que muestra que las tasas de impago, de denegación de crédito o de pérdida patrimonial del

[0.40, 0.62]

Taxonomía General de Aplicaciones

Descripción y ejemplos en el dominio crediticio

Nivel Tipo de evidencia

Rango

w

y financiero

del sistema crediticio

grupo afectado son estadísticamente incompatibles con su perfil crediticio objetivo; comparación de tasas de aprobación y condiciones entre grupos con perfiles comparables que muestra un diferencial estadísticamente significativo; análisis de la correlación entre el perfil del algoritmo de scoring y el patrón de segregación residencial histórica.

CF5 Documentación estructural del algoritmo o del producto con inferencia de función

Especificaciones técnicas del modelo de scoring o del producto financiero que muestran variables proxy discriminatorias o condiciones diseñadas para producir impago; estados financieros de la institución que muestran patrones de comisiones y penalizaciones inconsistentes con un producto diseñado para ser pagado.

[0.28, 0.48]

CF6 Inferencia estructural por posición en el sistema crediticio o financiero

El directivo o la institución tenía la posición, la información y el control sobre el sistema para haber diseñado o aprobado las condiciones que produjeron el daño, sin documentación directa del acto específico de diseño o aprobación.

[0.18, 0.38]

CF7 Correlación patrimonial o de

El deterioro patrimonial o la tasa de impago del grupo afectado correlaciona con

[0.07, 0.24]

Taxonomía General de Aplicaciones

Descripción y ejemplos en el dominio crediticio

Nivel Tipo de evidencia

Rango

w

y financiero

impago sin análisis causal

la variable o el período analizado sin que haya análisis que establezca la cadena causal específica.

CF8 Dicho único sin corroboración

Un solo testimonio o documento sin respaldo cuantitativo ni corroboración documental.

[0.04, 0.16]

CF0 Ausencia documentada de conexión causal

Análisis cuantitativo que establece que las tasas de impago o de denegación de crédito del grupo son estadísticamente consistentes con su perfil crediticio objetivo, o que el colapso habría ocurrido igualmente sin la posición causal del nodo analizado.

w = 0.00

El análisis de disparate impact como instrumento de traducción de CF4 a CF2 El análisis de disparate impact toma una diferencia estadística observada (tasa de denegación 80% mayor para un grupo dado sus características crediticias objetivas) y establece si esa diferencia es causalmente atribuible al diseño del algoritmo o del producto. Cuando el análisis de disparate impact es realizado por un perito especializado con metodología reproducible, la evidencia CF4 del patrón estadístico se transforma en evidencia CF2 del mecanismo causal. Sin el peritaje que establece el mecanismo, la diferencia estadística es CF4 y sustenta aristas en el rango [0.40, 0.62]. Con el peritaje, la evidencia alcanza CF2 [0.65, 0.85].

### §3  Firmas documentales por Hijo e información para S

### En el dominio crediticio, los Hijos de Afrodita aplican exclusivamente a los directivos y reguladores con poder de

Taxonomía General de Aplicaciones

decisión sobre el diseño del producto, el algoritmo o la política crediticia. No aplican al algoritmo, al dataset, al producto financiero como nodo sin voluntad, ni al entorno macroeconómico. Para los nodos sin voluntad, S se estima directamente desde la evidencia cuantitativa de la determinación sistémica.

La distinción más relevante para la política regulatoria es entre Potós (el directivo persistió en el sistema heredado sin cuestionarlo — cualquier directivo en esa cultura institucional habría actuado igual: S alto, culpa habitual, solución regulatoria) y Anteros (el directivo defendió deliberadamente un sistema que sabía sesgado o defectuoso: S bajo, dolo eventual o directo, solución penal-civil).

### §3.1 Hijos de legibilidad alta en el dominio crediticio

Qué informa para S del

Firma en

Error de discrimina

Fuente document

el expediente

Hijo

ción frecuente

al típica

directivo

financiero

Anter os

S bajo [0.05, 0.28]. El directivo diseñó o defendió deliberadam ente condiciones crediticias sesgadas, predatorias o fraudulenta s con conocimien to explícito del daño que producían. La decisión

Comunicaci ones internas que documenta n el conocimien to del directivo del sesgo o del riesgo: alertas de equidad desestimada s por escrito, análisis de riesgo que el directivo recibió y no actuó,

Correos internos del directivo. Actas de comités de riesgo y cumplimien to. Documenta ción de alertas recibidas. Comparaci ón con decisiones de directivos de institucione s pares en el

Confundir con Potós cuando el directivo recibió alertas, pero las desestimó por creer genuinamen te que el modelo era correcto. La pregunta discriminan te: ¿el directivo sabía que el sistema producía

Taxonomía General de Aplicaciones

Qué informa para S del

Firma en

Error de discrimina

Fuente document

el expediente

Hijo

ción frecuente

al típica

directivo

financiero

fue genuinamen te idiosincrátic a: otros directivos en condiciones similares, con el mismo marco regulatorio y los mismos incentivos, no habrían producido las mismas condiciones .

presión documenta da sobre el equipo de cumplimien to para no reportar irregularida des. Decisiones que excedieron lo que el sistema de incentivos requería.

mismo período.

daño injusto, o creía que el modelo era técnicament e válido? El primero es Anteros; el segundo puede ser Potós.

Potós S moderado-alto [0.45, 0.80]. El directivo persistió en el uso del sistema crediticio heredado — el modelo de scoring, el producto financiero, la política de aprobación — sin cuestionarlo críticamente ni auditarlo para

Ausencia de documentac ión de análisis de equidad o de auditoría de riesgo en el expediente del modelo o del producto. Uso del modelo estándar de la industria sin evaluación independien te. Resistencia pasiva a

Expediente del modelo de scoring con fecha de última revisión o auditoría. Política interna de crédito con historial de actualizacio nes. Documenta ción de la industria sobre las prácticas estándar del período.

Confundir con Anteros cuando el directivo recibió advertencia s explícitas de miembros del equipo y las desestimó activamente . Si hay documenta ción de que el directivo suprimió o ignoró advertencia s de

Taxonomía General de Aplicaciones

Qué informa para S del

Firma en

Error de discrimina

Fuente document

el expediente

Hijo

ción frecuente

al típica

directivo

financiero

detectar sesgo o riesgo excesivo. "Los datos son los datos." "Siempre hemos usado este modelo." La conducta era deliberada pero no idiosincrátic a: cualquier directivo en esa cultura institucional habría hecho lo mismo.

revisiones del sistema. Documenta ción de que el directivo estaba al tanto del modelo pero no lo cuestionó.

equidad, Anteros moderado es más preciso que Potós.

Deim os

S alto [0.65, 0.90]. El directivo genuinamen te no comprendía las implicacion es del modelo o del producto financiero que aprobó. La parálisis ante la complejidad técnica del sistema de scoring o de

Ausencia total de documentac ión de evaluación del algoritmo o del producto antes de la aprobación. Sin alertas internas (que confirmaría n Potós o Anteros). El directivo aprobó el sistema

Expediente de aprobación del modelo o del producto. Documenta ción de onboarding del directivo. Comparaci ón con el nivel técnico esperado del cargo.

Confundir con Potós cuando había análisis disponibles en el sector que el directivo ignoró. Si el análisis de disparate impact era una práctica conocida en la industria en ese período y el directivo no lo aplicó,

Taxonomía General de Aplicaciones

Qué informa para S del

Firma en

Error de discrimina

Fuente document

el expediente

Hijo

ción frecuente

al típica

directivo

financiero

la estructura de riesgo del producto determinó la aprobación. Ausencia de análisis, no supresión de análisis.

siguiendo el procedimie nto estándar sin análisis adicional.

puede ser Potós (ignorancia electiva) más que Deimos (ignorancia genuina).

### §3.2 El Hijo del deudor: relevante para S del deudor en el impago idiosincrático

En el análisis del impago individual, cuando el análisis establece que R*_deudor es significativo, los Hijos del deudor informan la posición de v_t en el momento de las decisiones financieras que contribuyeron al impago. Fobos del deudor: actuó bajo presión financiera sistémica (pérdida de empleo, emergencia médica, crisis sistémica) que determinó el impago — S alto del deudor. Anteros del deudor: tomó decisiones idiosincráticas que, dado su perfil y las condiciones disponibles, otros deudores en la misma posición no habrían tomado — S bajo del deudor. Deimos del deudor: no comprendió completamente las condiciones del producto que firmó — lo que puede incidir en la responsabilidad del diseñador del producto que no proveyó información adecuada.

§3.3 Los nodos sin voluntad no tienen Hijo — el dataset y el producto financiero El algoritmo de scoring, el dataset de entrenamiento, el producto financiero estructurado y el índice de calificación crediticia son nodos causales sin voluntad propia. No tienen Hijo, no tienen α, no pueden ser sancionados directamente.

Taxonomía General de Aplicaciones

Su R* se imputa hacia los actores humanos que los diseñaron y aprobaron: el directivo que aprobó el algoritmo sin auditoría (R*_efectivo_directivo = R*_directivo + R*_dataset × P (detección | auditoría)), el diseñador del producto que estructuró las condiciones del impago, el regulador que permitió la escala del riesgo sin intervenir.

### §4  ¿Qué cuenta como asunción (α) en el dominio crediticio?

α en el dominio crediticio mide lo que el acreedor, el directivo o el regulador han hecho concretamente sobre su posición causal: corrección del sesgo del algoritmo con auditoría verificable, modificación del producto financiero para hacerlo razonablemente pagable, compensación a los deudores excluidos incorrectamente, reestructuración del crédito ante choques exógenos. Para el Estado: regulación que corrige la discriminación sistémica, programas de inclusión financiera proporcionales al déficit histórico.

α en el dominio crediticio es completamente independiente del dolo Un directivo que diseñó deliberadamente condiciones predatorias puede tener α alto si después auditó el sistema, corrigió el sesgo y compensó a los afectados. Un directivo que replicó el modelo estándar del sector sin comprender sus implicaciones puede tener α = 0 si nunca auditó ni corrigió el sistema una vez informado. Los Hijos informan S; α mide lo que el actor hizo después sobre su posición causal.

Acción del

¿Cuenta

para α? Razón Tipo de

actor

α

Auditoría de equidad del algoritmo con corrección verificable antes o después del daño

Sí — α estructural alto

La auditoría que detecta y corrige el sesgo es la asunción más valiosa en el dominio algorítmico: reduce P(detección|auditorí

Voluntari o

Taxonomía General de Aplicaciones

Acción del

¿Cuenta

para α? Razón Tipo de

actor

α

a) que determina R*_efectivo del directivo.

Compensación a los deudores afectados por el sesgo proporcional al AD_i

Sí — α económico proporcion al

Asunción económica directa de la posición causal verificable en el expediente.

Voluntari o o forzado

Modificación del producto para hacerlo razonablemente pagable dado el perfil del deudor

Sí — α estructural del producto

Modifica el sistema que producía el impago estructural.

Voluntari o o requerido

Reestructuració n del crédito ante choque macroeconómic o exógeno documentado

Sí — α de respuesta proporcion al

El acreedor asume parte del R*_entorno cuando reestructura ante choques que no son imputables al deudor.

Voluntari o o regulatori o

El regulador estableció estándares de auditoría de equidad obligatorios

Sí — α regulatorio

La regulación que hace obligatoria la auditoría es α institucional del regulador sobre el déficit que permitió.

Requerid o por mandato

El Estado implementó programas de inclusión financiera proporcionales al déficit histórico

Sí — α_diferido del Estado

Asunción diferida de la posición causal histórica del fraude annona crediticio estatal. Ver cap. 3 para el marco del α_diferido.

Voluntari o / político

No Declaración sin consecuencia concreta sobre la

—

Publicar un reporte de responsabilidad corporativa sin

Taxonomía General de Aplicaciones

Acción del

¿Cuenta

para α? Razón Tipo de

actor

α

modificar el algoritmo

posición causal. No modifica α.

### §4.3 La imputación del R* del dataset al directivo

R*_efectivo del directivo en el sesgo algorítmico R*_efectivo_directivo = R*_directivo + R*_dataset × P (detección | auditoría) P (detección | auditoría) es la probabilidad de que una auditoría de disparate impact estándar habría detectado el sesgo. Para sesgos de alta magnitud (diferencias de 80% o más en tasas de denegación controlando por perfil crediticio), P ≈ 0.90. Eso significa que el directivo que aprobó el modelo sin auditoría tiene responsabilidad causal efectiva del orden de R*_directivo + 0.9 × R*_dataset — la mayor parte de la posición causal del dataset le es imputable. Cuando el directivo realiza la auditoría y corrige el sesgo: α sube significativamente y R*_efectivo_directivo cae a R*_directivo solo (ya no incluye R*_dataset porque el sesgo fue detectado y corregido). La auditoría es tanto una acción de α como una reducción del R*_efectivo futuro. Eso es la auditoría como instrumento de α estructural.

### §4.4 El índice de concentración de riesgo sistémico (ICRS) en el colapso financiero

En el análisis de colapso financiero, el instrumento central no es el α individual de cada actor sino el ICRS — el índice de concentración de riesgo sistémico — que establece qué nodo del sistema financiero tenía mayor R* sobre el colapso colectivo. El ICRS responde la pregunta: sin este nodo específico (esta institución, este instrumento, esta política regulatoria), ¿habría ocurrido el colapso a esta escala?

Taxonomía General de Aplicaciones

ICRS_i = R*_i sobre el grafo de interdependencias financieras del sistema ICRS alto de un nodo significa que ese nodo era condición necesaria del colapso a esa escala — ya sea porque era un puente necesario en la red de transmisión del riesgo, porque su quiebra activaba cláusulas que producían quiebras en cascada, o porque su existencia era condición para que otros nodos mantuvieran su solvencia aparente. Diferencia fundamental con el análisis de riesgo convencional: el riesgo financiero convencional es un cálculo sobre la probabilidad de que un actor individual incumpla sus obligaciones. El ICRS es algo diferente y más difícil: la probabilidad de que la interconexión entre actores produzca un colapso en cascada que ninguno de ellos habría producido individualmente. Esta distinción no se captura con ninguna medida de riesgo convencional porque las medidas convencionales son por definición individuales.

### La escala de α en el dominio crediticio

Nivel Rango

Descripción

Indicadores en

α

observable

el expediente

Negación / evasión total

### 0.00 – 0.05 El acreedor o el directivo niega el sesgo o el daño, combate activamente el proceso sin ninguna acción concreta de corrección ni compensación.

Sin auditorías, sin correcciones del algoritmo, sin compensaciones. Impugnación activa de las determinaciones del regulador.

Reconocimiento nominal

0.06 – 0.20 Reconocimiento del impacto del sesgo o del daño crediticio sin consecuencia concreta. Declaración de "compromiso con la equidad financiera" sin modificación del sistema.

Comunicados de equidad financiera. Sin auditorías documentadas. Sin correcciones del modelo. Sin compensaciones.

Taxonomía General de Aplicaciones

Nivel Rango

Descripción

Indicadores en

α

observable

el expediente

Asunción parcial

### 0.21 – 0.45 Auditoría del algoritmo realizada pero sin corrección completa del sesgo, o compensación menor al AD_i estimado.

Reporte de auditoría documentado. Correcciones menores del modelo. Compensaciones documentadas del 10–30% del AD_i.

Asunción activa en proceso

### 0.46 – 0.70 Auditoría con corrección del modelo en proceso verificable y compensaciones sustanciales en curso.

Corrección documentada del algoritmo con datos comparativos antes-después. Compensaciones del 40–60% del AD_i. Programa de inclusión en proceso.

Asunción funcional

### 0.71 – 0.89 El modelo fue corregido con datos verificables de reducción del disparate impact y las compensaciones son proporcionales a la mayor parte del daño.

Reducción verificable del disparate impact post-corrección. Compensaciones del 70–85% del AD_i. Cumplimiento documentado con los estándares regulatorios de equidad.

Asunción plena 0.90 – 1.00 Corrección integral del sistema, compensaciones proporcionales al R* y mecanismos de auditoría permanentes que previenen la recurrencia.

Reducción del disparate impact a niveles estadísticamente no significativos. Compensaciones integrales documentadas. Programa de auditoría

Taxonomía General de Aplicaciones

Nivel Rango

Descripción

Indicadores en

α

observable

el expediente

permanente con seguimiento verificable.

### §5  Construcción del grafo típico del dominio crediticio

### Tipos de nodo en el grafo crediticio y financiero

Ejemplo

Tipo Función en el grafo S típico

en el dominio

Diseñador de política / directivo aprobador (D)

El actor con poder de decisión sobre el diseño del producto crediticio, el algoritmo de scoring o la política de aprobación. Es el nodo humano de mayor R*_neta cuando el sistema era idiosincrático. Sus Hijos informan S. La distinción Anteros/Potós/Dei mos determina si el proceso es penal o regulatorio.

Variable [0.15– 0.60]

El directivo que aprobó el algoritmo de scoring sin auditoría de equidad. El ejecutivo que diseñó el producto predatorio. El regulador que no estableció estándares de equidad a pesar de evidencia de disparate impact.

Nodo algorítmico / dataset (NA)

El algoritmo de scoring, el dataset de entrenamiento, el producto

N/A — no es actor con voluntad

El algoritmo de scoring entrenado

Taxonomía General de Aplicaciones

Ejemplo

Tipo Función en el grafo S típico

en el dominio

estructurado o la calificación crediticia. Tiene posición causal real en el grafo sin tener voluntad. Su R* se imputa al directivo que lo aprobó y al diseñador de la política que generó los datos sesgados. No tiene α, no puede ser sancionado directamente.

con datos históricos de segregación residencial. El dataset de hipotecas que reproduce el mapa del redlining. El modelo de calificación que otorgó AAA a instrument os de alto riesgo.

Institución financiera (IF)

El banco, la fintech o la institución de crédito que implementa y comercializa el sistema crediticio. R* positivo cuando sus decisiones institucionales eran condición de la escala del daño. S informa si cualquier institución con los mismos incentivos habría actuado igual.

Moderad o-alto [0.40– 0.80]

El banco que comercializ ó hipotecas subprime a deudores con perfil inadecuado . La fintech que desplegó el algoritmo sesgado. La institución que diseñó y vendió instrument os de alto riesgo como seguros.

Taxonomía General de Aplicaciones

Ejemplo

Tipo Función en el grafo S típico

en el dominio

Regulador omisivo (Reg)

La autoridad financiera que tenía información del riesgo sistémico o del sesgo algorítmico y no estableció los estándares que lo habrían prevenido. R* positivo cuando la omisión regulatoria fue condición de la continuidad del sistema que produjo el daño.

Alto [0.60– 0.90]

La Reserva Federal que observó el crecimient o de la burbuja hipotecaria y no usó los instrument os regulatorio s disponibles . La CFPB que tardó en establecer estándares de auditoría de equidad algorítmica.

Entorno macroeconómi co (EM)

Los choques exógenos (crisis financiera, pandemia, recesión) que contribuyeron causalmente al impago sin ser atribuibles a ningún actor específico. Nodo sin voluntad que informa S del deudor: cuanto más determinante fue el entorno, mayor es S del deudor y menor es R*_deudor.

N/A — no es actor

La crisis financiera de 2008. La pandemia de COVID-19. El ciclo de tasas de interés que hizo insostenibl es los créditos variables.

Deudor (Deu) El receptor del crédito y su capacidad de servicio de la deuda. R* positivo cuando las condiciones y

Variable [0.15– 0.80]

El deudor que incumplió el crédito hipotecario . El cliente

Taxonomía General de Aplicaciones

Ejemplo

Tipo Función en el grafo S típico

en el dominio

conductas específicas del deudor eran causalmente determinantes del impago. S informa cuánto del impago era estructural versus idiosincrático.

del producto predatorio. El solicitante de crédito excluido por el algoritmo sesgado.

### Configuraciones canónicas del grafo crediticio

Configuración 1 — Impago estructural con inversión causal contra el deudor D (diseñador del producto con tasa excesiva para el perfil) → IF (institución que comercializó) → Deu (deudor con R*_deudor bajo) → Impago La estructura clásica de la inversión causal crediticia: el sistema de cobro intenta recuperar el 100% del AD del impago del deudor cuando R*_deudor es menor que R*_sistema. AD_deudor = R*_deudor × (1 − S_deudor) × D_total. Si este valor es significativamente menor que el monto reclamado al deudor, la reclamación íntegra al deudor es jurídicamente inverosímil.

Configuración 2 — Sesgo algorítmico con nodo dataset y directivo aprobador Redlining histórico (N1, diseño original) → Dataset histórico (NA, nodo sin voluntad) → Directivo aprobador (D, R*_efectivo alto) → IF (institución, despliegue) → Deudores excluidos incorrectamente (Nf) R*_efectivo_directivo = R*_directivo + R*_dataset × P (detección | auditoría). El directivo no discriminó con intención, pero discriminó con precisión estadística al aprobar sin auditar. La solución regulatoria (auditoría obligatoria) actúa sobre el vínculo directivo-dataset reduciendo P (impacto no detectado).

Taxonomía General de Aplicaciones

Configuración 3 — Riesgo sistémico y colapso en cascada Marco_regulatorio_permisivo (ICRS alto como diseño) → Institución_sistémica (ICRS alto como nodo de transmisión) → Instrumentos_de_riesgo (NA sin voluntad) → Calificadoras_sesgadas (ICRS moderado) → Colapso_sistémico (Nf: todo el sistema financiero y sus usuarios) En el análisis de colapso sistémico, el ICRS de cada nodo determina quién era condición necesaria del colapso a esa escala. El argumento central: el colapso no fue el fracaso de la voluntad de los directivos de las instituciones involucradas, sino el fracaso de la arquitectura del sistema en el que operaban. La solución no puede ser solo individual: requiere reforma de la arquitectura del sistema.

### §6  Preguntas que responde este capítulo

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

¿El impago era principalmente atribuible al deudor (R*_deudor > R*_sistema) o al diseño del sistema crediticio (R*_sistema > R*_deudor)?

Análisis de R*_impago descompuesto en sus cuatro componentes: R*_deudor (capacidad objetiva de servicio de la deuda), R*_producto (condiciones del crédito frente al perfil), R*_dataset (sesgo algorítmico si aplica), R*_entorno (choques exógenos). El peritaje CF2 establece cada componente.

Declaración A o B si el expediente crediticio es completo. Declaración C si el análisis del algoritmo requiere inferencia estructural CF6.

¿El directivo que aprobó el algoritmo de scoring tiene R*_efectivo que incluye R* del dataset?

R*_efectivo_directivo = R*_directivo + R*_dataset × P (detección | auditoría). P se estima desde el análisis de disparate impact CF2: cuánto habría detectado

Declaración B si hay análisis CF2 del disparate impact y documentación CF1 del proceso de aprobación. Declaración C si P(detección) debe

Taxonomía General de Aplicaciones

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

una auditoría estándar del sector en ese período.

estimarse desde CF4.

¿El sistema crediticio producía discriminación sistemática contra un grupo con perfil crediticio comparable?

Análisis CF4 de disparate impact: tasa de denegación o de condiciones desfavorables del grupo afectado versus grupo comparable en ingresos y deudas. Si la diferencia es estadísticamente significativa → CF4 con w [0.40, 0.62]. Si el peritaje CF2 establece el mecanismo causal → CF2.

Declaración A o B si hay datos del Home Mortgage Disclosure Act u equivalente con análisis CF2. Declaración C si el análisis debe inferirse desde CF5.

¿El producto financiero era predatorio — diseñado para producir impago y capturar el activo o las comisiones?

Análisis CF2 de la estructura del producto: ¿las condiciones eran razonablemente pagables dado el perfil estándar del cliente objetivo? ¿El margen de comisiones y penalizaciones por impago superaba el ingreso esperado del crédito pagado? ¿El diseñador tenía incentivos para maximizar el impago?

Declaración B si los términos del producto y el perfil del cliente objetivo están documentados. Declaración C si el análisis de la intención del diseñador requiere inferencia CF6.

¿Qué nodo del sistema financiero tenía mayor ICRS — mayor posición causal en el colapso?

Construcción del grafo de interdependencias financieras del sistema y cálculo del ICRS_i = R*_i sobre ese grafo. El nodo con ICRS más alto es el que era condición necesaria del colapso a esa escala.

Declaración B si los datos del sistema de interdependencias son suficientes. Declaración C para los sistemas donde las interdependencias deben estimarse desde posiciones de mercado y correlaciones.

Taxonomía General de Aplicaciones

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

¿El Estado tiene posición causal histórica como nodo de diseño del sistema de exclusión crediticia — fraude annona crediticio?

Grafo histórico: Estado como diseñador del sistema de exclusión + análisis de α_diferido actual (cuánto ha asumido desde la prohibición del redlining formal). El mismo instrumento del cap. 3 (plano histórico): Posición_heredada del Estado y α_diferido de los sucesores institucionales del sistema de exclusión.

Declaración B si hay documentación histórica del sistema de exclusión y análisis CF4 del diferencial patrimonial persistente. Declaración C para la atribución de ΔT_trayectoria.

### §7  Traducción de D_crédito al dominio financiero

El D_crédito tiene una estructura tricomponente que se aplica a tres objetos distintos según el tipo de caso: el D_crédito del deudor individual (patrimonio perdido), el D_crédito de la comunidad excluida (acumulación de riqueza truncada), y el D_crédito del sistema (colapso sistémico). La distinción entre estos tres objetos es fundamental para construir la pretensión correctamente.

D_crédito del deudor

D_crédito de la

D_crédito del sistema

Componente

comunidad

individual

excluida

(colapso)

T_invertido (pérdida directa verificable)

Capital prestado no recuperado (acreedor). O: pagos que excedían el costo real del capital en crédito

Capital que los grupos excluidos habrían acumulado en el período de exclusión activa del sistema crediticio.

Pérdidas directas de depositantes, accionistas e inversores en el colapso. Capitalización pública de las instituciones en crisis.

Taxonomía General de Aplicaciones

D_crédito del deudor

D_crédito de la

D_crédito del sistema

Componente

comunidad

individual

excluida

(colapso)

predatorio (deudor).

T_impedido (oportunidad truncada durante el período activo)

Patrimonio no acumulado durante el período de exclusión crediticia: la vivienda no comprada, el negocio no capitalizado, la educación no financiada.

El diferencial de acumulación patrimonial entre los grupos con acceso al crédito justo y los grupos excluidos durante el período del sistema sesgado.

Crédito no disponible para empresas y familias durante el período de congelamient o del crédito post-colapso. Empleos no creados. Proyectos no ejecutados.

ΔT_trayectori a (diferencial persistente)

El diferencial de acumulació n futura entre la trayectoria con acceso al crédito justo y la trayectoria real con el sistema sesgado: brecha de riqueza que persiste después de la corrección del sistema.

La brecha de riqueza intergeneraciona l que persiste hoy como consecuencia del sistema histórico de exclusión. En el redlining: el componente del diferencial de riqueza 1:7 atribuible causalmente al sistema de exclusión.

El daño permanente a la confianza en el sistema financiero, la destrucción de valor de mercado de largo plazo, el costo de las reformas regulatorias necesarias como consecuencia directa del colapso.

Taxonomía General de Aplicaciones

D_vital_crédito: el daño crediticio expresado en horas de vida de trabajo cristalizado D_vital_crédito = D_crédito / w_ref [horas de vida cristalizadas en trabajo no recompensado] Esta conversión hace visible la dimensión ontológica del daño crediticio. Los recursos que el sistema sesgado extrajo de las comunidades excluidas representan horas de trabajo de personas que no se tradujeron en patrimonio acumulado porque el acceso al instrumento de conversión — el crédito justo — les fue negado por diseño. El dinero es tiempo de vida cristalizado: negar el acceso al crédito justo es negar la posibilidad de convertir el tiempo de trabajo en patrimonio duradero. Para el redlining: D_vital = (~$9.8 billones de patrimonio truncado) / $8 por hora ≈ 1.2 × 10¹² horas. Más de un billón de horas de vida de trabajo cristalizado que no se convirtieron en patrimonio acumulado por el diseño del sistema crediticio. Ese es el número que hace visible que la exclusión crediticia histórica no fue un problema de política pública secundario: fue uno de los daños ontológicamente más grandes documentados en la historia financiera de los Estados Unidos.

AD_i en el dominio crediticio: el ajuste debitor proporcional

AD_deudor = R*_deudor × (1 − S_deudor) × D_total. Este es el monto que es jurídicamente exigible al deudor: la fracción del impago causalmente atribuible a sus condiciones idiosincráticas. Si el monto reclamado al deudor supera significativamente el AD_deudor calculado, hay inversión causal en el sistema de cobro: el deudor está siendo imputado por más de lo que causó.

AD_sistema = R*_sistema × D_total es la fracción del daño atribuible al diseño del sistema. Para el acreedor que diseñó condiciones predatorias: AD_D = R*_D × D_total. Ese monto es la base de la pretensión de los deudores afectados y del regulador contra el diseñador del sistema que causó el impago estructural.

Taxonomía General de Aplicaciones

### §8  Límites del método y errores frecuentes de aplicación

Límites del método en el dominio crediticio y financiero

Límite 1 — El problema de la causalidad reversa en el crédito. El bajo score crediticio puede ser causado por condiciones estructurales (que producen el impago), pero el bajo score también puede causar condiciones estructurales (acceso a crédito de mayor costo, que produce mayor probabilidad de impago). Esta retroalimentación hace que la construcción del grafo causal sea más compleja que en los dominios anteriores, y que el R* del deudor pueda tanto sobrestimarse como subestimarse dependiendo de qué parte del ciclo se captura.

Límite 2 — El problema de las variables proxy y la causalidad mediada. Cuando el sesgo opera a través de proxis (el código postal como proxy de la historia de segregación racial), la causalidad es mediada: el algoritmo no causa directamente discriminación racial — causa discriminación geográfica que es estadísticamente equivalente a la racial dado el patrón de segregación histórica. La construcción del grafo causal debe explicitar esa mediación.

Límite 3 — El R* del entorno macroeconómico en impagos masivos. En crisis sistémicas, R*_entorno puede dominar el grafo de impagos. En esos casos, imputar el impago principalmente al deudor produce la inversión causal más visible del sistema financiero. Los datos macroeconómicos necesarios para estimar R*_entorno con rigor requieren series de tiempo que no siempre están disponibles a nivel de caso individual.

Límite 4 — La solución regulatoria trasciende el litigio individual. Cuando el nodo de mayor R* es el dataset o el marco regulatorio (estructural y sistémico), el análisis identifica el problema con precisión, pero la reparación proporcional al daño total requiere acción sistémica: cambio regulatorio, auditorías obligatorias, programas de compensación colectiva.

Taxonomía General de Aplicaciones

### El sistema identifica los nodos de mayor R* y Δ, pero la política que actúa sobre ellos trasciende el litigio individual.

### Errores frecuentes de aplicación

Error Por qué

Consecuen

cia Corrección

ocurre

Tratar el impago como hecho del deudor — R*_deudor = 1.0

El sistema de evaluación crediticia usa el score como predictor del impago y lo convierte en causa. La correlación estadística se confunde con causalidad causal.

El acreedor reclama el 100% del daño al deudor cuando R*_sistema puede ser mayor que R*_deudor. Inversión causal en el sistema de cobro.

Descomponer R*_impago en sus cuatro componentes con el expediente del caso. AD_deudor = R*_deudor × (1 − S_deudor) × D_total es el monto jurídicamente exigible al deudor.

Asignar R* al nodo algorítmico como si tuviera voluntad y pudiera ser sancionado

El analista incluye el dataset como actor en el grafo con R* y α propios.

El análisis produce una cadena de responsabilid ad que no puede ejecutarse: el dataset no puede ser sancionado ni puede asumir. La cadena de responsabilid ad se interrumpe.

El dataset y el algoritmo son nodos causales sin voluntad. Su R* se imputa íntegramente al directivo aprobador y al diseñador de la política histórica que generó los datos. No tienen α ni Hijos.

Taxonomía General de Aplicaciones

Error Por qué

Consecuen

cia Corrección

ocurre

No calcular R*_efectivo del directivo incluyendo R*_dataset

El analista separa el R* del directivo del R* del dataset sin calcular cuánto habría podido detectar el directivo con una auditoría.

R*_efectivo del directivo subestimado. La responsabilid ad del directivo parece menor de lo que la causalidad justifica porque no se incluye la fracción del dataset que habría podido corregir.

R*_efectivo_direc tivo = R*_directivo + R*_dataset × P (detección | auditoría). Estimar P desde el análisis de disparate impact CF2 del período: ¿qué habría detectado una auditoría estándar?

Usar el ICRS individual de una institución sin el contexto del sistema de interdependen cias

El analista calcula el riesgo de la institución sin mapear su posición en la red de dependenci as del sistema financiero.

El ICRS subestimado o sobreestimad o. Una institución puede tener riesgo individual bajo pero ICRS alto porque su colapso activa cascadas que la institución sola no explicaría.

El ICRS requiere el grafo de interdependencias del sistema completo, no solo el riesgo individual de cada nodo. El análisis del colapso sistémico es sistémico por definición.

### §9  Guía de prioridades de recolección de evidencia

Taxonomía General de Aplicaciones

Si tu prioridad es saber qué buscar primero para reducir la incertidumbre más relevante de tu caso crediticio o financiero, usa la tabla y el árbol que siguen. La primera decisión siempre es identificar el análisis: impago individual, sesgo algorítmico, o colapso sistémico.

### Tabla de prioridades de recolección de evidencia crediticia y financiera

Si tu incertid

Qué buscar /

La evidencia

Qué rango reduce

Por qué funciona

umbre principa

que más la reduce es…

qué pregunt

l es…

ar

### 1. ¿El impago era atribuible al deudor o al sistema crediticio ?

Análisis de capacidad de servicio de la deuda CF2: ¿las condiciones del producto (tasa, plazo, pago mensual) eran razonablement e pagables dado el perfil de ingresos del deudor al momento de la aprobación? Comparación con productos equivalentes del mercado.

Si las condicione s hacían el pago objetivame nte inviable dado el perfil del deudor → R*_produc to alto → la acción de cobro íntegra contra el deudor no tiene base causal proporcion al.

Reduce rango de R*_deud or vs R*_prod ucto (incertid umbre empírica)

¿Cuál era la relación pago/ing reso del deudor al moment o de la aprobaci ón? ¿El producto era estándar del sector o tenía condicio nes atípicas? ¿Había opciones de renegoci ación disponibl es que el acreedor no ofreció?

Taxonomía General de Aplicaciones

Si tu incertid

Qué buscar /

La evidencia

Qué rango reduce

Por qué funciona

umbre principa

que más la reduce es…

qué pregunt

l es…

ar

### 2. ¿El algoritm o producía disparate impact contra un grupo con perfil compara ble?

Análisis CF4 de tasas de aprobación y condiciones por grupo controlando por perfil crediticio objetivo. Si el diferencial es estadísticamen te significativo → CF4. Peritaje CF2 que establece el mecanismo causal si el análisis supera CF4.

Sin análisis cuantitativ o comparativ o, la discriminac ión algorítmica no es demostrabl e con certeza. El análisis CF4 es la puerta de entrada; el peritaje CF2 es el instrument o que establece la causalidad.

Determi na si hay sesgo algorítmi co y el nivel CF de la evidencia (incertid umbre empírica)

¿Hay datos del tipo HMDA u equivalen te para analizar las tasas de aprobaci ón por grupo? ¿La institució n tiene documen tación del proceso de aprobaci ón y de las variables usadas por el algoritm o?

### 3. ¿El directivo tenía conocimi ento del sesgo — Hijo dominan te del directivo ?

Comunicacion es internas CF1 que muestran si el directivo recibió alertas de equidad o de riesgo. La distinción Anteros/Potó s/Deimos desde esas comunicacion

El Hijo dominante determina el tipo de culpabilida d y el tipo de solución. Potós → solución regulatoria. Anteros → proceso

Reduce rango de S del directivo (incertid umbre ontológic a)

¿Hay correos internos del directivo sobre el algoritm o o el producto ? ¿Recibió adverten cias de

Taxonomía General de Aplicaciones

Si tu incertid

Qué buscar /

La evidencia

Qué rango reduce

Por qué funciona

umbre principa

que más la reduce es…

qué pregunt

l es…

ar

es (§3.1) determina si el proceso es penal o regulatorio.

penal. Deimos → negligencia civil y cambio de proceso.

equidad o de riesgo? ¿Actuó sobre ellas o las desestim ó? ¿Cuál era la práctica estándar del sector en ese período?

### 4. ¿Cuál es el R*_efecti vo del directivo incluyen do el R* del dataset?

Análisis CF2 del disparate impact + documentació n CF1 del proceso de aprobación. P(detección | auditoría) se estima desde la magnitud del disparate impact documentado y la disponibilidad de herramientas de auditoría estándar en el período.

R*_efectiv o = R*_directi vo + R*_dataset × P(detecció n). Si P ≈ 0.90 (sesgo de alta magnitud), el directivo tiene responsabil idad efectiva dominante sobre el sesgo del algoritmo.

Establec e la magnitud de la responsa bilidad del directivo (incertid umbre empírica)

¿Qué magnitud tenía el disparate impact documen tado? ¿Había herramie ntas de auditoría estándar disponibl es en el sector en ese período? ¿El directivo las usó para otros sistemas del portafoli o?

Taxonomía General de Aplicaciones

Si tu incertid

Qué buscar /

La evidencia

Qué rango reduce

Por qué funciona

umbre principa

que más la reduce es…

qué pregunt

l es…

ar

### 5. ¿Qué nodo del sistema financier o tenía mayor ICRS en el colapso?

Construcción del grafo de interdependen cias CF2: mapear las exposiciones cruzadas entre nodos, las cláusulas de activación en cascada, y las dependencias de liquidez entre instituciones. El ICRS se calcula sobre ese grafo.

El ICRS identifica el eslabón crítico del sistema — el nodo sin cuyo colapso la crisis no habría alcanzado esa escala. Sin el grafo de interdepen dencias, el análisis del colapso solo puede atribuir causalidad a los nodos visibles (los que quebraron) no a los que hicieron inevitable la quiebra sistémica.

Identifica el nodo de mayor posición causal en el colapso (incertid umbre sistémica )

¿Qué institució n, instrume nto o política tenía mayor exposició n cruzada con el resto del sistema? ¿Cuáles eran las cláusulas de activació n en cascada? ¿Qué habría ocurrido si ese nodo específic o hubiera sido rescatado o eliminad o antes del colapso?

### 6. ¿Cuál es el D_crédit o de la comunid ad excluida

Análisis de brecha patrimonial CF2: diferencial de acumulación de riqueza

El D_vital_cr édito = D_crédito / w_ref hace visible la

Establec e la escala del argument o de reparació n

¿Hay datos de registro de propieda des del período

Taxonomía General de Aplicaciones

Si tu incertid

Qué buscar /

La evidencia

Qué rango reduce

Por qué funciona

umbre principa

que más la reduce es…

qué pregunt

l es…

ar

— base del argument o de reparació n?

entre el grupo excluido y el grupo comparable con acceso al crédito justo, durante el período de exclusión. El análisis histórico del tipo del redlining usa los mapas históricos de exclusión y los registros de transferencias inmobiliarias del período.

magnitud del daño en horas de trabajo cristalizado . Sin esa conversión , la brecha patrimonia l puede parecer un diferencial económico abstracto.

(incertid umbre empírica e histórica)

del sistema de exclusión ? ¿Hay datos de riqueza comparat iva actual entre grupos que permitan establece r el diferenci al atribuible al sistema? ¿El perito puede construir el escenario contrafác tico de acumulac ión sin exclusión ?

### Árbol de decisión crediticio: ¿qué buscar primero?

### El árbol comienza con la identificación del análisis: impago individual, sesgo algorítmico, o colapso sistémico.

Taxonomía General de Aplicaciones

¿Cuál es tu análisis principal?

├─ Análisis del impago individual: ¿R*_deudor o R*_sistema? │

└─  PRIORIDAD: Análisis de capacidad de servicio CF2 + condiciones del producto CF1.

· ¿Pago/ingreso > 40% al momento de la aprobación? → R*_producto significativo. · ¿El producto tenía condiciones atípicas del sector? → peritaje CF2 del diseño del producto. · AD_deudor = R*_deudor × (1 − S_deudor) × D_total. Si es < monto reclamado → inversión causal en el cobro.

├─ Análisis del sesgo algorítmico: ¿disparate impact y R*_efectivo del directivo? │

└─  PRIORIDAD 1: Análisis CF4 de disparate impact con datos HMDA u equivalente.

· ¿El diferencial de tasas de aprobación es estadísticamente significativo controlando por perfil? · Si sí → peritaje CF2 del mecanismo causal del sesgo. · PRIORIDAD 2: Comunicaciones internas CF1 del directivo para determinar Hijo (§3.1). · Potós → solución regulatoria (auditoría obligatoria). Anteros → proceso penal-civil. · R*_efectivo_directivo = R*_directivo + R*_dataset × P (detección | auditoría).

└─ Análisis del colapso sistémico: ¿qué nodo tenía mayor ICRS?

└─  PRIORIDAD: Grafo de interdependencias CF2 del sistema financiero en el período.

· Mapear exposiciones cruzadas entre instituciones y cláusulas de activación en cascada. · ICRS_i = R*_i sobre el grafo de interdependencias. El nodo de mayor ICRS era condición necesaria del colapso a esa escala.

Taxonomía General de Aplicaciones

· El colapso no fue fracaso de voluntad individual: fue fracaso de la arquitectura del sistema. La solución es sistémica.

— Fin del Capítulo 11 — Centro Multidisciplinario Meriadock Formación y Asesoría A.C.  · 2026

Taxonomía General de Aplicaciones

