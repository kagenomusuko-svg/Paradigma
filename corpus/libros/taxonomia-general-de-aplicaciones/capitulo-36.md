PARTE V · Organizaciones y Gestión

## Capítulo 36

### Gestión de proyectos — responsabilidad

### en retrasos y sobrecostos

Organ.  Estru.  Model.  Educa.  Crisi.

Para el mediador que busca precisión · Cómo usar este capítulo

Este capítulo es Nivel A: deriva y amplía los instrumentos del paradigma para el dominio de la gestión de proyectos y la responsabilidad en retrasos y sobrecostos. El dominio tiene una característica que lo distingue de todos los demás capítulos de la Parte V: el daño no se produce por un evento discreto sino por la acumulación de desviaciones desde el plan base a lo largo del ciclo de vida del proyecto. Cada decisión tomada en los nodos de decisión críticos del proyecto —la estimación inicial, la aprobación del alcance, la gestión de los cambios, la respuesta ante las alertas de riesgo— tiene R* sobre el retraso o el sobrecosto final.

Si tu caso es de retraso atribuible a estimación inicial deficiente (falacia de planificación), ve a §1 sub-variante 1 y §5 configuración 1. Si es de sobrecosto por cambios de alcance no gestionados (scope creep), ve a §5 configuración 2. Si es de incumplimiento del contratista con plan verificablemente alcanzable, ve a §3 y §5 configuración 3. Para la prioridad de evidencia, ve directamente a §9.

Nota de calibración: los rangos w de la escala Gp0–Gp8 y los rangos de α están derivados por extensión desde los principios del sistema, con referencia a los rangos del cap. 12 (ingeniería de sistemas) para el nodo de presión y la estructura de decisión crítica. Pendientes de calibración empírica con datos de arbitrajes de proyectos.

### §1  Descripción del subcampo

Taxonomía General de Aplicaciones

La responsabilidad en gestión de proyectos opera sobre un daño acumulativo con múltiples nodos causales simultáneos y temporalmente distribuidos que ningún otro capítulo de la Taxonomía captura con la misma complejidad temporal. El retraso y el sobrecosto de un proyecto grande no son el resultado de una decisión única: son la consecuencia de decenas de decisiones tomadas por actores distintos en momentos distintos del ciclo de vida, donde cada decisión aumentó o redujo la probabilidad de alcanzar el resultado contratado. La imputación del retraso al contratista —el actor más visible porque es quien no entregó— reproduce la misma inversión causal que el sistema documentó en Volkswagen y en Wells Fargo: el nodo más visible puede tener el menor R*_neta.

La distinción central del dominio es entre tres causas de retraso o sobrecosto con grafos causales distintos y distribuciones de R* distintas. La primera es la falacia de planificación: la estimación inicial era estructuralmente insuficiente porque ignoró riesgos conocidos, usó datos históricos de proyectos comparables que también tuvieron retrasos, o fue optimizada para ganar la licitación en lugar de reflejar el tiempo y costo reales. La segunda es el scope creep: el alcance del proyecto creció durante la ejecución por cambios no gestionados adecuadamente, sin la correspondiente extensión del plazo y el presupuesto. La tercera es el incumplimiento genuino del contratista: el plan era alcanzable con recursos razonables y el contratista no los movilizó con la calidad y la cantidad adecuadas.

El IPR (Índice de Perturbación del Proyecto) como instrumento central del dominio El IPR mide la brecha entre el rendimiento del proyecto y el plan base verificablemente alcanzable —no el plan base contractual, que puede haber sido fijado con falacia de planificación. IPR ∈ [0, 1]: IPR = 0 indica rendimiento en línea con el plan alcanzable; IPR = 1 indica perturbación máxima del plan alcanzable.

Taxonomía General de Aplicaciones

IPR = (retraso_o_sobrecosto_real − retraso_o_sobrecosto_del_plan_alcanzable) /

retraso_o_sobrecosto_del_plan_alcanzable El IPR tiene dos componentes: (a) la perturbación atribuible al plan base (falacia de planificación o scope creep no gestionado), y (b) la perturbación atribuible a la ejecución (incumplimiento del contratista respecto al plan alcanzable). La distribución del R* entre el dueño del proyecto, el director de proyecto y el contratista es proporcional a la fracción del IPR causalmente atribuible a cada uno.

AD_nodo = R*_nodo × D_proyecto × (1 − α_nodo) donde

D_proyecto = costo_del_retraso + sobrecosto_directo +

daño_indirecto

Sub-variantes del dominio

Sub-variante Descripción y singularidades del dominio

Retraso por falacia de planificación en la estimación inicial

El plan base del proyecto contenía estimaciones de plazo y costo estructuralmente insuficientes porque el dueño del proyecto o el director de proyecto ignoraron riesgos conocidos, usaron datos históricos de proyectos que también tuvieron retrasos significativos, o fijaron el plan base para ganar la licitación en lugar de reflejar el tiempo y costo alcanzables con los recursos disponibles. La falacia de planificación es el error de categoría más frecuente en proyectos grandes: el plan era optimista por diseño, no por incompetencia del contratista. El R* del dueño del proyecto y del director de proyecto sobre el retraso es alto cuando el plan base irrealista era una condición del contrato.

Sobrecosto por scope creep no gestionado

El alcance del proyecto creció durante la ejecución por cambios solicitados por el dueño del proyecto —modificaciones de diseño, adiciones de funcionalidad, cambios regulatorios que el dueño no anticipó— sin la correspondiente extensión formal del plazo y el presupuesto. El scope creep es la causa más frecuente de sobrecosto en proyectos de

Taxonomía General de Aplicaciones

Sub-variante Descripción y singularidades del dominio

tecnología de la información y en proyectos de construcción con especificaciones técnicas complejas. El R* del dueño del proyecto sobre el sobrecosto es positivo cuando los cambios de alcance fueron aprobados por él sin aprobación simultánea de los recursos adicionales.

Incumplimiento del contratista respecto al plan alcanzable

El plan base era verificablemente alcanzable con los recursos razonables del contratista — la estimación era realista, el alcance estaba definido y no cambió significativamente — y el contratista no movilizó los recursos en la calidad y la cantidad necesarias, no gestionó adecuadamente las interdependencias entre actividades, o tomó decisiones técnicas que produjeron retrabajo evitable. Es la sub-variante donde el R*_contratista es dominante. Se conecta con el cap. 12 (ingeniería de sistemas) para los proyectos donde el incumplimiento produjo fallos de seguridad.

Retraso por riesgo materializado sin gestión de riesgo adecuada

Un riesgo identificado o identificable del proyecto se materializó sin que el plan de proyecto incluyera un plan de respuesta adecuado: riesgos climáticos, riesgos regulatorios, riesgos de disponibilidad de materiales o de recursos especializados. El R* del director de proyecto sobre el retraso producido por el riesgo materializado es positivo cuando el plan de gestión de riesgo era inadecuado respecto a los riesgos que el estado del arte de la gestión de proyectos requería identificar y mitigar en el período.

Retraso por presión de plazo que ignoró las señales de riesgo

El dueño del proyecto o la dirección fijaron un plazo de entrega que los análisis internos mostraban como insuficiente, y presionaron para mantenerlo ignorando las alertas del director de proyecto o del contratista. Es el patrón del Challenger en el dominio de proyectos: la presión para cumplir el hito produjo que las señales de riesgo fueran ignoradas. El R* del dueño del proyecto sobre el retraso es alto cuando la presión de plazo fue la condición que determinó que las señales no produjeran corrección del plan.

Taxonomía General de Aplicaciones

Sub-variante Descripción y singularidades del dominio

Se conecta directamente con el cap. 12 (ingeniería de sistemas) para el nodo de presión.

Reclamación de retraso y sobrecosto entre partes del contrato

El análisis de responsabilidad se produce en el contexto de una disputa contractual entre las partes: el dueño reclama al contratista por incumplimiento, el contratista reclama al dueño por causas de retraso que le son atribuibles. El instrumento central es el análisis de impacto del cronograma (schedule impact analysis) que establece qué fracción del retraso total es causalmente atribuible a cada parte. El grafo del proyecto es el instrumento de arbitraje de la reclamación.

### §2  Escala de evidencia Gp0–Gp8 · Gestión de proyectos

La escala Gp0–Gp8 traduce la jerarquía general E0–E8 al vocabulario de la gestión de proyectos y el análisis de responsabilidad en retrasos y sobrecostos. Su característica más relevante es la posición del análisis del cronograma (Gp2) — el instrumento que establece el IPR y su descomposición entre las causas atribuibles a cada parte — y del análisis forense del plan base (Gp2) que establece si el plan era verificablemente alcanzable. Sin el plan base alcanzable como referencia, el IPR no tiene base y el análisis de responsabilidad no puede distribuir el R* entre las partes.

Descripción y ejemplos en el dominio de gestión

Rango

Nivel Tipo de evidencia

w

de proyectos

Gp1 Plan base verificablemente alcanzable con datos de proyectos comparables + análisis forense del

Plan de proyecto con estimaciones respaldadas por datos históricos de proyectos comparables terminados, con análisis de los factores de diferencia

[0.72, 0.90]

Taxonomía General de Aplicaciones

Descripción y ejemplos en el dominio de gestión

Rango

Nivel Tipo de evidencia

w

de proyectos

cronograma + registros de decisión en los nodos críticos

entre el proyecto analizado y los comparables; análisis forense del cronograma por experto en gestión de proyectos que establece la evolución del retraso desde el plan base hasta la terminación, identificando los eventos que lo produjeron y el momento en que cada actor tuvo la primera señal de que el plan estaba en riesgo; registros de las decisiones tomadas en los nodos de decisión críticos del proyecto — aprobación del plan base, decisiones de cambio de alcance, respuestas ante alertas de riesgo.

Gp2 Análisis del cronograma por experto en programación de obras + análisis de la distribución de causas de retraso + comparación con proyectos de referencia

Análisis pericial del cronograma que establece el IPR total y su descomposición entre las causas atribuibles a cada parte (método de análisis de impacto del cronograma: time impact analysis o windows analysis); comparación del plan base con el rendimiento de proyectos comparables que establece si la estimación inicial era alcanzable dado el estado del arte; análisis de la gestión de cambios de alcance que establece cuáles cambios fueron aprobados por el dueño sin ajuste correspondiente de plazo y presupuesto.

[0.60, 0.80]

Taxonomía General de Aplicaciones

Descripción y ejemplos en el dominio de gestión

Rango

Nivel Tipo de evidencia

w

de proyectos

Gp3 Registros del proyecto (actas, correos, informes de avance) + análisis del cronograma actualizado + registro de cambios de alcance

Registros completos del proyecto que muestran la evolución del cronograma durante la ejecución, las alertas de riesgo emitidas por el director de proyecto o el contratista, las decisiones de respuesta del dueño ante esas alertas, y el historial de cambios de alcance aprobados; análisis del cronograma con los datos de avance real que establece la magnitud del retraso en cada período y los eventos que lo explican.

[0.46, 0.64]

Gp4 Informes de avance del proyecto + actas de reuniones de seguimiento + contratos y adendas

Informes de avance periódicos que documentan el estado del cronograma y el presupuesto en cada período de reporte; actas de las reuniones de seguimiento que muestran las decisiones tomadas ante las alertas de riesgo; contratos y adendas que documentan los cambios de alcance aprobados y su tratamiento en cuanto al plazo y el presupuesto.

[0.36, 0.56]

Gp5 Comparación entre el plan base y el resultado sin análisis forense del cronograma

La diferencia entre el plazo y el costo del plan base y el plazo y el costo real al cierre del proyecto, sin análisis forense que establezca las causas del diferencial y su atribución a cada parte.

[0.26, 0.44]

Gp6 Inferencia desde el patrón de retrasos de la industria y el tipo de proyecto

El tipo de proyecto y el sector de la industria permiten inferir que el plan base era probable que

[0.14, 0.28]

Taxonomía General de Aplicaciones

Descripción y ejemplos en el dominio de gestión

Rango

Nivel Tipo de evidencia

w

de proyectos

subestimara el plazo real, sin análisis del proyecto específico.

Gp7 Correspondencia entre las partes sobre el retraso sin análisis del cronograma

Las comunicaciones entre las partes muestran el desacuerdo sobre las causas del retraso sin análisis técnico del cronograma que establezca la distribución causal.

[0.06, 0.20]

Gp8 Afirmación de una parte sobre las causas del retraso sin evidencia técnica del cronograma

La afirmación de una de las partes del contrato sobre las causas del retraso sin análisis pericial del cronograma ni registros del proyecto que la respalden.

[0.02, 0.12]

Gp0 Ausencia documentada de nexo causal entre la conducta del nodo analizado y el retraso o sobrecosto

Análisis Gp2 que establece que el retraso o sobrecosto es causalmente atribuible a factores exógenos a las partes del contrato — eventos de fuerza mayor documentados, cambios regulatorios imprevisibles — o que la parte analizada cumplió plenamente con sus obligaciones contractuales y el retraso fue producido exclusivamente por la otra parte.

w = 0.00

### §3  Firmas documentales por Hijo

### Los Hijos de Afrodita aplican en el dominio de la gestión de proyectos a los actores con voluntad propia: el dueño del proyecto que aprobó el plan base y tomó las decisiones de

Taxonomía General de Aplicaciones

cambio de alcance, el director de proyecto que diseñó el plan base y gestionó los riesgos, el contratista que ejecutó, y la dirección que fijó los plazos bajo presión. La distinción más relevante del dominio es entre el Fobos del director de proyecto que fijó un plan base optimista para ganar la licitación o complacer al dueño y el Deimos genuino del director que subestimó el plazo en buena fe porque los datos de proyectos comparables también eran optimistas.

§3.1  Hijos de legibilidad alta en el dominio de proyectos

Qué informa para S del

Error de discrimina

Firma documental

Fuente

Hijo

típica

ción

actor

Anter os

S muy bajo [0.03, 0.22]. El dueño del proyecto, el director de proyecto o el directivo que fijó el plazo sabía que el plan era insuficiente —los análisis internos lo mostraban — y deliberadam ente aprobó un plan optimista para ganar la licitación, satisfacer al cliente, o mantener la aprobación política del proyecto. El Anteros en proyectos es el patrón de los

Análisis internos que mostraban plazos y costos significativam ente superiores al plan base aprobado, sin que eso produjera ajuste del plan. Correos donde la dirección instruyó al director de proyecto a reducir la estimación para cumplir con el presupuesto o el plazo requerido. Comparacion es con proyectos similares que mostraban

Registros internos del proceso de elaboración del plan base. Correos de la dirección sobre los objetivos del plan. Comparaci ones históricas de proyectos del mismo tipo en la organizació n.

Confundir con Potós cuando el director de proyecto usó las estimacione s estándar del sector del período sin análisis específico de los riesgos del proyecto concreto. La pregunta: ¿el director tenía información específica de que su proyecto tenía característic as que lo hacían más difícil que el promedio histórico del sector?

Taxonomía General de Aplicaciones

Qué informa para S del

Error de discrimina

Firma documental

Fuente

Hijo

típica

ción

actor

megaproyect os públicos donde el plan base se construye para pasar el filtro político, no para reflejar el costo y el plazo reales. El isomorfismo con el Challenger: la presión política para cumplir un hito hace que las señales de riesgo sean ignoradas deliberadam ente.

que el plan base era estadísticame nte improbable, sin que eso produjera revisión.

Potós S moderado-alto [0.42, 0.72]. El director de proyecto o el dueño usaron los datos históricos de proyectos comparables del sector — que también tenían sesgos optimistas sistémicos— para construir el plan base, sin

Plan base construido con datos históricos de proyectos comparables sin análisis de los riesgos específicos del proyecto concreto que lo hacían más difícil. Ausencia de un registro de riesgos con probabilidade s e impactos estimados

Datos históricos del sector sobre plazos y costos de proyectos similares. El plan base del proyecto. La ausencia de un registro de riesgos validado.

Confundir con Anteros cuando el director tenía análisis paramétrico s o de riesgos específicos que indicaban la insuficiencia del plan y los ignoró. Con Deimos cuando genuinamen te no había datos de

Taxonomía General de Aplicaciones

Qué informa para S del

Error de discrimina

Firma documental

Fuente

Hijo

típica

ción

actor

ajustar por los riesgos específicos del proyecto concreto. El Potós en proyectos es el sesgo de planificación sistémico del sector: si todos los proyectos del tipo se retrasan en promedio un 30%, el director que usa el promedio histórico sin ajuste por los riesgos del proyecto específico reproduce el sesgo sin haber tomado una decisión idiosincrática de ser optimista.

antes del inicio de la ejecución. Uso de estimaciones análogas sin verificación paramétrica.

proyectos comparables para la estimación paramétrica.

Fobo s

S moderado [0.32, 0.60]. El director de proyecto adoptó un plan base que sabía era optimista, motivado por el miedo

Propuestas con plazos significativam ente inferiores a los de los competidores sin justificación técnica de la

Registros de la propuesta técnica. Comparaci ón con las propuestas de los competidor es. Historial

Confundir con Potós cuando el director usó metodología s de estimación estándar del sector que producen

Taxonomía General de Aplicaciones

Qué informa para S del

Error de discrimina

Firma documental

Fuente

Hijo

típica

ción

actor

a perder la licitación o a que el proyecto fuera cancelado si el plan realista superaba el presupuesto disponible del dueño. El Fobos en proyectos produce el plan base deshonesto-racional: el director sabe que el plazo es insuficiente, pero propone el que el dueño quiere escuchar porque de otro modo el proyecto no sería aprobado. Es la versión organizacion al de la trampa en la que el contratista entra cuando el mercado de licitaciones premia los

diferencia. Correos o comunicacio nes que muestran que el director era consciente de que el plazo era insuficiente antes de presentar la propuesta. Proyectos del mismo director o empresa donde el patrón se repite.

de proyectos del contratista.

sesgo optimista sistémico sin que el director fuera consciente del sesgo específico de su propuesta.

Taxonomía General de Aplicaciones

Qué informa para S del

Error de discrimina

Firma documental

Fuente

Hijo

típica

ción

actor

planes más optimistas.

Deim os

S alto [0.58, 0.86]. El director de proyecto no anticipó los riesgos que materializaro n el retraso porque genuinament e no disponía de los datos para identificarlos o porque los riesgos eran de un tipo que el estado del arte de la gestión de riesgos del período no requería anticipar. El Deimos genuino en proyectos: el riesgo que materializó el retraso no estaba en la literatura de riesgos del tipo de proyecto en el período, o las característica s del proyecto lo hacían

Registro de riesgos previo a la ejecución que no incluía el riesgo que materializó el retraso, con justificación de por qué ese riesgo no era identificable con el análisis disponible en el período. Proyectos comparables del sector que tampoco identificaron el mismo riesgo. Respuesta rápida y transparente ante la materializació n del riesgo.

El registro de riesgos pre-ejecución del proyecto. Proyectos comparable s del sector y su tratamiento del mismo riesgo.

Confundir con Potós cuando la falta de identificació n del riesgo fue consecuenci a de no haber realizado el análisis de riesgos que el estado del arte del período requería.

Taxonomía General de Aplicaciones

Qué informa para S del

Error de discrimina

Firma documental

Fuente

Hijo

típica

ción

actor

genéricamen te difícil de estimar con los datos disponibles.

§3.2  El nodo de presión de plazo: el patrón del Challenger en proyectos

El nodo de presión de plazo en proyectos es el equivalente funcional del nodo de presión política en el Challenger (cap. 12): el actor que fijó un hito de entrega inamovible bajo presión política, comercial o contractual, ignorando las alertas del director de proyecto y del contratista sobre la insuficiencia del plazo. La frase que define el patrón en proyectos es el equivalente de «ponte el sombrero de gestión»: la dirección que instruye al director de proyecto a mantener el plan, aunque los riesgos hagan su cumplimiento improbable.

El R* del nodo de presión de plazo sobre el retraso es positivo cuando: (a) las alertas del director de proyecto estaban documentadas y fueron ignoradas; y (b) el incumplimiento del hito habría producido la revisión del plan si las alertas hubieran sido atendidas. El S del nodo de presión es moderado-bajo cuando la presión fue idiosincrática de ese directivo específico — ningún otro directivo en esa posición habría mantenido el plazo ante las mismas alertas.

### §4  Escala de α con la tabla de acciones que cuentan

α_dueño · α_director_de_proyecto · α_contratista: tres nodos con lógica distinta α_dueño mide el grado en que el dueño del proyecto generó las condiciones para la ejecución exitosa: la definición completa del alcance antes del inicio, la

Taxonomía General de Aplicaciones

gestión de los cambios con el ajuste correspondiente de plazo y presupuesto, la respuesta oportuna ante las alertas del director y el contratista, y la provisión de los insumos del proyecto bajo responsabilidad del dueño (permisos, acceso al sitio, información técnica) en los plazos del plan. α_director_de_proyecto mide la calidad del plan base (realismo de las estimaciones, robustez del registro de riesgos, adecuación de los márgenes de contingencia), de la gestión del cronograma (seguimiento de la ruta crítica, gestión de las interdependencias, respuesta ante desviaciones), y de la comunicación de las alertas a las partes relevantes. α_contratista mide la movilización de recursos en la calidad y la cantidad del plan, la gestión de los subcontratistas y proveedores críticos, el rendimiento en las actividades de la ruta crítica, y la comunicación oportuna de las alertas de riesgo.

Nivel de α

α en el dominio

Conducta que

típico en desempeño

Nodo

de gestión de

sube α

proyectos

deficiente

Dueño del proyecto (ND)

Alcance definido completamente antes del inicio con especificaciones técnicas verificadas; proceso de gestión de cambios que evalúa el impacto en plazo y presupuesto antes de aprobar cada cambio; provisión en plazo de los insumos bajo responsabilidad del dueño; respuesta dentro del plazo contractual ante

Especificacion es técnicas completas y verificadas antes de la firma del contrato. Proceso documentado de gestión de cambios con análisis de impacto en plazo y presupuesto previo a la aprobación. Provisión de permisos, acceso y documentos técnicos dentro de los plazos

0.05–0.20 para dueños que aprobaron cambios de alcance sin ajuste de plazo y presupuesto de manera sistemática. 0.10–0.30 para dueños que no respondieron en plazo a los requerimiento s de información del contratista que estaban en la ruta crítica.

Taxonomía General de Aplicaciones

Nivel de α

α en el dominio

Conducta que

típico en desempeño

Nodo

de gestión de

sube α

proyectos

deficiente

los requerimientos de información del contratista; aceptación de la revisión del plan cuando las alertas del director o del contratista lo justificaban.

del plan. Revisión del plan base cuando las alertas del director de proyecto mostraban que el plan era inalcanzable.

Director de proyecto (DDP)

Plan base con estimaciones verificadas por datos de proyectos comparables y análisis de riesgos documentado; registro de riesgos actualizado durante la ejecución con respuesta ante la materialización de cada riesgo; seguimiento semanal de la ruta crítica con alerta documentada al dueño cuando el plan estaba en riesgo; gestión de las interdependencia s entre actividades con acciones preventivas ante los retrasos potenciales.

Plan base aprobado con análisis paramétrico documentado y registro de riesgos con probabilidades e impactos estimados. Seguimiento semanal de la ruta crítica con informes documentados de estado del cronograma. Alerta escrita al dueño cuando el cronograma tenía riesgo de incumplir el hito con plazo suficiente para la corrección. Gestión documentada de los cambios de alcance con impacto en el cronograma.

0.05–0.20 para directores con Anteros: plan base construido para complacer al dueño en lugar de reflejar el plazo alcanzable. 0.20–0.45 para directores con Potós: plan sin análisis de riesgos específico del proyecto. 0.45–0.65 para directores que no emitieron alertas oportunas ante las desviaciones del cronograma.

Taxonomía General de Aplicaciones

Nivel de α

α en el dominio

Conducta que

típico en desempeño

Nodo

de gestión de

sube α

proyectos

deficiente

Contratista (DC)

Movilización de recursos en la calidad y la cantidad del plan en las fechas comprometidas; rendimiento en las actividades de la ruta crítica dentro de los rendimientos del plan; gestión de subcontratistas y proveedores críticos con colchones adecuados para las interdependencia s; comunicación oportuna de las alertas de riesgo con propuestas de solución; retrabajo mínimo por errores de calidad.

Movilización documentada del personal y los equipos en las fechas del plan. Rendimiento en la ruta crítica verificable desde los registros diarios de producción. Informes de estado del cronograma al director de proyecto con indicadores de desviación. Comunicación inmediata de los eventos que afectan el cronograma con análisis de impacto y propuesta de recuperación.

0.05–0.20 para contratistas que no movilizaron los recursos comprometid os en las fechas del plan sin causa exógena documentada. 0.20–0.45 para contratistas que gestionaron los subcontratista s críticos con retrasos sistémicos sin acciones correctoras. 0.45–0.70 para contratistas que no comunicaron las alertas de riesgo en el plazo que habría permitido la corrección.

Subcontratist a crítico (DSC)

El subcontratista que ejecuta actividades de la ruta crítica tiene R* directo sobre el retraso cuando su incumplimiento fue condición necesaria del retraso del

Las mismas que para el contratista, aplicadas a las actividades del subcontratista específico.

Las mismas que para el contratista, con la distinción de que el contratista principal tiene R* adicional por la gestión

Taxonomía General de Aplicaciones

Nivel de α

α en el dominio

Conducta que

típico en desempeño

Nodo

de gestión de

sube α

proyectos

deficiente

proyecto. El análisis del R* del subcontratista sigue la misma lógica que el del contratista principal, con la distinción adicional de que el R* del contratista principal sobre el rendimiento del subcontratista es positivo cuando la selección, la dirección y el seguimiento del subcontratista fue inadecuada.

del subcontratista.

### La falacia de planificación: cuando el plan base era la causa del retraso

Nivel de realismo

Descripción del plan base y su relación con

del plan base

el IPR

Plan optimista por diseño (Fobos/Anteros del director)

El plan base fue construido para ganar la licitación o para satisfacer el presupuesto disponible del dueño, no para reflejar el plazo y costo reales. El IPR del contratista respecto a este plan es positivo pero el R* del IPR es mayoritariamente del director de proyecto y del dueño que aprobaron el plan. La desviación del contratista respecto al plan irreal no es evidencia de incumplimiento: es evidencia de que el plan era irreal.

Plan con sesgo optimista sistémico

El plan base fue construido con datos históricos del sector que tienen sesgo optimista sistémico documentado — si el promedio histórico del

Taxonomía General de Aplicaciones

Nivel de realismo

Descripción del plan base y su relación con

del plan base

el IPR

del sector (Potós del director)

tipo de proyecto tiene retrasos del 30%, el plan que usa el promedio sin ajuste tiene sesgo optimista sistémico. El R* del IPR es compartido entre el director (por no ajustar por los riesgos específicos del proyecto) y el sector (por producir datos históricos sesgados).

Plan realista con riesgos no identificados (Deimos del director)

El plan base era realista dado el análisis de riesgos disponible, pero un riesgo no identificable con el análisis del período se materializó. El IPR del contratista respecto al plan es positivo por la materialización del riesgo, pero el R* del director es bajo porque la falta de identificación del riesgo no fue negligente. El R* del riesgo materializado se desplaza a los factores exógenos.

Plan realista con riesgos identificados y gestionados (Harmonía del director)

El plan base era realista, el registro de riesgos identificaba los riesgos relevantes con planes de respuesta, y el director de proyecto ejecutó los planes de respuesta ante cada riesgo materializado. El IPR del contratista respecto al plan es positivo solo por el incumplimiento genuino del contratista — no por la falacia de planificación ni por los riesgos. α_director ≈ 1.00.

### §5  Tipos de nodo, tipos de arista y configuraciones canónicas del dominio

### Tipos de nodo en el grafo de gestión de proyectos

R* en el grafo de retraso o sobrecosto

Tipo de

Función en el

grafo S típico

nodo

Dueño del proyecto (ND)

Definió el alcance, aprobó el plan base,

Variable: S bajo [0.08–0.30] cuando las

R*_ND × D_proyecto × (1 − α_ND).

Taxonomía General de Aplicaciones

R* en el grafo de retraso o sobrecosto

Tipo de

Función en el

grafo S típico

nodo

gestionó los cambios y proveyó los insumos del proyecto bajo su responsabilidad. R* positivo sobre el retraso atribuible al scope creep no gestionado, a los insumos no provistos en plazo y a la presión de plazo que ignoró las alertas del director.

decisiones que produjeron el retraso fueron idiosincráticas del dueño específico. S moderado-alto [0.42–0.68] cuando el scope creep era el patrón de la organización en todos sus proyectos.

El R*_ND sobre el scope creep es proporcional a la fracción del retraso causalmente atribuible a los cambios de alcance no compensados con ajuste de plazo y presupuesto.

Director de proyecto (DDP)

Diseñó el plan base, gestionó el cronograma y los riesgos, y comunicó las alertas. R* positivo sobre el retraso atribuible a la falacia de planificación (plan base irrealista), a la gestión inadecuada de los riesgos identificables, y a la falta de alertas oportunas.

S alto [0.55–0.82] cuando la falacia de planificación era el patrón del sector (cualquier director habría construido el mismo plan). S bajo [0.05–0.30] cuando el plan fue construido deliberadamente optimista para ganar la licitación.

R*_DDP × D_proyecto × (1 − α_DDP). El R*_DDP sobre la falacia de planificación es proporcional a la fracción del IPR atribuible al plan base irreal — la diferencia entre el plan base contractual y el plan alcanzable.

Contratista (DC)

Ejecutó el proyecto movilizando los recursos comprometidos y

Variable: S alto [0.55–0.80] cuando el incumplimiento fue sistémico del

R*_DC × D_proyecto × (1 − α_DC). El R*_DC se calcula

Taxonomía General de Aplicaciones

R* en el grafo de retraso o sobrecosto

Tipo de

Función en el

grafo S típico

nodo

gestionando los subcontratistas. R* positivo sobre el retraso atribuible al incumplimiento del contratista respecto al plan alcanzable — no respecto al plan base irreal.

sector para ese tipo de proyecto (cualquier contratista en esas condiciones habría tenido el mismo incumplimiento). S bajo [0.08–0.35] cuando el incumplimiento fue idiosincrático del contratista específico.

respecto al plan alcanzable, no al plan base contractual. Si el plan base era irreal, R*_DC sobre el retraso respecto al plan base es bajo.

Nodo de presión de plazo (NPP)

El directivo que fijó el hito inamovible bajo presión política o comercial, ignorando las alertas del director de proyecto y del contratista. R* positivo sobre el retraso producido después del momento en que las alertas habrían permitido la corrección si hubieran sido atendidas.

S bajo-moderado [0.15–0.42] cuando la presión fue idiosincrática de ese directivo. S moderado-alto [0.45–0.68] cuando la presión de plazo era el patrón sistémico de la organización.

Fracción del D_proyecto atribuible al retraso que habría sido evitable si la presión de plazo hubiera permitido atender las alertas y revisar el plan.

Factores exógenos (NE)

Los eventos fuera del control de todas las partes: fuerza mayor, cambios regulatorios imprevisibles, condiciones del

N/A — no son actores con voluntad.

La fracción del D_proyecto no atribuible a ninguna parte reduce el D_atribuible que se

Taxonomía General de Aplicaciones

R* en el grafo de retraso o sobrecosto

Tipo de

Función en el

grafo S típico

nodo

sitio radicalmente distintas a las reveladas en los estudios de suelo. No tienen R* en sentido de responsabilidad, pero su materialización determina la fracción del IPR que no es atribuible a ninguna de las partes.

distribuye entre los nodos con R* positivo.

### Configuraciones canónicas del dominio

Configuración 1 — Retraso por falacia de planificación: el contratista que no causó el retraso del plan irreal

ND (dueño que fijó el presupuesto y el plazo que el proyecto políticamente tenía que cumplir, sin análisis de la factibilidad: Anteros si sabía que el plan era insuficiente; Potós si usó el promedio del sector sin análisis específico) + DDP (director de proyecto que construyó el plan base para cumplir el presupuesto y el plazo del dueño en lugar de reflejar el tiempo y costo reales: Fobos si fue para ganar la licitación; Potós si siguió las metodologías estándar del sector) + DC (contratista que ejecutó con los recursos del plan base y produjo el retraso respecto al plan irreal: Deimos porque no identificó que el plan era irreal antes de firmar el contrato) → Retraso del proyecto respecto al plan base irreal El instrumento central: el análisis comparativo del plan base con proyectos comparables terminados establece si el plan era verificablemente alcanzable. Si el promedio histórico del tipo de proyecto en el sector tenía retrasos del 30%, y el plan base no incluía un margen de contingencia para ese riesgo sistémico, el plan era optimista por diseño y el R* del retraso respecto al plan base es del DDP y del ND — no del DC.

Taxonomía General de Aplicaciones

Configuración 2 — Sobrecosto por scope creep: el dueño que aprobó cambios sin ajuste de recursos

ND (dueño que aprobó cambios de alcance durante la ejecución —cambios de diseño, adiciones de funcionalidad, cambios de especificaciones técnicas— sin el ajuste correspondiente de plazo y presupuesto: Potós si la gestión sin ajuste era el patrón de la organización; Anteros si el dueño conocía que los cambios requerían ajuste y deliberadamente no lo tramitó para evitar la revisión del presupuesto aprobado) + DC (contratista que ejecutó los cambios aprobados sin el presupuesto adicional, generando sobrecosto no gestionado) → Sobrecosto atribuible al scope creep del ND El análisis de responsabilidad distingue entre los cambios de alcance aprobados explícitamente por el dueño (R*_ND positivo sobre el sobrecosto derivado), los cambios de alcance implícitos en las especificaciones originales que el contratista debía haber anticipado (R*_DC positivo), y los cambios derivados de errores de diseño del proyecto que no eran obligación del contratista prever (R*_DDP positivo por el plan con errores de diseño).

Configuración 3 — Incumplimiento genuino del contratista con plan verificablemente alcanzable

DC (contratista con plan verificablemente alcanzable que no movilizó los recursos comprometidos: Anteros si la no movilización fue deliberada —el contratista asignó los recursos a un proyecto más rentable—; Potós si siguió las prácticas del sector que sistemáticamente subcontratan en exceso; Deimos si el rendimiento de los recursos fue genuinamente inferior al esperado por causas no previsibles) + DDP (director de proyecto con Harmonía: alertas oportunas, seguimiento de la ruta crítica, acciones correctoras propuestas) → Retraso atribuible al incumplimiento del DC respecto al plan alcanzable En esta configuración, la prueba del R*_DC es la comparación entre el rendimiento real de los recursos movilizados por el DC y el rendimiento del plan alcanzable. Si el DC movilizó 60% de los recursos comprometidos y el rendimiento de esos recursos era el planificado, el retraso es atribuible a la movilización insuficiente, no al rendimiento de los recursos. El análisis del cronograma en ventanas (windows analysis) establece cuánto del retraso

Taxonomía General de Aplicaciones

ocurrió en cada período y quién tenía R* sobre las actividades retrasadas en ese período.

### §6  Preguntas que responde este capítulo

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

¿El plan base era verificablemente alcanzable — la falacia de planificación contribuyó al retraso?

Análisis comparativo del plan base con datos históricos de proyectos comparables terminados del sector: ¿el plazo y el costo del plan base estaban dentro del rango histórico de proyectos de complejidad equivalente? ¿El registro de riesgos del plan base incluía los riesgos que el sector documenta sistemáticamente para ese tipo de proyecto? La diferencia entre el plan base contractual y el plan alcanzable estimado es la fracción del IPR atribuible a la falacia de planificación.

Declaración A si hay datos de proyectos comparables terminados con análisis estadístico del plazo y costo real vs. plan base (Gp1). Declaración B con análisis pericial del plan base comparado con los datos del sector (Gp2). Declaración C cuando el plan alcanzable debe estimarse desde los datos disponibles sin un análisis estadístico robusto de proyectos comparables.

¿El retraso fue causado por scope creep no gestionado — cuál es el R* del dueño?

Análisis del historial de cambios de alcance: ¿cuántos cambios fueron aprobados por el dueño? ¿Cuáles tuvieron ajuste correspondiente de plazo y presupuesto? ¿Cuál es el impacto acumulado en el cronograma de los cambios sin ajuste? La fracción del retraso atribuible al scope creep sin ajuste es el R*_ND

Declaración A si hay un registro de cambios de alcance documentado con la aprobación del dueño y el análisis de impacto para cada cambio (Gp1). Declaración B con análisis del contrato y las adendas que muestran los cambios aprobados sin ajuste

Taxonomía General de Aplicaciones

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

sobre ese componente del retraso.

de plazo y presupuesto (Gp2). Declaración C cuando el scope creep debe inferirse desde las diferencias entre el alcance inicial y el alcance ejecutado sin un registro de cambios.

¿El contratista incumplió respecto al plan alcanzable — cuál es el IPR_DC?

Análisis del cronograma en ventanas que establece la distribución de causas del retraso período por período: ¿en qué períodos el retraso fue causado por actividades bajo control del DC? ¿El rendimiento de los recursos movilizados por el DC fue inferior al del plan alcanzable? El IPR_DC es la fracción del IPR total causalmente atribuible al incumplimiento del DC respecto al plan alcanzable.

Declaración A con análisis del cronograma en ventanas (windows analysis) y registros diarios de producción del DC (Gp1). Declaración B con análisis pericial del cronograma y registros de avance del proyecto (Gp2). Declaración C cuando el IPR_DC debe estimarse desde los informes de avance sin acceso a los registros diarios de producción.

¿Hay un nodo de presión de plazo — la presión produjo que las alertas fueran ignoradas?

Análisis de las comunicaciones entre el nodo de presión y el director de proyecto o el contratista: ¿hay alertas documentadas de riesgo al cronograma que el nodo de presión ignoró? ¿El nodo de presión instruyó al director a mantener el plan a pesar de las alertas? ¿El retraso habría sido evitable si las alertas hubieran

Declaración A si hay correos o actas de reuniones donde el nodo de presión ignoró explícitamente las alertas documentadas (Gp1). Declaración B con análisis del historial de comunicaciones entre el nodo de presión y el director de proyecto (Gp2). Declaración C cuando la presión de

Taxonomía General de Aplicaciones

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

producido la revisión del plan?

plazo debe inferirse desde la ausencia de revisión del plan ante alertas documentadas.

¿Cuál es el D_proyecto total y cómo se distribuye el AD entre los nodos?

D_proyecto = costo_del_retraso + sobrecosto_directo + daño_indirecto. El costo del retraso incluye los costos financieros del capital invertido durante el período adicional, los ingresos perdidos durante el período de retraso y los costos contractuales de penalización por retraso. El AD_nodo = R*_nodo × D_proyecto × (1 − α_nodo) para cada nodo del grafo.

Declaración B con análisis del D_proyecto desde los registros contables del proyecto y el análisis del cronograma (Gp2). Declaración A con acceso a los registros financieros completos del proyecto más el análisis del cronograma en ventanas (Gp1).

### §7  Traducción de D_total al dominio de gestión de proyectos

D_proyecto = D_retraso + D_sobrecosto + D_indirecto El daño en gestión de proyectos tiene tres componentes que deben calcularse separadamente porque tienen nodos causales distintos y contrafácticos distintos. El D_retraso es el daño producido por el tiempo adicional de ejecución: los costos financieros del capital invertido durante el período adicional, los ingresos perdidos durante el período de retraso, y los costos de las penalizaciones contractuales. El D_sobrecosto es el daño producido por el costo superior al presupuesto del plan alcanzable — no del plan base irreal. El D_indirecto es el daño a terceros producido por el retraso del proyecto: el perjuicio a los beneficiarios del proyecto que no pudieron usar la infraestructura durante el período de retraso.

Taxonomía General de Aplicaciones

En el dominio

Fuente

de gestión

Compo

de evidenci

Cómo se cuantifica

nente

de proyecto

a

s

D_retra so (costo del tiempo adiciona l de ejecució n)

El daño producid o por la extensión del plazo de ejecución más allá del plan alcanzabl e: los costos directos de mantener los recursos del proyecto durante el período adicional (personal , equipos, instalacio nes de obra), los costos financier os del capital inmoviliz ado durante el período adicional, y las

D_retraso = (días_de_retraso_respecto_al_pla n_alcanzable) × (costo_diario_de_los_recursos_d el_proyecto) + (ingresos_perdidos_por_día × días_de_retraso) + penalizaciones_contractuales. El costo diario de los recursos del proyecto se establece desde el presupuesto del plan base ajustado por los recursos realmente movilizados.

Registro s contable s del proyecto (costos reales por período). Presupu esto del plan base. Contrato y adendas con las cláusulas de penalizac ión. Análisis financier o del capital inmovili zado.

Taxonomía General de Aplicaciones

En el dominio

Fuente

de gestión

Compo

de evidenci

Cómo se cuantifica

nente

de proyecto

a

s

penalizac iones contractu ales por incumpli miento del plazo. El contrafác tico es el plazo del plan alcanzabl e, no el plan base contractu al cuando éste era irreal.

D_sobr ecosto (exceso de costo sobre el presupu esto del plan alcanzab le)

El daño producid o por el costo total del proyecto superior al costo del plan alcanzabl e. El contrafác tico es el costo del plan alcanzabl e — si el plan base era irreal, la diferenci

D_sobrecosto = costo_real_total − costo_del_plan_alcanzable. El costo del plan alcanzable se establece desde el análisis comparativo con proyectos similares terminados. La fracción atribuible al scope creep = Σ(costo_de_cada_cambio_sin_aj uste_de_presupuesto).

Registro s contable s del proyecto . Análisis compara tivo de costos de proyecto s similares. Historial de cambios de alcance con su costo.

Taxonomía General de Aplicaciones

En el dominio

Fuente

de gestión

Compo

de evidenci

Cómo se cuantifica

nente

de proyecto

a

s

a entre el costo real y el plan base irreal no es sobrecost o atribuible al contratist a. La fracción del sobrecost o atribuible al scope creep se calcula separada mente del sobrecost o atribuible al incumpli miento del contratist a.

D_indir ecto (daño a terceros por el retraso del proyect o)

El daño a los beneficia rios del proyecto que no pudieron usar la infraestru

D_indirecto = Σ (daño_por_período × períodos_de_retraso) para cada categoría de afectados. Para infraestructura pública: el valor de la infraestructura no disponible estimado desde el tráfico o el uso esperado × el costo unitario del perjuicio por usuario × el número

Datos de uso esperado de la infraestr uctura. Estudios de impacto

Taxonomía General de Aplicaciones

En el dominio

Fuente

de gestión

Compo

de evidenci

Cómo se cuantifica

nente

de proyecto

a

s

ctura o el sistema durante el período de retraso: el daño económi co a los usuarios de la infraestru ctura no disponibl e, el daño a la calidad de vida por la indisponi bilidad del servicio, el daño a otras actividad es que dependía n de la terminaci ón del proyecto en plazo. Relevant e especialm ente en proyectos de infraestru

de usuarios afectados × los días de retraso.

económi co del proyecto . Datos de costos por retraso de proyecto s compara bles. Encuesta s a los usuarios afectado s.

Taxonomía General de Aplicaciones

En el dominio

Fuente

de gestión

Compo

de evidenci

Cómo se cuantifica

nente

de proyecto

a

s

ctura pública.

### §8  Límites del método y errores frecuentes de aplicación

### Límites del método en el dominio de gestión de proyectos

Límite 1 — El plan alcanzable tiene incertidumbre inherente. El análisis del plan alcanzable requiere establecer qué plazo y costo habría tenido el proyecto con la gestión adecuada y los recursos razonables — un contrafáctico con incertidumbre inherente que aumenta con la complejidad y la singularidad del proyecto. Para proyectos sin comparables cercanos, la incertidumbre del plan alcanzable puede hacer difícil establecer si el retraso respecto al plan base era atribuible a la falacia de planificación o al incumplimiento del contratista.

Límite 2 — El análisis del cronograma en ventanas requiere registros completos del proyecto. El análisis que distribuye el retraso entre las causas atribuibles a cada parte período por período requiere el cronograma actualizado en cada período de reporte, los registros diarios de producción, y las comunicaciones entre las partes que documentan quién tenía responsabilidad sobre las actividades retrasadas en cada período. Sin esos registros, el análisis de la distribución de causas tiene alta incertidumbre.

Límite 3 — La concurrencia de causas. En la mayoría de los proyectos con retrasos significativos, las causas atribuibles a cada parte son concurrentes — ocurren simultáneamente y su

Taxonomía General de Aplicaciones

efecto no es aditivo sino sinérgico. El retraso total no es la suma del retraso atribuible al dueño más el retraso atribuible al contratista: es el resultado de la interacción entre ambos, donde el retraso de una parte frecuentemente produce el retraso en cascada de la otra. El análisis de la concurrencia de causas requiere metodologías específicas de análisis del cronograma (modified but-for, fragnets) que el análisis convencional no captura.

### Errores frecuentes de aplicación

Error Por qué ocurre Consecuencia Corrección

Calcular el IPR_DC respecto al plan base irreal en lugar del plan alcanzable

El plan base contractual es el documento de referencia más obvio. El análisis compara el resultado real con el plan base sin verificar si el plan base era alcanzable.

R*_DC sobreestimado cuando el plan base era irreal. El contratista aparece como incumplidor respecto a un plan que nunca fue alcanzable. R*_ND y R*_DDP subestimados.

El análisis debe establecer el plan alcanzable antes de calcular el IPR_DC. Si el plan base era irreal, el IPR_DC se calcula respecto al plan alcanzable, no al plan base contractual.

Ignorar el scope creep como causa del sobrecosto y atribuirlo al contratista

El sobrecosto es visible en los registros contables del contratista. La causa del sobrecosto (scope creep aprobado por el dueño sin ajuste de presupuesto) requiere el análisis del historial de cambios.

R*_ND subestimado sobre el sobrecosto atribuible al scope creep. La pretensión del dueño contra el contratista incluye el sobrecosto que el dueño mismo causó con los cambios no compensados.

El análisis del sobrecosto debe comenzar por el historial de cambios de alcance: ¿cuáles fueron aprobados por el dueño sin ajuste de presupuesto? La fracción del sobrecosto atribuible a

Taxonomía General de Aplicaciones

Error Por qué ocurre Consecuencia Corrección

esos cambios es R*_ND, no R*_DC.

No analizar el nodo de presión de plazo como nodo causal del retraso

El nodo de presión de plazo es parte de la organización del dueño y se confunde con el dueño del proyecto como actor único. El análisis no distingue entre las decisiones del dueño como contratante y las decisiones del directivo que presionó para mantener el plazo.

R*_nodo_presión no captado. El retraso producido por ignorar las alertas de riesgo bajo presión de plazo queda sin nodo causal identificado.

El grafo del proyecto debe incluir el nodo de presión de plazo como nodo independiente cuando hay evidencia de que las alertas del director de proyecto fueron ignoradas por un directivo específico bajo presión política o comercial.

Atribuir al contratista el retraso producido por factores exógenos sin análisis de causalidad

El contratista es responsable del resultado del proyecto y el retraso es su incumplimiento contractual. El análisis no diferencia entre el retraso por causas exógenas (que reducen el D_atribuible a las partes) y el retraso por causas endógenas.

D_proyecto sobreestimado y R*_DC sobreestimado por la inclusión del retraso exógeno en el análisis de responsabilidad.

El análisis de la distribución de causas del retraso debe comenzar por identificar la fracción del retraso atribuible a factores exógenos — fuerza mayor, cambios regulatorios imprevisibles, condiciones del sitio radicalmente distintas — que no es atribuible a ninguna parte.

Taxonomía General de Aplicaciones

### §9  Guía de prioridades de recolección de evidencia

La primera decisión es establecer si el plan base era verificablemente alcanzable. Sin ese análisis previo, el análisis de la distribución del R* entre el dueño, el director y el contratista carece de base: el IPR_DC calculado respecto al plan base irreal sobreestima el R* del contratista.

### Tabla de prioridades de recolección de evidencia en gestión de proyectos

Si tu incertidu

La evidencia que más la

Qué buscar /

Qué rango reduce

Por qué funciona

mbre principal

qué preguntar

reduce

es...

es...

### 1. ¿El plan base era verificable mente alcanzable?

Datos históricos de proyectos comparable s terminados del sector + análisis paramétric o del plan base. Si el plan base era estadística mente improbable dado el historial del sector, hay falacia de planificació n.

El plan alcanzable es la referencia correcta para calcular el IPR_DC. Sin él, el análisis de responsabili dad atribuye al contratista el retraso causado por el plan irreal.

Establece la referencia del IPR (incertidu mbre estructural central).

¿Cuál es el plazo y costo promedio de proyectos comparabl es terminados en el sector? ¿El plan base incluía márgenes de contingenc ia para los riesgos sistémicos del tipo de proyecto? ¿Hay análisis paramétric

Taxonomía General de Aplicaciones

Si tu incertidu

La evidencia que más la

Qué buscar /

Qué rango reduce

Por qué funciona

mbre principal

qué preguntar

reduce

es...

es...

o del plan base documenta do?

### 2. ¿El retraso fue por scope creep no gestionado?

Historial de cambios de alcance con la aprobación del dueño y el análisis de impacto para cada cambio. La suma de los cambios sin ajuste de plazo y presupuest o es el scope creep no gestionado.

El scope creep es la causa de R*_ND más frecuente y más frecuentem ente ignorada en los análisis de responsabili dad de proyectos.

Establece el R*_ND sobre el sobrecost o por scope creep (incertidu mbre del nodo dueño).

¿Hay un registro de cambios de alcance? ¿Cuáles cambios tuvieron ajuste formal de plazo y presupuest o? ¿Cuál es el costo acumulado de los cambios sin ajuste?

### 3. ¿El IPR_DC es calculable respecto al plan alcanzable?

Análisis del cronogram a en ventanas (Gp2) con los registros de avance del proyecto: ¿en qué períodos el retraso fue causado por actividades bajo control del DC? ¿El

El IPR_DC establece el R*_DC sobre el incumplimi ento genuino. Sin el análisis de ventanas, el IPR_DC puede incluir el retraso causado por el ND y el DDP.

Establece el R*_DC (incertidu mbre del nodo contratista ).

¿Qué porcentaje de los recursos comprome tidos movilizó el DC en las fechas del plan? ¿El rendimient o de los recursos movilizado s era el planificado en las actividades

Taxonomía General de Aplicaciones

Si tu incertidu

La evidencia que más la

Qué buscar /

Qué rango reduce

Por qué funciona

mbre principal

qué preguntar

reduce

es...

es...

rendimient o de los recursos movilizado s era el planificado ?

de la ruta crítica? ¿El DC comunicó alertas oportunas al DDP?

### 4. ¿Hay un nodo de presión de plazo — las alertas fueron ignoradas bajo presión?

Comunicac iones entre el DDP y el directivo que presionó para mantener el plazo: ¿hay alertas documenta das de riesgo al cronogram a? ¿La respuesta del directivo fue mantener el plazo en lugar de revisar el plan?

El nodo de presión de plazo puede ser el nodo de mayor R* cuando las alertas del DDP eran suficientes para la corrección y fueron ignoradas deliberada mente.

Establece el R* del nodo de presión (incertidu mbre del nodo de presión).

¿Hay correos o actas donde el DDP alertó sobre el riesgo al cronogram a? ¿La respuesta del directivo fue mantener el plazo o revisar el plan? ¿Hay antecedent es de que ese directivo ignoró alertas similares en otros proyectos?

### 5. ¿Cuál es el D_proyect o total?

D_retraso (costos directos del período adicional + ingresos perdidos +

Sin el D_proyecto , el AD de cada nodo no tiene base

Establece la escala del D_proyec to (incertidu mbre

¿Cuál es el costo diario de los recursos del proyecto

Taxonomía General de Aplicaciones

Si tu incertidu

La evidencia que más la

Qué buscar /

Qué rango reduce

Por qué funciona

mbre principal

qué preguntar

reduce

es...

es...

penalizacio nes) + D_sobreco sto (exceso sobre el plan alcanzable) + D_indirect o (daño a los beneficiario s del proyecto durante el retraso).

cuantificada .

empírica del daño).

durante el período de retraso? ¿Cuáles son los ingresos perdidos por día de retraso? ¿Hay penalizacio nes contractual es por retraso? ¿Cuál es el daño a los beneficiari os del proyecto durante el período de retraso?

### 6. ¿El Hijo dominante del director de proyecto es Anteros, Fobos o Potós — qué tipo de falacia hay?

Análisis del proceso de elaboración del plan base: ¿hay análisis internos que mostraban plazos superiores al plan base aprobado? ¿El director tenía datos de proyectos comparable s que

El Hijo del DDP determina el S de la falacia de planificació n y la fracción del R*_DDP que es idiosincrátic a.

Establece el S del DDP (incertidu mbre ontológica del nodo director).

¿Hay análisis internos del proceso de elaboració n del plan base? ¿El director presentó estimacion es distintas al plan base aprobado? ¿Hay proyectos anteriores del mismo director

Taxonomía General de Aplicaciones

Si tu incertidu

La evidencia que más la

Qué buscar /

Qué rango reduce

Por qué funciona

mbre principal

qué preguntar

reduce

es...

es...

indicaban la insuficienci a del plan?

con el mismo patrón de retraso?

### Árbol de decisión en gestión de proyectos: tres pasos

¿El plan base era verificablemente alcanzable — cuál es la referencia para el IPR? │

├─ Plan base IRREAL (falacia de planificación documentada) → IPR_DC respecto al plan alcanzable

│  └─  PRIORIDAD 1: ¿La falacia fue Anteros (deliberada) o Potós (sistémica del sector)?

│         · Anteros → S_DDP bajo [0.05–0.22]. R*_DDP pleno sobre el plan irreal. │         · Potós → S_DDP moderado-alto [0.42– 0.70]. R* compartido con el sector. │  └─  PRIORIDAD 2: ¿El ND aprobó el plan sabiendo que era irreal?

│         · Sí → R*_ND sobre la fracción del retraso atribuible al plan irreal que aprobó. │  └─  PRIORIDAD 3: ¿Hay scope creep no gestionado — R*_ND adicional?

│         · Cambios sin ajuste de plazo y presupuesto → R*_ND sobre el sobrecosto del scope creep.

└─ Plan base ALCANZABLE → IPR_DC respecto al plan base

└─  PRIORIDAD 1: ¿El DC incumplió respecto al plan alcanzable?

· Análisis de ventanas del cronograma establece el IPR_DC.

Taxonomía General de Aplicaciones

└─  PRIORIDAD 2: ¿Hay nodo de presión de plazo que ignoró alertas?

· Alertas documentadas ignoradas → R*_NPP sobre el retraso posterior a la alerta.

├─ Paso 2: ¿Cuál es la distribución del R* entre ND, DDP, DC y NPP? │

├─ R*_ND dominante → scope creep + plan irreal aprobado → pretensión principal contra el dueño

│  └─  AD_ND = R*_ND × D_proyecto × (1 − α_ND). ├─ R*_DDP dominante → falacia de planificación idiosincrática → plan irreal por diseño del director

│  └─  AD_DDP = R*_DDP × D_proyecto × (1 − α_DDP). └─ R*_DC dominante → incumplimiento genuino respecto al plan alcanzable

└─  AD_DC = R*_DC × D_proyecto × (1 − α_DC).

└─ Paso 3: ¿El D_proyecto incluye el D_indirecto a terceros?

├─ SÍ (proyecto de infraestructura pública con beneficiarios identificados)

│  └─  D_indirecto = daño_por_período × períodos_de_retraso × N_beneficiarios_afectados. └─ NO (proyecto privado sin afectados externos) → D_proyecto = D_retraso + D_sobrecosto

└─  AD_nodo = R*_nodo × (D_retraso + D_sobrecosto) × (1 − α_nodo).

— Fin del Capítulo 36 —

Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

