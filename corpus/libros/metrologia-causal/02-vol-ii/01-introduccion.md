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

