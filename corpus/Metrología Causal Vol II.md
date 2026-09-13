CENTRO MULTIDISCIPLINARIO MERIADOCK

Formación y Asesoría A.C.

R.F.C. CMM250808AC8 “La fuerza interior nos impulsa, un pequeño apoyo de los demás nos bendice”

### Metrología Causal

——————

### Vol II

Miguel Hilario Olvera Aguilar

Colección: Metrología Causal

Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · Primera edición: 2026

© Centro Multidisciplinario Meriadock Formación y Asesoría A.C., 2026

Todos los derechos reservados. Ninguna parte de esta publicación

puede ser reproducida, almacenada o transmitida en manera alguna ni

por ningún medio, ya sea eléctrico, químico, mecánico, óptico, de

grabación o de fotocopia, sin permiso previo del editor.

Metrología Causal: Vol II causal © 2026 by Miguel Hilario Olvera Aguilar is licensed under CC BY-NC-ND 4.0. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-nd/4.0/ Metrología Causal · Vol. II

METROLOGÍA CAUSAL · VOLUMEN II

### INTRODUCCIÓN

### El lenguaje universal del análisis causal

Cómo leer el sistema sin importar el dominio del caso

### I.  El problema que esta introducción resuelve

El mediador que domina el Volumen I tiene un instrumento preciso y un problema concreto: la primera vez que abre un expediente real —un caso jurídico, una auditoría institucional, un caso clínico, un análisis de política pública— se enfrenta a un vocabulario que el sistema no habló. El abogado tiene nexo causal y dolo. El médico tiene factor etiológico y negligencia. El economista tiene variable instrumental y externalidad. El clínico tiene patrón de conducta y déficit de mentalización. Cada disciplina construyó durante siglos el lenguaje con el que describe lo mismo: quién fue condición necesaria de qué resultado, en qué proporción, con qué grado de asunción.

El sistema tiene la respuesta para todos ellos. La metrología causal no es una ciencia jurídica, ni médica, ni económica, ni psicológica: opera en el nivel de la estructura causal, que es invariante al dominio [Vol.I · Cap. I·3]. Pero tener la respuesta en un lenguaje que el interlocutor no reconoce produce el resultado más costoso en cualquier práctica: el mediador que sabe lo que hay

Metrología Causal · Vol. II

que calcular no puede comunicarlo, y el destinatario que necesita el análisis no puede usarlo.

Esta introducción resuelve ese problema una sola vez. No lo resuelve para cada dominio por separado —eso produciría setenta y ocho glosarios distintos para los setenta y ocho capítulos de la Taxonomía General de Aplicaciones, que es exactamente lo que el sistema no puede permitirse. Lo resuelve en el nivel de abstracción correcto: el nivel donde los conceptos del sistema y los conceptos de cada disciplina son reconocibles como instancias del mismo operador.

Lo que esta introducción produce es un glosario operativo de nueve conceptos con su tabla de equivalencias disciplinares, y una clasificación de los cinco tipos de pregunta causal que aparecen en todos los dominios. Con esos dos instrumentos, el mediador puede entrar a cualquier caso en cualquier dominio y comenzar a trabajar sin perder un grado de rigor formal.

### II.  Lo que este glosario es y lo que no es

El glosario de esta introducción no es un glosario filosófico. No define los conceptos en su nivel ontológico ni repite las derivaciones formales del Volumen I. El lector que necesita saber por qué el eigenvector es la medida correcta de la responsabilidad causal tiene el Capítulo IV·2 de este volumen y la Parte II del Volumen I. El lector que necesita saber qué es φ□ en su estructura formal tiene la Axiomatización del Sistema de la Doble Mediación. Este glosario asume que el mediador ya sabe qué son los conceptos y responde una pregunta diferente: cómo se llaman en cada dominio y cómo se operan.

La distinción es más importante de lo que parece. Un glosario filosófico dice qué es algo. Un glosario operativo dice qué

Metrología Causal · Vol. II

hacer con algo cuando el caso lo requiere. Este es un glosario operativo: cada entrada define el concepto en términos de la operación que produce, no de la ontología que lo funda.

La segunda restricción es igualmente importante. Este glosario no es exhaustivo sobre ninguna disciplina. Un abogado penalista encontrará que la columna "Derecho" simplifica vocabulario que en la práctica forense tiene matices importantes. Esa simplificación es deliberada: el propósito no es que el sistema hable el idioma de cada disciplina con toda su riqueza técnica interna, sino que el mediador pueda identificar en el vocabulario de su interlocutor el concepto del sistema que está siendo descripto. El glosario es una tabla de traducción, no un tratado disciplinar.

### III.  El glosario operativo universal

Los nueve conceptos que siguen son los únicos que el mediador necesita traducir para operar el sistema en cualquier dominio. El resto del vocabulario —eigenvector, método de potencias, grafo de Markov, convergencia, robustez— es vocabulario técnico del sistema que el mediador usa internamente y que no necesita traducirse al dominio del interlocutor. El análisis puede entregarse completamente en el idioma de la disciplina del destinatario; la maquinaria que lo produce es del sistema.

Concepto 1 · Nodo

Definición operativa: cualquier entidad —persona, institución, norma, sistema, algoritmo, proceso— que tenía capacidad de influir en el resultado analizado y que tomó decisiones o generó condiciones que actuaron sobre el grafo causal.

Metrología Causal · Vol. II

La condición de nodo no requiere intención ni conciencia: un protocolo institucional mal diseñado es un nodo si su operación fue condición necesaria de parte del resultado. Un algoritmo de scoring es un nodo si su función fue condición de parte del daño.

Dominio Cómo se llama el nodo

Lo que el mediador busca

Derecho penal / civil

Sujeto, parte, imputado, demandado, tercero

Quien tenía capacidad jurídica de actuar y cuya actuación fue condición del daño

Medicina / Salud pública

Factor etiológico, agente causal, actor institucional

El factor cuya eliminación contrafactual habría prevenido o modificado el resultado clínico

Economía / Política pública

Agente, actor, variable estructural, institución

El agente cuya decisión alteró la trayectoria del sistema más allá del ruido esperado

Psicología clínica

Actor, figura vincular, sistema familiar, institución

La entidad cuyo patrón de conducta fue condición del patrón de respuesta del sujeto

Ingeniería / Tecnología

Componente, subsistema, equipo diseñador, operador

El elemento cuya falla o decisión fue condición estructural de la falla sistémica

Auditoría institucional

Área, directivo, comité, protocolo, incentivo

La unidad de decisión cuya actuación fue condición de la desviación auditada

### Concepto 2 · Arista y peso

Metrología Causal · Vol. II

Definición operativa: la relación de influencia causal entre dos nodos, con una dirección —quién influye sobre quién— y un peso —con qué intensidad esa influencia contribuye al resultado. Las aristas no son correlaciones ni relaciones de precedencia temporal: son relaciones de condición necesaria estructural verificadas con evidencia.

El peso de cada arista se expresa como un rango [a_ij, b_ij] calibrado según el nivel de evidencia disponible. El mediador nunca asigna un peso puntual arbitrario: asigna el rango que la evidencia puede sostener. El midpoint del rango es el valor de cálculo; la amplitud determina la robustez del resultado [Vol.I · Cap. VI·2].

Dominio Cómo se llama la arista

Cómo se calibra el peso

Derecho Nexo causal, relación de causalidad, vínculo jurídico

Grado en que la actuación del nodo fue condición sine qua non verificada en el expediente

Medicina Relación etiológica, mecanismo causal, vía de acción

Fuerza de la evidencia clínica o epidemiológica que sostiene la relación

Economía Transmisión, canal de impacto, efecto estructural

Magnitud estimada del efecto con su intervalo de confianza o rango de sensibilidad

Psicología Influencia, patrón vincular, condicionamiento

Frecuencia, intensidad y consistencia temporal de la influencia observada

Ingeniería Dependencia funcional, propagación de falla, interfaz

Probabilidad de propagación de falla bajo condiciones operativas documentadas

Metrología Causal · Vol. II

Dominio Cómo se llama la arista

Cómo se calibra el peso

Auditoría Línea de reporte, dependencia de decisión, flujo de información

Grado en que la decisión del nodo superior condicionó la del nodo subordinado

Concepto 3 · R* (peso causal estructural)

Definición operativa: la fracción del resultado total que se explica por la posición estructural del nodo en el grafo causal. R* no mide la intención del nodo ni su visibilidad documental: mide cuánto del resultado desaparecería si el nodo fuera eliminado del grafo y reemplazado por el nodo nulo. Es el eigenvector principal normalizado de la matriz de pesos W.

La propiedad más contraintuitiva de R* —que un nodo puede tener R* alto, aunque esté poco documentado— es una consecuencia matemática del eigenvector, no una hipótesis adicional. El nodo que influye sobre muchos nodos de alto R* hereda centralidad, aunque sus aristas directas al nodo sumidero sean débiles [Vol.I · Cap. III·2].

Dominio Cómo se llama R*

Qué comunica al entregar R*

Derecho penal

Grado de responsabilidad causal, participación estructural

"Este nodo explica el X% del resultado dañoso independientemente de su intención declarada"

Derecho civil Contribución causal proporcional,

"La distribución que satisface los cuatro axiomas de proporcionalidad causal"

Metrología Causal · Vol. II

Dominio Cómo se llama R*

Qué comunica al entregar R*

cuota de responsabilidad

Medicina Peso etiológico, fracción atribuible, contribución al resultado

"Este factor explica el X% del resultado clínico en este sistema específico"

Economía Atribución de impacto, contribución estructural al resultado

"Esta decisión explica el X% de la variación observada en el indicador"

Psicología clínica

Peso causal del factor, contribución al patrón

"Este factor vincular explica el X% del patrón de conducta en este sistema"

Auditoría Responsabilidad estructural, peso en la distribución del riesgo

"Esta unidad concentra el X% de la responsabilidad causal de la desviación"

### Concepto 4 · S (sustituibilidad)

Definición operativa: la probabilidad de que cualquier otro nodo con el mismo perfil en la misma posición estructural hubiera producido el mismo resultado. S = 1.00 significa que la conducta era completamente predecible desde el campo: cualquier otro en esa posición habría hecho lo mismo. S = 0.00 significa que la conducta era completamente idiosincrática: ningún otro la habría producido.

Metrología Causal · Vol. II

S no es un juicio moral sobre el nodo. Es una descripción estructural de cuánto del resultado es atribuible al actor específico versus al campo que lo contenía. Los tres criterios universales de calibración son: (1) existencia de alternativa documentada, (2) conformidad con la norma o protocolo del dominio, (3) replicabilidad ante un par equivalente en la misma posición.

Dominio Cómo se llama S

Los tres criterios universales

Derecho Presión sistémica, estándar del sector, práctica habitual

Alternativa documentada + conformidad con la norma + replicabilidad ante par

Medicina Protocolo estándar, práctica clínica habitual, estándar de cuidado

Guía clínica existente + desviación documentada + conducta de pares equivalentes

Economía Incentivo estructural, regla de decisión sectorial, restricción institucional

Alternativa viable + cumplimiento de la regla del sector + comparación con agentes equivalentes

Psicología Condicionamiento heredado, patrón vincular aprendido, presión del contexto

Historia de refuerzo documentada + respuesta alternativa disponible + conducta de pares

Auditoría Incentivo de diseño, presión de meta, restricción de protocolo

Diseño del incentivo que generó la conducta + alternativas disponibles + unidades equivalentes

Metrología Causal · Vol. II

### Concepto 5 · α (asunción)

Definición operativa: la fracción de R* que el nodo integró como propia mediante acciones verificables orientadas a producir, modificar, o mitigar el resultado. α no mide intención ni declaración: mide conducta verificable con evidencia. Un nodo que declara alta responsabilidad, pero no tomó ninguna acción orientada a modificar el resultado tiene α bajo.

Los tres criterios universales de α: conocimiento —el nodo tenía información suficiente para prever el resultado—; acción —tomó acciones verificables orientadas a modificarlo—; oportunidad —tuvo momentos concretos donde podía haber actuado diferente. Cada criterio que falla pone un techo a α.

Dominio Cómo se llama α

Qué evidencia la calibra

Derecho Diligencia debida, buena fe, cumplimiento del deber de cuidado

Acciones preventivas documentadas + informes de riesgo + medidas correctivas tomadas

Medicina Adhesión al protocolo, diligencia clínica, manejo adecuado

Historia clínica + órdenes médicas + registros de monitoreo + acciones ante señal de alarma

Economía Cumplimiento regulatorio, implementación de política, capacidad de respuesta

Registros de implementación + indicadores de cumplimiento + respuesta ante señales de alerta

Psicología clínica

Responsabilidad integrada,

Conducta observable de reconocimiento + acciones de

Metrología Causal · Vol. II

Dominio Cómo se llama α

Qué evidencia la calibra

reconocimiento del acto, capacidad de rectificación

reparación + cambio de patrón verificable

Auditoría Cumplimiento del protocolo declarado, ejecución del control interno

Evidencia de aplicación del control + documentación de excepciones + acciones correctivas

### Conceptos 6 a 9 · Los cuatro conceptos derivados

Los cuatro conceptos que siguen se derivan formalmente del Teorema de la Responsabilidad Causal Proporcional [Vol.II · Cap. IV·2]. No son hipótesis adicionales: son consecuencias necesarias de R*, S y α. Se presentan aquí en su forma operativa; la demostración formal está en la Parte IV de este volumen.

Concepto Definici ón operativ a

Equivalen te en derecho

Equivale nte en medicin a

Equivalen te en auditoría

R*_neta = R* × (1−S)

La fracción idiosincrá tica del peso causal: cuánto del resultado

Responsabil idad personal neta excluyendo presión sistémica

Fracción atribuible idiosincrát ica excluyend o el estándar de práctica

Responsabil idad individual neta excluyendo incentivo de diseño

Metrología Causal · Vol. II

Concepto Definici ón operativ a

Equivalen te en derecho

Equivale nte en medicin a

Equivalen te en auditoría

es atribuible al actor específic o, excluyen do lo que cualquier otro en esa posición también habría producid o

Δ = R* × (1−α)

El déficit de asunción: cuánto del peso causal del nodo no fue integrado mediante acción verificabl e. Δ > 0 indica que el nodo causó más de lo

Incumplimi ento de obligación de cuidado, brecha de diligencia

Déficit de manejo, brecha entre deber de cuidado y conducta real

Brecha de cumplimien to entre protocolo declarado y ejecutado

Metrología Causal · Vol. II

Concepto Definici ón operativ a

Equivalen te en derecho

Equivale nte en medicin a

Equivalen te en auditoría

que asumió

IIC (Índice de Integridad Causal)

La congruen cia entre lo que el nodo de diseño declaró que producirí a y lo que produjo en operació n real. IIC = 1 indica congruen cia total; IIC = 0 indica divergenc ia total

Buena fe objetiva, coherencia entre declaración y conducta

Calidad del protocolo , congruen cia entre guía declarada y práctica real

Integridad del control interno, congruencia entre diseño y operación

Fraude annona = R*×(1−α)×(1 −IIC)

El producto de alta centralida d causal, baja asunción y baja congruen cia: la

Incumplimi ento agravado por posición de garante

Negligenc ia institucio nal agravada por posición de diseño

Falla sistémica de control interno con responsabili dad de diseño

Metrología Causal · Vol. II

Concepto Definici ón operativ a

Equivalen te en derecho

Equivale nte en medicin a

Equivalen te en auditoría

posición más grave que el sistema puede medir en un nodo de diseño institucio nal

### IV.  Los cinco tipos de pregunta causal

Todos los casos en todos los dominios producen exactamente uno de cinco tipos de pregunta causal. Identificar el tipo antes de construir el grafo es la primera operación del mediador porque el tipo de pregunta determina la serie del Método Prometeo que el análisis requiere, el estándar de evidencia que aplica, y la forma del documento que el análisis entrega.

La identificación del tipo no requiere conocer el dominio del caso: requiere escuchar con precisión lo que el destinatario necesita saber. Las preguntas de umbral que siguen son universales.

Metrología Causal · Vol. II

Tipo La pregunta que el destinatario necesita responder

Serie Ejemplo multidominio

I Derecho: ¿quién causó el daño y en qué fracción? · Medicina: ¿qué factor produjo el resultado clínico? · Auditoría: ¿qué decisión generó la desviación?

1 · Diagnóstico

¿Quién o qué fue condición necesaria de este resultado, y en qué proporción?

II Derecho: ¿la empresa cumplió su deber declarado? · Medicina: ¿el hospital siguió el protocolo? · Auditoría: ¿la política se implementó como fue diseñada?

2 · Compliance

¿El nodo de diseño operó en conformidad con lo que declaró que haría?

III Derecho: ¿resiste el análisis ante el tribunal? · Regulación: ¿resiste ante el regulador? · Medicina: ¿resiste ante el comité de ética?

3 · Imputación

¿Puede sostenerse la atribución de responsabilidad ante impugnación adversarial?

I + II Derecho: ¿cómo rediseñar el protocolo para evitar reincidencia? · Medicina: ¿cómo rediseñar el estándar? · Institución: ¿cómo rediseñar el incentivo?

4 · Prevención

¿Qué rediseño reduciría la centralidad causal de los nodos críticos en sistemas futuros?

Metrología Causal · Vol. II

Tipo La pregunta que el destinatario necesita responder

Serie Ejemplo multidominio

5 · Seguimiento

¿Cómo evoluciona la posición causal de un nodo a lo largo del tiempo?

I longitudinal

Psicología: ¿está cambiando el patrón de conducta? · Medicina: ¿está respondiendo el paciente? · Política pública: ¿está mejorando el indicador?

Los tipos 4 y 5 no estaban en el documento editorial original del Volumen II. Se incorporan en esta edición porque el corpus empírico de programas de intervención longitudinal —entre ellos el Programa ECO documentado en el Apéndice A— demostró que el sistema necesita protocolo explícito para preguntas prospectivas y de seguimiento, no solo retrospectivas. La serie que activan es la misma Serie I; lo que cambia es la orientación temporal del grafo y el tipo de declaración que el análisis puede producir.

### V.  Cómo leer este volumen

El Volumen II no explica. Opera. Cada sección responde exactamente una pregunta: ¿qué hace el mediador ahora? Nada que esté explicado en el Volumen I se repite aquí: se referencia con la

Metrología Causal · Vol. II

notación [Vol.I · Cap. X·Y]. El mediador que necesita entender por qué algo funciona sabe exactamente dónde ir. El mediador que ya lo entiende y necesita saber qué hacer lo encontrará sin rodeo.

La Parte I establece el flujo de trabajo completo del mediador desde la entrada del caso hasta la entrega del expediente. La Parte II recorre el protocolo completo para cada tipo de análisis simple. La Parte III establece el protocolo del análisis integrado con las tres series sobre el mismo grafo. La Parte IV contiene la demostración formal del Teorema de la Responsabilidad Causal Proporcional y sus corolarios.

El Apéndice A contiene el protocolo de calibración empírica del sistema desde programas de intervención longitudinal. El Apéndice B contiene la tabla de equivalencias extendida por dominio para los nueve conceptos del glosario de esta introducción.

Si el lector necesita que este volumen le explique qué es R* o por qué se usa el eigenvector, ese lector debe leer el Volumen I primero. Si el lector sabe qué es R* y necesita saber cómo calcularlo paso a paso con un caso delante, este volumen fue escrito para él.

La prueba de audiencia del Volumen II

Notas a la introducción

1  La invarianza al dominio del operador causal es demostrada en La transformación formal (Cap. 1.2) y presupuesta en todos los capítulos del Volumen I. Lo que esta introducción agrega no es la demostración sino el protocolo de traducción que hace esa invarianza operativa en la práctica del mediador.

2  Los setenta y ocho capítulos de la Taxonomía General de Aplicaciones desarrollan cada dominio con sus firmas documentales específicas, sus

Metrología Causal · Vol. II

rutas hacia S, y sus estándares de evidencia propios. Esta introducción no reemplaza esos capítulos: establece el lenguaje común que los hace comparables entre sí.

3  La incorporación de los tipos 4 (Prevención) y 5 (Seguimiento) responde a evidencia acumulada en el Programa ECO (Apéndice A) y en las aplicaciones de la Taxonomía en dominios de política pública y acompañamiento clínico. La clasificación original del documento editorial contemplaba solo los tres tipos asociados a las tres series. La evidencia de campo demostró que esa clasificación era incompleta.

4  El glosario de este volumen complementa el glosario del Volumen I. Donde el Volumen I define los términos en su nivel ontológico y matemático, este volumen los define en su nivel operativo y disciplinar. Los dos glosarios son complementarios, no redundantes.

Metrología Causal · Vol. II

PARTE I · El flujo de trabajo del mediador

### Capítulo I·1

### Cómo entra un caso al sistema

Los cinco tipos de pregunta causal y qué serie activan

### I.  El primer acto del mediador

El mediador no comienza el análisis construyendo el grafo. Comienza con una pregunta anterior al grafo: ¿qué necesita poder decir el destinatario cuando este análisis termine? Esa pregunta no es retórica. Es el dato que determina qué instrumento del sistema se activa, bajo qué estándar de evidencia opera, y qué documentos el expediente entrega. Un análisis bien construido sobre la pregunta equivocada produce resultados técnicamente correctos que el destinatario no puede usar.

El primer acto del mediador es, por tanto, la escucha. No la escucha del relato del caso —eso vendrá después— sino la escucha de la necesidad del destinatario. La pregunta que el mediador hace antes de abrir el expediente es invariante al dominio: ¿qué tiene que ser verdad al final para que este análisis le sirva? La respuesta a esa pregunta identifica el tipo de pregunta causal que el caso plantea. El tipo de pregunta determina todo lo demás.

Metrología Causal · Vol. II

### II.  Los cinco tipos de pregunta y su identificación

Existen exactamente cinco tipos de pregunta causal que aparecen en todos los dominios. Cada tipo tiene una pregunta de umbral —la frase que el mediador escucha del destinatario— y un producto de salida distinto. Identificar el tipo no requiere conocer el expediente: requiere escuchar con precisión lo que el destinatario formula.

Tipo La frase que el mediador escucha

Lo que el destinatario necesita

1 · Diagnóstico

"Necesito saber quién causó esto y en qué medida"

Distribución de R* con Declaración de robustez. El análisis describe la estructura causal del resultado específico

2 · Compliance

"Necesito saber si el diseño operó como fue declarado"

IIC del nodo de diseño + ajuste debitor. El análisis evalúa la congruencia entre el campo declarado y el observable

3 · Imputación

"Necesito sostener esta atribución ante impugnación"

Declaración de nivel A, B, C, o D con reporte de sensibilidad. El análisis resiste el escrutinio adversarial

4 · Prevención

"Necesito saber cómo evitar que esto se repita"

Mapa de nodos críticos + hipótesis de rediseño. El análisis orienta intervenciones estructurales futuras

5 · Seguimiento

"Necesito saber si la posición causal está cambiando"

Curva longitudinal de R* y α. El análisis registra la evolución del grafo a lo largo del tiempo

Metrología Causal · Vol. II

El tipo de pregunta no siempre se formula con esa claridad. El destinatario puede decir simplemente: "Quiero saber qué pasó". Eso puede ser un Tipo 1 o un Tipo 3 dependiendo de para qué lo quiere saber. La pregunta de seguimiento del mediador —"¿qué tiene que poder decir usted con este análisis en la mano?"— resuelve la ambigüedad en la totalidad de los casos.

### III.  La tabla de decisión: tipo de pregunta → serie

Cada tipo activa una serie del Método Prometeo o una combinación de series. La selección no es discrecional: está determinada por la estructura de la pregunta. El mediador que activa la serie equivocada produce un análisis formalmente impecable pero materialmente incorrecto: el cálculo cierra, los números son internamente coherentes, el expediente tiene todos sus documentos — pero el instrumento no era el que el destinatario necesitaba. Esa es precisamente su peligrosidad: un error de cálculo es visible porque algo no cuadra; un error de serie no produce ninguna señal interna de fallo.

Tipo Serie principal

Serie adicional

Por qué esta combinación

— La Serie I produce la distribución R* que responde directamente quién y en qué proporción

1 · Diagnóstico

I — Contabilidad Ontológica

2 · Compliance

II — Compliance Causal

Siempre precedida de I

Sin R* base de Serie I, el IIC no tiene denominador. Serie II ajusta los pesos; Serie I los establece

3 · Imputación

III — Imputación Causal

Siempre precedida de I

El hipercubo de parámetros de Serie III requiere el vector R* de

Metrología Causal · Vol. II

Tipo Serie principal

Serie adicional

Por qué esta combinación

Serie I como punto de referencia

— Prevención requiere tanto el mapa causal (I) como el diagnóstico de congruencia del diseño (II)

4 · Prevención

I + II combinadas

— El mismo protocolo de Serie I aplicado en t□, t□... t□. La curva es el producto, no un punto

5 · Seguimiento

I longitudinal (repetida)

Una regla absoluta: la Serie II y la Serie III nunca se aplican sin Serie I previa. La Serie II ajusta los pesos del grafo — para ajustar, primero hay que tener pesos de referencia. La Serie III construye el hipercubo sobre el vector R* — para construir el hipercubo, primero hay que tener ese vector. El mediador que aplica II o III sin I está construyendo sobre aire.

### IV.  Los casos compuestos: cuando el destinatario necesita más de un tipo

El destinatario puede necesitar más de un tipo de respuesta sobre el mismo caso. El abogado que necesita explicar quién causó el daño ante el juez (Tipo 3) y al mismo tiempo orientar al cliente sobre cómo rediseñar el proceso (Tipo 4) necesita I + II + III — el análisis integrado completo. El médico que necesita documentar la contribución causal de cada factor (Tipo 1) y verificar si el protocolo se siguió (Tipo 2) necesita I + II.

### La regla de los casos compuestos es simple: se activan todas las series que corresponden a todos los tipos identificados, en el

Metrología Causal · Vol. II

orden que la Parte III de este volumen establece. Nunca se reduce la demanda del destinatario para simplificar el análisis: si el destinatario necesita I + II + III, el mediador produce I + II + III.

Combinaciones más frecuentes en la práctica

Tipos 1 + 3 (Diagnóstico + Imputación) → Series I + III · La combinación más frecuente en contextos jurídicos adversariales. El diagnóstico establece la distribución; la imputación la blinda ante impugnación.

Tipos 1 + 2 (Diagnóstico + Compliance) → Series I + II · La combinación más frecuente en auditoría institucional y salud pública. El diagnóstico identifica los nodos críticos; el compliance evalúa el diseño que los produjo.

Tipos 1 + 2 + 3 (análisis completo) → Series I + II + III · La combinación más exigente. Reservada para casos donde el análisis debe resistir tanto el escrutinio regulatorio como el adversarial, y donde el diseño institucional es parte central del resultado.

### V.  Producto de salida: la hoja de ruta inicial

Al terminar este capítulo, el mediador tiene un dato y solo uno: qué serie o series se activan en este caso. Ese dato es el producto de salida del Capítulo I·1. No es un análisis, no es un grafo, no es un cálculo. Es una decisión de arquitectura que gobierna todo el trabajo que sigue.

Producto de salida · Capítulo I·1

Decisión documentada de serie(s) a aplicar: Tipo(s) de pregunta identificado(s) → Serie(s) seleccionada(s) → Orden

Metrología Causal · Vol. II

### de producción. Esta decisión queda registrada en el encabezado del expediente y no se modifica sin revisión explícita del tipo de pregunta con el destinatario.

Notas al Capítulo I·1

1  La pregunta de umbral —"¿qué tiene que poder decir usted con este análisis en la mano?"— es el instrumento de elicitación más eficiente disponible para el mediador. El destinatario que no puede responderla no ha articulado aún su necesidad real. El mediador que comienza sin esa respuesta trabaja sin brújula.

2  Los cinco tipos de pregunta corresponden a las cinco posiciones desde las que un destinatario puede relacionarse con un resultado: quien lo padece (Diagnóstico), quien diseñó el sistema que lo produjo (Compliance), quien debe atribuirlo formalmente (Imputación), quien debe evitarlo en el futuro (Prevención), y quien lo acompaña en su evolución (Seguimiento). La clasificación no es exhaustiva en sentido lógico absoluto, pero sí cubre la totalidad de los casos que la práctica de catorce dominios ha producido.

3  La restricción de que Series II y III nunca se aplican sin Serie I no es una convención procedimental. Es una consecuencia matemática: IIC requiere el vector R* como denominador [Vol.I · Cap. V·3], y el hipercubo de Serie III requiere el vector R* como punto central [Vol.I · Cap. VI·8]. Sin R*, ninguna de las dos tiene objeto matemático.

Metrología Causal · Vol. II

PARTE I · El flujo de trabajo del mediador

### Capítulo I·2

### El mapa completo del proceso

De ECO al expediente: seis estaciones, un producto en cada una

### I.  El proceso como cadena de productos

El análisis causal no es un evento sino una cadena. Cada estación del proceso recibe el producto de la estación anterior y entrega un producto nuevo. El mediador que sabe exactamente qué produce en cada estación sabe cuándo terminó cada paso — y sabe, también, qué pasa si una estación falla: qué producto queda sin insumo y qué parte del expediente resulta comprometida.

El mapa que este capítulo establece tiene seis estaciones. No todas se activan en todos los casos: la Estación ECO solo aplica cuando hay un ego humano a localizar; la Estación HISTOS solo aplica cuando el caso tiene componente de acompañamiento. Pero el orden entre las estaciones que se activan es invariante: ninguna puede producir su producto sin el insumo de la anterior.

### II.  Estación 1 · ECO — Localización del ego

Metrología Causal · Vol. II

La Entrevista Clínica Ontológica es el primer instrumento que opera cuando el caso tiene un ego humano como nodo relevante. Su función no es clínica en el sentido de diagnóstico de salud mental: es metrológica. ECO produce la localización del ego en el campo de posibilidades — qué Hijo domina su voluntad, con qué nivel de evidencia, con qué consistencia entre la autopercepción del sujeto y la conducta observable.

El producto de la Estación ECO es la DI-ECO: la Declaración de Identidad de la Entrevista Clínica Ontológica. La DI-ECO contiene el vector P(Hijos) con sus niveles EP, el código de eje del SDO, y la descripción del contexto que alimentará el Bloque II del grafo. Todo lo que la DI-ECO no captura —el grafo del campo, los nodos institucionales, los nodos normativos— es insumo de las estaciones siguientes.

Estación ECO → Producto

Entrada: el ego a localizar (sujeto de la entrevista o caso documental).

Operación: administración de los seis módulos del Bloque I + preguntas contextuales del Bloque II.

Producto: DI-ECO completa → P(Hijos) con niveles EP + código de eje SDO + descripción de contexto.

Condición de completitud: todos los módulos administrados sin condiciones de invalidación [ECO · Cap. II·V]. Si hay invalidación parcial, documentar y aplicar protocolo de datos incompletos [Vol.I · Cap. IV·4].

### III.  Estación 2 · SDO — Posición estructural del ego

El Sistema de Diagnóstico Ontológico recibe la DI-ECO y produce la lectura de los cinco ejes del ego. La diferencia entre ECO y SDO no es de escala sino de perspectiva: ECO observa

Metrología Causal · Vol. II

desde el diálogo; SDO lee desde la estructura. El mismo ego puede producir una DI-ECO con señales mixtas que el SDO resuelve al leer la configuración de los cinco ejes en conjunto.

El producto del SDO es el código de eje: una secuencia de cinco dígitos que describe la posición estructural del ego con suficiente precisión para que el Capítulo I·4 asigne el rango de S correcto. El código de eje es también el punto de entrada de HISTOS si el caso tiene componente de acompañamiento — el Protocolo Histos parte del código SDO como diagnóstico de situación inicial.

### IV.  Estación 3 · Grafo G = (N, E, W)

La construcción del grafo es la estación central del proceso. Recibe como insumo la DI-ECO (para los nodos humanos), el SDO (para la posición de S de esos nodos), y el expediente documental del caso (para todos los nodos, incluyendo los institucionales, normativos, y algorítmicos que ECO y SDO no cubren).

El grafo tiene tres componentes que el mediador construye en secuencia. Primero: el conjunto de nodos N — todos los actores con capacidad causal sobre el resultado D, incluyendo los que no aparecen en la evidencia disponible pero cuya posición estructural los hace necesarios. Segundo: el conjunto de aristas E con su dirección — quién influye sobre quién. Tercero: la matriz de pesos W — la intensidad de cada influencia expresada como rango [a_ij, b_ij] calibrado según el nivel de evidencia E0–E8.

El producto de la Estación Grafo es la hoja de calibración completa: una tabla con todos los nodos, todas las aristas, todos los rangos de peso, todos los niveles de evidencia, y los valores de S y α asignados a cada nodo. La hoja de calibración es el insumo completo de la Estación Cálculo.

Metrología Causal · Vol. II

Estación Grafo → Producto

Entrada: DI-ECO + código SDO + expediente documental.

Operación: identificación de nodos → construcción de aristas → asignación de rangos [a_ij, b_ij] según E0–E8 → asignación de S y α.

Producto: Hoja de Calibración completa [plantilla Vol.II · Sec. 4.1].

Condición de completitud: todos los nodos con capacidad causal identificados — incluyendo los no documentados cuya posición estructural los hace necesarios. Un grafo incompleto produce R* incorrecto con independencia de la precisión del cálculo.

### V.  Estación 4 · Cálculo

La Estación Cálculo recibe la hoja de calibración y produce los parámetros del expediente. No requiere decisión sobre qué calcular: esa decisión fue tomada en el Capítulo I·1 (qué serie), en el I·4 (S), en el I·5 (α), y en el I·6 (eigenvector o Shapley). El cálculo ejecuta.

Para la Serie I: el método de potencias sobre la matriz W de midpoints produce el vector R*. Con R* y S se calcula R*_neta. Con R* y α se calcula Δ. Para la Serie II: el IIC del nodo de diseño ajusta los pesos de sus aristas; el cálculo se repite sobre W ajustada. Para la Serie III: el hipercubo de parámetros se construye sobre los rangos [a_ij, b_ij] y el ranking σ(w) se calcula en cada punto del hipercubo. El nivel de la Declaración (A, B, C, D) emerge del análisis de estabilidad del ranking.

### VI.  Estaciones 5 y 6 · Expediente y HISTOS

Metrología Causal · Vol. II

El expediente recibe los parámetros del cálculo y los organiza en los cuatro documentos que el análisis entrega: la hoja de calibración (ya producida en la Estación 3), el vector R* (con sus derivados R*_neta, Δ, e IIC según la serie), el reporte de sensibilidad (solo para Serie III), y la Declaración. Las plantillas de estos documentos están en la Sección 4 de este volumen.

HISTOS recibe el expediente completo y produce el plan de acompañamiento cuando el caso lo requiere. El Protocolo Histos parte del Δ como medida de la brecha que el acompañamiento debe trabajar y del código SDO como diagnóstico de situación. HISTOS es la estación de cierre del proceso en los casos con componente de acompañamiento clínico u ontológico.

Producto de salida · Capítulo I·2

Mapa de ruta del caso: qué estaciones se activan, en qué orden, qué produce cada una, y cuáles son las condiciones de completitud que habilitan el paso a la siguiente. El mapa de ruta queda registrado en el encabezado del expediente junto a la decisión de serie del Capítulo I·1.

Notas al Capítulo I·2

Metrología Causal · Vol. II

tiene evidencia de él debe incluirlo con nivel de evidencia E0 y documentar la ausencia.

3  HISTOS no es una estación obligatoria. Es el protocolo de cierre cuando el análisis tiene consecuencias de acompañamiento para el ego localizado. En contextos puramente forenses o de auditoría, el proceso termina con la entrega del expediente.

Metrología Causal · Vol. II

PARTE I · El flujo de trabajo del mediador

### Capítulo I·3

### Cómo la DI-ECO alimenta el grafo

De la localización clínica a los parámetros de la hoja de calibración

### I.  Lo que la DI-ECO produce y lo que el grafo necesita

La DI-ECO y la hoja de calibración del grafo parecen documentos de mundos diferentes. La DI-ECO habla de Hijos de Afrodita, de niveles EP, de la distinción entre φ□ y φ□. La hoja de calibración habla de nodos, aristas, rangos de peso, y niveles de evidencia E0–E8. La proposición central de este capítulo es que esa diferencia es vocabulario, no contenido: cada elemento de la DI-ECO tiene un correlato exacto en la hoja de calibración, y la conversión es directa.

El grafo necesita cuatro tipos de información para cada nodo humano: quién es el nodo (su identidad como actor), cuánto pesa su influencia sobre el resultado (el rango de su arista hacia el sumidero), cuánto de esa influencia es idiosincrática del ego vs. del campo (S), y cuánto de su responsabilidad ha integrado como propia (α). La DI-ECO produce, en ese mismo orden: el perfil del sujeto, la intensidad de φ□ (Hijo dominante), la posición de v_t en relación al campo (→ S), y la actividad de ₂ φ (→ α).

Metrología Causal · Vol. II

### II.  Del Bloque I al grafo: P(Hijos) y EP como fuentes de S y v_t

El Bloque I de la DI-ECO administra seis módulos, uno por Hijo. Cada módulo produce un código H (H-3, H-2, H-1, o no determinado) y un nivel de evidencia EP (EP-0 a EP-5). El código H indica la posición del sujeto respecto a ese Hijo: H-3 es localización clara, H-2 es localización probable, H-1 es señal presente pero no dominante, indeterminado es evidencia insuficiente.

Del Bloque I emergen dos parámetros directos para el grafo. El primero es el Hijo dominante: el Hijo con código H-3 más alto EP determina el rango de S que el Capítulo I·4 formaliza. Si hay más de un H-3 o si el máximo es H-2, se aplica el protocolo de evidencia contradictoria de ese mismo capítulo. El segundo parámetro es la calidad de v_t: la consistencia entre los códigos H del Hijo dominante a lo largo de los módulos del Bloque I es el proxy observable del grado de estructuración de v_t en el momento del acto analizado.

Lectura para el grafo

Código H del módulo

EP del módulo

H-3 EP-5 o EP-4

Localización confirmada. S desde el rango central del Hijo. v_t estructurado.

H-3 EP-3 Localización probable. S desde el rango completo del Hijo. v_t estructurado con moderada certeza.

H-3 EP-2 o EP-1

Localización débil. Ampliar rango de S en 0.10 hacia ambos lados. Documentar incertidumbre.

Metrología Causal · Vol. II

Lectura para el grafo

Código H del módulo

EP del módulo

H-2 EP-4 o EP-5

Señal probable. Usar rango del Hijo con margen inferior. Verificar módulos de Hijos adyacentes.

H-1 cualquier EP

Señal presente pero no dominante. Hijo no es el dominante. Datos para análisis de campo secundario.

? — Evidencia insuficiente. No asignar S desde este módulo. Activar Ruta B para S [Cap. I·5].

### III.  Del Bloque II al grafo: el contexto como fuente de aristas

El Bloque II de la DI-ECO recoge la descripción del campo que el sujeto habita: las personas que influyen en sus decisiones, las instituciones que estructuran su entorno, los eventos que determinaron su historia acumulada. Este bloque no produce parámetros para el nodo del ego — produce los candidatos a nodos adicionales del grafo y las aristas entre ellos.

Cada persona mencionada en el Bloque II con influencia recurrente sobre las decisiones del sujeto es un candidato a nodo. Cada institución cuyo protocolo el sujeto sigue o viola es un candidato a nodo de diseño. Cada evento histórico que el sujeto identifica como determinante es evidencia de una arista de alta intensidad entre ese evento y el nodo del ego. El mediador no convierte automáticamente toda mención del Bloque II en un nodo: convierte en nodo todo actor cuya presencia o ausencia habría cambiado el resultado analizado.

Metrología Causal · Vol. II

### IV.  La hoja de conversión DI-ECO → parámetros del grafo

La hoja de conversión es el documento operativo que cierra este capítulo. El mediador la completa con los datos de la DI-ECO antes de construir la hoja de calibración del grafo. Una vez completada, todos los parámetros del nodo del ego quedan definidos con suficiente precisión para comenzar la construcción del grafo.

Campo de la DI-ECO

Operación de conversión

Parámetro en la hoja de calibración

Hijo dominante (código H-3 + EP más alto)

Tabla de conversión P(Hijos) → rango de S [Cap. I·4]

S del nodo del ego: rango [a_S, b_S]

Nivel EP del Hijo dominante

Modulación del rango: EP-5 → midpoint, EP-4 → ±0.05, EP-3 → rango completo

Amplitud del rango de S en la hoja

Actividad de φ□ observada en el módulo dominante

Tabla de conversión φ□ → α [Cap. I·5, Ruta A]

α del nodo del ego: estimado inicial

Consistencia de H-3 en los módulos del Bloque I

Alta consistencia → v_t estructurado. Baja consistencia → v_t difuso

Anotación de calidad de v_t en la hoja

Actores del Bloque II con influencia recurrente

Cada actor → nodo candidato con arista hacia el ego

Nodos adicionales del grafo con arista preliminar

Metrología Causal · Vol. II

Campo de la DI-ECO

Operación de conversión

Parámetro en la hoja de calibración

Instituciones del Bloque II

Cada institución relevante → nodo de diseño candidato

Nodos de diseño con arista de campo hacia el ego

### Producto de salida · Capítulo I·3

Hoja de conversión DI-ECO → parámetros del grafo: S y α del nodo del ego con sus rangos y niveles de certeza, calidad de v_t, y lista de nodos candidatos desde el Bloque II. Esta hoja es el insumo directo de la construcción del grafo en la Estación 3.

Notas al Capítulo I·3

1  El Bloque II de la DI-ECO no es una entrevista de historia de vida. Es una elicitación estructurada del campo del ego orientada a identificar nodos causalmente relevantes. El mediador que deja que el Bloque II se convierta en una narrativa sin estructura obtiene material clínico valioso, pero no produce los datos que el grafo necesita.

2  La actividad de φ□ como proxy de α requiere una aclaración importante: φ□ mide la integración del acto en I(t), mientras α mide la asunción verificable mediante conducta observable. Son el mismo fenómeno desde dos perspectivas [La transformación formal · Cap. 1.2]. En contextos forenses donde la conducta es el único dato disponible, la Ruta B [Cap. I·5] reemplaza a la Ruta A. En contextos clínicos donde φ□ es directamente observable, la Ruta A es más precisa.

Metrología Causal · Vol. II

PARTE I · El flujo de trabajo del mediador

### Capítulo I·4

### Cómo el Hijo dominante determina S

Tabla de conversión P(Hijos) → rango de S para cada nodo del grafo

### I.  Por qué el Hijo dominante determina S

S mide cuánto del acto del nodo es atribuible al campo y cuánto al ego específico. La posición de la voluntad en el momento del acto —qué Hijo domina v_t— es exactamente lo que determina esa proporción. Cuando Fobos domina φ□, el ego actúa desde el miedo al campo: cualquier otro ego con el mismo nivel de amenaza habría actuado igual. La sustituibilidad es alta. Cuando Harmonía domina φ□, el ego actúa desde la integración plena de su historia acumulada: nadie más, con ninguna otra historia, habría actuado igual. La sustituibilidad es mínima.

Esta no es una analogía entre el Hijo y S. Es la misma dimensión del mismo fenómeno descrita desde dos perspectivas: el Hijo la describe desde adentro del ego que opera φ□; S la describe desde afuera del campo que observa el acto [La transformación formal · Cap. 1.2]. La conversión entre los dos vocabularios es, por tanto, una traducción entre perspectivas, no una correlación entre variables independientes.

Metrología Causal · Vol. II

### II.  La tabla de conversión P(Hijos) → rango de S

La tabla que sigue es el instrumento central de este capítulo. El mediador identifica el Hijo dominante del nodo (desde la DI-ECO para nodos humanos, desde la evidencia documental para nodos institucionales) y lee directamente el rango de S que le corresponde. El midpoint del rango es el valor de cálculo cuando la evidencia es EP-5 o EP-4. Los extremos del rango se usan cuando la evidencia es más débil.

Midpoint Qué significa este S para el caso

Hijo dominante

Rango de S

0.70 – 1.00 0.85 Alta sustituibilidad. El acto fue respuesta predecible a la amenaza del campo. Cualquier ego en esa posición habría actuado igual ante el mismo miedo. El campo explica la mayor parte del resultado.

Fobos (miedo al campo)

0.60 – 0.85 0.73 Sustituibilidad alta-media. La angustia difusa ante el campo produce respuestas ampliamente compartibles. Hay más varianza que en Fobos pero el campo sigue siendo dominante.

Deimos (angustia difusa)

0.40 – 0.70 0.55 Sustituibilidad media. El acto fue condicional a la respuesta del otro. Depende de quién es ese otro en este caso específico. Requiere análisis de la arista entre el ego y su referente de reciprocidad.

Anteros (reciprocidad)

### 0.20 – 0.50 0.35 Sustituibilidad baja-media. El acto está orientado a algo que

Potós (anhelo de lo ausente)

Metrología Causal · Vol. II

Midpoint Qué significa este S para el caso

Hijo dominante

Rango de S

no está presente en el campo. El objeto del anhelo es particular del ego. La idiosincrasia crece conforme el objeto es más específico.

0.10 – 0.35 0.23 Sustituibilidad baja. El acto emerge del deseo específico del ego en el momento del colapso. Difícilmente otro ego en la misma posición estructural habría tenido el mismo deseo con la misma intensidad.

Eros (deseo presente)

0.00 – 0.25 0.13 Sustituibilidad mínima. El acto emerge de la integración plena del ego. Es el acto más idiosincrático posible: es el resultado de toda la historia acumulada de ese ego específico, irreplicable.

Harmonía (integración)

### III.  El nivel EP como modulador del rango

El rango de cada Hijo tiene una amplitud de 0.30. El nivel de evidencia EP determina qué parte del rango se usa en el cálculo. Esta modulación no es arbitraria: refleja que la localización del ego en un Hijo con alta certeza de evidencia permite una asignación más precisa de S que una localización con evidencia débil.

Metrología Causal · Vol. II

Nivel EP Cómo usar el rango de S

EP-5 — Evidencia múltiple convergente

Usar el midpoint del rango. La localización es suficientemente precisa para un valor puntual.

EP-4 — Evidencia directa sólida

Usar el midpoint ± 0.05. El rango efectivo se reduce a 0.10 centrado en el midpoint.

EP-3 — Evidencia directa moderada

Usar el rango completo del Hijo. El cálculo se realiza con el midpoint; la amplitud del rango alimenta el análisis de sensibilidad.

EP-2 — Evidencia indirecta

Ampliar el rango del Hijo en ±0.10. El rango efectivo pasa de 0.30 a 0.50. Documentar la amplitud en la hoja de calibración.

EP-1 — Evidencia mínima

No asignar S desde este módulo. Activar Ruta B de calibración de S desde la evidencia documental [Cap. I·5].

EP-0 — Sin evidencia

S no asignable desde ECO. El nodo requiere fuente alternativa de S o tratamiento como nodo de evidencia incompleta [Vol.I · Cap. IV·4].

### IV.  El protocolo de evidencia contradictoria

El protocolo de evidencia contradictoria se activa cuando el Bloque I de la DI-ECO produce señales de dos o más Hijos con codificación H-3 o cuando la señal más fuerte es H-2 en múltiples módulos. En esos casos, no existe un Hijo claramente dominante y la tabla del apartado anterior no produce un rango de S sin ambigüedad.

### El protocolo tiene tres pasos. Primero: verificar si la contradicción es real o es un artefacto de la administración. Las

Metrología Causal · Vol. II

condiciones de invalidación de la ECO —sesgo de imagen, resistencia activa, fatiga— pueden producir señales mixtas que no reflejan la posición real del ego. Si hay condición de invalidación, repetir los módulos afectados antes de proceder.

Segundo: si la contradicción es real, identificar en qué contexto se activa cada señal. Un ego que muestra Fobos en el módulo de relaciones de autoridad y Eros en el módulo de relaciones entre pares no tiene evidencia contradictoria sino evidencia de que el Hijo dominante depende del tipo de relación. El caso analizado determina cuál de los dos contextos es el relevante.

Tercero: si la contradicción persiste sin resolución contextual, usar el rango más amplio posible — el que cubre el espectro entre los dos Hijos con mayor señal — y documentar la incertidumbre con nivel EP-2 en la hoja de calibración. El análisis de sensibilidad de la Serie III absorberá esa incertidumbre en el hipercubo de parámetros.

Producto de salida · Capítulo I·4

Valor de S para cada nodo del grafo: rango [a_S, b_S] derivado del Hijo dominante y modulado por el nivel EP, con el midpoint como valor de cálculo y la amplitud documentada en la hoja de calibración. Para nodos sin ECO disponible: S desde Ruta B [Cap. I·5, criterios universales de S].

Notas al Capítulo I·4

Metrología Causal · Vol. II

Programa ECO [Vol.II · Apéndice A] permitirán, con suficiente muestra, verificar si los rangos teóricos corresponden a los rangos observados en poblaciones específicas.

2  La distinción entre Fobos y Deimos en términos de S merece una nota. Fobos opera desde el miedo a una amenaza concreta y específica del campo: la amenaza está en el objeto del miedo. Deimos opera desde la angustia difusa ante el campo en general: la amenaza no tiene objeto preciso. Esta distinción reduce ligeramente S en Deimos respecto a Fobos porque la angustia difusa tiene algo más de idiosincrasia en cómo se procesa — dos egos pueden tener la misma amenaza concreta (→ Fobos, S muy alto) pero la angustia ante el mismo campo general se procesa con más variación individual (→ Deimos, S algo más bajo).

Metrología Causal · Vol. II

PARTE I · El flujo de trabajo del mediador

### Capítulo I·5

### Cómo se infiere α desde la localización y la

### evidencia

Ruta A clínica, Ruta B forense, Ruta C longitudinal: tres fuentes de

un mismo parámetro

### I.  Los tres orígenes de α y su jerarquía

α mide la fracción de R* que el nodo integró como propia mediante acciones verificables. Esta definición abre tres posibilidades de acceso al dato: desde la observación directa de φ□ en la entrevista clínica (Ruta A), desde el análisis de la conducta verificable en el expediente documental (Ruta B), y desde la observación acumulada de patrones de atribución a lo largo del tiempo (Ruta C). Las tres rutas miden el mismo parámetro desde distintas perspectivas.

La jerarquía entre rutas no es de precisión sino de disponibilidad. La Ruta A, cuando es posible, produce la estimación más directa porque observa φ□ en acción. La Ruta B es la ruta estándar en contextos forenses donde el ego no es accesible para entrevista. La Ruta C es la más robusta en términos de validez longitudinal, pero requiere observación acumulada a lo largo del tiempo. Las tres pueden combinarse: cuando dos rutas

Metrología Causal · Vol. II

producen estimados convergentes, la certeza del valor de α aumenta. Cuando divergen, el protocolo de resolución de este capítulo aplica.

### II.  Ruta A — Clínica: α desde la DI-ECO

La Ruta A infiere α desde la actividad de φ□ observable en la sesión de ECO. φ□ es la función de retorno evaluativo del ego sobre sus propios actos — el mecanismo por el que el acto producido por φ□ es o no integrado en I(t). La ECO accede a φ□ directamente a través de la calidad del reconocimiento del sujeto de sus propios actos durante la entrevista.

El mediador no califica la actividad de φ□ con una escala cuantitativa durante la entrevista. La calificación emerge de cuatro observaciones que se realizan de forma natural en el módulo dominante: si el sujeto reconoce actos propios sin ser preguntado directamente, si conecta sus actos con sus consecuencias, si puede nombrar qué habría hecho diferente, y si mantiene esa posición cuando el facilitador introduce una perspectiva alternativa.

Descripción del patrón

Observación de φ□ en ECO

α estimado (Ruta A)

### 0.70 – 1.00 El ego integra sus colapsos en I(t) con mínima resistencia. Alta asunción.

φ□ activo espontáneo: el sujeto nombra actos propios con consecuencias sin facilitación directa

### 0.40 – 0.70 El ego puede integrar, pero requiere el señalamiento del campo para hacerlo. Asunción media.

φ□ activo con facilitación: el sujeto reconoce con preguntas directas pero no evade

Metrología Causal · Vol. II

Descripción del patrón

Observación de φ□ en ECO

α estimado (Ruta A)

### 0.20 – 0.45 El ego tiene capacidad de φ₂, pero la ejerce selectivamente. El contexto y la audiencia afectan el resultado.

φ□ parcial: el sujeto oscila entre el reconocimiento y la atribución externa; inconsistente

### 0.00 – 0.25 El ego no integra sus colapsos en I(t). Δ alto. La asunción no está bloqueada — está ausente.

φ□ ausente: el sujeto atribuye consistentemente los actos al campo, al otro, o al azar

### III.  Ruta B — Forense: α desde la evidencia documental

La Ruta B calcula α desde la evidencia disponible en el expediente del caso, sin acceso directo al ego. Opera sobre los tres criterios universales de asunción establecidos en la Introducción de este volumen: conocimiento, acción, y oportunidad. Cada criterio es verificable con evidencia documental y contribuye de forma independiente al valor de α.

Criterio Pregunta de verificación

Contribución máxima a α

Evidencia que lo acredita

Conocimiento ¿El nodo tenía información suficiente para prever el resultado en el momento del acto?

### 0.33 Informes de riesgo recibidos, reuniones documentadas, comunicaciones sobre el resultado potencial,

Metrología Causal · Vol. II

Criterio Pregunta de verificación

Contribución máxima a α

Evidencia que lo acredita

evaluaciones previas disponibles

Acción ¿El nodo tomó acciones verificables orientadas a modificar o prevenir el resultado?

### 0.33 (gradable) Acciones preventivas, protocolos activados, controles implementados, reportes generados, intervenciones documentadas

Oportunidad ¿El nodo tuvo momentos específicos donde podía haber actuado diferente y no lo hizo?

### 0.33 Reuniones donde el resultado fue advertido, comunicaciones que solicitaban acción, instancias de decisión con alternativa documentada

El criterio de Acción es el único gradable: un nodo que tomó algunas acciones, pero no las completas recibe una fracción de los 0.33 proporcional a la completitud de sus acciones. Los criterios de Conocimiento y Oportunidad son binarios: el nodo tenía la información o no la tenía; el momento existió o no existió. La suma de los tres criterios produce α directamente en el rango [0.00, 1.00].

### IV.  Ruta C — Longitudinal: α desde la observación acumulada

Metrología Causal · Vol. II

La Ruta C produce α desde la observación sistemática del patrón de atribución de un ego a lo largo del tiempo. Es la ruta más robusta en términos de validez porque elimina el sesgo de un momento único de observación: el patrón de diez sesiones es más representativo del α estructural del ego que cualquier observación puntual.

La Ruta C requiere un protocolo de observación longitudinal con registros estructurados. El protocolo estándar para poblaciones de acompañamiento está en el Apéndice A de este volumen. Para otros contextos, el principio es el mismo: se observa la gramática de atribución del ego (¿quién es el sujeto gramatical de sus relatos sobre sus propios actos?) en situaciones repetidas, y se promedian los valores a lo largo del tiempo.

El promedio de α en la Ruta C converge al valor estructural del ego después de un número suficiente de observaciones. El número mínimo de observaciones para una estimación estable varía por población: el Apéndice A proporciona los datos para la población de adolescentes en contexto escolar. Para otras poblaciones, la estabilización se detecta cuando el promedio deja de cambiar significativamente entre observaciones sucesivas.

### V.  Cuándo las rutas divergen: el protocolo de resolución

Cuando dos rutas disponibles producen estimados de α significativamente diferentes — con una brecha mayor a 0.25 — el mediador no promedia. La brecha es información: señala que hay algo que una perspectiva ve y la otra no.

Protocolo de resolución de divergencia entre rutas de α

Ruta A > Ruta B: el ego reconoce en la entrevista más de lo que su conducta documenta. Interpretación más frecuente: Metrología Causal · Vol. II

φ□ está activo, pero no ha producido acción verificable. El ego sabe que el acto es suyo, pero no ha actuado sobre esa conciencia. Δ real puede ser mayor que Δ aparente. Usar el valor más bajo (Ruta B) como estimado conservador y documentar la brecha.

Ruta B > Ruta A: el ego tiene más acciones verificables de asunción que las que reconoce en la entrevista. Interpretación más frecuente: el ego actuó correctamente por protocolo, pero no integró esos actos como propios. La conducta supera la conciencia. Usar el promedio de ambas rutas y documentar la interpretación.

Ambas rutas divergen de Ruta C: el patrón longitudinal es diferente de la conducta documentada o del reconocimiento en entrevista. Esto señala que α varía significativamente con el contexto o el tiempo. No usar un único valor — documentar el rango y comunicar la variabilidad al destinatario.

Producto de salida · Capítulo I·5

Valor de α para cada nodo del grafo: estimado desde Ruta A, B, o C (con fuente documentada), con el rango de certeza y las notas de divergencia cuando aplican. Este valor queda registrado en la columna α de la hoja de calibración, junto a la fuente de evidencia que lo sostiene.

Notas al Capítulo I·5

Metrología Causal · Vol. II

2  El criterio de Oportunidad merece una aclaración sobre su relación con S. Es posible que un ego haya tenido oportunidades de actuar diferente (→ Oportunidad presente, contribuye a α) pero que cualquier otro ego en esa posición también las hubiera ignorado (→ S alto). En ese caso, el ego tiene α bajo, pero también S alto: la responsabilidad neta (R*_neta = R* × (1-S)) es pequeña, aunque Δ sea grande. El sistema captura ambas dimensiones independientemente: S describe el acto en relación al campo; α describe la integración del acto por el ego. Son dimensiones ortogonales.

Metrología Causal · Vol. II

PARTE I · El flujo de trabajo del mediador

### Capítulo I·6

### El protocolo de decisión entre eigenvector y

### Shapley

Cuándo cada método aplica y cómo elegir

### I.  El problema que este capítulo resuelve

El sistema tiene dos métodos de cálculo de responsabilidad causal: el eigenvector principal de W y el valor de Shapley. El Volumen I establece cuándo cada uno es matemáticamente válido [Vol.I · Cap. VII·3]. Este capítulo establece cómo el mediador identifica, desde la estructura del grafo que tiene delante, cuál de los dos métodos aplica a su caso.

La confusión entre los dos métodos no es un error de cálculo: es un error de tipo. Aplicar el eigenvector cuando la condición que lo justifica no se cumple produce R* que mide centralidad estructural pero no responsabilidad causal. Aplicar Shapley cuando el eigenvector es el método correcto produce un cálculo más costoso computacionalmente que produce el mismo resultado. El primero error es sustantivo; el segundo, ineficiente. Este capítulo previene ambos.

Metrología Causal · Vol. II

### II.  El eigenvector: condición de aplicación

El eigenvector principal de W es el método correcto cuando al menos uno de los nodos del grafo es individualmente condición sine qua non del resultado D. Un nodo i es condición sine qua non de D si, al eliminar i del grafo y todas sus aristas, el resultado D no puede ocurrir en su forma específica a través de los nodos y aristas restantes.

La condición sine qua non individual es una condición estructural del grafo, no una condición empírica. El mediador no la verifica experimentalmente —el evento ya ocurrió. La verifica estructuralmente: ¿existe en G algún camino alternativo de cualquier otro nodo a D que no pase por i, con peso total suficiente para producir D en su forma específica? Si no existe ese camino alternativo, i es condición sine qua non individual.

El eigenvector mide cuánto de D se explica por la posición estructural de cada nodo en el grafo, tomando en cuenta no solo la influencia directa sino la indirecta a través de todos los caminos. Su validez como medida de responsabilidad causal descansa sobre la condición de que al menos un nodo sea condición necesaria individual: sin esa condición, la distribución eigenvectorial no tiene la interpretación causal que R* requiere.

Vol.I · Cap. VII·3

### III.  El valor de Shapley: condición de aplicación

El valor de Shapley es el método correcto cuando ningún nodo del grafo es individualmente condición sine qua non de D. Esto ocurre cuando las contribuciones de los nodos son genuinamente no separables: cada nodo solo produce D en conjunto con otros nodos, y no existe ningún nodo cuya eliminación sola impediría D.

Metrología Causal · Vol. II

El caso Shapley no es infrecuente en la práctica. Es el caso de los sistemas donde el resultado emerge de la intersección de múltiples condiciones necesarias colectivamente pero no individualmente: la falla sistémica que requiere que todos los controles fallen simultáneamente, el resultado social que requiere que múltiples actores mantengan su conducta en paralelo, el colapso organizacional que resulta de la acumulación de decisiones ninguna de las cuales sola lo habría producido.

En el caso Shapley, la distribución de responsabilidad es el valor de Shapley de la función característica v(S) donde S es cualquier coalición de nodos y v(S) es la fracción del resultado D que la coalición S puede producir por sí sola. El valor de Shapley de cada nodo es su contribución marginal promedio sobre todas las coaliciones posibles en las que podría participar.

### IV.  El test de decisión: la prueba de condición sine qua non

El test de decisión se aplica nodo por nodo sobre el grafo construido. Para cada nodo i, el mediador responde la siguiente pregunta estructural: eliminado i del grafo, ¿existe algún conjunto de nodos restantes suficiente para producir D en su forma específica?

El test de condición sine qua non individual · Protocolo

Paso 1: Identificar el nodo candidato i y el resultado específico D (el nodo sumidero Nf).

Paso 2: Eliminar i y todas sus aristas del grafo. Llamar G' al grafo resultante.

Metrología Causal · Vol. II

Paso 3: Verificar si en G' existe al menos un camino desde cualquier nodo fuente a Nf con peso acumulado suficiente para producir D en su forma específica.

Resultado A — No existe ese camino: i es condición sine qua non individual → el eigenvector es el método correcto.

Resultado B — Existe ese camino: i no es condición sine qua non individual → i no funda por sí solo la condición del eigenvector.

Decisión final: si al menos un nodo produce Resultado A → eigenvector. Si todos los nodos producen Resultado B → Shapley.

### V.  Los casos mixtos y la conjetura del operador unificador

Un caso mixto es un grafo donde algunos nodos son condición sine qua non individual y otros no lo son. En ese caso, la teoría del sistema predice que el eigenvector es el método correcto para la distribución global — porque la condición que funda su validez se cumple para al menos un nodo— pero que los nodos que no son individualmente sine qua non tienen una componente de su R* que el eigenvector distribuye de manera diferente a como lo haría Shapley.

El sistema maneja los casos mixtos con el eigenvector como método primario y el Shapley como verificación secundaria para los nodos que no son individualmente sine qua non. Si los dos métodos producen valores similares para esos nodos, el eigenvector se usa como resultado definitivo. Si producen valores significativamente diferentes, se documenta la diferencia y se reporta al destinatario como incertidumbre estructural del análisis.

La conjetura del operador unificador — la demostración formal de que existe un operador que produce el eigenvector en el caso sine qua non y el Shapley en el caso no-sine-qua-non,

Metrología Causal · Vol. II

interpolando entre ellos en casos mixtos — está formulada con precisión en el Capítulo IV·7 de este volumen y en la Axiomatización del Sistema de la Doble Mediación. Es el programa de investigación abierto más importante del paradigma. Los precedentes de la literatura que apuntan en esta dirección (Hu & Shapley 2003, Teng 2016, Aleandri et al. 2025) sugieren que la conjetura es verdadera, pero la demostración completa no existe aún.

### Producto de salida · Capítulo I·6

Decisión de método de cálculo: eigenvector (si al menos un nodo supera el test de condición sine qua non) o Shapley (si ningún nodo la supera), con la documentación del test aplicado. En casos mixtos: eigenvector primario con verificación Shapley sobre los nodos no-sine-qua-non y documentación de la diferencia.

Notas al Capítulo I·6

1  El "peso acumulado suficiente" del Paso 3 del test requiere una aclaración operativa. En términos del grafo, significa que el camino alternativo en G' produce un resultado D' tal que D' = D en su forma específica — no en alguna forma aproximada. Si la eliminación de i produciría un resultado cuantitativamente menor pero cualitativamente idéntico, i no es condición sine qua non: el resultado habría ocurrido de todas formas, solo con menor intensidad. Si la eliminación de i produciría un resultado cualitativamente diferente, i es condición sine qua non.

2  La confusión entre la fórmula I = R* × (1−S) × (1−α) —que circuló en la conversación con modelos de lenguaje externos— y el sistema formal merece una aclaración explícita. Esa fórmula combina dos corolarios del Teorema (R*_neta y Δ) en una sola cantidad que el sistema no define como tal. R*_neta = R* × (1−S) mide la fracción idiosincrática del peso causal. Δ = R* × (1−α) mide el déficit de asunción. Son cantidades independientes con interpretaciones distintas. El producto de las dos es

Metrología Causal · Vol. II

una cantidad sin nombre en el sistema formal porque no tiene interpretación metrológica propia.

Metrología Causal · Vol. II

PARTE I · El flujo de trabajo del mediador

### Capítulo I·7

### Los errores más frecuentes del protocolo

Cómo detectarlos antes de que afecten el resultado

### I.  Por qué los errores del protocolo son más costosos que los del cálculo

Un error de cálculo —un error aritmético, un midpoint mal computado, una suma que no cierra— es detectable y corregible. La suma de los R* no da 1.00: el mediador lo ve, encuentra el error, lo corrige. Los errores del protocolo son de otra naturaleza: producen resultados técnicamente correctos que miden algo diferente de lo que el análisis necesita medir. El R* de un grafo construido sobre los nodos equivocados suma exactamente 1.00. El análisis es impecable. El resultado es incorrecto.

Los errores que este capítulo cataloga son los que la práctica del sistema en catorce dominios ha producido con mayor frecuencia. No son errores de comprensión teórica — el mediador que llegó a este capítulo tiene el dominio teórico requerido. Son errores de ejecución: momentos específicos del protocolo donde la presión del caso, la urgencia del destinatario, o la complejidad del expediente llevan al mediador a tomar un atajo que compromete el resultado.

Metrología Causal · Vol. II

### II.  Errores en la identificación del tipo de pregunta

El error más frecuente y más costoso del protocolo es comenzar a construir el grafo sin haber identificado el tipo de pregunta. El grafo se construye, el cálculo se realiza, el expediente se entrega — y el destinatario dice que eso no era lo que necesitaba. No hay versión más costosa de este error.

El segundo error de identificación es confundir el tipo que el destinatario formula con el tipo que el destinatario necesita. El destinatario que dice "quiero saber qué pasó" puede necesitar Tipo 1, Tipo 3, o Tipo 4 dependiendo de para qué lo quiere saber. La pregunta de seguimiento —"¿qué tiene que poder decir usted con este análisis en la mano?"— no es opcional.

El tercer error es activar una sola serie cuando el caso requiere dos o tres. El análisis simple es más rápido, más barato, y satisface menos al destinatario que llegó con una necesidad compuesta. El mediador que simplifica la demanda para simplificar el trabajo produce un análisis menor que el necesario.

### III.  Errores en la construcción del grafo

Error Síntoma en el resultado

Cómo detectarlo antes del cálculo

Nodo sumidero no específico: D definido como 'el problema' o 'los daños' sin forma específica

R* distribuido entre nodos sin coherencia interpretable. No hay forma de comunicar el resultado.

Verificar que D pueda enunciarse en una sola frase específica con magnitud y forma. 'El fraude de 10M en Q3' es D específico. 'Los problemas del banco' no lo es.

Metrología Causal · Vol. II

Error Síntoma en el resultado

Cómo detectarlo antes del cálculo

Nodos de alto R* excluidos por falta de documentación

R* artificialmente concentrado en nodos documentados. El grafo describe lo que se puede probar, no lo que ocurrió.

Preguntarse: ¿hay algún actor cuya ausencia del grafo habría cambiado el resultado? Si la respuesta es sí, ese actor es un nodo necesario aunque no esté documentado.

Aristas construidas por correlación o precedencia temporal, no por influencia causal

El grafo describe la secuencia de eventos, no la estructura causal. R* mide quién actuó antes, no quién fue condición necesaria.

Para cada arista, verificar: ¿la eliminación del nodo de origen cambia el resultado del nodo de destino? Si la respuesta es no, la arista no es causal.

Grafo no irreducible: hay nodos sin camino al sumidero

El eigenvector no está definido o no converge. El método de potencias no termina.

Verificar antes del cálculo que desde cada nodo existe al menos un camino dirigido al sumidero Nf. Si no existe, el nodo no es causalmente relevante para D y debe eliminarse del grafo.

### IV.  Errores en la calibración de S y α

Error Por qué ocurre Cómo corregirlo

S asignado por intuición, no

El mediador conoce el dominio del caso y cree

Siempre derivar S desde el Hijo dominante con su nivel EP [Cap. I·4]. Si no hay ECO, usar

Metrología Causal · Vol. II

Error Por qué ocurre Cómo corregirlo

desde la tabla P(Hijos)

saber qué tan sustituible fue el nodo sin pasar por el instrumento.

los tres criterios universales de S de la Introducción y documentar la fuente.

α confundido con remordimiento o declaración

El ego muestra culpa intensa o declara alta responsabilidad y el mediador registra α alto.

α requiere conducta verificable, no emoción ni declaración. Verificar los tres criterios de la Ruta B [Cap. I·5] con evidencia documental antes de asignar α alto.

S y α asignados al caso en general, no al acto específico analizado

El mediador describe el perfil general del nodo, no su posición en el acto que produjo D.

S y α son parámetros del nodo en relación a D específico. El mismo nodo puede tener S = 0.20 en un acto y S = 0.80 en otro del mismo caso si las condiciones del campo cambiaron.

α > 1 − S (asunción mayor que la fracción idiosincrática)

El nodo asume más de lo que su idiosincrasia permite. Matemáticamente posible; interpretativamente señala que el ego se hace cargo de responsabilidad sistémica.

No corregir el dato — documentar la condición. Es el caso del 'vanguardista de la asunción' [Vol.I · Cap. IX·4]: el ego que asume antes de que el sistema lo requiera.

### V.  La lista de verificación pre-cálculo

### La lista que sigue se completa antes de iniciar cualquier cálculo. No es opcional: es la condición de validez del análisis. El

Metrología Causal · Vol. II

mediador que encuentra un ítem sin completar no avanza al cálculo: regresa al paso del protocolo donde ese ítem se produce.

Lista de verificación pre-cálculo

☐  Tipo(s) de pregunta identificado(s) con el destinatario → serie(s) seleccionada(s) [Cap. I·1]

☐  Nodo sumidero Nf identificado con resultado D específico en una sola frase

☐  Todos los nodos con capacidad causal identificados, incluyendo los no documentados [Cap. I·2]

☐  Cada arista verificada como relación de influencia causal, no de correlación o precedencia temporal

☐  Cada arista tiene nivel de evidencia E0–E8 asignado y rango [a_ij, b_ij] correspondiente [Vol.I · Cap. VI·2]

☐  S de cada nodo derivado desde la tabla P(Hijos) → rango de S [Cap. I·4] o desde criterios universales con fuente documentada

☐  α de cada nodo derivado desde Ruta A, B, o C [Cap. I·5] con fuente de evidencia documentada

☐  Test de condición sine qua non realizado → método de cálculo seleccionado (eigenvector o Shapley) [Cap. I·6]

☐  Grafo verificado como irreducible: desde cada nodo existe camino al sumidero Nf

☐  Si Serie II: nodo de diseño identificado y protocolos declarados relevantes documentados

☐  Si Serie III: estándar adversarial verificado — solo evidencia E1–E4 en el grafo, rangos estrechos confirmados

Producto de salida · Capítulo I·7

Metrología Causal · Vol. II

Lista de verificación completada y firmada: todos los ítems confirmados. Esta lista queda archivada en el expediente como evidencia de que el protocolo fue completado antes del cálculo. Un ítem sin completar invalida el análisis hasta que sea resuelto.

Notas al Capítulo I·7

1  El ítem sobre nodos no documentados —que el grafo debe incluir todo actor cuya presencia o ausencia habría cambiado el resultado, aunque no esté en el expediente— es el ítem más frecuentemente omitido y el que produce los errores más costosos. La razón es comprensible: el análisis documental crea un sesgo de visibilidad hacia lo que está en el expediente. El mediador que trabaja en un caso largo puede confundir lo que está documentado con lo que ocurrió. El test preventivo es simple: "¿hay algún actor que obviamente importó en este resultado, pero del que no tengo evidencia?" Si la respuesta es sí, ese actor entra al grafo con nivel de evidencia E0 y rango amplio.

2  El ítem sobre la irreducibilidad del grafo tiene una consecuencia técnica que el mediador debe conocer: la irreducibilidad no solo es condición del método de potencias, sino del Teorema de Perron-Frobenius que garantiza la existencia y unicidad del eigenvector positivo [Vol.II · Cap. IV·2]. Un grafo reducible puede tener múltiples eigenvectores y el método de potencias converge al mayor de ellos, que no necesariamente corresponde a la distribución de responsabilidad causal. La verificación de irreducibilidad no es burocrática: es la verificación de que el resultado tiene interpretación metrológica válida.

Metrología Causal · Vol. II

PARTE II · El análisis simple: una sola serie

### Capítulo II·1

### Serie I: Contabilidad Ontológica

El protocolo completo del análisis causal base

### I.  Cuándo aplica la Serie I

La Serie I es el análisis causal base del sistema. Responde la pregunta de Tipo 1 —¿quién fue condición necesaria de este resultado y en qué proporción? — y es el punto de partida obligatorio de toda combinación de series. Ningún análisis del sistema, con independencia del tipo de pregunta que responda, omite la Serie I: sus siete pasos producen el vector R* que todas las series subsiguientes usan como insumo.

La Serie I aplica en solitario cuando el destinatario necesita únicamente el diagnóstico causal: la distribución de responsabilidad entre los nodos del grafo, con sus componentes de sustituibilidad y asunción, y con las hipótesis de prevención que esa distribución produce. Cuando el destinatario necesita también compliance o imputación adversarial, la Serie I se ejecuta primero y sus resultados alimentan la Serie II o la III.

### II.  Paso 1 · Construcción del grafo G = (N, E, W)

Metrología Causal · Vol. II

El grafo es el objeto matemático sobre el que opera todo el cálculo de la Serie I. Su construcción no es un paso previo al análisis: es la primera operación analítica, y determina la validez de todo lo que sigue. Un grafo bien construido produce R* que mide responsabilidad causal real. Un grafo mal construido produce R* que mide algo diferente con exacta precisión formal.

El grafo G = (N, E, W) tiene tres componentes. El conjunto de nodos N contiene todos los actores con capacidad causal sobre el resultado D, incluyendo el nodo sumidero Nf que representa D. El conjunto de aristas E contiene las relaciones de influencia causal entre nodos, con su dirección. La matriz de pesos W asigna a cada arista un peso w_ij que refleja la intensidad de la influencia del nodo i sobre el nodo j.

El peso de cada arista no se asigna como un valor puntual: se asigna como un rango [a_ij, b_ij] calibrado según el nivel de evidencia disponible para esa relación. El valor de cálculo del Paso 3 es el midpoint m_ij = (a_ij + b_ij) / 2. La amplitud del rango alimenta el análisis de sensibilidad de la Serie III si el caso lo requiere.

Descripción de la evidencia Amplitud del rango [a_ij, b_ij]

Nivel E

E8 Evidencia experimental controlada o réplica verificada

±0.02 sobre el midpoint estimado

E7 Estudio observacional prospectivo con grupo de control

±0.05

E6 Múltiples estudios convergentes o consenso de expertos

±0.07

E5 Evidencia documental directa y consistente

±0.10

Metrología Causal · Vol. II

Descripción de la evidencia Amplitud del rango [a_ij, b_ij]

Nivel E

E4 Evidencia documental directa con inconsistencias menores

±0.12

E3 Evidencia indirecta sólida o inferencia estructural fuerte

±0.15

E2 Evidencia indirecta débil o inferencia estructural moderada

±0.18

E1 Evidencia mínima o testimonial no corroborada

±0.22

E0 Sin evidencia: nodo estructuralmente necesario pero no documentado

±0.25 sobre midpoint 0.30

### Ejemplo numérico — Caso de referencia (4 nodos)

### Nf = resultado D (nodo sumidero). N = {D (diseño), E (ejecutor), S (supervisor), Nf}.

### Aristas: D → Nf [0.35, 0.55], E → Nf [0.20, 0.40], S → Nf [0.10, 0.24], D → E [0.40, 0.60], S → E [0.25, 0.45].

Niveles de evidencia: D→Nf E5, E→Nf E4, S→Nf E3, D→E E5, S→E E4. Midpoints: D→Nf 0.45, E→Nf 0.30, S→Nf 0.17, D→E 0.50, S→E 0.35.

### III.  Paso 2 · Verificación de condiciones de validez

Antes del cálculo, el grafo debe cumplir dos condiciones que el Teorema de Perron-Frobenius requiere para garantizar la existencia y unicidad del eigenvector principal positivo: irreducibilidad y aperiodicidad.

Metrología Causal · Vol. II

El grafo es irreducible si desde cada nodo existe al menos un camino dirigido al nodo sumidero Nf. Un nodo sin camino al sumidero no tiene relación causal con D y debe eliminarse del grafo antes del cálculo. La irreducibilidad se verifica inspeccionando el grafo: si hay nodos "flotantes" sin camino a Nf, no son causalmente relevantes para el resultado analizado.

El grafo es aperiódico si no contiene ciclos de longitud fija que atrapen el método de potencias en una oscilación permanente. En la práctica, la aperiodicidad se garantiza añadiendo un autolazo de peso ε = 0.01 al nodo sumidero Nf: w_Nf,Nf = ε. Este ajuste es suficiente para romper cualquier periodicidad sin afectar la distribución R* de manera significativa.

Corrección de aperiodicidad

w_Nf,Nf = ε = 0.01  →  renormalizar cada columna de W para que Σ_j w_ij = 1

Solo se aplica si el grafo falla el test de aperiodicidad. En la mayoría de los casos prácticos el grafo ya es aperiódico.

### IV.  Paso 3 · Cálculo de R* por el método de potencias

Con la matriz W de midpoints construida y las condiciones de validez verificadas, el método de potencias calcula el eigenvector principal normalizado. El método es iterativo: parte de un vector inicial uniforme y lo multiplica repetidamente por W hasta que la diferencia entre iteraciones sucesivas cae por debajo del umbral de convergencia.

Método de potencias — iteración

R*(k+1) = W · R*(k)  /  ||W · R*(k)||□

Metrología Causal · Vol. II

Condición inicial: R*(0) = [1/n, 1/n, ..., 1/n]. Criterio de convergencia: ||R*(k+1) ₁ ⁶ ⁻ − R*(k)|| < 10 . En sistemas de 3–8 nodos típicos, la convergencia ocurre entre 15 y 40 iteraciones.

La condición de convergencia 10 ⁶ ⁻ garantiza que el vector R* es estable hasta la sexta cifra decimal. Para los propósitos del expediente, se reportan cuatro cifras decimales. La verificación final es simple: Σ_i R*_i = 1.000 (±0.001 por redondeo).

Nodo R* (resultado del caso de referencia)

Interpretación

0.4812 El nodo de diseño explica el 48% del resultado. Su influencia directa sobre Nf y su influencia estructural sobre E lo posicionan como el nodo de mayor centralidad causal.

D — Diseño

### 0.3104 El ejecutor explica el 31% del resultado. Su posición es significativa pero dependiente del diseño que lo orienta.

E — Ejecutor

### 0.1521 El supervisor explica el 15% del resultado. Su influencia se ejerce principalmente a través de E.

S — Supervisor

### 0.0563 El nodo sumidero retiene el residuo del autolazo ε. Este valor no tiene interpretación de responsabilidad.

Nf — Resultado

### V.  Paso 4 · Determinación de S y cálculo de R*_neta

Metrología Causal · Vol. II

Con el vector R* calculado, el Paso 4 determina S para cada nodo y calcula R*_neta: la fracción idiosincrática del peso causal de cada nodo, excluyendo la parte que cualquier otro en esa posición también habría producido.

S se deriva del Hijo dominante de cada nodo usando la tabla de conversión del Capítulo I·4. Para nodos institucionales o algoritmos sin ECO disponible, S se determina desde los tres criterios universales de la Introducción de este volumen: existencia de alternativa documentada, conformidad con la norma del dominio, y replicabilidad ante un par equivalente.

R*_neta

R*_neta_i = R*_i × (1 − S_i)

La fracción (1−S_i) es la proporción del acto que es idiosincrática del nodo i. Σ R*_neta_i ≤ 1. La diferencia 1 − Σ R*_neta_i es la responsabilidad sistémica total del campo.

Nodo R* S 1 − S

R*_neta Fuente de S

D — Diseño 0.4812 0.20 0.80 0.3850 Harmonía dominante — EP4. Decisión de diseño altamente idiosincrática.

E — Ejecutor 0.3104 0.72 0.28 0.0869 Fobos dominante — EP4. Alta presión del sistema de incentivos

Metrología Causal · Vol. II

Nodo R* S 1 − S

R*_neta Fuente de S

diseñado por D.

S — Supervisor 0.1521 0.55 0.45 0.0684 Anteros dominante — EP3. Supervisión condicionada a la respuesta del ejecutivo.

— — — 0.4597 Campo c: fracción del resultado que cualquier actor en estas posiciones habría producido.

Responsabilidad sistémica

### VI.  Paso 5 · Determinación de α y cálculo de Δ

El Paso 5 determina α para cada nodo usando la ruta disponible (A, B, o C según el tipo de caso) y calcula Δ: el déficit de asunción, la fracción de R* que el nodo causó, pero no integró como propia mediante acciones verificables.

Δ — Déficit de asunción

Δ_i  =  R*_i  ×  (1 − α_i)       Δ_total  =  Σ_i  Δ_i

Δ_i > 0 indica que el nodo causó más de lo que asumió. Δ_i < 0 indica inversión causal: el nodo asumió más de lo que causó. Δ_i = 0 indica equilibrio de asunción.

Metrología Causal · Vol. II

Nodo R* α 1 − α

Δ_i Fuente de α

### 0.4812 0.15 0.85 0.4090 Ruta B — Criterio de conocimiento: sí. Acción: mínima. Oportunidad: sí. α = 0.15.

D — Diseño

### 0.3104 0.40 0.60 0.1862 Ruta A — φ□ activo con facilitación. Reconoce el acto con apoyo del ECO.

E — Ejecutor

### 0.1521 0.62 0.38 0.0578 Ruta B — Acción de supervisión parcialmente documentada. Tres oportunidades de intervención identificadas, una actuada.

S — Supervisor

Δ_total — — — 0.6530 63% del resultado total no fue integrado como propio por ningún nodo. Brecha sistémica de asunción.

### VII.  Paso 6 · Cuantificación del daño D y las fracciones AD_i

El análisis causal distribuye responsabilidad en términos relativos (R*). Cuando el caso requiere también una distribución en términos absolutos —cuánto del daño total corresponde a cada nodo— el Paso 6 cuantifica D_total y calcula la fracción atribuible AD_i a cada nodo.

Metrología Causal · Vol. II

D_total tiene tres componentes que el mediador cuantifica desde el expediente del caso. T_inv es el daño de inversión: costos directos incurridos como consecuencia del resultado analizado. T_imp es el daño de impacto: consecuencias directas del resultado sobre los afectados, cuantificadas en las mismas unidades que T_inv. ΔT_tray es el daño de trayectoria: la diferencia entre el valor de la trayectoria esperada sin el resultado y el valor de la trayectoria real, proyectada al horizonte relevante para el caso.

D_total y fracción atribuible AD_i

D_total = T_inv + T_imp + ΔT_tray       AD_i = R*_i × D_total

AD_i es la contribución causal del nodo i al daño total en unidades absolutas. La suma Σ AD_i = D_total. Las fracciones AD_i son el insumo directo para cualquier determinación de compensación o reparación proporcional.

La cuantificación de D_total es responsabilidad del destinatario del análisis, no del mediador. El mediador recibe los valores de T_inv, T_imp, y ΔT_tray del expediente del caso y aplica la fórmula. Si el destinatario no tiene estimados de los tres componentes, el mediador entrega únicamente R* y documenta que AD_i está condicionado a la cuantificación de D_total por el destinatario.

### VIII.  Paso 7 · El expediente de Serie I

El expediente de Serie I contiene tres documentos. El mediador los produce en el orden que sigue: primero la hoja de calibración (ya completada en el Paso 1), después el vector R* con su análisis descriptivo, y finalmente las hipótesis de prevención.

Metrología Causal · Vol. II

Documento Contenido Criterio de completitud

1 · Hoja de calibración

Todos los nodos, todas las aristas con sus rangos [a_ij, b_ij] y niveles E0–E8, valores de S y α con sus fuentes, método de cálculo seleccionado.

Todos los ítems de la lista de verificación del Cap. I·7 completados y firmados.

2 · Vector R* con análisis descriptivo

Tabla de distribución con R*, S, R*_neta, α, Δ para cada nodo. Párrafo narrativo que describe la distribución causal en lenguaje del dominio del destinatario. Δ_total y su interpretación sistémica.

Σ R*_i = 1.000 (±0.001). El análisis narrativo no introduce juicios que el vector no sostiene.

3 · Hipótesis de prevención

Para cada nodo con R* > 0.15: una hipótesis de rediseño que reduciría su R* en sistemas futuros similares. Las hipótesis se formulan como condiciones estructurales, no como recomendaciones de conducta.

Cada hipótesis especifica qué cambio en el grafo produciría qué reducción estimada en R*. No se formulan hipótesis sin ancla estructural.

### Producto de salida · Capítulo II·1

Expediente de Serie I completo: hoja de calibración + vector R* con análisis descriptivo + hipótesis de prevención. El vector R* es el producto central que toda serie subsiguiente presupone. Sin el expediente de Serie I completo y verificado, ninguna otra serie puede iniciarse.

Notas al Capítulo II·1

Metrología Causal · Vol. II

1  El nodo sumidero Nf no tiene R* interpretable como responsabilidad causal: es el nodo que representa el resultado D, no un actor que lo produjo. El valor residual que retiene por el autolazo ε no debe incluirse en el análisis narrativo ni en las hipótesis de prevención. Cuando se reporta el vector R*, Nf se excluye de la tabla o se incluye con la nota explícita de que su valor es el residuo del ajuste de aperiodicidad.

2  La separación entre R* (responsabilidad causal estructural) y Δ (déficit de asunción) es una de las distinciones más importantes del sistema para la práctica. Un nodo con R* alto y Δ bajo ha asumido correctamente su posición causal: el daño es grande pero la responsabilidad fue integrada. Un nodo con R* bajo y Δ alto ha causado poco pero no ha asumido ni eso: la proporción es pequeña pero la evasión es total. Las dos situaciones tienen consecuencias completamente distintas para la prevención y para cualquier determinación de reparación.

3  La cuantificación de ΔT_tray requiere especificar el horizonte temporal de la proyección. Un horizonte demasiado corto subestima el daño de trayectoria; uno demasiado largo lo sobreestima con incertidumbre creciente. La práctica estándar es usar el horizonte que el destinatario del análisis considera relevante para su decisión, documentado en el expediente.

Metrología Causal · Vol. II

PARTE II · El análisis simple: una sola serie

### Capítulo II·2

### Serie II: Compliance Causal

El protocolo de evaluación de congruencia del nodo de diseño

### I.  Cuándo aplica la Serie II

La Serie II responde la pregunta de Tipo 2: ¿el nodo de diseño operó en conformidad con lo que declaró que haría? Es la serie del compliance en su sentido más preciso — no el cumplimiento de una norma externa sino la congruencia entre el campo que el nodo de diseño declaró que produciría y el campo que efectivamente produjo.

El nodo de diseño es el actor que diseñó las condiciones estructurales bajo las cuales los demás nodos del grafo operaron: la institución que estableció el protocolo, la organización que diseñó el sistema de incentivos, el regulador que fijó las reglas, el arquitecto del sistema que determinó las restricciones de operación. La Serie II evalúa a ese nodo en términos de la brecha entre su diseño declarado y su operación real.

La Serie II nunca se aplica sin Serie I previa. El IIC requiere el vector R* del nodo de diseño como denominador de la fracción de responsabilidad que la congruencia modula. Sin R*, el IIC no tiene contexto causal: mide la brecha entre declaración y

Metrología Causal · Vol. II

operación, pero no dice cuánto pesa esa brecha en el resultado analizado.

### II.  Paso 1 · El grafo con horizonte prospectivo y el nodo de diseño

El grafo de la Serie II tiene la misma estructura del grafo de la Serie I con dos diferencias. La primera: el nodo de diseño N_D debe estar identificado explícitamente antes de comenzar el Paso 2. No todos los grafos tienen un único nodo de diseño claro — en algunos casos hay múltiples niveles de diseño. El mediador identifica el nodo de diseño más relevante para la pregunta de compliance que el destinatario plantea.

La segunda diferencia: el grafo puede incluir aristas prospectivas — relaciones de influencia que el nodo de diseño declaró que existirían pero que el análisis retroactivo de Serie I no incluyó porque no se verificaron en la evidencia disponible. Estas aristas prospectivas son el insumo del Paso 2: son los protocolos declarados que el IIC contrasta con lo observable.

Identificación del nodo de diseño — criterios

El nodo de diseño N_D es el nodo que cumple simultáneamente tres condiciones: (1) diseñó las condiciones estructurales bajo las que operaron otros nodos, (2) declaró explícitamente qué campo produciría su diseño (en documentos, normas, contratos, o comunicaciones verificables), y (3) tiene R* > 0 en el análisis de Serie I — es causalmente relevante para el resultado analizado.

Si hay múltiples candidatos a nodo de diseño, el análisis de Serie II se aplica al nodo con mayor R* entre ellos, salvo que el destinatario especifique otro nodo explícitamente.

Metrología Causal · Vol. II

### III.  Paso 2 · Cálculo del IIC

El Índice de Integridad Causal (IIC) mide la correlación promedio entre lo que el nodo de diseño declaró que produciría y lo que produjo. Opera sobre los protocolos declarados del nodo de diseño que son relevantes para el resultado analizado: no sobre todos los protocolos del nodo, sino sobre los que tienen relación directa con la cadena causal que produjo D.

Para cada protocolo declarado k relevante para D, el mediador calcula la correlación c_k entre la variable declarada (lo que el protocolo prometía producir) y la variable observable (lo que efectivamente produjo en el período analizado). La correlación puede calcularse sobre datos cuantitativos o estimarse cualitativamente usando la escala de la tabla siguiente.

IIC — Índice de Integridad Causal

IIC  =  (1/n)  Σ_k  c_k        con  c_k  =  corr(declarado_k, observable_k)

n = número de protocolos declarados relevantes para D. c_k □ [−1, 1]. IIC = 1 indica congruencia total entre todos los protocolos. IIC = 0 indica ausencia de correlación. IIC < 0 indica divergencia sistemática (el campo real es opuesto al declarado).

Descripción Cómo se estima cualitativamente

Valor de c_k

c_k = 1.00 Congruencia perfecta: el protocolo produjo exactamente lo que declaró.

El indicador de cumplimiento del protocolo muestra 100% o el evaluador no puede distinguir el campo real del declarado.

c_k □ [0.70, 1.00)

Alta congruencia: el campo real sigue la

Las principales variables del protocolo se comportaron como

Metrología Causal · Vol. II

Descripción Cómo se estima cualitativamente

Valor de c_k

dirección del declarado con desviaciones menores.

fueron diseñadas; hay excepciones documentadas menores.

c_k □ [0.40, 0.70)

Congruencia moderada: el campo real se parece al declarado pero con brechas significativas.

Algunos indicadores clave del protocolo funcionaron; otros no. Las desviaciones tienen efecto material.

c_k □ [0.00, 0.40)

Congruencia baja: el campo real diverge sustancialmente del declarado.

La mayoría de los indicadores del protocolo no produjeron lo prometido. El diseño existe en papel.

c_k < 0 Divergencia: el campo real va en dirección opuesta al declarado.

El protocolo prometía controlar algo que en la práctica amplificó. El diseño produjo el efecto inverso al declarado.

### Ejemplo numérico — IIC del nodo D (caso de referencia)

Protocolos declarados relevantes (n = 3): P1 — sistema de incentivos: c□ = 0.18 (los incentivos prometían alinear crecimiento con riesgo; en la práctica desalinearon). P2 — protocolo de aprobación: c□ = 0.35 (el protocolo prometía filtrar activos tóxicos; en la práctica los aprobó con excepciones). P3 — reporte de riesgo: c□ = 0.61 (el sistema de reporte funcionó moderadamente).

IIC_D = (0.18 + 0.35 + 0.61) / 3 = 1.14 / 3 = 0.38. El nodo de diseño opera con 38% de congruencia respecto a sus declaraciones. Baja congruencia — el campo real diverge sustancialmente del declarado.

Metrología Causal · Vol. II

### IV.  Paso 3 · Ajuste de pesos por IIC y recalculo de R*

El IIC del nodo de diseño ajusta los pesos de sus aristas estructurales salientes. La lógica del ajuste es directa: un nodo de diseño con baja congruencia influye sobre los demás nodos con menos efectividad de la que su posición estructural indicaría — su influencia real es mayor que la que el campo observable refleja porque parte de esa influencia opera a través de la brecha entre el diseño declarado y el real.

Ajuste de pesos por IIC

w_ij(ajustado) = w_ij(base) × (1 + k × (1 − IIC_D))

k es el coeficiente de amplificación de la brecha: k □ [0.5, 1.5] según la magnitud del resultado analizado. Valor estándar: k = 1.0. El ajuste amplifica las aristas del nodo de diseño reflejando que la brecha entre su campo declarado y real tiene efecto causal.

Con los pesos ajustados, se recalcula R* usando el mismo método de potencias del Paso 3 de la Serie I sobre la nueva matriz W(ajustado). El nuevo vector R*(ajustado) refleja la posición causal del nodo de diseño una vez que su baja congruencia es incorporada en la estructura del grafo.

Ejemplo numérico — Ajuste y recalculo (k = 1.0)

IIC_D = 0.38. Factor de ajuste: 1 + 1.0 × (1 − 0.38) = 1 + 0.62 = 1.62.

Aristas ajustadas de D: D→Nf pasa de 0.45 a 0.45 × 1.62 = 0.73 (luego renormalizado). D→E pasa de 0.50 a 0.81.

R*(ajustado): D = 0.5841, E = 0.2713, S = 0.1082. El ajuste por IIC aumenta R* del nodo de diseño en 10 puntos porcentuales, reflejando que su baja congruencia amplifica su peso causal real.

Metrología Causal · Vol. II

### V.  Paso 4 · El fraude annona y el umbral de acción

El fraude annona es el corolario III del Teorema de la Responsabilidad Causal Proporcional. Mide la posición más grave que el sistema puede registrar en un nodo de diseño: alta centralidad causal (R* alto), baja asunción (α bajo), y baja congruencia (IIC bajo). El nombre proviene del término romano annona — la gestión del suministro de grano — y la figura del funcionario que administra un bien esencial prometiendo calidad que no entrega.

Fraude annona

Fraude_annona_D  =  R*_D  ×  (1 − α_D)  ×  (1 − IIC_D)

El fraude annona alcanza su máximo cuando R*_D = 1, α_D = 0, e IIC_D = 0: el nodo es el único responsable, no ha asumido nada, y opera en dirección opuesta a lo que declaró. En la práctica, valores superiores a 0.20 indican una posición de responsabilidad institucional grave.

Ejemplo numérico — Fraude annona del caso de referencia

R*_D(ajustado) = 0.5841, α_D = 0.15, IIC_D = 0.38.

Fraude_annona_D = 0.5841 × (1 − 0.15) × (1 − 0.38) = 0.5841 × 0.85 × 0.62 = 0.3078.

Interpretación: el nodo de diseño genera una posición de fraude annona del 31% — dentro del rango de responsabilidad institucional grave. Este valor supera el umbral de 0.20 que, en la mayoría de los dominios regulatorios, activa requisitos formales de intervención.

### VI.  Paso 5 · El ajuste debitor

Metrología Causal · Vol. II

El ajuste debitor es la propuesta del sistema al destinatario sobre cómo reducir la brecha de compliance del nodo de diseño. No es una sanción ni una prescripción: es la lectura estructural de qué cambios en el nodo de diseño reducirían su Δ y su fraude annona. El mediador formula el ajuste debitor en tres componentes que corresponden a los tres orígenes de la brecha.

Qué corrige Cómo se formula

Componente del ajuste debitor

Estructural — protocolos

La brecha entre el campo declarado y el real (IIC bajo). Corrige los protocolos cuyo c_k es más bajo.

Para cada protocolo con c_k < 0.50: describir qué cambio de diseño elevaría c_k al rango [0.70, 1.00]. Expresar como condición estructural, no como instrucción de conducta.

Procesal — acción pendiente

El déficit de acción del nodo de diseño (α bajo). Corrige los criterios de la Ruta B que no se cumplieron.

Para cada criterio de α que el nodo de diseño no cumplió (conocimiento sin acción, oportunidades no actuadas): describir la acción concreta con plazo verificable que cubriría ese criterio.

Reparatorio — daño en curso

La fracción AD_D del daño que el nodo de diseño generó y que no ha sido abordada. Corrige el Δ del nodo de diseño hacia atrás.

Si D_total está cuantificado: AD_D = R*_D(ajustado) × D_total. El ajuste reparatorio es esa fracción no cubierta por acciones verificables de α ya registradas.

Metrología Causal · Vol. II

### VII.  Paso 6 · El expediente de Serie II

### El expediente de Serie II entrega cuatro documentos. Los dos primeros son actualizaciones de los documentos de Serie I; los dos siguientes son específicos de Serie II.

Documento Contenido Diferencia respecto a Serie I

1 · Hoja de calibración (actualizada)

La hoja de Serie I con la adición de: identificación del nodo de diseño, protocolos declarados relevantes con sus c_k, coeficiente k del ajuste.

Añade la sección de compliance al documento base de Serie I.

2 · Vector R* ajustado

El vector R* recalculado con los pesos ajustados por IIC. Tabla comparativa R*(base) vs R*(ajustado) para cada nodo.

El vector R* de Serie I es el punto de referencia; el de Serie II es el resultado del ajuste por congruencia.

3 · Mapa de brecha IIC

Para cada protocolo declarado relevante: c_k documentado, descripción de la brecha, evidencia que la sustenta. El IIC global del nodo de diseño con su cálculo explícito.

Documento nuevo. Específico de Serie II.

4 · Ajuste debitor con cronograma

Los tres componentes del ajuste debitor (estructural, procesal, reparatorio) con plazos verificables para cada acción propuesta.

Documento nuevo. Específico de Serie II.

### Producto de salida · Capítulo II·2

Metrología Causal · Vol. II

Expediente de Serie II completo: hoja de calibración actualizada + vector R* ajustado + mapa de brecha IIC + ajuste debitor con cronograma. El IIC del nodo de diseño y el fraude annona son los dos indicadores centrales que el destinatario recibe como resultado del análisis de compliance.

Notas al Capítulo II·2

1  El coeficiente k del ajuste de pesos por IIC tiene rango [0.5, 1.5]. El valor estándar k = 1.0 aplica cuando la magnitud del resultado es consistente con el dominio típico del sistema. En casos donde el resultado es extraordinariamente grave para el dominio (colapsos sistémicos, daños masivos, crisis institucionales) puede justificarse k > 1.0. En casos donde el resultado es menor o el contexto es de alta incertidumbre regulatoria genuina, puede justificarse k < 1.0. La elección de k debe documentarse en la hoja de calibración con su justificación explícita.

2  El fraude annona tiene el nombre que tiene porque el sistema lo diseñó para capturar una posición específica: la de quien administra un bien esencial (un sistema de crédito, un protocolo de salud, un programa social) declarando estándares que luego no cumple, con alta centralidad causal en el resultado dañoso que esa brecha produce. No es una calificación moral: es una medición estructural de la combinación de R* alto, α bajo, e IIC bajo. El nombre orienta la interpretación, pero la medición es formal.

3  El ajuste debitor en su componente reparatorio no es equivalente a una determinación de reparación legal o contractual. Es la lectura estructural de la fracción del daño que corresponde al nodo de diseño según el análisis causal. Cualquier determinación de reparación formal requiere instancias adicionales (jurídicas, regulatorias, arbitrales) que el análisis causal informa, pero no reemplaza.

Metrología Causal · Vol. II

PARTE II · El análisis simple: una sola serie

### Capítulo II·3

### Serie III: Imputación Causal

El protocolo del análisis adversarial con Declaración de robustez

### I.  Cuándo aplica la Serie III

La Serie III responde la pregunta de Tipo 3: ¿puede sostenerse la atribución de responsabilidad ante impugnación adversarial? Es la serie del escrutinio. Su función no es producir una distribución de responsabilidad más precisa que la de la Serie I — es verificar que la distribución de la Serie I es robusta: que no cambia sustancialmente cuando los parámetros del grafo varían dentro de los rangos que la evidencia permite.

La Serie III aplica siempre que el análisis deba resistir un cuestionamiento externo organizado: el tribunal que puede revisar cada arista del grafo, el regulador que puede impugnar cada valor de S, el árbitro que puede cuestionar cada estimado de α. La distinción respecto a la Serie I es de estándar, no de método: la Serie I trabaja con midpoints; la Serie III trabaja con rangos completos y verifica si la conclusión es estable a través de ellos.

La Serie III también se aplica siempre que el caso tenga consecuencias de alta magnitud para el destinatario — no porque las consecuencias cambien la metodología, sino porque el nivel de

Metrología Causal · Vol. II

### escrutinio que esas consecuencias atraerán justifica invertir el esfuerzo adicional del análisis de sensibilidad.

### II.  Paso 1 · El estándar adversarial

El estándar adversarial restringe el grafo de Serie III a la evidencia que resistiría impugnación en el foro donde el análisis será usado. El mediador no puede usar en Serie III ninguna arista que el adversario podría rechazar por deficiente en ese foro específico.

En la práctica, el estándar adversarial se traduce en dos restricciones concretas. Primera: solo las aristas con evidencia E1 o superior se incluyen en el grafo adversarial — las aristas E0 (nodos estructuralmente necesarios, pero no documentados) quedan fuera o se incluyen con rangos muy amplios y nivel de incertidumbre explícito. Segunda: los rangos [a_ij, b_ij] se calculan con criterio conservador — se usa el rango más amplio que la evidencia disponible puede justificar, no el más estrecho.

Foro Estándar de evidencia aplicable

Restricción sobre el grafo adversarial

Tribunal civil Prueba por preponderancia de evidencia — más probable que no

Aristas con evidencia E2 o superior. Rangos moderados. Declaración B o superior para sostener la atribución.

Tribunal penal

Más allá de duda razonable

Aristas con evidencia E3 o superior. Rangos estrechos. Declaración A recomendada; B como mínimo sostenible.

Regulador / Arbitraje

Estándar específico del organismo —

Aristas con evidencia E2 o E3 según el reglamento del

Metrología Causal · Vol. II

Foro Estándar de evidencia aplicable

Restricción sobre el grafo adversarial

generalmente entre civil y penal

organismo. Verificar el estándar específico antes de construir el grafo.

Auditoría interna / Investigación

Estándar de razonabilidad administrativa

Aristas con evidencia E1 o superior. Rangos amplios aceptables. Declaración C suficiente en la mayoría de los casos.

Comité de ética / Par académico

Escrutinio metodológico riguroso

Todas las aristas documentadas y justificadas. Rangos con fuente explícita. Declaración A o B preferida.

### III.  Paso 2 · R* bajo estándar adversarial

Con el grafo adversarial construido, el Paso 2 calcula R* sobre los midpoints adversariales y R*_neta con S calibrado desde evidencia admisible. El proceso es idéntico al de la Serie I — la diferencia es que la hoja de calibración adversarial es más restrictiva: menos aristas, rangos más amplios, valores de S con fuentes explícitamente admisibles.

El vector R*(adversarial) es el punto de referencia del análisis de sensibilidad del Paso 4. Si R*(adversarial) es significativamente diferente de R*(base) de la Serie I, el mediador documenta la diferencia y la incluye en el reporte de sensibilidad. Una divergencia grande entre los dos vectores indica que parte de la atribución de la Serie I descansa en evidencia que el foro adversarial no admite — lo que el destinatario necesita saber antes de presentar el análisis.

Metrología Causal · Vol. II

### IV.  Paso 3 · El hipercubo de parámetros Π

El hipercubo de parámetros Π es el espacio de todas las matrices de pesos W consistentes con los rangos [a_ij, b_ij] de la hoja de calibración adversarial. Cada punto del hipercubo es una matriz W específica — una asignación concreta de valores para todos los pesos del grafo dentro de sus rangos admisibles.

El hipercubo tiene dimensión igual al número de aristas del grafo. Un grafo de 4 nodos con 5 aristas tiene un hipercubo en □□. El espacio es continuo, pero el análisis de sensibilidad no requiere explorarlo exhaustivamente: un conjunto de puntos de evaluación bien elegido cubre las conclusiones relevantes.

Puntos de evaluación mínimos del hipercubo

Esquinas del hipercubo: todos los vértices donde cada peso toma su valor mínimo a_ij o su valor máximo b_ij. Para n aristas: 2ⁿ esquinas. En grafos de 4–6 nodos típicos (5–10 aristas): 32–1024 esquinas. Evaluar todas.

Centro del hipercubo: el vector de midpoints m_ij = (a_ij + b_ij) / 2. Es el punto R*(adversarial) del Paso 2.

Muestreo aleatorio: si el número de esquinas supera 1000 (grafos de más de 10 aristas), completar con 500–1000 puntos aleatorios dentro del hipercubo usando distribución uniforme sobre cada rango.

Puntos de quiebre: puntos específicos donde el ranking de los nodos cambia. Identificarlos permite caracterizar exactamente qué condición produce cada cambio de conclusión.

### V.  Paso 4 · Análisis de estabilidad del ranking σ(w)

Metrología Causal · Vol. II

Para cada punto w del hipercubo, el mediador calcula R*(w) y registra el ranking σ(w): el ordenamiento de los nodos de mayor a menor R*. La pregunta central del análisis de sensibilidad no es si R* cambia — inevitablemente cambia cuando los parámetros varían. La pregunta es si el ranking cambia: si el nodo que tiene el mayor R* en el midpoint mantiene esa posición en todos los puntos del hipercubo, o si en algunos puntos otro nodo lo supera.

Los puntos donde σ(w) cambia se llaman puntos de quiebre. Un punto de quiebre es un valor específico de los parámetros donde la conclusión sobre quién tiene mayor responsabilidad causal se invierte. Identificar los puntos de quiebre permite al mediador decirle al destinatario exactamente bajo qué condiciones la atribución principal cambiaría.

Función de robustez ρ(θ)

∈ ∀ ρ(θ)  =  Vol{ w  Π : R*_θ(w) > R*_j(w)   j ≠ θ }  / Vol(Π)

ρ(θ) es la fracción del hipercubo donde el nodo θ mantiene el ranking que tiene en el midpoint. ρ(θ) = 1 significa que θ es siempre el nodo de mayor R*, independientemente de cómo varíen los parámetros dentro de sus rangos admisibles.

### VI.  Paso 5 · La Declaración de robustez: niveles A, B, C, D

La Declaración es el documento que comunica la robustez del análisis al destinatario. Tiene cuatro niveles que corresponden a distintos umbrales de la función ρ(θ). El nivel de Declaración determina con qué fuerza el mediador puede sostener la atribución ante el foro adversarial.

Metrología Causal · Vol. II

Nivel Condición de ρ(θ)

Cuando aplica

Enunciado de la Declaración

A — Robustez total

ρ(θ) = 1.00 (100% del hipercubo)

"La atribución es estructuralmente robusta: el nodo θ mantiene la posición causal más alta en todos los escenarios consistentes con la evidencia disponible. Ninguna variación admisible de los parámetros cambia esta conclusión."

Análisis con evidencia de alta calidad (E4–E8) y rangos estrechos. Recomendado para foros penales.

B — Robustez sustancial

ρ(θ) ≥ 0.90 (90% del hipercubo)

"La atribución es sustancialmente robusta: el nodo θ mantiene la posición causal más alta en el 90% o más de los escenarios consistentes con la evidencia. Los escenarios donde esto cambia representan casos extremos de los rangos admisibles."

Análisis con mezcla de evidencia E3–E5. Estándar para foros civiles y regulatorios en la mayoría de los dominios.

C — Robustez moderada

ρ(θ) ≥ 0.70 (70% del hipercubo)

"La atribución es moderadamente robusta: el nodo θ mantiene la posición causal más alta en el 70–89% de los escenarios consistentes con la evidencia. Existe un conjunto no trivial de escenarios admisibles

Análisis con evidencia mixta o amplia incertidumbre en algunos parámetros. Útil para auditorías internas y comités.

Metrología Causal · Vol. II

Nivel Condición de ρ(θ)

Cuando aplica

Enunciado de la Declaración

donde otro nodo tiene mayor R*."

ρ(θ) < 0.70 "La atribución tiene robustez limitada: en más del 30% de los escenarios consistentes con la evidencia, otro nodo tiene mayor R* que θ. La conclusión es sensible a variaciones razonables de los parámetros y requiere evidencia adicional antes de ser presentada en foros adversariales."

D — Robustez limitada

La evidencia es insuficiente para sostener la imputación ante escrutinio adversarial. Se recomienda buscar evidencia adicional.

### VII.  Paso 6 · El expediente de Serie III

### El expediente de Serie III es el más completo del sistema. Contiene todos los documentos de la Serie I y añade tres documentos específicos del análisis adversarial.

Documento Contenido Nota

1 · Hoja de calibración adversarial

La hoja de calibración con el estándar adversarial aplicado: aristas excluidas documentadas, rangos ampliados con justificación, fuentes de evidencia con su nivel admisible en el foro.

Diferente de la hoja de Serie I: refleja las restricciones del foro, no la evidencia total disponible.

Metrología Causal · Vol. II

Documento Contenido Nota

2 · Vector R*(adversarial)

El vector R* calculado bajo el estándar adversarial. Comparación con R*(base) de Serie I si hay diferencias significativas.

La comparación entre los dos vectores informa al destinatario qué parte de la atribución descansa en evidencia no admisible en el foro.

3 · Reporte de sensibilidad

La función ρ(θ) para el nodo principal de la atribución. Los puntos de quiebre identificados con la descripción de qué condición los produce. El mapa de estabilidad del ranking sobre el hipercubo.

El reporte de sensibilidad es el documento más técnico del expediente. Se presenta en un apéndice separado para audiencias no técnicas.

4 · Declaración de robustez

El enunciado formal del nivel A, B, C o D con los valores exactos de ρ(θ) que lo sustentan. Firmado por el mediador como responsable del análisis.

La Declaración es el documento que el destinatario presenta en el foro. Es autocontenida: no requiere que el destinatario entienda el cálculo detrás.

### Producto de salida · Capítulo II·3

Expediente de Serie III completo: hoja de calibración adversarial + vector R*(adversarial) + reporte de sensibilidad + Declaración de robustez en nivel A, B, C, o D. La Declaración es el producto central que el destinatario lleva al foro adversarial.

Notas al Capítulo II·3

Metrología Causal · Vol. II

1  El análisis de sensibilidad de la Serie III responde una pregunta que con frecuencia el destinatario no ha formulado pero que necesita responder: ¿qué tendría que ser verdad sobre el caso para que mi conclusión cambiara? Los puntos de quiebre del hipercubo responden esa pregunta con precisión. Un destinatario que conoce sus puntos de quiebre está mejor preparado para el escrutinio adversarial que uno que solo conoce R*(midpoint), porque sabe exactamente qué argumentos del adversario cambiarían la conclusión y cuáles no.

2  La Declaración de nivel D no es un fracaso del análisis: es el resultado honesto cuando la evidencia disponible no es suficiente para sostener la atribución ante escrutinio adversarial. Una Declaración D informa al destinatario que necesita evidencia adicional antes de presentar el análisis — información que vale tanto como una Declaración A, porque previene el error de presentar una atribución que el adversario puede demoler con variaciones razonables de los parámetros.

3  La función ρ(θ) tal como se define en este capítulo mide la robustez de la posición relativa de un nodo — si mantiene el ranking más alto. En algunos casos el destinatario no necesita que el nodo θ tenga el R* más alto; necesita que R*_θ supere un umbral específico (por ejemplo, que supere 0.30 para activar una consecuencia normativa particular). En esos casos, ρ se redefine como la fracción del hipercubo donde R*_θ(w) > umbral, y el análisis sigue el mismo procedimiento con ese criterio de estabilidad ajustado.

Metrología Causal · Vol. II

PARTE III · El análisis integrado: las tres series

### Capítulo III·1

### El protocolo integrado

Secuencia de producción de las tres series y por qué el orden importa

### I.  Qué es el análisis integrado y cuándo se activa

El análisis integrado aplica las tres series del Método Prometeo sobre el mismo grafo causal. No es la suma de tres análisis independientes: es un análisis único cuyas tres series están relacionadas por insumos compartidos, verificaciones cruzadas y un expediente que consolida sus resultados en un producto coherente. La diferencia entre ejecutar tres series separadas y ejecutar el análisis integrado es exactamente esa coherencia: el análisis integrado verifica que los tres resultados son mutuamente consistentes, y cuando no lo son, lo diagnostica.

El análisis integrado se activa cuando el destinatario necesita más de un tipo de respuesta sobre el mismo caso. Las combinaciones más frecuentes son: Tipos 1+3 (diagnóstico e imputación) → Series I+III; Tipos 1+2 (diagnóstico y compliance) → Series I+II; y Tipos 1+2+3 (diagnóstico, compliance e imputación) → las tres series. En todos los casos, la regla es la misma: el mediador activa todas las series que

Metrología Causal · Vol. II

corresponden a todos los tipos identificados y las ejecuta en el orden que este capítulo establece.

### II.  Por qué el orden de producción es invariante

El orden de las tres series no es una convención procedimental. Es una consecuencia de las dependencias matemáticas entre sus resultados. La Serie II requiere el vector R* de la Serie I como denominador del IIC y como base del ajuste de pesos. La Serie III requiere el vector R* de la Serie I como punto central del hipercubo de parámetros. Ninguna de las dos series puede producir un resultado válido sin el vector R* que la Serie I entrega.

La dependencia va en una sola dirección: I → II → III. No existe ninguna operación de la Serie I que requiera resultados de la Serie II o III. No existe ninguna operación de la Serie II que requiera resultados de la Serie III. El grafo de dependencias es acíclico y el orden topológico es único: Serie I primero, Serie II después si aplica, Serie III al final si aplica.

Por qué ejecutar las series en orden incorrecto produce resultados inválidos

Serie II antes de Serie I: el IIC no tiene denominador. El ajuste de pesos no tiene referencia. El fraude annona es un número sin contexto causal.

Serie III antes de Serie I: el hipercubo no tiene punto central. El análisis de sensibilidad mide variación alrededor de un punto inexistente. La Declaración no tiene R*(adversarial) que sostener.

Serie III antes de Serie II (cuando ambas aplican): el grafo adversarial de Serie III no incorpora el ajuste de pesos por IIC que Serie II produjo. La

Metrología Causal · Vol. II

Declaración mide la robustez del R*(base), no del R*(ajustado). Es una robustez incompleta.

### III.  El protocolo paso a paso del análisis integrado

El protocolo integrado tiene diez pasos. Los primeros siete son idénticos a los siete pasos de la Serie I — construyen el grafo base y producen el vector R* con todos sus componentes. Los pasos ocho, nueve y diez añaden las series adicionales en el orden correcto.

Paso Operación Producto Serie

1 Construcción del grafo G = (N, E, W) con todos los nodos, aristas, rangos [a_ij, b_ij] y niveles E0–E8

I

Hoja de calibración base

2 Verificación de irreducibilidad y aperiodicidad. Corrección ε si hay periodicidad

I

Hoja de calibración validada

3 Cálculo de R* por método de potencias sobre midpoints. Verificar Σ R*_i = 1

Vector R*(base) I

4 Determinación de S para cada nodo desde P(Hijos) o criterios universales. Cálculo de R*_neta

R*_neta por nodo I

5 Determinación de α para cada nodo desde Ruta A, B o C. Cálculo de Δ por nodo y Δ_total

I

Δ por nodo — Δ_total

Metrología Causal · Vol. II

Paso Operación Producto Serie

6 Cuantificación de D_total si el destinatario lo requiere. Cálculo de AD_i

I

Fracciones AD_i (condicional)

7 Producción del expediente de Serie I: hoja de calibración + vector R* + hipótesis de prevención

I

Expediente Serie I completo

8 Identificación del nodo de diseño N_D. Cálculo de IIC sobre protocolos declarados relevantes. Ajuste de pesos por IIC. Recalculo de R*(ajustado). Cálculo de fraude annona. Producción del ajuste debitor

II

Expediente Serie II completo

9 Construcción del grafo adversarial sobre R*(ajustado) de Serie II. Verificación del estándar del foro. Construcción del hipercubo Π sobre rangos adversariales. Evaluación del ranking σ(w) en esquinas, centro y muestra. Cálculo de ρ(θ). Determinación del nivel de Declaración

III

Expediente Serie III completo

10 Verificación cruzada de consistencia entre las tres series. Diagnóstico de inconsistencias. Producción del expediente integrado consolidado

I+II+III

Expediente integrado

Metrología Causal · Vol. II

### IV.  La decisión crítica del Paso 9: cuál vector R* entra al hipercubo

Cuando el análisis integrado incluye las tres series, el mediador debe decidir qué vector R* usa como punto central del hipercubo de la Serie III. Hay dos opciones: R*(base) de la Serie I o R*(ajustado) de la Serie II. La decisión no es discrecional.

Si el caso incluye Series I+II+III, el hipercubo de Serie III se construye sobre R*(ajustado) de la Serie II. La razón es directa: el análisis de compliance de la Serie II actualizó la distribución de responsabilidad incorporando la congruencia real del nodo de diseño. La Serie III evalúa la robustez de esa distribución actualizada, no de la distribución sin ajuste. Presentar una Declaración basada en R*(base) cuando hay un R*(ajustado) disponible sería medir la robustez de una distribución que el propio análisis ya superó.

Si el caso incluye solo Series I+III (sin Serie II), el hipercubo se construye sobre R*(base). No hay ajuste disponible y el vector base es el correcto. El mediador documenta en la hoja de calibración adversarial que no se aplicó ajuste de compliance y los motivos (tipo de pregunta Tipo 1+3, sin nodo de diseño identificado, o sin pregunta de compliance formulada por el destinatario).

### V.  El grafo único como fuente de coherencia

La característica más importante del análisis integrado es que las tres series operan sobre el mismo grafo. No son tres grafos distintos adaptados a cada pregunta: son tres lecturas distintas del mismo objeto. El grafo base construido en el Paso 1 es la fuente común de todas las distribuciones R* del expediente integrado.

Esta unicidad del grafo no impide que las series tengan diferencias en sus versiones del grafo. La Serie II añade aristas

Metrología Causal · Vol. II

prospectivas del nodo de diseño. La Serie III restringe el grafo al estándar adversarial del foro. Pero esas diferencias son versiones del grafo base — extensiones o restricciones de un objeto común, no grafos independientes. El mediador que construye grafos separados para cada serie produce resultados que no son comparables entre sí y pierde la ventaja principal del análisis integrado: la verificación cruzada del Paso 10.

### Producto de salida · Capítulo III·1

Mapa de ruta del análisis integrado: qué pasos se ejecutan, en qué orden, qué produce cada uno, y cuál es la fuente de insumo de cada paso. La decisión sobre qué vector R* entra al hipercubo de Serie III queda documentada en el encabezado del expediente integrado.

Notas al Capítulo III·1

1  La analogía entre el análisis integrado y una auditoría financiera con tres niveles de revisión es útil pero imprecisa. Una auditoría financiera puede realizarse en niveles independientes — cada nivel produce su resultado sin necesidad de los demás. El análisis integrado no: la Serie III literalmente no puede comenzar sin el vector R* de la Serie I, y cuando hay compliance, necesita el vector de la Serie II. La dependencia no es opcional ni procedimental: es matemática.

2  El Paso 10 — la verificación cruzada — no está en la mayoría de los sistemas de análisis multicapa porque esos sistemas no producen resultados que deberían ser mutuamente consistentes. El análisis integrado sí los produce, porque las tres series describen el mismo sistema desde tres perspectivas. La verificación cruzada no añade un cuarto resultado: detecta si los tres resultados existentes cuentan la misma historia. Cuando no la cuentan, el Capítulo III·2 establece qué significa esa divergencia y qué hacer con ella.

Metrología Causal · Vol. II

PARTE III · El análisis integrado: las tres series

### Capítulo III·2

### La verificación cruzada entre series

Consistencias esperadas y diagnóstico de inconsistencias

### I.  Por qué la verificación cruzada es parte del protocolo

Las tres series del análisis integrado describen el mismo sistema causal desde tres perspectivas. Si el análisis es internamente coherente, sus resultados deben ser mutuamente consistentes: lo que la Serie I dice sobre la posición del nodo de diseño debe ser compatible con lo que la Serie II dice sobre su congruencia, y ambas deben ser compatibles con lo que la Serie III dice sobre la robustez de esa posición. Una inconsistencia entre series no es un problema estético del expediente: es una señal de que algo en la construcción del grafo o en la calibración de los parámetros requiere revisión.

La verificación cruzada es el Paso 10 del protocolo integrado. No produce un resultado nuevo — produce una auditoría de los resultados existentes. Su output es binario: consistencia confirmada o inconsistencia detectada con diagnóstico. Cuando hay inconsistencia, el protocolo de diagnóstico de este capítulo

Metrología Causal · Vol. II

identifica el origen y prescribe la corrección antes de que el expediente sea entregado al destinatario.

### II.  Las cuatro consistencias esperadas del análisis integrado

Hay cuatro relaciones de consistencia que el análisis integrado debe cumplir. El mediador las verifica en orden después de completar los Pasos 7, 8 y 9 del protocolo del Capítulo III·1.

Consistenci a

Relación que se verifica

Umbral de consistencia

Qué señala la violación

C1 · R*(base) ↔ R*(ajustado)

El ajuste de pesos por IIC debe ampliar R* del nodo de diseño N_D respecto al R*(base), o mantenerlo igual si IIC = 1. Nunca puede reducirlo: una baja congruencia del diseño siempre amplifica su peso causal real, nunca lo reduce.

R*(ajustado)_N D ≥ R*(base)_ND en todos los casos donde IIC_ND < 1

Si R*(ajustado)_N D < R*(base)_ND: el coeficiente k del ajuste está mal calibrado o la fórmula de ajuste tiene un error aritmético. Revisar el Paso 8.

C2 · Δ ↔ IIC El déficit de asunción

No hay umbral rígido.

Si IIC bajo con Δ muy bajo: el

Metrología Causal · Vol. II

Consistenci a

Relación que se verifica

Umbral de consistencia

Qué señala la violación

Δ_ND del nodo de diseño y su IIC deben moverse en la misma dirección: cuando IIC es bajo (alta brecha de congruencia), α tiende a ser bajo también (baja asunción), y por tanto Δ tiende a ser alto. No es una identidad — son dimensiones distintas del mismo ego — pero una divergencia extrema requiere diagnóstico.

Divergencia extrema: IIC < 0.30 con Δ_ND < 0.10 (o IIC > 0.80 con Δ_ND > 0.60)

nodo de diseño declaró mal su campo, pero asumió sus actos con alta calidad — posible si el diseño fue erróneo, pero de buena fe. Documentar y comunicar al destinatario. Si IIC alto con Δ muy alto: el campo real coincidió con el declarado pero el nodo no actuó sobre sus consecuencias. También posible — documentar.

C3 · R*(adversarial ) ↔ R*(ajustado)

El vector R*(adversarial ) de Serie III debe ser consistente con R*(ajustado)

|R*(adversarial) _i − R*(ajustado)_i| ≤ 0.15 para el nodo principal de la atribución

Si la diferencia supera 0.15: el grafo adversarial incorporó cambios de estructura (aristas

Metrología Causal · Vol. II

Consistenci a

Relación que se verifica

Umbral de consistencia

Qué señala la violación

de Serie II: si el análisis adversarial se construye sobre R*(ajustado), la diferencia entre los dos vectores debe explicarse solo por el estándar adversarial más restrictivo, no por diferencias en la estructura del grafo.

eliminadas, nodos removidos) que van más allá del estándar adversarial. Verificar que la única diferencia entre el grafo ajustado y el adversarial es el estándar de evidencia admisible.

C4 · ρ(θ) ↔ amplitud de rangos

La función de robustez ρ(θ) debe ser consistente con la amplitud promedio de los rangos [a_ij, b_ij] del grafo adversarial: rangos más estrechos (evidencia más fuerte) deben

No hay umbral rígido. Señal de alerta: ρ(θ) < 0.70 con amplitud promedio de rangos < 0.10

Si ρ(θ) baja con rangos estrechos: la inestabilidad es estructural, no de evidencia. Significa que hay múltiples nodos con R* muy similar y cualquier variación pequeña cambia el ranking. Este es el caso de mayor incertidumbre

Metrología Causal · Vol. II

Consistenci a

Relación que se verifica

Umbral de consistencia

Qué señala la violación

producir ρ(θ) más alto. Una ρ(θ) baja con rangos estrechos es una señal de que el ranking es genuinamente inestable — el nodo principal es vulnerable a pequeñas variaciones de los parámetros.

genuina del sistema.

### III.  El protocolo de diagnóstico de inconsistencias

Cuando una o más de las cuatro consistencias se violan, el mediador no entrega el expediente. Ejecuta el protocolo de diagnóstico antes de continuar. El protocolo tiene tres pasos que se aplican a cada inconsistencia detectada.

El primer paso es clasificar la inconsistencia: ¿es aritmética, de calibración, o estructural? Una inconsistencia aritmética es un error de cálculo — un número equivocado en algún paso. Una inconsistencia de calibración es un parámetro (S, α, k, o los rangos) que no refleja correctamente la evidencia disponible. Una inconsistencia estructural es una propiedad del grafo que produce resultados matemáticamente válidos, pero interpretativamente

Metrología Causal · Vol. II

incompatibles — típicamente, un nodo mal clasificado o una arista mal dirigida.

El segundo paso es localizar el origen. Cada inconsistencia tiene un paso del protocolo donde se origina. La tabla del Paso 10 del Capítulo III·1 mapea las series a sus pasos — el mediador sigue esa traza hasta encontrar el paso específico donde la inconsistencia se introduce.

El tercer paso es corregir y reverificar. Una vez corregido el origen, el mediador repite todos los cálculos que dependen del parámetro corregido — incluyendo todos los pasos de todas las series que usan ese parámetro como insumo — y reverifica las cuatro consistencias sobre los resultados nuevos.

Diagnóstico rápido por tipo de inconsistencia

C1 violada (R* ajustado < R* base): origen aritmético en el Paso 8. Revisar la fórmula del ajuste de pesos: w_ij(ajustado) debe ser mayor que w_ij(base) cuando IIC < 1 y k > 0. Verificar que la renormalización de W(ajustado) se aplicó correctamente.

C2 extrema (IIC bajo con Δ muy bajo): origen de calibración de α. Revisar la Ruta B del nodo de diseño: los tres criterios (conocimiento, acción, oportunidad) pueden estar calibrados hacia arriba sin evidencia suficiente. O es un caso genuino de diseño erróneo de buena fe — documentar.

C3 violada (R* adversarial diverge de R* ajustado > 0.15): origen estructural en el grafo adversarial. El mediador introdujo cambios de estructura al construir el grafo adversarial que van más allá del estándar de evidencia. Solo se pueden eliminar aristas que no cumplen el estándar adversarial — no aristas que se podrían cuestionar por otras razones.

Metrología Causal · Vol. II

C4 con ρ(θ) bajo y rangos estrechos: no es un error — es una característica estructural del caso. El ranking es genuinamente inestable. Documentar en el reporte de sensibilidad y comunicar al destinatario como incertidumbre irreducible del análisis.

### IV.  La inconsistencia que no se corrige: el caso de incertidumbre genuina

Hay una situación donde la verificación cruzada detecta una inconsistencia que no tiene corrección: cuando múltiples nodos tienen valores de R* muy similares y cualquier variación razonable de los parámetros cambia el ranking. Esta situación no es un error del análisis — es una propiedad del sistema analizado: la responsabilidad causal está distribuida de manera tan homogénea entre varios nodos que no existe una diferencia estructural que el sistema pueda capturar con la evidencia disponible.

En ese caso, la verificación cruzada produce el diagnóstico correcto: incertidumbre estructural genuina. El expediente integrado documenta esa incertidumbre explícitamente, la Declaración de Serie III es nivel C o D, y el análisis narrativo comunica al destinatario que la distribución de responsabilidad en este caso no tiene un nodo principal claramente distinguible dado el nivel de evidencia disponible. Esa comunicación honesta es más valiosa para el destinatario que una falsa certeza producida por ignorar la incertidumbre.

Producto de salida · Capítulo III·2

Verificación cruzada completada: las cuatro consistencias C1–C4 verificadas con resultado documentado (consistente / inconsistente con diagnóstico). Si hay inconsistencias corregidas: los cálculos afectados repetidos y las consistencias reverificadas. Si hay incertidumbre genuina (C4

Metrología Causal · Vol. II

### estructural): documentada en el expediente integrado con su interpretación.

Notas al Capítulo III·2

1  La consistencia C2 entre Δ e IIC merece una clarificación conceptual importante. Δ y el IIC miden fenómenos relacionados pero distintos. Δ mide si el ego integró sus colapsos como propios mediante conducta verificable — es una medición de la segunda mediación φ□ desde afuera. El IIC mide si el campo que el ego de diseño prometió producir corresponde al campo que efectivamente produjo — es una medición de la congruencia entre el diseño declarado y el real. Son el mismo ego visto desde dos dimensiones: la asunción de sus actos (Δ) y la integridad de su diseño (IIC). Su relación es esperada pero no matemáticamente determinada — dos egos pueden tener patrones distintos y ambos ser internamente coherentes.

2  El protocolo de diagnóstico de tres pasos (clasificar → localizar → corregir y reverificar) tiene un costo que el mediador debe anticipar: una corrección en el Paso 3 (cálculo de R* base) invalida todos los cálculos de los Pasos 4 al 9. Cuando se detecta una inconsistencia de origen aritmético en pasos tempranos, el mediador repite el análisis desde ese paso. La verificación cruzada al final del protocolo previene que errores de pasos tempranos lleguen al expediente final — su costo es el tiempo de la reverificación, que es siempre menor que el costo de entregar un expediente incorrecto.

Metrología Causal · Vol. II

PARTE III · El análisis integrado: las tres series

### Capítulo III·3

### El expediente integrado completo

Qué documentos entrega, en qué formato y para qué audiencia

### I.  La arquitectura del expediente integrado

El expediente integrado consolida los resultados de las tres series en un conjunto ordenado de documentos. No es la yuxtaposición de tres expedientes separados: es un expediente único con una estructura interna que permite al destinatario acceder a cualquier nivel de detalle que su audiencia o su foro requiera, sin por ello renunciar a la coherencia del conjunto.

El expediente integrado tiene cuatro niveles de detalle. El nivel de resumen ejecutivo es accesible a cualquier audiencia — formula el resultado central del análisis en lenguaje del dominio del destinatario, sin referencias al aparato técnico del sistema. El nivel de documentos del análisis contiene los resultados formales de las tres series — es el nivel que el destinatario usa en el foro adversarial o en la reunión de dirección. El nivel de sustentación contiene la hoja de calibración y los reportes de sensibilidad — es el nivel que resiste el escrutinio técnico externo. El nivel de verificación contiene los registros de la verificación cruzada — es

Metrología Causal · Vol. II

### el nivel que el propio mediador consulta si el expediente es revisado con posterioridad.

### II.  Los documentos del expediente integrado

Nivel Contenido Audiencia principal

Docume nto

Resumen Una página. El resultado central del análisis en tres párrafos: qué ocurrió (estructura causal en lenguaje del dominio), quién responde y en qué proporción (distribución R* en términos absolutos si D_total está cuantificado), y qué se recomienda (hipótesis de prevención más relevantes + componentes del ajuste debitor si aplica). Sin fórmulas, sin referencias al aparato técnico.

1 · Resumen ejecutivo integrado

Dirección ejecutiva, junta de gobierno, destinatario no técnico

Análisis Tabla con R*(base), R*(ajustado) y R*(adversarial) para cada nodo, con sus componentes R*_neta, α y Δ. Columna de fuente de S y α. Análisis narrativo de la distribución: qué dice el vector sobre la estructura causal del sistema analizado.

2 · Vector R* comparati vo

Destinatari o principal, abogado litigante, regulador

Análisis Los protocolos declarados relevantes del nodo de diseño con sus c_k. El IIC global con su cálculo. La brecha entre el

3 · Mapa de brecha IIC

Regulador, auditor interno,

Metrología Causal · Vol. II

Nivel Contenido Audiencia principal

Docume nto

campo declarado y el real descrita en lenguaje del dominio. Aplicar solo si Serie II está en el análisis.

comité de compliance

Análisis Los tres componentes del ajuste debitor (estructural, procesal, reparatorio) con sus plazos verificables. Aplicar solo si Serie II está en el análisis.

4 · Ajuste debitor con cronogra ma

Consejo de administrac ión, directivo responsable , regulador

Análisis El nivel A/B/C/D con el enunciado formal completo. El valor exacto de ρ(θ) que lo sustenta. Aplicar solo si Serie III está en el análisis.

5 · Declaraci ón de robustez

Tribunal, árbitro, regulador, foro adversarial

6 · Hoja de calibració n (consolida da)

Sustentac ión

La hoja de calibración adversarial con todas las adiciones de Series II y III: nodo de diseño identificado, protocolos declarados con c_k, rangos adversariales con sus fuentes admisibles. Es el documento técnico completo que sustenta todos los resultados del expediente.

Experto contrario, revisor técnico, apelación

7 · Reporte de sensibilida d

Sustentac ión

La función ρ(θ) con los puntos de quiebre identificados y su interpretación. El mapa de estabilidad del ranking sobre el hipercubo. Aplicar solo si Serie III está en el análisis.

Experto contrario, tribunal técnico, revisión académica

8 · Registro de

Verificaci ón

Las cuatro consistencias C1– C4 con su resultado (consistente/diagnosticado/c

Revisión interna del expediente,

Metrología Causal · Vol. II

Nivel Contenido Audiencia principal

Docume nto

verificació n cruzada

orregido). Las correcciones aplicadas con su trazabilidad. La incertidumbre residual documentada si la hay.

auditoría de calidad del análisis

### III.  Qué documentos entrega cada combinación de series

No todas las combinaciones de series producen todos los documentos. La tabla siguiente especifica qué documentos forman el expediente según la combinación activada. Los documentos marcados como obligatorios deben estar presentes para que el expediente sea válido. Los marcados como condicionales se incluyen solo si la operación que los produce se activó.

Document o

Solo Serie I

Series I+II

Series I+III

Series I+II+III

Obligatorio Obligatori o

1 · Resumen ejecutivo

Obligatori o

Obligatori o

2 · Vector R* comparativ o

Solo R*(base)

R*(base) y R*(ajustad o)

R*(base) y R*(adversaria l)

Los tres vectores

No aplica Obligatori o

No aplica Obligatori o

3 · Mapa de brecha IIC

No aplica Obligatori o

No aplica Obligatori o

4 · Ajuste debitor

Metrología Causal · Vol. II

Document o

Solo Serie I

Series I+II

Series I+III

Series I+II+III

No aplica No aplica Obligatorio Obligatori o

5 · Declaración de robustez

Base Base + compliance

6 · Hoja de calibración

Base + adversarial

Base + complianc e + adversarial

No aplica No aplica Obligatorio Obligatori o

7 · Reporte de sensibilidad

C1 y C2 C3 y C4 C1, C2, C3 y C4

8 · Registro de verificación

Simplificad o

### IV.  El formato del expediente según el foro

Los ocho documentos del expediente integrado tienen un contenido invariante — lo que dicen no cambia según el foro. Lo que cambia es el orden en que se presentan, el nivel de detalle que se pone en primer plano, y el vocabulario del dominio que se usa en el análisis narrativo. Esta sección establece las tres configuraciones más frecuentes.

### Configuración A — Presentación ante tribunal o árbitro

### Orden: Declaración (5) → Vector R* comparativo (2) → Hoja de calibración (6) → Reporte de sensibilidad (7) → Resumen ejecutivo (1) como apéndice para el jurado no técnico.

Metrología Causal · Vol. II

Énfasis: la Declaración al frente porque es el documento que el foro evalúa primero. La hoja de calibración disponible para revisión técnica. El resumen ejecutivo como auxiliar para audiencias mixtas.

Vocabulario: usar el vocabulario jurídico del dominio en el análisis narrativo. R* se comunica como 'contribución causal proporcional'. S como 'estándar del sector' o 'práctica habitual'. Δ como 'brecha de diligencia debida'.

Configuración B — Presentación ante regulador o auditor

Orden: Resumen ejecutivo (1) → Mapa de brecha IIC (3) → Ajuste debitor (4) → Vector R* comparativo (2) → Hoja de calibración (6) → Registro de verificación (8).

Énfasis: el mapa de brecha IIC y el ajuste debitor al frente porque el regulador necesita la descripción del incumplimiento de diseño antes que la distribución de responsabilidad. La Declaración en el expediente solo si el foro regulatorio la requiere explícitamente.

Vocabulario: usar terminología de compliance y regulación. R* como 'peso en la distribución del riesgo'. IIC como 'índice de cumplimiento declarado vs. real'. Fraude annona como 'posición de responsabilidad institucional agravada'.

Configuración C — Presentación ante consejo de administración o dirección

Orden: Resumen ejecutivo (1) → Ajuste debitor (4) → Vector R* comparativo (2) → Hoja de calibración (6) en apéndice.

Metrología Causal · Vol. II

Énfasis: el resumen ejecutivo y el ajuste debitor son los documentos centrales para la toma de decisión de un consejo. La distribución R* informa, pero la pregunta práctica que el consejo necesita responder es qué debe cambiar en el diseño del sistema — eso está en el ajuste debitor.

Vocabulario: lenguaje de gestión y gobierno corporativo. R* como 'contribución causal al resultado'. Δ como 'brecha de asunción'. El ajuste debitor se presenta como 'plan de acciones correctivas con responsables y plazos'.

Producto de salida · Capítulo III·3

Expediente integrado completo en la configuración de presentación correcta para el foro del destinatario. Los ocho documentos están presentes según la combinación de series activas. El orden y el vocabulario reflejan la audiencia principal.

Notas al Capítulo III·3

1  El resumen ejecutivo de una página es el documento más difícil de producir del expediente integrado. Requiere que el mediador traduzca resultados técnicos precisos a lenguaje accesible sin perder la precisión de la atribución. La regla práctica: si el resumen ejecutivo puede ser malinterpretado de una manera que cambie la acción que el destinatario tomaría, necesita más precisión. Si añadir más precisión lo hace ilegible para la audiencia de dirección, necesita dos versiones: una ejecutiva y una técnica.

2  La hoja de calibración consolidada es el documento que determina si el expediente integrado puede ser reproducido independientemente por otro mediador con la misma evidencia. Una hoja de calibración bien construida contiene toda la información necesaria para que un par metodológico pueda verificar el análisis desde el principio. Esta propiedad de reproducibilidad es la condición de que el expediente sea un documento científico y no solo una opinión experta.

Metrología Causal · Vol. II

PARTE III · El análisis integrado: las tres series

### Capítulo III·4

### La comunicación del análisis integrado

Resumen ejecutivo, tribunal, regulador y consejo: cuatro registros del

mismo resultado

### I.  El problema de la comunicación técnica en foros no técnicos

El análisis integrado produce resultados matemáticamente precisos. La mayoría de los foros donde esos resultados importan no tienen formación matemática. El tribunal que evalúa una Declaración de nivel B no sabe qué es un hipercubo de parámetros. El consejo de administración que recibe un ajuste debitor no sabe qué es un eigenvector. El regulador que lee el mapa de brecha IIC no sabe qué es la primera mediación.

El problema no es simplificar el análisis hasta perder precisión — eso sería un error de comunicación que podría derivar en un error de decisión. El problema es encontrar el registro correcto para cada audiencia: el lenguaje que le permite al destinatario entender lo suficiente para tomar la decisión que el análisis informó, sin tener que aprender metrología causal para hacerlo. Ese registro existe en cada dominio. Este capítulo lo establece para los cuatro foros más frecuentes.

Metrología Causal · Vol. II

### II.  El resumen ejecutivo: estructura invariante

El resumen ejecutivo tiene la misma estructura en todos los casos y para todos los foros. Lo que cambia es el vocabulario. La estructura tiene tres párrafos que responden tres preguntas en ese orden exacto: qué ocurrió, quién responde y en qué proporción, y qué debe cambiar.

Estructura del resumen ejecutivo

Párrafo 1 — Qué ocurrió: una descripción del resultado D en términos del dominio del destinatario. Sin R*, sin vectores, sin fórmulas. La descripción establece el resultado específico que se analiza, su magnitud si está cuantificada, y el sistema de actores que lo produjo.

Párrafo 2 — Quién responde y en qué proporción: la distribución R* en lenguaje del dominio, reportando los nodos con R* más alto y su fracción del resultado. Si D_total está cuantificado: las fracciones AD_i. Si el análisis incluye Series II y III: una frase sobre la congruencia del diseño y una frase sobre el nivel de robustez de la atribución.

Párrafo 3 — Qué debe cambiar: las hipótesis de prevención más relevantes (de Serie I) y los componentes del ajuste debitor más urgentes (de Serie II si aplica). Formulados como condiciones de rediseño, no como instrucciones de conducta.

Extensión: una página. Si el caso tiene más nodos o más complejidad que una página permite, el resumen ejecutivo reduce la granularidad — reporta los tres nodos con mayor R*, no todos — y remite al Vector R* comparativo para el detalle completo.

### III.  El registro ante tribunal

Metrología Causal · Vol. II

La comunicación ante tribunal tiene dos audiencias simultáneas: el juez o panel técnico que evalúa la metodología, y el jurado o parte no técnica que necesita entender la conclusión. El expediente atiende a los dos en paralelo con documentos diferenciados.

Para el juez o panel técnico, los documentos centrales son la Declaración, la hoja de calibración y el reporte de sensibilidad. La comunicación oral del mediador sobre estos documentos debe ser precisa y sin rodeos: el nivel de Declaración, el valor de ρ(θ), los puntos de quiebre principales, y qué evidencia adicional cambiaría la Declaración de nivel. Un experto técnico que cuestiona el análisis recibe esta respuesta: los rangos [a_ij, b_ij] de la hoja de calibración son los rangos que la evidencia admisible en este foro justifica; si el experto contrario tiene evidencia adicional que estrecharía esos rangos, el hipercubo se reduce y ρ(θ) sube.

Para el jurado o parte no técnica, el documento central es el resumen ejecutivo en registro jurídico. Los términos clave tienen una traducción estándar que el mediador usa consistentemente a lo largo del proceso: R* se convierte en 'contribución causal proporcional verificada', S se convierte en 'probabilidad de que cualquier otro en esa posición hubiera actuado igual', Δ se convierte en 'fracción de esa contribución que el nodo no ha asumido como propia'.

La pregunta que el foro adversarial invariablemente formula y que el mediador debe poder responder en dos oraciones: ¿qué tendría que ser verdad para que su conclusión fuera incorrecta? La respuesta correcta no es defender la conclusión — es describir exactamente los puntos de quiebre del hipercubo: 'si el peso de la arista entre N_D y Nf fuera menor a 0.28, el nodo D ya no tendría el R* más alto'. Esa respuesta demuestra que el análisis conoce sus propios límites, lo que es más convincente que pretender que no los tiene.

Principio de comunicación adversarial del análisis causal

Metrología Causal · Vol. II

### IV.  El registro ante regulador

La comunicación ante regulador tiene énfasis diferente al tribunal. El regulador no evalúa si la atribución resiste una impugnación adversarial — evalúa si el diseño institucional que produjo el resultado debe ser modificado y cómo. Los documentos centrales son el mapa de brecha IIC y el ajuste debitor.

El registro regulatorio traduce el IIC como tasa de cumplimiento declarado versus real: un IIC de 0.38 se comunica como 'el sistema operó con 38% de congruencia respecto a sus estándares declarados'. El fraude annona se comunica como 'índice de responsabilidad institucional del diseño': un valor de 0.31 indica que el nodo de diseño concentra una posición de responsabilidad grave según los tres criterios del sistema (centralidad causal, asunción y congruencia).

El ajuste debitor se comunica en el registro regulatorio como un plan estructurado de tres componentes con plazos: qué protocolos deben rediseñarse (componente estructural), qué acciones deben tomarse de forma inmediata (componente procesal), y qué fracción del daño debe ser abordada (componente reparatorio). El regulador puede adoptar, modificar o rechazar cada componente de forma independiente.

### V.  El registro ante consejo de administración

La comunicación ante consejo tiene el registro más sintético. El consejo necesita tres respuestas: qué ocurrió, qué posición ocupa la organización en la distribución de responsabilidad, y qué debe decidir. Los documentos centrales son el resumen ejecutivo y el ajuste debitor en su componente estructural.

El vector R* se presenta ante el consejo como una tabla de tres columnas: nodo, fracción del resultado, y acción

Metrología Causal · Vol. II

recomendada. Para cada nodo con R* relevante: su contribución causal en porcentaje, si esa contribución es mayor o menor a la del ciclo anterior si hay seguimiento, y la acción del ajuste debitor que le corresponde. El consejo no necesita saber cómo se calculó R* — necesita saber qué decisión tomar sobre la base de R*.

La Declaración de robustez, si aplica, se comunica ante el consejo en términos de riesgo: 'la atribución tiene robustez sustancial (nivel B): en más del 90% de los escenarios consistentes con la evidencia disponible, la posición del nodo principal se mantiene'. Ese lenguaje le permite al consejo evaluar el riesgo de actuar sobre la base del análisis sin necesitar entender qué es un hipercubo.

Producto de salida · Capítulo III·4

Versión del expediente calibrada para el foro principal del destinatario: vocabulario del dominio en el análisis narrativo, documentos en el orden de la configuración correcta (A, B o C del Capítulo III·3), y resumen ejecutivo en el registro apropiado. Los documentos técnicos del nivel de sustentación están disponibles en apéndice para el escrutinio experto.

Notas al Capítulo III·4

Metrología Causal · Vol. II

porque demuestra que el análisis conoce sus propios límites con precisión. Un análisis que no puede responder esa pregunta no tiene robustez verificable. Un análisis que la responde con precisión — 'si el peso de esta arista fuera menor a X, el ranking cambiaría' — demuestra que la robustez fue calculada y no solo afirmada.

Metrología Causal · Vol. II

PARTE III · El análisis integrado: las tres series

### Capítulo III·5

### Los límites del expediente integrado

Qué puede responder el análisis y qué no puede responder por diseño

### I.  Por qué comunicar los límites es parte del protocolo

Un análisis que pretende responder más preguntas de las que puede responder con rigor es menos útil que uno que conoce sus límites con precisión. El destinatario que recibe un análisis sin límites explícitos no tiene manera de saber cuándo confiar en el resultado y cuándo buscar información adicional. El destinatario que recibe un análisis con sus límites claramente establecidos sabe exactamente qué preguntas el análisis responde con solidez, cuáles responde con incertidumbre documentada, y cuáles están fuera de su alcance por diseño.

Comunicar los límites no es una debilidad del análisis: es su forma de integridad metrológica. La metrología establece no solo qué mide un instrumento sino bajo qué condiciones es válida esa medición y cuándo deja de serlo. Este capítulo establece esas condiciones para el análisis integrado.

Metrología Causal · Vol. II

### II.  Lo que el expediente integrado puede responder

Pregunta Instrumento que la responde

Condición de validez

¿Quién fue condición necesaria de este resultado específico y en qué proporción?

Vector R*(base) de Serie I

El grafo incluye todos los nodos con capacidad causal. El resultado D está específicamente definido.

¿Cuánto del resultado es atribuible al actor específico vs. al campo que lo contenía?

R*_neta = R* × (1−S) de Serie I

S está correctamente derivado desde el Hijo dominante o los criterios universales con evidencia suficiente.

¿Cuánto causó cada nodo vs. cuánto asumió?

Δ = R* × (1−α) de Serie I

α está correctamente estimado desde Ruta A, B o C con evidencia documentada.

IIC de Serie II Los protocolos declarados del nodo de diseño están identificados y son verificables. El período analizado es el mismo que el del grafo base.

¿El nodo de diseño operó en conformidad con sus estándares declarados?

¿Qué fracción del daño corresponde causalmente a cada nodo?

AD_i = R* × D_total

D_total ha sido cuantificado por el destinatario en unidades consistentes.

Metrología Causal · Vol. II

Pregunta Instrumento que la responde

Condición de validez

¿Puede sostenerse la atribución ante impugnación con la evidencia disponible?

Declaración A/B/C/D de Serie III

El grafo adversarial refleja solo evidencia admisible en el foro. El hipercubo fue evaluado en todos los puntos requeridos.

¿Qué rediseño estructural reduciría la responsabilidad causal de los nodos críticos en sistemas futuros?

Hipótesis de prevención de Serie I + componente estructural del ajuste debitor de Serie II

Las hipótesis están ancladas en cambios verificables del grafo, no en instrucciones de conducta.

### III.  Lo que el expediente integrado no puede responder por diseño

Los límites del análisis no son limitaciones contingentes que una mejor evidencia o un análisis más extenso resolvería. Son límites estructurales del instrumento: preguntas que el sistema no está diseñado para responder, independientemente de la calidad de la evidencia o la extensión del análisis.

Pregunta que el análisis no responde

Por qué no la responde

Qué instrumento la respondería

¿El nodo tuvo intención de

El sistema mide responsabilidad causal estructural, no

Análisis jurídico de dolo y culpa. Historia clínica de

Metrología Causal · Vol. II

Pregunta que el análisis no responde

Por qué no la responde

Qué instrumento la respondería

producir el resultado?

intención. R* mide posición en el grafo — un nodo puede tener R* alto sin intención y R* bajo con intención plena. La intención es irrelevante para la causalidad y el sistema no la incorpora por diseño.

estado mental. Evaluación psicológica forense.

¿El resultado fue justo o injusto?

El sistema describe qué fue: quién causó qué, en qué proporción. No prescribe qué debe ser. La justicia del resultado — si la distribución es equitativa, si el daño merece reparación — es una pregunta normativa que el sistema informa pero no responde.

Análisis jurídico de equidad. Evaluación ética. Decisión de la autoridad competente.

¿Qué habría ocurrido si el sistema hubiera sido diseñado de manera diferente?

El sistema analiza el grafo real del caso analizado. Las hipótesis de prevención son condicionales estructurales sobre sistemas futuros similares — no son

Simulación de escenarios. Modelado prospectivo. Análisis de política comparada.

Metrología Causal · Vol. II

Pregunta que el análisis no responde

Por qué no la responde

Qué instrumento la respondería

contrafácticos sobre el caso analizado. La pregunta 'qué habría pasado si N_D hubiera diseñado diferente' no tiene respuesta con el mismo nivel de rigor que R*(base).

¿Cuánto vale el daño en unidades monetarias o de bienestar?

El sistema distribuye el daño en proporciones (AD_i = R*_i × D_total) pero no cuantifica D_total. La cuantificación del daño requiere instrumentos de valoración económica, actuarial o clínica que son externos al análisis causal.

Peritaje económico. Actuaría. Valoración de daños en jurisdicción competente.

¿El nodo va a repetir la conducta en el futuro?

El sistema describe la posición causal histórica del nodo. La predicción de conducta futura requiere un modelo prospectivo que el análisis causal no provee. Las hipótesis de prevención no son predicciones de conducta — son

Evaluación de riesgo de reincidencia. Análisis de trayectoria longitudinal (Tipo 5 del sistema).

Metrología Causal · Vol. II

Pregunta que el análisis no responde

Por qué no la responde

Qué instrumento la respondería

condiciones estructurales de rediseño.

¿El resultado fue evitable?

El sistema establece que el nodo fue condición necesaria del resultado — sin el nodo, el resultado no habría ocurrido en esa forma específica. Pero no establece si el nodo tenía la capacidad real de actuar diferente dado su estado interno en ese momento. Esa pregunta requiere acceso a v_t del nodo en el instante del colapso, que el expediente puede aproximar pero no determinar con certeza.

Evaluación psicológica del estado interno en el momento del acto. Análisis del SDO con ECO completo.

### IV.  El protocolo de comunicación de límites

Cuando el destinatario formula una pregunta que el análisis no puede responder, el mediador no intenta responderla con el instrumento equivocado. Comunica el límite con precisión y orienta al destinatario hacia el instrumento que sí puede responderla.

Metrología Causal · Vol. II

La comunicación del límite tiene tres componentes. El primero: confirmar que la pregunta es importante y legítima — no es un defecto del destinatario formularla. El segundo: explicar por qué el análisis causal no la responde — no por falta de evidencia sino por diseño del instrumento. El tercero: señalar qué instrumento externo al sistema respondería esa pregunta y qué información del expediente integrado ese instrumento necesitaría como insumo.

Este tercer componente es el más valioso para el destinatario. El análisis causal integrado no opera en el vacío: es un insumo para decisiones más amplias que requieren otros instrumentos. El mediador que conoce con precisión los límites del suyo está en posición de articular cómo se conecta con los demás — y esa articulación es parte del valor del análisis.

Ejemplo de comunicación de límite — la pregunta de intención

Pregunta del destinatario: '¿El director sabía que esto iba a pasar? ¿Lo hizo a propósito?'

Comunicación incorrecta: 'El análisis muestra que R* del director es 0.58, lo que indica alta responsabilidad causal. Eso sugiere que tuvo un papel central en el resultado.' (La respuesta usa R* para inferir intención, que es exactamente lo que R* no mide.)

Comunicación correcta: 'El análisis establece que el director fue condición necesaria del 58% del resultado — independientemente de su intención. Lo que el análisis no puede establecer es si el director tuvo intención de producir ese resultado: esa pregunta requiere un análisis jurídico de dolo o un peritaje psicológico forense. Lo que el expediente sí puede aportar a ese análisis externo es el mapa de oportunidades de conocimiento del director: los momentos documentados donde tenía información sobre el resultado potencial y las decisiones que tomó en cada uno.'

Metrología Causal · Vol. II

### Producto de salida · Capítulo III·5

Protocolo de comunicación de límites documentado en el expediente integrado: la tabla de lo que el análisis responde y lo que no responde, con los instrumentos externos que complementan el análisis causal para cada pregunta fuera de alcance. Este protocolo acompaña al resumen ejecutivo como apéndice de alcance del análisis.

Notas al Capítulo III·5

1  El límite más frecuentemente violado en la práctica es el de la intención. El análisis causal mide posición estructural — cuánto del resultado se explica por la posición del nodo en el grafo. Es tentador para el destinatario, y a veces para el propio mediador, interpretar R* alto como evidencia de intención. Esa interpretación es un error metrológico: R* alto puede coexistir con intención nula (un nodo que ocupa una posición estructural crítica sin ningún conocimiento de sus consecuencias) e intención alta puede coexistir con R* bajo (un nodo que quiso el resultado pero que no fue condición necesaria de él). La confusión entre causalidad e intención es uno de los errores más costosos que el análisis integrado puede producir si el mediador no comunica este límite con claridad.

2  El límite sobre la evitabilidad — si el resultado era evitable — tiene una relación especial con el parámetro α. α mide la asunción del acto: cuánto del acto el nodo integró como propio mediante conducta verificable. Un α bajo no significa que el resultado no era evitable — significa que el nodo no actuó sobre esa posibilidad. La pregunta de si el nodo podía actuar diferente dado su estado interno v_t en ese momento es una pregunta distinta que requiere acceso a la dimensión interior del ego. El SDO con ECO completo provee esa dimensión cuando está disponible. Cuando no lo está, α es la mejor aproximación exterior disponible.

3  La pregunta sobre qué habría ocurrido con un diseño diferente —el contrafáctico de diseño— tiene una respuesta parcial pero útil que el análisis sí puede proveer: las hipótesis de prevención de la Serie I. Estas hipótesis dicen qué cambio estructural en el grafo reduciría R* del nodo crítico en sistemas futuros similares. No son contrafácticos sobre el caso

Metrología Causal · Vol. II

analizado, pero son la mejor aproximación a 'qué habría cambiado si el sistema se hubiera diseñado diferente' que el análisis puede producir de forma rigurosa.

Metrología Causal · Vol. II

PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·1

### Los cuatro axiomas de la responsabilidad

### causal proporcional

Enunciado formal y justificación de cada axioma

### I.  La función del sistema axiomático

El Teorema de la Responsabilidad Causal Proporcional descansa sobre cuatro axiomas. Los axiomas no son hipótesis empíricas que pueden ser verificadas o refutadas con datos — son condiciones que cualquier distribución de responsabilidad debe satisfacer para ser interpretable como distribución de responsabilidad causal proporcional en el sentido de este sistema. Su función es doble: determinan de manera única la distribución correcta (el Capítulo IV·2 demuestra que solo el eigenvector las satisface simultáneamente) y permiten diagnosticar exactamente qué propiedad se viola cuando una distribución alternativa es propuesta.

Los cuatro axiomas son independientes entre sí: ninguno se sigue de los demás. Y son suficientes en conjunto: cualquier distribución que los satisface simultáneamente es el eigenvector. La demostración de ambas propiedades — independencia y suficiencia conjunta — forma el núcleo del Capítulo IV·2.

Metrología Causal · Vol. II

### II.  Axioma A1 — Eficiencia

Axioma A1 · Eficiencia

Σᵢ R*(i) = 1

La totalidad del resultado D está distribuida entre los nodos causalmente necesarios. Ninguna fracción se pierde ni se inventa.

La eficiencia exige que la distribución cierre: la suma de las responsabilidades causales de todos los nodos es exactamente el resultado total. No puede ser menor — eso significaría que parte del resultado no tiene origen causal asignado, lo que contradice que el grafo incluye todos los nodos causalmente relevantes. No puede ser mayor — eso significaría que el sistema atribuye más responsabilidad de la que el resultado contiene, lo cual es metrológicamente incoherente.

La eficiencia no es una convención aritmética de normalización. Es la condición de que el análisis causal es completo: si el grafo es correcto y todos los nodos causalmente relevantes están incluidos, la suma de sus pesos debe ser exactamente uno. Una distribución que no cumple A1 señala que el grafo está incompleto o que la distribución se calculó incorrectamente.

### III.  Axioma A2 — Causalidad necesaria

Axioma A2 · Causalidad necesaria

R*(i) > 0  □  i es condición sine qua non de D

El nodo i tiene responsabilidad causal positiva si y solo si su eliminación del grafo produce un resultado D' tal que D' ≠ D en su forma específica. Los nodos causalmente irrelevantes tienen R* = 0.

Metrología Causal · Vol. II

La causalidad necesaria vincula la distribución de responsabilidad a la estructura causal del grafo. Un nodo que no es condición necesaria de D — cuya eliminación dejaría D intacto — no tiene responsabilidad causal en D. Asignarle R* > 0 violaría el principio más básico de la causalidad: no se es responsable de algo que hubiera ocurrido igual sin uno.

La dirección inversa del bicondicional es igualmente importante: un nodo que sí es condición necesaria de D debe tener R* > 0. Una distribución que asigna R* = 0 a un nodo que es condición sine qua non viola A2, aunque sea aritméticamente coherente. Esta exigencia es la condición que previene que el análisis omita actores con alta responsabilidad estructural por razones extra-metodológicas.

### IV.  Axioma A3 — Centralidad recursiva

Axioma A3 · Centralidad recursiva

R*(i) es proporcional a Σ□ w_ij · R*(j)

La responsabilidad de un nodo es proporcional a la suma ponderada de las responsabilidades de los nodos sobre los que ejerce influencia causal. La responsabilidad se propaga recursivamente a través de toda la estructura del grafo.

La centralidad recursiva captura la dimensión más importante de la responsabilidad en sistemas complejos: que la influencia no es solo directa. Un nodo que influye sobre nodos intermedios que a su vez influyen sobre el resultado final tiene responsabilidad causal que va más allá de sus aristas directas al nodo sumidero. El diseñador que produce el incentivo que produce la conducta que produce el daño es responsable no solo de su arista directa al daño sino de toda la cadena causal que su diseño habilitó.

Metrología Causal · Vol. II

Sin la centralidad recursiva, el análisis causal sería superficial: mediría quién actuó en el último paso, ignorando quién construyó el sistema que hizo posible ese último paso. A3 es el axioma que hace al sistema capaz de identificar la responsabilidad estructural de los nodos de diseño, que frecuentemente no tienen aristas directas al resultado, pero tienen R* alto porque su influencia se ejerce a través de múltiples niveles del grafo.

### V.  Axioma A4 — Monotonicidad

Axioma A4 · Monotonicidad

Si w_ji aumenta → R*(i) no decrece

Si la influencia del nodo j sobre el nodo i se intensifica, la responsabilidad causal de i no puede disminuir. Más influencia causal recibida no reduce la centralidad causal del receptor.

La monotonicidad es la condición de coherencia ordinal del sistema. Si un nodo recibe más influencia causal de otros nodos, su posición causal en el resultado no puede ser menor que antes. Una distribución que viola A4 produciría la paradoja de que un nodo con más influencia sobre el resultado tiene menos responsabilidad, lo que contradice el principio de que la responsabilidad causal crece con la influencia estructural.

A4 también tiene una consecuencia importante para el análisis de sensibilidad de la Serie III: cuando los pesos del grafo varían dentro de sus rangos admisibles, el ranking de los nodos solo puede cambiar de maneras consistentes con la monotonicidad. Un nodo no puede ganar influencia y perder posición en el ranking simultáneamente.

Metrología Causal · Vol. II

Axioma Nombre Condición Lo que viola si se relaja

A1 Eficiencia Σᵢ R*(i) = 1 La distribución no cubre todo el resultado o lo excede. El análisis es incompleto o sobrecontribuyente.

A2 Causalidad necesaria

R*(i) > 0 □ condición sine qua non

Nodos irrelevantes reciben responsabilidad, o nodos necesarios son ignorados. El vínculo entre causalidad y responsabilidad se rompe.

A3 Centralidad recursiva

R*(i) □ Σ□ w_ij · R*(j)

La responsabilidad es solo directa. Los nodos de diseño con influencia indirecta son invisibles al análisis.

A4 Monotonicidad ↑w_ji □ R*(i) no decrece

Más influencia produce menos responsabilidad. El análisis viola coherencia ordinal básica.

### Producto de salida · Capítulo IV·1

Los cuatro axiomas formalmente enunciados con su justificación. Cualquier distribución de responsabilidad causal proporcional debe satisfacerlos simultáneamente. El Capítulo IV·2 demuestra que exactamente una distribución los satisface: el eigenvector principal normalizado de W.

Notas al Capítulo IV·1

1  La independencia de los cuatro axiomas puede verificarse mostrando que para cada axioma existe una distribución que satisface los tres restantes,

Metrología Causal · Vol. II

pero viola ese axioma específico. Para A3: la distribución de pesos directos al sumidero (sin propagación recursiva) satisface A1, A2 y A4, pero viola A3. La demostración completa de independencia está en el apéndice de la Axiomatización del Sistema de la Doble Mediación.

2  El axioma A2 formula la condición sine qua non en términos de forma específica del resultado: 'D' ≠ D en su forma específica'. Esta precisión es metrológicamente crítica. Si un nodo es eliminado del grafo y el resultado ocurre con menor magnitud, pero la misma forma, el nodo no es condición sine qua non bajo A2. Si el resultado ocurre en una forma diferente, sí lo es. La distinción entre magnitud y forma del resultado tiene consecuencias directas para la aplicación en dominios donde la forma del resultado importa más que su magnitud.

Metrología Causal · Vol. II

PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·2

### Teorema de la Responsabilidad Causal

### Proporcional

Existencia, unicidad y demostración

### I.  El enunciado del teorema

Teorema de la Responsabilidad Causal Proporcional

Sea G = (N, E, W) un grafo causal dirigido con matriz de adyacencia ponderada W ≥ 0 e irreducible sobre N□{Nf}, donde Nf es el nodo sumidero que representa el resultado D.

Existe una única distribución R*: N → [0,1] con Σᵢ R*(i) = 1 que satisface simultáneamente los axiomas A1, A2, A3 y A4.

Esa distribución es el eigenvector principal normalizado de W: el único vector positivo v tal que W·v = λ_max·v, normalizado para que ||v||□ = 1.

### II.  Lema previo: el Teorema de Perron-Frobenius

Metrología Causal · Vol. II

La demostración del teorema descansa sobre el Teorema de Perron-Frobenius para matrices no negativas e irreducibles. El lema que este capítulo usa en su forma operativa es el siguiente.

Lema PF (Perron-Frobenius, forma operativa)

Sea W una matriz cuadrada n×n con entradas no negativas (W ≥ 0) e irreducible. Entonces:

(i) W tiene un eigenvalor real positivo λ_max > 0, estrictamente mayor que el módulo de cualquier otro eigenvalor: λ_max > |λᵢ| para todo i ≠ max.

(ii) El eigenvector correspondiente a λ_max es único (salvo escala) y tiene todas sus entradas estrictamente positivas: v_i > 0 para todo i.

(iii) El método de potencias converge a v desde cualquier vector inicial positivo: W^k·u / ||W^k·u||₁ → v cuando k → ∞.

La irreducibilidad de W es la condición que garantiza las tres propiedades del lema. Un grafo es irreducible si y solo si su matriz de adyacencia es irreducible — es decir, si desde cualquier nodo existe un camino dirigido al nodo sumidero Nf. Esta es exactamente la condición de completitud del grafo verificada en el Paso 2 del protocolo.

### III.  Demostración: el eigenvector satisface los cuatro axiomas

La primera parte muestra que la distribución eigenvectorial satisface A1, A2, A3 y A4.

A1 — Eficiencia: el eigenvector v está normalizado por construcción: ||v||□ = Σᵢ v_i = 1. La normalización en la norma ℓ¹ asegura exactamente que la suma de todas las entradas es uno.

Metrología Causal · Vol. II

R*(i) = v_i / ||v||□ satisface A1 por definición del procedimiento de normalización.

A2 — Causalidad necesaria: por el lema PF(ii), todas las entradas del eigenvector son estrictamente positivas: v_i > 0 para todo i. Esto significa que todo nodo del grafo tiene R* > 0. La dirección '→' (si R* > 0 entonces condición necesaria) se garantiza porque el grafo por construcción contiene solo nodos causalmente relevantes para D. La dirección '←' (si es condición necesaria entonces R* > 0) se satisface por PF(ii).

A3 — Centralidad recursiva: la ecuación eigenvectorial W·v = λ_max·v dice exactamente que v_i = (1/λ_max) · Σ□ w_ij · v_j. Es decir: el valor de v_i es proporcional a la suma ponderada de los valores v_j de los nodos sobre los que i ejerce influencia. Esto es exactamente A3. La ecuación eigenvectorial es la forma matricial de A3.

A4 — Monotonicidad: si el peso w_ji aumenta, la entrada (W)_ji de la matriz W aumenta. Por el teorema de Perron para matrices con entradas no negativas, el eigenvalor principal λ_max es una función creciente de cada entrada de W. Y la entrada v_i del eigenvector principal es proporcional a la suma de los pesos de las aristas que entran a i, ponderados por los valores eigenvectoriales de sus fuentes — por lo tanto, v_i no puede decrecer cuando w_ji aumenta.

### IV.  Demostración: unicidad por relajación de axiomas

La segunda parte demuestra que relajar cualquier axioma permite distribuciones distintas del eigenvector que satisfacen los tres axiomas restantes.

Si se relaja A1: la distribución v' = 2·v satisface A2, A3 y A4 pero tiene Σ v'_i = 2 ≠ 1. Cualquier múltiplo escalar positivo del

Metrología Causal · Vol. II

eigenvector satisface A2–A4, pero no A1. La normalización ℓ¹ selecciona el único representante que satisface A1.

Si se relaja A2: la distribución que asigna R* = 0 al nodo de mayor eigenvector y distribuye su peso uniformemente entre los demás satisface A1, A3 (modificada) y A4, pero viola A2 porque un nodo causalmente necesario tiene R* = 0.

Si se relaja A3: cualquier distribución proporcional al grado de salida (número de aristas salientes de cada nodo, sin ponderación recursiva) satisface A1, A2 y A4, pero viola A3 porque ignora la propagación recursiva de la influencia.

Si se relaja A4: la distribución que invierte el ranking del eigenvector satisface A1 y A2, pero viola A4 porque los nodos con mayor influencia recibida tienen menor responsabilidad. Los cuatro casos muestran que cada axioma excluye una familia de distribuciones distintas del eigenvector. Juntos, los cuatro no dejan lugar para ninguna otra distribución.

La demostración por unicidad desde la relajación de axiomas no solo prueba que el eigenvector es la respuesta correcta: muestra con precisión por qué cada axioma es necesario. Un sistema que propone una distribución de responsabilidad distinta del eigenvector está, explícitamente, violando al menos uno de los cuatro axiomas. Identificar cuál axioma viola una distribución alternativa permite al mediador articular exactamente en qué sentido esa alternativa es metodológicamente inadecuada.

Función de la demostración por unicidad en el contexto adversarial

### V.  La condición de irreducibilidad: qué pasa si no se cumple

El teorema requiere que W sea irreducible. Si el grafo tiene nodos desde los que no existe camino al sumidero, W es reducible

Metrología Causal · Vol. II

y el eigenvector principal puede no ser único o puede no tener todas sus entradas positivas.

El protocolo maneja esta situación en el Paso 2 del análisis: cualquier nodo sin camino al sumidero se elimina del grafo antes del cálculo. Con esa eliminación, la submatriz resultante es irreducible y el teorema aplica. Los nodos eliminados tienen R* = 0 por A2 — no son condición necesaria de D.

Producto de salida · Capítulo IV·2

Demostración completa del Teorema de la Responsabilidad Causal Proporcional: el eigenvector principal normalizado de W es la única distribución que satisface A1–A4 simultáneamente. La demostración tiene dos partes: satisfacción directa de los cuatro axiomas (por verificación con el lema PF) y unicidad (por demostración desde relajación de axiomas).

Notas al Capítulo IV·2

1  La demostración de A2 presenta una sutileza técnica: el lema PF garantiza que todas las entradas del eigenvector son positivas cuando la matriz es irreducible. Pero la condición A2 exige que las entradas sean positivas exactamente para los nodos sine qua non, y cero para los que no lo son. La reconciliación es que el protocolo elimina del grafo los nodos no-sine-qua-non antes del cálculo. Con esa eliminación, todos los nodos presentes son sine qua non y el eigenvector les asigna entradas positivas.

Metrología Causal · Vol. II

PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·3

### Corolario I · La descomposición de R*

Derivación formal de R*_neta y R*_sistémica desde el teorema

principal

### I.  La pregunta que el corolario responde

El teorema principal establece que R*(i) mide la contribución causal estructural del nodo i al resultado D. Esta medición no distingue entre dos fuentes de esa contribución que son metrológicamente distintas: la parte que proviene del ego específico del nodo y la parte que habría producido cualquier otro actor en esa misma posición estructural. El Corolario I formaliza esa descomposición.

### II.  La definición de S como operador de descomposición

S_i □ [0,1] mide la probabilidad de que cualquier otro nodo con el mismo perfil en la misma posición estructural que i hubiera producido el mismo resultado. S_i = 1 significa que el acto era completamente determinado por el campo. S_i = 0 significa que el acto era completamente idiosincrático.

Metrología Causal · Vol. II

La interpretación ontológica de S está en el Capítulo I·4 de este volumen: S_i es la lectura exterior de la posición de v_t en φ□ del ego i. Cuando c domina φ□ (S alto), el acto emerge principalmente del campo heredado. Cuando v_t domina φ□ (S bajo), el acto emerge principalmente de la posición propia de la voluntad.

### III.  La derivación del Corolario I

Corolario I · Descomposición de R*

Dado el Teorema IV·2 y la definición de S_i como la fracción de R*(i) atribuible al campo c:

R*_neta_i = R*(i) × (1 − S_i) [fracción idiosincrática]

R*_sistémica_i = R*(i) × S_i [fracción del campo]

R*(i) = R*_neta_i + R*_sistémica_i

La descomposición es exhaustiva: los dos componentes suman exactamente R*(i). La fracción idiosincrática mide cuánto del peso causal de i es atribuible a ese ego específico. La fracción sistémica mide cuánto habría producido cualquier otro en esa posición.

La derivación es directa desde el teorema y la definición de S. R*(i) es la responsabilidad causal total del nodo i. S_i es la fracción de esa responsabilidad que el campo explica. Por tanto (1 − S_i) es la fracción que el ego específico explica. R*_neta_i = R*(i) × (1 − S_i) es esa fracción idiosincrática — el producto de la responsabilidad total por la proporción que no puede explicarse por el campo.

### IV.  Propiedades de la descomposición

Metrología Causal · Vol. II

Propiedad 1 — Σᵢ R*_neta_i ≤ 1: la suma de las fracciones idiosincráticas de todos los nodos es siempre menor o igual a uno. La diferencia 1 − Σᵢ R*_neta_i = Σᵢ R*_sistémica_i es la responsabilidad sistémica total del campo c.

Propiedad 2 — R*_neta_i = 0 cuando S_i = 1: si el acto del nodo era completamente predecible desde el campo, su fracción idiosincrática es cero. El nodo tiene R*(i) > 0 (fue condición necesaria del resultado) pero R*_neta_i = 0 (cualquier otro habría producido lo mismo). Esta es la posición del ejecutor completamente sustituible.

Propiedad 3 — R*_neta_i = R*(i) cuando S_i = 0: si el acto era completamente idiosincrático, toda la responsabilidad causal es atribuible al ego específico. Nadie más en esa posición habría producido ese resultado.

Producto de salida · Capítulo IV·3

Corolario I formalmente derivado: la descomposición R*(i) = R*_neta_i + R*_sistémica_i con sus tres propiedades. La fracción idiosincrática R*_neta_i = R*(i) × (1−S_i) es la medida de responsabilidad causal que el sistema atribuye al ego específico, excluyendo la parte que cualquier otro en esa posición también habría producido.

Notas al Capítulo IV·3

Metrología Causal · Vol. II

2  La distinción entre R*_neta y R*_sistémica tiene un paralelo directo con la distinción jurídica entre responsabilidad individual y responsabilidad institucional. R*_neta corresponde aproximadamente a la responsabilidad del individuo por encima y más allá del estándar del sistema. R*_sistémica corresponde a la responsabilidad de quien diseñó el sistema que produjo el comportamiento del individuo.

Metrología Causal · Vol. II

PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·4

### Corolario II · El déficit de asunción Δ

Derivación formal del déficit desde el teorema principal

### I.  La pregunta que el corolario responde

El Corolario I descompone R* entre la fracción del ego y la fracción del campo. El Corolario II aborda una segunda dimensión: la brecha entre lo que el nodo causó (R*) y lo que el nodo integró como propio mediante conducta verificable (α). Esta brecha — el déficit de asunción Δ — es la medida de cuánto del impacto causal del nodo no fue reconocido ni abordado por ese nodo.

### II.  La definición de α como operador de integración

α_i □ [0,1] mide la fracción de R*(i) que el nodo i integró como propia mediante acciones verificables orientadas a producir, modificar o mitigar el resultado. α_i = 1 significa asunción completa. α_i = 0 significa que el nodo no asumió nada a pesar de haber sido condición necesaria del resultado.

Metrología Causal · Vol. II

La interpretación ontológica de α es el grado en que la segunda mediación φ□ operó sobre los colapsos del nodo: cuánto de lo que φ□ produjo fue integrado en I(t) como parte constitutiva del ego. La relación entre α y φ□ es una derivación formal establecida en La transformación formal (Cap. 2.3).

### III.  La derivación del Corolario II

Corolario II · El déficit de asunción

Dado el Teorema IV·2 y la definición de α_i como la fracción de R*(i) que el nodo i integró como propia:

Δ_i = R*(i) × (1 − α_i) [déficit de asunción del nodo i]

Δ_total = Σᵢ Δ_i [déficit sistémico de asunción]

Δ_i mide la fracción de R*(i) que el nodo causó, pero no integró como propia. Δ_i > 0 indica déficit. Δ_i < 0 indica inversión causal: el nodo asumió más de lo que causó. Δ_i = 0 indica equilibrio.

### IV.  Los tres casos de Δ y su interpretación

Interpretación operativa

Signo de Δ_i

Condición formal

Nombre del patrón

Δ_i > 0 R*(i) > α_i · R*(i)

Déficit de asunción

El nodo causó más de lo que asumió. La brecha puede originarse en evasión deliberada (φ□ capaz pero no ejercida) o en bloqueo ontológico (φ□ estructuralmente impedida).

Metrología Causal · Vol. II

Interpretación operativa

Signo de Δ_i

Condición formal

Nombre del patrón

El SDO distingue los dos casos.

Δ_i = 0 α_i = 1 o R*(i) = 0

Equilibrio de asunción

El nodo asumió exactamente lo que causó. El equilibrio puede ocurrir en cualquier punto de la escala.

Δ_i < 0 α_i · R*(i) > R*(i)

Inversión causal

El nodo asumió más de lo que el análisis le asigna. Puede indicar chivo expiatorio (asume responsabilidad ajena) o vanguardia de asunción (integra su contribución antes de que el campo la reconozca).

### V.  Δ y los dos orígenes del déficit

Cuando Δ_i > 0, la brecha tiene dos orígenes estructuralmente distintos. El primero es la evasión: φ□ tiene la capacidad de operar sobre el colapso, pero el ego elige no ejercerla. Desde el exterior, la evasión se manifiesta como α bajo en presencia de los tres criterios de la Ruta B: el nodo tenía conocimiento, capacidad de acción, y oportunidades verificadas de actuar diferente.

El segundo origen es el bloqueo ontológico: φ□ no tiene la capacidad de operar en este momento porque el estado de I(t) del ego no lo permite. Desde el exterior, el bloqueo se manifiesta como α bajo en ausencia del criterio de conocimiento. El SDO accede a esta dimensión interior; el análisis forense no puede hacerlo.

Metrología Causal · Vol. II

### Producto de salida · Capítulo IV·4

Corolario II formalmente derivado: Δ_i = R*(i) × (1 − α_i) con sus tres casos y su interpretación. Δ_total = Σᵢ Δ_i como medida del déficit sistémico. La distinción entre los dos orígenes del déficit (evasión y bloqueo ontológico) como guía para la intervención y el acompañamiento.

Notas al Capítulo IV·4

1  La imposibilidad matemática de α_i > 1 cierra el corolario con precisión: un nodo no puede asumir más del 100% de su responsabilidad causal. Si la calibración de α produce α_i > 1, hay un error de calibración — el criterio de acción de la Ruta B se aplicó sobre un denominador incorrecto.

2  El caso Δ < 0 (inversión causal) tiene una interpretación asimétrica importante. Si el Δ negativo se debe a que el nodo asumió la responsabilidad del nodo de diseño (chivo expiatorio), el análisis preventivo debe señalar ese patrón explícitamente: el rediseño que previene el resultado debe redistribuir la responsabilidad desde el ejecutor hacia el diseñador, no solo exigir más asunción del ejecutor.

Metrología Causal · Vol. II

PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·5

### Corolario III · El fraude annona

Derivación formal como identidad matemática desde R*, α e IIC

### I.  El fraude annona como caso específico del Corolario II

El Corolario II establece el déficit de asunción Δ para cualquier nodo del grafo. El Corolario III aplica el mismo marco al nodo de diseño institucional incorporando una tercera dimensión que solo es relevante para ese nodo: la congruencia entre el campo que declaró que produciría y el campo que efectivamente produjo.

El fraude annona es una identidad matemática — una cantidad que se deriva directamente de R*, α e IIC sin supuestos adicionales. Es el Corolario II aplicado al nodo de diseño con el IIC como modulador de la fracción de Δ que proviene de la brecha de congruencia.

### II.  El papel del IIC en la derivación

Metrología Causal · Vol. II

El IIC_D del nodo de diseño mide la correlación entre el campo que N_D declaró que produciría y el campo que efectivamente produjo. Cuando IIC es bajo, la brecha de congruencia genera por sí misma una fracción de Δ — incluso si el nodo hubiera actuado con α moderado, la divergencia entre su diseño declarado y su operación real amplía el déficit efectivo.

Un nodo que diseña un protocolo prometiendo ciertos resultados y luego opera el sistema de manera diferente no solo tiene el Δ de la asunción que cualquier nodo puede tener. Tiene además la brecha entre lo que prometió y lo que hizo — que amplifica su Δ en proporción a la magnitud de esa divergencia.

### III.  La derivación del Corolario III

Corolario III · El fraude annona

Sea N_D el nodo de diseño con R*_D > 0, α_D □ [0,1] e IIC_D □ [0,1]:

Fraude_annona_D = R*_D × (1 − α_D) × (1 − IIC_D)

El fraude annona es el Corolario II aplicado al nodo de diseño con (1 − IIC_D) como el factor que amplifica el déficit de asunción en función de la brecha de congruencia del diseño. Es equivalente a Δ_efectivo_D = Δ_D × (1 − IIC_D).

### IV.  Las propiedades formales

Propiedad 1 — Fraude annona □ [0,1]: los tres factores son no negativos y menores o iguales a uno, por lo que su producto también lo es.

Propiedad 2 — El máximo se alcanza en el vértice (R*_D = 1, α_D = 0, IIC_D = 0): el nodo de diseño es el único responsable

Metrología Causal · Vol. II

### del resultado, no ha asumido nada, y su campo real va en dirección opuesta al declarado. Esta es la posición más grave que el sistema puede medir.

Propiedad 3 — El fraude annona es cero en tres casos independientes: R*_D = 0 (no causalmente relevante), α_D = 1 (asunción completa), o IIC_D = 1 (congruencia plena). En cualquiera de los tres casos, no hay fraude annona independientemente de los otros factores. La figura más grave requiere los tres factores simultáneamente.

R*_D α_D IIC_D Fraude annona

Interpretación

### 0.60 0.10 0.20 0.432 Posición grave. Alta centralidad, baja asunción, baja congruencia. El diseño es el factor dominante y operó muy diferente a lo declarado.

### 0.60 0.60 0.20 0.192 Posición moderada. Alta centralidad, asunción moderada. La congruencia sigue baja pero la asunción parcial reduce el fraude annona.

### 0.60 0.10 0.80 0.108 Posición baja-moderada. Alta centralidad y baja asunción, pero el campo real es mayormente congruente con el declarado.

### 0.20 0.10 0.20 0.144 A pesar de R* moderado, la combinación de baja asunción y baja congruencia supera el umbral de 0.20.

### Producto de salida · Capítulo IV·5

Metrología Causal · Vol. II

Corolario III formalmente derivado: Fraude_annona_D = R*_D × (1−α_D) × (1−IIC_D) con sus tres propiedades. El umbral de acción 0.20 corresponde al punto donde la combinación de los tres factores es suficientemente significativa para activar requisitos formales de intervención en la mayoría de los dominios regulatorios.

Notas al Capítulo IV·5

1  El nombre fraude annona proviene del derecho romano: la annona era la gestión del abastecimiento de grano de Roma, y el fraudator annonae era el funcionario que adulteraba o desviaba el suministro de un bien esencial. La analogía con el nodo de diseño institucional moderno es precisa: quien diseña un sistema de salud, crédito, educación o justicia está gestionando un bien esencial. El fraude annona causal mide qué tanto ese gestor prometió una calidad de servicio que no entregó.

2  La relación formal entre el Corolario III y el Corolario II merece explicitarse: el fraude annona es el Δ efectivo del nodo de diseño. Δ_efectivo_D = Δ_D × (1 − IIC_D) = R*_D × (1−α_D) × (1−IIC_D). La baja congruencia del diseño amplifica el déficit de asunción porque el nodo no solo no asumió su responsabilidad — prometió controles que no implementó, amplificando el daño de su déficit.

Metrología Causal · Vol. II

PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·6

### Extensión al caso acumulativo

El valor de Shapley cuando ningún nodo es condición sine qua non

individual

### I.  El límite del Teorema IV·2

El Teorema de la Responsabilidad Causal Proporcional requiere que al menos un nodo del grafo sea condición sine qua non individual de D. Hay sistemas causales complejos donde esta condición no se cumple: el resultado emerge de la intersección de múltiples contribuciones ninguna de las cuales es individualmente necesaria. En esos sistemas, el axioma A2 no puede cumplirse en su formulación original.

En esos sistemas, el eigenvector sigue siendo matemáticamente calculable, pero su interpretación como responsabilidad causal proporcional pierde el fundamento que A2 le provee. Este capítulo establece qué distribución aplica en ese caso.

### II.  La función característica del juego cooperativo asociado

Metrología Causal · Vol. II

Cuando ningún nodo es condición sine qua non individual, el sistema causal se modela como un juego cooperativo. El juego tiene como jugadores los nodos de N (excluyendo Nf) y como función característica v: 2^N → [0,1] donde v(S) mide la fracción del resultado D que la coalición S puede producir por sí sola.

Función característica v(S)

v(S) = fracción de D que la submatriz W_S (restringida a nodos en S) produce en Nf

v (□) = 0 (la coalición vacía no produce nada) · v(N□{Nf}) = 1 (todos los nodos producen todo D). v(S) se calcula como el eigenvector principal de W_S normalizado sobre Nf.

### III.  El valor de Shapley como distribución de responsabilidad

El valor de Shapley φᵢ de cada nodo i es su contribución marginal promedio sobre todas las coaliciones posibles. Mide cuánto agrega cada nodo al resultado cuando se une a una coalición que ya existía, promediado sobre todos los órdenes posibles.

Valor de Shapley

φᵢ = Σ_ {¡S ⊆ ¡N∖ {i, Nf}} [|S|! · (n−|S|−1)! / n!]  × [v(S∪{i}) − v(S)]

n = |N□{Nf}| es el número de nodos sin el sumidero. El factor combinatorio es la probabilidad de que S sea exactamente el conjunto de nodos que precedieron a i en un orden aleatorio.

El valor de Shapley satisface cuatro axiomas propios: eficiencia (los valores suman v(N)), simetría (nodos con contribuciones idénticas reciben valores idénticos), nulidad (nodos

Metrología Causal · Vol. II

### que no contribuyen a ninguna coalición reciben cero), y aditividad. En el caso acumulativo, estos axiomas determinan de manera única la distribución Shapley.

### IV.  El Shapley como caso límite del eigenvector

La relación entre el eigenvector y el valor de Shapley no es de oposición sino de continuidad. El valor de Shapley es el caso límite del eigenvector cuando la condición sine qua non individual se debilita hacia cero. Esta continuidad tiene una consecuencia práctica: en grafos donde la condición se cumple para algunos nodos, pero no para todos, los dos métodos producen valores similares.

Característica Eigenvector (caso s.q.n.)

Valor de Shapley (caso acumulativo)

Condición de aplicación

Al menos un nodo es condición sine qua non individual

Ningún nodo es condición sine qua non individual

Axiomas A1 eficiencia, A2 causalidad necesaria, A3 centralidad recursiva, A4 monotonicidad

Eficiencia, simetría, nulidad, aditividad

Complejidad O(n²·k) con k iteraciones. Eficiente para grafos grandes.

O(2ⁿ) exacto. Para n > 20 requiere métodos de aproximación.

Corolarios derivados

R*_neta, Δ, fraude annona — todos válidos

R*_neta y Δ son válidos con Shapley como base. Fraude annona requiere adaptación del IIC.

Metrología Causal · Vol. II

### Producto de salida · Capítulo IV·6

Extensión del Teorema IV·2 al caso acumulativo: el valor de Shapley φᵢ como la distribución de responsabilidad cuando ningún nodo es condición sine qua non individual. La función característica v(S) del juego cooperativo asociado al grafo G. El Shapley como caso límite del eigenvector con sus axiomas propios.

Notas al Capítulo IV·6

1  La complejidad computacional O(2ⁿ) del valor de Shapley exacto es una limitación práctica para grafos grandes. Los métodos de aproximación más eficientes son: (a) muestreo de permutaciones aleatorias — calcular la contribución marginal de cada nodo en K permutaciones aleatorias y promediar, con error que decrece como 1/√K; y (b) el algoritmo de Strömberg (2018) que calcula Shapley en tiempo O(n·2^(n/2)) para estructuras con independencia condicional.

2  La relación entre el eigenvector y el Shapley tiene un precedente en la literatura relevante para la Conjetura del Operador Unificador del Capítulo IV·7. Teng (2016) demuestra que el PageRank puede interpretarse como el valor de Shapley de un juego de influencia social específico. Si esa relación puede generalizarse al grafo causal ponderado de este sistema, el eigenvector y el Shapley serían instancias del mismo operador con diferentes funciones características.

Metrología Causal · Vol. II

PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·7

### La conjetura del operador unificador

Programa de investigación: un operador que produce eigenvector o

Shapley según la estructura del grafo

### I.  El problema que la conjetura formula

Los Capítulos IV·2 y IV·6 establecen dos distribuciones de responsabilidad para dos tipos de grafo: el eigenvector cuando hay condición sine qua non individual, el Shapley cuando no la hay. Ambos métodos son matemáticamente sólidos y sus condiciones de aplicación están claramente delimitadas. La conjetura del operador unificador es la afirmación de que existe un operador único que produce la distribución correcta en ambos casos y en los casos mixtos.

### II.  El enunciado formal de la conjetura

Conjetura del Operador Unificador (C.O.U.)

Sea C la clase de grafos causales dirigidos ponderados G = (N, E, W) con W ≥ 0. Existe un operador O: C → □^|N| tal que: Metrología Causal · Vol. II

### (i) Cuando G tiene al menos un nodo condición sine qua non individual: O(G) = eigenvector principal normalizado de W.

### (ii) Cuando ningún nodo de G es condición sine qua non individual: O(G) = valor de Shapley del juego cooperativo v(S) asociado a G.

(iii) Para grafos mixtos con condición sine qua non parcial: O(G) interpola de manera continua entre los dos casos anteriores, sin discontinuidades.

### III.  Los cuatro precedentes en la literatura

Referencia Resultado relevante

Conexión con la C.O.U.

Hu & Shapley (2003) 'On authority distributions in organizations'

Demuestran que en estructuras jerárquicas, la distribución de autoridad que satisface el axioma eigenvectorial de centralidad y el axioma de Shapley de contribución marginal es la misma distribución.

Establece que eigenvector y Shapley pueden coincidir en una misma estructura. La C.O.U. generaliza este resultado a estructuras no jerárquicas.

Teng (2016) 'Scalable and Accurate Graph Clustering'

Demuestra que el PageRank puede interpretarse como el valor de Shapley de un juego de influencia social con función característica específica.

El eigenvector es un valor de Shapley para cierto juego. Si el juego correcto puede identificarse para el grafo causal, los dos son el mismo objeto con diferentes representaciones.

Metrología Causal · Vol. II

Referencia Resultado relevante

Conexión con la C.O.U.

Aleandri, Ciardiello & Di Liddo (2025) 'Power indices and graph centrality'

Demuestran que índices de poder que combinan centralidad eigenvectorial son valores de Shapley de juegos TU sobre grafos con uniones a priori.

Extiende el resultado de Teng a grafos con estructura de coalición explícita — el contexto del grafo causal con aristas ponderadas.

Forré & Jansma (2025) 'Causal Shapley values on DAGs'

Generalizan el valor de Shapley a funciones vectoriales en multigrafos dirigidos acíclicos ponderados.

El marco formal de Forré & Jansma es el contexto natural donde O podría definirse. Su generalización al grafo causal con IIC y los corolarios está pendiente.

### IV.  Lo que falta para la demostración

### Programa de demostración de la C.O.U. — tres pasos

Paso 1 — Definir C con precisión: especificar la clase de grafos sobre la que O está definido. La clase C debe incluir los grafos causales de este sistema (W ≥ 0, irreducibles, con nodo sumidero) y excluir los grafos donde ni eigenvector ni Shapley tienen interpretación causal válida.

Paso 2 — Encontrar los axiomas que determinan O unívocamente en toda C: los axiomas deben (a) reducirse a A1–A4 en el caso sine qua non, (b) reducirse a los axiomas de Shapley en el caso acumulativo, y (c) determinar una distribución única para casos mixtos.

Paso 3 — Demostrar continuidad entre los dos extremos: la interpolación del punto (iii) requiere una métrica sobre C que mida qué tan 'cerca' está

Metrología Causal · Vol. II

un grafo del caso sine qua non o del caso acumulativo, y demostrar que O varía continuamente con esa métrica.

### V.  El valor de la conjetura para el sistema

La conjetura del operador unificador no es necesaria para operar el sistema. El mediador que tiene claro cuándo usar eigenvector y cuándo usar Shapley tiene todo lo que necesita para el análisis de cualquier caso real. La conjetura importa por razones distintas.

La primera: la demostración de C.O.U. convertiría la metrología causal en una ciencia matemáticamente más completa. Un operador unificador sería la respuesta a todos los tipos de problema — lo que corresponde al nivel de generalidad que una teoría matemática de la responsabilidad causal debería alcanzar.

La segunda: la demostración identificaría la función característica v(S) del juego cooperativo que corresponde al grafo causal de este sistema. Esa función característica haría el cálculo del Shapley significativamente más eficiente para los casos acumulativos.

La tercera: el programa de investigación de C.O.U. es el punto de contacto más natural entre el sistema y la literatura matemática establecida. Una demostración publicable es la vía de validación externa más robusta que el sistema tiene disponible.

La conjetura del operador unificador se formula aquí con precisión matemática y honestidad sobre su estatus: es una conjetura, no un resultado. Su inclusión en este volumen no es para afirmar más de lo que la evidencia actual permite sino exactamente para lo contrario — para delimitar con precisión dónde está el límite del conocimiento formalizado del sistema y dónde comienza el programa de investigación que lo extenderá.

Metrología Causal · Vol. II

Principio de honestidad metrológica sobre los límites del sistema

### Producto de salida · Capítulo IV·7

La Conjetura del Operador Unificador formalmente enunciada: el operador O que produce el eigenvector en el caso sine qua non y el Shapley en el caso acumulativo, con interpolación continua en casos mixtos. Los cuatro precedentes de la literatura. El programa de demostración en tres pasos con identificación precisa de la brecha técnica que falta cerrar.

Notas al Capítulo IV·7

1  El enunciado del punto (iii) de la conjetura — interpolación continua para casos mixtos — es el más delicado porque 'fracción de sine qua non' no está formalmente definida. Una definición candidata: dado un grafo G con n nodos, sea k el número de nodos que pasan el test de condición sine qua non individual. La fracción de sine qua non es k/n. O(G) interpola entre el eigenvector (k/n = 1) y el Shapley (k/n = 0). El problema matemático es que k puede no ser continuo en ningún parámetro natural del grafo.

2  El resultado de Teng (2016) es el más directamente relevante para la C.O.U. Su demostración que el PageRank es el valor de Shapley de un juego de influencia social sugiere que la función característica v(S) del juego asociado al grafo causal podría expresarse en términos de la submatriz W_S. Esta línea de investigación es la más prometedora para el Paso 2 del programa de demostración.

3  La validación matemática externa de la C.O.U. es uno de los objetivos del programa de investigación del Centro Multidisciplinario Meriadock. Investigadores con formación en teoría de juegos cooperativos o álgebra lineal aplicada interesados en colaborar pueden contactar al Centro para acceder al manuscrito completo de la Axiomatización del Sistema de la Doble Mediación.

Metrología Causal · Vol. II

APÉNDICES

### Apéndice A

### Protocolo de calibración empírica

Recolección de datos desde programas de intervención longitudinal

### I.  El propósito del Apéndice A

El Apéndice A documenta el protocolo completo para generar datos de calibración del sistema desde programas de intervención longitudinal. A diferencia de los datos forenses o clínicos que alimentan el análisis causal en casos individuales, los datos de calibración tienen un propósito diferente: verificar empíricamente que los parámetros teóricos del sistema — los rangos de S por Hijo dominante del Capítulo I·4, los pesos de φ□ de la Axiomatización, la velocidad de convergencia del eigenvector humano — corresponden a los valores observables en poblaciones reales.

El protocolo está diseñado para funcionar con operadores sin formación en el paradigma. Toda la inteligencia teórica está contenida en el diseño de los instrumentos y en la tabla de conversión — el operador marca casillas. El Centro Multidisciplinario Meriadock aplica la tabla de conversión y produce los parámetros de calibración. La cadena es: casillas → Metrología Causal · Vol. II

### parámetros operativos → calibración de instrumentos → calibración de la Axiomatización.

### II.  Los cuatro parámetros a estimar

El protocolo genera datos para estimar cuatro parámetros que ningún otro corpus existente puede proveer, porque ningún otro corpus combina una base ontológica formal con observación longitudinal sistemática.

Parámetro Qué mide Por qué ningún otro corpus lo provee

w(τ) — Función de peso del integral de Bochner

El peso que cada momento del pasado tiene en el estado presente de I(t). ¿Decae exponencialmente, linealmente, o con otra función?

Requiere observación repetida del mismo sujeto a lo largo del tiempo con variables estructurales definidas formalmente. Los corpus psicométricos no tienen la base ontológica; los filosóficos no tienen datos longitudinales.

Pesos relativos de φ□ (v_t, c, h)

En la función ₁ φ (v_t, c, h) → acto, qué tanto predice el acto el estado interno del sujeto (v_t), su campo heredado (c), y su historia acumulada (h)

Requiere que las tres variables sean operacionalizadas con el mismo sistema conceptual. No hay instrumento externo que mida v_t, c y h simultáneamente con la ontología de este sistema.

Dimensión efectiva de E

Cuántas dimensiones independientes son necesarias para describir el patrón de

Requiere que las variables observadas mapeen directamente al espacio E de la Axiomatización. Solo los

Metrología Causal · Vol. II

Parámetro Qué mide Por qué ningún otro corpus lo provee

comportamiento de un ego en un contexto específico. Si n dimensiones explican el 80% de la varianza, la dimensión efectiva de E para esa población es n.

instrumentos de este sistema producen esas variables.

Velocidad de convergencia del eigenvector humano

Cuántas 'iteraciones' (sesiones, interacciones, eventos) requiere el eigenvector de un sistema humano real para converger. El análogo empírico de la convergencia 10 ⁶ ⁻ del método de potencias.

Requiere observación longitudinal con suficientes puntos de tiempo sobre las mismas variables estructurales. Los estudios de cambio actitudinal típicos no miden las variables correctas.

### III.  Los dos formularios del protocolo

El protocolo opera con dos formularios que el operador usa en cada sesión del programa de intervención. El Formulario A lo llena el operador observando. El Formulario B lo llena el participante al final de la sesión. Los dos son idénticos en las n sesiones del programa — solo cambia el número de sesión. Toda la inteligencia del sistema está en el diseño de las opciones y en la tabla de conversión del Apartado V.

Metrología Causal · Vol. II

### FORMULARIO A · Registro del operador

Una hoja por grupo por sesión. El operador observa durante la sesión y marca UNA sola opción por variable para cada participante. No escribe nada. No interpreta nada. Solo marca.

Instrucción: marca lo que observaste, no lo que crees que el participante quiso decir. Si no tuviste oportunidad de observar una variable, deja la celda en blanco.

Variable Opción A Opción B Opción C

V1 · ¿Quién fue el sujeto de sus frases?

Dijo 'yo hice / yo decidí / yo elegí'

Dijo 'me sentí / me ocurrió / me di cuenta'

Dijo 'él me hizo / fue la presión / no había opción'

V2 · ¿Su respuesta fue igual o diferente al grupo?

Su respuesta fue diferente a las demás

No respondió nada en la actividad

Su respuesta fue similar a lo que ya habían dicho otros

V3 · ¿Sabía qué quería antes de actuar?

Sí, nombró qué quería antes de actuar

Nombró cómo se sentía, pero no qué quería

Solo habló de lo que otros hicieron o de las circunstancias

V4 · ¿Nombró algo concreto que él hizo?

Sí, nombró un acto específico suyo con consecuencia

Dijo que algo dependía de él, sin especificar qué

No mencionó nada de lo que él hizo

### FORMULARIO B · Reporte del participante

### Una hoja individual por participante por sesión. Se entrega en los últimos 3 minutos. El participante la llena solo. 4

Metrología Causal · Vol. II

preguntas. Sin opciones neutras — cada pregunta obliga a tomar posición. Los participantes no ven el Formulario A.

Sesión: ___ · Clave del participante: _________ · Fecha: ___________

Encierra en un círculo la opción que más se parece a lo que pasó HOY en la sesión.

1. Cuando hablé de algo que hice o que me pasó, lo describí como:    A — Algo que yo decidí o hice, aunque no haya salido bien    B — Algo que sentí o que me ocurrió    C — Algo que pasó por lo que otros hicieron o por las circunstancias

### 2. Lo que dije o compartí en la actividad de hoy fue:    A — Diferente a lo que dijeron mis compañeros    B — No compartí nada hoy    C — Parecido a lo que ya habían dicho otros

3. Cuando recuerdo algo que hice esta semana, puedo decir: A — Sé qué quería lograr cuando lo hice    B — Recuerdo cómo me sentí, pero no bien qué quería    C — No sé bien por qué lo hice, simplemente pasó

4. Al terminar esta sesión, puedo decir:    A — Identifiqué algo concreto que yo hice y que tuvo consecuencias    B — Siento que algo de lo que pasó dependió de mí, pero no sé exactamente qué    C — Lo que pasó no tuvo mucho que ver con lo que yo hice

### IV.  La tabla de conversión — solo Meriadock

Metrología Causal · Vol. II

### Esta tabla nunca sale del equipo central. Es el motor que convierte los datos crudos de los formularios en parámetros del sistema. El operador y el participante nunca la ven.

Variable Opción Valor numérico

Parámetro que alimenta

A 1.00 α directo — alta asunción observada

V1 · Atribución (α proxy)

B 0.50 α directo — asunción media

C 0.00 α directo — baja asunción

A 0.10 S directo — baja sustituibilidad

V2 · Conformidad (S proxy)

B — Sin dato — no se incluye en el promedio de S

C 0.90 S directo — alta sustituibilidad

A 2 v_t estructurado

V3 · Estado interno (v_t)

B 1 v_t difuso

C 0 v_t ausente

A 2 φ□ activo

V4 · Reconocimiento (φ□)

B 1 φ□ parcial

C 0 φ□ ausente

Metrología Causal · Vol. II

El cálculo de Δ emerge de la brecha entre los dos formularios sobre la misma variable. Para V1: Δ_sesión = valor de V1 en Formulario A − valor de pregunta 1 en Formulario B. Δ > 0 indica que el participante se atribuye menos responsabilidad de lo que su lenguaje observable refleja (evasión conductual). Δ < 0 indica que se atribuye más de lo que muestra (asunción que supera la conducta observable). Δ ≈ 0 indica calibración: el participante se ve aproximadamente como el operador lo ve.

### V.  El árbol de clasificación del Hijo dominante

El árbol clasifica el Hijo dominante del participante desde los promedios de las cuatro variables a lo largo de todas las sesiones del programa. Se aplica después de la última sesión, sobre los promedios □, S□, v□_t y φ□□.

Árbol de clasificación — lectura secuencial

Paso 1 — ¿S□ > 0.60? Si SÍ → el campo domina sobre la voluntad individual. Ir al Paso 2. Si NO → hay individuación en la voluntad. Ir al Paso 4.

Paso 2 (S□ > 0.60) — ¿□ < 0.30? Si SÍ → Ir al Paso 3. Si NO → ANTEROS. La voluntad se orienta por reciprocidad. Condicionamiento de la asunción a la respuesta del otro.

Paso 3 (S□ > 0.60, □ < 0.30) — ¿φ□□ < 0.50? Si SÍ → FOBOS. La voluntad se orienta por miedo al campo. No asume, no reconoce, se conforma. Si NO → DEIMOS. La voluntad se orienta por la amenaza difusa. Reconoce actos, pero los atribuye a presión externa.

Paso 4 (S□ ≤ 0.60) — ¿□ > 0.60? Si SÍ → Ir al Paso 5. Si NO → POTÓS. La voluntad se orienta por anhelo de lo ausente. Baja sustituibilidad con asunción media.

Metrología Causal · Vol. II

Paso 5 (S□ ≤ 0.60, □ > 0.60) — ¿v□_t > 1.0? Si SÍ → HARMONÍA. La voluntad se orienta por integración plena. Alta asunción, claridad interna, ₂ φ activo. Si NO → EROS. La voluntad se orienta por deseo presente. Asume, pero desde impulso más que desde claridad.

Hijo □ esperad o

S□ esperad o

v□_t esperad o

φ□□ esperad o

Patrón Δ típico

Fobos 0.00– 0.25 0.70– 1.00 0.00– 0.50 0.00– 0.50 Δ negativo — asume menos de lo que hace

Deimos 0.20– 0.40 0.65– 0.90 0.50– 1.00 0.50– 1.00 Δ negativo moderado

Anteros 0.30– 0.60 0.40– 0.70 0.50– 1.20 0.50– 1.20 Δ variable — depende de la respuesta del referente

Potós 0.35– 0.60 0.20– 0.50 0.80– 1.50 0.50– 1.20 Δ positivo — asume más de lo que el campo justifica

Eros 0.55– 0.80 0.10– 0.35 0.80– 1.50 1.00– 1.80 Δ ≈ 0 con varianza alta

Harmon ía

0.70– 1.00 0.00– 0.25 1.20– 2.00 1.50– 2.00 Δ ≈ 0 estable, convergen

Metrología Causal · Vol. II

Hijo □ esperad o

S□ esperad o

v□_t esperad o

φ□□ esperad o

Patrón Δ típico

cia temprana

### VI.  El criterio de convergencia k_conv

Un participante ha convergido en la sesión k si las opciones modales de V1 (proxy de α) y V4 (proxy de φ□) en el Formulario A son iguales en las sesiones k−2, k−1 y k. Es decir: tres sesiones consecutivas con el mismo patrón en las dos variables estructurales.

La sesión de convergencia se registra como k_conv. Si el patrón no se estabiliza antes de la última sesión, k_conv = indefinido — lo que es en sí mismo un dato: significa que el proceso no fue suficiente para estabilizar la posición de ese sujeto. El promedio de k_conv sobre toda la muestra es la estimación empírica de cuántas iteraciones requiere el eigenvector humano para converger en esa población.

k_conv Interpretación para el sistema

Implicación para la Axiomatización

Sesiones 3–4 Patrón muy estable desde el inicio. El programa lo reveló, no lo formó.

v_t y φ□ preexistían al programa. El peso de h en φ□ es dominante para este sujeto.

Sesiones 5–6 Convergencia media. El programa produjo el cambio en la primera mitad.

Peso balanceado entre v_t y c en φ□. Valor típico para la población general.

Metrología Causal · Vol. II

k_conv Interpretación para el sistema

Implicación para la Axiomatización

Sesiones 7–8 Convergencia tardía. El proceso requirió más iteraciones.

S alto al inicio — el campo dominaba φ□. El cambio requirió más exposición.

Sesiones 9–n Convergencia al límite. Las sesiones disponibles apenas suficientes.

El sistema necesita más iteraciones que las del programa estándar.

Indefinido Sin convergencia en el programa.

Requiere análisis individual. Puede indicar bloqueo ontológico o condición que excede el programa.

### VII.  La hoja de calibración de la Axiomatización

Al final de cada cohorte (todos los grupos del ciclo escolar), los datos agregados producen la hoja de calibración de la Axiomatización. Esta hoja es el insumo directo para verificar los postulados formales del sistema y — con suficiente muestra — para estimarlos empíricamente.

Parámetro de la Axiomatización

Cómo se estima desde los datos del protocolo

Qué nivel de evidencia produce

w(τ) — función de peso de I(t)

Correlación entre α en la sesión τ y α en la sesión final, para cada distancia τ. Si la correlación decrece exponencialmente con τ, w(τ) tiene forma exponencial. Si decrece

Evidencia empírica directa de la forma de w(τ) para esta población. Primer dato empírico de la Axiomatización sobre I(t).

Metrología Causal · Vol. II

Parámetro de la Axiomatización

Cómo se estima desde los datos del protocolo

Qué nivel de evidencia produce

linealmente, tiene forma lineal.

Pesos relativos de v_t, c, h en φ□

Regresión de α_final sobre: v_t en sesión 1 (estado interno inicial), S□ global (campo heredado — proxy de c), α en sesión 1 (historia previa — proxy de h). Los coeficientes son los pesos relativos de los tres inputs de φ□.

Estimación empírica de la función φ□ para esta población. El predictor con mayor coeficiente independiente es el input dominante.

Dimensión efectiva de E

Análisis de componentes principales sobre las 4 variables × n sesiones. El número de componentes necesarios para explicar el 80% de la varianza es la dimensión efectiva.

La Axiomatización postula E separable. Este dato dice cuántas dimensiones son efectivamente necesarias en un sistema humano adolescente en contexto escolar.

Velocidad de convergencia del eigenvector

Promedio y desviación estándar de k_conv sobre la cohorte. Distribución de k_conv por Hijo dominante clasificado.

El k_conv promedio es la estimación empírica del número de iteraciones que requiere el eigenvector humano para converger en esta población.

Con tres o más cohortes (ciclos escolares), los parámetros estimados producen valores estables y comparables entre grupos. Con diez o más cohortes, la estimación de w(τ) y de los pesos de φ□ alcanza el nivel de precisión necesario para publicación en literatura de psicometría formal.

Metrología Causal · Vol. II

### Productos del Apéndice A

Formulario A (operador) y Formulario B (participante) listos para imprimir y usar en campo. Tabla de conversión para Meriadock. Árbol de clasificación del Hijo dominante. Criterio de convergencia k_conv. Hoja de calibración de la Axiomatización con sus cuatro parámetros estimables. Los dos formularios son autosuficientes — el operador no necesita ningún otro documento para su uso.

Notas al Apéndice A

1  El protocolo requiere que las claves de los participantes sean asignadas por Meriadock antes de comenzar el programa — no por el operador o la institución. Esto garantiza que los datos de múltiples escuelas y ciclos son vinculables longitudinalmente sin exponer datos personales. La clave es el identificador permanente del participante a través de todas las cohortes en las que participe.

2  La escala de cuatro variables (V1–V4) es el mínimo operativo: cuatro variables producen todos los parámetros necesarios si se observan en suficientes sesiones. Agregar más variables por sesión aumenta la carga del operador sin aumentar proporcionalmente la información de calibración. La restricción de cuatro variables es un principio de diseño, no una limitación técnica.

3  El protocolo puede adaptarse a poblaciones distintas de adolescentes en secundaria con ajustes menores en el lenguaje del Formulario B. Los valores de la tabla de conversión (Apartado IV) son los mismos para cualquier población — representan la estructura formal del sistema, no características de la población específica. Los rangos del árbol de clasificación del Hijo dominante (Apartado V) pueden necesitar calibración para poblaciones con características estructurales muy diferentes (adultos mayores, contextos institucionales, poblaciones clínicas).

Metrología Causal · Vol. II

APÉNDICES

### Apéndice B

### Tabla de equivalencias extendida por

### dominio

Los nueve conceptos del sistema en ocho dominios disciplinares

### I.  El propósito del Apéndice B

La Introducción de este volumen establece el glosario operativo universal con tablas de equivalencias para los nueve conceptos del sistema en seis dominios. El Apéndice B extiende esas tablas en dos dimensiones: añade dos dominios adicionales (educación y psicología forense) y profundiza cada equivalencia con el vocabulario técnico específico que el mediador encuentra en documentos, expedientes y comunicaciones formales de cada disciplina.

La función de este apéndice no es reemplazar al glosario de la Introducción — es complementarlo. La Introducción establece el principio de traducción. Este apéndice provee el léxico completo que el mediador necesita cuando trabaja en un dominio específico con sus terminologías propias. Un abogado penalista y un epidemiólogo describen el mismo fenómeno causal con vocabularios tan distintos que el mediador sin este apéndice puede no reconocer que está ante el mismo concepto del sistema.

Metrología Causal · Vol. II

### II.  Tabla maestra de equivalencias — Nodo

Dominio Término equivalente más frecuente

Términos adicionales del dominio

Criterio de identificación

Derecho penal

Imputado, acusado, responsable

Autor material, coautor, partícipe, instigador, cómplice, sujeto activo

Actor cuya conducta activa u omisiva fue condición necesaria del tipo penal. Incluye personas jurídicas cuando el sistema legal lo permite.

Derecho civil / mercantil

Parte demandada, deudor, responsable civil

Garante, fiduciario, mandatario, representante legal, socio gestor

Actor con deber jurídico cuyo incumplimiento fue condición necesaria del daño resarcible.

Medicina y salud pública

Factor de riesgo, factor etiológico, agente causal

Comorbilidad, determinante de salud, variable de exposición, actor institucional

El factor cuya eliminación contrafactual habría prevenido o modificado el resultado clínico. Incluye sistemas de salud como nodos.

Economía y política pública

Agente económico, actor institucional, variable de política

Formador de precios, regulador, institución, tomador de decisiones

El agente cuya decisión alteró la trayectoria del sistema más allá del ruido esperado y es identificable como

Metrología Causal · Vol. II

Dominio Término equivalente más frecuente

Términos adicionales del dominio

Criterio de identificación

condición necesaria del resultado.

Psicología clínica

Actor vincular, figura de apego, sistema familiar

Referente significativo, cuidador primario, institución socializadora

La entidad cuyo patrón de conducta fue condición del patrón de respuesta del sujeto analizado.

Psicología forense

Peritado, evaluado, sujeto de la pericia

Imputado evaluado, víctima evaluada, testigo evaluado

El sujeto cuya capacidad de actuar, comprender o integrar sus actos es el objeto de la evaluación pericial.

Educación Estudiante, docente, directivo, familia

Comunidad educativa, institución educativa, diseñador curricular

El actor cuya decisión o patrón de conducta fue condición del resultado educativo analizado (abandono, rendimiento, comportamiento).

Ingeniería e industria

Componente, sistema, equipo de diseño, operador

Subsistema, interfaz, arquitecto del sistema, proveedor crítico

El elemento cuya falla o decisión de diseño fue condición estructural de la falla sistémica o del accidente analizado.

Metrología Causal · Vol. II

### III.  Tabla maestra de equivalencias — Arista

Dominio Término equivalente más frecuente

Lo que acredita la arista en ese dominio

Derecho penal

Nexo causal, relación de causalidad penal, vínculo típico

Prueba de que la conducta del nodo fue condición necesaria del resultado típico. Estándar: más allá de duda razonable en foros penales.

Derecho civil

Relación de causalidad adecuada, nexo causal civil

Prueba de que el daño es consecuencia previsible de la conducta del nodo. Estándar: preponderancia de la evidencia.

Medicina Relación etiológica, mecanismo causal, vía fisiopatológica

Evidencia de que el factor i actúa sobre el factor j a través de un mecanismo biológico, farmacológico o conductual documentado.

Economía Canal de transmisión, efecto estructural, mecanismo de política

Evidencia teórica o empírica de que la decisión de i afecta el resultado en j a través de un mecanismo económico identificable.

Psicología clínica

Influencia vincular, condicionamiento, transmisión intergeneracional

Historia de interacciones documentadas entre i y j con patrón de respuesta de j contingente al comportamiento de i.

Psicología forense

Influencia sobre la capacidad, condicionamiento de la conducta

Evidencia de que el nodo i afectó la capacidad de comprensión, motivación o control de conducta del nodo j en el momento del acto.

Educación Influencia pedagógica, efecto docente,

Evidencia de interacciones entre i y j (docente-estudiante, familia-estudiante, pares) con efecto

Metrología Causal · Vol. II

Dominio Término equivalente más frecuente

Lo que acredita la arista en ese dominio

transmisión de expectativas

documentado sobre el resultado educativo.

Ingeniería Dependencia funcional, propagación de falla, interfaz crítica

Documentación de que el estado o decisión del componente i determina o limita el estado del componente j en condiciones operativas normales y de falla.

### IV.  Tabla maestra de equivalencias — R*

Dominio Cómo se comunica R*

Frase estándar de presentación ante ese foro

Derecho penal

Grado de responsabilidad causal, participación estructural en el resultado

'El análisis establece que el nodo [X] fue condición causal del [resultado] con un peso estructural de [R*×100]%.'

Derecho civil

Cuota de responsabilidad proporcional, contribución causal al daño

'La distribución causal proporcional asigna al [demandado] el [R*×100]% del resultado dañoso analizado.'

Medicina Fracción atribuible, peso etiológico del factor

'El factor [X] explica el [R*×100]% del resultado clínico en este sistema causal específico.'

Metrología Causal · Vol. II

Dominio Cómo se comunica R*

Frase estándar de presentación ante ese foro

Economía Atribución de impacto, contribución estructural al resultado

'Esta decisión de política explica el [R*×100]% de la variación observada en el indicador analizado.'

Psicología clínica

Peso causal del factor, contribución al patrón de respuesta

'El patrón vincular de [X] explica el [R*×100]% del patrón de conducta del sujeto en este sistema.'

Psicología forense

Contribución causal a la capacidad o conducta del peritado

'La influencia del factor [X] explica el [R*×100]% del patrón conductual objeto de la pericia.'

Educación Contribución al resultado educativo, peso en la trayectoria

'El factor [X] explica el [R*×100]% del resultado educativo analizado en este contexto específico.'

Ingeniería Contribución a la falla sistémica, peso causal del componente

'El componente [X] concentra el [R*×100]% de la responsabilidad causal de la falla sistémica analizada.'

### V.  Tabla maestra de equivalencias — S

Metrología Causal · Vol. II

Dominio Término equivalente de S

Cómo se calibra en ese dominio

Derecho penal

Presión del entorno, contexto coactivo, estado de necesidad

¿Otro sujeto en esa posición habría cometido el mismo acto bajo la misma presión? Jurisprudencia del estándar del 'hombre medio' en ese contexto.

Derecho civil

Práctica habitual del sector, estándar de la industria

¿El comportamiento del nodo era el comportamiento estándar de otros actores en posición equivalente? Evidencia de prácticas del sector.

Medicina Adherencia al protocolo, práctica clínica habitual

¿Otros profesionales en condición equivalente habrían actuado igual según el protocolo vigente? Guías de práctica clínica del período.

Economía Incentivo estructural, regla de decisión del sector

¿El comportamiento del agente era el comportamiento racional dado el sistema de incentivos? Documentación de incentivos y restricciones del período.

Psicología clínica

Condicionamiento heredado, presión del sistema vincular

¿La respuesta del sujeto era la respuesta condicionada por su historia de aprendizaje? Historia de refuerzos documentada.

Psicología forense

Imputabilidad reducida, disminución de la capacidad de control

¿El estado interno del peritado en el momento del acto limitaba su capacidad de actuar diferente? Evaluación del estado mental en el momento del acto.

Educación Presión normativa, expectativa institucional,

¿El comportamiento del estudiante o docente era el comportamiento esperado por el sistema educativo en ese contexto?

Metrología Causal · Vol. II

Dominio Término equivalente de S

Cómo se calibra en ese dominio

condicionamiento del aula

Ingeniería Operación dentro de especificaciones, condición de diseño normal

¿El componente operaba dentro de los parámetros de diseño en que cualquier componente equivalente habría fallado igual?

### VI.  Tabla maestra de equivalencias — α

Dominio Término equivalente de α

Evidencia que lo acredita en ese dominio

Derecho penal

Culpabilidad subjetiva, conocimiento y voluntad del acto

Dolo directo / eventual: el imputado sabía y quiso el resultado. Culpa: el imputado debía haber previsto el resultado. Las acciones de mitigación tomadas se suman al α.

Derecho civil

Diligencia debida, buena fe objetiva, cumplimiento del deber de cuidado

Acciones preventivas documentadas, informes de riesgo, medidas correctivas tomadas antes y después del resultado.

Medicina Adhesión al protocolo, diligencia clínica, consentimiento informado

Historia clínica completa, órdenes médicas, registros de monitoreo, acciones tomadas ante señales de alarma documentadas.

Economía Cumplimiento regulatorio,

Registros de implementación, indicadores de cumplimiento,

Metrología Causal · Vol. II

Dominio Término equivalente de α

Evidencia que lo acredita en ese dominio

implementación efectiva de política

respuesta documentada ante señales de alerta sistémica.

Psicología clínica

Reconocimiento del acto, responsabilidad integrada, capacidad de rectificación

Conducta observable de reconocimiento en sesión, acciones de reparación verificables, cambio de patrón documentado en el tiempo.

Psicología forense

Imputabilidad, capacidad de comprensión y de autodeterminación

Evaluación del estado mental en el momento del acto: ¿el peritado comprendía el alcance de su conducta y tenía capacidad de autodeterminación?

Educación Responsabilidad pedagógica, actuación conforme al rol

Registros de asistencia, planificación documentada, seguimiento del estudiante, acciones tomadas ante señales de riesgo educativo.

Ingeniería Cumplimiento del protocolo de mantenimiento y operación, actuación del operador

Registros de mantenimiento, bitácoras de operación, reportes de anomalías, acciones correctivas ante alertas del sistema.

### VII.  Tabla maestra de equivalencias — Δ, IIC y Fraude annona

Metrología Causal · Vol. II

Concepto Dominio Término equivalente

Consecuencia normativa típica

Δ — Déficit de asunción

Derecho penal

Ausencia de arrepentimiento activo, falta de colaboración con la justicia

Agravante de responsabilidad penal en algunos sistemas. Impacto en la determinación de la pena.

Derecho civil

Brecha entre responsabilidad declarada y acciones reparatorias

Fundamento de la responsabilidad solidaria ampliada o del deber de reparación integral.

Medicina Déficit de manejo activo, falta de respuesta ante el evento adverso

Elemento de responsabilidad médica. Fundamento de quejas ante colegios profesionales.

Economía Incumplimiento de obligaciones de implementación

Fundamento de sanciones regulatorias por incumplimiento de metas o compromisos declarados.

Psicología clínica

Déficit de integración, trabajo ontológico pendiente

Objetivo central del acompañamiento con HISTOS. No tiene consecuencia normativa directa.

IIC — Integridad causal

Derecho civil / regulatorio

Buena fe objetiva, congruencia entre declaración y conducta

Elemento de responsabilidad por diseño defectuoso. Fundamento de acciones de compliance y regulación.

Metrología Causal · Vol. II

Concepto Dominio Término equivalente

Consecuencia normativa típica

Auditoría Tasa de cumplimiento declarado vs. real

Indicador central de auditoría de efectividad. Fundamento de observaciones y recomendaciones.

Medicina Adherencia al protocolo declarado, calidad del diseño del protocolo

Elemento de evaluación de la calidad del sistema de salud. Fundamento de acreditaciones institucionales.

Fraude annona

Derecho regulatorio

Incumplimiento agravado por posición de garante o administrador fiduciario

Activación de medidas cautelares, intervención regulatoria, responsabilidad penal de administradores.

Medicina Negligencia institucional del sistema o de la autoridad sanitaria

Fundamento de investigaciones de salud pública, reformas de protocolo, responsabilidad institucional.

Educación Incumplimiento del sistema educativo como nodo de diseño

Fundamento de evaluaciones de política educativa, reformas curriculares, responsabilidad institucional.

### VIII.  Nota sobre la precisión de las equivalencias

Metrología Causal · Vol. II

Las equivalencias de este apéndice son instrumentos de traducción, no de identificación exacta. El vocabulario de cada disciplina fue construido con propósitos propios — el concepto jurídico de diligencia debida no coincide perfectamente con α, el concepto epidemiológico de fracción atribuible no coincide perfectamente con R*. En todos los casos, el concepto del sistema es más preciso que el equivalente disciplinar: tiene una definición operativa exacta, un procedimiento de cálculo reproducible, y una justificación formal desde el Teorema IV·2.

El error que el mediador debe evitar es la dirección inversa: usar el vocabulario disciplinar para interpretar los conceptos del sistema. 'Diligencia debida' es lo que los abogados llaman α en contextos civiles — pero α no es diligencia debida. α es la fracción de R* integrada mediante acciones verificables, calculada con los tres criterios del Capítulo I·5. La equivalencia sirve para comunicar al abogado qué está leyendo cuando ve α en el expediente. No sirve para sustituir la definición formal de α por la noción jurídica de diligencia.

Este apéndice y el glosario de la Introducción son instrumentos de comunicación, no de reducción. El sistema no se traduce al vocabulario de ningún dominio — el vocabulario de cada dominio se aproxima al sistema. Esa dirección asimétrica es la condición de que el análisis causal mantenga su rigor cuando opera en cualquier dominio.

Principio de dirección de la traducción terminológica

Productos del Apéndice B

Tablas de equivalencias extendidas para los nueve conceptos del sistema (Nodo, Arista, R*, S, α, Δ, IIC, Fraude annona) en ocho dominios: derecho penal, derecho civil, medicina, economía, psicología clínica, psicología forense, educación, e ingeniería. El mediador usa este apéndice como referencia

Metrología Causal · Vol. II

### rápida cuando prepara la presentación del expediente para un foro o audiencia específica.

Notas al Apéndice B

1  El dominio de psicología forense se agrega a los seis dominios de la Introducción porque es el contexto donde la tensión entre el sistema y el vocabulario establecido es más aguda. La psicología forense tiene conceptos propios muy desarrollados (imputabilidad, capacidad de comprensión, actio libera in causa) que parcialmente se solapan con los del sistema (α, v_t, φ□) pero que fueron construidos con propósitos legales específicos. El mediador que opera en ese dominio necesita conocer con precisión dónde coinciden y dónde divergen los dos vocabularios.

2  El dominio de educación se agrega porque el Programa ECO del Apéndice A genera datos en ese contexto, y los operadores educativos necesitan el vocabulario equivalente para interpretar los resultados del protocolo. R* en educación no es un concepto familiar para docentes y directivos — pero 'contribución al resultado educativo' sí lo es, y esa es la equivalencia que el apéndice provee.

3  La tabla de Fraude annona del Apartado VII es la más compleja porque el concepto no tiene equivalente directo en ningún dominio — es una identidad matemática específica de este sistema. Las equivalencias listadas son aproximaciones funcionales que el mediador puede usar para comunicar la gravedad de la posición del nodo de diseño, no para equiparar el fraude annona con ningún concepto jurídico o disciplinar preexistente. La precisión del concepto solo puede comunicarse refiriendo al Corolario III del Capítulo IV·5.

## Notas al pie

[^1]: La Estación ECO es opcional en el sentido de que no todos los casos 
tienen un ego humano a localizar. Los casos de auditoría institucional 
donde todos los nodos son institucionales o normativos —sin ego 
individual identificable como objeto de localización— no activan ECO. 
El grafo se construye directamente desde el expediente documental.

[^2]: La condición de completitud del grafo —que incluya todos los nodos con 
capacidad causal, incluyendo los no documentados— es la condición 
metrológica más exigente del sistema y la más frecuentemente violada 
en la práctica. Un nodo estructuralmente necesario que no aparece en el 
expediente no desaparece del grafo real: desaparece del análisis, 
concentrando artificialmente R* en los nodos documentados [Vol.I · 
Cap. III·5]. El mediador que sabe que hay un nodo relevante pero no

[^1]: Los rangos de S por Hijo que este capítulo establece son valores de 
referencia derivados de la correspondencia formal entre el Hijo 
dominante y la sustituibilidad [La transformación formal · Cap. 2.1]. No 
son valores empíricos calibrados sobre una muestra: son consecuencias 
de la estructura de la doble mediación. Los datos empíricos del

[^1]: α no mide remordimiento, culpa, ni declaración de responsabilidad. Mide 
asunción verificable mediante conducta. Un ego que declara alta 
responsabilidad, pero no tomó ninguna acción orientada a modificar el 
resultado tiene α bajo independientemente de lo que diga. Un ego que 
no declara responsabilidad, pero tomó acciones completas de mitigación 
tiene α alto. La confusión entre declaración y asunción es el error más 
frecuente de calibración de α en la práctica.

[^1]: La traducción de términos técnicos al vocabulario del dominio requiere 
una precaución importante: la traducción debe ser consistente a lo largo 
de todo el proceso del caso. Si R* se traduce como 'contribución causal 
proporcional' en el resumen ejecutivo, debe traducirse igual en el análisis 
oral ante el tribunal y en cualquier documento adicional que el análisis 
genere. La inconsistencia terminológica en un proceso adversarial es una 
vulnerabilidad que el experto contrario puede explotar para cuestionar 
la coherencia del análisis.

[^2]: La pregunta de los puntos de quiebre — qué tendría que ser verdad para 
que la conclusión cambiara — es la más poderosa en cualquier foro

[^2]: La versión del Teorema de Perron-Frobenius que este capítulo usa es para 
matrices no negativas e irreducibles, no necesariamente estrictamente 
positivas. La irreducibilidad de la matriz (en el sentido de que el grafo 
subyacente es fuertemente conexo al sumidero) es suficiente para 
garantizar el eigenvector positivo único sin necesitar que todas las 
entradas de W sean estrictamente positivas.

[^1]: El Corolario I tiene una consecuencia importante para la comunicación en 
contextos donde la responsabilidad colectiva está en cuestión. Cuando 
Σᵢ R*_neta_i es muy menor a 1 — cuando la responsabilidad sistémica 
del campo es muy alta — el análisis puede y debe comunicar que el 
problema es estructural: el resultado habría ocurrido en gran medida 
independientemente de quiénes fueran los actores individuales. Esa 
comunicación no exime a los individuos de su R*_neta — exige que el 
análisis correctivo se dirija también a la estructura del campo.
