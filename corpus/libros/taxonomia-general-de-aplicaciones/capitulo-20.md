## PARTE II · Ciencias Económicas y Financieras

### Capítulo 20
Criptoeconomía y activos digitales —
protocolos, exchanges y responsabilidad
Organ. Estru. Model. Educa. Crisi.
Para el mediador que busca precisión · Cómo usar este
capítulo
Este capítulo es Nivel C. Sus rangos son candidatos pendientes de calibración
empírica con jurisprudencia de litigios de activos digitales (SEC, CFTC,
Unión Europea, casos nacionales). La aportación central es conceptual: los
mismos principios que en el cap. 17 (plataformas digitales) aplican aquí con
una singularidad nueva — el smart contract ejecuta determinísticamente sin
voluntad propia (S ≈ 1.0 respecto al código desplegado), por lo que R* del
smart contract apunta hacia quien lo diseñó, quien lo auditó y quien lo
desplegó. El arquitecto del tokenomics es el nodo de mayor R* en la cadena
algorítmica del protocolo — análogo al diseñador de la métrica del cap. 17.
Este capítulo opera con cuatro ejes que deben distinguirse antes del análisis.
El primero es la responsabilidad del fundador / arquitecto del protocolo:
diseñó el tokenomics y las reglas del sistema que produjeron el daño. El
segundo es la responsabilidad del exchange centralizado (CEX): custodia
activos, conoce a sus clientes, tiene obligaciones de segregación de fondos. El
tercero es el fraude en la emisión de tokens: captación de capital con
representaciones falsas sobre el protocolo o sus perspectivas. El cuarto es la
explotación de vulnerabilidades en contratos inteligentes: el auditor tenía R*
sobre el exploit que no detectó. Para la prioridad de evidencia, ve a §9.
§1 Descripción del subcampo

Taxonomía General de Aplicaciones
La criptoeconomía introduce en el sistema de imputación
causal dos características que ningún capítulo anterior había
combinado simultáneamente. La primera es la
descentralización del daño: el protocolo de blockchain opera
sin un actor central identificable, los smart contracts se
ejecutan automáticamente sin intervención humana en cada
transacción, y los inversores están dispersos globalmente sin
relación contractual directa con el fundador del protocolo. La
segunda es la paradoja de la transparencia opaca: el código del
protocolo es públicamente visible en la blockchain —
cualquiera puede leerlo — pero la intención, el diseño del
tokenomics y las decisiones de los fundadores son
frecuentemente tan opacas como en cualquier otro dominio.
La combinación de código transparente e intención opaca es
el desafío central del análisis de responsabilidad en el dominio.
El principio estructural del dominio: el smart contract no tiene
voluntad — ejecuta exactamente el código desplegado. S del
smart contract ≈ 1.0 respecto a su comportamiento: cualquier
instancia del mismo código en las mismas condiciones
produce el mismo resultado. Por eso, R* del smart contract
apunta íntegramente hacia los actores humanos que lo
diseñaron (el arquitecto del protocolo), lo auditaron (o no lo
auditaron) y lo desplegaron. El diseñador del tokenomics —
quien decidió los incentivos, la distribución inicial de tokens,
los mecanismos de estabilización y las reglas de gobernanza —
es el nodo de mayor R* en el grafo del protocolo, análogo al
diseñador de la métrica del cap. 17.
El smart contract como nodo sin voluntad: S ≈ 1.0 y la jerarquía
de R* en el protocolo
El smart contract ejecuta determinísticamente. Si el código tiene una
vulnerabilidad de reentrancy y un atacante la explota, el smart contract no
"actuó mal" — ejecutó exactamente su código. R* del smart contract =
R*_vulnerabilidad apunta hacia: (a) el diseñador del protocolo que no
contempló ese vector de ataque en el diseño; (b) el auditor de seguridad que no
detectó la vulnerabilidad antes del despliegue; (c) el equipo que desplegó el
contrato sin las pruebas de seguridad suficientes.
La misma lógica del cap. 17 (el modelo tiene S ≈ 1.0 y su R* apunta al
diseñador de la métrica) aplica aquí: cambiar el smart contract sin cambiar

Taxonomía General de Aplicaciones
el diseño del tokenomics no resuelve el daño si el tokenomics tiene los incentivos
que lo producen. El mecanismo de estabilización del terraUSD que colapsó
en mayo 2022 no era un bug del código — era el diseño del tokenomics que
hacía inevitable el colapso en una espiral de muerte bajo condiciones de estrés
que eran previsibles.
Sub-variantes del dominio
Rug pull (abandono fraudulento del protocolo): los
fundadores de un proyecto de DeFi o NFT captaron capital
de los inversores mediante la venta de tokens con
representaciones sobre el protocolo, y después retiraron la
liquidez del proyecto o simplemente abandonaron el
desarrollo, produciendo pérdida total a los inversores. Es la
forma más directa de Anteros en el dominio: los fundadores
diseñaron el esquema para extraer capital y retirarse. La
distinción entre el rug pull deliberado y el proyecto que fracasó
genuinamente sin malicia es el análisis central.
Colapso de stablecoin algorítmica: el emisor de una stablecoin
algorítmica diseñó un mecanismo de mantenimiento del peg
que era estructuralmente frágil ante espirales de ventas en
condiciones de estrés — el diseño del tokenomics era la
condición del colapso, no una falla técnica del código. El daño
a los tenedores es la diferencia entre el valor prometido (el peg)
y el valor realizado post-colapso. R* del arquitecto del
mecanismo de estabilización es alto; S moderado-bajo cuando
el diseño era idiosincrático.
Quiebra de exchange centralizado (CEX): el exchange que
custodiaba activos de clientes mezcló los fondos de los clientes
con sus activos propios, los usó para operaciones especulativas
no reveladas, o simplemente operó insolvente durante un
período antes del colapso (FTX como caso paradigmático). El
análisis es una compilación directa de los instrumentos del cap.
13 (gobierno corporativo) y del cap. 12 (insolvencia y quiebra)
aplicados al exchange como empresa.

Taxonomía General de Aplicaciones
Manipulación de precio en mercados de activos digitales: el
actor realizó operaciones de wash trading, spoofing o pump-
and-dump sobre activos con mercados de menor liquidez —
aprovechando la escasa supervisión regulatoria del dominio
para usar los mismos mecanismos que en el cap. 14 (finanzas
de mercado), con menor riesgo de detección. El análisis es una
extensión directa de la escala FM con la particularidad de que
los registros de la blockchain son públicos y permanentes.
Fraude en la emisión de tokens (ICO/IEO/IDO): los
emisores de tokens vendieron instrumentos financieros con
representaciones materiales falsas sobre el protocolo, sus
perspectivas o el uso de los fondos captados. La distinción
entre el token que es un valor (security token, sujeto a la
regulación de valores) y el que no lo es (utility token) es el
análisis regulatorio previo que determina qué marco legal
aplica.
Exploit de smart contract por vulnerabilidad de código: un
atacante identificó y explotó una vulnerabilidad en el código
de un protocolo DeFi para drenar sus fondos. El grafo incluye
al atacante (R* directo sobre el daño), al diseñador del
protocolo (R* por el diseño que no contempló el vector de
ataque), al auditor de seguridad (R* por no detectar la
vulnerabilidad) y al equipo que desplegó el contrato sin el nivel
de auditoría requerido por la magnitud del capital expuesto.
§2 Escala de evidencia CD0–CD8 ·
Criptoeconomía y activos digitales
La escala CD0–CD8 traduce la jerarquía general E0–E8 al
vocabulario de la criptoeconomía. Su característica más
relevante y singular respecto a todos los dominios anteriores
es que la blockchain registra públicamente y de manera
permanente todas las transacciones del protocolo — lo que
significa que los datos de la cadena (on-chain data) tienen una
calidad documental sin precedente para establecer qué
transacciones ocurrieron, cuándo y en qué secuencia. Esa
transparencia on-chain contrasta con la opacidad de las

Taxonomía General de Aplicaciones
comunicaciones internas de los fundadores, que con
frecuencia operan de manera pseudónima o anónima. Nivel C
— rangos candidatos pendientes de calibración empírica
formal.
Nota de calibración Nivel C
Los rangos CD0–CD8 son candidatos. La calibración empírica requiere: (a)
análisis de los casos de enforcement de la SEC, la CFTC, la FCA y
equivalentes europeos contra emisores de tokens y exchanges; (b) litigios civiles
contra fundadores de protocolos que colapsaron; (c) jurisprudencia de los casos
de insolvencia de exchanges (FTX, Celsius, Voyager). Antes de usar estos
rangos en una pretensión formal, ajustar con los desarrollos jurisprudenciales
más recientes del dominio.
Descripción y
Tipo de ejemplos en el Rango w
Nivel
evidencia dominio de la (candidato)
criptoeconomía
CD1 Datos on-chain Registros de la [0.72, 0.88]
verificables y blockchain que
documentos establecen las
directos del transacciones
emisor o relevantes con
exchange timestamp, dirección
de origen y destino, y
valor transferido;
código del smart
contract desplegado
públicamente con su
historial de versiones;
whitepaper y
documentos de
emisión del token con
las representaciones
sobre el protocolo y el
uso de fondos;
registros de custodia
del exchange que
establezcan la mezcla
de fondos de clientes
con fondos propios;
comunicaciones
internas del equipo
fundador obtenidas

Taxonomía General de Aplicaciones
Descripción y
Tipo de ejemplos en el Rango w
Nivel
evidencia dominio de la (candidato)
criptoeconomía
mediante discovery o
filtradas.
CD2 Peritaje técnico Análisis forense on- [0.60, 0.80]
de blockchain y chain que reconstruye
análisis forense la cadena causal de las
on-chain, o transacciones
peritaje de relevantes — rastreo
tokenomics de fondos a través de
múltiples carteras,
análisis de los patrones
de transacción que
establecen la
coordinación entre
actores, identificación
de los flujos de capital
entre el protocolo y las
carteras de los
fundadores; análisis
técnico del código del
smart contract que
establece la
vulnerabilidad
explotada y su
detectabilidad previa
al exploit; peritaje del
diseño del tokenomics
que establece si el
mecanismo de
estabilización era
estructuralmente
viable o
inevitablemente frágil
bajo condiciones de
estrés documentadas.
CD3 Testimonios Declaraciones de [0.48, 0.66]
convergentes de inversores,
participantes del desarrolladores o
ecosistema con insiders del protocolo
corroboración que describen
on-chain consistentemente las
decisiones de diseño,
las representaciones

Taxonomía General de Aplicaciones
Descripción y
Tipo de ejemplos en el Rango w
Nivel
evidencia dominio de la (candidato)
criptoeconomía
de los fundadores o la
gestión de fondos del
exchange, con al
menos una
transacción on-chain o
un documento del
proyecto consistente.
Las declaraciones de
colaboradores del
equipo fundador son
CD3 de alto valor
cuando incluyen
detalles verificables
on-chain.
CD4 Análisis Análisis on-chain que [0.38, 0.58]
estadístico del muestra que los
comportamiento patrones de
del protocolo o transacción son
del mercado del estadísticamente
token incompatibles con el
comportamiento de
un mercado sin
manipulación — wash
trading detectado por
transacciones
circulares entre
carteras relacionadas,
pump-and-dump
detectado por la
correlación entre el
patrón de tenencia de
los fundadores y el
movimiento de precio,
selección adversa en el
mecanismo de
estabilización de la
stablecoin.
CD5 Análisis del Comparación del [0.28, 0.48]
diseño del diseño del tokenomics
tokenomics y del descrito en el
whitepaper whitepaper con el
versus el comportamiento real

Taxonomía General de Aplicaciones
Descripción y
Tipo de ejemplos en el Rango w
Nivel
evidencia dominio de la (candidato)
criptoeconomía
comportamiento del protocolo, que
observable establece las
discrepancias entre las
representaciones y la
realidad; análisis de la
distribución inicial de
tokens (allocations)
versus los
compromisos
declarados; análisis de
los mecanismos de
gobernanza en la
práctica versus lo
descrito en el
whitepaper.
CD6 Inferencia El diseño del [0.18, 0.38]
estructural por la protocolo y el
arquitectura del comportamiento del
protocolo y el mercado del token son
comportamiento consistentes con el
del mercado mecanismo de daño
analizado, sin análisis
técnico específico que
establezca la cadena
causal.
CD7 Correlación Las acciones [0.05, 0.22]
temporal entre conocidas de los
acciones de los fundadores (ventas de
fundadores y tokens, cambios en el
movimientos del protocolo) coinciden
precio o del temporalmente con
protocolo los movimientos de
precio o los eventos
dañinos sin análisis
causal.
CD8 Especulación Afirmaciones sobre las [0.00, 0.10]
sobre el intenciones de los
comportamiento fundadores sin datos
de los fundadores verificables on-chain
sin datos on- ni documentación del
proyecto.

Taxonomía General de Aplicaciones
Descripción y
Tipo de ejemplos en el Rango w
Nivel
evidencia dominio de la (candidato)
criptoeconomía
chain ni
documentos
CD0 Ausencia Análisis forense CD2 w = 0.00
documentada de que establece que el
conexión causal daño fue producido
con el daño por factores externos
al protocolo o al
exchange (colapso del
mercado general,
exploit de otro
protocolo que afectó
en cascada), o que el
diseño del tokenomics
era estructuralmente
sólido dado el estado
del conocimiento en el
momento del diseño.
La singularidad de los datos on-chain como evidencia:
transparencia sin interpretación automática
El registro de la blockchain es el más completo y permanente de todos los
dominios del libro. Todas las transacciones son públicas, verificables, con
timestamp y sin posibilidad de alteración retroactiva. Eso hace que CD1 on-
chain sea la evidencia más confiable del dominio para establecer qué
transacciones ocurrieron. Pero la transparencia on-chain no resuelve la
pregunta de la intención: el análisis forense on-chain establece qué pasó, no por
qué. La intención de los fundadores — la distinción entre rug pull deliberado
y proyecto fallido sin malicia — requiere evidencia off-chain (comunicaciones,
documentos del proyecto, whitepaper) para establecer lo que la blockchain no
registra.
§3 Firmas documentales por Hijo e
información para S del fundador y del operador
del exchange

Taxonomía General de Aplicaciones
Los Hijos de Afrodita aplican a los actores humanos
identificables en el dominio: el fundador / arquitecto del
protocolo, el CEO y los directivos del exchange centralizado,
el auditor de seguridad que emitió el informe previo al exploit.
No aplican al smart contract (nodo sin voluntad), ni al
protocolo de blockchain como sistema descentralizado.
La distinción más crítica del dominio es entre el fundador que
diseñó el esquema desde el inicio con intención de captar
capital y retirarse (Anteros dominante, rug pull deliberado, S
muy bajo) y el fundador que diseñó un protocolo que
genuinamente creía viable y que fracasó por razones de
mercado o por un diseño deficiente que no anticipó (Potós /
Deimos, proyecto fallido sin malicia, S más alto). Esa
distinción determina si el proceso es penal o civil. El análisis
forense on-chain establece los hechos; el análisis de los Hijos
desde las comunicaciones y el whitepaper establece la
intención.
§3.1 Hijos de legibilidad alta en el dominio de la
criptoeconomía
Qué
informa
para S del Firma en el Error de
Fuente
fundador expediente discrimina
Hijo documenta
/ on-chain y ción
l típica
operador off-chain frecuente
del
exchange
Anter S muy Patrones de Análisis Confundir
os bajo [0.03, venta on- forense on- con
0.22]. El chain de chain de los Potós/Dei
fundador tokens de flujos de mos cuando
diseñó el los fondos de el proyecto
protocolo fundadores los fracasó por
o el coincidentes fundadores. condiciones
exchange con Comunicaci de mercado
como un campañas de ones adversas sin
esquema marketing filtradas o que los

Taxonomía General de Aplicaciones
Qué
informa
para S del Firma en el Error de
Fuente
fundador expediente discrimina
Hijo documenta
/ on-chain y ción
l típica
operador off-chain frecuente
del
exchange
para dirigidas a discovery. fundadores
captar inversores Auditoría se
capital de externos. forense del enriqueciera
inversores Transferenci exchange. n a expensas
con as de fondos Comparació de los
intención del n del inversores.
de protocolo a whitepaper La pregunta
retirarse carteras con el discriminant
con los controladas comportami e: ¿los
fondos o por los ento real del fundadores
de operar fundadores protocolo. vendieron
de manera inmediatam sus tokens
que ente antes antes del
enriquece del colapso colapso en
a los (exit scam). un patrón
insiders a Comunicaci que sugiere
expensas ones conocimient
de los privadas o previo, o
inversores donde los perdieron
externos. fundadores ellos
La discuten la también?
conducta estrategia de
fue extracción
genuinam de valor.
ente Mezcla de
idiosincrát fondos de
ica: el clientes con
diseño fondos
específico propios del
del exchange
mecanism para
o de operaciones
extracción especulativa
, el timing s no
de las reveladas.
ventas de
tokens de
los
insiders
antes del

Taxonomía General de Aplicaciones
Qué
informa
para S del Firma en el Error de
Fuente
fundador expediente discrimina
Hijo documenta
/ on-chain y ción
l típica
operador off-chain frecuente
del
exchange
colapso, la
arquitectu
ra de las
carteras
que
recibieron
los
fondos, no
son los de
un equipo
que
genuinam
ente creyó
en el
proyecto.
Potós S Diseño del Whitepapers Confundir
moderado tokenomics de proyectos con Anteros
-alto [0.40, que replica comparables cuando el
0.70]. El el estándar del período. equipo
fundador del sector en Estándares vendió sus
replicó el ese período. del sector en tokens antes
modelo de Whitepapers el diseño de del colapso
proyecto con tokenomics. de manera
de cripto representaci Cultura del que sugiere
estándar ones ecosistema conocimient
del comparables cripto en el o previo del
período a otros período fracaso
— proyectos analizado. inminente.
whitepape del sector El timing de
r con que también las ventas
promesas fracasaron. on-chain de
ambiciosa Mecanismos los insiders
s, de es el
tokenomic rendimiento instrumento
s con alta (APY) que que
proporció eran discrimina
n de comparables Anteros de
tokens con otros Potós en los
para el protocolos casos límite.

Taxonomía General de Aplicaciones
Qué
informa
para S del Firma en el Error de
Fuente
fundador expediente discrimina
Hijo documenta
/ on-chain y ción
l típica
operador off-chain frecuente
del
exchange
equipo de DeFi del
fundador, período.
mecanism
os de
staking
con
rendimien
tos
insostenib
les — sin
cuestionar
si el
modelo
era viable
a largo
plazo o
éticament
e
sostenible.
Cualquier
equipo
fundador
con la
misma
cultura del
ecosistem
a de cripto
en ese
período
habría
diseñado
un
proyecto
similar.
Fobo S Comunicaci Comunicaci Confundir
s moderado ones que ones del con Anteros
-alto [0.52, documentan equipo cuando el
0.78]. El la presión fundador. fundador
fundador sobre el Análisis de diseñó

Taxonomía General de Aplicaciones
Qué
informa
para S del Firma en el Error de
Fuente
fundador expediente discrimina
Hijo documenta
/ on-chain y ción
l típica
operador off-chain frecuente
del
exchange
o el equipo los específicam
operador fundador rendimiento ente el
del para s del sector esquema
exchange mantener en el para
tomó rendimiento período. beneficiarse
decisiones s Evidencia de de la presión
que sabía competitivo la presión de del mercado
que eran s con otros los a expensas
problemát protocolos. inversores de los
icas bajo la Evidencia de institucional inversores
presión que el es o de los finales.
del equipo sabía validadores
entorno que los de
— la rendimiento gobernanza.
presión s eran
competitiv insostenible
a de otros s, pero los
protocolo mantuvo
s con para no
rendimien perder
tos aún competitivid
más altos, ad. Análisis
la presión de la
de los dinámica del
inversores sector en el
para período.
mostrar
crecimient
o, la
presión de
la carrera
hacia el
TVL (total
value
locked)
como
métrica de
éxito del
sector. La
presión

Taxonomía General de Aplicaciones
Qué
informa
para S del Firma en el Error de
Fuente
fundador expediente discrimina
Hijo documenta
/ on-chain y ción
l típica
operador off-chain frecuente
del
exchange
del
ecosistem
a en ese
período
era
condición
de las
decisiones
dañinas.
§3.2 Hijos de legibilidad baja en el dominio cripto
Deimos: puede aparecer en fundadores que genuinamente no
comprendieron los riesgos estructurales de su diseño de
tokenomics — el equipo que diseñó el mecanismo de
estabilización del terraUSD creyendo que la tensión entre
LUNA y UST era un mecanismo robusto sin anticipar las
condiciones de espiral de muerte que se materializaron. S alto
cuando el conocimiento de las fragilidades de los mecanismos
de estabilización algorítmica no estaba consolidado en la
literatura al momento del diseño. Asignar con nota de
incertidumbre alta dado el estado del conocimiento del
ecosistema DeFi en el período analizado.
Harmonía en el dominio cripto: el equipo fundador que
implementó los estándares de seguridad más rigurosos
disponibles (auditorías múltiples, bug bounties, tiempo de lock
de los tokens del equipo), publicó transparentemente la
arquitectura del protocolo incluyendo sus riesgos, y actuó de
buena fe ante el fracaso para minimizar el daño a los inversores
(reembolso parcial, transparencia sobre las causas del colapso).
Es la referencia normativa del equipo fundador diligente en el
ecosistema.

Taxonomía General de Aplicaciones
§3.3 El smart contract no tiene Hijo — la jerarquía de R*
en el protocolo
Principio derivado del cap. 17 (plataformas digitales): el smart contract ejecuta
determinísticamente. S ≈ 1.0 respecto a su comportamiento en las condiciones
del código desplegado. Su R* apunta íntegramente hacia los actores humanos
que lo diseñaron, auditaron y desplegaron. La jerarquía en el protocolo DeFi:
R*_arquitecto_tokenomics > R*_auditor_seguridad > R*_deployer >
R*_smart_contract. Cambiar el smart contract sin cambiar el diseño del
tokenomics no resuelve el daño si el tokenomics tiene los incentivos que lo
producen — análogo a cambiar el modelo sin cambiar la métrica en el cap.
17.
§4 ¿Qué cuenta como asunción (α) en el
dominio de la criptoeconomía?
α en el dominio cripto mide lo que el fundador, el operador
del exchange o el auditor de seguridad han hecho
concretamente sobre su posición causal: restitución a los
inversores proporcional a su AD_i = R*_i × D_total,
cooperación activa con reguladores e investigadores,
implementación de los estándares de seguridad y transparencia
que su posición requería antes del daño, reforma del protocolo
cuando el diseño fallido fue identificado.
α del fundador es completamente independiente del dolo en el
dominio cripto
Un fundador que diseñó deliberadamente el rug pull puede tener α alto si
después cooperó plenamente con el regulador, permitió la recuperación de
fondos y restituyó a los inversores. Un fundador que genuinamente creyó en el
proyecto y fracasó puede tener α = 0 si nunca fue transparente sobre las causas
del fracaso ni cooperó con los investigadores. Los Hijos informan S del
fundador; α mide lo que hizo después sobre su posición causal.

Taxonomía General de Aplicaciones
Acción del ¿Cuenta
Razón Tipo de α
actor para α?
Restitución a los Sí — α Asunción Voluntario
inversores económico económica de la o forzado
proporcional al directo posición causal.
AD_i del actor, La
usando fondos proporcionalidad
propios al AD_i establece
si es completa o
parcial.
Cooperación Sí — α de La cooperación Voluntario
activa con el cooperación permite
regulador — reconstruir el
información grafo completo
completa sobre del esquema. Su
el protocolo, los valor es mayor
flujos de fondos que el pago
y las decisiones proporcional
de diseño cuando permite
identificar a otros
nodos.
Implementación Sí — α Las auditorías de Voluntario
de auditorías de estructural seguridad son el α
seguridad preventivo más directo para
múltiples antes el exploit de smart
del despliegue contract: reducen
del smart el R* del auditor y
contract, del deployer.
proporcionales al
capital expuesto
Lock de los Sí — α de El lock on-chain Voluntario
tokens del alineación verificable alinea
equipo fundador de los incentivos del
con vesting de incentivos fundador con los
largo plazo y cliff del inversor. Sin
period lock, el fundador
documentados puede vender en
on-chain cualquier
momento sin
señal previa.
Bug bounty Sí — α de El bug bounty Voluntario
activo con prevención incentiva la
recompensas de exploit detección
proporcionales al proactiva de

Taxonomía General de Aplicaciones
Acción del ¿Cuenta
Razón Tipo de α
actor para α?
capital expuesto vulnerabilidades
del protocolo antes de que sean
explotadas.
El exchange Sí — α La segregación Voluntario
separó estructural efectiva de fondos
efectivamente los del con proof of
fondos de los exchange reserves
clientes de los verificable reduce
fondos propios el R* del exchange
con verificación en el daño a los
de reservas clientes.
proofable on-
chain
Anuncio de No — hasta La promesa no —
"compensación que se ejecutada no es α.
total" sin ejecuta la Es comunicación
mecanismo distribución sin consecuencia
verificable de verificable sobre la posición
distribución causal.
La escala de α en el dominio cripto
Indicadores on-
Rango Descripción
Nivel chain y off-
α observable
chain
Extracción 0.00 – Los fundadores Transferencias
activa / exit 0.03 retiraron on-chain de los
scam activamente los fondos del
fondos del protocolo a
protocolo o del carteras no
exchange hacia relacionadas con
carteras propias y el proyecto.
desaparecieron. Abandono de los
canales de
comunicación.
Sin cooperación
con el regulador.

Taxonomía General de Aplicaciones
Indicadores on-
Rango Descripción
Nivel chain y off-
α observable
chain
Abandono 0.04 – El proyecto Sin restitución
pasivo / 0.15 colapsó y los documentada.
opacidad fundadores no Sin cooperación
han cooperado ni con el regulador.
restituido. Comunicaciones
Comunicaciones evasivas sobre los
mínimas sobre fondos.
las causas del
colapso.
Reconocimiento 0.16 – El fundador Comunicados
nominal 0.28 reconoció el públicos de
fracaso reconocimiento.
públicamente Sin restitución
pero sin verificable.
restitución ni Cooperación
cooperación parcial o evasiva.
sustancial.
Asunción 0.29 – Restitución Restitución
parcial 0.50 parcial a los documentada
inversores, menor al AD_i.
cooperación Cooperación con
limitada con el algunos aspectos
regulador o de la
transparencia investigación.
sobre las causas Publicación de
del fracaso. análisis post-
mortem.
Asunción activa 0.51 – Restitución Restitución del
0.75 sustancial en 50–70% del
proceso, AD_i.
cooperación Cooperación
activa con el documentada por
regulador, el regulador.
implementación Proof of reserves
de los activo para el
mecanismos de exchange.
seguridad Auditorías
requeridos en el múltiples del
nuevo protocolo. nuevo protocolo.
Asunción 0.76 – Restitución Restitución del
funcional 0.92 proporcional a la 75–90% del

Taxonomía General de Aplicaciones
Indicadores on-
Rango Descripción
Nivel chain y off-
α observable
chain
mayor parte del AD_i.
AD_i, Cooperación
cooperación plena
plena con el documentada.
regulador, Proof of reserves
reforma del con auditoría
protocolo o del independiente.
exchange Vesting de tokens
verificable. del equipo on-
chain.
Asunción plena 0.93 – Restitución Restitución
1.00 integral, integral.
cooperación que Cooperación que
permitió identificó a todos
establecer el los actores del
grafo completo, esquema. Proof
implementación of reserves
de todos los verificable.
estándares de Auditorías de
seguridad y seguridad
transparencia. públicas del
protocolo
reformado.
§5 Construcción del grafo típico del dominio
La jerarquía del grafo cripto: R*_arquitecto_tokenomics >
R*_auditor_seguridad > R*_deployer >
R*_smart_contract
Esta jerarquía es el principio más importante del capítulo y su
derivación directa del cap. 17. El smart contract (el nodo más
técnicamente analizable) tiene el R* más bajo porque S ≈ 1.0:
cualquier instancia del mismo código en las mismas
condiciones produce el mismo comportamiento. El arquitecto
del tokenomics (el menos visible en el código) tiene el R* más
alto porque sus decisiones sobre qué incentivos construir en

Taxonomía General de Aplicaciones
el protocolo son la causa raíz de los daños predecibles del
sistema.
Tipo de Función en el Ejemplo en el
S típico
nodo grafo dominio
Arquitecto El fundador o el Variable El equipo de
del equipo que tomó [0.10 – Terraform Labs
tokenomics las decisiones 0.55] que diseñó el
(AT) normativas de mecanismo
diseño del LUNA/UST
protocolo — qué con la tensión
incentivos entre el token
construir, cómo de gobernanza y
distribuir los tokens la stablecoin. El
inicialmente, qué fundador de un
mecanismo de protocol DeFi
estabilización que reservó el
implementar, 30% de los
cuánto del tokens para el
suministro reservar equipo con
para el equipo vesting de 6
fundador. Es el meses. El CEO
nodo de mayor R* del exchange
del grafo del que decidió usar
protocolo. Sus los fondos de
Hijos informan S. los clientes para
Anteros: diseñó el operaciones
esquema para especulativas.
extraer valor.
Potós: replicó el
modelo estándar
sin cuestionar su
viabilidad. Deimos:
no comprendió las
fragilidades del
diseño.
Auditor de La firma que auditó Moderado La firma de
seguridad el smart contract [0.30 – auditoría que
(AS) antes del 0.65] revisó el código
despliegue. R* del protocolo
positivo cuando su DeFi que fue
proceso de explotado
auditoría no mediante
detectó la reentrancy
vulnerabilidad que attack — un

Taxonomía General de Aplicaciones
Tipo de Función en el Ejemplo en el
S típico
nodo grafo dominio
fue explotada y vector
cuando el estándar documentado
de la industria en en la literatura
ese momento hacía desde el hack
esa detección del DAO en
razonablemente 2016. El auditor
esperable. S del que emitió
auditor es certificación de
moderado cuando seguridad sin
el vector de ataque incluir pruebas
estaba de fuzzing o
documentado en la análisis formal
literatura de del mecanismo
seguridad de smart de
contracts y otros estabilización.
auditores lo habrían
detectado.
Operador El CEO y los Variable El CEO de
del directivos del [0.10 – FTX que
exchange exchange que 0.55] para mezcló fondos
centralizad tomaron las directivos de clientes con
o (OE) decisiones de individuale fondos del
custodia, de s hedge fund
segregación de afiliado. El
fondos y de directivo de
gobernanza del Celsius que
exchange. Su continuó
análisis sigue los pagando
instrumentos del rendimientos
cap. 13 (gobierno altos a los
corporativo) — los inversores
Hijos aplican a los mientras el
directivos protocolo
individuales, no al acumulaba
exchange como pérdidas
entidad. El ocultas. El
exchange como COO de
entidad tiene R* Voyager que no
sobre el daño a los implementó la
clientes segregación de
proporcional a fondos
cuánto las requerida por
decisiones de su las licencias
gobierno estatales.
corporativo fueron

Taxonomía General de Aplicaciones
Tipo de Función en el Ejemplo en el
S típico
nodo grafo dominio
la condición del
daño.
Deployer El equipo o la Moderado- El equipo que
del smart persona que alto [0.40 – desplegó el
contract desplegó el 0.72] contrato del
(DE) contrato en la cuando protocolo DeFi
blockchain. R* desplegó con $500M en
positivo cuando sin liquidez después
desplegó sin el nivel auditoría de solo una
de auditoría suficiente auditoría de
proporcionado al firmas con track
capital expuesto, o record limitado.
cuando desplegó El equipo que
sabiendo que había ignoró los
vulnerabilidades hallazgos de la
identificadas que auditoría interna
no se habían para cumplir el
resuelto. deadline de
lanzamiento.
Smart El código del ≈ 1.00 El contrato de
contract protocolo Euler Finance
(SC) desplegado en la explotado por
blockchain. Nodo $197M en 2023.
sin voluntad con S El contrato de
≈ 1.0. R* residual Ronin Bridge
apunta al arquitecto explotado por
del tokenomics y al $625M en 2022.
deployer. El contrato del
Transparente on- DAO explotado
chain — cualquiera por $60M en
puede leer su 2016. En todos
código — pero los casos, el
ejecuta smart contract
determinísticament ejecutó su
e sin posibilidad de código — el
"actuar mal". Los problema estaba
exploits no son el en el diseño o
smart contract en la auditoría,
actuando no en el
inesperadamente: comportamient
son el smart o del contrato.
contract ejecutando
exactamente su
código en

Taxonomía General de Aplicaciones
Tipo de Función en el Ejemplo en el
S típico
nodo grafo dominio
condiciones que el
diseñador no
contempló.
Atacante El actor que Variable El atacante que
(ATK) identificó y explotó [0.15 – ejecutó el
la vulnerabilidad. 0.60] exploit del
R* positivo sobre el DAO en 2016
daño directo. S usando
moderado-bajo reentrancy —
cuando el exploit un vector que
requería un nivel de otros actores en
sofisticación la comunidad ya
técnica habían señalado
idiosincrática y no como riesgo
habría sido antes del ataque.
encontrado por El grupo de
cualquier actor con atacantes que
acceso al código — explotó la clave
S bajo cuando el privada del
vector de ataque validator de
era conocido y Ronin Bridge.
documentado en la
literatura de
seguridad.
Configuraciones canónicas del grafo de criptoeconomía
Configuración 1 — Rug pull deliberado (Anteros dominante del
fundador)
AT (fundador con Anteros: diseñó el esquema para captar capital y retirarse,
S muy bajo) → SC (smart contract que ejecuta el mecanismo de extracción,
S ≈ 1.0) → Inversores (Nf)
Los patrones on-chain del rug pull: (a) ventas masivas de tokens del equipo
fundador en el período previo al abandono; (b) transferencias de los fondos del
protocolo a carteras externas no identificadas; (c) abandono de los canales de
comunicación del proyecto. AD_fundador = R*_fundador × D_total.
D_total = capital captado en la emisión − valor residual del token post-
colapso.

Taxonomía General de Aplicaciones
Configuración 2 — Colapso de stablecoin algorítmica (diseño del
tokenomics frágil)
AT (arquitecto del mecanismo de estabilización: S moderado-bajo si el diseño
era idiosincrático y frágil bajo condiciones de estrés previsibles) + AS (auditor
de seguridad que no auditó el mecanismo de estabilización, solo el código) →
SC (smart contract que ejecuta el mecanismo de quema/emisión) →
Tenedores del stablecoin (Nf)
D_stablecoin = N_tenedores × (valor_nominal_del_peg −
valor_realizado_post_colapso). El análisis del arquitecto del tokenomics
establece si el mecanismo de estabilización era estructuralmente viable o si la
espiral de muerte era previsible bajo condiciones de estrés. Si otros actores del
ecosistema habían señalado públicamente la fragilidad del mecanismo antes
del colapso, la S del arquitecto disminuye (la fragilidad era detectable con los
instrumentos disponibles).
Configuración 3 — Quiebra del exchange con mezcla de fondos
de clientes
OE (directivos del exchange: análisis del cap. 13 gobierno corporativo —
Anteros si la mezcla de fondos fue deliberada, Deimos si los directivos no
tenían visibilidad de la insolvencia) + SC_exchange (sistemas de custodia del
exchange, nodo sin voluntad) → Clientes del exchange (Nf)
Este análisis es una compilación directa del cap. 12 (insolvencia y quiebra)
aplicado al exchange. La distinción central: ¿cuándo cruzó el exchange la
zona de insolvencia? ¿Qué decisiones tomaron los directivos en esa zona? ¿Los
fondos de los clientes estaban segregados o mezclados con los fondos propios?
El análisis forense on-chain establece los flujos de fondos. El análisis de
gobierno corporativo establece las responsabilidades individuales de los
directivos.
Configuración 4 — Exploit de smart contract por vulnerabilidad
no auditada
ATK (atacante: R* directo sobre el exploit, S variable según sofisticación
requerida) + AT (diseñador del protocolo que no contempló el vector de
ataque: R* por el diseño) + AS (auditor que no detectó la vulnerabilidad:
R* proporcional a la detectabilidad del vector con los estándares de auditoría
disponibles) → Proveedores de liquidez / usuarios del protocolo (Nf)

Taxonomía General de Aplicaciones
El análisis del auditor es el instrumento más técnico del capítulo: S del auditor
depende de si el vector de ataque estaba documentado en la literatura de
seguridad de smart contracts al momento de la auditoría. Para los vectores
clásicos (reentrancy, integer overflow, flash loan attacks en protocolos con
ciertos patrones), S del auditor es moderado-bajo — eran previsibles y
detectables con los instrumentos de auditoría estándar. Para vectores
novedosos, S es más alto y R* del auditor es menor.
§6 Preguntas que responde este capítulo
Nota de calibración: respuestas Nivel C. Ajustar con la jurisprudencia
más reciente de los reguladores de valores y de los tribunales en casos de
activos digitales.
Nivel de
Pregunta del
Instrumento que la responde certeza
caso
posible
¿El colapso del Análisis forense on-chain CD2 del Declaración
protocolo fue patrón de ventas de tokens de los B con
un rug pull fundadores antes del colapso + CD1/CD2
deliberado análisis off-chain CD1/CD3 de las de calidad.
(Anteros) o un comunicaciones del equipo + Declaración
proyecto análisis del diseño del tokenomics C si el
fallido sin versus las representaciones del patrón on-
malicia whitepaper. chain es
(Potós/Deimo ambiguo
s)? entre ventas
de insiders
con
información
privilegiada
y ventas de
mercado
normales.
¿El mecanismo Peritaje técnico del tokenomics Declaración
de CD2: análisis del mecanismo de B con
estabilización estabilización bajo distintos peritaje CD2
del stablecoin escenarios de estrés (reducción del de calidad.
era capital, caída del precio del token El
estructuralmen de gobernanza, espirales de contrafáctic
te viable o ventas). Comparación con la o del
inevitablement literatura de estabilidad de mecanismo

Taxonomía General de Aplicaciones
Nivel de
Pregunta del
Instrumento que la responde certeza
caso
posible
e frágil bajo mecanismos algorítmicos bajo
condiciones de disponible al momento del diseño. condiciones
estrés de estrés
previsibles? tiene
incertidumb
re y debe
presentarse
con análisis
de
sensibilidad.
¿El exchange Análisis forense on-chain Declaración
mezcló fondos CD1/CD2 de los flujos de fondos A o B si hay
de clientes con entre las carteras del exchange y las análisis
fondos propios carteras de entidades relacionadas. forense on-
— hay Auditoría de la segregación de chain
insolvencia de fondos y del proof of reserves completo de
custodia? declarado versus el real. los flujos de
fondos. La
trazabilidad
on-chain es
el
instrumento
más
poderoso
del dominio
para este
análisis.
¿El exploit de Análisis técnico CD2 de la Declaración
smart contract vulnerabilidad explotada: ¿estaba B con
era previsible documentada en la literatura de peritaje
dado el estado seguridad de smart contracts al técnico CD2
de la auditoría momento de la auditoría? ¿Los de alta
de seguridad al auditores del estándar de la calidad. La
momento del industria la habrían detectado con detectabilida
despliegue? los procesos disponibles? d de la
vulnerabilida
d con los
instrumento
s disponibles
al momento
de la
auditoría es
la pregunta

Taxonomía General de Aplicaciones
Nivel de
Pregunta del
Instrumento que la responde certeza
caso
posible
técnica
central.
¿El token El análisis jurídico del test de Declaración
emitido es un Howey (EE.UU.) o los A o B si el
security — equivalentes en otras análisis
sujeto a la jurisdicciones: ¿es una inversión de jurídico del
regulación de capital en un esfuerzo común con instrumento
valores expectativa de beneficio derivada está
aplicable? del trabajo de otros? Este análisis establecido
es previo a cualquier análisis de por el
responsabilidad y determina el regulador.
marco regulatorio aplicable. Declaración
C si el
carácter del
token como
security está
disputado en
la
jurisdicción
aplicable.
¿Cuál es el D_total = Declaración
D_total del capital_captado_en_la_emisión − B para el
esquema y el valor_residual_del_token_post_co D_total
AD_i de cada lapso (para rug pulls y emisiones cuando los
nodo del fraudulentas). D_total = datos on-
grafo? capital_de_clientes_no_recuperad chain
o (para insolvencia de exchange). permiten
D_total = cuantificar
valor_drenado_del_protocolo los flujos.
(para exploits). AD_i = R*_i × Declaración
D_total para cada nodo del grafo. C para la
distribución
del AD_i
entre los
nodos
cuando los
R* requieren
estimación
con alta
incertidumb
re.

Taxonomía General de Aplicaciones
§7 Traducción de D_total al dominio de la
criptoeconomía
En el
dominio
Compon Fuente de
de la Cómo se cuantifica
ente evidencia
criptoecon
omía
T_inverti El capital D_capital = Análisis
do de los valor_USD_enviado − forense on-
(pérdida inversores valor_residual_post_col chain CD2
directa perdido en apso. Calculable de los
verificable el esquema, directamente desde el flujos de
on-chain) cuantificabl análisis forense on-chain fondos.
e on-chain usando los precios del Precios
con activo en cada momento históricos
precisión: el relevante (datos de del activo
valor en exchange públicos). en
USD o en el plataforma
activo de s de datos
referencia de mercado
del capital (CoinGeck
enviado al o,
protocolo o CoinMarke
al tCap, datos
exchange, de
menos el exchange).
valor
recuperado
o el valor
residual del
token.
T_impedi La D_oportunidad = Datos
do apreciación (rendimiento_alternativa históricos
(oportuni que el _referencia − de
dades capital rendimiento_token) × rendimient
perdidas perdido capital_invertido × o de
durante el habría período. La alternativa alternativas
período producido de referencia (stablecoin de
del en en depósito, activo de referencia.
esquema) alternativas menor riesgo) debe Análisis del
de justificarse en el peritaje. período en
inversión que el
comparable inversor
s durante el mantuvo su
período del posición

Taxonomía General de Aplicaciones
En el
dominio
Compon Fuente de
de la Cómo se cuantifica
ente evidencia
criptoecon
omía
esquema. por las
Para los representac
inversores iones del
que emisor.
mantuviero
n el token
bajo
representac
iones falsas
de
estabilidad:
el
diferencial
de
rendimient
o entre el
token y la
alternativa
de menor
riesgo
disponible.
ΔT_trayec El daño a la Análisis de los efectos Datos de
toria confianza del colapso sobre el mercado
(impacto en los volumen de mercado, la post-
permanen mercados participación de colapso.
te en la de activos inversores Estudios
confianza digitales institucionales y el costo del sector
del producido de capital de proyectos sobre el
mercado) por el del sector en el período impacto de
esquema — posterior. Siempre eventos de
reducción Declaración C. confianza
de la en los
participació mercados
n de de activos
inversores digitales.
en el
ecosistema,
mayores
costos de
capital para
proyectos
legítimos,

Taxonomía General de Aplicaciones
En el
dominio
Compon Fuente de
de la Cómo se cuantifica
ente evidencia
criptoecon
omía
aumento de
la fricción
regulatoria
para todo el
sector. Es el
component
e más difícil
de
cuantificar
y siempre
Declaració
n C.
D_vital_cripto = D_total / w_ref · La transparencia on-chain
como fundamento de la cuantificación
La transparencia on-chain hace que T_invertido en la criptoeconomía sea el
componente mejor documentado de todos los dominios del libro cuando el
análisis forense está disponible. Cada transacción tiene un timestamp, un
valor y una dirección de origen y destino verificables y permanentes. El
D_total de un exploit, un rug pull o una insolvencia de exchange puede
calcularse con una precisión que pocos otros dominios alcanzan — no porque
la criptoeconomía sea más transparente en sus intenciones, sino porque la
blockchain hace públicos e irrevocables los registros de los movimientos de
capital.
La conversión D_vital = D_total / w_ref en este dominio tiene una
particularidad: los inversores en activos digitales tienen perfiles de ingreso muy
heterogéneos. Algunos son institucionales con alto nivel de sofisticación; otros
son inversores minoristas que asignaron ahorros significativos a sus posiciones.
El análisis debe distinguir el D_vital de los inversores minoristas (que puede
representar una fracción significativa de su patrimonio y de sus horas de vida
de trabajo) del D_vital de los inversores institucionales (que puede ser una
fracción menor de un portafolio diversificado).
§8 Límites del método y errores frecuentes de
aplicación

Taxonomía General de Aplicaciones
Nota especial: el dominio más incierto del libro en
términos regulatorios
La criptoeconomía es el dominio donde el marco regulatorio aplicable es más
incierto, más variado entre jurisdicciones y más cambiante en el tiempo. El
análisis causal de la responsabilidad puede establecer quién tiene R* sobre el
daño con relativa precisión usando los datos on-chain y off-chain disponibles.
Pero la determinación de si ese R* se traduce en responsabilidad jurídica bajo
la ley aplicable depende de qué marco regulatorio aplica (ley de valores, ley de
servicios financieros, ley de commodities, regulación específica de activos
digitales) y eso varía significativamente entre jurisdicciones. El analista debe
ser especialmente explícito sobre esta incertidumbre jurisdiccional al usar este
capítulo en una pretensión formal.
Límites del método en el dominio de la criptoeconomía
Límite 1 — La pseudonimidad de los actores. La blockchain
registra públicamente las transacciones de las carteras, pero la
identidad de los titulares de las carteras no siempre es
verificable. El análisis forense on-chain puede rastrear los
flujos de fondos con alta precisión, pero la vinculación de las
carteras on-chain con identidades reales requiere KYC del
exchange que custodió la cartera, cooperación de exchanges
con los investigadores o análisis de cluster de carteras. Sin esa
vinculación, el grafo causal puede estar incompleto en la
identidad de los actores.
Límite 2 — La distinción entre proyecto fallido y fraude. La
frontera entre el equipo fundador que diseñó un proyecto
genuinamente pero que fracasó por razones de mercado y el
equipo que diseñó un esquema de captación fraudulenta es
difícil de establecer retrospectivamente cuando los fundadores
no se enriquecieron deliberadamente a expensas de los
inversores. El análisis del patrón de ventas de tokens de los
insiders on-chain es el instrumento más robusto para esta
distinción, pero tiene limitaciones cuando los fundadores
también perdieron significativamente en el colapso.
Límite 3 — La velocidad de evolución del dominio. Los
protocolos, los mecanismos de ataque y los estándares de

Taxonomía General de Aplicaciones
seguridad en el ecosistema de activos digitales evolucionan
rápidamente. El análisis de la detectabilidad de una
vulnerabilidad de smart contract al momento de la auditoría
debe ser especialmente preciso sobre qué instrumentos de
auditoría estaban disponibles y cuáles eran los estándares de la
industria en ese momento específico — no los del momento
del análisis.
Límite 4 — La jurisdicción aplicable y la fragmentación
regulatoria. El dominio es el más fragmentado del libro en
términos de regulación aplicable. Un protocolo puede ser
operado desde una jurisdicción, los inversores pueden estar en
múltiples países, el smart contract está en una blockchain sin
jurisdicción territorial. La determinación de qué ley aplica y
qué regulador tiene jurisdicción es frecuentemente la pregunta
más difícil del análisis, anterior al análisis de responsabilidad
causal.
Errores frecuentes de aplicación
Por qué Consec
Error Corrección
ocurre uencia
Atribuir El smart R* del El smart contract tiene S ≈ 1.0 —
el daño contract arquitec cualquier instancia del mismo
del ejecutó to del código en las mismas condiciones
exploit su tokeno habría producido el mismo
al smart código mics y exploit. R* del smart contract
contract — el del apunta al diseñador del protocolo
como exploit auditor y al auditor. La reforma correcta:
"fallo es visible = 0 diseño más robusto y auditorías
técnico" como "el aunque múltiples con los vectores de
sin smart el ataque documentados.
incluir contract diseño
al fue del
diseñad hackead protocol
or del o". o y el
protoco proceso
lo y al de
auditor auditorí
a fueron

Taxonomía General de Aplicaciones
Por qué Consec
Error Corrección
ocurre uencia
las
condicio
nes del
exploit.
Usar el El D_total D_total por inversor =
precio D_total sobreest valor_en_moneda_de_referencia
pico del es más imado. _al_momento_de_la_compra −
token llamativ El valor_recuperado_al_momento_
como o usando inversor de_la_salida. El D_total del
base del el precio que esquema no es la capitalización
D_total máximo compró de mercado en el pico: es el
en lugar del el token capital real de los inversores
del token, a $0.01 y perdido.
precio que lo
de puede vendió a
compra estar $0.005
del muy por no tiene
inversor encima el
del mismo
precio D_total
de que el
compra que
del compró
inversor. a $1.
Tratar El Culpabil El análisis del patrón de ventas de
el analista idad tokens de los fundadores on-
proyect concluye sobreest chain antes del colapso es el
o fallido fraude imada instrumento central para esta
como porque del distinción: ¿los fundadores
equivale el fundado vendieron sus tokens antes de
nte al proyecto r. El que el proyecto colapsara en un
rug pull fracasó y proceso patrón que sugiere conocimiento
sin los penal previo, o perdieron ellos
analizar inversor puede también? Si los fundadores
el es no también perdieron, el proyecto
patrón perdiero prosper fallido tiene un perfil distinto al
de n, sin ar si la del rug pull.
ventas analizar evidenci
de los si los a del
insiders fundado enriquec
res se imiento
enriquec delibera
ieron do no
delibera está

Taxonomía General de Aplicaciones
Por qué Consec
Error Corrección
ocurre uencia
damente estableci
. da.
Ignorar El R* del S del auditor es moderado-bajo
la análisis auditor cuando el vector de ataque estaba
respons identific = 0 documentado en la literatura de
abilidad a al aunque seguridad de smart contracts al
del atacante emitió momento de la auditoría. El
auditor y al una auditor tiene R* sobre el daño del
de equipo certifica exploit proporcional a la
segurida fundado ción de detectabilidad de la
d r como segurida vulnerabilidad y a la escala del
cuando responsa d para capital que su certificación
el bles sin un permitió exponer.
exploit incluir al contrato
usó un auditor con una
vector que vulnera
docume emitió el bilidad
ntado informe detectab
en la de le con
literatur segurida los
a d previo estándar
al es
exploit. disponi
bles.
§9 Guía de prioridades de recolección de
evidencia
Nota de uso obligatoria: todas las estimaciones de este capítulo
son Nivel C. La primera decisión siempre es identificar el
mecanismo del caso: rug pull / emisión fraudulenta, colapso
del protocolo (stablecoin o DeFi), insolvencia del exchange, o
exploit de smart contract. Cada mecanismo tiene instrumentos
y prioridades de evidencia radicalmente distintos.
Tabla de prioridades de recolección de evidencia en
criptoeconomía y activos digitales

Taxonomía General de Aplicaciones
Si tu Qué
Por
incertid Qué buscar
La evidencia que qué
umbre rango / qué
más la reduce es… funcion
princip reduce pregunt
a
al es… ar
1. ¿El Análisis forense on- Cada Determ ¿Los
mecanis chain CD2 de los mecanis ina el fondos
mo del flujos de fondos en mo instrum salieron
caso — el período del tiene un ento del
rug pull, colapso: ¿los fondos grafo de princip protocol
colapso salieron del respons al del o a
de protocolo a carteras abilidad análisis carteras
protocol de los fundadores distinto controla
o, (rug pull), el y das por
insolven mecanismo de evidenci los
cia de estabilización falló as fundado
exchang bajo su propia lógica prioritar res? ¿El
e, o (colapso de ias mecanis
exploit? protocolo), los distintas mo de
fondos de clientes . La estabiliz
no estaban confusi ación del
segregados ón entre stablecoi
(exchange), o mecanis n entró
fondos fueron mos en
drenados por una produce espiral?
transacción de evidenci ¿El
ataque (exploit)? a exchang
relevant e tiene
e para proof of
uno reserves
pero no que no
para el cuadra?
que ¿Hay
determi una
na R*. transacci
ón de
exploit
identific
able on-
chain?
2. [RUG Análisis forense on- El Reduce ¿Las
PULL] chain CD1/CD2 del patrón rango carteras
¿Los patrón de ventas de de de S del de los
fundado tokens de las ventas fundad fundado
res carteras de los de or res
vendiero fundadores en el insiders (incerti vendiero

Taxonomía General de Aplicaciones
Si tu Qué
Por
incertid Qué buscar
La evidencia que qué
umbre rango / qué
más la reduce es… funcion
princip reduce pregunt
a
al es… ar
n sus período previo al antes dumbre n tokens
tokens colapso: ¿las ventas del ontológ en los
antes del de los insiders colapso ica días/se
colapso precedieron al es la crítica) manas
en un colapso por días o señal previos
patrón semanas en un on- al
de patrón chain colapso?
insider? estadísticamente más ¿El
incompatible con robusta volumen
ventas de mercado para de
normales? establec ventas
er de las
Anteros carteras
del de
fundado insiders
r. Es el era
instrum estadísti
ento camente
que anómalo
discrimi versus el
na el rug período
pull del anterior?
proyect ¿Los
o fallido fondos
sin de las
malicia. ventas
fueron
enviados
a
exchang
es o a
carteras
de
mezcla?

### 3. Peritaje técnico del La Reduce ¿Habían
[COLAP tokenomics CD2: fragilida rango artículos
SO DE análisis del d de R* o posts
PROTO mecanismo bajo estructu del en el
COLO] distintos escenarios ral del arquitec ecosiste
¿El de estrés. ¿Habían mecanis to del ma
mecanis señales en la mo es el tokeno sobre la
mo de literatura o en el instrum mics fragilida

Taxonomía General de Aplicaciones
Si tu Qué
Por
incertid Qué buscar
La evidencia que qué
umbre rango / qué
más la reduce es… funcion
princip reduce pregunt
a
al es… ar
estabiliz ecosistema sobre la ento (incerti d del
ación era fragilidad del que dumbre mecanis
estructur mecanismo antes del establec empíric mo
almente colapso? e si el a) antes del
viable? colapso colapso?
era ¿Otros
previsib stablecoi
le dado ns con
el mecanis
diseño mos
— y por similares
tanto si habían
el colapsad
diseñad o antes?
or tenía ¿El
R* con análisis
S bajo. del
mecanis
mo bajo
condicio
nes de
estrés
produce
espiral
de
muerte
predecib
le?

### 4. Análisis forense on- La Estable ¿Hay
[EXCH chain CD1/CD2 de segregac ce la transfere
ANGE] los flujos entre las ión de mezcla ncias
¿Los carteras del fondos de docume
fondos exchange y las es la fondos ntadas
de carteras de entidades obligaci (incerti on-chain
clientes relacionadas: ¿hay ón dumbre entre las
estaban transferencias entre central empíric carteras
segregad las carteras de del a de
os de los custodia de clientes y exchang central) custodia
fondos las carteras de e de del
propios? trading propio o de custodia exchang
entidades afiliadas . Su e y las
sin justificación de verificac carteras

Taxonomía General de Aplicaciones
Si tu Qué
Por
incertid Qué buscar
La evidencia que qué
umbre rango / qué
más la reduce es… funcion
princip reduce pregunt
a
al es… ar
servicio a los ión on- de
clientes? chain es Alameda
el Researc
instrum h o
ento equivale
más ntes? ¿El
directo proof of
para reserves
establec publicad
er la o
mezcla correspo
de ndía al
fondos. capital
realment
e
custodia
do?

### 5. Análisis técnico La Estable ¿Cuándo
[EXPL CD2 de la detectab ce R* fue
OIT] ¿El vulnerabilidad ilidad del docume
vector explotada versus el del auditor ntado el
de estado de la vector (incerti vector
ataque literatura de determi dumbre de
estaba seguridad de smart na S del técnica) ataque
docume contracts al auditor en la
ntado en momento de la — y por literatur
la auditoría. ¿El vector tanto a de
literatura (reentrancy, flash cuánto segurida
de loan, price oracle del R* d de
segurida manipulation) estaba del smart
d al documentado en los exploit contract
moment estándares de le s?
o de la auditoría corresp ¿Otros
auditoría disponibles? onde al auditore
? auditor s con
versus al estándar
atacante es
. similares
lo
incluían
en sus
proceso

Taxonomía General de Aplicaciones
Si tu Qué
Por
incertid Qué buscar
La evidencia que qué
umbre rango / qué
más la reduce es… funcion
princip reduce pregunt
a
al es… ar
s al
moment
o de la
auditoría
del
protocol
o
explotad
o? ¿El
informe
de
auditoría
analiza
explícita
mente
este tipo
de
vector?
6. ¿El Análisis jurídico del Sin Determ ¿Los
token instrumento (previo determi ina el compra
emitido al análisis de nar el marco dores
califica responsabilidad): marco legal del
como aplicación del test de regulato aplicabl token
security Howey (EE.UU.) o rio e tenían
en la el equivalente aplicabl (incerti expectat
jurisdicci regulatorio de la e, el dumbre iva
ón jurisdicción análisis jurisdic razonabl
aplicable aplicable. Este de cional) e de
? análisis determina respons benefici
qué marco legal abilidad o
aplica y qué no derivada
regulador tiene puede del
jurisdicción. establec trabajo
er qué del
obligaci equipo
ones emisor?
tenía el ¿El
emisor y token
cuáles otorga
incumpl derecho
ió. s
económi

Taxonomía General de Aplicaciones
Si tu Qué
Por
incertid Qué buscar
La evidencia que qué
umbre rango / qué
más la reduce es… funcion
princip reduce pregunt
a
al es… ar
cos
sobre
los
resultad
os del
protocol
o? ¿El
regulado
r de
valores
de la
jurisdicc
ión
aplicable
se ha
pronunc
iado
sobre
tokens
similares
?
7. ¿Cuál D_total = Sin el Estable ¿Cuánto
es el valor_capital_perdid D_total ce la capital
D_total o_verificable_on- cuantifi escala total
y el chain. AD_i = R*_i cado y de la enviaron
AD_i de × D_total para cada los pretensi los
cada nodo del grafo. Los AD_i ón inversor
nodo del R* son estimaciones estimad (incerti es al
grafo? Nivel C que deben os, la dumbre protocol
declararse con pretensi empíric o o al
incertidumbre ón de a) exchang
explícita. respons e?
abilidad ¿Cuánto
no tiene recupera
base ron?
calculad ¿Qué
a. fracción
del daño
total es
atribuibl
e a cada
actor del

Taxonomía General de Aplicaciones
Si tu Qué
Por
incertid Qué buscar
La evidencia que qué
umbre rango / qué
más la reduce es… funcion
princip reduce pregunt
a
al es… ar
grafo
dado el
análisis
de R*?
Árbol de decisión en criptoeconomía y activos digitales
El árbol comienza con la identificación del mecanismo del
caso, porque cada mecanismo tiene un grafo de
responsabilidad, evidencias prioritarias y prioridades de
reforma completamente distintos.
¿Cuál es el mecanismo principal del caso?
├─ Mecanismo A: RUG PULL / EMISIÓN
FRAUDULENTA
│
└─ PRIORIDAD 1: Análisis forense on-chain del
patrón de ventas de tokens de los insiders.
· ¿Los insiders vendieron antes del colapso en patrón
estadísticamente anómalo?
· Si sí → Anteros del fundador, S bajo. Proceso penal
viable si el marco regulatorio aplica.
├─ Mecanismo B: COLAPSO DE PROTOCOLO
(stablecoin o DeFi)
│
└─ PRIORIDAD 1: Peritaje técnico del tokenomics
— ¿era estructuralmente viable?
· Si la fragilidad era previsible → R* del arquitecto del
tokenomics es alto, S bajo.

Taxonomía General de Aplicaciones
· Si el conocimiento de la fragilidad no estaba disponible
→ Deimos dominante, S alto.
├─ Mecanismo C: INSOLVENCIA DEL EXCHANGE
(CEX)
│
└─ PRIORIDAD 1: Análisis forense on-chain de
flujos entre carteras de custodia y carteras propias.
· Aplicar instrumentos del cap. 12 (insolvencia) y cap. 13
(gobierno corporativo) al exchange.
└─ Mecanismo D: EXPLOIT DE SMART CONTRACT
├─ PRIORIDAD 1: ¿El vector era conocido en la
literatura — S del auditor?
· Si sí → R* del auditor es positivo. AD_auditor =
R*_auditor × D_total_exploit.
└─ PRIORIDAD 2: ¿El diseño del protocolo
contemplaba el vector de ataque?
· Si no → R* del arquitecto del tokenomics positivo
sobre el diseño que lo hizo posible.
— Fin del Capítulo 20 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

