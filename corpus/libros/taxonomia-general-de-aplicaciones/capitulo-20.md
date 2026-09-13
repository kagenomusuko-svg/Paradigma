PARTE II · Ciencias Económicas y Financieras

## Capítulo 20

### Criptoeconomía y activos digitales — protocolos, exchanges y responsabilidad

Organ.  Estru.  Model.  Educa.  Crisi.

Para el mediador que busca precisión · Cómo usar este capítulo Este capítulo es Nivel C. Sus rangos son candidatos pendientes de calibración empírica con jurisprudencia de litigios de activos digitales (SEC, CFTC, Unión Europea, casos nacionales). La aportación central es conceptual: los mismos principios que en el cap. 17 (plataformas digitales) aplican aquí con una singularidad nueva — el smart contract ejecuta determinísticamente sin voluntad propia (S ≈ 1.0 respecto al código desplegado), por lo que R* del smart contract apunta hacia quien lo diseñó, quien lo auditó y quien lo desplegó. El arquitecto del tokenomics es el nodo de mayor R* en la cadena algorítmica del protocolo — análogo al diseñador de la métrica del cap. 17. Este capítulo opera con cuatro ejes que deben distinguirse antes del análisis. El primero es la responsabilidad del fundador / arquitecto del protocolo: diseñó el tokenomics y las reglas del sistema que produjeron el daño. El segundo es la responsabilidad del exchange centralizado (CEX): custodia activos, conoce a sus clientes, tiene obligaciones de segregación de fondos. El tercero es el fraude en la emisión de tokens: captación de capital con representaciones falsas sobre el protocolo o sus perspectivas. El cuarto es la explotación de vulnerabilidades en contratos inteligentes: el auditor tenía R* sobre el exploit que no detectó. Para la prioridad de evidencia, ve a §9.

### §1  Descripción del subcampo

Taxonomía General de Aplicaciones

La criptoeconomía introduce en el sistema de imputación causal dos características que ningún capítulo anterior había combinado simultáneamente. La primera es la descentralización del daño: el protocolo de blockchain opera sin un actor central identificable, los smart contracts se ejecutan automáticamente sin intervención humana en cada transacción, y los inversores están dispersos globalmente sin relación contractual directa con el fundador del protocolo. La segunda es la paradoja de la transparencia opaca: el código del protocolo es públicamente visible en la blockchain — cualquiera puede leerlo — pero la intención, el diseño del tokenomics y las decisiones de los fundadores son frecuentemente tan opacas como en cualquier otro dominio. La combinación de código transparente e intención opaca es el desafío central del análisis de responsabilidad en el dominio.

El principio estructural del dominio: el smart contract no tiene voluntad — ejecuta exactamente el código desplegado. S del smart contract ≈ 1.0 respecto a su comportamiento: cualquier instancia del mismo código en las mismas condiciones produce el mismo resultado. Por eso, R* del smart contract apunta íntegramente hacia los actores humanos que lo diseñaron (el arquitecto del protocolo), lo auditaron (o no lo auditaron) y lo desplegaron. El diseñador del tokenomics — quien decidió los incentivos, la distribución inicial de tokens, los mecanismos de estabilización y las reglas de gobernanza — es el nodo de mayor R* en el grafo del protocolo, análogo al diseñador de la métrica del cap. 17.

El smart contract como nodo sin voluntad: S ≈ 1.0 y la jerarquía de R* en el protocolo El smart contract ejecuta determinísticamente. Si el código tiene una vulnerabilidad de reentrancy y un atacante la explota, el smart contract no "actuó mal" — ejecutó exactamente su código. R* del smart contract = R*_vulnerabilidad apunta hacia: (a) el diseñador del protocolo que no contempló ese vector de ataque en el diseño; (b) el auditor de seguridad que no detectó la vulnerabilidad antes del despliegue; (c) el equipo que desplegó el contrato sin las pruebas de seguridad suficientes. La misma lógica del cap. 17 (el modelo tiene S ≈ 1.0 y su R* apunta al diseñador de la métrica) aplica aquí: cambiar el smart contract sin cambiar

Taxonomía General de Aplicaciones

el diseño del tokenomics no resuelve el daño si el tokenomics tiene los incentivos que lo producen. El mecanismo de estabilización del terraUSD que colapsó en mayo 2022 no era un bug del código — era el diseño del tokenomics que hacía inevitable el colapso en una espiral de muerte bajo condiciones de estrés que eran previsibles.

Sub-variantes del dominio

Rug pull (abandono fraudulento del protocolo): los fundadores de un proyecto de DeFi o NFT captaron capital de los inversores mediante la venta de tokens con representaciones sobre el protocolo, y después retiraron la liquidez del proyecto o simplemente abandonaron el desarrollo, produciendo pérdida total a los inversores. Es la forma más directa de Anteros en el dominio: los fundadores diseñaron el esquema para extraer capital y retirarse. La distinción entre el rug pull deliberado y el proyecto que fracasó genuinamente sin malicia es el análisis central.

Colapso de stablecoin algorítmica: el emisor de una stablecoin algorítmica diseñó un mecanismo de mantenimiento del peg que era estructuralmente frágil ante espirales de ventas en condiciones de estrés — el diseño del tokenomics era la condición del colapso, no una falla técnica del código. El daño a los tenedores es la diferencia entre el valor prometido (el peg) y el valor realizado post-colapso. R* del arquitecto del mecanismo de estabilización es alto; S moderado-bajo cuando el diseño era idiosincrático.

Quiebra de exchange centralizado (CEX): el exchange que custodiaba activos de clientes mezcló los fondos de los clientes con sus activos propios, los usó para operaciones especulativas no reveladas, o simplemente operó insolvente durante un período antes del colapso (FTX como caso paradigmático). El análisis es una compilación directa de los instrumentos del cap. 13 (gobierno corporativo) y del cap. 12 (insolvencia y quiebra) aplicados al exchange como empresa.

Taxonomía General de Aplicaciones

Manipulación de precio en mercados de activos digitales: el actor realizó operaciones de wash trading, spoofing o pump-and-dump sobre activos con mercados de menor liquidez — aprovechando la escasa supervisión regulatoria del dominio para usar los mismos mecanismos que en el cap. 14 (finanzas de mercado), con menor riesgo de detección. El análisis es una extensión directa de la escala FM con la particularidad de que los registros de la blockchain son públicos y permanentes.

Fraude en la emisión de tokens (ICO/IEO/IDO): los emisores de tokens vendieron instrumentos financieros con representaciones materiales falsas sobre el protocolo, sus perspectivas o el uso de los fondos captados. La distinción entre el token que es un valor (security token, sujeto a la regulación de valores) y el que no lo es (utility token) es el análisis regulatorio previo que determina qué marco legal aplica.

Exploit de smart contract por vulnerabilidad de código: un atacante identificó y explotó una vulnerabilidad en el código de un protocolo DeFi para drenar sus fondos. El grafo incluye al atacante (R* directo sobre el daño), al diseñador del protocolo (R* por el diseño que no contempló el vector de ataque), al auditor de seguridad (R* por no detectar la vulnerabilidad) y al equipo que desplegó el contrato sin el nivel de auditoría requerido por la magnitud del capital expuesto.

### §2  Escala de evidencia CD0–CD8  · Criptoeconomía y activos digitales

La escala CD0–CD8 traduce la jerarquía general E0–E8 al vocabulario de la criptoeconomía. Su característica más relevante y singular respecto a todos los dominios anteriores es que la blockchain registra públicamente y de manera permanente todas las transacciones del protocolo — lo que significa que los datos de la cadena (on-chain data) tienen una calidad documental sin precedente para establecer qué transacciones ocurrieron, cuándo y en qué secuencia. Esa transparencia on-chain contrasta con la opacidad de las

Taxonomía General de Aplicaciones

### comunicaciones internas de los fundadores, que con frecuencia operan de manera pseudónima o anónima. Nivel C — rangos candidatos pendientes de calibración empírica formal.

Nota de calibración Nivel C Los rangos CD0–CD8 son candidatos. La calibración empírica requiere: (a) análisis de los casos de enforcement de la SEC, la CFTC, la FCA y equivalentes europeos contra emisores de tokens y exchanges; (b) litigios civiles contra fundadores de protocolos que colapsaron; (c) jurisprudencia de los casos de insolvencia de exchanges (FTX, Celsius, Voyager). Antes de usar estos rangos en una pretensión formal, ajustar con los desarrollos jurisprudenciales más recientes del dominio.

Descripción y ejemplos en el

Nivel Tipo de evidencia

Rango w (candidato)

dominio de la criptoeconomía

CD1 Datos on-chain verificables y documentos directos del emisor o exchange

[0.72, 0.88]

Registros de la blockchain que establecen las transacciones relevantes con timestamp, dirección de origen y destino, y valor transferido; código del smart contract desplegado públicamente con su historial de versiones; whitepaper y documentos de emisión del token con las representaciones sobre el protocolo y el uso de fondos; registros de custodia del exchange que establezcan la mezcla de fondos de clientes con fondos propios; comunicaciones internas del equipo fundador obtenidas

Taxonomía General de Aplicaciones

Descripción y ejemplos en el

Nivel Tipo de evidencia

Rango w (candidato)

dominio de la criptoeconomía

mediante discovery o filtradas.

CD2 Peritaje técnico de blockchain y análisis forense on-chain, o peritaje de tokenomics

[0.60, 0.80]

Análisis forense on-chain que reconstruye la cadena causal de las transacciones relevantes — rastreo de fondos a través de múltiples carteras, análisis de los patrones de transacción que establecen la coordinación entre actores, identificación de los flujos de capital entre el protocolo y las carteras de los fundadores; análisis técnico del código del smart contract que establece la vulnerabilidad explotada y su detectabilidad previa al exploit; peritaje del diseño del tokenomics que establece si el mecanismo de estabilización era estructuralmente viable o inevitablemente frágil bajo condiciones de estrés documentadas.

CD3 Testimonios convergentes de participantes del ecosistema con corroboración on-chain

[0.48, 0.66]

Declaraciones de inversores, desarrolladores o insiders del protocolo que describen consistentemente las decisiones de diseño, las representaciones

Taxonomía General de Aplicaciones

Descripción y ejemplos en el

Nivel Tipo de evidencia

Rango w (candidato)

dominio de la criptoeconomía

de los fundadores o la gestión de fondos del exchange, con al menos una transacción on-chain o un documento del proyecto consistente. Las declaraciones de colaboradores del equipo fundador son CD3 de alto valor cuando incluyen detalles verificables on-chain.

CD4 Análisis estadístico del comportamiento del protocolo o del mercado del token

[0.38, 0.58]

Análisis on-chain que muestra que los patrones de transacción son estadísticamente incompatibles con el comportamiento de un mercado sin manipulación — wash trading detectado por transacciones circulares entre carteras relacionadas, pump-and-dump detectado por la correlación entre el patrón de tenencia de los fundadores y el movimiento de precio, selección adversa en el mecanismo de estabilización de la stablecoin.

CD5 Análisis del diseño del tokenomics y del whitepaper versus el

[0.28, 0.48]

Comparación del diseño del tokenomics descrito en el whitepaper con el comportamiento real

Taxonomía General de Aplicaciones

Descripción y ejemplos en el

Nivel Tipo de evidencia

Rango w (candidato)

dominio de la criptoeconomía

comportamiento observable

del protocolo, que establece las discrepancias entre las representaciones y la realidad; análisis de la distribución inicial de tokens (allocations) versus los compromisos declarados; análisis de los mecanismos de gobernanza en la práctica versus lo descrito en el whitepaper.

CD6 Inferencia estructural por la arquitectura del protocolo y el comportamiento del mercado

[0.18, 0.38]

El diseño del protocolo y el comportamiento del mercado del token son consistentes con el mecanismo de daño analizado, sin análisis técnico específico que establezca la cadena causal.

CD7 Correlación temporal entre acciones de los fundadores y movimientos del precio o del protocolo

[0.05, 0.22]

Las acciones conocidas de los fundadores (ventas de tokens, cambios en el protocolo) coinciden temporalmente con los movimientos de precio o los eventos dañinos sin análisis causal.

CD8 Especulación sobre el comportamiento de los fundadores sin datos on-

[0.00, 0.10]

Afirmaciones sobre las intenciones de los fundadores sin datos verificables on-chain ni documentación del proyecto.

Taxonomía General de Aplicaciones

Descripción y ejemplos en el

Nivel Tipo de evidencia

Rango w (candidato)

dominio de la criptoeconomía

chain ni documentos

CD0 Ausencia documentada de conexión causal con el daño

w = 0.00

Análisis forense CD2 que establece que el daño fue producido por factores externos al protocolo o al exchange (colapso del mercado general, exploit de otro protocolo que afectó en cascada), o que el diseño del tokenomics era estructuralmente sólido dado el estado del conocimiento en el momento del diseño.

La singularidad de los datos on-chain como evidencia: transparencia sin interpretación automática El registro de la blockchain es el más completo y permanente de todos los dominios del libro. Todas las transacciones son públicas, verificables, con timestamp y sin posibilidad de alteración retroactiva. Eso hace que CD1 on-chain sea la evidencia más confiable del dominio para establecer qué transacciones ocurrieron. Pero la transparencia on-chain no resuelve la pregunta de la intención: el análisis forense on-chain establece qué pasó, no por qué. La intención de los fundadores — la distinción entre rug pull deliberado y proyecto fallido sin malicia — requiere evidencia off-chain (comunicaciones, documentos del proyecto, whitepaper) para establecer lo que la blockchain no registra.

### §3  Firmas documentales por Hijo e información para S del fundador y del operador del exchange

Taxonomía General de Aplicaciones

Los Hijos de Afrodita aplican a los actores humanos identificables en el dominio: el fundador / arquitecto del protocolo, el CEO y los directivos del exchange centralizado, el auditor de seguridad que emitió el informe previo al exploit. No aplican al smart contract (nodo sin voluntad), ni al protocolo de blockchain como sistema descentralizado.

La distinción más crítica del dominio es entre el fundador que diseñó el esquema desde el inicio con intención de captar capital y retirarse (Anteros dominante, rug pull deliberado, S muy bajo) y el fundador que diseñó un protocolo que genuinamente creía viable y que fracasó por razones de mercado o por un diseño deficiente que no anticipó (Potós / Deimos, proyecto fallido sin malicia, S más alto). Esa distinción determina si el proceso es penal o civil. El análisis forense on-chain establece los hechos; el análisis de los Hijos desde las comunicaciones y el whitepaper establece la intención.

### §3.1 Hijos de legibilidad alta en el dominio de la criptoeconomía

Qué informa para S del

Firma en el

Error de discrimina

Fuente documenta

fundador

expediente

Hijo

/ operador

on-chain y

ción frecuente

l típica

off-chain

del exchange

Anter os

S muy bajo [0.03, 0.22]. El fundador diseñó el protocolo o el exchange como un esquema

Patrones de venta on-chain de tokens de los fundadores coincidentes con campañas de marketing

Análisis forense on-chain de los flujos de fondos de los fundadores. Comunicaci ones filtradas o

Confundir con Potós/Dei mos cuando el proyecto fracasó por condiciones de mercado adversas sin que los

Taxonomía General de Aplicaciones

Qué informa para S del

Firma en el

Error de discrimina

Fuente documenta

fundador

expediente

Hijo

/ operador

on-chain y

ción frecuente

l típica

off-chain

del exchange

para captar capital de inversores con intención de retirarse con los fondos o de operar de manera que enriquece a los insiders a expensas de los inversores externos. La conducta fue genuinam ente idiosincrát ica: el diseño específico del mecanism o de extracción , el timing de las ventas de tokens de los insiders antes del

dirigidas a inversores externos. Transferenci as de fondos del protocolo a carteras controladas por los fundadores inmediatam ente antes del colapso (exit scam). Comunicaci ones privadas donde los fundadores discuten la estrategia de extracción de valor. Mezcla de fondos de clientes con fondos propios del exchange para operaciones especulativa s no reveladas.

discovery. Auditoría forense del exchange. Comparació n del whitepaper con el comportami ento real del protocolo.

fundadores se enriqueciera n a expensas de los inversores. La pregunta discriminant e: ¿los fundadores vendieron sus tokens antes del colapso en un patrón que sugiere conocimient o previo, o perdieron ellos también?

Taxonomía General de Aplicaciones

Qué informa para S del

Firma en el

Error de discrimina

Fuente documenta

fundador

expediente

Hijo

/ operador

on-chain y

ción frecuente

l típica

off-chain

del exchange

colapso, la arquitectu ra de las carteras que recibieron los fondos, no son los de un equipo que genuinam ente creyó en el proyecto.

Potós S moderado -alto [0.40, 0.70]. El fundador replicó el modelo de proyecto de cripto estándar del período — whitepape r con promesas ambiciosa s, tokenomic s con alta proporció n de tokens para el

Diseño del tokenomics que replica el estándar del sector en ese período. Whitepapers con representaci ones comparables a otros proyectos del sector que también fracasaron. Mecanismos de rendimiento (APY) que eran comparables con otros protocolos

Whitepapers de proyectos comparables del período. Estándares del sector en el diseño de tokenomics. Cultura del ecosistema cripto en el período analizado.

Confundir con Anteros cuando el equipo vendió sus tokens antes del colapso de manera que sugiere conocimient o previo del fracaso inminente. El timing de las ventas on-chain de los insiders es el instrumento que discrimina Anteros de Potós en los casos límite.

Taxonomía General de Aplicaciones

Qué informa para S del

Firma en el

Error de discrimina

Fuente documenta

fundador

expediente

Hijo

/ operador

on-chain y

ción frecuente

l típica

off-chain

del exchange

equipo fundador, mecanism os de staking con rendimien tos insostenib les — sin cuestionar si el modelo era viable a largo plazo o éticament e sostenible. Cualquier equipo fundador con la misma cultura del ecosistem a de cripto en ese período habría diseñado un proyecto similar.

de DeFi del período.

Fobo s

S moderado -alto [0.52, 0.78]. El fundador

Comunicaci ones que documentan la presión sobre el

Comunicaci ones del equipo fundador. Análisis de

Confundir con Anteros cuando el fundador diseñó

Taxonomía General de Aplicaciones

Qué informa para S del

Firma en el

Error de discrimina

Fuente documenta

fundador

expediente

Hijo

/ operador

on-chain y

ción frecuente

l típica

off-chain

del exchange

o el operador del exchange tomó decisiones que sabía que eran problemát icas bajo la presión del entorno — la presión competitiv a de otros protocolo s con rendimien tos aún más altos, la presión de los inversores para mostrar crecimient o, la presión de la carrera hacia el TVL (total value locked) como métrica de éxito del sector. La presión

equipo fundador para mantener rendimiento s competitivo s con otros protocolos. Evidencia de que el equipo sabía que los rendimiento s eran insostenible s, pero los mantuvo para no perder competitivid ad. Análisis de la dinámica del sector en el período.

los rendimiento s del sector en el período. Evidencia de la presión de los inversores institucional es o de los validadores de gobernanza.

específicam ente el esquema para beneficiarse de la presión del mercado a expensas de los inversores finales.

Taxonomía General de Aplicaciones

Qué informa para S del

Firma en el

Error de discrimina

Fuente documenta

fundador

expediente

Hijo

/ operador

on-chain y

ción frecuente

l típica

off-chain

del exchange

del ecosistem a en ese período era condición de las decisiones dañinas.

### §3.2 Hijos de legibilidad baja en el dominio cripto

Deimos: puede aparecer en fundadores que genuinamente no comprendieron los riesgos estructurales de su diseño de tokenomics — el equipo que diseñó el mecanismo de estabilización del terraUSD creyendo que la tensión entre LUNA y UST era un mecanismo robusto sin anticipar las condiciones de espiral de muerte que se materializaron. S alto cuando el conocimiento de las fragilidades de los mecanismos de estabilización algorítmica no estaba consolidado en la literatura al momento del diseño. Asignar con nota de incertidumbre alta dado el estado del conocimiento del ecosistema DeFi en el período analizado.

Harmonía en el dominio cripto: el equipo fundador que implementó los estándares de seguridad más rigurosos disponibles (auditorías múltiples, bug bounties, tiempo de lock de los tokens del equipo), publicó transparentemente la arquitectura del protocolo incluyendo sus riesgos, y actuó de buena fe ante el fracaso para minimizar el daño a los inversores (reembolso parcial, transparencia sobre las causas del colapso). Es la referencia normativa del equipo fundador diligente en el ecosistema.

Taxonomía General de Aplicaciones

§3.3 El smart contract no tiene Hijo — la jerarquía de R* en el protocolo Principio derivado del cap. 17 (plataformas digitales): el smart contract ejecuta determinísticamente. S ≈ 1.0 respecto a su comportamiento en las condiciones del código desplegado. Su R* apunta íntegramente hacia los actores humanos que lo diseñaron, auditaron y desplegaron. La jerarquía en el protocolo DeFi: R*_arquitecto_tokenomics > R*_auditor_seguridad > R*_deployer > R*_smart_contract. Cambiar el smart contract sin cambiar el diseño del tokenomics no resuelve el daño si el tokenomics tiene los incentivos que lo producen — análogo a cambiar el modelo sin cambiar la métrica en el cap. 17.

### §4  ¿Qué cuenta como asunción (α) en el dominio de la criptoeconomía?

α en el dominio cripto mide lo que el fundador, el operador del exchange o el auditor de seguridad han hecho concretamente sobre su posición causal: restitución a los inversores proporcional a su AD_i = R*_i × D_total, cooperación activa con reguladores e investigadores, implementación de los estándares de seguridad y transparencia que su posición requería antes del daño, reforma del protocolo cuando el diseño fallido fue identificado.

α del fundador es completamente independiente del dolo en el dominio cripto Un fundador que diseñó deliberadamente el rug pull puede tener α alto si después cooperó plenamente con el regulador, permitió la recuperación de fondos y restituyó a los inversores. Un fundador que genuinamente creyó en el proyecto y fracasó puede tener α = 0 si nunca fue transparente sobre las causas del fracaso ni cooperó con los investigadores. Los Hijos informan S del fundador; α mide lo que hizo después sobre su posición causal.

Taxonomía General de Aplicaciones

Acción del

¿Cuenta

para α? Razón Tipo de α

actor

Restitución a los inversores proporcional al AD_i del actor, usando fondos propios

Sí — α económico directo

Asunción económica de la posición causal. La proporcionalidad al AD_i establece si es completa o parcial.

Voluntario o forzado

Voluntario

Cooperación activa con el regulador — información completa sobre el protocolo, los flujos de fondos y las decisiones de diseño

Sí — α de cooperación

La cooperación permite reconstruir el grafo completo del esquema. Su valor es mayor que el pago proporcional cuando permite identificar a otros nodos.

Voluntario

Implementación de auditorías de seguridad múltiples antes del despliegue del smart contract, proporcionales al capital expuesto

Sí — α estructural preventivo

Las auditorías de seguridad son el α más directo para el exploit de smart contract: reducen el R* del auditor y del deployer.

Voluntario

Lock de los tokens del equipo fundador con vesting de largo plazo y cliff period documentados on-chain

Sí — α de alineación de incentivos

El lock on-chain verificable alinea los incentivos del fundador con los del inversor. Sin lock, el fundador puede vender en cualquier momento sin señal previa.

Voluntario

Bug bounty activo con recompensas proporcionales al

Sí — α de prevención de exploit

El bug bounty incentiva la detección proactiva de

Taxonomía General de Aplicaciones

Acción del

¿Cuenta

para α? Razón Tipo de α

actor

capital expuesto del protocolo

vulnerabilidades antes de que sean explotadas.

Voluntario

El exchange separó efectivamente los fondos de los clientes de los fondos propios con verificación de reservas proofable on-chain

Sí — α estructural del exchange

La segregación efectiva de fondos con proof of reserves verificable reduce el R* del exchange en el daño a los clientes.

—

Anuncio de "compensación total" sin mecanismo verificable de distribución

No — hasta que se ejecuta la distribución verificable

La promesa no ejecutada no es α. Es comunicación sin consecuencia sobre la posición causal.

### La escala de α en el dominio cripto

Indicadores on-

Nivel Rango

Descripción

chain y off-

α

observable

chain

Extracción activa / exit scam

### 0.00 – 0.03 Los fundadores retiraron activamente los fondos del protocolo o del exchange hacia carteras propias y desaparecieron.

Transferencias on-chain de los fondos del protocolo a carteras no relacionadas con el proyecto. Abandono de los canales de comunicación. Sin cooperación con el regulador.

Taxonomía General de Aplicaciones

Indicadores on-

Nivel Rango

Descripción

chain y off-

α

observable

chain

Abandono pasivo / opacidad

### 0.04 – 0.15 El proyecto colapsó y los fundadores no han cooperado ni restituido. Comunicaciones mínimas sobre las causas del colapso.

Sin restitución documentada. Sin cooperación con el regulador. Comunicaciones evasivas sobre los fondos.

Reconocimiento nominal

### 0.16 – 0.28 El fundador reconoció el fracaso públicamente pero sin restitución ni cooperación sustancial.

Comunicados públicos de reconocimiento. Sin restitución verificable. Cooperación parcial o evasiva.

Asunción parcial

### 0.29 – 0.50 Restitución parcial a los inversores, cooperación limitada con el regulador o transparencia sobre las causas del fracaso.

Restitución documentada menor al AD_i. Cooperación con algunos aspectos de la investigación. Publicación de análisis post-mortem.

Asunción activa 0.51 – 0.75 Restitución sustancial en proceso, cooperación activa con el regulador, implementación de los mecanismos de seguridad requeridos en el nuevo protocolo.

Restitución del 50–70% del AD_i. Cooperación documentada por el regulador. Proof of reserves activo para el exchange. Auditorías múltiples del nuevo protocolo.

Asunción funcional

### 0.76 – 0.92 Restitución proporcional a la

Restitución del 75–90% del

Taxonomía General de Aplicaciones

Indicadores on-

Nivel Rango

Descripción

chain y off-

α

observable

chain

mayor parte del AD_i, cooperación plena con el regulador, reforma del protocolo o del exchange verificable.

AD_i. Cooperación plena documentada. Proof of reserves con auditoría independiente. Vesting de tokens del equipo on-chain.

Asunción plena 0.93 – 1.00 Restitución integral, cooperación que permitió establecer el grafo completo, implementación de todos los estándares de seguridad y transparencia.

Restitución integral. Cooperación que identificó a todos los actores del esquema. Proof of reserves verificable. Auditorías de seguridad públicas del protocolo reformado.

### §5  Construcción del grafo típico del dominio

### La jerarquía del grafo cripto: R*_arquitecto_tokenomics > R*_auditor_seguridad > R*_deployer > R*_smart_contract

Esta jerarquía es el principio más importante del capítulo y su derivación directa del cap. 17. El smart contract (el nodo más técnicamente analizable) tiene el R* más bajo porque S ≈ 1.0: cualquier instancia del mismo código en las mismas condiciones produce el mismo comportamiento. El arquitecto del tokenomics (el menos visible en el código) tiene el R* más alto porque sus decisiones sobre qué incentivos construir en

Taxonomía General de Aplicaciones

### el protocolo son la causa raíz de los daños predecibles del sistema.

Tipo de

Función en el

grafo S típico Ejemplo en el

nodo

dominio

Arquitecto del tokenomics (AT)

El fundador o el equipo que tomó las decisiones normativas de diseño del protocolo — qué incentivos construir, cómo distribuir los tokens inicialmente, qué mecanismo de estabilización implementar, cuánto del suministro reservar para el equipo fundador. Es el nodo de mayor R* del grafo del protocolo. Sus Hijos informan S. Anteros: diseñó el esquema para extraer valor. Potós: replicó el modelo estándar sin cuestionar su viabilidad. Deimos: no comprendió las fragilidades del diseño.

Variable [0.10 – 0.55]

El equipo de Terraform Labs que diseñó el mecanismo LUNA/UST con la tensión entre el token de gobernanza y la stablecoin. El fundador de un protocol DeFi que reservó el 30% de los tokens para el equipo con vesting de 6 meses. El CEO del exchange que decidió usar los fondos de los clientes para operaciones especulativas.

Auditor de seguridad (AS)

La firma que auditó el smart contract antes del despliegue. R* positivo cuando su proceso de auditoría no detectó la vulnerabilidad que

Moderado [0.30 – 0.65]

La firma de auditoría que revisó el código del protocolo DeFi que fue explotado mediante reentrancy attack — un

Taxonomía General de Aplicaciones

Tipo de

Función en el

grafo S típico Ejemplo en el

nodo

dominio

fue explotada y cuando el estándar de la industria en ese momento hacía esa detección razonablemente esperable. S del auditor es moderado cuando el vector de ataque estaba documentado en la literatura de seguridad de smart contracts y otros auditores lo habrían detectado.

vector documentado en la literatura desde el hack del DAO en 2016. El auditor que emitió certificación de seguridad sin incluir pruebas de fuzzing o análisis formal del mecanismo de estabilización.

Operador del exchange centralizad o (OE)

El CEO y los directivos del exchange que tomaron las decisiones de custodia, de segregación de fondos y de gobernanza del exchange. Su análisis sigue los instrumentos del cap. 13 (gobierno corporativo) — los Hijos aplican a los directivos individuales, no al exchange como entidad. El exchange como entidad tiene R* sobre el daño a los clientes proporcional a cuánto las decisiones de su gobierno corporativo fueron

Variable [0.10 – 0.55] para directivos individuale s

El CEO de FTX que mezcló fondos de clientes con fondos del hedge fund afiliado. El directivo de Celsius que continuó pagando rendimientos altos a los inversores mientras el protocolo acumulaba pérdidas ocultas. El COO de Voyager que no implementó la segregación de fondos requerida por las licencias estatales.

Taxonomía General de Aplicaciones

Tipo de

Función en el

grafo S típico Ejemplo en el

nodo

dominio

la condición del daño.

Deployer del smart contract (DE)

El equipo o la persona que desplegó el contrato en la blockchain. R* positivo cuando desplegó sin el nivel de auditoría proporcionado al capital expuesto, o cuando desplegó sabiendo que había vulnerabilidades identificadas que no se habían resuelto.

Moderado-alto [0.40 – 0.72] cuando desplegó sin auditoría suficiente

El equipo que desplegó el contrato del protocolo DeFi con $500M en liquidez después de solo una auditoría de firmas con track record limitado. El equipo que ignoró los hallazgos de la auditoría interna para cumplir el deadline de lanzamiento.

≈ 1.00 El contrato de Euler Finance explotado por $197M en 2023. El contrato de Ronin Bridge explotado por $625M en 2022. El contrato del DAO explotado por $60M en 2016. En todos los casos, el smart contract ejecutó su código — el problema estaba en el diseño o en la auditoría, no en el comportamient o del contrato.

Smart contract (SC)

El código del protocolo desplegado en la blockchain. Nodo sin voluntad con S ≈ 1.0. R* residual apunta al arquitecto del tokenomics y al deployer. Transparente on-chain — cualquiera puede leer su código — pero ejecuta determinísticament e sin posibilidad de "actuar mal". Los exploits no son el smart contract actuando inesperadamente: son el smart contract ejecutando exactamente su código en

Taxonomía General de Aplicaciones

Tipo de

Función en el

grafo S típico Ejemplo en el

nodo

dominio

condiciones que el diseñador no contempló.

Atacante (ATK)

El actor que identificó y explotó la vulnerabilidad. R* positivo sobre el daño directo. S moderado-bajo cuando el exploit requería un nivel de sofisticación técnica idiosincrática y no habría sido encontrado por cualquier actor con acceso al código — S bajo cuando el vector de ataque era conocido y documentado en la literatura de seguridad.

Variable [0.15 – 0.60]

El atacante que ejecutó el exploit del DAO en 2016 usando reentrancy — un vector que otros actores en la comunidad ya habían señalado como riesgo antes del ataque. El grupo de atacantes que explotó la clave privada del validator de Ronin Bridge.

### Configuraciones canónicas del grafo de criptoeconomía

Configuración 1 — Rug pull deliberado (Anteros dominante del fundador) AT (fundador con Anteros: diseñó el esquema para captar capital y retirarse, S muy bajo) → SC (smart contract que ejecuta el mecanismo de extracción, S ≈ 1.0) → Inversores (Nf) Los patrones on-chain del rug pull: (a) ventas masivas de tokens del equipo fundador en el período previo al abandono; (b) transferencias de los fondos del protocolo a carteras externas no identificadas; (c) abandono de los canales de comunicación del proyecto. AD_fundador = R*_fundador × D_total. D_total = capital captado en la emisión − valor residual del token post-colapso.

Taxonomía General de Aplicaciones

Configuración 2 — Colapso de stablecoin algorítmica (diseño del tokenomics frágil) AT (arquitecto del mecanismo de estabilización: S moderado-bajo si el diseño era idiosincrático y frágil bajo condiciones de estrés previsibles) + AS (auditor de seguridad que no auditó el mecanismo de estabilización, solo el código) → SC (smart contract que ejecuta el mecanismo de quema/emisión) → Tenedores del stablecoin (Nf) D_stablecoin = N_tenedores × (valor_nominal_del_peg − valor_realizado_post_colapso). El análisis del arquitecto del tokenomics establece si el mecanismo de estabilización era estructuralmente viable o si la espiral de muerte era previsible bajo condiciones de estrés. Si otros actores del ecosistema habían señalado públicamente la fragilidad del mecanismo antes del colapso, la S del arquitecto disminuye (la fragilidad era detectable con los instrumentos disponibles).

Configuración 3 — Quiebra del exchange con mezcla de fondos de clientes OE (directivos del exchange: análisis del cap. 13 gobierno corporativo — Anteros si la mezcla de fondos fue deliberada, Deimos si los directivos no tenían visibilidad de la insolvencia) + SC_exchange (sistemas de custodia del exchange, nodo sin voluntad) → Clientes del exchange (Nf) Este análisis es una compilación directa del cap. 12 (insolvencia y quiebra) aplicado al exchange. La distinción central: ¿cuándo cruzó el exchange la zona de insolvencia? ¿Qué decisiones tomaron los directivos en esa zona? ¿Los fondos de los clientes estaban segregados o mezclados con los fondos propios? El análisis forense on-chain establece los flujos de fondos. El análisis de gobierno corporativo establece las responsabilidades individuales de los directivos.

Configuración 4 — Exploit de smart contract por vulnerabilidad no auditada ATK (atacante: R* directo sobre el exploit, S variable según sofisticación requerida) + AT (diseñador del protocolo que no contempló el vector de ataque: R* por el diseño) + AS (auditor que no detectó la vulnerabilidad: R* proporcional a la detectabilidad del vector con los estándares de auditoría disponibles) → Proveedores de liquidez / usuarios del protocolo (Nf)

Taxonomía General de Aplicaciones

El análisis del auditor es el instrumento más técnico del capítulo: S del auditor depende de si el vector de ataque estaba documentado en la literatura de seguridad de smart contracts al momento de la auditoría. Para los vectores clásicos (reentrancy, integer overflow, flash loan attacks en protocolos con ciertos patrones), S del auditor es moderado-bajo — eran previsibles y detectables con los instrumentos de auditoría estándar. Para vectores novedosos, S es más alto y R* del auditor es menor.

### §6  Preguntas que responde este capítulo

### Nota de calibración: respuestas Nivel C. Ajustar con la jurisprudencia más reciente de los reguladores de valores y de los tribunales en casos de activos digitales.

Nivel de

Pregunta del

caso Instrumento que la responde

certeza posible

¿El colapso del protocolo fue un rug pull deliberado (Anteros) o un proyecto fallido sin malicia (Potós/Deimo s)?

Análisis forense on-chain CD2 del patrón de ventas de tokens de los fundadores antes del colapso + análisis off-chain CD1/CD3 de las comunicaciones del equipo + análisis del diseño del tokenomics versus las representaciones del whitepaper.

Declaración B con CD1/CD2 de calidad. Declaración C si el patrón on-chain es ambiguo entre ventas de insiders con información privilegiada y ventas de mercado normales.

¿El mecanismo de estabilización del stablecoin era estructuralmen te viable o inevitablement

Peritaje técnico del tokenomics CD2: análisis del mecanismo de estabilización bajo distintos escenarios de estrés (reducción del capital, caída del precio del token de gobernanza, espirales de ventas). Comparación con la literatura de estabilidad de

Declaración B con peritaje CD2 de calidad. El contrafáctic o del mecanismo

Taxonomía General de Aplicaciones

Nivel de

Pregunta del

caso Instrumento que la responde

certeza posible

e frágil bajo condiciones de estrés previsibles?

mecanismos algorítmicos disponible al momento del diseño.

bajo condiciones de estrés tiene incertidumb re y debe presentarse con análisis de sensibilidad.

¿El exchange mezcló fondos de clientes con fondos propios — hay insolvencia de custodia?

Análisis forense on-chain CD1/CD2 de los flujos de fondos entre las carteras del exchange y las carteras de entidades relacionadas. Auditoría de la segregación de fondos y del proof of reserves declarado versus el real.

Declaración A o B si hay análisis forense on-chain completo de los flujos de fondos. La trazabilidad on-chain es el instrumento más poderoso del dominio para este análisis.

¿El exploit de smart contract era previsible dado el estado de la auditoría de seguridad al momento del despliegue?

Análisis técnico CD2 de la vulnerabilidad explotada: ¿estaba documentada en la literatura de seguridad de smart contracts al momento de la auditoría? ¿Los auditores del estándar de la industria la habrían detectado con los procesos disponibles?

Declaración B con peritaje técnico CD2 de alta calidad. La detectabilida d de la vulnerabilida d con los instrumento s disponibles al momento de la auditoría es la pregunta

Taxonomía General de Aplicaciones

Nivel de

Pregunta del

caso Instrumento que la responde

certeza posible

técnica central.

¿El token emitido es un security — sujeto a la regulación de valores aplicable?

El análisis jurídico del test de Howey (EE.UU.) o los equivalentes en otras jurisdicciones: ¿es una inversión de capital en un esfuerzo común con expectativa de beneficio derivada del trabajo de otros? Este análisis es previo a cualquier análisis de responsabilidad y determina el marco regulatorio aplicable.

Declaración A o B si el análisis jurídico del instrumento está establecido por el regulador. Declaración C si el carácter del token como security está disputado en la jurisdicción aplicable.

¿Cuál es el D_total del esquema y el AD_i de cada nodo del grafo?

D_total = capital_captado_en_la_emisión − valor_residual_del_token_post_co lapso (para rug pulls y emisiones fraudulentas). D_total = capital_de_clientes_no_recuperad o (para insolvencia de exchange). D_total = valor_drenado_del_protocolo (para exploits). AD_i = R*_i × D_total para cada nodo del grafo.

Declaración B para el D_total cuando los datos on-chain permiten cuantificar los flujos. Declaración C para la distribución del AD_i entre los nodos cuando los R* requieren estimación con alta incertidumb re.

Taxonomía General de Aplicaciones

### §7  Traducción de D_total al dominio de la criptoeconomía

En el dominio

Compon

Cómo se cuantifica Fuente de

de la criptoecon

ente

evidencia

omía

T_inverti do (pérdida directa verificable on-chain)

El capital de los inversores perdido en el esquema, cuantificabl e on-chain con precisión: el valor en USD o en el activo de referencia del capital enviado al protocolo o al exchange, menos el valor recuperado o el valor residual del token.

D_capital = valor_USD_enviado − valor_residual_post_col apso. Calculable directamente desde el análisis forense on-chain usando los precios del activo en cada momento relevante (datos de exchange públicos).

Análisis forense on-chain CD2 de los flujos de fondos. Precios históricos del activo en plataforma s de datos de mercado (CoinGeck o, CoinMarke tCap, datos de exchange).

T_impedi do (oportuni dades perdidas durante el período del esquema)

La apreciación que el capital perdido habría producido en alternativas de inversión comparable s durante el período del

D_oportunidad = (rendimiento_alternativa _referencia − rendimiento_token) × capital_invertido × período. La alternativa de referencia (stablecoin en depósito, activo de menor riesgo) debe justificarse en el peritaje.

Datos históricos de rendimient o de alternativas de referencia. Análisis del período en que el inversor mantuvo su posición

Taxonomía General de Aplicaciones

En el dominio

Compon

Cómo se cuantifica Fuente de

de la criptoecon

ente

evidencia

omía

esquema. Para los inversores que mantuviero n el token bajo representac iones falsas de estabilidad: el diferencial de rendimient o entre el token y la alternativa de menor riesgo disponible.

por las representac iones del emisor.

ΔT_trayec toria (impacto permanen te en la confianza del mercado)

El daño a la confianza en los mercados de activos digitales producido por el esquema — reducción de la participació n de inversores en el ecosistema, mayores costos de capital para proyectos legítimos,

Análisis de los efectos del colapso sobre el volumen de mercado, la participación de inversores institucionales y el costo de capital de proyectos del sector en el período posterior. Siempre Declaración C.

Datos de mercado post-colapso. Estudios del sector sobre el impacto de eventos de confianza en los mercados de activos digitales.

Taxonomía General de Aplicaciones

En el dominio

Compon

Cómo se cuantifica Fuente de

de la criptoecon

ente

evidencia

omía

aumento de la fricción regulatoria para todo el sector. Es el component e más difícil de cuantificar y siempre Declaració n C.

D_vital_cripto = D_total / w_ref · La transparencia on-chain como fundamento de la cuantificación La transparencia on-chain hace que T_invertido en la criptoeconomía sea el componente mejor documentado de todos los dominios del libro cuando el análisis forense está disponible. Cada transacción tiene un timestamp, un valor y una dirección de origen y destino verificables y permanentes. El D_total de un exploit, un rug pull o una insolvencia de exchange puede calcularse con una precisión que pocos otros dominios alcanzan — no porque la criptoeconomía sea más transparente en sus intenciones, sino porque la blockchain hace públicos e irrevocables los registros de los movimientos de capital. La conversión D_vital = D_total / w_ref en este dominio tiene una particularidad: los inversores en activos digitales tienen perfiles de ingreso muy heterogéneos. Algunos son institucionales con alto nivel de sofisticación; otros son inversores minoristas que asignaron ahorros significativos a sus posiciones. El análisis debe distinguir el D_vital de los inversores minoristas (que puede representar una fracción significativa de su patrimonio y de sus horas de vida de trabajo) del D_vital de los inversores institucionales (que puede ser una fracción menor de un portafolio diversificado).

### §8  Límites del método y errores frecuentes de aplicación

Taxonomía General de Aplicaciones

Nota especial: el dominio más incierto del libro en términos regulatorios La criptoeconomía es el dominio donde el marco regulatorio aplicable es más incierto, más variado entre jurisdicciones y más cambiante en el tiempo. El análisis causal de la responsabilidad puede establecer quién tiene R* sobre el daño con relativa precisión usando los datos on-chain y off-chain disponibles. Pero la determinación de si ese R* se traduce en responsabilidad jurídica bajo la ley aplicable depende de qué marco regulatorio aplica (ley de valores, ley de servicios financieros, ley de commodities, regulación específica de activos digitales) y eso varía significativamente entre jurisdicciones. El analista debe ser especialmente explícito sobre esta incertidumbre jurisdiccional al usar este capítulo en una pretensión formal.

Límites del método en el dominio de la criptoeconomía

Límite 1 — La pseudonimidad de los actores. La blockchain registra públicamente las transacciones de las carteras, pero la identidad de los titulares de las carteras no siempre es verificable. El análisis forense on-chain puede rastrear los flujos de fondos con alta precisión, pero la vinculación de las carteras on-chain con identidades reales requiere KYC del exchange que custodió la cartera, cooperación de exchanges con los investigadores o análisis de cluster de carteras. Sin esa vinculación, el grafo causal puede estar incompleto en la identidad de los actores.

Límite 2 — La distinción entre proyecto fallido y fraude. La frontera entre el equipo fundador que diseñó un proyecto genuinamente pero que fracasó por razones de mercado y el equipo que diseñó un esquema de captación fraudulenta es difícil de establecer retrospectivamente cuando los fundadores no se enriquecieron deliberadamente a expensas de los inversores. El análisis del patrón de ventas de tokens de los insiders on-chain es el instrumento más robusto para esta distinción, pero tiene limitaciones cuando los fundadores también perdieron significativamente en el colapso.

Límite 3 — La velocidad de evolución del dominio. Los protocolos, los mecanismos de ataque y los estándares de

Taxonomía General de Aplicaciones

seguridad en el ecosistema de activos digitales evolucionan rápidamente. El análisis de la detectabilidad de una vulnerabilidad de smart contract al momento de la auditoría debe ser especialmente preciso sobre qué instrumentos de auditoría estaban disponibles y cuáles eran los estándares de la industria en ese momento específico — no los del momento del análisis.

Límite 4 — La jurisdicción aplicable y la fragmentación regulatoria. El dominio es el más fragmentado del libro en términos de regulación aplicable. Un protocolo puede ser operado desde una jurisdicción, los inversores pueden estar en múltiples países, el smart contract está en una blockchain sin jurisdicción territorial. La determinación de qué ley aplica y qué regulador tiene jurisdicción es frecuentemente la pregunta más difícil del análisis, anterior al análisis de responsabilidad causal.

### Errores frecuentes de aplicación

Error Por qué

Consec

uencia Corrección

ocurre

Atribuir el daño del exploit al smart contract como "fallo técnico" sin incluir al diseñad or del protoco lo y al auditor

El smart contract ejecutó su código — el exploit es visible como "el smart contract fue hackead o".

R* del arquitec to del tokeno mics y del auditor = 0 aunque el diseño del protocol o y el proceso de auditorí a fueron

El smart contract tiene S ≈ 1.0 — cualquier instancia del mismo código en las mismas condiciones habría producido el mismo exploit. R* del smart contract apunta al diseñador del protocolo y al auditor. La reforma correcta: diseño más robusto y auditorías múltiples con los vectores de ataque documentados.

Taxonomía General de Aplicaciones

Error Por qué

Consec

uencia Corrección

ocurre

las condicio nes del exploit.

Usar el precio pico del token como base del D_total en lugar del precio de compra del inversor

El D_total es más llamativ o usando el precio máximo del token, que puede estar muy por encima del precio de compra del inversor.

D_total sobreest imado. El inversor que compró el token a $0.01 y lo vendió a $0.005 no tiene el mismo D_total que el que compró a $1.

D_total por inversor = valor_en_moneda_de_referencia _al_momento_de_la_compra − valor_recuperado_al_momento_ de_la_salida. El D_total del esquema no es la capitalización de mercado en el pico: es el capital real de los inversores perdido.

Tratar el proyect o fallido como equivale nte al rug pull sin analizar el patrón de ventas de los insiders

El analista concluye fraude porque el proyecto fracasó y los inversor es perdiero n, sin analizar si los fundado res se enriquec ieron delibera

Culpabil idad sobreest imada del fundado r. El proceso penal puede no prosper ar si la evidenci a del enriquec imiento delibera do no está

El análisis del patrón de ventas de tokens de los fundadores on-chain antes del colapso es el instrumento central para esta distinción: ¿los fundadores vendieron sus tokens antes de que el proyecto colapsara en un patrón que sugiere conocimiento previo, o perdieron ellos también? Si los fundadores también perdieron, el proyecto fallido tiene un perfil distinto al del rug pull.

Taxonomía General de Aplicaciones

Error Por qué

Consec

uencia Corrección

ocurre

damente .

estableci da.

Ignorar la respons abilidad del auditor de segurida d cuando el exploit usó un vector docume ntado en la literatur a

El análisis identific a al atacante y al equipo fundado r como responsa bles sin incluir al auditor que emitió el informe de segurida d previo al exploit.

R* del auditor = 0 aunque emitió una certifica ción de segurida d para un contrato con una vulnera bilidad detectab le con los estándar es disponi bles.

S del auditor es moderado-bajo cuando el vector de ataque estaba documentado en la literatura de seguridad de smart contracts al momento de la auditoría. El auditor tiene R* sobre el daño del exploit proporcional a la detectabilidad de la vulnerabilidad y a la escala del capital que su certificación permitió exponer.

### §9  Guía de prioridades de recolección de evidencia

Nota de uso obligatoria: todas las estimaciones de este capítulo son Nivel C. La primera decisión siempre es identificar el mecanismo del caso: rug pull / emisión fraudulenta, colapso del protocolo (stablecoin o DeFi), insolvencia del exchange, o exploit de smart contract. Cada mecanismo tiene instrumentos y prioridades de evidencia radicalmente distintos.

### Tabla de prioridades de recolección de evidencia en criptoeconomía y activos digitales

Taxonomía General de Aplicaciones

Si tu incertid

Qué buscar

Por qué funcion

Qué rango reduce

La evidencia que más la reduce es…

umbre princip

/ qué pregunt

a

al es…

ar

### 1. ¿El mecanis mo del caso — rug pull, colapso de protocol o, insolven cia de exchang e, o exploit?

Análisis forense on-chain CD2 de los flujos de fondos en el período del colapso: ¿los fondos salieron del protocolo a carteras de los fundadores (rug pull), el mecanismo de estabilización falló bajo su propia lógica (colapso de protocolo), los fondos de clientes no estaban segregados (exchange), o fondos fueron drenados por una transacción de ataque (exploit)?

Cada mecanis mo tiene un grafo de respons abilidad distinto y evidenci as prioritar ias distintas . La confusi ón entre mecanis mos produce evidenci a relevant e para uno pero no para el que determi na R*.

Determ ina el instrum ento princip al del análisis

¿Los fondos salieron del protocol o a carteras controla das por los fundado res? ¿El mecanis mo de estabiliz ación del stablecoi n entró en espiral? ¿El exchang e tiene proof of reserves que no cuadra? ¿Hay una transacci ón de exploit identific able on-chain?

### 2. [RUG PULL] ¿Los fundado res vendiero

Análisis forense on-chain CD1/CD2 del patrón de ventas de tokens de las carteras de los fundadores en el

El patrón de ventas de insiders

Reduce rango de S del fundad or (incerti

¿Las carteras de los fundado res vendiero

Taxonomía General de Aplicaciones

Si tu incertid

Qué buscar

Por qué funcion

Qué rango reduce

La evidencia que más la reduce es…

umbre princip

/ qué pregunt

a

al es…

ar

n sus tokens antes del colapso en un patrón de insider?

período previo al colapso: ¿las ventas de los insiders precedieron al colapso por días o semanas en un patrón estadísticamente incompatible con ventas de mercado normales?

antes del colapso es la señal on-chain más robusta para establec er Anteros del fundado r. Es el instrum ento que discrimi na el rug pull del proyect o fallido sin malicia.

dumbre ontológ ica crítica)

n tokens en los días/se manas previos al colapso? ¿El volumen de ventas de las carteras de insiders era estadísti camente anómalo versus el período anterior? ¿Los fondos de las ventas fueron enviados a exchang es o a carteras de mezcla?

### 3. [COLAP SO DE PROTO COLO] ¿El mecanis mo de

Peritaje técnico del tokenomics CD2: análisis del mecanismo bajo distintos escenarios de estrés. ¿Habían señales en la literatura o en el

La fragilida d estructu ral del mecanis mo es el instrum

Reduce rango de R* del arquitec to del tokeno mics

¿Habían artículos o posts en el ecosiste ma sobre la fragilida

Taxonomía General de Aplicaciones

Si tu incertid

Qué buscar

Por qué funcion

Qué rango reduce

La evidencia que más la reduce es…

umbre princip

/ qué pregunt

a

al es…

ar

estabiliz ación era estructur almente viable?

ecosistema sobre la fragilidad del mecanismo antes del colapso?

ento que establec e si el colapso era previsib le dado el diseño — y por tanto si el diseñad or tenía R* con S bajo.

(incerti dumbre empíric a)

d del mecanis mo antes del colapso? ¿Otros stablecoi ns con mecanis mos similares habían colapsad o antes? ¿El análisis del mecanis mo bajo condicio nes de estrés produce espiral de muerte predecib le?

### 4. [EXCH ANGE] ¿Los fondos de clientes estaban segregad os de los fondos propios?

Análisis forense on-chain CD1/CD2 de los flujos entre las carteras del exchange y las carteras de entidades relacionadas: ¿hay transferencias entre las carteras de custodia de clientes y las carteras de trading propio o de entidades afiliadas sin justificación de

La segregac ión de fondos es la obligaci ón central del exchang e de custodia . Su verificac

Estable ce la mezcla de fondos (incerti dumbre empíric a central)

¿Hay transfere ncias docume ntadas on-chain entre las carteras de custodia del exchang e y las carteras

Taxonomía General de Aplicaciones

Si tu incertid

Qué buscar

Por qué funcion

Qué rango reduce

La evidencia que más la reduce es…

umbre princip

/ qué pregunt

a

al es…

ar

servicio a los clientes?

ión on-chain es el instrum ento más directo para establec er la mezcla de fondos.

de Alameda Researc h o equivale ntes? ¿El proof of reserves publicad o correspo ndía al capital realment e custodia do?

### 5. [EXPL OIT] ¿El vector de ataque estaba docume ntado en la literatura de segurida d al moment o de la auditoría ?

Análisis técnico CD2 de la vulnerabilidad explotada versus el estado de la literatura de seguridad de smart contracts al momento de la auditoría. ¿El vector (reentrancy, flash loan, price oracle manipulation) estaba documentado en los estándares de auditoría disponibles?

La detectab ilidad del vector determi na S del auditor — y por tanto cuánto del R* del exploit le corresp onde al auditor versus al atacante .

Estable ce R* del auditor (incerti dumbre técnica)

¿Cuándo fue docume ntado el vector de ataque en la literatur a de segurida d de smart contract s? ¿Otros auditore s con estándar es similares lo incluían en sus proceso

Taxonomía General de Aplicaciones

Si tu incertid

Qué buscar

Por qué funcion

Qué rango reduce

La evidencia que más la reduce es…

umbre princip

/ qué pregunt

a

al es…

ar

s al moment o de la auditoría del protocol o explotad o? ¿El informe de auditoría analiza explícita mente este tipo de vector?

### 6. ¿El token emitido califica como security en la jurisdicci ón aplicable ?

Análisis jurídico del instrumento (previo al análisis de responsabilidad): aplicación del test de Howey (EE.UU.) o el equivalente regulatorio de la jurisdicción aplicable. Este análisis determina qué marco legal aplica y qué regulador tiene jurisdicción.

Sin determi nar el marco regulato rio aplicabl e, el análisis de respons abilidad no puede establec er qué obligaci ones tenía el emisor y cuáles incumpl ió.

Determ ina el marco legal aplicabl e (incerti dumbre jurisdic cional)

¿Los compra dores del token tenían expectat iva razonabl e de benefici o derivada del trabajo del equipo emisor? ¿El token otorga derecho s económi

Taxonomía General de Aplicaciones

Si tu incertid

Qué buscar

Por qué funcion

Qué rango reduce

La evidencia que más la reduce es…

umbre princip

/ qué pregunt

a

al es…

ar

cos sobre los resultad os del protocol o? ¿El regulado r de valores de la jurisdicc ión aplicable se ha pronunc iado sobre tokens similares ?

### 7. ¿Cuál es el D_total y el AD_i de cada nodo del grafo?

D_total = valor_capital_perdid o_verificable_on-chain. AD_i = R*_i × D_total para cada nodo del grafo. Los R* son estimaciones Nivel C que deben declararse con incertidumbre explícita.

Sin el D_total cuantifi cado y los AD_i estimad os, la pretensi ón de respons abilidad no tiene base calculad a.

Estable ce la escala de la pretensi ón (incerti dumbre empíric a)

¿Cuánto capital total enviaron los inversor es al protocol o o al exchang e? ¿Cuánto recupera ron? ¿Qué fracción del daño total es atribuibl e a cada actor del

Taxonomía General de Aplicaciones

Si tu incertid

Qué buscar

Por qué funcion

Qué rango reduce

La evidencia que más la reduce es…

umbre princip

/ qué pregunt

a

al es…

ar

grafo dado el análisis de R*?

### Árbol de decisión en criptoeconomía y activos digitales

El árbol comienza con la identificación del mecanismo del caso, porque cada mecanismo tiene un grafo de responsabilidad, evidencias prioritarias y prioridades de reforma completamente distintos.

¿Cuál es el mecanismo principal del caso?

├─ Mecanismo A: RUG PULL / EMISIÓN FRAUDULENTA │

└─  PRIORIDAD 1: Análisis forense on-chain del patrón de ventas de tokens de los insiders.

· ¿Los insiders vendieron antes del colapso en patrón estadísticamente anómalo? · Si sí → Anteros del fundador, S bajo. Proceso penal viable si el marco regulatorio aplica.

├─ Mecanismo B: COLAPSO DE PROTOCOLO (stablecoin o DeFi) │

└─  PRIORIDAD 1: Peritaje técnico del tokenomics — ¿era estructuralmente viable?

· Si la fragilidad era previsible → R* del arquitecto del tokenomics es alto, S bajo.

Taxonomía General de Aplicaciones

· Si el conocimiento de la fragilidad no estaba disponible → Deimos dominante, S alto.

├─ Mecanismo C: INSOLVENCIA DEL EXCHANGE (CEX) │

└─  PRIORIDAD 1: Análisis forense on-chain de flujos entre carteras de custodia y carteras propias.

· Aplicar instrumentos del cap. 12 (insolvencia) y cap. 13 (gobierno corporativo) al exchange.

└─ Mecanismo D: EXPLOIT DE SMART CONTRACT

├─  PRIORIDAD 1: ¿El vector era conocido en la literatura — S del auditor?

· Si sí → R* del auditor es positivo. AD_auditor = R*_auditor × D_total_exploit.

└─  PRIORIDAD 2: ¿El diseño del protocolo contemplaba el vector de ataque?

· Si no → R* del arquitecto del tokenomics positivo sobre el diseño que lo hizo posible.

— Fin del Capítulo 20 — Centro Multidisciplinario Meriadock Formación y Asesoría A.C.  · 2026

Taxonomía General de Aplicaciones

