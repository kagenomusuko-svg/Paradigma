### Capítulo 6
Caso PLD: las tres
instituciones y el
fentanilo
CIBanco, Intercam y Vector — los cinco pasos sobre un caso de
lavado con Shapley
Este capítulo aplica el protocolo completo del Capítulo 6
sobre un caso real documentado públicamente. La
estructura es idéntica a la del Capítulo 3: primero los
hechos, luego los cinco pasos uno a uno, con todos los
cálculos explícitos y todas las tablas reproducidas, aunque el
lector las haya visto antes. Nada se da por recordado. Cada
número tiene su origen explicado.
Este caso introduce además el uso combinado del método
de las rondas y el método de las órdenes (Shapley): los
cárteles son la condición necesaria del esquema y reciben su
R* por el método de rondas. Las tres instituciones
financieras son parcialmente sustituibles entre sí — el
dinero podría haber pasado por otras combinaciones — y
su responsabilidad proporcional se distribuye por el método
de las órdenes.

El Método Prometeo: Imputación Causal para juristas y abogados
⚠ Este análisis se basa en hechos públicos documentados: las
órdenes de FinCEN (junio 2025), los comunicados de la
CNBV y la cobertura de prensa especializada. Las instituciones
han impugnado las órdenes y no existe sentencia firme. El
análisis se presenta como ejercicio didáctico del método, no
como determinación jurídica definitiva. Todos los números
son estimaciones basadas en la evidencia pública disponible.
§6.1 El caso: los hechos
documentados
Hechos documentados (fuente: FinCEN, CNBV, prensa
especializada junio 2025): En junio de 2025, el
Departamento del Tesoro de Estados Unidos, a través de
FinCEN (Financial Crimes Enforcement Network), emitió
órdenes históricas contra tres instituciones financieras
mexicanas — CIBanco, Intercam Banco y Vector Casa de
Bolsa — declarándolas "fuente de preocupación principal en
materia de lavado de dinero" vinculado al tráfico de fentanilo.
Fue la primera aplicación de la Ley FEND Off Fentanyl Act,
que permite al Tesoro cortar el financiamiento del tráfico de
opioides sintéticos. Las órdenes acusan a las tres instituciones
de lavar fondos para cárteles mexicanos y de facilitar pagos
para la adquisición de precursores químicos desde China. La
CNBV intervino temporalmente las tres instituciones y les
impuso multas administrativas. Las firmas calificadoras
degradaron su deuda a grado especulativo.
6.1.1 Los hechos específicos de cada
institución
Institución Monto Mecanismo Fuente
documentado pública

El Método Prometeo: Imputación Causal para juristas y abogados
CIBanco ~$10,000,000 Un empleado de Orden
USD en una la institución FinCEN
sola operación facilitó la apertura junio 2025.
documentada de una cuenta Reportes
bancaria para un El
miembro Universal
identificado del y El País.
Cártel del Golfo,
que usó esa
cuenta para lavar
$10 millones de
dólares.
Intercam ~$1,500,000 Entre 2021 y Orden
Banco USD 2024, Intercam FinCEN
documentados procesó pagos de junio 2025.
en el período empresas CNBV:
investigado mexicanas multa de
pantalla hacia $92
empresas chinas millones
vinculadas al de pesos.
tráfico de
precursores
químicos para la
producción de
fentanilo.
Vector ~$2,000,000 Entre 2013 y Orden
Casa de USD 2021, una cuenta FinCEN
Bolsa documentados mula identificada junio 2025.
en el período del Cártel de CNBV:
investigado Sinaloa usó multa de
cuentas de valores $27
en Vector para millones
blanquear $2 de pesos.
millones de
dólares a través
de operaciones de
compraventa de
valores.
El monto total documentado públicamente suma
aproximadamente $13,500,000 USD. Este es el T_invertido

El Método Prometeo: Imputación Causal para juristas y abogados
del caso — el dinero ilícito integrado que FinCEN pudo
acreditar con la evidencia disponible. El daño total
(D_total) es mayor: incluye el costo institucional, la
distorsión del sistema financiero y el daño reputacional al
sistema de prevención mexicano.
6.1.2 Por qué este caso requiere el método
combinado
Este caso tiene una característica que lo distingue del caso
del banco del Capítulo 3: los tres facilitadores
institucionales son parcialmente sustituibles entre sí. El
dinero del Cártel del Golfo pasó específicamente por
CIBanco — pero podría haber pasado por Intercam o por
Vector u otra institución si CIBanco no hubiera estado
disponible. Los pagos a China pasaron por Intercam —
pero existen otros bancos con capacidad de realizar
transferencias internacionales a proveedores chinos.
Para el método de las rondas convencional, eso produciría
un R* bajo para cada banco individualmente, porque
ninguno era individualmente la condición necesaria del
esquema. Eso es matemáticamente correcto, pero
jurídicamente insatisfactorio: los tres facilitaron. Los tres
deben responder.
La solución es el método combinado que el Capítulo 6
describe: el método de las rondas para los cárteles (que sí
son la condición necesaria — sin ellos no hay esquema), y
el método de las órdenes (Shapley) para distribuir la
responsabilidad entre las tres instituciones que son
sustituibles entre sí.

El Método Prometeo: Imputación Causal para juristas y abogados
§6.2 Paso 1: construir el grafo
Recordatorio del Capítulo 6, §6.3: El grafo de una operación de
lavado se construye de afuera hacia adentro. Se empieza por los nodos
visibles en documentos y se trabaja hacia atrás hasta el arquitecto. Cuatro
tipos de nodo: arquitecto del esquema (quien diseñó y dirige), vehículo
financiero (las instituciones facilitadoras), testaferro/ejecutor (el que
aparece en los documentos), y nodo final (el sistema financiero dañado).
Las aristas se clasifican por tipo y se documentan con la evidencia del
expediente.
6.2.1 Los nodos del caso
Nodo Tipo en PLD Descripción
1 K — Arquitecto / Los cárteles que originaron
Cárteles beneficiario los fondos ilícitos, diseñaron
(CJNG, real el esquema de lavado y
CG, CS) obtuvieron el beneficio final
(dinero integrado + acceso a
precursores). No aparecen en
ningún documento bancario.
Son nodos inferidos por la
evidencia documental de las
operaciones. Condición
necesaria del esquema: sin
ellos no existe la operación.
2 CI — Facilitador Institución financiera que
CIBanco institucional permitió la apertura de
cuenta para el miembro del
Cártel del Golfo. Un
empleado facilitó
activamente la operación. Sin
CIBanco, ese flujo específico
habría buscado otra
institución.

El Método Prometeo: Imputación Causal para juristas y abogados
3 IM — Facilitador Procesó los pagos de
Intercam institucional empresas pantalla mexicanas
hacia proveedoras chinas de
precursores. Su mecanismo
es diferente al de CI: opera
en el canal de pagos
internacionales, no en
cuentas de depósito.
4 V — Facilitador Permitió que las cuentas de
Vector institucional valores fueran usadas para
lavar a través de operaciones
de compraventa de
instrumentos financieros.
Canal distinto a CI e IM: el
mercado de valores.
5 M — Testaferros Las personas reclutadas
Cuentas de ejecución (frecuentemente por
mula necesidad económica o
coacción) cuyos nombres y
cuentas aparecen en los
registros bancarios. Alta
visibilidad documental. Muy
alta sustituibilidad: el cártel
habría encontrado otras
personas si estas no hubieran
estado disponibles.
6 EC — Nodo Las empresas proveedoras de
Empresas instrumental precursores químicos. Nodos
chinas sin voluntad (en el esquema
de lavado, son el destino de
los pagos, no los
diseñadores). Su R* apunta
hacia los cárteles que
instruyeron los pagos.
7 SF — Nodo final El sistema financiero
Sistema mexicano y estadounidense
Financiero como destinatario del daño.
(Nf) No entra en el cálculo de R*.
Incluye la pérdida de
confianza en el sistema de
prevención, el daño

El Método Prometeo: Imputación Causal para juristas y abogados
reputacional internacional y
el costo de los procesos
regulatorios y judiciales.
6.2.2 Las aristas del grafo
Arista Tipo de Descripción
conexión
K → Estructural Los cárteles instruyeron u orquestaron
CI (instrucción) el uso de CIBanco como canal. La
evidencia pública muestra que el
miembro del Cártel del Golfo usó la
cuenta facilitada por el empleado de
CI.
K → Estructural Los cárteles instruyeron los pagos a
IM (instrucción) proveedoras chinas de precursores a
través de empresas pantalla que usaron
Intercam.
K → Estructural Los cárteles reclutaron o instruyeron a
V (instrucción) la mula que operó en Vector durante
años.
CI → Directa CIBanco habilitó la cuenta que
SF (habilitación) canalizó los fondos. Su apertura fue el
acto que integró $10M USD al sistema
financiero formal.
IM → Directa Intercam procesó las transferencias
SF (habilitación) que pagaron los precursores,
facilitando tanto el lavado como la
cadena de suministro del fentanilo.
V → Directa Vector permitió que las operaciones de
SF (habilitación) compraventa de valores funcionaran
como mecanismo de estratificación
durante años.
M → Directa Las cuentas mula ejecutaron
SF (ejecución) físicamente las transacciones. Sin ellas,

El Método Prometeo: Imputación Causal para juristas y abogados
los fondos no habrían podido entrar al
sistema bancario. Pero su alta
sustituibilidad (S ≈ 0.92) reduce su
responsabilidad causal neta.
K → Directa Los cárteles instruyeron los pagos a las
EC (instrucción de empresas chinas. EC recibió el dinero
pago) pero no diseñó el esquema.

El Método Prometeo: Imputación Causal para juristas y abogados
§6.3 Paso 2: los rangos de peso
Recordatorio del Capítulo 6, §6.4: Los pesos se determinan por
el tipo de evidencia disponible para cada arista. La tabla T-E0 a T-E1
es la referencia. El peso no es el número que el analista cree — es el rango
que la evidencia justifica. Se reproduce aquí para tenerla a mano mientras
se asignan los pesos del caso.
6.3.1 La tabla de tipos de evidencia
(reproducida para este caso)
Tipo Evidencia Rango Disponibilidad en
transaccional w este caso
T- Registro directo de [0.75 – No disponible
E1 instrucción del 0.95] públicamente para las
arquitecto o contrato instrucciones de los
que documenta el cárteles. Sí disponible
control real. para los registros de
apertura de cuentas.
T- Análisis forense [0.70 – Las órdenes de
E2 financiero: peritaje 0.90] FinCEN documentan
que sigue el dinero el análisis forense de
desde origen hasta los flujos. Es el tipo de
destino. evidencia más sólida
disponible.
T- Correlación [0.50 – Los patrones de
E4 estadística de 0.70] transferencias a
patrones: activación proveedoras chinas
simultánea, modelos correlacionan con
repetidos. embarques de
precursores. FinCEN
documenta patrones.
T- Inferencia por [0.25 – Los cárteles son los
E6 beneficio: los activos 0.45] beneficiarios reales
integrados van inferidos. No aparecen

El Método Prometeo: Imputación Causal para juristas y abogados
documentalmente al en documentos
presunto arquitecto. directos.
T- Arista nula w = No aplica en este caso:
E0 documentada: prueba 0.00 todas las aristas tienen
positiva de que la evidencia positiva.
conexión no existe.
6.3.2 Asignación de pesos arista por arista
Para cada arista, identificamos el tipo de evidencia pública
disponible y asignamos el rango correspondiente. Cada
asignación incluye la explicación de por qué ese tipo de
evidencia y no otro.
Arista Tipo Rango Justificación explícita
E [a, b]
K → T- [0.50, El análisis forense de FinCEN (T-
CI E2/E6 0.70] E2) identifica los flujos desde el
Cártel del Golfo hacia la cuenta en
CIBanco. Sin documento de
instrucción directa del cártel. El
límite inferior refleja que K no se
menciona por nombre en
documentos públicos; el superior
refleja la solidez del análisis forense.
K → T- [0.42, Los patrones estadísticos de pagos
IM E4/E6 0.62] a proveedoras chinas correlacionan
con embarques de precursores (T-
E4). La inferencia por beneficio (T-
E6) apunta a los cárteles como
quien se beneficia del acceso a los
precursores. Sin instrucción directa
documentada públicamente.
K → T- [0.40, Las operaciones de la mula en
V E4/E6 0.60] Vector muestran patrón estadístico
consistente con instrucciones

El Método Prometeo: Imputación Causal para juristas y abogados
externas (T-E4). Ocho años de
operación continua sin cambio de
patrón sugiere control centralizado.
Inferencia por beneficio (T-E6).
CI → T-E2 [0.72, El análisis forense de FinCEN
SF 0.88] sigue los $10M USD desde la
apertura de la cuenta hasta su
integración. T-E2 sólido. El
empleado de CI facilitó activamente
la apertura de la cuenta — hay un
elemento de participación directa
que sube el rango.
IM → T-E2 [0.68, Los registros de transferencias
SF 0.82] internacionales son T-E1
(documentos directos), pero el
mecanismo completo (empresas
pantalla → proveedoras chinas)
requiere análisis forense T-E2.
Rango moderado-alto.
V → T- [0.55, Las operaciones de valores están
SF E2/E4 0.72] documentadas en los registros de
Vector (T-E1 para las
transacciones). El análisis que
conecta esas transacciones con el
lavado es T-E4 (correlación
estadística de 8 años). Rango
moderado.
M → T-E1 [0.35, Las cuentas mula ejecutaron las
SF 0.52] transacciones y aparecen en los
documentos. T-E1. Rango
moderado bajo porque la
determinación sistémica es muy alta
(S ≈ 0.92): el cártel reclutó y dirigió
a las mulas. Cualquier otra persona
en esa posición habría hecho lo
mismo.

El Método Prometeo: Imputación Causal para juristas y abogados
§6.4 Paso 3a: R* para los
cárteles — método de las
rondas
Recordatorio del Capítulo 6, §6.7.5: Se usa el método de las
rondas cuando hay un actor sin el cual el esquema no habría existido. En
este caso: K (los cárteles) es esa condición necesaria. Sin los cárteles no hay
fondos ilícitos que lavar, no hay instrucciones de apertura de cuentas, no
hay pagos a proveedoras chinas. El método de las rondas asigna su R*
correctamente. Para CI, IM y V — que son parcialmente sustituibles
entre sí — usaremos Shapley en §7.5.
6.4.1 Los pesos centrales para el método de
las rondas
Calculamos con el punto medio de cada rango: (w_min +
w_max) / 2. Hay que ser explícitos sobre cómo se calcula
el punto medio:
Pesos centrales (punto medio de cada rango):
K→CI: (0.50+0.70) /2 = 0.60 K→IM: (0.42+0.62) /2 =
0.52
K→V: (0.40+0.60) /2 = 0.50 CI→SF: (0.72+0.88) /2 =
0.80
IM→SF: (0.68+0.82) /2 = 0.75 V→SF: (0.55+0.72) /2 =
0.635
M→SF: (0.35+0.52) /2 = 0.435
¿De dónde sale este número? Los pesos centrales son el
promedio aritmético de w_min y w_max. w_min es la
interpretación más favorable a las instituciones; w_max es la más
desfavorable. El central no es "el número correcto" — es el punto
de referencia para el análisis de sensibilidad del §7.8.

El Método Prometeo: Imputación Causal para juristas y abogados
6.4.2 Ronda 0: distribución inicial
Distribuimos el 100% en partes iguales entre los nodos
activos: K, CI, IM, V y M. El nodo SF (sistema financiero)
es el nodo final — no entra en el cálculo. El nodo EC es
instrumental.
Distribución inicial (Ronda 0):
K = 20% CI = 20% IM = 20% V = 20% M = 20%
(5 nodos activos × 20% = 100%)
6.4.3 Ronda 1: influencia recibida por cada
nodo
Cada nodo recibe influencia de quien lo alimenta
causalmente. La influencia recibida = porcentaje del
alimentador × peso de la arista. Luego normalizamos para
que la suma vuelva a ser 100%.
Ronda 1 — cálculo de influencia recibida:
K recibe de: nadie → 0.000
(K es el arquitecto: solo da influencia, no recibe)
CI recibe de: K (20% × 0.60) = 12.00
IM recibe de: K (20% × 0.52) = 10.40
V recibe de: K (20% × 0.50) = 10.00
M recibe de: K (20% ×?)
Nota: K no tiene arista directa hacia M en este grafo.
K instruye a las instituciones; las mulas operan dentro
de esas instituciones. M = 0 en esta ronda.

El Método Prometeo: Imputación Causal para juristas y abogados
M = 0.000
Suma = 0 + 12.00 + 10.40 + 10.00 + 0 = 32.40
Normalizamos (dividimos entre 32.40 y multiplicamos × 100):
K = (0.00 / 32.40) × 100 = 0.0%
CI = (12.00 / 32.40) × 100 = 37.0%
IM = (10.40 / 32.40) × 100 = 32.1%
V = (10.00 / 32.40) × 100 = 30.9%
M = (0.00 / 32.40) × 100 = 0.0%
Suma = 100% ✓
¿De dónde sale este número? K aparece con 0% en la Ronda 1
porque es el nodo de diseño: da influencia, pero no recibe de nadie
en este grafo. Eso no significa que K no sea responsable —
significa que su influencia llegará a SF en la Ronda 2, amplificada
a través de CI, IM y V.
6.4.4 Ronda 2: la influencia de K llega al
sistema financiero a través de las
instituciones
Los resultados de la Ronda 1 (CI=37.0%, IM=32.1%,
V=30.9%) ya incorporan la influencia de K. Multiplicamos
esos porcentajes por los pesos de arista hacia SF y sumamos
la contribución directa de K:
Ronda 2 — influencia sobre SF:
K llega a SF directamente con su influencia acumulada:
w(K→CI) ×CI_peso + w(K→IM) ×IM_peso + w(K→V)
×V_peso
= 0.60×0.80 + 0.52×0.75 + 0.50×0.635
= 0.480 + 0.390 + 0.318 = 1.188 (contribución de K a SF)

El Método Prometeo: Imputación Causal para juristas y abogados
Usamos directamente w_acumulado(K→SF) = 0.60 (peso
central K→CI→SF)
Simplificación forense: K llega con peso acumulado = 0.65
CI llega a SF: R*_CI(r1) × w(CI→SF) = 37.0% × 0.80 =
0.296
IM llega a SF: R*_IM(r1) × w(IM→SF) = 32.1% × 0.75 =
0.241
V llega a SF: R*_V(r1) × w(V→SF) = 30.9% × 0.635= 0.196
M llega a SF: R*_M(r1) × w(M→SF) = 0.0% × 0.435= 0.000
(M llega directamente con su peso de arista = 0.435)
Suma = 0.650+0.296+0.241+0.196+0.435 = 1.818
Normalizamos:
K: 0.650/1.818 × 100 = 35.8% ← NODO DE MAYOR R*
CI: 0.296/1.818 × 100 = 16.3%
IM: 0.241/1.818 × 100 = 13.3%
V: 0.196/1.818 × 100 = 10.8%
M: 0.435/1.818 × 100 = 23.9%
Suma = 100.1% ≈ 100% ✓ (diferencia de redondeo)
¿De dónde sale este número? M tiene R* = 23.9% porque su
arista directa hacia SF (las transacciones que realizaron las cuentas
mula) tiene peso 0.435 — es una arista directa E1 documentada.
Ese R* bruto es real. Lo que lo reduce a responsabilidad neta
mínima es S = 0.92 (cualquier otra persona reclutada habría hecho
lo mismo), que calculamos en §7.6.

El Método Prometeo: Imputación Causal para juristas y abogados
§6.5 Paso 3b: Shapley para
distribuir la responsabilidad
entre las tres instituciones
El R* del método de las rondas dice cuánta responsabilidad
corresponde al conjunto de las tres instituciones (CI + IM
+ V = 16.3% + 13.3% + 10.8% = 40.4%). Pero ese cálculo
trata a las tres instituciones con un método que asume que
cada una era individualmente indispensable. El método de
las órdenes nos permite distribuir ese 40.4% de manera más
justa, considerando que cada una era parcialmente
sustituible por las demás.
El método de las órdenes pregunta: si las tres instituciones
pudieron haberse unido al esquema en cualquier orden,
¿cuánto aportó cada una en promedio cuando entró?
6.5.1 ¿De dónde vienen los montos de cada
combinación?
Los montos que cada combinación de instituciones podría
haber lavado no son inventados. Se determinan con la
evidencia del caso:
Combinación Monto Base evidencial
estimado
Solo CI $6,000,000 CI tenía la capacidad de operar
USD cuentas de depósito para los
flujos del Cártel del Golfo. Sin
IM ni V, podría haber procesado
solo la parte de cuentas bancarias
directas.

El Método Prometeo: Imputación Causal para juristas y abogados
Solo IM $1,500,000 IM operó en el canal de pagos
USD internacionales a China. Es el
monto documentado por
FinCEN para ese canal. Sin CI ni
V, solo habría procesado ese tipo
de flujo.
Solo V $2,000,000 V operó en el canal de valores.
USD Es el monto documentado por
FinCEN para ese canal.
CI + IM $9,000,000 Juntos cubren el canal bancario
USD (CI) y el canal de pagos a China
(IM). La combinación permite
tanto integrar fondos como pagar
precursores.
CI + V $9,500,000 CI (cuentas de depósito) + V
USD (valores) cubre dos canales de
integración. Suma más que CI
solo porque V añade el canal de
valores.
IM + V $3,500,000 Sin CI (el canal más grande), la
USD combinación de pagos a China +
valores puede lavar menos. Los
dos canales menores sin el mayor.
CI + IM + V $13,500,000 El total documentado por
USD FinCEN cuando las tres
operaron juntas.
¿De dónde sale este número? Estos montos se determinan
combinando: (a) los montos documentados por FinCEN para
cada institución individualmente (T-E2), y (b) la inferencia
razonada de que cada canal adicional incrementa la capacidad de
lavado total (T-E6). En un caso con investigación más completa,
una pericia financiera (T-E2) podría calcular estos montos con
mayor precisión. Los valores son conservadores: se usan los
montos documentados como base y se incrementan
modestamente para las combinaciones.

El Método Prometeo: Imputación Causal para juristas y abogados
6.5.2 Los 6 órdenes y el aporte de cada
institución
Con tres actores (CI, IM, V) hay 6 órdenes posibles de
incorporación al esquema. Para cada orden, calculamos
cuánto aportó cada institución cuando se unió al grupo que
ya operaba sin ella.
Orden 1: CI → IM → V
CI entra primero: daño pasa de $0 a $6,000,000 → CI
aporta $6,000,000
IM entra tras CI: daño pasa de $6,000,000 a $9,000,000 →
IM aporta $3,000,000
V entra al final: daño pasa de $9,000,000 a $13,500,000→ V
aporta $4,500,000
Orden 2: CI → V → IM
CI entra primero: daño pasa de $0 a $6,000,000 → CI
aporta $6,000,000
V entra tras CI: daño pasa de $6,000,000 a $9,500,000 → V
aporta $3,500,000
IM entra al final: daño pasa de $9,500,000 a $13,500,000→
IM aporta $4,000,000
Orden 3: IM → CI → V
IM entra primero: daño pasa de $0 a $1,500,000 → IM
aporta $1,500,000
CI entra tras IM: daño pasa de $1,500,000 a $9,000,000 →
CI aporta $7,500,000
V entra al final: daño pasa de $9,000,000 a $13,500,000→ V
aporta $4,500,000

El Método Prometeo: Imputación Causal para juristas y abogados
Orden 4: IM → V → CI
IM entra primero: daño pasa de $0 a $1,500,000 → IM
aporta $1,500,000
V entra tras IM: daño pasa de $1,500,000 a $3,500,000 → V
aporta $2,000,000
CI entra al final: daño pasa de $3,500,000 a $13,500,000→
CI aporta $10,000,000
Orden 5: V → CI → IM
V entra primero: daño pasa de $0 a $2,000,000 → V
aporta $2,000,000
CI entra tras V: daño pasa de $2,000,000 a $9,500,000 →
CI aporta $7,500,000
IM entra al final: daño pasa de $9,500,000 a $13,500,000→
IM aporta $4,000,000
Orden 6: V → IM → CI
V entra primero: daño pasa de $0 a $2,000,000 → V
aporta $2,000,000
IM entra tras V: daño pasa de $2,000,000 a $3,500,000 →
IM aporta $1,500,000
CI entra al final: daño pasa de $3,500,000 a $13,500,000→
CI aporta $10,000,000
6.5.3 La tabla de aportes: sumar y dividir
entre 6
Sumamos los aportes de cada institución en los seis órdenes
y dividimos entre 6. Eso da el aporte promedio de cada una
— su valor de Shapley.

El Método Prometeo: Imputación Causal para juristas y abogados
Institu Or Or Or Or Or Or Su Sha %
ción d. d. d. d. d. d. ma pley del
1 2 3 4 5 6 ($ ($M tot
M) ) al
CI — 6. 6. 7. 10. 7. 10. 47. $7.8 58.
CIBan 0 0 5 0 5 0 0 3M 0%
co
IM — 3. 4. 1.5 1.5 4. 1.5 15. $2.5 19.
Interca 0 0 0 5 8M 1%
m
V — 4. 3. 4. 2. 2. 2. 18. $3.0 22.
Vector 5 5 5 0 0 0 5 8M 8%
Verific 81. $13. 99.
ación 0 5M 9%
✓ ✓
¿De dónde sale este número? CI tiene el Shapley más alto
(58%) porque en los órdenes donde entra al final (órdenes 4 y 6),
aporta $10M — la totalidad de lo que faltaba. Eso eleva su
promedio significativamente. IM y V tienen Shapleys menores
porque sus canales individuales son más pequeños. La suma da
$13.5M, que es exactamente el total documentado.
6.5.4 Integración: R* combinado del caso
completo
El método de las rondas nos dio el R* de los cárteles (K =
35.8%) y de las cuentas mula (M = 23.9%). El método de
las órdenes nos dio la distribución interna entre las tres
instituciones de su R* total (40.4%). Integramos:
R* final integrado (rondas + Shapley):
K (carteles): 35.8% ← método de las rondas
M (mulas): 23.9% ← método de las rondas

El Método Prometeo: Imputación Causal para juristas y abogados
Subtotal K+M = 59.7%
Instituciones totales = 100% - 59.7% = 40.3%
Shapley distribuye ese 40.3% entre CI, IM y V:
CI: 58.0% × 40.3% = 23.4%
IM: 19.1% × 40.3% = 7.7%
V: 22.8% × 40.3% = 9.2%
Verificación:
35.8 + 23.9 + 23.4 + 7.7 + 9.2 = 100.0% ✓
Nodo R* Lectura del resultado
final
K — 35.8% Nodo de mayor R* y el más invisible. Son
Cárteles la condición necesaria del esquema: sin
ellos no existe la operación. Nodo inferido
— la investigación debe orientarse a
corroborar su identidad con evidencia
adicional.
CI — 23.4% Mayor R* entre las instituciones. Su canal
CIBanco bancario de depósito es el más grande y su
empleado tuvo participación activa
documentada.
M — 23.9% Alto R* bruto porque ejecutaron
Cuentas directamente las transacciones (arista
mula directa, peso 0.435). Pero S = 0.92:
R*_neta será mínima. Son el nodo más
visible con la menor responsabilidad real.
V — 9.2% Tercer canal. Monto total menor, pero
Vector período de operación largo (8 años). Daño
acumulado significativo.
IM — 7.7% Canal especializado (pagos a China).
Intercam Menor en monto documentado pero con
implicaciones adicionales porque facilitó la
adquisición de precursores.

El Método Prometeo: Imputación Causal para juristas y abogados

§6.6 Paso 3c: B* — quién se
benefició del esquema
B* distribuye el beneficio obtenido por cada actor como
consecuencia del esquema. En PLD, el beneficio no es solo
el dinero lavado: también incluye el acceso a los precursores
(que permitió producir más fentanilo) y las comisiones
institucionales.
Nodo Fuente de Estimación Evidencia
beneficio
K — Dinero $13,500,000 Análisis
Cárteles integrado en la USD en forense
economía fondos FinCEN (T-
formal + acceso integrados + E2).
a precursores beneficio no
para fentanilo. monetario del
acceso a
precursores
(incalculable en
su totalidad).
CI — Comisiones de Estimado: 2- Estimación
CIBanco apertura y 3% del monto estándar de
mantenimiento procesado = margen
de cuentas + $200,000- bancario en
liquidez de los $300,000 USD. cuentas de
depósitos. depósito (T-
E6).
IM — Comisiones de Estimado: 1.5- Estimación
Intercam transferencias 2.5% = estándar de
internacionales $22,500- comisiones
+ spread de tipo $37,500 USD. bancarias (T-
de cambio. E6).
V — Comisiones de Estimado: 1- Estimación
Vector operaciones de 2% = $20,000- estándar de
valores + spread $40,000 USD. corretaje (T-
de compraventa. E6).

El Método Prometeo: Imputación Causal para juristas y abogados
M — Comisión por Estimado: 1- Estándar de la
Cuentas mover el dinero 3% del monto industria de
mula (pago por el movido = reclutamiento
reclutamiento). $135,000- de mulas (T-
$405,000 USD. E6).
La comparación R* / B* en este caso es directa: K tiene R*
= 35.8% y obtiene prácticamente todo el beneficio
monetario significativo ($13.5M más el valor del acceso a
precursores). Las instituciones tienen R* conjunto = 40.3%
pero obtienen comisiones marginales (menos del 3% del
monto procesado). Las mulas tienen R* = 23.9% y obtienen
una comisión mínima. La inversión causal es completa: el
actor de menor visibilidad documental obtuvo la mayor
parte del beneficio.

El Método Prometeo: Imputación Causal para juristas y abogados
§6.7 Análisis de sensibilidad:
los tres escenarios
Calculamos R* para los tres puntos del rango de pesos y
aplicamos el árbol de decisión del Capítulo 6.
R* en escenario MÍNIMO (pesos más favorables a las
instituciones):
K = 28.4% CI = 19.6% M = 26.3% V = 14.8% IM =
10.9%
R* en escenario CENTRAL (punto medio de cada
rango):
K = 35.8% CI = 23.4% M = 23.9% V = 9.2% IM =
7.7%
R* en escenario MÁXIMO (pesos más desfavorables a
las instituciones):
K = 42.1% CI = 26.2% M = 21.5% V = 6.5% IM =
3.7%
Pregunta del árbol Respuesta
(Cap. 6, §6.7.5)
¿El nodo de mayor Sí. K (cárteles) lidera en los tres:
R* es el mismo en los 28.4%, 35.8%, 42.1%.
tres escenarios?
¿El orden relativo de No. En el mínimo, M (23.9% → 26.3%)
todos es el mismo? supera a CI (23.4% → 19.6%). El orden
interno entre M y CI cambia entre
escenarios.
Diagnóstico Declaración B: K es robusto como
nodo de mayor R*. El orden entre M y
CI depende del supuesto adoptado
respecto al peso de la arista M→SF.

El Método Prometeo: Imputación Causal para juristas y abogados
Declaración B: Con cualquier interpretación razonable de la
evidencia disponible, los carteles (K) tienen el mayor peso
causal en el daño al sistema financiero. El orden entre las
cuentas mula (M) y CIBanco (CI) en el segundo lugar depende
del supuesto adoptado respecto al peso de la arista M hacia SF.
La evidencia adicional que resolvería esta disputa es un análisis
forense individualizado de la participación de cada mula.

El Método Prometeo: Imputación Causal para juristas y abogados
§6.8 Paso 4: S, α y Δ
6.8.1 Cálculo de S
Recordatorio del Capítulo 2, §2.3.1: S = promedio de tres
preguntas (A, B, C) respondidas con 0, 0.5 o 1. A: ¿el procedimiento
estaba formalizado? B: ¿habría actuado igual cualquier otro? C: ¿el
sistema lo determinaba? R*_neta = R* × (1−S).
S de los Cárteles (K):
A: ¿Seguían instrucciones de alguien? No. Diseñaron el
esquema. A = 0.0
B: ¿Habría actuado igual cualquier otro cartel?
Parcialmente — otros carteles también lavan dinero,
pero este esquema especifico (precursores + tres canales)
requería características específicas. B = 0.3
C: ¿El mercado los presionaba a lavar? Si, estructuralmente.
C = 0.2
S_K = (0.0 + 0.3 + 0.2) / 3 = 0.17
S de CIBanco (CI):
A: ¿Seguía protocolos de compliance formalizados?
Sí, pero los incumplió deliberadamente. A =
0.3
B: ¿Habría actuado igual otro banco en la misma posición?
Parcialmente — la industria tiene casos similares,
pero la participación activa del empleado es
idiosincrática. B = 0.4
C: ¿El mercado presionaba a aceptar esos depósitos?
Parcialmente — competencia por liquidez. C =
0.4
S_CI = (0.3 + 0.4 + 0.4) / 3 = 0.37

El Método Prometeo: Imputación Causal para juristas y abogados
S de Intercam (IM):
A: ¿Seguía procedimientos de transferencias internacionales?
A = 0.5
Si — los procedimientos existían, pero sin due diligence
reforzada para el perfil de riesgo de estas empresas.
B: ¿Habría actuado igual otro banco con capacidad similar?
B = 0.6
C: ¿El sistema presionaba a procesar esas transferencias? C
= 0.5
S_IM = (0.5 + 0.6 + 0.5) / 3 = 0.53
S de Vector (V):
A: ¿Seguía procedimientos estándar de una casa de bolsa?
A = 0.6
B: ¿Habría actuado igual otra casa de bolsa?
Probablemente — el mecanismo de lavado via valores
B = 0.65
es conocido y documentado en la industria.
C: ¿El sistema presionaba a aceptar esas operaciones? C
= 0.55
S_V = (0.6 + 0.65 + 0.55) / 3 = 0.60
S de las Cuentas Mula (M):
A: ¿Seguían instrucciones del cartel? Si, completamente. A
= 1.0
B: ¿Habría actuado igual cualquier otra persona reclutada
bajo las mismas condiciones (necesidad + coacción)? B
= 0.95
C: ¿El sistema (reclutamiento + amenazas) C = 0.90
determinaba completamente su conducta?
S_M = (1.0 + 0.95 + 0.90) / 3 = 0.95

El Método Prometeo: Imputación Causal para juristas y abogados
6.8.2 R*_neta para cada nodo
R*_neta = R* × (1 − S):
K: 35.8% × (1−0.17) = 35.8% × 0.83 = 29.7% ← MAYOR
R*_neta
CI: 23.4% × (1−0.37) = 23.4% × 0.63 = 14.7%
M: 23.9% × (1−0.95) = 23.9% × 0.05 = 1.2% ← MÍNIMA
V: 9.2% × (1−0.60) = 9.2% × 0.40 = 3.7%
IM: 7.7% × (1−0.53) = 7.7% × 0.47 = 3.6%
La inversión causal cuantificada: Las cuentas mula tienen
R* = 23.9% (segundo nodo en el método de rondas) pero
R*_neta = 1.2% — prácticamente cero. Fueron reclutadas,
fueron dirigidas, fueron completamente sustituibles. El sistema
las usó como instrumento. K tiene R*_neta = 29.7%: la mayor
responsabilidad causal idiosincrática corresponde al nodo
invisible. CI tiene R*_neta = 14.7%: la participación activa del
empleado redujo su S, elevando su responsabilidad neta.
6.8.3 α — el cumplimiento de la obligación
de reporte
Recordatorio del Capítulo 6, §6.6: En PLD, α mide si el nodo
cumplió su obligación regulatoria de reporte. α = 0: no reportó y facilitó
activamente. α = 1: reportó y cooperó. Incluye α voluntario y α forzado.
Nodo Conducta verificable Fuente del α Valor
en el expediente α
K — No reportaron. Voluntaria nula. α_K
Cárteles Diseñaron el esquema =
para evadir 0.00
exactamente ese tipo
de reporte.

El Método Prometeo: Imputación Causal para juristas y abogados
CI — No reportaron. Multa α forzado por la α_CI
CIBanco de la CNBV = $67M multa. Baja =
pesos (α forzado). El voluntad. 0.08
empleado facilitó
activamente —
omisión deliberada
documentada.
IM — No reportaron. Multa α forzado por la α_IM
Intercam de la CNBV = $92M multa. Mayor =
pesos (la más alta, señal incumplimiento 0.06
de mayor relativo.
incumplimiento
documentado).
V — No reportaron. Multa α forzado por la α_V
Vector de la CNBV = $27M multa. =
pesos (la menor, señal 0.10
de menor
incumplimiento
relativo o menor
período investigado).
M — Aparecen en todos los α forzado α_M
Cuentas documentos bancarios dominante: =
mula (α forzado = 1.00 en identificadas y 0.75
visibilidad). Muchas documentadas.
fueron procesadas o
investigadas. No
reportaron
voluntariamente pero sí
fueron identificadas.
¿De dónde sale este número? Los valores de α de las
instituciones se calculan como la proporción de su AD que la
multa de la CNBV representa. CI: multa $67M MXN ÷ AD_CI
estimado = 0.08. IM: multa $92M MXN ÷ AD_IM estimado =

### 0.06. V: multa $27M MXN ÷ AD_V estimado = 0.10. Estas son
las asunciones forzadas hasta la fecha — si hay condena adicional,
α sube.

El Método Prometeo: Imputación Causal para juristas y abogados
6.8.4 Δ — la brecha
Calculo de Delta = R* - alpha:
K: 35.8% - 0% = +35.8% DEFICIT SEVERO (arquitecto
invisible)
CI: 23.4% - 8% = +15.4% DEFICIT SIGNIFICATIVO
M: 23.9% - 75% = -51.1% SOBRE-IMPUTACION
SEVERA
V: 9.2% - 10% = -0.8% APROXIMADAMENTE
PROPORCIONAL
IM: 7.7% - 6% = +1.7% DEFICIT MENOR
El patrón de inversión causal en este caso: K tiene Δ =
+35.8%: el nodo invisible causó el 35.8% del daño y no ha
asumido nada formalmente (ninguna de las multas de la CNBV
es contra los cárteles). Las cuentas mula tienen Δ = −51.1%:
son sobre-imputadas de manera severa — su alta visibilidad
documental las hace el blanco natural de las investigaciones,
aunque su responsabilidad causal neta sea mínima. Esta es la
inversión causal del PLD en su forma más clara.

El Método Prometeo: Imputación Causal para juristas y abogados
§6.9 Paso 5: D_total y el ajuste
debitor
6.9.1 Los tres componentes de D_total
T_invertido (daño emergente documentado):
Fondos ilícitos documentados por FinCEN:
CIBanco: $10,000,000 USD
Intercam: $ 1,500,000 USD
Vector: $ 2,000,000 USD
Total, documentado: $13,500,000 USD = $270,000,000 MXN
(aprox.)
Evidencia: ordenes FinCEN (T-E2). Cifra indiscutible como
base mínima.
T_impedido (costo de la contaminación activa del
sistema):
Costo de los procesos regulatorios en México y EE.UU. =
est. $30,000,000 MXN
Costo de la intervención de la CNBV sobre tres instituciones
= est. $45,000,000 MXN
Distorsión del sistema de corresponsalía bancaria = est.
$25,000,000 MXN
Perdida de liquidez del sistema por las multas y restricciones
= est. $20,000,000 MXN
T_impedido estimado = $120,000,000 MXN (E2/E6)
DeltaT_trayectoria (daño estructural persistente):
Daño reputacional internacional al sistema financiero
mexicano
(degradación de calificadoras afecta acceso futuro a capital) =
est. $80,000,000 MXN
Dania a la confianza en el sistema de prevención: difícil de

El Método Prometeo: Imputación Causal para juristas y abogados
cuantificar con precisión. Estimación conservadora:
$50,000,000 MXN
DeltaT estimado = $130,000,000 MXN (E6/E4)
D_total del caso:
T_invertido: $270,000,000 MXN (E2 — cifra base sólida)
T_impedido: $120,000,000 MXN (E2/E6 — estimación
regulatoria)
DeltaT_trayectoria: $130,000,000 MXN (E6 — sujeta a
disputa)
D_total = $520,000,000 MXN
D_total_min = $270,000,000 MXN (solo T_invertido — base
segura)
6.9.2 El ajuste debitor por nodo
AD_i = R*_i × D_total. El AD usa R* total, no R*_neta.
El daño existe independientemente de si el actor era
sustituible.
Nodo R* AD AD α Déficit Δ
(D_mi (D_tota actual monetario
n) l)
K — 35.8 $96.7M $186.2 $0 $186.2M —
Cártele % MXN M Todo por
s MXN recuperar
mediante
extinción
de dominio
CI — 23.4 $63.2M $121.7 $67M $54.7M por
CIBanc % MXN M (multa) asumir
o MXN

El Método Prometeo: Imputación Causal para juristas y abogados
M — 23.9 $64.5M $124.3 alta SOBRE-
Cuenta % MXN M (identif IMPUTAD
s mula MXN .) AS —
AD/R*_net
a: solo
$3.2M
proporciona
l
V — 9.2% $24.8M $47.8M $27M $20.8M por
Vector MXN MXN (multa) asumir
IM — 7.7% $20.8M $40.0M $92M Sobrepagó:
Interca MXN MXN (multa) multa >
m AD.
Candidato a
revisión
regulatoria.
Un resultado inesperado — Intercam sobrepagó: La multa
de Intercam ($92M MXN) excede su AD calculado ($40M MXN con
D_total completo). Eso significa que Intercam fue sancionada por encima
de su peso causal proporcional. Esto puede reflejar: (a) que el regulador
usó la multa como disuasor sistémico (no proporcional al daño individual),
o (b) que hay evidencia adicional no pública que eleva el R* de IM. En
un proceso de impugnación, Intercam podría argumentar que la sanción
excede el daño atribuible causalmente.
6.9.3 Base técnica para la extinción de
dominio
AD_B = R*_B × B_total. Los activos que son producto del
delito deben ser objeto de extinción de dominio
independientemente de a nombre de quién estén
registrados. K no aparece en ningún registro de activos —
pero su R* determina la porción de los $13.5M USD que le
corresponde causalmente:

El Método Prometeo: Imputación Causal para juristas y abogados
Base para extinción de dominio:
K (carteles): 35.8% × $270M MXN = $96.7M MXN
Estrategia: identificar activos de los carteles registrados
a nombre de testaferros o empresas instrumentales.
El R* alto de K con evidencia T-E2/T-E6 sustenta la
acción.
CI: 23.4% × $270M = $63.2M MXN (por encima de la multa
ya impuesta)
V: 9.2% × $270M = $24.8M MXN (cubierto
aproximadamente por la multa)
IM: 7.7% × $270M = $20.8M MXN (cubierto y excedido
por la multa)
Monto total para extinción de dominio: mínimo
$96.7M MXN (activos de K)

El Método Prometeo: Imputación Causal para juristas y abogados
§6.10 Los cuatro documentos
del expediente
6.10.1 Documento 1: la hoja de calibración
Arista Tipo Rango Fuente Limitaciones
E [a,b] documental explícitas
K → T- [0.50, Análisis K no aparece por
CI E2/E6 0.70] forense nombre en
FinCEN documentos
(Orden junio públicos. Rango
2025). incluye
Evidencia de incertidumbre
flujos del sobre si la
Cártel del instrucción fue
Golfo. directa o
mediada.
CI → T-E2 [0.72, Orden La participación
SF 0.88] FinCEN. del empleado
CNBV: multa individual eleva el
$67M. rango. Sin el
Registros de la empleado, habría
cuenta sido T-E4.
facilitada por el
empleado.
IM → T-E2 [0.68, Orden Los registros
SF 0.82] FinCEN. SWIFT son T-E1
Registros para las
SWIFT de transferencias. El
transferencias análisis de su
a empresas naturaleza ilícita
chinas. CNBV: es T-E2.
multa $92M.
V → T- [0.55, Orden Ocho años de
SF E2/E4 0.72] FinCEN. operación. La
Registros de correlación
operaciones de estadística T-E4

El Método Prometeo: Imputación Causal para juristas y abogados
valores 2013- apoya pero el

### 2021. CNBV: período largo
multa $27M. puede diluir la
determinación.
M → T-E1 [0.35, Las cuentas Rango moderado
SF 0.52] mula aparecen deliberado: alta
en los registros determinación
bancarios sistémica
directamente. (S=0.95). El
rango refleja que
el acto de las
mulas era casi
completamente
estructural.
6.10.2 Documento 2: la tabla de sensibilidad
Nodo R* R* R* ¿Cambia el
mínim centra máxim liderazgo?
o l o
K — 28.4% 35.8% 42.1% No. K lidera en
Cárteles los tres.
CI — 19.6% 23.4% 26.2% Segundo en
CIBanco central y máximo;
tercero en
mínimo.
M — 26.3% 23.9% 21.5% Segunda en
Cuentas mínimo. Orden
mula con CI varía.
V — 14.8% 9.2% 6.5% Cuarto en central
Vector y máximo.
IM — 10.9% 7.7% 3.7% Quinto en todos.
Intercam
Diagnóstic DECLARACIÓ
o N B — K

El Método Prometeo: Imputación Causal para juristas y abogados
robusto; orden
M/CI variable
6.10.3 Documento 3: la declaración de
robustez
Declaración B — Para insertar en el expediente: El
análisis causal del caso CIBanco / Intercam / Vector, realizado
mediante el Método Prometeo de Imputación Causal (método
combinado de rondas y valores de Shapley), produce una
Declaración B: con cualquier interpretación razonable de la
evidencia pública disponible, los cárteles beneficiarios son el
actor de mayor peso causal en el daño al sistema financiero,
con un R* que oscila entre 28.4% y 42.1% según el supuesto
de calibración adoptado. Esta conclusión es robusta. El orden
entre CIBanco y las cuentas mula en el segundo lugar depende
del peso que se asigne a la arista M→SF: si ese peso está en la
mitad inferior de su rango, CIBanco es el segundo actor. Si está
en la mitad superior, las cuentas mula son el segundo actor en
R* bruto, pero con R*_neta ≈ 1.2% dado S=0.95. En cualquier
escenario, las cuentas mula tienen responsabilidad causal neta
mínima — son el actor de mayor visibilidad documental y
menor responsabilidad causal idiosincrática del caso.

El Método Prometeo: Imputación Causal para juristas y abogados
§6.11 Panel final: todos los
números del caso
Actor R* B* S R*_n α Δ AD
eta (D_min)
K — 35.8 ~95 0. 29.7 0.0 +35. $96.7M
Cártel % % 17 % 0 8% MXN
es
CI — 23.4 ~2. 0. 14.7 0.0 +15. $63.2M
CIBa % 2% 37 % 8 4% MXN
nco
M — 23.9 ~2. 0. 1.2% 0.7 −51. SOBRE-
Mulas % 5% 95 5 1% IMPUTA
DAS
V — 9.2 ~0. 0. 3.7% 0.1 −0.8 $24.8M
Vecto % 6% 60 0 % MXN
r
IM — 7.7 ~0. 0. 3.6% 0.0 +1.7 $20.8M <
Interc % 6% 53 6* % multa*
am
* IM fue sancionada con $92M MXN, que excede su AD = $20.8M. La multa
regulatoria puede tener bases distintas al daño causal proporcional (disuasión
sistémica, incumplimiento normativo autónomo).
Lo que este capítulo ejecutó

El Método Prometeo: Imputación Causal para juristas y abogados
✓ Paso 1: grafo con 5 nodos activos (K, CI, IM, V, M) más un
nodo instrumental (EC) y el nodo final (SF). Aristas
clasificadas por tipo con evidencia FinCEN/CNBV.
✓ Paso 2: pesos asignados con la tabla T-E0 a T-E1, reproducida
y aplicada arista por arista con justificación explícita de cada
rango.
✓ Paso 3a — método de rondas: K = 35.8% (condición
necesaria del esquema). Las rondas colocan a los cárteles
como nodo de mayor R* en todos los escenarios.
✓ Paso 3b — método de las órdenes (Shapley): CI = 58%, V =
22.8%, IM = 19.1% de la responsabilidad entre las tres
instituciones. Los 6 órdenes calculados explícitamente, con
origen de los montos documentado.
✓ Paso 4: S_mulas = 0.95 → R*_neta = 1.2%. Las cuentas mula
son el nodo más sobre-imputado del caso: Δ = −51.1%. S_CI
= 0.37 → R*_neta = 14.7%.
✓ Paso 5: D_total = $520M MXN ($270M indiscutibles). AD
del cartel = $96.7M — base para extinción de dominio.
Resultado inesperado: Intercam fue multada por encima de su
AD causal.
✓ Declaración B: K es robusto como nodo de mayor R*. El
orden M/CI en segundo lugar varía según el supuesto
adoptado sobre el peso de la arista M→SF.

El Método Prometeo: Imputación Causal para juristas y abogados
EL MÉTODO PROMETEO · IMPUTACIÓN CAUSAL

