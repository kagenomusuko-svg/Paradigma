### Capítulo 3
Las herramientas en
acción
Los cinco pasos del protocolo, calculados paso a paso sobre un caso
real
El Capítulo 2 explicó qué hace cada herramienta y para qué
sirve. Este capítulo la opera. Tomamos el mismo caso del
banco que recorrió el Capítulo 2 y lo llevamos de principio
a fin: desde la construcción del grafo hasta el expediente
listo para presentar ante el tribunal.
Cada sección reproduce en forma compacta la tabla o el
criterio relevante del Capítulo 2 antes de aplicarlo, para que
no sea necesario volver atrás. Cada operación se muestra
completa, con todos sus números, sin saltar ningún paso.
Las matemáticas son sumas, multiplicaciones y divisiones.
Si en algún punto el resultado parece sorprendente, el
cálculo está ahí para que pueda verificarse.
Al terminar este capítulo, el lector tendrá el protocolo
completo ejecutado una vez. Los Capítulos 4, 5 y 6 lo
aplicarán a distintos tipos de caso. Lo que se aprende aquí
es la mecánica; lo que se aprende allá es el juicio.

El Método Prometeo: Imputación Causal para juristas y abogados
§3.1 El caso que usaremos:
banco, producto defectuoso,
cuarenta víctimas
Este caso es el mismo que el Capítulo 2 usó como
referencia. Lo presentamos ahora en su versión completa,
con todos los hechos relevantes para el análisis.
Hechos del caso Un banco diseñó en 2020 un producto de
inversión llamado "Fondo Seguro Plus" que prometía
rendimientos del 12% anual. Su propio departamento de
riesgos ya había documentado internamente que el fondo era
especulativo y que el 12% no era sostenible. La dirección del
banco presionó a riesgos para que aprobara el producto de
todas formas. Se diseñó un script obligatorio para los asesores
de ventas que incluía frases como "capital garantizado" y
"riesgo mínimo". El script fue instrumentalizado en un
protocolo de ventas (material, guiones y contrato) que los
asesores debían usar sin variación. Cuarenta asesores
vendieron el producto durante dos años a 1,200 clientes. En
2022 el fondo colapsó. Los 1,200 clientes perdieron en
promedio $4,000 pesos de capital invertido. El banco
despidió a tres asesores, los denunció penalmente y publicó
un comunicado exonerando a la institución.
Los cinco nodos del caso:
Nodo Símbolo Tipo Descripción en el caso
1 B — Diseño La dirección del banco.
Banco Diseñó el producto,
ignoró la advertencia de
riesgos, diseñó el script,
fijó las metas de
colocación y creó el

El Método Prometeo: Imputación Causal para juristas y abogados
sistema de incentivos que
determinó el
comportamiento de los
asesores.
2 R — Ejecución La dirección de riesgos.
Riesgos Tenía el mandato de
aprobar o vetar el
producto. Lo aprobó bajo
presión de la dirección.
Tenía función de
supervisión independiente
que no ejerció.
3 A — Ejecución Los cuarenta asesores de
Asesores ventas. Presentaron el
producto a los clientes
usando el script
obligatorio diseñado por el
banco. No tenían margen
para modificar el mensaje
ni para negarse sin
consecuencias laborales.
4 P — Instrumental El script de ventas, el
Protocolo material publicitario y el
contrato de adhesión. No
tiene voluntad — es una
mediación neutral. Su
presencia en el grafo
apunta causalmente hacia
quien lo diseñó: el banco
(B). Es el instrumento que
convirtió el diseño del
banco en el acto de venta
de los asesores.
5 C — Final (Nf) Los 1,200 clientes que
Clientes perdieron su inversión.
Son el nodo final del
grafo: el destinatario del
daño. No entran en el
cálculo de R* ni de S —
son el punto de llegada del
análisis.

El Método Prometeo: Imputación Causal para juristas y abogados
Sobre el nodo P (Protocolo): P es un nodo instrumental: un
instrumento sin voluntad que tiene posición causal. Aparece en el grafo
porque sin el script y el contrato de adhesión diseñados por B, los asesores
no habrían tenido el instrumento concreto con el que presentaron el
producto a los clientes. P no tiene R* propio — toda su influencia causal
se canaliza a través de las aristas que lo conectan con A y con C, y esas
aristas reflejan el peso de B como diseñador. Incluirlo en el grafo hace
visible ese mecanismo de manera explícita.

El Método Prometeo: Imputación Causal para juristas y abogados
§3.2 Paso 1 en acción:
construir el grafo
Del Capítulo 2: Del Capítulo 2, §2.1.2: una arista directa es cuando A
realizó la acción que produjo directamente el resultado. Una arista estructural
es cuando A creó las condiciones bajo las cuales B pudo causar el resultado.
Una arista de omisión es cuando A tenía el deber de impedir el resultado y no
lo hizo. Una arista nula (w = 0) requiere evidencia positiva de la ausencia
— no es simplemente la falta de evidencia.
Identificamos todas las aristas causales del caso y las
clasificamos por tipo. Para cada arista anotamos también la
evidencia del expediente que la sustenta, porque esa
evidencia determinará el rango de peso en el Paso 2.
Arista Tipo Dirección Evidencia del
causal expediente
B → Estructural B diseñó P El script y el contrato
P de adhesión fueron
elaborados por el
departamento de
marketing del banco,
aprobados por la
dirección.
Documentos internos
verificables.
B → Estructural / B presionó a Testimonios del
R omisión R equipo de riesgos
sobre la presión de la
dirección. Correo
parcial que referencia
la discusión interna. El
memorándum de
riesgos fue archivado
sin consecuencias.

El Método Prometeo: Imputación Causal para juristas y abogados
B → Estructural B determinó La política comercial
A el sistema con el script
que A operó obligatorio y las metas
de colocación están
documentadas. El
sistema de incentivos
laborales está en
contratos.
P → Instrumental P fue el Cuarenta asesores
A → Ejecución instrumento usaron el mismo script
que A usó en las mismas fechas.
Correlación estadística
del patrón de ventas.
Los contratos
firmados por los
clientes son idénticos.
R → Directa R habilitó El dictamen de
C (habilitación) que el aprobación de riesgos
producto (firmado) fue el
llegara a C mecanismo jurídico
que permitió la
comercialización. Sin
ese dictamen, el
producto no habría
podido venderse.
A → Directa A realizó la Cuarenta asesores,
C venta a C 1,200 contratos
firmados. Evidencia
masiva y directa del
acto de venta.
P → Instrumental P fue el El contrato de
C → Final instrumento adhesión que los
de la venta a clientes firmaron es el
C instrumento diseñado
por B que materializó
el daño. Los 1,200
contratos son el rastro
directo.
B → Estructural (a B creó las La arista estructural
C través de P y condiciones acumula todas las
A) del daño a C rutas: B→P→C,

El Método Prometeo: Imputación Causal para juristas y abogados
B→A→C, B→R→C.
El daño a C es la
consecuencia del
diseño total de B.
⚠ El nodo P (Protocolo) no tiene arista hacia R. R aprobó el
producto con base en los documentos de riesgo, no con base
en el script de ventas. Las aristas del grafo se trazan desde los
hechos del caso, no desde el organigrama. P solo tiene aristas
hacia A y hacia C, que son los nodos sobre los que el
instrumento actuó directamente.

El Método Prometeo: Imputación Causal para juristas y abogados
§3.3 Paso 2 en acción: asignar
los rangos de peso
Del Capítulo 2: Del Capítulo 2, §2.2.3: el peso w de una arista no es el
número que el analista cree que es correcto — es el rango que la evidencia
disponible justifica. La tabla E0-E8 determina ese rango según el tipo de
evidencia. No hay discrecionalidad en la asignación: si la evidencia es E3, el
rango es [0.55, 0.75], no ningún otro.
Reproducimos la tabla E0-E8 compacta para tener el
criterio a mano mientras asignamos cada peso:
Tipo Descripción de la Rango Referencia en
evidencia w este caso
E1 Documento directo: [0.75 – Script aprobado,
contrato, correo, acta, 0.95] política comercial,
registro digital. dictamen firmado.
E2 Mecanismo técnico [0.70 – Peritaje sobre el
documentado 0.90] diseño del
pericialmente. producto.
E3 Testimonio múltiple [0.55 – Testimonios del
convergente con 0.75] equipo de riesgos
corroborante sobre la presión.
documental.
E4 Correlación estadística [0.50 – Patrón de ventas
controlada. 0.70] idéntico en los 40
asesores.
E5 Testimonio único con [0.35 – —
corroborante 0.55]
documental parcial.
E6 Inferencia razonada por [0.25 – —
posición estructural. 0.45]

El Método Prometeo: Imputación Causal para juristas y abogados
E7 Correlación [0.10 – —
temporal/espacial sin 0.30]
mecanismo.
E8 Dicho único sin ningún [0.05 – —
respaldo. 0.20]
E0 Arista nula 0.00 —
documentada: evidencia
de la ausencia de
conexión.
3.3.1 Asignación arista por arista
Para cada arista respondemos: ¿qué evidencia del
expediente la sustenta? Según la respuesta, asignamos el
tipo E y el rango correspondiente.
Arista Tipo Rango Evidencia Razonamiento
E [a,b] clave
B → E1 [0.85, Script E1 directo: B
P 0.95] aprobado por diseñó y aprobó
dirección (doc. P. El rango es alto
interno). dentro de E1
Política porque no hay
comercial ninguna
firmada. ambigüedad — B
es el autor formal
del instrumento.
B → E1/E3 [0.60, Dictamen de El dictamen
R 0.78] riesgos archivado es E1
archivado sin (documento). La
consecuencias. presión es E3
Testimonios (testimonios
sobre presión. convergentes). El
rango refleja la
combinación: el
techo E1

El Método Prometeo: Imputación Causal para juristas y abogados
levantado
parcialmente por
la necesidad de
acreditar el
mecanismo de
presión.
B → E1 [0.80, Política E1 directo: los
A 0.92] comercial con documentos que
script determinaron el
obligatorio. comportamiento
Sistema de de A están en el
incentivos en expediente. Rango
contratos. alto porque la
formalización es
total.
P → E4 [0.55, 40 asesores, E4: correlación
A 0.72] mismo script, estadística. El
mismo patrón patrón idéntico en
estadístico de 40 asesores es
ventas. evidencia de que P
determinó el
comportamiento
de A. No hay
documento
individual asesor-
por-asesor, pero la
correlación es
muy fuerte.
R → E1 [0.62, Dictamen de E1: el dictamen es
C 0.78] aprobación un documento
firmado (doc. directo que
directo). habilitó la
comercialización.
El rango es
moderado dentro
de E1 porque R es
un nodo de
habilitación
(permitió que
ocurriera) no de
ejecución directa.

El Método Prometeo: Imputación Causal para juristas y abogados
A → E1 [0.40, 1,200 E1 documental,
C 0.58] contratos pero rango
firmados. moderado: A
Registro ejecutó el acto,
directo de pero P (el
ventas. instrumento) y B
(el diseño)
determinaron casi
todo el contenido.
El rango bajo para
una arista E1
refleja que la
discrecionalidad
real de A era
mínima.
P → E1 [0.55, El contrato de E1: el contrato es
C 0.72] adhesión el instrumento
firmado por que materializó el
los 1,200 daño. Es el nexo
clientes. directo entre el
diseño de B (que
creó P) y el daño a
C.
B → E1/E3 [0.72, Toda la cadena La arista
C 0.88] de estructural
documentos acumulada de B
institucionales hacia C se
+ testimonios sustenta en toda la
sobre el diseño cadena
deliberado. documental. Es la
arista de mayor
peso del grafo
porque es la
condición
necesaria de todas
las demás.
¿Por qué A → C tiene rango bajo si hay 1,200 contratos
firmados? Los contratos son E1 para la arista A→C en el sentido
de que A realizó el acto de venta. Pero el peso w de una arista no mide si
el acto ocurrió — eso ya lo captura la existencia de la arista. El peso mide
cuánto del comportamiento de A era determinado por el sistema, no

El Método Prometeo: Imputación Causal para juristas y abogados
cuántas veces A repitió ese comportamiento. La determinación de A por
B y P es muy alta, lo que hace que el rango de A→C sea moderado: A
ejecutó, pero casi todo el contenido de esa ejecución venía del sistema.
3.3.2 El grafo con sus rangos: visión de
conjunto
Esta es la estructura completa del caso con los rangos
asignados. Cada arista tiene su tipo de evidencia y su
intervalo de peso:
Arista Tipo Rango Interpretación
E w
B → E1 [0.85, El banco es el autor formal del
P 0.95] instrumento. Arista de diseño total.
B → E1/E3 [0.60, El banco presionó a riesgos.
R 0.78] Combinación de documento y
testimonios.
B → E1 [0.80, El banco diseñó el sistema que
A 0.92] determinó el comportamiento de
A.
P → E4 [0.55, El instrumento determinó el
A 0.72] comportamiento de los asesores.
Correlación estadística.
R → E1 [0.62, Riesgos habilitó la comercialización
C 0.78] con su dictamen.
A → E1 [0.40, Los asesores ejecutaron la venta.
C 0.58] Rango moderado por alta
determinación sistémica.
P → E1 [0.55, El instrumento materializó el daño
C 0.72] en el cliente.

El Método Prometeo: Imputación Causal para juristas y abogados
B → E1/E3 [0.72, La arista estructural acumulada.
C 0.88] Condición necesaria de todo el
sistema.

El Método Prometeo: Imputación Causal para juristas y abogados
§3.4 Paso 3 en acción: calcular
R*
Del Capítulo 2: Del Capítulo 2, §2.3.1: R* es el vector que distribuye
la responsabilidad causal del daño entre todos los nodos activos. La suma de
todos los R* es siempre 100%. R* no mide intención ni culpabilidad: mide
posición causal en el sistema de mediaciones. Se calcula mediante el método de
las rondas.
3.4.1 Qué nodos entran en el cálculo de R*
Antes de calcular, identificamos qué nodos participan en el
cálculo y cuáles no:
• B, R y A entran en el cálculo: son los nodos activos con
voluntad que tienen posición causal en el resultado.
• P entra en el cálculo como nodo instrumental: no tiene
voluntad propia, pero tiene aristas que transmiten la
influencia de B hacia A y hacia C. Su R* propio
reflejará exactamente cuánta influencia del sistema pasa
por él.
• C no entra en el cálculo: es el nodo final, el destinatario
del daño. Su R* no se calcula porque es el punto de
llegada, no un actor causal.
El nodo instrumental P en el cálculo: P es un nodo sin
voluntad, pero eso no significa que no tenga influencia causal en el
resultado. Su influencia en R* será real pero derivada: P recibe influencia
de B (quien lo diseñó) y la transmite hacia A y hacia C. Al final, el R*
de P mostrará la fracción del resultado que pasó a través del instrumento.
Esa fracción le corresponde causalmente a B, porque B diseñó P — pero
hacerlo visible en el cálculo muestra el mecanismo con precisión.

El Método Prometeo: Imputación Causal para juristas y abogados
3.4.2 El método de las rondas: con el
escenario central
Usamos los pesos centrales (punto medio de cada rango)
para el cálculo base. Los tres escenarios (mínimo, central,
máximo) se calculan en el análisis de sensibilidad del §3.6.
Pesos centrales para este cálculo:
Pesos centrales (punto medio de cada rango):
B→P = (0.85+0.95) /2 = 0.90
B→R = (0.60+0.78) /2 = 0.69
B→A = (0.80+0.92) /2 = 0.86
P→A = (0.55+0.72) /2 = 0.64
R→C = (0.62+0.78) /2 = 0.70
A→C = (0.40+0.58) /2 = 0.49
P→C = (0.55+0.72) /2 = 0.64
B→C = (0.72+0.88) /2 = 0.80
Ronda 0: distribución inicial igual entre los nodos
activos
Distribuimos el 100% en partes iguales entre B, R, A y P —
los cuatro nodos que pueden recibir influencia de otros. C
queda fuera porque es el nodo final.
Distribución inicial (Ronda 0):
B = 25.0% R = 25.0% A = 25.0% P = 25.0%
Suma = 100% ✓

El Método Prometeo: Imputación Causal para juristas y abogados
Ronda 1: cada nodo recibe la influencia de quien lo
alimenta
Para cada nodo calculamos la influencia que recibe de sus
alimentadores: el porcentaje del alimentador × el peso de la
arista correspondiente. Luego normalizamos dividiendo
cada resultado entre la suma total y multiplicando por 100.
Ronda 1 — influencia recibida por cada nodo:
B recibe de: nadie → 0.000
(B es nodo de diseño: solo da, no recibe en este grafo)
R recibe de: B (25.0% × 0.69) → 17.25
A recibe de: B (25.0% × 0.86) → 21.50
P (25.0% × 0.64) → 16.00
Total, A → 37.50
P recibe de: B (25.0% × 0.90) → 22.50
Suma total = 0 + 17.25 + 37.50 + 22.50 = 77.25
Normalizamos (dividimos entre 77.25 y multiplicamos × 100):
B = (0.00 / 77.25) × 100 = 0.0%
R = (17.25 / 77.25) × 100 = 22.3%
A = (37.50 / 77.25) × 100 = 48.5%
P = (22.50 / 77.25) × 100 = 29.1%
Suma = 99.9% ≈ 100% ✓ (diferencia por
redondeo)
¿Por qué A recibió influencia de P además de B? En la
Ronda 0, P tenía el 25% inicial. Ese 25% se multiplicó por el peso de
P→A (0.64), produciendo 16.00 unidades de influencia que A recibió
de P. A su vez, A recibió 21.50 de B directamente. La suma de ambas
(37.50) refleja que el comportamiento de A estaba determinado por dos

El Método Prometeo: Imputación Causal para juristas y abogados
rutas: la instrucción directa del banco (B→A) y el instrumento concreto
que el banco diseñó (P→A). Eso es correcto: los asesores recibieron
órdenes del banco Y usaron el script del banco.
Ronda 2: la influencia de B llega a C a través de R,
A y P
Los resultados de la Ronda 1 (R = 22.3%, A = 48.5%, P =
29.1%) ya incorporan la influencia de B. Multiplicamos esos
porcentajes por sus pesos de arista hacia C y sumamos la
contribución directa de B:
Ronda 2 — influencia total sobre C:
B llega a C directamente con su peso de arista: w(B→C) =
0.80
R llega a C: R*_R(r1) × w(R→C) = 22.3% × 0.70 = 0.1561
A llega a C: R*_A(r1) × w(A→C) = 48.5% × 0.49 = 0.2377
P llega a C: R*_P(r1) × w(P→C) = 29.1% × 0.64 = 0.1862
B llega a C directamente: 0.8000
Suma total = 0.1561 + 0.2377 + 0.1862 + 0.8000 = 1.3800
Normalizamos:
B: 0.8000 / 1.3800 × 100 = 57.97% ≈ 58.0%
R: 0.1561 / 1.3800 × 100 = 11.31% ≈ 11.3%
A: 0.2377 / 1.3800 × 100 = 17.22% ≈ 17.2%
P: 0.1862 / 1.3800 × 100 = 13.49% ≈ 13.5%
Suma = 100.0% ✓
3.4.3 Resultado de R* y cómo leerlo

El Método Prometeo: Imputación Causal para juristas y abogados
Nodo R* Lectura del resultado
B — 58.0% El banco tiene el mayor peso causal del
Banco grafo. Más de la mitad de la responsabilidad
por el daño a los clientes es causalmente
atribuible a las decisiones de diseño del
banco: el producto, el script, las metas, el
sistema de incentivos.
P — 13.5% El instrumento tiene un R* real, aunque no
Protocolo tenga voluntad. Ese 13.5% es la fracción
del resultado que pasó específicamente a
través del script y el contrato. Causalmente
le corresponde a B, que lo diseñó. Tenerlo
visible demuestra el mecanismo.
A — 17.2% Los asesores tienen el menor R* entre los
Asesores nodos de ejecución. A pesar de haber
realizado directamente el acto de venta, su
posición en el sistema estaba tan
determinada por B y P que su peso causal
real es modesto.
R — 11.3% Riesgos tiene el R* más bajo de los nodos
Riesgos con voluntad. Su función era de
habilitación (aprobó el producto) no de
diseño ni de ejecución directa. Pero ese
11.3% es real: sin su dictamen, el producto
no habría podido venderse.
La regla del nodo de diseño se confirma: B (nodo de
diseño) tiene R* = 58.0%. A (nodo de ejecución directa) tiene
R* = 17.2%. El diseñador tiene más del triple del peso causal
del ejecutor más visible. Eso no es una coincidencia: es el
resultado matemático de que B tiene aristas de alta influencia
hacia todos los demás nodos del sistema, y esas aristas se
acumulan en las rondas.

El Método Prometeo: Imputación Causal para juristas y abogados
§3.5 Paso 3 continuado:
calcular B*
Del Capítulo 2: Del Capítulo 2, §2.3.2: B* distribuye el beneficio
obtenido por los actores del grafo como consecuencia del evento dañino. B*_i
= Beneficio_neto_i / Beneficio_total. R* y B* son vectores distintos. La
comparación revela el perfil completo de cada actor: quién causó el daño y quién
se benefició de él.
3.5.1 Identificar las fuentes de beneficio
Para calcular B* hay que responder primero: ¿quién se
benefició del evento dañino y de qué manera? Los
beneficios no siempre son monetarios directos. En este
caso hay cuatro tipos de beneficio:
Fuente de Descripción Monto ¿Quién se
beneficio estimado benefició?
Comisiones El banco 3% × B: el banco
de venta cobró $4,800,000 + recibió las
comisiones 1.5% × comisiones. R
de entrada al $4,800,000 × y A recibieron
fondo (3% 2 = $144,000 fracciones
del capital + $144,000 como bonos.
invertido) y = $288,000
comisiones
de gestión
anuales
(1.5%)
durante dos
años.
Protección Al imputar al Estimado B: la dirección
reputacional asesor, el pericialment del banco es el
banco e en principal
protegió su $450,000 beneficiario de
imagen ante (fracción del la narrativa

El Método Prometeo: Imputación Causal para juristas y abogados
reguladores y costo de un que lo
clientes. Eso incidente sin exonera.
tiene un valor resolución
estimable en de este tipo
términos de para un
capital banco de ese
reputacional tamaño).
conservado.
Evasión de La dirección Estimado en R: el director
consecuencia de riesgos $120,000 de riesgos
s de R evitó que su (valor de la personalmente
aprobación continuidad .
negligente laboral y el
tuviera diferencial
consecuencia de
s formales. trayectoria).
Mantuvo su
posición y su
trayectoria
profesional.
Bonos sobre Los asesores Estimado en A: los asesores
metas de que $96,000 total de ventas.
colocación superaron las (40 asesores
metas de × bono
colocación promedio de
del producto $2,400 por
recibieron colocación
bonos. Ese exitosa).
beneficio
ocurrió
durante la
venta, antes
del colapso
del fondo.
Beneficio total del evento dañino:
Comisiones (B): $288,000
Protección reputacional (B): $450,000
Evasión consecuencias (R): $120,000
Bonos de colocación (A): $96,000

El Método Prometeo: Imputación Causal para juristas y abogados
Beneficio_total = $954,000
3.5.2 Calcular B* para cada nodo
B*_i = Beneficio_neto_i / Beneficio_total. Para cada nodo
sumamos los beneficios que le corresponden y los
dividimos entre el beneficio total:
Cálculo de B*:
B (banco): ($288,000 + $450,000) / $954,000 = $738,000 /
$954,000 = 0.774 = 77.4%
R (riesgos): $120,000 / $954,000 = 0.126 = 12.6%
A (asesores): $96,000 / $954,000 = 0.101 = 10.1%
P (protocolo): $0 (instrumento sin beneficio propio) = 0.0%
Suma: 77.4% + 12.6% + 10.1% + 0.0% = 100.1% ≈
100% ✓
3.5.3 Comparación R* vs. B*: el mapa
completo
Nodo R* B* B* − Interpretación
R*
B — 58.0% 77.4% +19.4% Causó el 58% y
Banco obtuvo el 77% del
beneficio. Diseñador
beneficiario: el actor
que más causó y más
se benefició. Base de la

El Método Prometeo: Imputación Causal para juristas y abogados
pretensión de
responsabilidad
principal Y de
enriquecimiento sin
causa.
R — 11.3% 12.6% +1.3% Causó el 11.3% y
Riesgos obtuvo el 12.6%.
Posición casi
equilibrada: su
beneficio es
marginalmente mayor
que su causa. Sin perfil
de chivo expiatorio ni
de beneficiario
excesivo.
A — 17.2% 10.1% −7.1% Causó el 17.2% y
Asesores obtuvo el 10.1%.
Causaron más de lo
que se beneficiaron.
Perfil de ejecutor sin
beneficio: ni la
causalidad ni el
beneficio justifican que
sean el nodo principal
de la imputación.
P — 13.5% 0.0% −13.5% El instrumento tiene
Protocolo R* real, pero B* = 0.
El beneficio del
instrumento le
pertenece a su
diseñador (B). Esto
confirma que la
pretensión de
enriquecimiento debe
dirigirse a B, no al
instrumento.
Lo que R* y B* juntos permiten decir: "El banco causó el
58% del daño y obtuvo el 77% del beneficio del evento. Los
asesores causaron el 17.2% del daño y obtuvieron el 10.1% del
beneficio. Ni la causalidad ni el beneficio justifican que los

El Método Prometeo: Imputación Causal para juristas y abogados
asesores sean el nodo principal de la imputación. El banco es
simultáneamente el mayor causante y el mayor beneficiario —
eso es lo que el análisis causal demuestra con precisión."

El Método Prometeo: Imputación Causal para juristas y abogados
§3.6 Análisis de sensibilidad:
los tres escenarios
Del Capítulo 2: Del Capítulo 2, §2.2.5: el análisis de sensibilidad calcula
R* en tres puntos del rango de pesos (mínimo, central, máximo) y aplica el
árbol de decisión para determinar si el resultado es robusto. El objetivo no es
elegir el valor correcto: es demostrar que la conclusión no depende del valor
elegido.
3.6.1 Los tres escenarios de peso
Arista w_min w_central w_max Rango origen
B → P 0.85 0.90 0.95 E1 [0.85, 0.95]
B → R 0.60 0.69 0.78 E1/E3 [0.60, 0.78]
B → 0.80 0.86 0.92 E1 [0.80, 0.92]
A
P → A 0.55 0.64 0.72 E4 [0.55, 0.72]
R → 0.62 0.70 0.78 E1 [0.62, 0.78]
C
A → 0.40 0.49 0.58 E1/contexto [0.40,
C 0.58]
P → C 0.55 0.64 0.72 E1 [0.55, 0.72]
B → 0.72 0.80 0.88 E1/E3 [0.72, 0.88]
C
3.6.2 R* en los tres escenarios

El Método Prometeo: Imputación Causal para juristas y abogados
Aplicamos el método de las rondas para cada escenario.
Aquí mostramos los resultados; el procedimiento es
idéntico al del §3.4.2.
Resultados de R* — los tres escenarios:
Escenario MÍNIMO (pesos favorables al banco —
interpretación más
conservadora de la evidencia):
B = 51.8% R = 12.4% A = 20.3% P = 15.5%
Escenario CENTRAL (punto medio de cada rango):
B = 58.0% R = 11.3% A = 17.2% P = 13.5%
Escenario MÁXIMO (pesos desfavorables al banco —
interpretación
más severa de la evidencia):
B = 63.7% R = 10.2% A = 14.8% P = 11.3%
Suma en cada escenario = 100% ✓
3.6.3 El árbol de decisión aplicado
Del Capítulo 2: Del Capítulo 2, §2.2.5: el árbol de decisión tiene siete
pasos. Paso 1: ¿el nodo de mayor R* es el mismo en los tres escenarios? Si sí
→ paso 2. Si no → paso 5.
# Pregunta Respuesta Decisión
1 ¿El nodo de mayor Sí. En los tres → Paso 2
R* es el mismo en escenarios el nodo de
los tres escenarios? mayor R* es B
(banco): 51.8%,
58.0% y 63.7%.

El Método Prometeo: Imputación Causal para juristas y abogados
2 ¿El orden relativo Sí. El orden es B > A →
de todos los nodos > P > R en los tres Declaración
es el mismo en los escenarios sin A
tres escenarios? excepción.
Declaración A — Robusto: Con cualquier interpretación
razonable de la evidencia disponible en este expediente, el
banco (B) es el actor de mayor peso causal en el daño a los
clientes, con un R* que oscila entre 51.8% y 63.7% según el
supuesto adoptado. El orden de responsabilidad causal es B >
A > P > R en todo el rango. Esta conclusión no depende del
valor puntual de los pesos: es robusto a cualquier
interpretación razonable de la evidencia.
⚠ R es el nodo de menor R* aunque fue quien emitió el
dictamen que habilitó la venta. Eso no lo exime de
responsabilidad jurídica — su función de supervisión
independiente crea obligaciones que van más allá del peso
causal puro. El método mide causalidad estructural; el análisis
de deberes específicos de cargo es un elemento adicional que
el abogado debe incorporar.

El Método Prometeo: Imputación Causal para juristas y abogados
§3.7 Paso 4 en acción: calcular
S, R*_neta, α y Δ
Del Capítulo 2: Del Capítulo 2, §2.4.1: S mide la fracción de la
contribución causal que era estructural. Se calcula como promedio de tres
preguntas (A, B, C), cada una respondida con 0, 0.5 o 1. R*_neta = R* ×
(1−S). Del §2.4.2: α mide acciones concretas de asunción, incluyendo α
voluntario y α forzado. Δ = R* − α.
3.7.1 Cálculo de S para cada nodo
Criterios para estimar S (recordatorio del Capítulo 2):
Pregunta S bajo → 0 S alto → 1
A ¿El procedimiento estaba No. Alta Sí. Script rígido.
formalizado discreción.
institucionalmente?
B ¿Habría actuado igual No. Solo Sí. Cualquiera
cualquier otro actor en esa este actor. igual.
posición?
C ¿El sistema de incentivos No. Sin Sí.
determinaba esa presión. Inevitablemente.
conducta?
S del Banco (B) — nodo de diseño:
A: ¿Seguía instrucciones de alguien superior? No. A =
0.0
B: ¿Habría actuado igual cualquier banco en esa posición?
Parcialmente — la industria tenia prácticas similares
pero este banco fue deliberadamente más lejos. B =
0.4
C: ¿El sistema presionaba a B? No — B era el diseñador. C
= 0.1

El Método Prometeo: Imputación Causal para juristas y abogados
S_B = (0.0 + 0.4 + 0.1) / 3 = 0.50 / 3 = 0.17
La escala de 0 a 1 en la pregunta B es continua: 0 =
completamente idiosincrático, 1 = completamente sustituible.
0.4 refleja que el banco compartía prácticas de la industria (lo
que subiría S) pero su decisión deliberada de ir más allá lo hacía
menos sustituible (lo que baja S).
S de Riesgos (R):
A: ¿Seguía instrucciones formales? Parcialmente. A = 0.5
Mandato independiente, pero con presión documentada.
B: ¿Habría actuado igual otro director de riesgos B = 0.5
bajo la misma presión? Probablemente.
C: ¿El sistema presionaba hacia la aprobación? Si, C = 0.7
cultura de no obstaculizar el negocio documentada.
S_R = (0.5 + 0.5 + 0.7) / 3 = 1.70 / 3 = 0.57
S de los Asesores (A):
A: ¿Seguían un script obligatorio? Si, completamente. A = 1.0
B: ¿Habría actuado igual cualquier asesor bajo B = 1.0
el mismo script y las mismas metas? Si.
C: ¿El sistema de incentivos determinaba la C = 1.0
conducta? Si. Metas de colocación con
consecuencias laborales documentadas.
S_A = (1.0 + 1.0 + 1.0) / 3 = 3.0 / 3 = 1.00
S del Protocolo (P) — nodo instrumental:

El Método Prometeo: Imputación Causal para juristas y abogados
P no tiene voluntad. S no se calcula para nodos
instrumentales.
Su influencia causal es completamente derivada de B, su
diseñador.
S_P = N/A (instrumento sin voluntad)
3.7.2 Responsabilidad causal neta (R*_neta)
R*_neta = R* × (1 − S). El resultado es la contribución
idiosincrática de cada actor: lo que solo ese actor, con sus
características específicas, podría haber producido.
R*_neta para cada nodo:
B: R*_neta = 58.0% × (1 − 0.17) = 58.0% × 0.83 = 48.1%
R: R*_neta = 11.3% × (1 − 0.57) = 11.3% × 0.43 = 4.9%
A: R*_neta = 17.2% × (1 − 1.00) = 17.2% × 0.00 = 0.0%
P: N/A (nodo instrumental)
Lo que R*_neta confirma: Los asesores tienen R*_neta =
0.0%. Su contribución causal total (17.2%) era completamente
estructural: cualquier asesor en esa posición, bajo ese script y
esos incentivos, habría actuado igual. Toda la responsabilidad
idiosincrática está en el banco (48.1%) y en menor medida en
riesgos (4.9%).
Índice de sustituibilidad del banco (S_B): S_B = 0.17
indica que el banco tenía baja sustituibilidad: sus decisiones
específicas fueron condición necesaria del resultado. Eso es
coherente con su rol de nodo de diseño.
3.7.3 Cálculo de α (asunción efectiva)

El Método Prometeo: Imputación Causal para juristas y abogados
Revisamos los hechos del caso para determinar qué
acciones concretas tomó cada actor. Recordamos: α incluye
tanto asunción voluntaria como asunción forzada. El
despido y el proceso penal del asesor son α forzado que
aumentan su α, aunque no lo haya elegido.
Nodo Acciones Fuente del α Valor
verificables en el α
expediente
B — Pagó multa α voluntario α_B
Banco regulatoria mínimo: la multa =
equivalente al 8% fue impuesta por el 0.08
del capital perdido regulador (α
por los clientes forzado = 0.08). El
($384,000). Publicó comunicado de
comunicado exoneración no
exonerándose. No cuenta. Sin reforma
modificó el sistema del sistema.
de ventas.
R — Fue reubicado α forzado mínimo: α_R
Riesgos dentro del banco sin la reubicación no =
consecuencias implica pérdida de 0.03
formales. Ningún posición
pago, ningún significativa.
reconocimiento,
ninguna
modificación del
proceso de
aprobación.
A — Tres asesores fueron α forzado α_A
Asesores despedidos. Todos dominante: el =
fueron denunciados despido + el 0.62
penalmente. Tienen proceso penal + la
proceso penal pérdida de ingresos
activo. Perdieron son consecuencias
ingresos. No impuestas por el
recibieron banco, no elegidas.
compensación. Producen un α alto
aunque los asesores

El Método Prometeo: Imputación Causal para juristas y abogados
no lo hayan
deseado.
P — Instrumento sin N/A α_P
Protocolo voluntad. No tiene =
α. N/A
3.7.4 Cálculo de Δ
Δ_i = R*_i − α_i. Δ positivo: el actor causó más de lo que
asumió (déficit). Δ negativo: el actor asumió más de lo que
causó (sobre-imputación).
Calculo de Delta:
B (banco): Delta = 58.0% - 8% = +50.0% DEFICIT
SEVERO
R (riesgos): Delta = 11.3% - 3% = +8.3% DEFICIT
A (asesores): Delta = 17.2% - 62% = -44.8% SOBRE-
IMPUTACION
Nodo R* α Δ Diagnóstico
B — 58.0% 8% +50.0% Déficit severo. Causó el
Banco 58% del daño y asumió el
8%. La brecha de 50
puntos porcentuales es la
medida de lo que falta
por asumir. Base de la
pretensión principal
contra el banco.
R — 11.3% 3% +8.3% Déficit moderado. Causó
Riesgos el 11.3% y asumió el 3%.
La reubicación sin
consecuencias formales
dejó una brecha real.
Pretensión secundaria.

El Método Prometeo: Imputación Causal para juristas y abogados
A — 17.2% 62% −44.8% Sobre-imputación severa.
Asesores Los asesores causaron el
17.2% pero cargaron con
el 62% de las
consecuencias.
Argumento central de su
defensa: el sistema les
impuso consecuencias
que superan en más de
tres veces su peso causal
real.
La inversión causal cuantificada en este caso: El banco
tiene Δ = +50.0%: causó la mitad del daño y no asumió casi
nada. Los asesores tienen Δ = −44.8%: causaron menos de una
quinta parte del daño y cargaron con más de tres veces su peso.
La diferencia entre ambos Δ (+50.0% vs. −44.8%) es la medida
precisa de la inversión causal. El actor de menor peso causal
real absorbió la mayor parte de las consecuencias del sistema
que el actor de mayor peso causal diseñó.

El Método Prometeo: Imputación Causal para juristas y abogados
§3.8 Paso 5 en acción: D_total
y el ajuste debitor
Del Capítulo 2: Del Capítulo 2, §2.5.1: D_total = T_invertido +
T_impedido + ΔT_trayectoria. T_invertido es el daño emergente (lo que se
perdió). T_impedido es el lucro cesante (lo que no se ganó). ΔT_trayectoria es
la pérdida de oportunidad futura. Del §2.5.2: AD_i = R*_i × D_total.
3.8.1 Cuantificar D_total
T_invertido (daño emergente):
1,200 clientes × $4,000 capital perdido promedio =
$4,800,000
Evidencia: estados de cuenta + contratos del fondo (E1).
Impugnación posible: ninguna — cifra documentada
directamente.
T_impedido (lucro cesante):
Rendimiento de mercado comparable (CETES 2020-2022):
5.5% anual.
Periodo de afectación documentado: 2 años.
T_impedido = $4,800,000 × 5.5% × 2 = $528,000
Evidencia: tasas BANXICO publicadas + periodo en
expediente (E2).
Impugnación posible: disputa sobre tasa de referencia. Rango
conservador: 4.0% → $384,000. Rango amplio: 7% →
$672,000.
DeltaT_trayectoria (perdida de oportunidad):
Perfil de los 1,200 clientes: ahorradores de largo plazo con
historial de inversión de bajo riesgo.
Impacto documentado: deterioro del perfil crediticio,
liquidación

El Método Prometeo: Imputación Causal para juristas y abogados
de otros activos para cubrir pérdidas, acceso restringido a
productos futuros de inversión.
Estimación pericial: $360,000 (D-E4 — sujeta a
impugnación).
Nota: este componente puede ser limitado por la
jurisprudencia
local. El abogado debe verificar la admisibilidad en el fuero.
D_total del caso:
T_invertido: $4,800,000 (E1 — indiscutible)
T_impedido: $ 528,000 (E2 — defendible con pericia)
DeltaT_trayectoria: $ 360,000 (E4 — sujeta a impugnación)
D_total = $5,688,000 (base completa con los tres
componentes)
D_total_min = $4,800,000 (solo T_invertido — mínimo
seguro)
D_total_conservador = $5,328,000 (T_inv + T_imp sin
DeltaT)
3.8.2 Calcular el ajuste debitor por nodo
AD_i = R*_i × D_total. Calculamos para los tres
escenarios de D_total:
Nodo AD con AD AD R*
D_total_mi conservado completo
n ($4.8M) r ($5.33M) ($5.69M)
B — $2,784,000 $3,091,440 $3,299,52 58.0
Banco 0 %
R — $ 542,400 $ 600,264 $ 642,744 11.3
Riesgos %

El Método Prometeo: Imputación Causal para juristas y abogados
A — $ 825,600 $ 914,016 $ 979,056 17.2
Asesores %
P — $ 648,000 $ 717,960 $ 768,120 13.5
Protocol %
o
Sobre el AD del nodo P: El protocolo (P) tiene un AD calculable
porque tiene R* = 13.5%. Sin embargo, P es un instrumento sin
voluntad: no puede ser demandado ni condenado. El AD de P le pertenece
causalmente a B, su diseñador. En términos procesales, el AD de P se
suma al AD de B para calcular la pretensión total contra el banco.
AD_B_total = AD_B + AD_P = $2,784,000 + $648,000 =
$3,432,000 (usando D_total_min).

El Método Prometeo: Imputación Causal para juristas y abogados
§3.9 Los cuatro documentos
del expediente
El análisis está completo. El paso final es traducirlo a los
cuatro documentos que se presentan ante el tribunal, el
árbitro o el regulador.
3.9.1 Documento 1: la hoja de calibración
La hoja de calibración documenta cada arista del grafo con
su tipo de evidencia, su rango de peso y las limitaciones del
análisis. Es el documento que resiste la impugnación
adversarial sobre los pesos.
Arista Tipo Rango Fuente Limitaciones
E [a,b] documental explícitas
B → E1 [0.85, Script Sin limitaciones.
P 0.95] aprobado El rango refleja
(Anexo 3). que incluso
Política documentos
comercial directos pueden
firmada ser parcialmente
(Anexo 7). ambiguos.
B → E1/E3 [0.60, Memorándum La presión
R 0.78] archivado institucional se
(Anexo 4). sustenta en
Testimonios testimonios (E3),
del equipo de no en documento
riesgos directo. Si la
(Testimonios contraparte
1-3). impugna los
testimonios, el
rango cae a E6:
[0.25, 0.45].
B → E1 [0.80, Política Sin limitaciones
A 0.92] comercial con relevantes. Los

El Método Prometeo: Imputación Causal para juristas y abogados
script (Anexo documentos son
3). Contratos directos y
de incentivos verificables.
(Anexo 8).
P → E4 [0.55, Análisis La correlación
A 0.72] estadístico de estadística no es
patrón de documento
ventas (Anexo individual por
12): 40 asesor. Si la
asesores, contraparte
mismo script, demuestra
mismo variación
período. significativa entre
asesores, el rango
cae a E5.
A → E1 [0.40, 1,200 Rango moderado
C 0.58] contratos deliberado: refleja
firmados que la
(Anexo 1). discrecionalidad
real de A era
mínima por el
diseño de B. Si la
contraparte
argumenta mayor
discrecionalidad
de A, el rango
sube — y con ello
el R* de A, no el
de B.
3.9.2 Documento 2: la tabla de sensibilidad
Nodo R* R* R* ¿Cambia el
mínim centra máxim liderazgo?
o l o
B — Banco 51.8% 58.0% 63.7% No. B lidera en
los tres
escenarios.

El Método Prometeo: Imputación Causal para juristas y abogados
P — 15.5% 13.5% 11.3% No aplica
Protocolo (instrumento).
A — 20.3% 17.2% 14.8% A es siempre el
Asesores segundo entre los
nodos con
voluntad.
R — 12.4% 11.3% 10.2% R es siempre el
Riesgos menor entre los
nodos con
voluntad.
Diagnóstic DECLARACIÓ
o N A — Análisis
robusto
3.9.3 Documento 3: la declaración de
robustez (para el expediente)
Declaración de robustez — para insertar en el expediente:
El análisis causal del presente caso, realizado mediante el
método de distribución de responsabilidad del Método
Prometeo de Imputación Causal, produce una Declaración A:
con cualquier interpretación razonable de la evidencia
disponible en el expediente, el Banco (B) es el actor de mayor
peso causal en el daño a los clientes, con un R* que oscila entre
51.8% y 63.7% según el supuesto de calibración adoptado. El
orden de responsabilidad causal es B > A > R en todo el rango
razonable de la evidencia. Esta conclusión es robusta: para que
cambiara, la contraparte tendría que demostrar que existe una
interpretación razonable de la evidencia bajo la cual algún otro
actor supera al banco en peso causal. El análisis de sensibilidad
adjunto demuestra que no existe tal interpretación dentro del
rango documentado.
3.9.4 Documento 4: la tabla de D_total y AD

El Método Prometeo: Imputación Causal para juristas y abogados
Component Monto Tipo Estado Nota
e evidenc
ia
T_invertido $4,800,0 E1 Indiscutib 1,200
00 le contratos
× $4,000
promedio.
T_impedido $528,000 E2 Defendibl Tasa
e CETES
5.5% × 2
años.
ΔT_trayecto $360,000 E4 Disputada Sujeta a
ria admisibilid
ad del
fuero.
D_total $5,688,0 Base para
00 AD.
Presentar
mínimo
($4.8M) y
completo
($5.69M).
Nodo R* AD AD (D_total
(D_total_min) completo)
B (+ P) 71.5% $3,432,000 $4,067,640
R — 11.3% $542,400 $642,744
Riesgos
A — 17.2% $825,600 $979,056
Asesores
Por qué se suman B y P en el AD: P es un instrumento sin
voluntad. No puede ser demandado. Su R* (13.5%) le corresponde
causalmente a B, que lo diseñó. Por eso en la tabla de AD se presenta
como "B (+P)": el banco responde por su propio R* más por el R* del

El Método Prometeo: Imputación Causal para juristas y abogados
instrumento que creó. Esta suma (58.0% + 13.5% = 71.5%) es la base
de la pretensión total contra el banco.

El Método Prometeo: Imputación Causal para juristas y abogados
§3.10 El perfil completo del
caso: todos los números
Esta tabla presenta el perfil completo de todos los actores
del caso con todos los indicadores calculados en este
capítulo. Es la síntesis del análisis.
Actor R* B* S R*n α Δ AD
eta (D_min
)
B — 58.0 77.4 0.1 48.1 0.0 +50. $3,432,0
Banco % % 7 % 8 0% 00*
P — 13.5 0% N/ N/A N/ N/A (*incluid
Protoc % A A o en B)
olo
A — 17.2 10.1 1.0 0.0% 0.6 −44. $825,60
Asesor % % 0 2 8% 0
es
R — 11.3 12.6 0.5 4.9% 0.0 +8.3 $542,40
Riesgo % % 7 3 % 0
s
⚠ El nodo colectivo como agregado: En este caso
didáctico, hemos tratado al banco (B) como un nodo único
para simplificar la exposición. En un análisis real, el nodo
"banco" debe desagregarse en los individuos que tomaron las
decisiones relevantes: CEO, director de marketing, jefe de
productos, comité de inversiones, etc. Cada uno tendrá su
propio R, su propia S, su propio α y su propio Δ. El método no prescribe
que las instituciones sean tratadas como personas; prescribe que se
identifiquen todos los nodos causales, incluyendo a los individuos dentro de
las instituciones. En este caso, el R agregado del banco (58.0%) es
la suma de los R* de esos individuos. Algunos de ellos pueden
tener S baja (actuaron idiosincráticamente) y R* alto. Esos son
los que deben responder personalmente.

El Método Prometeo: Imputación Causal para juristas y abogados
Lo que este capítulo ejecutó
✓ Paso 1: el grafo del caso con cinco nodos (B, R, A, P, C) y
ocho aristas clasificadas por tipo y documentadas con
evidencia del expediente.
✓ Paso 2: rangos de peso asignados arista por arista usando la
tabla E0-E8. Cada rango justificado por el tipo de evidencia
disponible.
✓ Paso 3 — R*: el banco tiene R* = 58.0%, los asesores 17.2%,
el protocolo 13.5%, riesgos 11.3%. Resultado robusto en los
tres escenarios: Declaración A.
✓ Paso 3 — B*: el banco obtuvo el 77.4% del beneficio del
evento. Los asesores el 10.1%. El instrumento P tiene B* =
0%. La comparación R*/B* confirma el perfil diseñador-
beneficiario del banco.
✓ Paso 4: S_banco = 0.17, S_asesores = 1.00. R*_neta del asesor
= 0.0%. α del asesor = 0.62 (α forzado por el despido y el
proceso). Δ del banco = +50.0%, Δ del asesor = −44.8%.
✓ Paso 5: D_total = $5,688,000 ($4,800,000 indiscutibles +
$528,000 defendibles + $360,000 disputados). AD del banco
= $3,432,000 (mínimo). AD del asesor = $825,600.
✓ Los cuatro documentos del expediente: hoja de calibración
con limitaciones explícitas, tabla de sensibilidad, declaración
de robustez lista para insertar, y tabla de D_total y AD.

El Método Prometeo: Imputación Causal para juristas y abogados
EL MÉTODO PROMETEO · IMPUTACIÓN CAUSAL

