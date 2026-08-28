## PARTE VII · Ingeniería y Tecnología

### Capítulo 48
Ciberseguridad — responsabilidad en
brechas y ataques
Organ. Estru. Model. Educa. Crisi.
Para el mediador que busca precisión · Cómo usar este
capítulo
Este capítulo es Compilación directa: aplica el cap. 12 de El cálculo de
la responsabilidad (Ingeniería de sistemas y confiabilidad) al dominio de
la ciberseguridad, con adaptaciones para las características específicas de
los sistemas digitales. El instrumento central es el INCF (Índice de
Necesidad Causal del Fallo) aplicado a brechas de datos y ataques
cibernéticos: no pregunta «¿cuál fue el vector del ataque?» sino «¿sin qué
decisión u omisión del arquitecto de seguridad el ataque no habría
producido daño a esa escala?»
La distinción central del dominio: la S del atacante externo es
frecuentemente alta — otro atacante con acceso a las mismas
herramientas habría explotado la misma vulnerabilidad. El R* del
atacante sobre el D_total es real pero moderado cuando la
vulnerabilidad era conocida y el parche existía: el nodo de mayor R* es
el arquitecto de la defensa que no implementó el parche disponible o que
diseñó el sistema sin los controles que el estándar del sector requería. Si
tu caso es de brecha por vulnerabilidad no parcheada, ve a §3 y §5 caso
A. Si es de ataque de phishing o ingeniería social, ve a §5 caso B. Para
responsabilidad del proveedor de software, ve a §4.
§1 Descripción del subcampo

Taxonomía General de Aplicaciones
La ciberseguridad es el dominio de la ingeniería donde la
distinción entre el fallo técnico y la decisión humana que lo
habilitó es más difícil y más frecuentemente confundida. La
narrativa espontánea de una brecha de datos concentra el R*
en el atacante externo — el hacker, el grupo de ransomware,
el Estado adversario. El análisis causal establece
sistemáticamente que el atacante tiene S alta: otro atacante con
acceso a las mismas herramientas habría explotado la misma
vulnerabilidad, porque la vulnerabilidad existía
independientemente del atacante específico. El nodo de mayor
R* en la mayoría de las brechas significativas es el arquitecto
de la seguridad del sistema atacado — el que diseñó el sistema
sin los controles del estándar, el que no aplicó el parche
disponible, el que otorgó privilegios de acceso excesivos que
amplificaron el alcance de la brecha.
INCF_cyber: la reformulación de la pregunta central
INCF_cyber(nodo_i) = P (daño_a_esa_escala | sin la decisión/omisión
del nodo_i) → diferencial respecto a P (daño | con el nodo_i)
El INCF_cyber traslada la pregunta del FTA convencional (¿cuál fue el
vector técnico del ataque?) a la pregunta de responsabilidad (¿sin qué decisión
humana el ataque no habría producido daño a esa escala?). La respuesta
establece el nodo de mayor INCF_cyber — que frecuentemente no es el
atacante sino el arquitecto de la defensa con S moderado-bajo: ese sistema
específico de seguridad era idiosincrático en sus deficiencias, y el parche
disponible habría prevenido la brecha.
Sub-variantes del dominio de ciberseguridad
Sub-variante Descripción
Brecha por El sistema fue comprometido a través de una
vulnerabilidad vulnerabilidad conocida para la que existía un parche
no parcheada oficial no aplicado. El R* del atacante es real pero
moderado — cualquier atacante con acceso a las
herramientas disponibles habría explotado la misma
vulnerabilidad. El INCF del responsable de la

Taxonomía General de Aplicaciones
Sub-variante Descripción
gestión de parches es alto: la no aplicación del parche
fue condición necesaria de que la brecha produjera
daño a esa escala.
Ataque de El atacante engañó a un empleado para obtener
ingeniería social credenciales o acceso. La distinción del dominio: el
(phishing, S del empleado que fue engañado es típicamente alto
spear-phishing) (cualquier empleado en esa posición, sin la
formación y los controles adecuados, habría
respondido igual); el INCF del responsable del
programa de formación y los controles técnicos de
detección es alto.
Ataque de El atacante comprometió el software de un
cadena de proveedor para llegar a los sistemas de sus clientes.
suministro El caso SolarWinds: el atacante insertó código
(supply chain malicioso en las actualizaciones del software de
attack) monitoreo. La distribución del R* requiere el análisis
de la cadena: el proveedor comprometido (con
INCF positivo sobre la falta de controles de
integridad del código), y el cliente que instaló el
software comprometido sin verificación adicional.
Ransomware: El atacante cifró los sistemas y exige rescate. La
cifrado de distribución del R* entre el atacante (con S
sistemas y moderada — el ransomware explota
extorsión vulnerabilidades genéricas pero requiere capacidad
operacional no trivial), el arquitecto de la seguridad
(INCF positivo si los sistemas no tenían backups
adecuados ni segmentación que hubiera limitado el
alcance), y el CISO que autorizó el pago del rescate.
Brecha de datos Un insider (empleado o contratista) accedió a datos
por acceso a los que no debería haber tenido acceso dado su rol,
interno excesivo causando daño. La distinción del dominio: el
diseñador del sistema de control de acceso tiene
INCF positivo cuando los privilegios otorgados eran
excesivos respecto al rol — el principio de menor
privilegio no fue implementado.
Responsabilidad El proveedor de software vendió o distribuyó un
del proveedor producto con vulnerabilidades conocidas que el
de software con proveedor tenía documentadas, pero no había
vulnerabilidades comunicado ni parcheado antes de la distribución. El
conocidas INCF del proveedor es alto cuando la vulnerabilidad

Taxonomía General de Aplicaciones
Sub-variante Descripción
era conocida y el parche disponible no fue
distribuido en tiempo razonable.
§2 Escala de evidencia Cd0–Cd8 · Código
digital / documentación técnica
La escala Cd0–Cd8 es la escala de evidencia de la Parte VII. Se
aplica al dominio de ciberseguridad con énfasis en la cadena
de custodia forense digital — la verificación de que los
artefactos digitales (logs, imágenes de disco, capturas de red)
no han sido alterados desde su recolección — y en la capacidad
de los análisis para establecer la cadena causal entre la
vulnerabilidad explotada, el actor que no la mitigó, y el daño
producido.
Tipo de
Rango
Nivel evidencia en Descripción y ejemplos
w
ciberseguridad
Cd1 Análisis forense El análisis forense de los [0.72,
digital con sistemas comprometidos con 0.90]
cadena de metodología documentada,
custodia cadena de custodia de los
verificada + artefactos digitales, y
logs de sistema verificación criptográfica de la
con integridad integridad de los logs. Incluye la
criptográfica reconstitución de la timeline del
ataque desde los logs
verificados, la identificación del
vector de entrada y la trayectoria
del atacante dentro del sistema.
Cd2 Análisis forense El informe de análisis forense [0.62,
de segunda de una empresa de respuesta a 0.80]
parte (empresa incidentes acreditada que tuvo
de respuesta a acceso completo a los sistemas
incidentes) con comprometidos, con
acceso metodología documentada y
completo a los acceso a los artefactos
sistemas + primarios. Incluye el análisis del

Taxonomía General de Aplicaciones
Tipo de
Rango
Nivel evidencia en Descripción y ejemplos
w
ciberseguridad
análisis del código malicioso (malware
código reverse engineering) que
malicioso establece el origen, los vectores
y las capacidades del atacante.
Cd3 Análisis Cuando dos o más análisis [0.52,
convergente de técnicos independientes de 0.70]
múltiples entidades acreditadas convergen
fuentes técnicas en la descripción de la misma
independientes cadena causal del incidente,
sobre el mismo incluyendo el vector de ataque,
incidente los sistemas comprometidos, y
el alcance del daño.
Cd4 Informe del Los informes de los centros de [0.40,
proveedor de respuesta a emergencias (CERT, 0.58]
ciberseguridad o CSIRT) o de proveedores de
del CERT con ciberseguridad sobre el
metodología incidente, con metodología
parcialmente parcialmente documentada y
documentada acceso parcial a los sistemas
comprometidos.
Cd5 Análisis de logs Los logs del sistema o de la red [0.26,
sin cadena de analizados sin cadena de 0.44]
custodia forense custodia forense verificada, y las
verificada + declaraciones del equipo de TI
declaraciones interno que gestionó el
del equipo de TI incidente.
interno
Cd6 Investigación Los reportes de medios [0.14,
periodística con especializados en ciberseguridad 0.28]
fuentes técnicas basados en fuentes técnicas
anónimas anónimas del equipo interno de
dentro de la la organización afectada.
organización
afectada
Cd7 Declaraciones Los comunicados oficiales de la [0.04,
públicas de la organización afectada sobre la 0.16]
organización brecha, sin corroboración
afectada sin técnica de análisis forense
corroboración independiente.

Taxonomía General de Aplicaciones
Tipo de
Rango
Nivel evidencia en Descripción y ejemplos
w
ciberseguridad
técnica
independiente
Cd8 Inferencia del La inferencia del tipo y escala [0.02,
incidente desde del incidente exclusivamente 0.10]
el impacto desde el impacto observable
observable sin (datos publicados, sistemas
análisis técnico inaccesibles, notificaciones a
del vector afectados) sin ningún análisis
técnico del vector de ataque.
Cd0 Análisis forense El análisis forense Cd1 que w =
Cd1 que establece positivamente que el 0.00
establece que la vector de ataque no
brecha no fue corresponde a la vulnerabilidad
causada por la atribuida al actor o que la cadena
vulnerabilidad o causal propuesta es
la conducta del técnicamente imposible dado la
actor imputado arquitectura del sistema.
§3 Las herramientas del análisis de
responsabilidad en ciberseguridad
El análisis de responsabilidad en ciberseguridad opera en tres
capas simultáneas que deben construirse separadamente antes
de integrarse. La capa técnica establece el vector de ataque
(qué vulnerabilidad fue explotada, con qué herramientas, por
qué ruta) y el alcance del daño (qué datos fueron accedidos,
exfiltrados o cifrados). La capa de decisión establece quién
tomó qué decisiones que hicieron posible el ataque a esa escala
(qué arquitectura de seguridad fue diseñada, qué controles no
fueron implementados, qué parches no fueron aplicados). La
capa de presión establece qué incentivos hicieron que las
decisiones de la capa anterior fueran racionales para quien las
tomó — la misma estructura de presión que el cap. 12
establece para el Challenger y el Boeing 737 MAX.

Taxonomía General de Aplicaciones
Tipo de Función en el
INCF típico S típica
nodo grafo
Arquitecto de Diseñó la Alto [0.28– Moderado-bajo
la seguridad arquitectura de 0.52] cuando [0.22–0.45]
(AS) seguridad del la arquitectura cuando las
sistema tenía deficiencias eran
comprometido: deficiencias idiosincráticas de
las decisiones que el ese sistema
sobre qué estándar del específico.
controles sector del
implementar, período no
qué superficie justificaba.
de ataque
exponer, qué
privilegios
otorgar. Es el
nodo de mayor
INCF en la
mayoría de las
brechas
significativas.
Responsable Tenía la Alto [0.32– Moderado-alto
de gestión de responsabilidad 0.55] cuando [0.40–0.65]
parches de identificar y el parche cuando la no
(RGP) aplicar los existía y no aplicación del
parches de fue aplicado. parche era la
seguridad práctica habitual
disponibles. del sector del
INCF positivo período.
cuando existía
un parche
oficial para la
vulnerabilidad
explotada que
no había sido
aplicado en el
tiempo
razonable del
estándar del
sector.
CISO / El ejecutivo Moderado Alto [0.55–0.78]
Director de con la [0.20–0.38] cuando los
Seguridad responsabilidad cuando las recursos de
(CISO) institucional de decisiones de seguridad eran el
la seguridad de priorización estándar del

Taxonomía General de Aplicaciones
Tipo de Función en el
INCF típico S típica
nodo grafo
los sistemas de eran sector para ese
información. idiosincráticas tipo de
INCF positivo de esa organización.
cuando conocía organización.
las deficiencias
del sistema y no
priorizó su
corrección, o
cuando diseñó
el programa de
seguridad con
recursos
insuficientes
para el nivel de
riesgo
conocido.
Atacante El actor que Moderado Alta [0.55–0.85]
externo (AE) explotó la [0.20–0.40] cuando explotó
vulnerabilidad — el INCF una
y produjo el del atacante es vulnerabilidad
daño. INCF real pero no genérica con
positivo sobre dominante herramientas
el D_total, pero cuando la ampliamente
S vulnerabilidad disponibles.
frecuentemente era genérica. Moderada-baja
alta: otro [0.25–0.45]
atacante con las cuando el ataque
mismas requería
herramientas capacidades
habría sofisticadas.
producido el
mismo
resultado dado
la
vulnerabilidad.
Proveedor de El proveedor Moderado- Moderado [0.35–
software con que vendió o alto [0.28– 0.60] cuando la
vulnerabilidad distribuyó el 0.48] cuando gestión de
(PSV) software con la la parches del
vulnerabilidad vulnerabilidad proveedor era el
explotada. era conocida y estándar del
INCF positivo el parche no sector.
cuando la
vulnerabilidad

Taxonomía General de Aplicaciones
Tipo de Función en el
INCF típico S típica
nodo grafo
era conocida fue
por el distribuido.
proveedor
antes de la
brecha y no
había sido
parcheada o
comunicada.
Regulador / El regulador Moderado Alto [0.65–0.85]
auditor de que estableció [0.10–0.28] — la mayoría de
cumplimiento los requisitos por omisión los reguladores
(RAC) mínimos de regulatoria. del período con
seguridad o el las mismas
auditor que restricciones
certificó el habrían
cumplimiento. establecido los
INCF positivo mismos
cuando los requisitos.
requisitos eran
insuficientes
para el nivel de
riesgo
conocido o
cuando la
certificación
fue emitida sin
verificación
adecuada.
§3.1 El IAS_cyber: el aprendizaje sistémico post-brecha
IAS_cyber = J_sistema_post_brecha −
J_sistema_pre_brecha
El IAS_cyber mide en qué medida el sistema de seguridad incorporó las
lecciones de la brecha en su diseño post-incidente. Un IAS_cyber próximo a
cero indica que las reformas post-brecha no redujeron el déficit de asunción en
los nodos de mayor INCF: la organización cambió los controles superficiales
(actualizó las contraseñas, instaló un nuevo firewall) sin modificar la
arquitectura de incentivos que hizo que la decisión de no aplicar el parche

Taxonomía General de Aplicaciones
fuera racional para el responsable. El isomorfismo con el Challenger: el
Informe Rogers identificó la junta teórica como causa y el sistema de decisión
como contexto — invirtiendo la distribución correcta del INCF. El
IAS_Challenger fue bajo porque la reforma no actuó sobre el nodo de mayor
INCF.
§4 Los Hijos del responsable de seguridad en
la decisión crítica
Los Hijos de Afrodita aplican en ciberseguridad a los actores
con voluntad propia que tomaron las decisiones críticas que
hicieron posible la brecha a esa escala. La frase más reveladora
del caso Challenger — «ponte el sombrero de gestión y deja el
de ingeniero» — tiene su equivalente exacto en ciberseguridad
en la frase que aparece en los informes post-brecha de casi
todas las organizaciones significativas: «sabíamos del riesgo,
pero no teníamos los recursos para mitigarlo». Esa frase es la
firma del Fobos del CISO: sabía de la vulnerabilidad (la
información de riesgo existía), no actuó (el Fobos de las
consecuencias de pedir más presupuesto), y el sistema que no
conectaba la información del riesgo con el poder de decisión
(la estructura que hace que el Fobos sea la respuesta racional)
tiene el INCF más alto del grafo.
Hijo
del Qué informa Firma en
R* resultante
CISO para S e INCF ciberseguridad
/ AS
Anteros S moderado- Documentos INCF del
bajo. El internos donde responsable alto con
responsable de el responsable S bajo.
seguridad tomó reconoció el Responsabilidad civil
decisiones riesgo alta. Potencialmente
deliberadas que específico y penal cuando la
reducían los decidió no decisión fue
controles a mitigarlo por deliberada y el daño
sabiendas del razones severo.
riesgo: eligió documentadas.

Taxonomía General de Aplicaciones
Hijo
del Qué informa Firma en
R* resultante
CISO para S e INCF ciberseguridad
/ AS
una arquitectura Análisis de
insegura para riesgo
ahorrar costos realizados que
sabiendo que identificaban la
creaba vulnerabilidad
vulnerabilidades sin la mitigación
críticas, o subsecuente.
decidió no
aplicar parches
críticos
sabiendo del
riesgo porque el
proceso de
parching
interfería con
las operaciones.
Fobos S moderado Correos donde INCF del
[0.35–0.58]. El el responsable responsable
responsable identifica el moderado. La
conocía las riesgo, pero lo estructura que hace
deficiencias de escala sin la racional el Fobos (el
seguridad pero urgencia que el sistema que castiga al
no escaló el nivel de riesgo que escala riesgos)
problema ni requería. tiene mayor INCF
solicitó los Evidencia de que el responsable
recursos que la solicitud individual.
necesarios por de recursos fue
miedo a las hecha, pero con
consecuencias: prioridad baja.
el miedo a ser El patrón de
percibido como «conocíamos el
alarmista, el riesgo pero no
miedo a que el teníamos los
presupuesto recursos».
solicitado fuera
rechazado, el
miedo a las
consecuencias
de retrasar el
lanzamiento de
un producto o
servicio por

Taxonomía General de Aplicaciones
Hijo
del Qué informa Firma en
R* resultante
CISO para S e INCF ciberseguridad
/ AS
requisitos de
seguridad.
Deimos S alto [0.55– Arquitectura de INCF bajo. El riesgo
0.80]. El seguridad sistémico del
responsable coherente con el dominio es la
genuinamente estándar del condición
no anticipó que sector del dominante. La
la configuración período. reforma del estándar
de seguridad era Ausencia de del sector es el
insuficiente señales de que el instrumento
porque el nivel responsable correcto.
de amenaza del conocía la
período no lo vulnerabilidad
hacía evidente, específica.
o porque la Respuesta
vulnerabilidad inmediata y
específica no proporcional
era conocida cuando la
públicamente. brecha fue
El daño fue detectada.
consecuencia
del riesgo
inherente de la
operación de
sistemas
digitales.
§5 Casos resueltos
Caso A — WannaCry (mayo 2017): el parche disponible y el
INCF de la gestión de TI
El 12 de mayo de 2017, el ransomware WannaCry cifró más
de 200,000 sistemas en 150 países. El vector técnico era
EternalBlue — una herramienta de explotación de la
vulnerabilidad MS17-010 en el protocolo SMB de Windows,
desarrollada por la NSA y filtrada por el grupo Shadow

Taxonomía General de Aplicaciones
Brokers en abril de 2017. Microsoft había publicado el parche
para MS17-010 el 14 de marzo de 2017 — casi dos meses antes
del ataque. Los sistemas afectados no habían aplicado el
parche disponible.
Nodo Actor/Factor INCF S Análisis
N1 Gestión de TI ~42% 0.35 INCF alto: el parche
de las existía, era gratuito y había
organizaciones sido distribuido por
afectadas (no Microsoft dos meses antes
aplicaron el del ataque. La no
parche) aplicación del parche fue
la condición necesaria
dominante de que
WannaCry pudiera
comprometer esos
sistemas específicos. S
moderado-bajo: la
decisión de no aplicar
parches críticos en dos
meses era más lenta que el
estándar del sector del
período para
vulnerabilidades críticas.
N2 NSA ~28% 0.45 INCF moderado-alto: si la
(desarrolló NSA hubiera reportado la
EternalBlue vulnerabilidad a Microsoft
sin reportarlo siguiendo el proceso de
a Microsoft) divulgación responsable,
el parche habría existido
mucho antes y el período
de exposición habría sido
menor. S moderado: la
decisión de acumular
vulnerabilidades sin
divulgarlas era la práctica
estándar de muchos
servicios de inteligencia
del período.
N3 Shadow ~18% 0.62 INCF moderado: la
Brokers (filtró filtración fue condición de
EternalBlue) que la herramienta
estuviera disponible para
actores no sofisticados. S

Taxonomía General de Aplicaciones
Nodo Actor/Factor INCF S Análisis
moderado-alto: otras
organizaciones con
capacidades similares
habrían podido filtrar o
vender herramientas
similares.
N4 Atacante ~8% 0.78 INCF bajo: el código
(WannaCry) WannaCry fue construido
con herramientas
ampliamente disponibles
post-filtración. Cualquier
actor con capacidades
técnicas modestas habría
podido producir el mismo
ataque dado el vector
disponible. S alta.
N5 Microsoft (por ~4% 0.82 INCF bajo: Windows XP
no haber y Server 2003 estaban
parchado más fuera del ciclo de soporte.
rápido Microsoft publicó un
versiones parche de emergencia para
fuera de esas versiones después del
soporte) ataque.
El resultado central: el nodo de mayor INCF no es el atacante (8%)
sino la gestión de TI de las organizaciones que no aplicaron el parche
disponible (42%). La narrativa que concentra la responsabilidad en el
atacante o en la NSA reproduce la inversión causal clásica: el nodo de
mayor visibilidad no es el de mayor INCF. La reforma que previene el
próximo WannaCry no es la captura del grupo atacante ni la
eliminación de la NSA: es la implementación de los procesos de gestión
de parches que el estándar del sector requería.
Caso B — Equifax (septiembre 2017): la vulnerabilidad
conocida sin parche
En septiembre de 2017, Equifax reportó una brecha que
expuso los datos personales y financieros de 147 millones de
personas. El vector de ataque fue Apache Struts CVE-2017-

Taxonomía General de Aplicaciones
5638 — una vulnerabilidad crítica para la que Apache había
publicado el parche el 7 de marzo de 2017. El atacante accedió
a los sistemas de Equifax el 12 de mayo de 2017 — 66 días
después de que el parche estuviera disponible. El
Departamento de Seguridad Nacional de los EEUU había
enviado una notificación específica a Equifax sobre esa
vulnerabilidad el 8 de marzo de 2017 — el día siguiente de la
publicación del parche.
Nodo Actor/Factor INCF S Análisis
N1 Equifax CISO ~45% 0.28 INCF muy alto: la
y gestión de organización recibió
TI (no notificación directa del
aplicaron el DHS el día siguiente de
parche en 66 que el parche estuviera
días con disponible. La no
notificación aplicación del parche en 66
directa) días con notificación
directa era
significativamente más
lenta que el estándar del
sector para
vulnerabilidades críticas
con notificación activa. S
bajo: esa velocidad de
respuesta era idiosincrática
de la gestión de Equifax —
otras organizaciones del
sector procesaron el
parche más rápidamente.
N2 Sistema de ~25% 0.45 El certificado SSL de
monitoreo de monitoreo del sistema
tráfico SSL había expirado en enero de
(no detectó el 2017 — meses antes del
ataque ataque. El tráfico del
durante 76 atacante pasó sin
días) inspección durante 76
días. INCF alto: el fallo del
sistema de detección fue
condición de que el ataque
no fuera detectado y
detenido.
N3 Arquitectura ~18% 0.42 La vulnerabilidad de
de Apache Struts estaba en

Taxonomía General de Aplicaciones
Nodo Actor/Factor INCF S Análisis
segmentación una aplicación expuesta a
de redes internet, pero el atacante
(acceso pudo moverse
excesivo lateralmente hacia bases de
desde el punto datos que contenían datos
de entrada) sensibles de 147 millones
de personas. El principio
de menor privilegio y la
segmentación de redes no
estaban implementados
adecuadamente.
N4 Atacante ~8% 0.72 INCF bajo relativo.
Cualquier actor con
conocimiento de la
vulnerabilidad y las
herramientas disponibles
habría podido producir la
misma brecha dado el
estado del sistema de
Equifax.
N5 Reguladores ~4% 0.80 Los estándares
(FTC, CFPB) regulatorios del período
por estándares para empresas de credit
insuficientes reporting no requerían
para custodios explícitamente la gestión
de datos de de parches críticos en
147M plazos específicos.
personas
D_total del caso Equifax: 147 millones de personas con datos
personales y financieros expuestos. D_monetary: acuerdo con la FTC,
CFPB y estados de $575 millones + costos de remediación ~$1,400
millones. El AD_N1 (CISO y gestión de TI) = 0.45 × $1,975M
≈ $889M. La CISO de Equifax fue reemplazada en el mes siguiente
a la revelación de la brecha. El IAS_Equifax post-brecha: la
organización implementó un programa agresivo de gestión de parches y
controles adicionales — IAS positivo pero concentrado en los controles
superficiales, con menor atención a los incentivos estructurales que
hicieron que el Fobos fuera la respuesta racional para el CISO.

Taxonomía General de Aplicaciones
§6 Preguntas que responde este capítulo
Pregunta del Instrumento que la
Nivel de certeza
caso responde
¿El vector Construcción del grafo de Declaración A con
técnico fue el tres capas (técnica, análisis forense Cd1 +
nodo de mayor decisión, presión): ¿existía documentación de la
INCF o hay un un parche para la gestión de parches.
nodo de vulnerabilidad explotada? Declaración B con
decisión ¿Cuánto tiempo llevaba Cd2/Cd3 + registros
humana con disponible? ¿El parciales.
INCF mayor? responsable tenía
notificación directa del
riesgo?
¿El S del Comparación con el Declaración B con
arquitecto de estándar de gestión de análisis Cd3 del
seguridad era parches del sector del estándar del sector +
alto o bajo — la período para el tipo y Cd4 de las prácticas
deficiencia era criticidad de la de la organización.
el estándar del vulnerabilidad. Análisis de
sector? las prácticas de
organizaciones
equivalentes.
¿El proveedor Análisis del registro de Declaración A con
de software vulnerabilidades del registro CVE Cd1 +
tiene INCF proveedor (CVE database), documentación de la
positivo — la el timeline de la comunicación del
vulnerabilidad publicación del parche, y la parche. Declaración B
era conocida? comunicación al usuario con análisis Cd2/Cd3.
final.
¿El IAS_cyber Análisis de las reformas Declaración B con
fue positivo — implementadas después de análisis Cd3/Cd4 de
la reforma post- la brecha: ¿actuaron sobre las reformas post-
brecha actuó los procesos de gestión de brecha.
sobre los nodos parches y la arquitectura de
de mayor seguridad (nodos de mayor
INCF? INCF) o solo sobre los
controles superficiales?
¿Cuál es el D_total = D_directo Declaración B con
D_total — (costos de remediación, análisis Cd4/Cd5 del
incluyendo el multas regulatorias) + D_directo.
D_reputacional D_reputacional (pérdida Declaración C para
y el D_a de clientes, prima de riesgo D_reputacional y

Taxonomía General de Aplicaciones
Pregunta del Instrumento que la
Nivel de certeza
caso responde
terceros adicional) + D_afectados D_afectados
afectados? (daño a los titulares de los individuales.
datos exfiltrados: fraude
facilitado, tiempo de
gestión, estrés).
§7 Límites y errores frecuentes
Límite 1 — La atribución del atacante tiene incertidumbre alta.
Establecer quién fue el atacante externo con certeza Cd1
requiere inteligencia técnica que frecuentemente no está
disponible para el análisis de responsabilidad civil. El análisis
de la responsabilidad puede distribuir el R* entre el arquitecto
de la defensa y el atacante externo sin necesidad de identificar
al atacante con certeza Cd1.
Límite 2 — La distinción entre la vulnerabilidad conocida y la
vulnerabilidad desconocida determina el INCF. El análisis
debe verificar si la vulnerabilidad explotada estaba en el
registro público de vulnerabilidades (CVE) antes del ataque: si
sí, el INCF del responsable de la gestión de parches es alto. Si
era un zero-day, el INCF del proveedor de software y del
arquitecto de la defensa por controles de mitigación
alternativos es el instrumento.
Por qué
Error Consecuencia Corrección
ocurre
Concentrar el La narrativa INCF del El INCF del
R* en el pública de la arquitecto de la atacante se
atacante brecha defensa no establece con S:
externo identifica al capturado. El ¿otro atacante con
ignorando el atacante responsable de las mismas
INCF del como el la no aplicación herramientas
arquitecto de causante. del parche habría producido
la defensa evade la el mismo
responsabilidad. resultado? Si sí
(vulnerabilidad

Taxonomía General de Aplicaciones
Por qué
Error Consecuencia Corrección
ocurre
genérica con
parche
disponible), el
INCF del atacante
es bajo relativo.
No distinguir El análisis INCF del El análisis del
entre trata todas responsable CVE y la timeline
vulnerabilidad las brechas sobreestimado del parche es el
conocida y como si el cuando el primer paso del
zero-day para responsable ataque usó un análisis de
establecer el hubiera zero-day responsabilidad
INCF podido desconocido. en ciberseguridad.
prevenir el
ataque.
Ignorar el El análisis D_total El D_afectados
D_a los calcula el D subestimado. incluye: el fraude
afectados de la Los afectados facilitado por los
individuales organización individuales son datos exfiltrados,
en brechas de (multas, el Nf más el tiempo de
datos costos de vulnerable del gestión de las
personales remediación) grafo. consecuencias, y
sin el D a los el daño a la
titulares de trayectoria
los datos. crediticia o
financiera de los
afectados.
§8 Guía de prioridades de evidencia
Incertidum Evidencia Qué
Por qué Qué
bre que más la rango
funciona buscar
principal reduce reduce
1. ¿Existía el Registro La INCF ¿Estaba la
parche — CVE de la existencia del vulnerabilid
cuál es el vulnerabilid del parche y arquitec ad en el
INCF de la ad + fecha la timeline to de la CVE antes
gestión de de de defensa. del ataque?
TI? publicación aplicación ¿Cuándo

Taxonomía General de Aplicaciones
Incertidum Evidencia Qué
Por qué Qué
bre que más la rango
funciona buscar
principal reduce reduce
del parche establecen fue
+ registros el INCF del publicado el
internos de responsabl parche? ¿La
gestión de e de la organizació
parches. gestión de n tenía un
parches. proceso de
gestión de
parches
documenta
do?
2. ¿El S del Análisis El S del S del ¿Cuál era el
responsable comparado responsabl arquitec tiempo
de seguridad de las e determina to de la promedio
era alto o prácticas del si la defensa. de
bajo? sector del reforma aplicación
período debe ser de parches
para el tipo individual o críticos en
de sistémica. el sector del
vulnerabilid período?
ad y ¿La
organizació organizació
n. n estaba por
encima o
por debajo
del
promedio?
3. ¿El Timeline de El INCF INCF ¿Hay
proveedor la del del registros de
de software vulnerabilid proveedor proveed que el
tiene INCF ad: ¿cuándo depende de or de proveedor
positivo? la conoció si tenía software conocía la
el conocimien . vulnerabilid
proveedor? to previo ad antes de
¿Cuándo de la la
publicó el vulnerabili publicación
parche? dad y no la del CVE?
¿Comunicó comunicó. ¿El proceso
el riesgo a de
los divulgación
usuarios? del
proveedor
seguía el

Taxonomía General de Aplicaciones
Incertidum Evidencia Qué
Por qué Qué
bre que más la rango
funciona buscar
principal reduce reduce
estándar del
sector?
— Fin del Capítulo 48 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

