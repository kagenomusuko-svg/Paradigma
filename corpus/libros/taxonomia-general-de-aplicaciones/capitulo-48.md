PARTE VII · Ingeniería y Tecnología

## Capítulo 48

### Ciberseguridad — responsabilidad en

### brechas y ataques

Organ.  Estru.  Model.  Educa.  Crisi.

Para el mediador que busca precisión · Cómo usar este capítulo

Este capítulo es Compilación directa: aplica el cap. 12 de El cálculo de la responsabilidad (Ingeniería de sistemas y confiabilidad) al dominio de la ciberseguridad, con adaptaciones para las características específicas de los sistemas digitales. El instrumento central es el INCF (Índice de Necesidad Causal del Fallo) aplicado a brechas de datos y ataques cibernéticos: no pregunta «¿cuál fue el vector del ataque?» sino «¿sin qué decisión u omisión del arquitecto de seguridad el ataque no habría producido daño a esa escala?»

La distinción central del dominio: la S del atacante externo es frecuentemente alta — otro atacante con acceso a las mismas herramientas habría explotado la misma vulnerabilidad. El R* del atacante sobre el D_total es real pero moderado cuando la vulnerabilidad era conocida y el parche existía: el nodo de mayor R* es el arquitecto de la defensa que no implementó el parche disponible o que diseñó el sistema sin los controles que el estándar del sector requería. Si tu caso es de brecha por vulnerabilidad no parcheada, ve a §3 y §5 caso A. Si es de ataque de phishing o ingeniería social, ve a §5 caso B. Para responsabilidad del proveedor de software, ve a §4.

### §1  Descripción del subcampo

Taxonomía General de Aplicaciones

La ciberseguridad es el dominio de la ingeniería donde la distinción entre el fallo técnico y la decisión humana que lo habilitó es más difícil y más frecuentemente confundida. La narrativa espontánea de una brecha de datos concentra el R* en el atacante externo — el hacker, el grupo de ransomware, el Estado adversario. El análisis causal establece sistemáticamente que el atacante tiene S alta: otro atacante con acceso a las mismas herramientas habría explotado la misma vulnerabilidad, porque la vulnerabilidad existía independientemente del atacante específico. El nodo de mayor R* en la mayoría de las brechas significativas es el arquitecto de la seguridad del sistema atacado — el que diseñó el sistema sin los controles del estándar, el que no aplicó el parche disponible, el que otorgó privilegios de acceso excesivos que amplificaron el alcance de la brecha.

INCF_cyber: la reformulación de la pregunta central

INCF_cyber(nodo_i) = P (daño_a_esa_escala | sin la decisión/omisión

del nodo_i) → diferencial respecto a P (daño | con el nodo_i) El INCF_cyber traslada la pregunta del FTA convencional (¿cuál fue el vector técnico del ataque?) a la pregunta de responsabilidad (¿sin qué decisión humana el ataque no habría producido daño a esa escala?). La respuesta establece el nodo de mayor INCF_cyber — que frecuentemente no es el atacante sino el arquitecto de la defensa con S moderado-bajo: ese sistema específico de seguridad era idiosincrático en sus deficiencias, y el parche disponible habría prevenido la brecha.

Sub-variantes del dominio de ciberseguridad

Sub-variante Descripción

Brecha por vulnerabilidad no parcheada

El sistema fue comprometido a través de una vulnerabilidad conocida para la que existía un parche oficial no aplicado. El R* del atacante es real pero moderado — cualquier atacante con acceso a las herramientas disponibles habría explotado la misma vulnerabilidad. El INCF del responsable de la

Taxonomía General de Aplicaciones

Sub-variante Descripción

gestión de parches es alto: la no aplicación del parche fue condición necesaria de que la brecha produjera daño a esa escala.

Ataque de ingeniería social (phishing, spear-phishing)

El atacante engañó a un empleado para obtener credenciales o acceso. La distinción del dominio: el S del empleado que fue engañado es típicamente alto (cualquier empleado en esa posición, sin la formación y los controles adecuados, habría respondido igual); el INCF del responsable del programa de formación y los controles técnicos de detección es alto.

Ataque de cadena de suministro (supply chain attack)

El atacante comprometió el software de un proveedor para llegar a los sistemas de sus clientes. El caso SolarWinds: el atacante insertó código malicioso en las actualizaciones del software de monitoreo. La distribución del R* requiere el análisis de la cadena: el proveedor comprometido (con INCF positivo sobre la falta de controles de integridad del código), y el cliente que instaló el software comprometido sin verificación adicional.

Ransomware: cifrado de sistemas y extorsión

El atacante cifró los sistemas y exige rescate. La distribución del R* entre el atacante (con S moderada — el ransomware explota vulnerabilidades genéricas pero requiere capacidad operacional no trivial), el arquitecto de la seguridad (INCF positivo si los sistemas no tenían backups adecuados ni segmentación que hubiera limitado el alcance), y el CISO que autorizó el pago del rescate.

Brecha de datos por acceso interno excesivo

Un insider (empleado o contratista) accedió a datos a los que no debería haber tenido acceso dado su rol, causando daño. La distinción del dominio: el diseñador del sistema de control de acceso tiene INCF positivo cuando los privilegios otorgados eran excesivos respecto al rol — el principio de menor privilegio no fue implementado.

Responsabilidad del proveedor de software con vulnerabilidades conocidas

El proveedor de software vendió o distribuyó un producto con vulnerabilidades conocidas que el proveedor tenía documentadas, pero no había comunicado ni parcheado antes de la distribución. El INCF del proveedor es alto cuando la vulnerabilidad

Taxonomía General de Aplicaciones

Sub-variante Descripción

era conocida y el parche disponible no fue distribuido en tiempo razonable.

### §2  Escala de evidencia Cd0–Cd8 · Código digital / documentación técnica

La escala Cd0–Cd8 es la escala de evidencia de la Parte VII. Se aplica al dominio de ciberseguridad con énfasis en la cadena de custodia forense digital — la verificación de que los artefactos digitales (logs, imágenes de disco, capturas de red) no han sido alterados desde su recolección — y en la capacidad de los análisis para establecer la cadena causal entre la vulnerabilidad explotada, el actor que no la mitigó, y el daño producido.

Tipo de evidencia en ciberseguridad

Descripción y ejemplos Rango

Nivel

w

Cd1 Análisis forense digital con cadena de custodia verificada + logs de sistema con integridad criptográfica

El análisis forense de los sistemas comprometidos con metodología documentada, cadena de custodia de los artefactos digitales, y verificación criptográfica de la integridad de los logs. Incluye la reconstitución de la timeline del ataque desde los logs verificados, la identificación del vector de entrada y la trayectoria del atacante dentro del sistema.

[0.72, 0.90]

Cd2 Análisis forense de segunda parte (empresa de respuesta a incidentes) con acceso completo a los sistemas +

El informe de análisis forense de una empresa de respuesta a incidentes acreditada que tuvo acceso completo a los sistemas comprometidos, con metodología documentada y acceso a los artefactos primarios. Incluye el análisis del

[0.62, 0.80]

Taxonomía General de Aplicaciones

Tipo de evidencia en ciberseguridad

Descripción y ejemplos Rango

Nivel

w

análisis del código malicioso

código malicioso (malware reverse engineering) que establece el origen, los vectores y las capacidades del atacante.

Cd3 Análisis convergente de múltiples fuentes técnicas independientes sobre el mismo incidente

Cuando dos o más análisis técnicos independientes de entidades acreditadas convergen en la descripción de la misma cadena causal del incidente, incluyendo el vector de ataque, los sistemas comprometidos, y el alcance del daño.

[0.52, 0.70]

Cd4 Informe del proveedor de ciberseguridad o del CERT con metodología parcialmente documentada

Los informes de los centros de respuesta a emergencias (CERT, CSIRT) o de proveedores de ciberseguridad sobre el incidente, con metodología parcialmente documentada y acceso parcial a los sistemas comprometidos.

[0.40, 0.58]

Cd5 Análisis de logs sin cadena de custodia forense verificada + declaraciones del equipo de TI interno

Los logs del sistema o de la red analizados sin cadena de custodia forense verificada, y las declaraciones del equipo de TI interno que gestionó el incidente.

[0.26, 0.44]

Cd6 Investigación periodística con fuentes técnicas anónimas dentro de la organización afectada

Los reportes de medios especializados en ciberseguridad basados en fuentes técnicas anónimas del equipo interno de la organización afectada.

[0.14, 0.28]

Cd7 Declaraciones públicas de la organización afectada sin corroboración

Los comunicados oficiales de la organización afectada sobre la brecha, sin corroboración técnica de análisis forense independiente.

[0.04, 0.16]

Taxonomía General de Aplicaciones

Tipo de evidencia en ciberseguridad

Descripción y ejemplos Rango

Nivel

w

técnica independiente

Cd8 Inferencia del incidente desde el impacto observable sin análisis técnico del vector

La inferencia del tipo y escala del incidente exclusivamente desde el impacto observable (datos publicados, sistemas inaccesibles, notificaciones a afectados) sin ningún análisis técnico del vector de ataque.

[0.02, 0.10]

Cd0 Análisis forense Cd1 que establece que la brecha no fue causada por la vulnerabilidad o la conducta del actor imputado

El análisis forense Cd1 que establece positivamente que el vector de ataque no corresponde a la vulnerabilidad atribuida al actor o que la cadena causal propuesta es técnicamente imposible dado la arquitectura del sistema.

w = 0.00

### §3  Las herramientas del análisis de responsabilidad en ciberseguridad

El análisis de responsabilidad en ciberseguridad opera en tres capas simultáneas que deben construirse separadamente antes de integrarse. La capa técnica establece el vector de ataque (qué vulnerabilidad fue explotada, con qué herramientas, por qué ruta) y el alcance del daño (qué datos fueron accedidos, exfiltrados o cifrados). La capa de decisión establece quién tomó qué decisiones que hicieron posible el ataque a esa escala (qué arquitectura de seguridad fue diseñada, qué controles no fueron implementados, qué parches no fueron aplicados). La capa de presión establece qué incentivos hicieron que las decisiones de la capa anterior fueran racionales para quien las tomó — la misma estructura de presión que el cap. 12 establece para el Challenger y el Boeing 737 MAX.

Taxonomía General de Aplicaciones

Tipo de

Función en el

grafo INCF típico S típica

nodo

Arquitecto de la seguridad (AS)

Diseñó la arquitectura de seguridad del sistema comprometido: las decisiones sobre qué controles implementar, qué superficie de ataque exponer, qué privilegios otorgar. Es el nodo de mayor INCF en la mayoría de las brechas significativas.

Alto [0.28– 0.52] cuando la arquitectura tenía deficiencias que el estándar del sector del período no justificaba.

Moderado-bajo [0.22–0.45] cuando las deficiencias eran idiosincráticas de ese sistema específico.

Responsable de gestión de parches (RGP)

Tenía la responsabilidad de identificar y aplicar los parches de seguridad disponibles. INCF positivo cuando existía un parche oficial para la vulnerabilidad explotada que no había sido aplicado en el tiempo razonable del estándar del sector.

Alto [0.32– 0.55] cuando el parche existía y no fue aplicado.

Moderado-alto [0.40–0.65] cuando la no aplicación del parche era la práctica habitual del sector del período.

CISO / Director de Seguridad (CISO)

El ejecutivo con la responsabilidad institucional de la seguridad de

Moderado [0.20–0.38] cuando las decisiones de priorización

Alto [0.55–0.78] cuando los recursos de seguridad eran el estándar del

Taxonomía General de Aplicaciones

Tipo de

Función en el

grafo INCF típico S típica

nodo

los sistemas de información. INCF positivo cuando conocía las deficiencias del sistema y no priorizó su corrección, o cuando diseñó el programa de seguridad con recursos insuficientes para el nivel de riesgo conocido.

eran idiosincráticas de esa organización.

sector para ese tipo de organización.

Atacante externo (AE)

El actor que explotó la vulnerabilidad y produjo el daño. INCF positivo sobre el D_total, pero S frecuentemente alta: otro atacante con las mismas herramientas habría producido el mismo resultado dado la vulnerabilidad.

Moderado [0.20–0.40] — el INCF del atacante es real pero no dominante cuando la vulnerabilidad era genérica.

Alta [0.55–0.85] cuando explotó una vulnerabilidad genérica con herramientas ampliamente disponibles. Moderada-baja [0.25–0.45] cuando el ataque requería capacidades sofisticadas.

Proveedor de software con vulnerabilidad (PSV)

El proveedor que vendió o distribuyó el software con la vulnerabilidad explotada. INCF positivo cuando la vulnerabilidad

Moderado-alto [0.28– 0.48] cuando la vulnerabilidad era conocida y el parche no

Moderado [0.35– 0.60] cuando la gestión de parches del proveedor era el estándar del sector.

Taxonomía General de Aplicaciones

Tipo de

Función en el

grafo INCF típico S típica

nodo

era conocida por el proveedor antes de la brecha y no había sido parcheada o comunicada.

fue distribuido.

Regulador / auditor de cumplimiento (RAC)

El regulador que estableció los requisitos mínimos de seguridad o el auditor que certificó el cumplimiento. INCF positivo cuando los requisitos eran insuficientes para el nivel de riesgo conocido o cuando la certificación fue emitida sin verificación adecuada.

Moderado [0.10–0.28] por omisión regulatoria.

Alto [0.65–0.85] — la mayoría de los reguladores del período con las mismas restricciones habrían establecido los mismos requisitos.

### §3.1  El IAS_cyber: el aprendizaje sistémico post-brecha

IAS_cyber = J_sistema_post_brecha −

J_sistema_pre_brecha El IAS_cyber mide en qué medida el sistema de seguridad incorporó las lecciones de la brecha en su diseño post-incidente. Un IAS_cyber próximo a cero indica que las reformas post-brecha no redujeron el déficit de asunción en los nodos de mayor INCF: la organización cambió los controles superficiales (actualizó las contraseñas, instaló un nuevo firewall) sin modificar la arquitectura de incentivos que hizo que la decisión de no aplicar el parche

Taxonomía General de Aplicaciones

fuera racional para el responsable. El isomorfismo con el Challenger: el Informe Rogers identificó la junta teórica como causa y el sistema de decisión como contexto — invirtiendo la distribución correcta del INCF. El IAS_Challenger fue bajo porque la reforma no actuó sobre el nodo de mayor INCF.

### §4  Los Hijos del responsable de seguridad en la decisión crítica

Los Hijos de Afrodita aplican en ciberseguridad a los actores con voluntad propia que tomaron las decisiones críticas que hicieron posible la brecha a esa escala. La frase más reveladora del caso Challenger — «ponte el sombrero de gestión y deja el de ingeniero» — tiene su equivalente exacto en ciberseguridad en la frase que aparece en los informes post-brecha de casi todas las organizaciones significativas: «sabíamos del riesgo, pero no teníamos los recursos para mitigarlo». Esa frase es la firma del Fobos del CISO: sabía de la vulnerabilidad (la información de riesgo existía), no actuó (el Fobos de las consecuencias de pedir más presupuesto), y el sistema que no conectaba la información del riesgo con el poder de decisión (la estructura que hace que el Fobos sea la respuesta racional) tiene el INCF más alto del grafo.

Hijo

del CISO

Qué informa para S e INCF

Firma en ciberseguridad R* resultante

/ AS

Anteros S moderado-bajo. El responsable de seguridad tomó decisiones deliberadas que reducían los controles a sabiendas del riesgo: eligió

Documentos internos donde el responsable reconoció el riesgo específico y decidió no mitigarlo por razones documentadas.

INCF del responsable alto con S bajo. Responsabilidad civil alta. Potencialmente penal cuando la decisión fue deliberada y el daño severo.

Taxonomía General de Aplicaciones

Hijo

del CISO

Qué informa para S e INCF

Firma en ciberseguridad R* resultante

/ AS

una arquitectura insegura para ahorrar costos sabiendo que creaba vulnerabilidades críticas, o decidió no aplicar parches críticos sabiendo del riesgo porque el proceso de parching interfería con las operaciones.

Análisis de riesgo realizados que identificaban la vulnerabilidad sin la mitigación subsecuente.

Fobos S moderado [0.35–0.58]. El responsable conocía las deficiencias de seguridad pero no escaló el problema ni solicitó los recursos necesarios por miedo a las consecuencias: el miedo a ser percibido como alarmista, el miedo a que el presupuesto solicitado fuera rechazado, el miedo a las consecuencias de retrasar el lanzamiento de un producto o servicio por

Correos donde el responsable identifica el riesgo, pero lo escala sin la urgencia que el nivel de riesgo requería. Evidencia de que la solicitud de recursos fue hecha, pero con prioridad baja. El patrón de «conocíamos el riesgo pero no teníamos los recursos».

INCF del responsable moderado. La estructura que hace racional el Fobos (el sistema que castiga al que escala riesgos) tiene mayor INCF que el responsable individual.

Taxonomía General de Aplicaciones

Hijo

del CISO

Qué informa para S e INCF

Firma en ciberseguridad R* resultante

/ AS

requisitos de seguridad.

Deimos S alto [0.55– 0.80]. El responsable genuinamente no anticipó que la configuración de seguridad era insuficiente porque el nivel de amenaza del período no lo hacía evidente, o porque la vulnerabilidad específica no era conocida públicamente. El daño fue consecuencia del riesgo inherente de la operación de sistemas digitales.

Arquitectura de seguridad coherente con el estándar del sector del período. Ausencia de señales de que el responsable conocía la vulnerabilidad específica. Respuesta inmediata y proporcional cuando la brecha fue detectada.

INCF bajo. El riesgo sistémico del dominio es la condición dominante. La reforma del estándar del sector es el instrumento correcto.

### §5  Casos resueltos

Caso A — WannaCry (mayo 2017): el parche disponible y el INCF de la gestión de TI

El 12 de mayo de 2017, el ransomware WannaCry cifró más de 200,000 sistemas en 150 países. El vector técnico era EternalBlue — una herramienta de explotación de la vulnerabilidad MS17-010 en el protocolo SMB de Windows, desarrollada por la NSA y filtrada por el grupo Shadow

Taxonomía General de Aplicaciones

Brokers en abril de 2017. Microsoft había publicado el parche para MS17-010 el 14 de marzo de 2017 — casi dos meses antes del ataque. Los sistemas afectados no habían aplicado el parche disponible.

Nodo Actor/Factor INCF S Análisis

N1 Gestión de TI de las organizaciones afectadas (no aplicaron el parche)

~42% 0.35 INCF alto: el parche existía, era gratuito y había sido distribuido por Microsoft dos meses antes del ataque. La no aplicación del parche fue la condición necesaria dominante de que WannaCry pudiera comprometer esos sistemas específicos. S moderado-bajo: la decisión de no aplicar parches críticos en dos meses era más lenta que el estándar del sector del período para vulnerabilidades críticas.

N2 NSA (desarrolló EternalBlue sin reportarlo a Microsoft)

~28% 0.45 INCF moderado-alto: si la NSA hubiera reportado la vulnerabilidad a Microsoft siguiendo el proceso de divulgación responsable, el parche habría existido mucho antes y el período de exposición habría sido menor. S moderado: la decisión de acumular vulnerabilidades sin divulgarlas era la práctica estándar de muchos servicios de inteligencia del período.

N3 Shadow Brokers (filtró EternalBlue)

~18% 0.62 INCF moderado: la filtración fue condición de que la herramienta estuviera disponible para actores no sofisticados. S

Taxonomía General de Aplicaciones

Nodo Actor/Factor INCF S Análisis

moderado-alto: otras organizaciones con capacidades similares habrían podido filtrar o vender herramientas similares.

N4 Atacante (WannaCry)

~8% 0.78 INCF bajo: el código WannaCry fue construido con herramientas ampliamente disponibles post-filtración. Cualquier actor con capacidades técnicas modestas habría podido producir el mismo ataque dado el vector disponible. S alta.

N5 Microsoft (por no haber parchado más rápido versiones fuera de soporte)

~4% 0.82 INCF bajo: Windows XP y Server 2003 estaban fuera del ciclo de soporte. Microsoft publicó un parche de emergencia para esas versiones después del ataque.

El resultado central: el nodo de mayor INCF no es el atacante (8%) sino la gestión de TI de las organizaciones que no aplicaron el parche disponible (42%). La narrativa que concentra la responsabilidad en el atacante o en la NSA reproduce la inversión causal clásica: el nodo de mayor visibilidad no es el de mayor INCF. La reforma que previene el próximo WannaCry no es la captura del grupo atacante ni la eliminación de la NSA: es la implementación de los procesos de gestión de parches que el estándar del sector requería.

Caso B — Equifax (septiembre 2017): la vulnerabilidad conocida sin parche

### En septiembre de 2017, Equifax reportó una brecha que expuso los datos personales y financieros de 147 millones de personas. El vector de ataque fue Apache Struts CVE-2017-

Taxonomía General de Aplicaciones

5638 — una vulnerabilidad crítica para la que Apache había publicado el parche el 7 de marzo de 2017. El atacante accedió a los sistemas de Equifax el 12 de mayo de 2017 — 66 días después de que el parche estuviera disponible. El Departamento de Seguridad Nacional de los EEUU había enviado una notificación específica a Equifax sobre esa vulnerabilidad el 8 de marzo de 2017 — el día siguiente de la publicación del parche.

Nodo Actor/Factor INCF S Análisis

N1 Equifax CISO y gestión de TI (no aplicaron el parche en 66 días con notificación directa)

~45% 0.28 INCF muy alto: la organización recibió notificación directa del DHS el día siguiente de que el parche estuviera disponible. La no aplicación del parche en 66 días con notificación directa era significativamente más lenta que el estándar del sector para vulnerabilidades críticas con notificación activa. S bajo: esa velocidad de respuesta era idiosincrática de la gestión de Equifax — otras organizaciones del sector procesaron el parche más rápidamente.

N2 Sistema de monitoreo de tráfico SSL (no detectó el ataque durante 76 días)

~25% 0.45 El certificado SSL de monitoreo del sistema había expirado en enero de 2017 — meses antes del ataque. El tráfico del atacante pasó sin inspección durante 76 días. INCF alto: el fallo del sistema de detección fue condición de que el ataque no fuera detectado y detenido.

N3 Arquitectura de

~18% 0.42 La vulnerabilidad de Apache Struts estaba en

Taxonomía General de Aplicaciones

Nodo Actor/Factor INCF S Análisis

segmentación de redes (acceso excesivo desde el punto de entrada)

una aplicación expuesta a internet, pero el atacante pudo moverse lateralmente hacia bases de datos que contenían datos sensibles de 147 millones de personas. El principio de menor privilegio y la segmentación de redes no estaban implementados adecuadamente.

N4 Atacante ~8% 0.72 INCF bajo relativo. Cualquier actor con conocimiento de la vulnerabilidad y las herramientas disponibles habría podido producir la misma brecha dado el estado del sistema de Equifax.

N5 Reguladores (FTC, CFPB) por estándares insuficientes para custodios de datos de 147M personas

~4% 0.80 Los estándares regulatorios del período para empresas de credit reporting no requerían explícitamente la gestión de parches críticos en plazos específicos.

D_total del caso Equifax: 147 millones de personas con datos personales y financieros expuestos. D_monetary: acuerdo con la FTC, CFPB y estados de $575 millones + costos de remediación ~$1,400 millones. El AD_N1 (CISO y gestión de TI) = 0.45 × $1,975M ≈ $889M. La CISO de Equifax fue reemplazada en el mes siguiente a la revelación de la brecha. El IAS_Equifax post-brecha: la organización implementó un programa agresivo de gestión de parches y controles adicionales — IAS positivo pero concentrado en los controles superficiales, con menor atención a los incentivos estructurales que hicieron que el Fobos fuera la respuesta racional para el CISO.

Taxonomía General de Aplicaciones

### §6  Preguntas que responde este capítulo

Pregunta del

Instrumento que la

responde Nivel de certeza

caso

¿El vector técnico fue el nodo de mayor INCF o hay un nodo de decisión humana con INCF mayor?

Construcción del grafo de tres capas (técnica, decisión, presión): ¿existía un parche para la vulnerabilidad explotada? ¿Cuánto tiempo llevaba disponible? ¿El responsable tenía notificación directa del riesgo?

Declaración A con análisis forense Cd1 + documentación de la gestión de parches. Declaración B con Cd2/Cd3 + registros parciales.

¿El S del arquitecto de seguridad era alto o bajo — la deficiencia era el estándar del sector?

Comparación con el estándar de gestión de parches del sector del período para el tipo y criticidad de la vulnerabilidad. Análisis de las prácticas de organizaciones equivalentes.

Declaración B con análisis Cd3 del estándar del sector + Cd4 de las prácticas de la organización.

¿El proveedor de software tiene INCF positivo — la vulnerabilidad era conocida?

Análisis del registro de vulnerabilidades del proveedor (CVE database), el timeline de la publicación del parche, y la comunicación al usuario final.

Declaración A con registro CVE Cd1 + documentación de la comunicación del parche. Declaración B con análisis Cd2/Cd3.

¿El IAS_cyber fue positivo — la reforma post-brecha actuó sobre los nodos de mayor INCF?

Análisis de las reformas implementadas después de la brecha: ¿actuaron sobre los procesos de gestión de parches y la arquitectura de seguridad (nodos de mayor INCF) o solo sobre los controles superficiales?

Declaración B con análisis Cd3/Cd4 de las reformas post-brecha.

¿Cuál es el D_total — incluyendo el D_reputacional y el D_a

D_total = D_directo (costos de remediación, multas regulatorias) + D_reputacional (pérdida de clientes, prima de riesgo

Declaración B con análisis Cd4/Cd5 del D_directo. Declaración C para D_reputacional y

Taxonomía General de Aplicaciones

Pregunta del

Instrumento que la

responde Nivel de certeza

caso

terceros afectados?

adicional) + D_afectados (daño a los titulares de los datos exfiltrados: fraude facilitado, tiempo de gestión, estrés).

D_afectados individuales.

### §7  Límites y errores frecuentes

Límite 1 — La atribución del atacante tiene incertidumbre alta. Establecer quién fue el atacante externo con certeza Cd1 requiere inteligencia técnica que frecuentemente no está disponible para el análisis de responsabilidad civil. El análisis de la responsabilidad puede distribuir el R* entre el arquitecto de la defensa y el atacante externo sin necesidad de identificar al atacante con certeza Cd1.

Límite 2 — La distinción entre la vulnerabilidad conocida y la vulnerabilidad desconocida determina el INCF. El análisis debe verificar si la vulnerabilidad explotada estaba en el registro público de vulnerabilidades (CVE) antes del ataque: si sí, el INCF del responsable de la gestión de parches es alto. Si era un zero-day, el INCF del proveedor de software y del arquitecto de la defensa por controles de mitigación alternativos es el instrumento.

Error Por qué

ocurre Consecuencia Corrección

Concentrar el R* en el atacante externo ignorando el INCF del arquitecto de la defensa

La narrativa pública de la brecha identifica al atacante como el causante.

INCF del arquitecto de la defensa no capturado. El responsable de la no aplicación del parche evade la responsabilidad.

El INCF del atacante se establece con S: ¿otro atacante con las mismas herramientas habría producido el mismo resultado? Si sí (vulnerabilidad

Taxonomía General de Aplicaciones

Error Por qué

ocurre Consecuencia Corrección

genérica con parche disponible), el INCF del atacante es bajo relativo.

No distinguir entre vulnerabilidad conocida y zero-day para establecer el INCF

El análisis trata todas las brechas como si el responsable hubiera podido prevenir el ataque.

INCF del responsable sobreestimado cuando el ataque usó un zero-day desconocido.

El análisis del CVE y la timeline del parche es el primer paso del análisis de responsabilidad en ciberseguridad.

Ignorar el D_a los afectados individuales en brechas de datos personales

El análisis calcula el D de la organización (multas, costos de remediación) sin el D a los titulares de los datos.

D_total subestimado. Los afectados individuales son el Nf más vulnerable del grafo.

El D_afectados incluye: el fraude facilitado por los datos exfiltrados, el tiempo de gestión de las consecuencias, y el daño a la trayectoria crediticia o financiera de los afectados.

### §8  Guía de prioridades de evidencia

Incertidum

Evidencia que más la

Qué rango reduce

Por qué funciona

Qué buscar

bre principal

reduce

### 1. ¿Existía el parche — cuál es el INCF de la gestión de TI?

Registro CVE de la vulnerabilid ad + fecha de publicación

La existencia del parche y la timeline de aplicación

INCF del arquitec to de la defensa.

¿Estaba la vulnerabilid ad en el CVE antes del ataque? ¿Cuándo

Taxonomía General de Aplicaciones

Incertidum

Evidencia que más la

Qué rango reduce

Por qué funciona

Qué buscar

bre principal

reduce

del parche + registros internos de gestión de parches.

establecen el INCF del responsabl e de la gestión de parches.

fue publicado el parche? ¿La organizació n tenía un proceso de gestión de parches documenta do?

### 2. ¿El S del responsable de seguridad era alto o bajo?

Análisis comparado de las prácticas del sector del período para el tipo de vulnerabilid ad y organizació n.

El S del responsabl e determina si la reforma debe ser individual o sistémica.

S del arquitec to de la defensa.

¿Cuál era el tiempo promedio de aplicación de parches críticos en el sector del período? ¿La organizació n estaba por encima o por debajo del promedio?

### 3. ¿El proveedor de software tiene INCF positivo?

Timeline de la vulnerabilid ad: ¿cuándo la conoció el proveedor? ¿Cuándo publicó el parche? ¿Comunicó el riesgo a los usuarios?

El INCF del proveedor depende de si tenía conocimien to previo de la vulnerabili dad y no la comunicó.

INCF del proveed or de software .

¿Hay registros de que el proveedor conocía la vulnerabilid ad antes de la publicación del CVE? ¿El proceso de divulgación del proveedor seguía el

Taxonomía General de Aplicaciones

Incertidum

Evidencia que más la

Qué rango reduce

Por qué funciona

Qué buscar

bre principal

reduce

estándar del sector?

— Fin del Capítulo 48 —

Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

