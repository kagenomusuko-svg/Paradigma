PARTE I · Derecho y Justicia

## Capítulo 4

### Derecho ambiental — responsabilidad por daño ecológico

Organ.  Estru.  Model.  Educa.  Crisi.

Para el mediador que busca precisión · Cómo usar este capítulo Este capítulo opera con dos instrumentos de imputación que no son intercambiables. El primero es R* convencional: se usa cuando al menos un actor es condición necesaria del daño — si ese actor no hubiera operado, el daño no habría ocurrido o habría sido sustancialmente menor. El segundo es el valor de Shapley (φᵢ): se usa cuando el daño es acumulativo y ningún actor es individualmente condición necesaria — el daño ocurre por la suma de contribuciones que superan un umbral, no por ninguna contribución individual. La decisión entre R* y Shapley es la primera pregunta del análisis ambiental y determina todo lo demás. Si tu prioridad es saber cuál aplica y qué buscar primero, ve directamente a §9.

### §1  Descripción del subcampo

El derecho ambiental es el dominio donde el sistema de imputación causal enfrenta sus límites más claros y donde su extensión —los valores de Shapley— es más necesaria. El daño ecológico tiene cuatro características que lo distinguen estructuralmente de todos los demás dominios de este libro y que determinan los instrumentos adecuados para su análisis.

Taxonomía General de Aplicaciones

Característica Descripción Consecuencia para el

análisis causal

Difusión temporal

El daño ecológico se acumula a lo largo de décadas o siglos. Los efectos pueden manifestarse mucho después de que la causa dejó de operar. El contaminante emitido en el año t puede producir daño documentable en t + 30.

El grafo causal debe incluir nodos históricos que ya no operan activamente. La distancia temporal entre causa y efecto complica la atribución causal directa y produce evidencia A6/A7 para las aristas de largo plazo.

Difusión espacial

Los contaminantes se dispersan por agua, aire y suelo cruzando fronteras jurisdiccionales. El punto de medición del daño puede estar lejos del punto de emisión. El contaminante cruza jurisdicciones por diseño del proceso físico, no del actor.

R* de un nodo emisor puede calcularse, aunque el daño ocurriera en otra jurisdicción, pero requiere modelado de la dispersión como evidencia pericial (A2). El análisis de dispersión es condición necesaria para establecer la arista entre el emisor y el daño.

Causalidad acumulativa

El daño es frecuentemente el resultado de la acumulación de contribuciones de múltiples actores sin que ninguno de ellos sea por sí solo condición necesaria y suficiente. El umbral de daño θ se supera solo cuando las contribuciones se suman, no con la de ningún actor individual.

El postulado de la condición necesaria (I5) no se cumple para ningún actor individual. R* convencional asigna cero a todos — resultado técnicamente correcto, pero jurídicamente inaplicable. Aquí es donde R* falla y los valores de Shapley son el instrumento correcto.

Irreversibilidad parcial

Algunos daños ecológicos son

ΔT_trayectoria es el componente dominante

Taxonomía General de Aplicaciones

Característica Descripción Consecuencia para el

análisis causal

permanentes o requieren siglos para recuperarse: extinción de especies, destrucción de ecosistemas únicos, contaminación de acuíferos profundos. La pérdida de biodiversidad tiene componentes irreversibles que ninguna remediación puede restaurar.

del daño ecológico de largo plazo. La incertidumbre sobre el horizonte temporal de la recuperación introduce rangos amplios en el cálculo. Para daños irreversibles, D_monetary_equiv no es lo que se puede pagar: es la medida de la inconmensurabilidad del daño con cualquier reparación finita.

La decisión central del análisis ambiental: ¿R* o Shapley? R* convencional es correcto cuando: al menos un actor es condición necesaria del daño — sin ese actor específico el daño no habría ocurrido o habría sido sustancialmente menor. Ejemplos: desastre industrial con fuente identificable única o dominante, derrame de una sola empresa en un área no contaminada previamente, vertido que produce daño inmediato localizable. Valores de Shapley son necesarios cuando: el daño es acumulativo y ningún actor es individualmente condición necesaria — incluso si ese actor hubiera eliminado completamente sus emisiones, el daño habría ocurrido de todas formas por la suma de las demás. Ejemplos: contaminación de largo plazo por múltiples operadores en la misma cuenca, daño climático global por emisiones de múltiples países, contaminación difusa de acuífero por múltiples fuentes industriales y agrícolas. La pregunta de diagnóstico: ¿Habría ocurrido el daño sin este actor específico, dado lo que los otros habrían emitido de todas formas? Si la respuesta es no → R*. Si la respuesta es sí → Shapley.

### Sub-variantes del dominio

Desastre industrial puntual: una instalación específica produjo el daño mediante un evento identificable con origen claro y único. El grafo incluye el operador directo, la casa matriz que

Taxonomía General de Aplicaciones

diseñó la tecnología y los estándares, el regulador que autorizó las condiciones de operación, y los factores ambientales que determinaron la magnitud de la dispersión. R* convencional aplica porque hay al menos un actor condición necesaria.

Contaminación crónica por fuente única: emisiones continuas de un solo operador durante un período prolongado. Similar al desastre industrial en estructura del grafo, pero ΔT_trayectoria es el componente dominante del daño. R* convencional aplica.

Contaminación acumulativa por múltiples fuentes: el daño es el resultado de la acumulación de contribuciones de varios operadores en el mismo ecosistema durante un período extendido. Ningún operador es condición necesaria individualmente. Shapley es el instrumento correcto. La estimación de v(S) para las coaliciones parciales es el desafío central del análisis.

Daño climático por emisiones acumuladas: el caso límite y el más político. Ningún emisor individual —ningún país, ninguna empresa— es condición necesaria del cambio climático. R* convencional asigna cero a todos. Los valores de Shapley distribuyen la responsabilidad proporcional a la contribución marginal promedio de cada emisor sobre todas las posibles coaliciones. Es la base técnica para el diseño de compromisos climáticos equitativos.

Daño por omisión regulatoria: el regulador que autorizó condiciones que el sistema no debería haber tolerado, que no inspeccionó instalaciones de riesgo conocido, o que asentó comunidades en zonas de riesgo documentado. El regulador tiene arista de omisión en el grafo con R* positivo cuando su inacción fue condición causal del daño.

Responsabilidad de casa matrices multinacionales: la empresa que diseñó la tecnología, estableció los estándares y aprobó las reducciones de costo que comprometieron la seguridad tiene R* positivo, aunque opere en otra jurisdicción. La separación jurídica entre casa matriz y filial no elimina la arista causal en el grafo.

Taxonomía General de Aplicaciones

### §2  Escala de evidencia A0–A8 · Dominio ambiental

La escala A0–A8 es la traducción de la jerarquía general E0– E8 al vocabulario del daño ecológico. Los rangos w reflejan la estructura epistémica específica del dominio: la evidencia científico-técnica (peritajes de dispersión, análisis ecotoxicológicos, modelado hidrológico) ocupa un lugar prominente y puede superar en utilidad a la documentación corporativa directa. Nivel A — rangos derivados por extensión desde los principios del sistema y la práctica del litigio ambiental; pendientes de calibración empírica formal.

Nivel Tipo de evidencia

Descripción y ejemplos en

Rango

el dominio ambiental

w

A1 Documento corporativo o regulatorio directo

Permisos de emisión con especificaciones que vinculan al operador, actas de inspección que documentan el incumplimiento, correos internos donde se tomó la decisión de reducir los estándares de seguridad, registros de monitoreo oficial que muestran la superación de límites permisibles con conocimiento del operador.

[0.74, 0.92]

A2 Peritaje científico-técnico de dispersión y atribución

Análisis forense de contaminación con trazado de la fuente, modelado de dispersión de contaminantes (hidrogeológico, atmosférico, sedimentológico), análisis ecotoxicológico que establece la relación dosis-respuesta, peritaje epidemiológico que establece la correlación entre exposición y daño en salud. Es frecuentemente el instrumento principal en el dominio ambiental.

[0.68, 0.87]

Taxonomía General de Aplicaciones

Nivel Tipo de evidencia

Descripción y ejemplos en

Rango

el dominio ambiental

w

A3 Monitoreo ambiental oficial convergente con análisis pericial

Registros de monitoreo de calidad del agua, suelo o aire de autoridades ambientales que muestran el patrón de contaminación, convergentes con al menos un análisis pericial que los vincula causalmente a la fuente. El patrón de monitoreo en el tiempo establece la trayectoria de la contaminación.

[0.50, 0.68]

A4 Correlación estadística controlada en datos de monitoreo

Análisis estadístico que muestra correlación significativa entre el patrón de operación del emisor y el patrón de contaminación en el ecosistema receptor, controlando por fuentes alternativas conocidas. La cadena causal directa no está probada pero la correlación es sólida y los factores de confusión están controlados.

[0.38, 0.58]

A5 Testimonios convergentes de comunidades afectadas con corroboración parcial

Testimonios de miembros de las comunidades afectadas sobre cambios observables en el ecosistema (desaparición de especies, cambio de color del agua, olores, enfermedades) que son convergentes entre sí y tienen al menos un elemento documental consistente aunque no prueba directa del vínculo causal.

[0.28, 0.48]

A6 Inferencia estructural por posición en el sistema productivo o regulatorio

El nodo tenía la posición operativa, la autoridad y el conocimiento técnico para saber que sus emisiones o sus estándares producirían el daño, sin documentación directa de la decisión

[0.18, 0.38]

Taxonomía General de Aplicaciones

Nivel Tipo de evidencia

Descripción y ejemplos en

Rango

el dominio ambiental

w

específica. Aplicable cuando la empresa destruyó registros o cuando el regulador nunca documentó la omisión.

A7 Correlación espacio-temporal sin modelado de dispersión

La proximidad geográfica entre el emisor y el daño sugiere causalidad, pero sin evidencia del mecanismo de dispersión ni de la cadena físico-química. La empresa está en el área, el daño está en el área, pero el vínculo causal no está modelado.

[0.07, 0.24]

A8 Estimación sin corroboración técnica

Única fuente sin respaldo técnico ni monitoreo corroborante. Solo se usa cuando no hay nada más y el contexto hace plausible la versión.

[0.04, 0.16]

A0 Ausencia documentada de conexión causal

Modelado de dispersión que demuestra que el contaminante del nodo no llegó al punto de daño bajo ningún escenario de condiciones ambientales razonables. Análisis que muestra que el nodo no operaba en el período del daño.

w = 0.00

### La jerarquía del peritaje científico en el dominio ambiental

En el dominio ambiental, la evidencia A2 (peritaje científico-técnico) frecuentemente supera en importancia operativa a la A1 (documentación corporativa directa) porque el vínculo causal entre la emisión y el daño es un hecho físico que el peritaje reconstruye independientemente de la documentación que el actor haya producido o destruido. Un análisis hidrogeológico que establece que el contaminante del nodo X

Taxonomía General de Aplicaciones

llegó al punto de daño Y bajo las condiciones ambientales del período relevante es evidencia más sólida que la ausencia de documentación interna del nodo — que puede deberse precisamente a que la documentación fue eliminada.

Cuando A2 contradice a A1 — el peritaje no confirma lo que los registros del operador declaran — se aplica la regla de prioridad del cap. U·2 con desplazamiento hacia el extremo conservador del rango A1. La contradicción es señal de investigación adicional, no de resolución automática a favor de la documentación corporativa.

### §3  Firmas documentales por Hijo e información para S

En el dominio ambiental, los Hijos de Afrodita informan S del actor específico — cuánto de su comportamiento era idiosincrático versus determinado por el marco regulatorio y económico en el que operaba. La distinción más relevante es entre Fobos (el operador actuó bajo un sistema de incentivos económicos que determinó el comportamiento: cualquier empresa en la misma posición habría actuado igual) y Anteros (el operador tomó decisiones específicas que excedían lo que el marco económico e incluso el marco regulatorio de su sector determinaban). S alto implica que el problema es del marco normativo, no de ese operador específico; S bajo implica que las prácticas idiosincráticas del operador eran la condición causal determinante.

§3.1 Hijos de legibilidad alta en el dominio ambiental

Taxonomía General de Aplicaciones

Firma en

Error de discrimina

Qué informa

Fuente document

el expediente

Hijo

ción frecuente

para S

al típica

ambiental

Fobo s

S alto [0.70, 0.90]. El sistema de incentivos económicos y el marco regulatorio determinaro n el comportami ento del operador: cualquier empresa con la misma tecnología disponible, bajo el mismo marco normativo y con los mismos incentivos de costo habría generado el mismo daño. El problema es del marco, no del operador específico.

Declaracion es que describen la decisión como inevitable dado el contexto económico y regulatorio: "los estándares que el sector usaba", "la tecnología disponible en el período". Evidencia de que el comportami ento del operador era común en el sector bajo las mismas condiciones regulatorias. Presión documenta da de costos desde la casa matriz que hacía inviable la alternativa más limpia.

Informes sectoriales que muestran el estándar de la industria en el período. Comunicaci ones internas sobre presión de costos. Comparació n con otras empresas del sector bajo el mismo marco normativo.

Confundir con Anteros cuando la empresa redujo estándares por debajo del promedio del sector. Si las prácticas del operador eran peores que las de sus pares bajo el mismo marco, S es moderado-bajo, no alto.

Deim os

S alto [0.75, 0.92]. La omisión del regulador: la

Ausencia de registros de inspección en períodos

Registros de inspección del regulador (o

Confundir con Anteros cuando el

Taxonomía General de Aplicaciones

Firma en

Error de discrimina

Qué informa

Fuente document

el expediente

Hijo

ción frecuente

para S

al típica

ambiental

agencia ambiental que no inspeccionó , que no actualizó los estándares cuando tenía evidencia de que eran insuficiente s, que procesó permisos rutinariame nte sin análisis de riesgo. La omisión era estructural mente producida por el marco institucional del regulador.

donde la normativa los requería. Aprobacion es rutinarias de permisos sin análisis de riesgo en expedientes que deberían tenerlo. Silencio documental ante alertas de organismos técnicos que llegaron al regulador.

ausencia de ellos). Expediente s de permisos con su contenido técnico. Comunicaci ones de organismos técnicos al regulador que quedaron sin respuesta documenta da.

regulador tomó decisiones discrecional es específicas que excedieron su omisión rutinaria — por ejemplo, reclasificar zonas de protección para facilitar una operación específica. Eso es Anteros del regulador con S bajo.

Anter os

S bajo [0.08, 0.32]. El operador tomó decisiones idiosincrátic as que excedían lo que el marco económico y el marco regulatorio del sector determinab

Documento s que muestran que las prácticas del operador eran inferiores al estándar de la industria bajo las mismas condiciones . Decisiones de

Informes técnicos internos que describían el riesgo antes del daño. Correos de ingenieros o técnicos objetando las reducciones de estándar.

Confundir Anteros con el resultado del daño. El hecho de que el daño ocurrió no implica Anteros: hay que verificar si las prácticas del operador

Taxonomía General de Aplicaciones

Firma en

Error de discrimina

Qué informa

Fuente document

el expediente

Hijo

ción frecuente

para S

al típica

ambiental

an: reducciones de costo que sus propios pares de sector no adoptaron, eliminación de sistemas de seguridad que sus competidor es mantuviero n, omisión de mantenimie nto que el estándar de la industria exigía. La condición causal idiosincrátic a del daño fue la decisión específica de ese operador.

reducción de costos que los propios ingenieros de la empresa objetaron. Comparació n con pares del sector que operaban con las mismas presiones económicas y no produjeron el mismo daño.

Datos comparativ os con empresas pares del sector en el mismo período.

diferían del estándar del sector. Si no diferían, S es alto aunque el daño fuera grave.

### §3.2 Hijos de legibilidad baja en el dominio ambiental

Potós: puede aparecer cuando el operador replicó prácticas heredadas de una gestión anterior sin cuestionarlas — la planta que siguió operando exactamente igual que siempre, sin actualizar sus estándares a pesar de que la evidencia científica sobre los daños de sus emisiones había cambiado. Informa S moderado-alto, pero es indistinguible de Deimos disfrazado

Taxonomía General de Aplicaciones

de tradición operativa. La pregunta discriminante: ¿el operador tenía información técnica de que sus prácticas producían el daño? Si la tenía y no actuó, puede ser Deimos. Asignar con nota obligatoria de incertidumbre alta.

Eros: puede aparecer cuando el operador adoptó nuevas tecnologías o procesos de manera proactiva y genuinamente convencida de que eran más eficientes, sin anticipar que producirían daño ambiental. La apertura hacia la innovación era genuina, el daño no estaba en el mapa de consecuencias del actor. Informa S moderado. Asignar con nota obligatoria de incertidumbre alta.

§3.3 Harmonía — irrelevante para los actores institucionales del dominio ambiental Las empresas y los reguladores son egos colectivos, no sujetos individuales con v_t localizable. Para los actores institucionales de este dominio, el análisis del Hijo se aplica solo si hay un actor individual identificable — el directivo que tomó la decisión específica, el funcionario que omitió la inspección. Para el ego colectivo institucional, S se estima directamente por Ruta B (escala DS del cap. U·3) desde la evidencia documental de la determinación sistémica del acto.

### §4  ¿Qué cuenta como asunción (α) en el dominio ambiental?

α en el dominio ambiental mide el grado en que el actor ha actuado sobre su posición causal mediante acciones concretas y verificables: remediación del daño producido, prevención de daño futuro, modificación del sistema que lo causó. α mide acciones, no declaraciones, compromisos sin ejecución ni programas de imagen.

α es completamente independiente del dolo en el dominio ambiental Un operador que contaminó deliberadamente puede tener α alto si después remedió proporcional a su R*. Un operador que contaminó sin intención

Taxonomía General de Aplicaciones

deliberada — porque el marco regulatorio lo permitía — puede tener α = 0 si nunca implementó ninguna medida de remediación ni prevención. Los Hijos informan S (idiosincrasia del acto); α mide lo que el actor hizo después sobre su posición causal.

### α voluntario, forzado e impuesto en el contexto ambiental

En el dominio ambiental, α forzado e impuesto es frecuente: las órdenes de remediación de autoridades ambientales, las sentencias de tribunales que imponen planes de limpieza, y las multas administrativas proporcionales al daño son α impuesto que el método registra igual que el α voluntario. Si el operador pagó la multa porque la autoridad ambiental se la impuso, su α sube igual que si la hubiera pagado voluntariamente.

Acción del

¿Cuenta para

α? Razón Tipo de α

actor

Remediación del suelo, agua o hábitat dañado con verificación técnica del resultado

Sí — α máximo

La forma más completa de α ambiental. Reconocimiento con reparación verificable del ecosistema.

Voluntari o o forzado por sentencia

Pago de multas administrativa s proporcionales al daño documentado

Sí — bajo a moderado

α forzado económico. Su nivel depende de la proporción de la multa respecto al AD_i = R*_i × D_total.

Forzado / impuesto

Adopción de tecnología más limpia que reduce emisiones futuras

Sí — α estructural de prevención

Reduce la probabilidad del próximo evento. La asunción preventiva tiene valor independiente de la remediación.

Voluntari o o requerido por regulación

Taxonomía General de Aplicaciones

Acción del

¿Cuenta para

α? Razón Tipo de α

actor

Plan de contingencia implementado con protocolos verificables

Sí — α estructural

Modifica el sistema que podría producir el daño futuro.

Voluntari o o impuesto

Compensación a comunidades afectadas proporcional al AD_i de la empresa

Sí — moderado a alto

Asunción económica directa hacia los afectados.

Voluntari o o negociado

No Declaración sin consecuencia concreta sobre la posición causal. No modifica α.

—

Publicar un informe de sostenibilidad sin modificar el sistema de emisiones

—

Comprar bonos de carbono sin reducir emisiones propias

No modifica α del daño propio — puede ser α de compensació n sistémica

La compra de bonos no modifica la posición causal del emisor sobre el daño que ya produjo.

Sí — bajo α real pero desproporcionado : el actor eligió asumir la parte más barata sin proporcionalidad a R*.

Remediación parcial de la zona menos dañada mientras la más dañada permanece sin tratar

Voluntari o selectivo — señal de alerta

### La escala de α en el dominio ambiental

### Rangos derivados por extensión de los principios del sistema. Pendientes de calibración empírica.

Taxonomía General de Aplicaciones

Descripción observable en el

Nivel Rango

Indicadores

α

verificables

dominio ambiental

Negación / evasión total

0.00 – 0.05 El operador niega su contribución al daño, combate activamente el proceso ambiental y no ha implementado ninguna medida de remediación ni prevención. El proceso regulatorio o judicial está activo sin acciones concretas.

Sin pagos, sin remediación, sin modificaciones del sistema de emisiones, sin reconocimiento ante la autoridad ambiental. Recurso activo de todas las resoluciones sin acciones paralelas.

Reconocimiento nominal

0.06 – 0.20 El operador reconoció formalmente su contribución, pero sin consecuencia concreta. Declaraciones de "compromiso ambiental", informe de sostenibilidad, "lamentamos el impacto" sin remediación.

Comunicados públicos documentados. Informes de sostenibilidad. Ninguna remediación verificable. Multas no pagadas o recurridas.

Asunción parcial

### 0.21 – 0.45 El operador pagó multas o implementó medidas de remediación menores a lo que su R* indica. Hay acciones concretas pero la proporcionalidad

Multas administrativas pagadas equivalentes al 10–30% del daño. Remediación de zonas menores o más accesibles. Planes de contingencia

Taxonomía General de Aplicaciones

Descripción observable en el

Nivel Rango

Indicadores

α

verificables

dominio ambiental

está muy lejos del AD_i.

aprobados pero no completamente implementados.

Asunción activa en proceso

0.46 – 0.70 El operador está en proceso activo de remediación con acciones concretas y verificables. Las acciones son sustanciales aunque no hayan alcanzado la proporcionalidad completa del AD_i.

Remediación del 40–60% del área afectada verificada por peritaje. Planes de remediación aprobados y en ejecución con seguimiento técnico. Compensaciones parciales a comunidades en proceso de pago.

Asunción funcional

### 0.71 – 0.89 El operador ha asumido la mayor parte de su posición. Las acciones de remediación son proporcionales a su R* aunque no perfectas.

Remediación del 70–85% del área documentada con verificación técnica. Compensaciones sustanciales pagadas a las comunidades afectadas. Modificación verificable del sistema de emisiones con datos de mejora.

Asunción plena 0.90 – 1.00 El operador asumió completamente su posición causal. La remediación es proporcional a su R*, el sistema que

Remediación completa certificada por peritaje independiente. Compensación integral a comunidades.

Taxonomía General de Aplicaciones

Descripción observable en el

Nivel Rango

Indicadores

α

verificables

dominio ambiental

produjo el daño fue modificado estructuralmente y hay seguimiento verificable de resultados distintos.

Modificación del sistema de emisiones con datos verificables de reducción sostenida. Reconocimiento formal de la posición causal ante la autoridad.

### Δ y el déficit de remediación

Δ_i = R*_i − α_i (en R* convencional) o Δ_i = φᵢ − α_i (en Shapley) mide la brecha entre la contribución causal al daño y la remediación implementada. Δ positivo es la base técnica para la acción de responsabilidad ambiental y para las órdenes de remediación proporcionales. La orden de remediación técnicamente justificada es: Orden_remediación_proporcional_i = R*_i × (1 − S_i) × D_total.

La irreversibilidad y el límite de la compensación monetaria Algunos daños ecológicos son irreversibles: la extinción de especies, la destrucción de ecosistemas únicos, el daño permanente a comunidades culturalmente arraigadas en un territorio. Para estos daños, D_monetary_equiv puede ser calculable pero la promesa de reparación monetaria es ontológicamente vacía. El sistema reconoce honestamente este límite: D_monetary_equiv no es lo que se debe pagar — es la medida de la magnitud del daño. Cuando esa magnitud supera cualquier capacidad de compensación, la fórmula cumple su función más importante, que es hacer visible la inconmensurabilidad entre el daño y cualquier reparación finita posible.

Taxonomía General de Aplicaciones

### §5  Construcción del grafo típico del dominio ambiental

### Tipos de nodo en el grafo ambiental

Ejemplo en el

Tipo Función en el

grafo S típico

dominio ambiental

Operador directo (Op)

La empresa u organización que opera la fuente de contaminación. Causa inmediata del daño. R* alto cuando es condición necesaria. S mide si cualquier otra empresa bajo las mismas condiciones habría actuado igual.

Variable [0.20–0.85]

La filial que opera la planta con los estándares comprometidos. El operador del pozo que produce el derrame. La empresa que vierte los residuos.

Diseñador / casa matriz (D)

La empresa que diseñó la tecnología, estableció los estándares de seguridad y aprobó las reducciones de costo. R* del nodo de diseño es comparable o mayor que el del operador cuando las decisiones de diseño eran condición causal del daño.

Bajo-moderado [0.15–0.50]

La casa matriz que diseñó la tecnología con riesgo conocido. La dirección corporativa que aprobó los estándares rebajados. La empresa que estableció el protocolo de operación deficiente.

Taxonomía General de Aplicaciones

Ejemplo en el

Tipo Función en el

grafo S típico

dominio ambiental

Regulador / gobierno (Reg)

El Estado que autorizó la operación, reguló las condiciones de seguridad y tenía obligación de inspeccionar. R* positivo cuando el regulador aprobó condiciones que el sistema no debería haber tolerado, o cuando la omisión de inspección fue condición del daño.

Alto [0.55– 0.85] La agencia ambiental que no inspeccionó. El gobierno que asentó comunidades en zona de riesgo conocido. El ministerio que aprobó el permiso sin análisis de riesgo adecuado.

Factor ambiental (FA)

Las condiciones del ecosistema receptor que determinaron la dispersión y el impacto del contaminante: dirección del viento, corrientes de agua, características del suelo, densidad de población. No tiene R* en sentido de responsabilidad — no es un actor — pero sus condiciones son parte del grafo causal y

N/A — no es actor

Dirección del viento que dirigió el contaminante hacia la comunidad. Corriente subterránea que transportó el lixiviado. Características del suelo que facilitaron la absorción.

Taxonomía General de Aplicaciones

Ejemplo en el

Tipo Función en el

grafo S típico

dominio ambiental

determinan la magnitud del daño dado el nivel de emisión.

Comunidad afectada (Nf)

El receptor del daño: las personas, comunidades y ecosistemas que sufrieron las consecuencias. No entra en el cálculo de R* del daño salvo cuando contribuyó causalmente — caso inusual dado la asimetría de información entre el operador y la comunidad sobre el riesgo.

Generalmente no aplica

La comunidad indígena cuyo territorio fue contaminado. La población cuya fuente de agua fue afectada. Los ecosistemas acuáticos dañados por el vertido.

### Tipos de arista en el grafo ambiental

Arista directa de emisión o vertido: conecta el operador directo con el daño mediante el proceso físico de contaminación. Sustentada por A2 (peritaje de dispersión que traza la huella del contaminante) o A1 (registros de emisiones del propio operador).

Arista estructural de diseño: conecta la casa matriz con el daño mediante los estándares, la tecnología y las decisiones de reducción de costo que diseñó. Sustentada por A1 (documentos internos de decisión) o A4/A6 (inferencia desde

Taxonomía General de Aplicaciones

la comparación con estándares alternativos disponibles en el período).

Arista de omisión regulatoria: conecta el regulador con el daño mediante la inacción documentada. Requiere: (1) deber de inspeccionar o regular documentado en normativa; (2) evidencia de que el regulador tenía o debía tener información del riesgo. Sin ambos elementos, la arista de omisión no tiene sustento.

Arista de amplificación ambiental: conecta el factor ambiental (FA) con la magnitud del daño. No tiene R* propio, pero pondera la proporcionalidad del daño — el mismo nivel de emisión produce daños de distinta magnitud según las condiciones ambientales del receptor.

Configuraciones canónicas del grafo ambiental

Configuración 1 — Desastre industrial puntual (R* convencional) D (casa matriz / estándares) → Op (operador directo / proceso de producción) + Reg (regulador omisivo) → FA (condiciones ambientales) → Daño en Nf Al menos un actor — típicamente la combinación Op + D — es condición necesaria del daño. R* convencional es el instrumento correcto. La distribución entre D y Op depende de si el operador actuaba dentro de los estándares aprobados por D (R* de D alto) o por debajo (R* compartido con distribución dependiente de cuánto D sabía y no actuó).

Configuración 2 — Contaminación acumulativa por múltiples operadores (Shapley) Op₁ (operador 1, período t₁-t₂) + Op₂ (operador 2, período t₂-t₃) + Op₃ (fuentes difusas) → Daño acumulado en Nf Ningún operador individual es condición necesaria: el daño habría ocurrido de todas formas por la suma de las otras fuentes. R* convencional asigna cero a todos — técnicamente correcto, pero jurídicamente inaplicable. Shapley distribuye la responsabilidad proporcional a la contribución marginal

Taxonomía General de Aplicaciones

promedio de cada operador sobre todas las posibles coaliciones. La función de valor v(S) para cada coalición se estima con los datos de monitoreo y el modelado de dispersión.

Configuración 3 — Responsabilidad de casa matriz multinacional D_matriz (casa matriz / diseñadora de estándares, jurisdicción A) → Op_filial (filial operadora, jurisdicción B) → Daño en Nf (jurisdicción B) La separación jurídica entre casa matriz y filial no elimina la arista causal. La condición para que D_matriz tenga R* positivo: las decisiones de D_matriz (tecnología, estándares, reducción de costos) eran condición causal del daño — sin esas decisiones, el daño no habría ocurrido en esa forma. El análisis de S de la filial determina cuánto de su comportamiento era determinado por las instrucciones de D_matriz.

### §6  Preguntas que responde este capítulo

Nivel de

Pregunta

del caso Instrumento que la responde

certeza posible

¿El daño tiene un actor condición necesaria o es acumulativo — R* o Shapley?

Diagnóstico previo: ¿Habría ocurrido el daño sin este actor dado lo que los otros habrían producido? Si no → R*. Si sí → Shapley. Ver §9, primera rama del árbol de decisión.

La respuesta a esta pregunta diagnóstica determina el instrumento. No es una Declaración en sí misma pero condiciona todas las que siguen.

¿La casa matriz tiene R* positivo aunque solo la filial operara la instalación?

R* positivo de D_matriz si sus decisiones (tecnología, estándares, reducciones de costo) eran condición causal del daño. Arista D_matriz → daño sustentada por A1 (documentos internos) o A4/A6 (comparación con pares del sector).

Declaración A o B si hay documentos internos A1 de las decisiones de la casa matriz. Declaración C

Taxonomía General de Aplicaciones

Nivel de

Pregunta

del caso Instrumento que la responde

certeza posible

si la inferencia es A6.

¿El regulador que no inspeccionó tiene R* significativo por su omisión?

Arista de omisión del regulador: deber de inspeccionar documentado en normativa (A1) + evidencia de que tenía o debía tener información del riesgo (A3 o A5). Si ambos están presentes, R* del regulador es positivo.

Declaración A si el deber está en normativa y la omisión está documentada. Declaración C si el deber es inferido o el conocimiento del riesgo es indirecto.

¿Cuánto del daño es proporcional a la contribución de cada operador en un caso acumulativo ?

Declaración B si los datos de monitoreo y el modelado de dispersión permiten estimar v(S) con buena precisión. Declaración C si v(S) de las coaliciones parciales requiere estimaciones contrafácticas con alta incertidumbre .

Valores de Shapley: φᵢ = contribución marginal promedio del actor i sobre todas las posibles coaliciones. Requiere estimación de v(S) para las coaliciones parciales. La suma Σφᵢ = D_total verifica la eficiencia.

¿S alto del operador implica que la reforma debe ser normativa, no una orden de remediación

S alto del operador (cualquier empresa bajo el mismo marco habría actuado igual) implica que el problema es del marco regulatorio, no de ese operador específico. La orden contra el operador es justa pero insuficiente si el marco no cambia.

Declaración A o B si la comparación con pares del sector está documentada con A3 o A4. Declaración C si la

Taxonomía General de Aplicaciones

Nivel de

Pregunta

del caso Instrumento que la responde

certeza posible

solo contra ese operador?

comparación es inferida.

¿La compra de bonos de carbono por el operador modifica su α?

No en el sentido de α del daño propio. La compra de bonos no remedia la posición causal del operador sobre el daño que ya produjo. α requiere acciones sobre la posición causal específica: remediación, modificación del sistema de emisiones, compensación a las comunidades afectadas.

Declaración A — la distinción es conceptual y no depende de evidencia adicional.

¿Cuál es la orden de remediación técnicament e proporcional al R* del operador?

Orden_remediación_proporcional_ i = R*_i × (1 − S_i) × D_total. La proporción (1 − S_i) refleja que solo la fracción idiosincrática de la contribución del operador justifica la orden sobre ese operador específico; la fracción S_i corresponde al marco regulatorio que el conjunto del sector debe modificar.

Depende de la calidad de R* y S. Declaración A si la evidencia es A1/A2. Declaración B o C si hay componentes de inferencia estructural.

### §7  Traducción de D_total al dominio ambiental

Los servicios ecosistémicos son tiempo de vida cristalizado de las comunidades que dependen de esos ecosistemas para subsistir. Cuando una comunidad pierde su suelo cultivable, su fuente de agua o sus recursos pesqueros por daño ambiental, cada año de pérdida de esos servicios es trabajo no recompensado, subsistencia no posible y salud deteriorada. D_vital = D_total / w_ref captura esa dimensión: el daño ambiental siempre es también un daño a la economía del tiempo de vida de las comunidades afectadas.

Taxonomía General de Aplicaciones

Definición

Component

en el dominio ambiental

Cómo se

Fuente de

e

mide

evidencia

T_invertido (daño inmediato)

Pérdida directa en el momento del evento o en el período inicial de contaminació n: muertes, lesiones agudas documentadas , destrucción de activos naturales (hábitat, suelo, agua), costos de atención médica de urgencia, pérdida inmediata de medios de subsistencia de las comunidades.

Inventario de daños documentados con registros médicos y ambientales. Costo de atención médica de urgencia. Valoración de activos naturales destruidos usando métodos de costo de reemplazo.

Registros médicos de la emergencia. Inventarios ambientales antes y después del evento. Peritaje de daños físicos inmediatos.

T_impedido (pérdida de servicios ecosistémicos durante el período de contaminació n activa)

Pérdida de los servicios que el ecosistema dañado proveía durante el período en que la contaminació n impidió su funcionamient o normal: agua potable no disponible, suelo no cultivable, recursos

Valoración económica de los servicios ecosistémicos perdidos por año, multiplicada por el período de contaminación activa. Métodos: costo de reemplazo, preferencia revelada (cuánto

Estudios de valoración de servicios ecosistémicos. Registros de producción agrícola, pesquera o turística antes y durante la contaminación . Facturas de alternativas que las comunidades debieron pagar.

Taxonomía General de Aplicaciones

Definición

Component

en el dominio ambiental

Cómo se

Fuente de

e

mide

evidencia

pesqueros no cosechables, ecoturismo imposible. Es la pérdida de flujos de servicios durante el período de contaminació n activa.

pagaron las comunidades por alternativas), valoración contingente.

ΔT_trayectori a (pérdida permanente o de muy largo plazo)

La diferencia entre el estado del ecosistema y de las comunidades si no hubiera ocurrido el daño y el estado real: pérdida permanente de biodiversidad, daño irreversible a ecosistemas únicos, reducción permanente de la esperanza de vida de las comunidades expuestas, daño generacional en salud. Es el componente dominante en los daños de largo plazo.

Modelos de recuperación ecológica con y sin remediación. Estudios epidemiológic os de largo plazo sobre el diferencial de esperanza de vida y de morbilidad entre la comunidad expuesta y una comparable sin exposición. Valoración de la pérdida permanente de biodiversidad mediante disposición a pagar.

Estudios epidemiológic os longitudinales. Modelos de recuperación ecológica de largo plazo. Censos de biodiversidad antes y después del daño con proyección de recuperación.

Taxonomía General de Aplicaciones

D_vital ambiental y la dualidad ontológica del daño ecológico D_vital = D_total / w_ref convierte el daño ambiental a horas de vida de las comunidades afectadas. Un año de pérdida de la fuente de agua de una comunidad es el equivalente en trabajo, salud y subsistencia de N personas × 8,760 horas × (1 − q), donde q es la fracción de las condiciones de vida que se mantuvieron sin la fuente de agua. Para los daños con componente de pérdida permanente de biodiversidad o de ecosistemas únicos: D_monetary_equiv puede ser calculable pero la promesa de reparación monetaria es ontológicamente vacía. La fórmula cumple su función más importante — hacer visible que el daño es inconmensurable con cualquier reparación finita posible — sin pretender que el resultado sea el monto que se puede exigir. El monto jurídicamente exigible es proporcional al AD_i del operador sobre la fracción del daño que es monetariamente cuantificable.

### §8  Límites del método y errores frecuentes de aplicación

Límites del método en el dominio ambiental

Límite 1 — El postulado de la condición necesaria en causalidad acumulativa. Cuando el daño es acumulativo y ningún actor es individualmente condición necesaria, R* convencional asigna cero a todos los actores — técnicamente correcto, pero jurídicamente inaplicable. La extensión Shapley resuelve este límite cuando la función de valor v(S) puede estimarse con datos suficientes. Si v(S) no puede estimarse, la Declaración es C o D.

Límite 2 — La incertidumbre en los datos de dispersión. El cálculo de R* y de los valores de Shapley en el dominio ambiental requiere estimar cuánto del daño observado es atribuible a cada fuente. En daños de largo plazo, esa atribución requiere modelos de dispersión con incertidumbre inherente. El resultado debe siempre presentarse como un rango, no como un valor puntual.

Límite 3 — La función de valor v(S) de las coaliciones parciales no siempre es estimable. El cálculo de Shapley requiere v(S) para todas las coaliciones posibles.

Taxonomía General de Aplicaciones

Frecuentemente solo el daño del conjunto completo v(N) es observable, mientras que los daños de las coaliciones parciales deben estimarse con modelos contrafácticos. Esa estimación tiene incertidumbre que se propaga a los valores de Shapley calculados.

Límite 4 — La irreversibilidad y la limitación de la compensación monetaria. Algunos daños ecológicos son irreversibles. Para estos, D_monetary_equiv no es lo que se puede exigir como reparación: es la medida de la magnitud del daño. El analista que presenta D_monetary_equiv de un daño irreversible como el monto de la pretensión jurídica está fuera del alcance del método.

### Errores frecuentes de aplicación

Error Por qué

Consecuen

cia Corrección

ocurre

Usar R* convencional cuando el daño es acumulativo y ningún actor es condición necesaria

El analista aplica el instrumento estándar sin verificar si el postulado I5 se cumple.

R* convencion al asigna cero a todos los actores — resultado jurídicamen te inútil. El análisis produce Declaración D cuando debería producir Declaración B con Shapley.

Verificar antes de calcular: ¿habría ocurrido el daño sin este actor dado lo que los otros habrían producido? Si sí → Shapley.

No incluir la casa matriz en el grafo porque solo la filial

El analista sigue la estructura jurídica de separación

R* de la casa matriz = 0 aunque sus decisiones de

Construir el grafo desde el resultado hacia atrás. Preguntar: ¿sin

Taxonomía General de Aplicaciones

Error Por qué

Consecuen

cia Corrección

ocurre

operó la instalación

entre casa matriz y filial sin preguntar si la casa matriz es nodo causal.

tecnología y estándares fueran condición causal del daño. La responsabili dad recae solo sobre la filial.

las decisiones de la casa matriz el daño habría ocurrido en esta forma?

No incluir el regulador en el grafo por la dificultad de probar la omisión

Las aristas de omisión son difíciles. El analista incluye solo al operador.

R* del regulador = 0 aunque su omisión de inspección fuera condición del daño. El operador carga con la totalidad del R* que correspond e distribuir entre operador y regulador.

Para cada actor con deber documentado de actuar: ¿tenía información del riesgo? ¿Actuó? Si no → incluir arista de omisión con el nivel disponible y declarar su certeza.

Aceptar la compra de bonos de carbono como α del daño ambiental propio

El analista registra el gasto en bonos como acción sobre la posición causal.

α sobreestima do. Δ subestimad o. El operador no ha remediado su posición causal pero aparece con α moderado.

α del daño propio requiere acciones sobre esa posición causal específica. Los bonos de carbono son compensación de otro daño (emisiones propias de CO₂), no remediación del daño ecológico

Taxonomía General de Aplicaciones

Error Por qué

Consecuen

cia Corrección

ocurre

directo analizado.

Presentar D_monetary_e quiv del daño irreversible como el monto de la pretensión jurídica

El analista calcula D_monetary_e quiv y lo usa directamente como pretensión.

La pretensión es numéricame nte imposible de satisfacer y puede desacreditar el análisis completo.

D_monetary_e quiv de daños irreversibles es la medida de la magnitud ontológica del daño, no el monto exigible. El monto exigible es AD_i = R*_i × D_cuantificabl e sobre la fracción monetariament e cuantificable.

### §9  Guía de prioridades de recolección de evidencia

### La primera pregunta del análisis ambiental — ¿R* o Shapley? — condiciona todo lo demás. El árbol de decisión comienza aquí.

### Tabla de prioridades de recolección de evidencia ambiental

Si tu incertidu

La evidencia

Qué buscar /

Qué rango reduce

Por qué funciona

mbre principal

que más la reduce

qué preguntar

es…

es…

### 1. ¿R* convencio

Evidencia de que el

Si el modelado

Determin a el

¿Operaban otras

Taxonomía General de Aplicaciones

Si tu incertidu

La evidencia

Qué buscar /

Qué rango reduce

Por qué funciona

mbre principal

que más la reduce

qué preguntar

es…

es…

nal o Shapley — hay actores condición necesaria?

daño habría ocurrido (o no) sin el actor específico dado lo que los otros habrían producido. Monitoreo ambiental de zonas comparabl es sin ese actor (A3/A4). Modelos de dispersión de las otras fuentes sin la contribució n del actor analizado (A2).

muestra que el daño habría ocurrido igualment e sin el actor → Shapley. Si muestra que el daño habría sido sustancial mente menor → R* convencio nal.

instrumen to de imputació n — decisión fundamen tal

fuentes de contaminac ión del mismo tipo en el área? ¿El daño hubiera ocurrido con esas fuentes solas? ¿El modelado de dispersión puede correr el escenario sin este actor?

### 2. ¿La arista entre el emisor y el punto de daño existe — modelo de dispersión ?

Peritaje de dispersión A2: modelado hidrológico , atmosféric o o sedimentol ógico que traza la trayectoria del contamina nte desde el punto de

Sin el modelo de dispersión, la arista entre el emisor y el daño es inferencia espacial A7 con w bajo [0.07– 0.24]. Con el modelo, la arista es A2 con w

Reduce rango de w de la arista principal (incertidu mbre empírica)

¿Existe un peritaje de dispersión del contamina nte específico bajo las condicione s ambientale s del período? ¿Los datos de monitoreo

Taxonomía General de Aplicaciones

Si tu incertidu

La evidencia

Qué buscar /

Qué rango reduce

Por qué funciona

mbre principal

que más la reduce

qué preguntar

es…

es…

emisión hasta el punto de daño bajo las condicione s ambientale s del período.

[0.68– 0.87]. muestran el patrón de propagació n del contamina nte?

### 3. ¿La casa matriz tiene R* positivo — decisiones de diseño y estándares ?

Document os A1 de las decisiones de la casa matriz: tecnología diseñada, estándares establecido s, decisiones de reducción de costo que comprome tieron la seguridad. Comparaci ón A4 con los estándares que el sector usaba para verificar que las decisiones de la casa matriz eran por debajo

La casa matriz tiene R* positivo cuando sus decisiones eran condición causal — sin ellas el daño no habría ocurrido en esa forma. La comparaci ón con el estándar del sector determina si las decisiones eran idiosincrát icas (S bajo del D_matriz) o no.

Reduce rango de R* de la casa matriz (incertidu mbre empírica)

¿La casa matriz diseñó la tecnología? ¿Aprobó las reduccione s de costo que comprome tieron los sistemas de seguridad? ¿Las prácticas resultantes eran inferiores al estándar del sector?

Taxonomía General de Aplicaciones

Si tu incertidu

La evidencia

Qué buscar /

Qué rango reduce

Por qué funciona

mbre principal

que más la reduce

qué preguntar

es…

es…

del estándar.

### 4. ¿El regulador tiene R* por omisión — deber y conocimie nto simultáne os?

Dos elementos simultáneo s: (a) normativa que establece el deber de inspeccion ar o regular (A1); (b) evidencia de que el regulador tenía o debía tener informació n del riesgo — alertas técnicas, denuncias recibidas, informes de otros organismos (A3/A5).

La arista de omisión requiere ambos elementos. Sin el deber document ado, la omisión no es condición causal. Sin el conocimie nto document ado, la arista es inferida (A6).

Reduce rango de R* del regulador (incertidu mbre empírica)

¿La normativa establecía la obligación de inspeccion ar en el período? ¿El regulador recibió alertas, denuncias o informes técnicos sobre el riesgo? ¿Hay registro de que esas comunicaci ones llegaron?

### 5. ¿S del operador — las prácticas eran idiosincrát icas o estándar del sector?

Comparaci ón A3/A4 entre las prácticas del operador y el estándar del sector bajo las mismas condicione s regulatorias

S alto implica que el problema es del marco regulatorio : la reforma debe ser normativa, no solo contra ese

Reduce rango de S del operador (incertidu mbre ontológic a)

¿Otras empresas del mismo sector, bajo el mismo marco, actuaron de manera diferente? ¿El operador adoptó reduccione

Taxonomía General de Aplicaciones

Si tu incertidu

La evidencia

Qué buscar /

Qué rango reduce

Por qué funciona

mbre principal

que más la reduce

qué preguntar

es…

es…

y económica s. Si otros operadores bajo el mismo marco actuaron igual → S alto. Si las prácticas del operador eran inferiores al estándar → S moderado-bajo.

operador. S bajo implica que las decisiones idiosincrát icas del operador eran la condición causal determina nte.

s de costo que sus pares no adoptaron? ¿Los propios ingenieros del operador objetaron las decisiones?

### 6. ¿v(S) de las coalicione s — para el cálculo de Shapley?

Datos de monitoreo ambiental por zona y por período que permitan estimar la contribució n de cada fuente en ausencia de las otras. Modelado de dispersión por fuente individual A2. Análisis de superposici ón

Shapley requiere v(S) para cada coalición posible. Si solo se tiene v(N) (el daño total), Shapley necesita estimacion es contrafácti cas. Cuanto más precisas sean las estimacion es de v(S) parciales,

Determin a la calidad de la Declaraci ón en el análisis Shapley

¿Hay datos de monitoreo que permitan aislar la contribució n de cada fuente? ¿El modelo de dispersión puede correr escenarios sin uno o varios de los actores? ¿Hay zonas del ecosistema influenciad as por una sola fuente

Taxonomía General de Aplicaciones

Si tu incertidu

La evidencia

Qué buscar /

Qué rango reduce

Por qué funciona

mbre principal

que más la reduce

qué preguntar

es…

es…

geográfica de zonas de influencia de cada operador.

más estrecho es el intervalo de confianza de φᵢ.

que sirvan de referencia?

### 7. ¿α del operador — qué remediaci ón real ha ocurrido?

Verificació n técnica independie nte del estado de remediació n: peritaje del área remediada versus el área total afectada (A2). Registros de pagos a comunidad es versus AD_i estimado. Datos de monitoreo post-remediació n que muestren recuperació n verificable del ecosistema.

α mide remediaci ón efectiva, no compromi sos ni planes. El peritaje de verificació n del estado post-remediaci ón es la fuente de evidencia para α, no las declaracio nes del operador.

Reduce rango de α del operador (incertidu mbre empírica)

¿Hay peritaje independie nte del estado del área afectada después de las medidas de remediació n? ¿La recuperació n del ecosistema es verificable con datos de monitoreo? ¿Los pagos a las comunidad es son proporcion ales al AD_i estimado?

### Árbol de decisión ambiental: ¿qué buscar primero?

Taxonomía General de Aplicaciones

### El árbol comienza con la decisión entre R* y Shapley — que es la más importante y la que condiciona todo el análisis posterior.

¿Cuál es tu principal incertidumbre?

├─ ¿R* o Shapley — primera decisión del análisis? │

└─  PRIORIDAD 1: Verificar si algún actor es condición necesaria del daño.

· Pregunta de diagnóstico: ¿Habría ocurrido el daño sin este actor dado lo que los otros habrían producido? · Si NO → R* convencional. Al menos un actor es condición necesaria. Calcular R* con el grafo completo. · Si SÍ → Shapley. El daño es acumulativo. Necesitas estimar v(S) para las coaliciones parciales. · Si no puedes determinarlo → buscar modelado de dispersión A2 que corra el escenario sin el actor analizado.

├─ [R* CONVENCIONAL] ¿Sobre la arista entre el emisor y el punto de daño? │

└─  PRIORIDAD: Obtener peritaje de dispersión A2.

· Sin modelo de dispersión → arista A7, w en [0.07– 0.24]. Declaración C. · Con modelo de dispersión → arista A2, w en [0.68– 0.87]. Declaración B probable. · El modelo debe correr con las condiciones ambientales del período del daño (dirección del viento, caudales, etc.).

├─ [R* CONVENCIONAL] ¿Sobre R* de la casa matriz — sus decisiones eran condición causal? │

└─  PRIORIDAD: Buscar documentos A1 de decisiones de diseño y estándares de la casa matriz.

· ¿La casa matriz diseñó la tecnología? ¿Aprobó las reducciones de estándar? · Comparar con el estándar del sector A4: ¿las decisiones de la casa matriz estaban por debajo del estándar?

Taxonomía General de Aplicaciones

· Si sí → S bajo de la casa matriz, R*_neta alto. Incluir como nodo D en el grafo.

├─ [R* CONVENCIONAL] ¿Sobre R* del regulador por omisión? │

└─  PRIORIDAD: Verificar los dos elementos de la omisión simultáneamente.

· Elemento 1 — deber: ¿La normativa establecía obligación de inspeccionar en el período? · Elemento 2 — conocimiento: ¿El regulador recibió alertas, denuncias o informes técnicos sobre el riesgo? · Si ambos → arista de omisión A1/A3. R* del regulador significativo. Declaración A o B. · Si solo uno → arista de omisión A6. Declaración C para esa arista.

├─ [SHAPLEY] ¿Sobre v(S) de las coaliciones — datos para el cálculo? │

└─  PRIORIDAD: Buscar datos de monitoreo que permitan aislar la contribución de cada fuente.

· ¿Hay zonas del ecosistema influenciadas por una sola fuente que sirvan de referencia calibrada? · ¿El modelo de dispersión puede correr escenarios sin uno o varios actores para estimar v(S) de las coaliciones parciales? · Si hay datos suficientes → Shapley con Declaración B. Si las coaliciones parciales requieren estimaciones contrafácticas con alta incertidumbre → Declaración C.

└─ ¿Sobre α del operador — qué remediación real ha ocurrido?

└─  PRIORIDAD: Obtener peritaje independiente del estado de remediación.

· ¿Hay verificación técnica independiente del área remediada versus el área total afectada? · ¿Los datos de monitoreo post-remediación muestran recuperación verificable del ecosistema?

Taxonomía General de Aplicaciones

· ¿Los pagos a comunidades son proporcionales al AD_i estimado (R*_i × D_total)? · Declaraciones sin peritaje de verificación no modifican α. α solo sube con evidencia A1/A2 de la remediación efectiva.

— Fin del Capítulo 4 — Centro Multidisciplinario Meriadock Formación y Asesoría A.C.  · 2026

Taxonomía General de Aplicaciones

