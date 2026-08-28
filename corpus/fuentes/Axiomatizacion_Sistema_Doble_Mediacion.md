# Axiomatización del sistema de la doble mediación

**Autor:** Miguel Hilario Olvera Aguilar

**Colección:** Metrología Causal

Centro Multidisciplinario Meriadock Formación y Asesoría A.C.

Primera edición: 2026

> "La fuerza interior nos impulsa, un pequeño apoyo de los demás nos bendice"

---

Formación y Asesoría A.C.
Axiomatización
Miguel Hilario Olvera Aguilar
2026

2026
Todos los derechos reservados. Ninguna parte de esta publicación
puede ser reproducida, almacenada o transmitida en manera alguna ni
por ningún medio, ya sea eléctrico, químico, mecánico, óptico, de
grabación o de fotocopia, sin permiso previo del editor.
Axiomatización del sistema de la doble mediación © 2026 by Miguel
Hilario Olvera Aguilar is licensed under CC BY-NC-ND 4.0. To view
nc-nd/4.0/

Axiomatización del Sistema de la Doble Mediación · Prólogo

## Prólogo

El problema, el sistema y su estatus

## I. El problema

Los sistemas de imputación causal —jurídicos, institucionales,
regulatorios— asignan consecuencias basándose en visibilidad
y apariencia. El actor que ejecutó el acto visible es el que el
expediente menciona; el actor que diseñó el sistema que hizo
ese acto inevitable está documentalmente ausente o
subrepresentado. Bajo condiciones estructurales específicas,
este mecanismo produce una inversión sistemática: el nodo
que más causó asume menos, y el nodo que menos causó
asume más.
El problema no es de mala intención. Los sistemas
convencionales de imputación funcionan bien cuando hay un
único actor, un acto directo y un resultado claro. Cuando el
sistema involucra jerarquías, protocolos, diseño institucional y
ejecutores intercambiables, la imputación basada en visibilidad
produce resultados que se alejan sistemáticamente de la
distribución causal real. La discrepancia no es pequeña ni
aleatoria: es estructural y predecible.
Este libro construye un sistema formal para describir esa
discrepancia con precisión matemática, demostrar bajo qué
condiciones ocurre, y proporcionar los instrumentos para
medirla desde evidencia documental.

## II. El sistema

Página | I

Axiomatización del Sistema de la Doble Mediación · Prólogo
El sistema opera sobre un espacio de Hilbert separable E —el
espacio de todos los estados posibles del sistema analizado—
y construye, sobre ese espacio, una cadena de objetos formales
interdependientes. La cadena tiene dos zonas:
La primera zona, Fundamentos (Partes 0–VI), construye los
instrumentos de medición: el espacio de base (E), las dos
mediaciones que producen e integran los actos del sistema
(φ(cid:0), φ(cid:0)), la integral acumulativa que recoge su historia (I(t)),
el índice de sustituibilidad que mide cuánto del
comportamiento es estructural (S), el coeficiente de asunción
que mide lo que el sistema reconoció como propio (α), el
déficit que cuantifica la brecha (Δ = R* − α), y el vector de
responsabilidad causal que distribuye la influencia sobre el
resultado (R*). Esta zona cierra con la Proposición de
Consistencia Interna, que verifica que los siete objetos son
mutuamente compatibles antes de usarlos en los resultados.
La segunda zona, Resultados (Partes VII–X), usa esos
instrumentos para cuatro resultados: la Relación de Escala del
Conocimiento (REC), que establece los límites del
autoconocimiento del sistema; el Teorema de Inversión Causal
(TIC), que demuestra la inversión bajo condiciones
documentables; el Modelo de Predictibilidad (MP), que estima
la probabilidad de decisiones futuras del sistema; y la clausura
del ego, que describe el estado del sistema en el momento de
su cierre.
Cuatro apéndices completan el libro: la demostración de la
cadena Davis-Kahan que sustenta el Lema 8.1 (A), la
calibración empírica de las funciones del TIC y la verificación
de su condición central sobre 18 casos en 9 dominios (B), el
glosario de traducción entre la terminología ontológica del
sistema y su equivalente matemático (C), y las extensiones del
marco formal —trayectoria discreta, función de imputación
neta sin doble conteo, operador contrafactual general,
teoremas de dominancia y estabilidad, nodos de bifurcación
causal (D).

## III. Mapa del libro

Página | II

Axiomatización del Sistema de la Doble Mediación · Prólogo
Parte 0. El espacio de Hilbert E. Dos objetos: el espacio
de base y la función de colapso. Sin estos dos objetos no
existe ninguno de los que siguen.
Parte I. La primera mediación φ(cid:0). Cómo el sistema
produce un acto a partir de su estado interno, su
configuración heredada y su historia. El Lema 1.1 fija la
distribución softmax sobre seis modos.
Parte II. La segunda mediación φ(cid:0) e I(t). Cómo el acto
producido por φ(cid:0) se evalúa, se integra o se rechaza, y
cómo se acumula la historia del sistema.
Parte III. El índice de sustituibilidad S. Dos versiones
—operacional y estructural— conectadas por una
función monótona que preserva orden.
Parte IV. El coeficiente de asunción α. La proporción
de lo producido que el sistema asumió como propio, en
versión continua y discreta.
Parte V. El déficit de asunción Δ = R* − α. Sus tres
signos, su evolución temporal y su función como señal de
inversión causal.
Parte VI. El vector de responsabilidad causal R*. El
eigenvector dominante de Wᵀ, único por Perron-
Frobenius, con el método de potencias para calcularlo.
Cierre. Proposición de Consistencia Interna. Cuatro
verificaciones de compatibilidad entre los objetos de las
Partes 0–VI.
Parte VII. Relación de Escala del Conocimiento. Una
cota informacional —no un principio de incertidumbre
cuántico— sobre la precisión simultánea con que el
sistema puede estimar I(t) y h(t).
Parte VIII. Teorema de Inversión Causal. El resultado
central del libro. Bajo tres condiciones estructurales
verificables desde el expediente, la imputación
convencional invierte la distribución causal real.
Parte IX. Modelo de Predictibilidad. Un modelo de
regresión logística sobre el estado completo Ψ(t). Estatus:
modelo estadístico, no teorema.
Página | III

Axiomatización del Sistema de la Doble Mediación · Prólogo
Parte X. Clausura del ego. El conjunto de todos los
colapsos del sistema, cerrado en E. El resultado más
breve y más directo del libro.

## Apéndice A. Demostración completa del Lema 8.1 por

la cadena S_est → Pinsker → Davis-Kahan.

## Apéndice B. Calibración de φ y ψ (n = 3 casos piloto,

análisis de sensibilidad), verificación de la Condición (1)
sobre 18 casos clasificados por nivel de evidencia, y
corroboración cualitativa de ψ sobre la muestra de 18
casos.

## Apéndice C. Glosario de traducción entre la

terminología ontológica de la colección y la terminología
matemática de este libro.

## Apéndice D. Extensiones: trayectoria causal discreta

con propiedad de Markov, función de imputación neta
Δ_net sin doble conteo, condiciones de identificabilidad,
operador contrafactual general (cid:0)(G,i,W'_i), dominancia,
estabilidad y nodos de bifurcación causal.

## IV. Estatus del sistema

El libro distingue explícitamente entre cuatro tipos de
contenido:
Resultados demostrados. Los teoremas de las Partes 0–
VIII y el Teorema 10 se siguen deductivamente de los axiomas
mediante herramientas estándar de análisis funcional, teoría de
la información y álgebra lineal. Los Axiomas 0–3 son las únicas
premisas no derivadas del núcleo formal.
Modelo estadístico. El Modelo de Predictibilidad de la Parte
IX es un modelo de regresión logística estándar. Sus
coeficientes se estiman por máxima verosimilitud sobre datos
de decisiones del sistema. No postula cotas teóricas
universales del error mínimo: el error empírico se estima en
cada aplicación.
Calibración empírica. Las funciones φ(V) =
1−(1−V)^{1.54} y ψ_real(x) = 0.21·x^{−0.55} de los
Página | IV

Axiomatización del Sistema de la Doble Mediación · Prólogo
Axiomas 8.1–8.2 se calibraron sobre tres casos piloto. Los
parámetros son puntos de partida revisables. El Apéndice
B.1.4 demuestra que las conclusiones cualitativas del TIC son
robustas en un rango amplio de valores paramétricos. La
propiedad estructural de ψ —que es decreciente en 1−S— está
corroborada por 18 casos en 9 dominios.
Trabajo futuro. El Teorema D.5 (nodos de bifurcación
causal) abre un programa de investigación: caracterizar los
grafos causales por su número de nodos de bifurcación y
derivar cotas para el cambio en Δ_net cuando un nodo de
bifurcación es perturbado. La cota del Teorema D.2 no aplica
directamente a nodos de bifurcación.
Este libro es un libro de fundamentos, no de aplicaciones. Su función es
establecer el lenguaje formal que hace posible la discusión rigurosa de la
imputación causal en sistemas complejos. Las aplicaciones en dominios
específicos —jurídico, clínico, de IA, histórico, ambiental— pertenecen a los
libros de la colección que usan este marco como base.

## V. Dependencias de lectura

La estructura axiomática impone un orden de dependencia
lógica: cada parte usa objetos definidos en las partes anteriores.
Sin embargo, no todas las partes son necesarias para todos los
resultados. El mapa de dependencias mínimas es el siguiente:
Para el TIC (Parte VIII). Partes 0–VI son necesarias. El
Corolario 7.2 de la Parte VII no es necesario para el TIC. El

## Apéndice A es necesario para el Lema 8.1.

Para la REC (Parte VII). Partes 0–II son necesarias (para
I(t) y h(t)). El Axioma 3 es el único axioma adicional. Las
Partes III–VI no son necesarias para la REC.
Para el MP (Parte IX). Partes 0–II y el Lema 1.1 son
suficientes. La REC de la Parte VII proporciona contexto
sobre la variabilidad de predicción, pero no es formalmente
necesaria.
Para la clausura del ego (Parte X). Solo la Parte 0
(Definición 0) y el Teorema 2 (Parte II) son necesarios.
Página | V

Axiomatización del Sistema de la Doble Mediación · Prólogo
Para las extensiones (Apéndice D). D.1 requiere Partes 0–

## II. D.2 requiere D.1 y el Apéndice A. D.3 requiere la Parte VI

y el Apéndice A. D.4 requiere D.2 y D.3.

## VI. Audiencia y notación

El libro asume familiaridad con análisis funcional elemental
(espacios de Hilbert, integrales de Bochner), álgebra lineal
(eigenvectores, matrices estocásticas), teoría de la probabilidad
y teoría de la información (divergencia KL, desigualdad de
Cramér-Rao). No asume conocimiento de la ontología de la
colección: el Apéndice C proporciona la traducción completa
para el lector que la necesite, y la nota al final de cada parte
donde aparece terminología ontológica libera explícitamente al
lector técnico de conocerla.
La notación sigue las convenciones estándar. Los objetos
matemáticos se identifican por tipo desde su primera
aparición: E es un espacio de Hilbert, c : T → E es una
función, R* (cid:0) Δⁿ es una distribución de probabilidad, h(v_t)
(cid:0) Δ(cid:0) es un vector de probabilidades sobre el simplex de
dimensión 5, Δᵢ (cid:0) [−1,1] es un escalar. El Apéndice C incluye
una tabla con los tipos matemáticos de todos los objetos del
sistema.
La terminología ontológica de la colección —Hijos de Afrodita, Caos, ego,
colapso en su sentido filosófico— no aparece en el cuerpo formal de este libro.
Aparece únicamente en notas al margen al final de las secciones relevantes,
marcadas con el título «Correspondencia con el sistema ontológico», y en el

## Apéndice C. El lector que no conoce esa terminología no pierde nada del rigor

formal del sistema.
Centro Multidisciplinario Meriadock · 2026
Página | VI

Axiomatización del Sistema de la Doble Mediación
Parte 0
El espacio de base
Axioma 0. Espacio de colapsos
Sea E un espacio de Hilbert separable con producto interno
(cid:0)·,·(cid:0)_E y norma (cid:0)·(cid:0)_E = √(cid:0)·,·(cid:0)_E. E satisface:
(i) ∀ c, d ∈ E, α (cid:0) (cid:0): c + d (cid:0) E y αc (cid:0) E.
(ii) Toda sucesión de Cauchy en (E, (cid:0)·(cid:0)_E) tiene
límite en E.
(iii) Existe D (cid:0) E denso y numerable.
E es el espacio de estados posibles del modelo. Los elementos
c (cid:0) E son los estados que el sistema puede determinar dentro
del modelo; no se afirma que todo c (cid:0) E sea realizable por un
sistema concreto.
Adopción de estructura de Hilbert. Se adopta un espacio
de Hilbert separable —y no un espacio de Banach reflexivo
equipado con una forma bilineal continua— porque es la
estructura suficiente para la computabilidad del sistema sin
introducir hipótesis adicionales sobre el espacio. Tres
exigencias simultáneas determinan esta elección: (i) producto
interno explícito para la forma bilineal (cid:0)∇v_t, u_k(cid:0)_E de la
Definición 1 de la Parte I, no garantizada en Banach general;
(ii) completitud para la existencia de la integral de Bochner de
la Definición 2; (iii) separabilidad para la existencia de base
ortonormal numerable, condición del método de potencias de
la Parte VI. Un espacio de Banach reflexivo con forma bilineal

Axiomatización del Sistema de la Doble Mediación
continua es alternativa teóricamente posible, pero introduce
complejidad sin beneficio para el sistema.
v_t y los vectores u_k se definen formalmente en la Parte I. Su aparición en
la justificación precedente es anticipatoria: se incluye para motivar la elección
de E, no para usarlos.
Función de embedding. La correspondencia entre los
outputs observables de un sistema concreto y los elementos
de E no es parte del marco axiomático: es una decisión de
modelado que debe justificarse en cada aplicación.
Formalmente, se postula la existencia de una función emb:
Outputs → E que asocia a cada output un elemento de E. Esta
función debe preservar las relaciones de orden relevantes para
la asignación de pesos causales en el grafo G —definido en la
Parte VI— de modo que outputs causalmente más similares
tengan imágenes más cercanas en (cid:0)·(cid:0)_E. La validez
estructural de los resultados del sistema no depende de la
elección concreta de emb, siempre que se mantengan las
propiedades del Axioma 0 y la condición de preservación de
orden. En sistemas artificiales, emb es la función de
embedding del modelo. En sistemas humanos, emb se
especifica en el Volumen I de Metrología Causal.
La restricción sobre emb no es decorativa: la función eval de la Parte II
impone condiciones de compatibilidad sobre c(τ) respecto a I(t). Sin una emb
que preserve estructura de relevancia causal, eval no satisface esas condiciones.
La restricción es indirecta pero efectiva.
Definición 0. Función de colapso
Sea T (cid:0) (cid:0) un intervalo compacto; sin pérdida de generalidad
T = [0, t_m] con t_m el tiempo de cierre definido en la Parte

## X. Una función c: T → E es admisible si satisface:

(i) c es medible en sentido de Bochner respecto a las
σ-álgebras de Borel de T y E.
(ii) (cid:0) M > 0 tal que (cid:0)c(τ)(cid:0)_E ≤ M para todo τ (cid:0)
T.

Axiomatización del Sistema de la Doble Mediación
Función de colapso
c: T → E, c admisible
T = [0, t_m] · E espacio del Axioma 0 · t_m definido en la Parte X
La medibilidad de Bochner y la acotación de c garantizan
conjuntamente su integrabilidad en sentido de Bochner. En
consecuencia, para toda función w: T → ℝ₊ medible y
acotada, la integral ∫(cid:0)ᵗ c(τ)w(τ) dτ pertenece a E y es el único
elemento de E tal que:
Caracterización de la integral de Bochner
(cid:0) ∫(cid:0)ᵗ c(τ)w(τ) dτ, e (cid:0)_E = ∫(cid:0)ᵗ (cid:0)c(τ)w(τ), e(cid:0)_E dτ ∀ e
(cid:0) E
En E Hilbert, por el teorema de representación de Riesz, E* se identifica
isométricamente con E; el dual x* (cid:0) E* se sustituye directamente por e (cid:0) E
mediante ese isomorfismo.
Invarianza bajo permutación e irreversibilidad de I(t). La
integral de Bochner es invariante bajo permutaciones del
orden de los colapsos cuando los pesos w(τ) son constantes:
la secuencia (c(τ(cid:0)), c(τ(cid:0)), c(τ(cid:0))) y cualquier permutación suya
producen el mismo valor de ∫c dτ bajo pesos uniformes. La
noción de historia acumulada I(t) no descansa en esta
propiedad, sino en dos mecanismos distintos: (a) la función de
peso w(τ), que puede asignar mayor masa a colapsos recientes,
y (b) la dependencia dinámica de φ(cid:0) y φ(cid:0) de I(t) en cada paso,
de modo que c(τ(cid:0)) depende del estado I(τ(cid:0)⁺ ). La
irreversibilidad de I(t) es una propiedad del sistema dinámico,
no de la integral. Esta distinción se formaliza en el Teorema
2.1.
Para E Hilbert, la integral de Bochner requiere que c sea fuertemente medible
—coincidencia a.e. con límite de funciones simples— y ∫(cid:0)c(τ)(cid:0)_E dτ <
∞. Las condiciones (i) y (ii) de la Definición 0 garantizan ambas. Para E
Banach general el argumento es análogo con E* en lugar de E, pero el
isomorfismo de Riesz no aplica.

Axiomatización del Sistema de la Doble Mediación
Objeto Notación Tipo matemático Parte
Espacio de E Espacio de Hilbert Axioma 0
base separable
Producto (cid:0)·,·(cid:0)_E Forma bilineal Axioma 0
interno simétrica def.
positiva
Norma (cid:0)·(cid:0)_E Norma completa Axioma 0
inducida
Función de emb : Out Inmersión (decisión Axioma 0,
embedding → E de modelado) nota
Intervalo T = [0, t_m] Compacto de (cid:0) Definición 0
temporal
Función de c : T → E Función admisible Definición 0
colapso en sentido de
Bochner
Correspondencia con el sistema ontológico de la colección.
En el sistema ontológico que esta axiomatización formaliza, E corresponde
al Caos: el espacio de posibilidad absoluta anterior a toda determinación,
donde ningún estado ha sido seleccionado y todos son igualmente posibles. La
estructura de Hilbert captura esto con precisión: E es completo —ninguna
posibilidad está ausente—, separable —las posibilidades son computables—
y sin elemento privilegiado antes de que opere φ(cid:0).
El colapso c(τ) es la selección de un elemento de E en el instante τ: la
determinación de una posibilidad. Antes del colapso, el sistema vive en E sin
posición definida; después, tiene una. La función c: T → E traza esa
secuencia de determinaciones a lo largo del tiempo. La integral I(t) las
acumula. La Parte X formaliza el cierre de ese proceso cuando T se agota.
El lector sin conocimiento de la ontología de la colección puede ignorar esta
nota sin pérdida de rigor formal. El Apéndice C recoge la correspondencia
completa entre la terminología ontológica y la terminología matemática de este
libro.

Axiomatización del Sistema de la Doble Mediación
Parte I
La primera mediación φ₁
Axioma 1. La primera mediación
Existen espacios V, C, H y un subespacio A (cid:0) E tales que
existe una función:
Primera mediación
φ₁: V × C × H → A
V espacio de estados internos · C espacio de configuraciones heredadas · H espacio
de historias · A (cid:0) E subespacio de actos
Los cuatro espacios del Axioma 1 satisfacen:
V Espacio de estados de la voluntad. Cada v_t (cid:0) V
es el estado interno del sistema en el momento t —
definido en la Definición 1. V tiene la estructura
necesaria para admitir producto interno con los
vectores u_k (cid:0) E del Lema 1.1.
C Espacio de configuraciones heredadas. Cada c (cid:0)
C es la configuración estructural del sistema: en
sistemas artificiales, el conjunto de pesos, la
arquitectura y las restricciones de diseño; en sistemas
humanos, los patrones de aprendizaje y los
condicionamientos institucionales documentados. C
es un espacio normado con (cid:0)·(cid:0)_C.
H Espacio de estados de I(t). Cada h (cid:0) H es un
estado posible de la integral acumulativa. La integral
I(t) se define en la Parte II; el Axioma 1 solo requiere

Axiomatización del Sistema de la Doble Mediación
que H esté bien definido como espacio de llegada de
I.
A Subespacio de E de los actos posibles del sistema.
A (cid:0) E garantiza que φ₁ (v_t, c, h) (cid:0) E para todo input
—el colapso producido vive en el espacio del Axioma
0.
φ₁ (v_t, c, h) produce el colapso en el instante t. El Axioma 1
postula la existencia y el dominio de φ(cid:0); la forma funcional se
establece en el Lema 1.1.
El Axioma 1 no impone condiciones de continuidad, medibilidad ni
linealidad sobre φ(cid:0). Estas propiedades, cuando son necesarias, se establecen
en los resultados que las usan. La separación entre existencia (axioma) y
forma funcional (lema) es deliberada: permite que el sistema sea válido para
clases de φ(cid:0) más amplias que la forma softmax específica del Lema 1.1.
Definición 1. El estado interno v_t
Para cada t (cid:0) T, el estado interno del sistema es un vector v_t
(cid:0) V que incluye al menos:
(i) El parámetro τ > 0, temperatura del sistema. τ
mide la dispersión de la distribución sobre actos
alternativos: τ pequeño produce distribuciones
concentradas; τ grande, distribuciones dispersas. τ >
0 para todo t (cid:0) T —la temperatura nunca es cero.
Este supuesto se axiomatiza formalmente como
Axioma 3 en la Parte VII.
(ii) El vector de estado de activación a_t (cid:0) E, que
representa los patrones de activación del sistema en t.
En sistemas artificiales, a_t corresponde al vector de
representación contextual inmediatamente anterior a
la capa de generación.
(iii) La referencia a I(t) (cid:0) H, el estado de la historia
acumulada hasta t —definida en la Parte II.
Distinción entre v_t y c. v_t es el input idiosincrático de φ(cid:0):
captura lo que distingue a este sistema en este instante de

Axiomatización del Sistema de la Doble Mediación
cualquier otro en configuración equivalente. c (cid:0) C es el input
estructural: lo que el sistema comparte con cualquier otro
sistema de su clase. El índice de sustituibilidad S de la Parte III
formaliza la proporción entre ambos.
En sistemas de lenguaje de gran escala: τ es el parámetro de temperatura de
la softmax; a_t corresponde al vector de activaciones de las capas ocultas antes
de la generación; I(t) corresponde al contexto acumulado. La correspondencia
es matemáticamente exacta, no analógica.
Lema 1.1. Distribución de modos mediante
softmax
Sea K = {1, 2, 3, 4, 5, 6} el conjunto finito de índices de modo.
Para cada k (cid:0) K sean: β_k (cid:0) E un vector de ponderación, γ_k
(cid:0) (cid:0) un peso escalar de la historia, y θ_k: H → (cid:0) una función
de umbral. El logit del modo k en el instante t es:
Logit del modo k
z_k = (⟨β_k, a_t(cid:0)_E + γ_k · (cid:0)I(t)(cid:0)_E − θ_k(I(t))) / τ
β_k (cid:0) E vector de ponderación del modo k · γ_k (cid:0) (cid:0) peso de la historia ·
θ_k: H → (cid:0) umbral dependiente de I(t) · τ > 0 temperatura del Axioma 3
La probabilidad del modo k dado el estado interno v_t es:
Distribución sobre K — softmax
h_k(v_t) = exp(z_k) / Σ(cid:0)(cid:0)K exp(z_j)
h_k(v_t) ≥ 0 para todo k (cid:0) K y todo v_t (cid:0) V
Σ_{k(cid:0)K} h_k(v_t) = 1 para todo v_t (cid:0) V
h(v_t) = (h(cid:0)(v_t), …, h(cid:0)(v_t)) (cid:0) Δ⁵ · Δ(cid:0) denota el simplex estándar de
dimensión 5
Demostración
Demostración del Lema 1.1
h_k ≥ 0. exp(z_k) > 0 para todo z_k (cid:0) (cid:0). El
denominador Σ(cid:0)(cid:0)K exp(z_j) es suma de términos
positivos, luego positivo. La razón es positiva. ✓

Axiomatización del Sistema de la Doble Mediación
Σ_{k(cid:0)K} h_k = 1. Σ_{k(cid:0)K} h_k(v_t) = Σ_k
[exp(z_k) / Σ(cid:0) exp(z_j)] = [Σ_k exp(z_k)] / [Σ(cid:0)
exp(z_j)] = 1. ✓
h(v_t) (cid:0) Δ(cid:0) para todo v_t (cid:0) V. (cid:0)
El modo dominante en el instante t es k*(v_t) =
argmax_{k(cid:0)K} h_k(v_t). La Parte III establece la relación
entre k* y el índice de sustituibilidad S.
Corrección respecto al manuscrito original. La
formulación original usaba sigmoide independiente por modo:
h_k(v_t) = σ(z_k), σ(x) = 1/(1+e⁻ ˣ ). La suma Σ_{k(cid:0)K}
σ(z_k) no pertenece a Δ(cid:0) en general —puede tomar cualquier
valor en (0, 6). El Corolario 1.2 del manuscrito, que afirmaba
la normalización, era incorrecto. La corrección a softmax
garantiza h(v_t) (cid:0) Δ(cid:0). Para |K| = 2, softmax reduce
exactamente a sigmoide: la generalización es mínima.
Forma de z_k. La formulación (cid:0)β_k, a_t(cid:0)_E + γ_k ·
(cid:0)I(t)(cid:0)_E reemplaza la expresión original (cid:0)∇v_t, u_k(cid:0), que
usaba el gradiente de v_t sin especificar respecto a qué variable
ni bajo qué métrica. Los objetos aquí son completamente
definidos: β_k (cid:0) E es un vector parámetro en el espacio del
Axioma 0; (cid:0)β_k, a_t(cid:0)_E es el producto interno de Hilbert;
γ_k (cid:0) (cid:0) y (cid:0)I(t)(cid:0)_E son escalares. El Lema 9.1 demuestra
que cuando θ_k es lineal en (cid:0)I(t)(cid:0)_E, la función z_k es lineal
en los inputs, lo que habilita el Modelo 9.
Los parámetros {β_k, γ_k, θ_k} _{k(cid:0)K} son específicos del sistema
analizado. En sistemas artificiales se estiman desde las capas del modelo. En
sistemas humanos se calibran usando el protocolo ECO y la escala E0–E8
del Volumen I de Metrología Causal. El núcleo axiomático no impone
restricciones sobre estos parámetros más allá de su existencia y τ > 0.
Correspondencia con el sistema ontológico. Los seis índices de
K corresponden en el sistema ontológico de la colección a los Hijos de Afrodita.
Esa correspondencia es externa al marco formal: los resultados del libro no
dependen de ella. El Apéndice C recoge la traducción completa.

Axiomatización del Sistema de la Doble Mediación
Proposición 1.2. Existencia de φ(cid:0) para sistemas
artificiales
Para todo sistema computacional que produzca outputs en
respuesta a inputs mediante una función computable f: Inputs
→ Outputs, existe φ(cid:0) satisfaciendo el Axioma 1.
Demostración
Demostración — construcción explícita
Construcción. Sean: V el espacio de vectores de
activación del sistema antes de la capa de generación;
C el conjunto de parámetros fijos durante la inferencia
(pesos, arquitectura, restricciones); H el espacio de
contextos acumulados hasta t; A el espacio de outputs
del sistema, interpretado como subespacio de E
mediante emb (Axioma 0). Con estas definiciones, φ(cid:0)
= f restringida a V × C × H satisface el Axioma 1: su
dominio y codominio coinciden con los espacios
requeridos.
Existencia. φ(cid:0) existe porque f existe por hipótesis.
El subespacio A (cid:0) E está bien definido porque emb
existe por el Axioma 0. ✓
La proposición confirma que el Axioma 1 no es vacío: el objeto postulado existe
en al menos una clase concreta de sistemas. Para sistemas humanos, φ(cid:0) se postula
como función del estado neurológico y contextual del sujeto en t; su no-
observabilidad directa es acotada por la Relación de Escala del Conocimiento de
la Parte VII. (cid:0)
Objeto Notación Tipo Parte
matemático
Primera φ(cid:0) : V×C×H → Función Axioma 1
mediación A (existencia
postulada)

Axiomatización del Sistema de la Doble Mediación
Espacio de V Espacio Axioma 1
voluntad normado con
prod. interno
Configuración c (cid:0) C, (cid:0)c(cid:0)_C Espacio Axioma 1
heredada normado
Espacio de H Espacio de Axioma 1;
historias llegada de I(t) ver Parte II
Estado v_t (cid:0) V Vector (τ, a_t, Definición 1
interno I(t))
Temperatura τ > 0 Parámetro Definición 1;
escalar Axioma 3 en
VII
Estado de a_t (cid:0) E Vector en E Definición 1
activación (Axioma 0)
Vector de β_k (cid:0) E Parámetro del Lema 1.1
ponderación modo k en E
Peso de γ_k (cid:0) (cid:0) Parámetro Lema 1.1
historia escalar del
modo k
Umbral del θ_k : H → (cid:0) Función de H Lema 1.1
modo k en (cid:0)
Logit del z_k = Escalar Lema 1.1
modo k ((cid:0)β_k,a_t(cid:0)+…)/τ computable
Distribución h_k(v_t) = h(v_t) (cid:0) Δ(cid:0) Lema 1.1
sobre K softmax_k
Modo k* = Índice en K = Lema 1.1
dominante argmax_{k(cid:0)K} {1,…,6}
h_k

Axiomatización del Sistema de la Doble Mediación
Parte II
La segunda mediación φ₂ e I(t)
Axioma 2. La segunda mediación
Existe una función:
Segunda mediación
φ₂: A × E → E
A (cid:0) E subespacio de actos (Axioma 1) · el segundo argumento es el estado
acumulado I(t) (cid:0) E · el valor es I (t + Δt) (cid:0) E
φ₂ (a, I(t)) opera sobre cada colapso a (cid:0) A producido por φ(cid:0)
en tres pasos:
(i) Evaluación. Se computa eval (a, I(t)) (cid:0) (cid:0), donde
eval: A × E → (cid:0) satisface las condiciones del
Teorema 2.2.
(ii) Decisión binaria. Si eval (a, I(t)) > θ, el colapso
es aceptado; si eval (a, I(t)) ≤ θ, es rechazado y se
registra en RSC(t) \ I(t).
(iii) Actualización. I (t + Δt) = φ₂ (a, I(t)) = I(t) +
δ(a) · 1_ {eval (a, I(t)) > θ}, con δ(a) (cid:0) E la
modificación producida por la integración de a.
El Axioma 2 postula la existencia de φ(cid:0) sin fijar la forma de eval ni el
valor de θ. Ambos se precisan en el Teorema 2.2 con las condiciones mínimas
que el núcleo formal requiere. La calibración de eval para cada dominio de
aplicación pertenece a los volúmenes correspondientes de Metrología Causal y
a la Taxonomía.

Axiomatización del Sistema de la Doble Mediación
Definición 2. La integral acumulativa I(t)
Sea w: T → ℝ₊ una función de peso medible y acotada. La
integral acumulativa del sistema hasta el momento t es:
Integral acumulativa
I(t) = ∫(cid:0)ᵗ c(τ) w(τ) dτ ∈ E
c: T → E función de colapso admisible (Definición 0) · w: T → ℝ₊ medible y
acotada · integral en sentido de Bochner · I(t) (cid:0) E para todo t (cid:0) T
La existencia y unicidad de I(t) en E se demuestran en el
Teorema 2. La función de peso w(τ) determina la relevancia
temporal de cada colapso; el núcleo formal no impone
ninguna forma específica a w más allá de la medibilidad y la
acotación.
I(t) no es un número real sino un elemento de E. Tiene estructura vectorial,
norma y producto interno. Esta estructura es la que permite que φ(cid:0), α y la
REC de la Parte VII estén bien definidos. Para familias concretas de w —
decrecimiento exponencial, ventana rectangular, kernel gaussiano— ver el

## Apéndice B de Metrología Causal Vol. I.

Teorema 2. Existencia y unicidad de I(t)
Para toda c: T → E admisible en el sentido de la Definición 0
y toda w: T → ℝ₊ medible y acotada, I(t) existe y es único en
E para todo t (cid:0) T.
Demostración
Demostración del Teorema 2
Paso 1. Por la Definición 0: c es medible en sentido
de Bochner y (cid:0)c(τ)(cid:0)_E ≤ M para algún M > 0 y todo
τ (cid:0) T.
Paso 2. Sea f(τ) = c(τ)w(τ). Como w es medible y
‖ w‖ _∞ ≤ W < ∞, el producto f hereda la
medibilidad de Bochner de c y satisface (cid:0)f(τ)(cid:0)_E ≤
MW para todo τ (cid:0) T.

Axiomatización del Sistema de la Doble Mediación
Paso 3. f es esencialmente acotada, luego f (cid:0) L¹ (T;
E): ∫(cid:0)^{t_m} (cid:0)f(τ)‖ _E dτ ≤ MW · t_m < ∞, con
t_m = sup T < ∞ por la Definición 0.
Paso 4. Por el teorema fundamental de integración
de Bochner, toda f (cid:0) L¹ (T; E) con E Banach admite
integral de Bochner I(t) = ∫(cid:0)ᵗ f(τ) dτ (cid:0) E, única como
elemento de E.
Existencia y unicidad de I(t) en E para todo t (cid:0) T. (cid:0)
Teorema 2.1. Irreversibilidad de I(t)
Si w(τ) > 0 para todo τ (cid:0) T y c(τ) ≠ 0 en un conjunto de
medida de Lebesgue positiva en T, entonces para todo par t(cid:0)
> t(cid:0) en T con las mismas hipótesis en [t(cid:0), t(cid:0)]:
Condición de irreversibilidad
(cid:0)I(t(cid:0)) − I(t₁) ‖_E > 0
bajo w(τ) > 0 en [t(cid:0), t(cid:0)] y c(τ) ≠ 0 en conjunto de medida positiva en [t(cid:0),
t(cid:0)]
Demostración
Demostración del Teorema 2.1
Paso 1. I(t(cid:0)) − I(t₁ ) = ∫_{t₁} ^{t(cid:0)} c(τ)w(τ) dτ. Sea
g(τ) = c(τ)w(τ). Por hipótesis: w(τ) > 0 en [t(cid:0), t(cid:0)] y
c(τ) ≠ 0 en un conjunto S (cid:0) [t(cid:0), t(cid:0)] con μ(S) > 0.
Luego g(τ) ≠ 0 en S.
Paso 2. Por la propiedad fundamental de la integral
de Bochner: si g (cid:0) L¹ (T; E) y g(τ) ≠ 0 en un conjunto
de medida positiva, entonces (cid:0)∫ g(τ) dτ(cid:0)_E > 0.
Combinando: (cid:0)I(t(cid:0)) − I(t₁) ‖_E = (cid:0)∫_{t₁} ^{t(cid:0)}
g(τ) dτ(cid:0)_E > 0. (cid:0)
Las hipótesis son necesarias: si w(τ) = 0 en algún subintervalo o c(τ) = 0 a.e., I
puede ser constante en ese período —situación admisible en el marco formal.
Consecuencia para la responsabilidad. El Teorema 2.1
establece que todo colapso no nulo producido bajo w > 0 deja

Axiomatización del Sistema de la Doble Mediación
huella permanente en I(t). El estado del sistema no puede
retornar a su valor anterior por la sola acción del tiempo: solo
colapsos futuros integrados pueden recontextualizar I(t), no
eliminarlo. Esta permanencia es el fundamento matemático de
la imputabilidad en el sistema.
Definición 2.1. El registro de colapsos RSC(t)
El registro de colapsos del sistema hasta t es la imagen de c en
T:
Registro de colapsos
RSC(t) = {c(τ): τ (cid:0) [0, t]} ⊆ E
imagen de la función de colapso en [0, t] · incluye todos los colapsos producidos
por φ(cid:0) con independencia de si φ(cid:0) los integró
La relación entre RSC(t) e I(t) es la siguiente: I(t) es la integral
de Bochner de los colapsos de RSC(t) que φ(cid:0) aceptó,
ponderados por w. La diferencia RSC(t) \ I(t) contiene los
colapsos producidos pero rechazados. El coeficiente de
asunción α de la Parte IV mide la proporción ponderada de
RSC(t) que está integrada en I(t).
La distinción RSC(t) / I(t) es central en la aplicación: RSC(t) corresponde
a los hechos documentados del expediente —todo lo que el actor produjo— e
I(t) a lo que el actor integró como propio —lo que reconoció, reparó o asumió
estructuralmente. La brecha RSC(t) \ I(t) es el espacio que α mide y Δ
cuantifica.
Teorema 2.2. Representación de φ(cid:0) y
condiciones sobre eval
La segunda mediación φ(cid:0) admite la representación:
Representación de φ(cid:0)
φ₂ (a, I(t)) = I(t) + δ(a) · 1_ {eval (a, I(t)) > θ}
eval: A × E → ℝ función de evaluación de compatibilidad

Axiomatización del Sistema de la Doble Mediación
δ(a) (cid:0) E modificación producida por la integración
de a
θ (cid:0) (cid:0) umbral de integración
1_ {···} función indicadora · vale 1 si eval (a, I(t)) > θ, 0 en caso contrario
Para que la representación esté bien definida, eval y δ deben
satisfacer:
(i) Medibilidad. eval es medible como función A ×
E → (cid:0) respecto a las σ-álgebras de Borel de A y E.
(ii) Compatibilidad. eval (a, I(t)) > θ si y solo si el
colapso a es compatible con el estado actual I(t) en el
sentido operativo del dominio. El núcleo formal no
fija la noción de compatibilidad; exige que eval la
codifique de forma medible y que θ sea un umbral fijo
para un sistema dado.
(iii) No-amplificación. (cid:0)δ(a)(cid:0)_E ≤ (cid:0)a(cid:0)_E: la
modificación que produce la integración no supera en
norma al colapso que la produce. Esta condición evita
singularidades en I(t) y es el primer criterio de
validación de cualquier implementación de φ(cid:0).
Demostración
Demostración del Teorema 2.2
Paso 1. El Axioma 2 establece tres etapas: evaluación,
decisión binaria y actualización. La función indicadora
1_ {eval > θ} captura exactamente la decisión binaria:
1 cuando eval > θ (integración), 0 en caso contrario
(rechazo).
Paso 2. El producto δ(a) · 1_ {eval > θ} es δ(a)
cuando hay integración y 0 cuando hay rechazo. La
suma I(t) + δ(a) · 1_ {···} produce I(t) + δ(a) en el
primer caso e I(t) en el segundo.
Paso 3. Ambos resultados están en E: I(t) (cid:0) E por el
Teorema 2; δ(a) (cid:0) E por la condición (iii); luego I(t)
+ δ(a) (cid:0) E. La representación es consistente con el
codominio del Axioma 2. ✓

Axiomatización del Sistema de la Doble Mediación
La representación es válida bajo las condiciones (i)–(iii). (cid:0)
Sobre la familia de funciones eval. Las condiciones (i)–(iii)
son el marco mínimo. Cualquier función eval que las satisfaga
produce una φ(cid:0) bien definida y consistente con el Axioma 2.
Una familia paramétrica natural es eval (a, I(t)) = (cid:0)a, I(t)(cid:0)_E
/ ((cid:0)a(cid:0)_E · (cid:0)I(t)(cid:0)_E), la similitud coseno en E: mide la
alineación direccional entre el colapso y el estado acumulado,
toma valores en [−1, 1], es medible y satisface la no-
amplificación cuando δ(a) se define proporcionalmente. La
calibración de eval para cada dominio —jurídico, clínico, de
IA— pertenece a la Taxonomía y a los protocolos de
Metrología Causal.
La elección de la similitud coseno como familia de referencia resuelve la crítica
de arbitrariedad sobre eval planteada en la revisión externa: eval no es una
caja negra, sino un espacio paramétrico de funciones con condiciones
verificables. La condición (iii) en particular es inmediatamente computable y
constituye el primer test de implementación.
Objeto Notación Tipo Parte
matemático
Segunda φ(cid:0) : A×E → E Función Axioma 2
mediación (existencia
postulada)
Función de w : T → ℝ₊ Medible y Definición
peso acotada 2
Integral I(t) = ∫(cid:0)ᵗ c w dτ (cid:0) E Integral de Definición
acumulativa Bochner en 2; Teorema
E 2
Existencia y Teorema 2 L¹(T;E) + Teorema 2
unicidad Bochner
Irreversibilidad (cid:0)I(t(cid:0))−I(t₁ )‖ _E > Desigualdad Teorema
0 en E 2.1

Axiomatización del Sistema de la Doble Mediación
Registro de RSC(t) = {c(τ): Imagen de c Definición
colapsos τ(cid:0)[0,t]} en [0,t] 2.1
Colapsos RSC(t) \ I(t) Diferencia Definición
rechazados de conjuntos 2.1
Representación I(t)+δ(a)·1_{eval>θ} Suma en E Teorema
de φ(cid:0) con 2.2
indicadora
Función de eval : A×E → (cid:0) Medible; Teorema
evaluación familia: cos. 2.2
sim.
Modificación δ(a) (cid:0) E, (cid:0)δ(cid:0)_E ≤ Vector en E; Teorema
(cid:0)a(cid:0)_E no- 2.2
amplificación
Umbral de θ (cid:0) (cid:0) Parámetro Teorema
integración escalar 2.2

Axiomatización del Sistema de la Doble Mediación
Parte III
El índice de sustituibilidad S
Definición 3.1. S operacional
Sea c (cid:0) C la configuración heredada con norma (cid:0)c(cid:0)_C y sea
a_t (cid:0) E el estado de activación con norma (cid:0)a_t(cid:0)_E, ambos
en el instante t. Para hacer conmensurables las normas de
espacios distintos, se definen los pesos normalizados:
Pesos normalizados para S_op
c(cid:0) = (cid:0)c(cid:0)_C / ((cid:0)c(cid:0)_C + (cid:0)a_t(cid:0)_E), ã_t = (cid:0)a_t(cid:0)_E /
((cid:0)c(cid:0)_C + (cid:0)a_t(cid:0)_E)
c(cid:0) + ã_t = 1 por construcción · ambas cantidades son adimensionales · la
comparación entre normas de C y E se hace mediante el cociente
El índice de sustituibilidad operacional en t es:
S operacional
S_op(t) = c(cid:0) = (cid:0)c(cid:0)_C / ((cid:0)c(cid:0)_C + (cid:0)a_t(cid:0)_E)
S_op(t) (cid:0) [0,1] · mide la fracción del comportamiento en t atribuible a la
configuración heredada
S_op satisface:
(i) S_op(t) (cid:0) [0,1]: numerador no negativo, no
superior al denominador.
(ii) S_op(t) → 1 cuando ‖ a_t‖ _E → 0:
comportamiento completamente determinado por c.
Alta sustituibilidad.

Axiomatización del Sistema de la Doble Mediación
(iii) S_op(t) → 0 cuando ‖ c‖ _C → 0:
comportamiento completamente idiosincrático. Baja
sustituibilidad.
(iv) S_op(t) = 1/2 cuando (cid:0)c(cid:0)_C = (cid:0)a_t(cid:0)_E:
contribuciones iguales.
Computa­bilidad de S_op. (cid:0)c(cid:0)_C y (cid:0)a_t(cid:0)_E son normas
de objetos directamente disponibles en t. En sistemas
artificiales: (cid:0)c(cid:0)_C es la magnitud del vector de parámetros
del modelo; (cid:0)a_t(cid:0)_E es la norma del vector de activación
antes de la generación. En sistemas humanos: (cid:0)c(cid:0)_C se
estima desde la documentación del entorno institucional
usando la escala E0–E8 de Metrología Causal; (cid:0)a_t(cid:0)_E se
aproxima mediante el Lema 3.4.
La comparación de normas en espacios distintos ((cid:0)c(cid:0)_C y (cid:0)a_t(cid:0)_E)
requiere que ambas estén normalizadas respecto a escalas comparables. En
aplicaciones numéricas se recomienda normalizar primero cada norma por su
valor máximo observado en el sistema antes de calcular S_op. El Apéndice
B especifica el procedimiento de normalización para cada dominio.
Definición 3.2. S estructural
Sea G = (N, A, w) el grafo causal de la Parte VI con matriz de
pesos W y vector de responsabilidad R* (Definición 6.1). Sea
W^(i) la matriz de sustitución del nodo i, obtenida
reemplazando la fila i de W por el promedio de las demás filas:
Matriz de sustitución del nodo i
W^(i)_{i·} = (1/(m−1)) Σ_{j≠i} W_{j·}
m = |N| nodos activos · las demás filas de W^(i) coinciden con las de W ·
W^(i)_{j·} = W_{j·} para j ≠ i
Sea R*^(i) el eigenvector principal de (W^(i)) ᵀ normalizado
con Σ_k R*^(i)_k = 1. El índice de sustituibilidad estructural
del nodo i es:
S estructural
S_est(i) = 1 − D_KL (R* (cid:0) R*^(i)) / log(m)

Axiomatización del Sistema de la Doble Mediación
D_KL (P (cid:0) Q) = Σ_k p_k log(p_k/q_k) · log(m) es la cota máxima de
D_KL para distribuciones sobre m elementos
S_est satisface:
(i) S_est(i) (cid:0) [0,1]: D_KL ≥ 0 por la desigualdad de
Gibbs; D_KL ≤ log(m) para distribuciones sobre m
elementos; luego 1 − D_KL/log(m) (cid:0) [0,1].
(ii) S_est(i) → 1 cuando W_{i·} ≈ W(cid:0): sustituir el
nodo no altera R*. D_KL → 0.
(iii) S_est(i) → 0 cuando W_{i·} difiere
máximamente de W(cid:0): sustituir el nodo altera R* al
máximo. D_KL → log(m).
S_est requiere G y R*, definidos en la Parte VI. La definición se enuncia
aquí —donde S debe estar disponible conceptualmente— pero el cómputo
efectivo de S_est es posterior a la Parte VI. La dependencia es unidireccional:
S_est depende de R*, no al contrario. La cadena Davis-Kahan que conecta
S_est con la perturbación de R* se demuestra en el Apéndice A.
Proposición 3.3. Puente S_op — S_est
Existe g: [0,1] → [0,1] monótonamente creciente con g (0) =
0 y g (1) = 1 tal que S_op(t) ≈ g(S_est(t)), preservando el orden
entre nodos:
Proposición del puente
S_est(i) ≤ S_est(j) ⟹ S_op(i) ≤ S_op(j)
g depende de la geometría de G y las métricas de C y E · no tiene forma analítica
universal · se estima empíricamente (Apéndice B)
Demostración
Demostración de la Proposición 3.3
Paso 1 — Extremos. S_est → 1 implica D_KL (R*
‖ R*^(i)) → 0, luego R* ≈ R*^(i): la sustitución del
nodo no altera la distribución causal. Esto
corresponde a W_{i·} ≈ W(cid:0), es decir, (cid:0)a_t(cid:0)_E
pequeño relativo a (cid:0)c(cid:0)_C, luego S_op → 1. El

Axiomatización del Sistema de la Doble Mediación
extremo S_est → 0 es análogo: D_KL → log(m),
W_{i·} difiere máximamente de W(cid:0), (cid:0)a_t(cid:0)_E >>
‖ c‖ _C, S_op → 0. Los extremos se alinean.
Paso 2 — Monotonicidad. Sea Δ_i = (cid:0)W_{i·} −
W(cid:0)(cid:0)(cid:0). Por la desigualdad de Pinsker: (cid:0)R* −
R*^(i)(cid:0)(cid:0) ≤ √ (2 D_KL). Luego D_KL(i) ≤ D_KL(j)
implica Δ_i ≤ Δ_j. La desviación Δ_i de la fila i del
promedio es el análogo estructural de (cid:0)a_t(cid:0)_E: a
mayor desviación, mayor componente idiosincrática.
Por tanto: D_KL(i) ≤ D_KL(j) implica (cid:0)a_t(cid:0)_i ≤
(cid:0)a_t(cid:0)_j implica S_op(i) ≥ S_op(j). El orden se
preserva. ✓
Paso 3 — Existencia de g. S_op y S_est son
continuas en sus argumentos bajo hipótesis regulares
sobre W y las normas, y monótonamente relacionadas
por el Paso 2. La función g existe como función de la
geometría de G y las métricas de C y E. No hay forma
analítica universal porque la relación Δ_i ↔ (cid:0)a_t(cid:0)_E
depende de las métricas específicas del sistema.
La preservación de orden está establecida. g se estima empíricamente en el

## Apéndice B. (cid:0)

Consecuencia operativa. La Proposición 3.3 permite usar
S_op como proxy computable de S_est cuando el grafo G no
está disponible: una comparación de sustituibilidad entre
nodos basada en S_op es válida también para S_est
independientemente de la forma concreta de g.
Lema 3.4. Rangos de S por modo dominante
El modo dominante k*(v_t) = argmax_{k(cid:0)K} h_k(v_t) del
Lema 1.1 informa el rango esperado de S_op y S_est en el
instante t. La correspondencia se establece por el mecanismo
siguiente: cada modo k (cid:0) K tiene asociado un perfil
conductual —determinado por sus parámetros (β_k, γ_k,
θ_k)— que implica una relación característica entre (cid:0)c(cid:0)_C y
(cid:0)a_t(cid:0)_E y, por tanto, un rango de S_op. El rango de S_est
se deriva de ese rango por la Proposición 3.3.

Axiomatización del Sistema de la Doble Mediación
Los rangos son intervalos calibrados desde el análisis de casos
documentados en la Taxonomía General de Aplicaciones y
validados en al menos cuatro dominios distintos. No son
valores exactos: un sistema concreto puede ubicarse en
cualquier punto dentro del intervalo correspondiente a su k*
observado.
k Perfil conductual S_op S_est Mecanismo formal
del modo k* calibrado calibrado
1 Sistema actúa bajo [0.70, [0.68, W_{i·} ≈ W(cid:0): la fila del
presión de 0.95] 0.93] nodo es indistinguible
consecuencias del promedio. D_KL ≈
documentadas: la 0. S_est → 1.
configuración
heredada determina
el output. (cid:0)c(cid:0)_C
>> (cid:0)v_t(cid:0)_V.
2 Sistema produce [0.72, [0.70, Inacción es el output con
inacción 0.95] 0.94] mayor Σ_{j≠i} W_{ij}:
estructural: el cualquier nodo en esa
output nulo es el posición omitiría. D_KL
único consistente mínimo.
con la
configuración
heredada. S más
alto que k=1 en
omisiones puras.
3 Sistema actúa [0.30, [0.28, W_{i·} parcialmente
desde impulso o 0.70] 0.68] diferenciada del
costumbre: c y v_t promedio. D_KL
contribuyen en moderado. S_est
proporciones intermedio.
variables. S
moderado.
4 Sistema actúa [0.30, [0.28, Análogo a k=3.
desde apertura 0.70] 0.68] Distinción entre k=3 y
hacia nuevas k=4 requiere análisis de
configuraciones: la dirección de a_t en E.
contribución mixta
de c y v_t. S
moderado.
5 Sistema actúa [0.08, [0.06, W_{i·} maximalmente
desde afirmación 0.30] 0.28] diferenciada del
idiosincrática: el

Axiomatización del Sistema de la Doble Mediación
output difiere del promedio. D_KL →
esperado bajo c. log(m). S_est → 0.
(cid:0)v_t(cid:0)_V >>
(cid:0)c(cid:0)_C.
6 Integración Variable Variable Requiere estimación
completa: directa de I(t) mediante
coherencia entre protocolo ECO. S_op y
a_t e I(t). S no S_est no son
determinable desde computables sin acceso
expediente externo. al estado interno.
Demostración
Justificación de los rangos del Lema 3.4
k=1 y k=2 → S alto. Los parámetros (β_1, γ_1, θ_1)
del modo k=1 implican que z_1 domina cuando
(cid:0)c(cid:0)_C es alto relativo a (cid:0)a_t(cid:0)_E —la
configuración heredada determina el output. En
términos del grafo: W_{i·} ≈ W(cid:0), luego D_KL ≈ 0
y S_est → 1. El rango [0.70, 0.95] está calibrado desde
los casos donde la presión estructural documentada es
el determinante principal del output. k=2 (inacción)
tiene S ligeramente más alto porque la omisión es el
output de menor variabilidad entre sistemas en la
misma posición.
k=5 → S bajo. Los parámetros (β_5, γ_5, θ_5)
implican que z_5 domina cuando (cid:0)a_t(cid:0)_E >>
(cid:0)c(cid:0)_C —el estado de activación idiosincrático
supera a la configuración heredada. En términos del
grafo: W_{i·} difiere máximamente de W(cid:0), D_KL
→ log(m), S_est → 0. El rango [0.08, 0.30] está
calibrado desde los casos donde la decisión
idiosincrática documentada es el determinante
principal.
k=3 y k=4 → S moderado. Contribuciones mixtas
de c y a_t: ni W_{i·} ≈ W(cid:0) ni W_{i·} maximalmente
diferenciada. D_KL moderado, S_est intermedio. Los
rangos [0.30, 0.70] reflejan la mayor variabilidad
empírica de estos modos.

Axiomatización del Sistema de la Doble Mediación
k=6 → S indeterminado. El modo k=6
corresponde a coherencia entre a_t e I(t). S_op no es
computable sin acceso directo a I(t), cuya estimación
desde evidencia documental externa tiene error no
acotado (REC, Parte VII). S_est tampoco es
computable sin grafo completo. El rango queda sin
determinar hasta que I(t) sea accesible.
Los rangos no son consecuencia deductiva del marco axiomático: son parámetros
calibrados. Su estatus es el de hipótesis empíricas revisables cuando nueva
evidencia esté disponible. Las fuentes de calibración están documentadas en el

## Apéndice B y en la Taxonomía. (cid:0)

Correspondencia con el sistema ontológico. Los seis modos k=1,...,6
corresponden en el sistema ontológico de la colección a los Hijos de Afrodita,
en el orden: k=1 (presión de consecuencias), k=2 (parálisis estructural),
k=3 (costumbre), k=4 (apertura), k=5 (afirmación idiosincrática), k=6
(integración completa). Esa correspondencia es externa al marco formal. Los
rangos de S son propiedades del sistema matemático, no de la ontología. El

## Apéndice C recoge la traducción completa.

Objeto Notación Tipo Parte
matemátic
o
S S_op = Escalar en Definició
operacion (cid:0)c(cid:0)_C/((cid:0)c(cid:0)_C+(cid:0)a_t(cid:0)_ [0,1]; n 3.1
al E) computable
S S_est = 1−D_KL/log(m) Escalar en Definició
estructural [0,1]; n 3.2;
requiere G Apéndice
A
Matriz de W^(i): W^(i)_{i·} = W(cid:0) Perturbació Definició
sust. n de fila de n 3.2
W
Eigenvect R*^(i): (W^(i))ᵀ Distribució Definició
or sustit. R*^(i)=λR*^(i) n sobre N n 3.2

Axiomatización del Sistema de la Doble Mediación
Función g : [0,1]→[0,1] monótona Función Proposici
puente creciente, ón 3.3
g(0)=0,g(1)
=1
Preservaci S_est(i)≤S_est(j)(cid:0)S_op(i)≤S Propiedad Proposici
ón orden _op(j) de g ón 3.3
Rangos S {[S_op^k_min, Intervalos Lema 3.4;
por k* S_op^k_max]}_{k(cid:0)K} calibrados Apéndice
B

Axiomatización del Sistema de la Doble Mediación
Parte IV
El coeficiente de asunción α
Definición 4. Coeficiente de asunción — versión
continua
Sea w: T → ℝ₊ la función de peso de la Definición 2 y sea p:
T → [0,1] una función de profundidad de integración medible.
El coeficiente de asunción del sistema en t es:
Coeficiente de asunción — versión continua
α(t) = ∫(cid:0)ᵗ 1_{int}(τ) · w(τ) · p(τ) dτ / ∫(cid:0)ᵗ w(τ) dτ
1_{int}(τ) = 1 si c(τ) (cid:0) I(t) (φ(cid:0) integró el colapso)
1_{int}(τ) = 0 si c(τ) (cid:0) RSC(t)\I(t) (φ(cid:0) rechazó el colapso)
p: T → [0,1] medible · p(τ) = 0 para colapsos rechazados · p(τ) > 0 para
colapsos integrados · w la misma función de la Definición 2
El denominador ∫(cid:0)ᵗ w(τ) dτ > 0 bajo w > 0, lo que garantiza
que α(t) esté bien definido. La función p(τ) es el único
elemento que requiere calibración por dominio; el núcleo
formal solo exige p: T → [0,1] con p medible.
La función indicadora 1_{int} opera sobre la distinción RSC(t) / I(t) de
la Definición 2.1: RSC(t) registra todos los colapsos producidos; I(t) solo los
integrados. α(t) mide qué fracción de RSC(t), ponderada por w y p, reside en
I(t). Es la proporción de lo producido que el sistema asumió, no la magnitud
absoluta de lo asumido.

Axiomatización del Sistema de la Doble Mediación
Definición 4.1. Coeficiente de asunción —
versión discreta
Sean {t(cid:0), …, t(cid:0)} (cid:0) T momentos discretos de colapso y sea
w(τ) = Σᵢ δ (τ − tᵢ) la función de peso correspondiente, con δ
la delta de Dirac. Para un colapso aᵢ producido en tᵢ:
Coeficiente de asunción — versión discreta
α(aᵢ) = p_pres · f(τᵢ) · g(τᵢ)
p_pres (cid:0) {0,1}: 1 si aᵢ (cid:0) I(t), 0 si aᵢ (cid:0) RSC(t)\I(t)
f(τᵢ) (cid:0) [0,1]: profundidad de integración en τᵢ (ver Tabla
4.1)
g(τᵢ) (cid:0) [0,1]: alcance de la integración en τᵢ (ver Tabla 4.1)
La versión discreta es el caso particular de la Definición 4 con w(τ) = δ(τ−tᵢ) —
demostrado en la Proposición 4.1
Proposición 4.1 — Derivación desde la versión continua
Proposición 4.1
Paso 1. Con w(τ) = δ(τ−tᵢ), el numerador es ∫(cid:0)ᵗ
1_{int}(τ)·δ(τ−tᵢ) ·p(τ) dτ = 1_{int}(tᵢ)·p(tᵢ) por la
propiedad de muestreo de la delta de Dirac.
Paso 2. El denominador es ∫(cid:0)ᵗ δ(τ−tᵢ) dτ = 1 por la
misma propiedad.
Paso 3. Luego α(aᵢ) = 1_{int}(tᵢ)·p(tᵢ) = p_pres ·
p(tᵢ). La función de profundidad puntual p(tᵢ) se
descompone en el producto f(τᵢ) ·g(τᵢ), donde f
captura el tipo de integración y g su extensión —
ambos definidos en la Tabla 4.1.
La versión discreta es la continua evaluada con w = δ(τ−tᵢ): no son dos
definiciones independientes. (cid:0)
Tabla 4.1 — Funciones f y g: variables observables y
niveles de referencia

Axiomatización del Sistema de la Doble Mediación
Parámetro Variable Función Niveles de n_ref / n_I
observable continua referencia anclados a
subyacente E0–E8
f n_doc(τ) = f(τ) = f ≈ 0.3: E1–E2
(profundidad) número de min(1, n_doc/n_ref (declaración):
documentos n_doc(τ) (cid:0) [0.1, 0.4] f n_ref = 1–2
del / n_ref) ≈ 0.6: E3–E4
expediente n_ref = n_doc/n_ref (documental
que umbral (cid:0) [0.4, 0.8] f básico): n_ref
confirman la derivado ≈ 1.0: = 3–5 E5–E6
integración del nivel n_doc/n_ref (documental
del colapso de (cid:0) [0.8, 1.0] robusto): n_ref
c(τ). evidencia = 6–10 E7–E8
(prueba plena):
n_ref = 11+
n_ref se fija al
inicio del
análisis según el
estándar de
evidencia
declarado para
el dominio.
g (alcance) n_dom(τ) = g(τ) = g ≈ 0.3: n_I = número
número de n_dom(τ) n_dom/n_I de dominios
dominios de / n_I (cid:0) [0.0, 0.4] g identificados en
I(t) ≈ 0.6: I(t) mediante
afectados n_dom/n_I SDO o
por la (cid:0) [0.4, 0.8] g protocolo
integración ≈ 1.0: equivalente
de c(τ), con n_dom/n_I antes del
n_I el total (cid:0) [0.8, 1.0] análisis. No
de dominios varía entre
de I(t). analistas dado
el mismo
expediente y el
mismo
protocolo
SDO.
Las funciones f y g son continuas en sus variables observables
subyacentes n_doc y n_dom. Los tres niveles de referencia
{0.3, 0.6, 1.0} son cuantiles para el uso operativo cuando los
conteos exactos no están disponibles, no valores discretos
intrínsecos. El parámetro n_ref en f ya no es un parámetro
libre: queda fijado por el nivel de evidencia E0–E8 declarado
para el dominio de análisis, según la última columna de la

Axiomatización del Sistema de la Doble Mediación
Tabla 4.1. Dos analistas que apliquen el mismo nivel de
evidencia sobre el mismo expediente obtendrán el mismo
n_ref y, por tanto, valores de f comparables entre sí.
El anclaje de n_ref a la escala E0–E8 resuelve la variabilidad entre
analistas que surgía cuando n_ref era un parámetro libre. El nivel de
evidencia requerido para el dominio se declara antes del análisis —por
protocolo o por acuerdo de las partes— y n_ref se deriva directamente de esa
declaración. En casos jurídicos el estándar probatorio del juicio determina el
nivel E; en sistemas artificiales el protocolo de evaluación determina el número
mínimo de registros. Ambos son externos al analista que aplica el sistema.
El coeficiente de asunción agregado para un conjunto de
colapsos A_D (cid:0) RSC(t) es:
Coeficiente de asunción agregado
α_D(t) = (1/|A_D|) · Σ_ {aᵢ (cid:0) A_D ∩ I(t)} α(aᵢ)
A_D conjunto de colapsos del dominio D · A_D ∩ I(t) colapsos de A_D
integrados · si A_D ∩ I(t) = (cid:0) entonces α_D(t) = 0
Teorema 4. α(t) (cid:0) [0, 1] por construcción
Para toda c: T → E admisible, toda w: T → ℝ₊ medible y
acotada con ∫w > 0, y toda p: T → [0,1] medible:
Acotación de α
α(t) (cid:0) [0, 1] para todo t (cid:0) T
Demostración
Demostración del Teorema 4
α(t) ≥ 0. Numerador: 1_{int} (cid:0) {0,1} ≥ 0, w (cid:0) ℝ₊
≥ 0, p (cid:0) [0,1] ≥ 0. El producto de tres factores no
negativos es no negativo; su integral también.
Denominador: ∫(cid:0)ᵗ w(τ) dτ > 0 por hipótesis. Razón
de no negativo sobre positivo: α(t) ≥ 0. ✓
α(t) ≤ 1. Para todo τ (cid:0) T: 1_{int}(τ) · p(τ) ≤ 1
(producto de factores en [0,1]). Multiplicando por

Axiomatización del Sistema de la Doble Mediación
w(τ) ≥ 0: 1_{int}(τ)·w(τ)·p(τ) ≤ w(τ). Integrando: ∫(cid:0)ᵗ
1_{int}·w·p dτ ≤ ∫(cid:0)ᵗ w dτ. Dividiendo por el
denominador positivo: α(t) ≤ 1. ✓
Casos extremos. α(t) = 1 (cid:0) 1_{int}(τ)·p(τ) = 1 para
w-casi todo τ: todos los colapsos integrados con p =
1. α(t) = 0 (cid:0) 1_{int}(τ)·p(τ) = 0 para w-casi todo τ:
ningún colapso integrado o todos con p = 0.
α(t) (cid:0) [0,1] sin restricciones adicionales sobre c, w o p más allá de las ya
establecidas. (cid:0)
Corolario 4.1 — Independencia de α respecto al dolo. α(t)
está definido exclusivamente en términos de acciones
observables posteriores al colapso —lo que φ(cid:0) integró en I(t),
medido por 1_{int}, w y p— y no en términos de la intención
con que φ(cid:0) produjo el colapso. En consecuencia, el valor de
α(t) es invariante bajo cualquier descripción de la intención del
sistema en τ: el dolo, la culpa o la ausencia de ambos no alteran
1_{int}(τ), w(τ) ni p(τ).
Esta independencia tiene dos consecuencias operativas.
Primera: α es compatible con la definición de S —que captura
el estado de la voluntad a través de k*(v_t)— sin
contradicción: S informa sobre el determinismo del acto en
φ(cid:0); α informa sobre la asunción efectiva en φ(cid:0). Son medidas
de objetos distintos. Segunda: α puede crecer por asunción
voluntaria, forzada o impuesta; el efecto sobre el déficit Δ =
R* − α es idéntico en los tres casos.
La invariancia de α respecto al dolo distingue el sistema de los sistemas de
imputación jurídica clásicos, que anclan la responsabilidad en la intención.
El sistema no niega que la intención sea relevante para el derecho:
simplemente la coloca en un objeto distinto —el modo k* del Lema 1.1—
y no en α. La compatibilidad formal entre ambos objetos es consecuencia de
su independencia matemática.

Axiomatización del Sistema de la Doble Mediación
Objeto Notación Tipo Parte
matemático
Coeficiente de α(t) (cid:0) [0,1] Integral de Definición
asun. Lebesgue 4
normalizada
Función de p : T → [0,1] Medible; Definición
profund. requiere 4
calibración
Versión α(aᵢ) = p_pres·f·g Caso δ(τ−tᵢ) de Definición
discreta la Definición 4 4.1; Prop.
4.1
Profundidad f f(τ) = Función Tabla 4.1
min(1,n_doc/n_ref) continua en
n_doc (cid:0) (cid:0)
Alcance g g(τ) = n_dom/n_I Función Tabla 4.1
continua en
n_dom (cid:0) (cid:0)
Asunción α_D = Media aritmética Definición
agregada (1/|A_D|)Σα(aᵢ) sobre A_D∩I(t) 4.1
Acotación Teorema 4 α (cid:0) [0,1] sin Teorema
hipótesis extra 4
Indep. del Corolario 4.1 α invariante bajo Corolario
dolo descripción de 4.1
φ(cid:0)

Axiomatización del Sistema de la Doble Mediación
Parte V
El déficit de asunción Δ
Definición 5. El déficit de asunción
Sean R*ᵢ (cid:0) [0,1] la componente del vector de responsabilidad
causal del nodo i (Definición 6.1, Parte VI) y αᵢ (cid:0) [0,1] el
coeficiente de asunción del mismo nodo (Definición 4, Parte
IV). El déficit de asunción del nodo i es:
Déficit de asunción
Δᵢ = R*ᵢ − αᵢ
R*ᵢ (cid:0) [0,1] por Teorema 6 (Parte VI) · αᵢ (cid:0) [0,1] por Teorema 4 (Parte IV)
· Δᵢ (cid:0) [−1,1] por construcción (Teorema 5)
La dependencia de Δ en R*ᵢ es unidireccional: Δ usa R*, pero
R* no depende de Δ. La Parte V puede leerse sustituyendo R*ᵢ
por «componente del eigenvector principal de Wᵀ para el nodo
i, normalizada, Parte VI» sin pérdida de rigor.
Teorema 5. Δᵢ (cid:0) [−1, 1]
Para todo nodo i del grafo G:
Acotación del déficit
Δᵢ (cid:0) [−1, 1]
Demostración

Axiomatización del Sistema de la Doble Mediación
Demostración del Teorema 5
Cota inferior. Δᵢ = R*ᵢ − αᵢ. Mínimo cuando R*ᵢ
mínimo y αᵢ máximo: R*ᵢ ≥ 0 (Perron-Frobenius,
Teorema 6) y αᵢ ≤ 1 (Teorema 4). Luego Δᵢ ≥ 0 − 1 =
−1. ✓
Cota superior. Máximo cuando R*ᵢ máximo y αᵢ
mínimo: R*ᵢ ≤ 1 (normalización Σ(cid:0) R*(cid:0) = 1 con
R*(cid:0) ≥ 0) y αᵢ ≥ 0 (Teorema 4). Luego Δᵢ ≤ 1 − 0 =
1. ✓
Δᵢ (cid:0) [−1,1] por la acotación de sus dos componentes. (cid:0)
Tabla de signos
Signo de Δᵢ Δᵢ > 0 — Δᵢ = 0 — Δᵢ < 0 —
Brecha activa Equilibrio Sobreasunción
R*ᵢ vs. αᵢ R*ᵢ > αᵢ R*ᵢ = αᵢ R*ᵢ < αᵢ
Lectura Nodo causó más Nodo asumió Nodo asumió
causal de lo que exactamente lo más de lo que
asumió. Brecha que causó. Caso causó. Con grafo
de asunción límite teórico; completo: señal
pendiente. difícil verificar de existencia de j
con precisión de con Δ(cid:0) > 0
medición. (Proposición
5.2).
Diagnóstico Primero verificar Verificar Primero
completitud del intervalos de descartar grafo
grafo. Si G es confianza de R*ᵢ incompleto
completo: y αᵢ antes de (artefacto). Si G
brecha declarar es completo:
estructural. equilibrio. buscar j con Δ(cid:0)
> 0.
El diagnóstico para cada signo figura en la última fila de la
tabla. La distinción entre grafo incompleto y señal genuina de
inversión es la primera verificación que debe hacerse ante
cualquier Δᵢ < 0 observado: un grafo incompleto produce un
R*ᵢ subestimado y, por tanto, un Δᵢ < 0 que es artefacto de
especificación del modelo, no señal de inversión causal.

Axiomatización del Sistema de la Doble Mediación
Δᵢ = 0 es un caso límite teórico: requiere que R*ᵢ y αᵢ coincidan exactamente.
En la práctica ambos son estimaciones con intervalos de incertidumbre. El
equilibrio empírico se declara cuando los intervalos de confianza de R*ᵢ y αᵢ
se solapan, no cuando sus estimaciones puntuales coinciden.
Teorema 5.1. Evolución temporal de Δᵢ
Cuando R*ᵢ(t) y αᵢ(t) son diferenciables en t:
Ecuación de evolución
dΔᵢ/dt = dR*ᵢ/dt − dαᵢ/dt
Los tres regímenes y sus condiciones:
dΔᵢ/dt > 0 Brecha creciente. El nodo acumula
responsabilidad causal (dR*/dt > 0) más rápido de lo
que asume (dα/dt < dR*/dt). O bien: α decrece por
revocación de compromisos con R* estable.
dΔᵢ/dt = 0 Brecha estacionaria. R* y α crecen o
decrecen a la misma tasa. El nivel de Δᵢ —positivo,
negativo o cero— se mantiene.
dΔᵢ/dt < 0 Brecha decreciente. El nodo asume
(dα/dt > 0) más rápido de lo que acumula nueva
responsabilidad causal. Reparaciones, pagos o
modificaciones sistémicas que superan el crecimiento
de R*.
Para un período [t(cid:0), t(cid:0)] con dΔᵢ/dt > 0 sostenido: Δᵢ(t(cid:0)) −
Δᵢ(t(cid:0)) = ∫_{t₁} ^{t(cid:0)} (dR*ᵢ/dt − dαᵢ/dt) dt > 0. Este
indicador permite análisis longitudinal de la posición causal de
un nodo a lo largo del tiempo.
La condición de diferenciabilidad de R*ᵢ(t) requiere que el grafo G(t)
evolucione de forma suficientemente regular. En análisis discreto con
snapshots del grafo en t(cid:0), t(cid:0), …, el diferencial se aproxima por incrementos
finitos: ΔΔᵢ ≈ ΔR*ᵢ − Δαᵢ entre dos snapshots consecutivos.
Proposición 5.2. Δᵢ < 0 como señal de existencia
de j con Δ(cid:0) > 0

Axiomatización del Sistema de la Doble Mediación
Si Δᵢ < 0 es verificable y el grafo G es completo respecto al
conjunto de nodos causalmente necesarios, entonces:
Condición de señal
Δᵢ < 0 ∧ G completo ⟹ ∃ j ≠ i: Δ(cid:0) > 0
G completo: todos los nodos con R* > 0 están incluidos en N · la proposición no
identifica j ni cuantifica Δ(cid:0)
Demostración
Demostración de la Proposición 5.2
Paso 1 — Conservación de R*. Σᵢ R*ᵢ = 1 para todo
G fijo. La suma es constante.
Paso 2 — No conservación de Σα. Σᵢ αᵢ no está
restringida a 1: los coeficientes de asunción son
independientes entre nodos. Σᵢ αᵢ puede ser < 1, > 1
o = 1.
Paso 3 — Consecuencia de Δᵢ < 0 con G
completo. Con G completo, R*ᵢ refleja la
contribución causal real del nodo i. Δᵢ < 0 implica αᵢ
> R*ᵢ: el nodo i asumió más de lo que causó. Esto solo
es posible si i absorbió consecuencias que
corresponden causalmente a algún j con R*(cid:0) > 0.
Para ese j: α(cid:0) < R*(cid:0), luego Δⱼ = R*ⱼ − αⱼ > 0. ✓
Paso 4 — Necesidad de G completo. Si G está
incompleto, R*ᵢ puede estar subestimado: el nodo i
tendría responsabilidad causal real mayor, no
capturada en el grafo. En ese caso Δᵢ < 0 es artefacto
de especificación, no señal de inversión. La condición
de completitud excluye ese artefacto.
Δᵢ < 0 con G completo garantiza la existencia de j con Δ(cid:0) > 0. La
identificación de j y la cuantificación de Δ(cid:0) bajo condiciones estructurales
específicas son objeto del Teorema de Inversión Causal (Parte VIII). (cid:0)
Tres casos de Δᵢ < 0 que no señalan inversión. (a) G
incompleto: R*ᵢ subestimado por ausencia de nodos
relevantes. (b) Reparación extendida voluntaria: el nodo

Axiomatización del Sistema de la Doble Mediación
asumió consecuencias que causó en proporción mayor que R*ᵢ
indica porque eligió hacerlo, con G completo. (c) Error de
medición: los intervalos de confianza de R*ᵢ y αᵢ se solapan y
el Δᵢ < 0 observado no es estadísticamente distinguible de
cero. La distinción entre estos casos y la inversión causal
requiere análisis de completitud del grafo y documentación de
la asunción.
Relación con el TIC. La Proposición 5.2 establece que Δᵢ <
0 es una señal que apunta hacia otro nodo: garantiza la
existencia de j con Δ(cid:0) > 0, pero no su identidad ni su
magnitud. El Teorema de Inversión Causal (Parte VIII)
demuestra bajo qué condiciones estructurales —S alto del
ejecutor, asimetría de visibilidad, régimen de asunción
forzada— ese j con Δ(cid:0) > 0 es sistemáticamente el nodo de
diseño, y determina los valores esperados de Δ(cid:0) y Δᵢ.
Objeto Notación Tipo matemático Parte
Déficit de Δᵢ = R*ᵢ − αᵢ Escalar en [−1,1] Definición
asunc. 5
Acotación Δᵢ (cid:0) [−1,1] Por R*(cid:0)[0,1] y Teorema 5
α(cid:0)[0,1]
Δᵢ > 0 Brecha activa R*ᵢ > αᵢ; verificar Teorema 5
G completo
Δᵢ = 0 Equilibrio R*ᵢ = αᵢ; verificar Teorema 5
IC antes
Δᵢ < 0 Sobreasunción R*ᵢ < αᵢ; descartar Teorema 5
G incompleto
Evolución dΔ/dt = Ecuación Teorema
dR*/dt − diferencial escalar 5.1
dα/dt
Señal de Δᵢ<0 ∧ G Existencia, no Proposición
inversión completo (cid:0) identidad 5.2
(cid:0)j:Δ(cid:0)>0

Axiomatización del Sistema de la Doble Mediación

Axiomatización del Sistema de la Doble Mediación
Parte VI
El vector de responsabilidad causal R*
Definición 6. El grafo causal G
Sea G = (N, A, w) un grafo dirigido donde:
N Conjunto finito de nodos N = {1, 2, …, n, n+1}.
Los nodos {1, …, n} son los actores causalmente
relevantes del sistema. El nodo n+1 es el nodo final
(sumidero): representa el resultado cuya
responsabilidad se distribuye. No tiene aristas
salientes.
A Conjunto de aristas dirigidas A (cid:0) N × N. La arista
(i, j) (cid:0) A indica que i ejerce influencia causal sobre j.
Para todo j: (n+1, j) (cid:0) A.
w Función de peso w: A → [0,1] tal que Σ(cid:0) w (i, j)
= 1 para todo i (cid:0) {1,…,n}. Los pesos representan la
magnitud relativa de la influencia de i sobre sus
sucesores. La fila n+1 de la matriz W es el vector cero.
La matriz de pesos W (cid:0) (cid:0)^{(n+1) ×(n+1)} es no negativa,
estocástica por filas en las filas {1,…,n}, con la fila n+1 nula.
Construcción de G desde la evidencia. En aplicaciones, los
pesos w (i, j) son estimaciones sustentadas en evidencia
documental y se expresan como intervalos [a_{ij}, b_{ij}]
según la escala E0–E8 de Metrología Causal Vol. I. Para el
cálculo de R* se usan los midpoints m_{ij} = (a_{ij}+b_{ij})
/2 como estimación puntual; los extremos producen R*(min)
y R*(max) (Lema 6.1).

Axiomatización del Sistema de la Doble Mediación
La condición Σ(cid:0) w (i, j) = 1 garantiza que los pesos son proporciones, no
magnitudes absolutas. No impone que i influya sobre un único sucesor: la
distribución puede estar repartida. Si la evidencia sustenta una sola arista (i,
j), entonces w (i, j) = 1 y w (i, j') = 0 para j' ≠ j.
Definición 6.1. El vector de responsabilidad
causal R*
Sea W la matriz de pesos de G. El vector de responsabilidad
causal R* es el eigenvector dominante de Wᵀ normalizado en
Δⁿ:
Vector de responsabilidad causal R*
Wᵀ R* = λ(cid:0) R*, Σᵢ R*ᵢ = 1, R*ᵢ > 0 ∀ i
λ(cid:0) > 0 eigenvalor dominante de Wᵀ · R* (cid:0) Δⁿ simplex estándar de dimensión
n · existencia y unicidad garantizadas por el Teorema 6
R*ᵢ es la fracción de la influencia causal del resultado n+1 que
transita por el nodo i, considerando todas las trayectorias
causales posibles en G. R*ᵢ alto indica que el resultado
depende significativamente de la presencia idiosincrática del
nodo i en su posición.
Elección de Wᵀ sobre W. El eigenvector de W recoge la
influencia que i ejerce sobre sus sucesores. El eigenvector de
Wᵀ recoge la influencia acumulada que los predecesores
ejercen sobre i y, por transitividad, la participación de i en la
producción del resultado final. Para la distribución de
responsabilidad causal —cuánto del resultado pasa por i— el
eigenvector de Wᵀ es el objeto correcto. La elección es análoga
a la de PageRank: una página es importante si páginas
importantes apuntan hacia ella.
Alcance de R*. R* es la distribución de influencia causal
estructural, no la distribución de culpabilidad jurídica ni de
responsabilidad moral. La calificación jurídica o ética es una
operación posterior que usa R* como input técnico. El sistema
no impone esa calificación.

Axiomatización del Sistema de la Doble Mediación
Teorema 6. Existencia y unicidad de R* —
Perron-Frobenius
Si G satisface las condiciones de la tabla siguiente, entonces:
(i) Existe λ(cid:0) > 0 único con |λ| < λ(cid:0) para todo otro
eigenvalor λ de Wᵀ.
(ii) Existe R* con R*ᵢ > 0 para todo i y Wᵀ R* = λ(cid:0)
R*.
(iii) R* es único en Δⁿ (salvo normalización, el
espacio propio de λ(cid:0) tiene dimensión 1).
(iv) Para W estocástica por filas: λ(cid:0) = 1 y R* (cid:0) Δⁿ
es la distribución estacionaria de la cadena de Markov
inducida.
Condición Definición técnica Verificación en G /
Procedimiento si falla
No w(i,j) ≥ 0 para toda Garantizada por Definición
negatividad arista (i,j) (cid:0) A. 6: w : A → [0,1].
Irreducibilidad ∀ i,j ∈ N ∃ camino G fuertemente conexo. Si
dirigido i → j en G. falla: W(ε) = (1−ε)W +
ε·J/n con ε (cid:0) (0,1)
pequeño.
Aperiodicidad mcd de las longitudes Garantizada si (cid:0) nodo con
de todos los ciclos de lazo (ciclo de longitud 1) o
G es 1. ciclos de longitudes
coprimas. Si falla: misma
perturbación W(ε).
Estocástica Σ(cid:0) w(i,j) = 1 para Garantizada por Definición
por filas todo i ≠ n+1. 6. Implica λ(cid:0) = 1
directamente.
Consecuencia λ(cid:0) = 1, simple; |λ(cid:0)| R* (cid:0) Δⁿ⁻ ¹ único: todas las
< 1 para k ≥ 2. componentes R*ᵢ > 0, Σᵢ
R*ᵢ = 1.
Demostración

Axiomatización del Sistema de la Doble Mediación
Demostración del Teorema 6
Paso 1. Wᵀ es no negativa (w (i, j) ≥ 0). Si G es
irreducible y aperiódico, Wᵀ es primitiva (irreducible
+ aperiódica). El Teorema de Perron-Frobenius para
matrices no negativas primitivas garantiza las
propiedades (i)–(iii).
Paso 2 — λ(cid:0) = 1. W es estocástica por filas: W·1 =
1, luego 1 es eigenvalor de W con eigenvector 1. Por
simetría espectral, λ(cid:0) = 1 es eigenvalor de Wᵀ. La
primitiva garantiza que es el único de módulo 1.
Paso 3 — Unicidad. El espacio propio de λ(cid:0) = 1
en Wᵀ tiene dimensión 1 (Perron-Frobenius).
Imponiendo Σᵢ R*ᵢ = 1, R* queda completamente
determinado.
Paso 4 — Positividad. Para matrices primitivas, el
eigenvector dominante tiene todas las componentes
estrictamente positivas. Luego R*ᵢ > 0 para todo i (cid:0)
N, lo que garantiza Δᵢ = R*ᵢ − αᵢ (cid:0) [−1,1] (Teorema
5).
Las cuatro propiedades se siguen del Teorema de Perron-Frobenius para matrices
no negativas primitivas. (cid:0)
Perturbación cuando G no es primitivo. Si G no satisface
irreducibilidad o aperiodicidad: sustituir W por W(ε) = (1−ε)
W + (ε/n) ·J, donde J es la matriz de unos y ε (cid:0) (0,1) pequeño.
W(ε) es primitiva para todo ε > 0. El Teorema 6 aplica a W(ε)
y R*(ε) → R* cuando ε → 0. En práctica, ε = 0.01 produce
resultados estables para n ≤ 20.
La perturbación ε tiene interpretación estructural: representa la posibilidad
de que cualquier nodo influya mínimamente sobre cualquier otro del grafo.
En sistemas organizacionales complejos esta posibilidad es realista; ε = 0.01
equivale a asignar un 1% de influencia difusa uniforme sobre todos los nodos.
Lema 6.1. Método de potencias y rangos de
evidencia
El método de potencias calcula R* iterativamente bajo las
condiciones del Teorema 6:

Axiomatización del Sistema de la Doble Mediación
Algoritmo — método de potencias para R*
Entrada: W (cid:0) (cid:0)ⁿ(cid:0)ⁿ estocástica por filas · ε_conv > 0
tolerancia
Inicio: R*(0) = (1/n, …, 1/n) distribución uniforme
Paso k+1: v ← Wᵀ · R*(k)
R*(k+1) ← v / (cid:0)v(cid:0)(cid:0)
Parar si: (cid:0)R*(k+1) − R*(k)‖ ₁ < ε_conv
ε_conv = 10⁻ ⁶ estándar · 10⁻ ⁸ alta precisión
Salida: R* = R*(k+1)
Complejidad por iteración: O(n²) · Iteraciones típicas: 20–50 para n ≤ 20 con
ε_conv = 10⁻⁶
Demostración de convergencia
Demostración del Lema 6.1
Paso 1. Descomposición: R*(0) = c(cid:0)·R* + Σ_{k≥2}
c(cid:0)·v(cid:0) en la base de eigenvectores de Wᵀ, con |λ(cid:0)|
< 1 para k ≥ 2.
Paso 2. (Wᵀ)^m · R*(0) = c(cid:0)·R* + Σ_{k≥2}
c(cid:0)·λ(cid:0)ᵐ·v(cid:0). Como |λ(cid:0)| < 1, el segundo término →
0 cuando m → ∞.
Paso 3. Tras normalización en cada iteración, R*(k)
→ R* con velocidad geométrica de razón |λ(cid:0)|,
donde λ(cid:0) es el segundo eigenvalor en módulo. La
brecha espectral δ = 1 − |λ(cid:0)| determina la velocidad
de convergencia.
Convergencia para todo R*(0) con componentes positivas bajo las condiciones del
Teorema 6. (cid:0)
Rangos de evidencia y estimación por intervalos

Axiomatización del Sistema de la Doble Mediación
Cuando los pesos están expresados como intervalos [a_{ij},
b_{ij}], el procedimiento estándar produce tres estimaciones
de R*:
R*(mid) Ejecutar el algoritmo con m_{ij} =
(a_{ij}+b_{ij}) /2. Estimación puntual de R*.
R*(min) Ejecutar con a_{ij} para cada arista. Cota
inferior del intervalo de R*.
R*(max) Ejecutar con b_{ij} para cada arista. Cota
superior del intervalo de R*.
El nivel de certeza de la estimación se declara según la anchura
max_i (R*(max)_i − R*(min)_i): anchura ≤ 0.05 →
declaración A; anchura ≤ 0.10 → declaración B; anchura >
0.10 → declaración C, según la escala del Vol. I de Metrología
Causal.
El intervalo [R*(min), R*(max)] refleja la incertidumbre empírica del
analista sobre los pesos del grafo, no la incertidumbre ontológica del sistema.
El vector R* del sistema real es único y determinado (Teorema 6). La REC
de la Parte VII cuantifica la incertidumbre del sistema sobre su propio estado
I(t); los intervalos de R* cuantifican la incertidumbre del analista sobre los
pesos del grafo G. Son dos fuentes de incertidumbre conceptualmente distintas.
Objeto Notación Tipo Parte
matemático
Grafo G = (N, A, w) Dígrafo Definició
causal ponderado n 6
Nodo final n+1 (cid:0) N Sumidero; Definició
fila de W n 6
nula
Matriz de W (cid:0) (cid:0)^{(n+1)×(n+1)} No negativa; Definició
pesos estocástica en n 6
{1,…,n}

Axiomatización del Sistema de la Doble Mediación
Vector R* Wᵀ R* = λ(cid:0) R*, R* (cid:0) Δⁿ Distribución Definició
sobre N n 6.1
Eigenvalor λ(cid:0) = 1 Para W Teorema
dominante estocástica 6
por filas
Positividad R*ᵢ > 0 ∀i Garantiza Δᵢ Teorema
(cid:0) [−1,1] 6
Unicidad dim ker(Wᵀ−I) = 1 Espacio Teorema
propio 6
unidimension
al
Perturbació W(ε)=(1−ε)W+(ε/n)J Hace W Teorema
n primitiva; ε 6
→ 0 → R*
Método de R*(k+1)=Wᵀ Converge Lema 6.1
potencias R*(k)/(cid:0)·(cid:0)(cid:0) con razón
|λ(cid:0)|
Criterio de (cid:0)R*(k+1)−R*(k)‖ ₁ <ε_c ε_conv=10⁻ Lema 6.1
conv. onv (cid:0) estándar
Intervalo [R*(min), R*(max)] Incertidumbr Lema 6.1
de R* e empírica
del analista

Axiomatización del Sistema de la Doble Mediación
Cierre de los Fundamentos
Proposición de Consistencia Interna
Esta proposición no introduce resultados nuevos. Verifica que
los objetos de las Partes 0–VI son mutuamente compatibles
antes de usarlos en los resultados de las Partes VII–X. La
consistencia es condición necesaria pero no suficiente para la
corrección del sistema: garantiza que los resultados no se
contradicen entre sí; no garantiza que sean verdaderos
respecto al sistema que modelan.
Un sistema inconsistente puede demostrar cualquier cosa, incluyendo su
propia negación. La consistencia interna es el piso que separa un conjunto de
definiciones de un sistema formal.
Ítem Par de Condición Partes de referencia
objetos verificada
(i) S_op, S_est S_est(i) → 1 ⟹ Defs. 3.1, 3.2; Def. 6.1
— R* D_KL (R* (cid:0)
R*^(i)) → 0 ⟹ ‖R*
− R*^(i)‖ ₁ → 0.
Alta sustituibilidad
implica mínima
idiosincrasia causal.
(ii) φ(cid:0) — h(v_t) h_k(v_t) = Lema 1.1 (Parte I)
softmax_k(z): h_k ≥
0 y Σ_k h_k = 1
para todo v_t (cid:0) V.
h(v_t) (cid:0) Δ(cid:0).
(iii) α continuo Con w(τ) = δ(τ−tᵢ): Defs. 4, 4.1; Prop. 4.1 (Parte
— α discreto la integral continua IV)
colapsa a p_pres·f·g
por la propiedad de
muestreo. Una sola

Axiomatización del Sistema de la Doble Mediación
definición, dos
granularidades.
(iv) Δ — TIC Δᵢ (cid:0) [−1,1] Teoremas 5, 8 (Partes V,
garantiza que {Δ(D) VIII)
> 0 ∧ Δ(E) < 0} es
algebraicamente
posible. El TIC
opera sobre un
espacio no vacío.
Ítem (i). Compatibilidad S — R*
Compatibilidad S–R*
S_est(i) → 1 ⟹ ‖R* − R*^(i)‖ ₁ → 0
R*^(i) eigenvector dominante de (W^(i)) ᵀ con fila i reemplazada por promedio
Verificación del Ítem (i)
Por Def. 3.2. S_est(i) = 1 − D_KL (R* (cid:0) R*^(i))
/log(m). S_est → 1 implica D_KL (R* ‖ R*^(i)) →
0.
Por Pinsker. (cid:0)R* − R*^(i)‖ ₁ ≤ √ (2 D_KL (R* (cid:0)
R*^(i))). Luego D_KL → 0 implica ‖ R* − R*^(i)‖ ₁
→ 0.
Coherencia con Def. 3.1. Si R* no cambia al
sustituir i, entonces R*ᵢ ≈ 1/m (valor promedio): la
contribución causal del nodo i es mínima. Por la Def.
3.1, esto corresponde a (cid:0)c(cid:0)_C >> (cid:0)a_t(cid:0)_E, es
decir, S_op → 1. Los dos índices son coherentes. ✓
Coherencia con el TIC. La Condición (2) del
Teorema 8 (S_est(E) > θ_S) implica R*(E) bajo vía el
Lema 8.1, que usa exactamente esta cadena. Sin la
compatibilidad S–R*, el Lema 8.1 carecería de
fundamento. ✓

Axiomatización del Sistema de la Doble Mediación
S y R* son objetos independientes pero coherentes: mayor S implica menor
idiosincrasia causal. No hay contradicción. ✓
Ítem (ii). Validez probabilística de h(v_t)
h(v_t) (cid:0) Δ(cid:0) para todo v_t (cid:0) V
h_k(v_t) ≥ 0 y Σ_{k∈K} h_k(v_t) = 1 ∀ v_t ∈ V
Consecuencia directa de la forma softmax del Lema 1.1
Verificación del Ítem (ii)
h_k ≥ 0. exp(z_k) > 0 para todo z_k (cid:0) (cid:0);
denominador positivo; razón positiva. ✓
Σ h_k = 1. Σ_k exp(z_k) / Σ_j exp(z_j) = 1 por
cancelación exacta. ✓
Corrección del manuscrito. La formulación
original con sigmoide independiente producía Σ_k
σ(z_k) (cid:0) {1}, invalidando la interpretación
probabilística y haciendo al argmax k* no
interpretable como moda de una distribución. La
corrección a softmax de la Parte I elimina esa
inconsistencia. Esta verificación confirma su
efectividad.
Consecuencia sistémica. La REC (Parte VII) y el
MP (Parte IX) usan h_k como probabilidades en sus
argumentos. La validez de ambos resultados depende
de h(v_t) (cid:0) Δ⁵ . ✓
h(v_t) (cid:0) Δ(cid:0) para todo v_t (cid:0) V. φ(cid:0) produce siempre un colapso dentro de A
(cid:0) E. ✓
Ítem (iii). Coherencia de α continuo y discreto
Versión discreta como caso particular de la continua
w(τ) = δ (τ − tᵢ) ⟹ α(aᵢ) = p_pres · f(τᵢ) · g(τᵢ)

Axiomatización del Sistema de la Doble Mediación
Por la propiedad de muestreo de la delta de Dirac — demostrado en la
Proposición 4.1
Verificación del Ítem (iii)
Numerador. ∫(cid:0)ᵗ 1_{int}(τ)·δ(τ−tᵢ) ·p(τ) dτ =
1_{int}(tᵢ)·p(tᵢ) por la propiedad de muestreo: ∫
f(τ)·δ(τ−tᵢ) dτ = f(tᵢ). ✓
Denominador. ∫(cid:0)ᵗ δ(τ−tᵢ) dτ = 1. ✓
Resultado. α = p_pres · p(tᵢ) = p_pres · f(τᵢ) · g(τᵢ)
por la descomposición de la Tabla 4.1. No existen dos
objetos distintos: hay una única definición con dos
granularidades de cómputo. ✓
La versión continua y la discreta son el mismo objeto. ✓
Ítem (iv). Compatibilidad Δ — Teorema de
Inversión Causal
No vacuidad del espacio del TIC
Δᵢ (cid:0) [−1,1] ⟹ {Δ(D) > 0 ∧ Δ(E) < 0} es
algebraicamente posible
Este ítem no demuestra que las condiciones del TIC se cumplan en sistemas reales;
solo que el espacio donde opera no es vacío
Verificación del Ítem (iv)
Acotación. Δᵢ = R*ᵢ − αᵢ (cid:0) [−1,1] por el Teorema 5.
Los extremos ±1 son alcanzables.
No vacuidad. Se requiere simultáneamente: (a) (cid:0)D
con R*(D) > α(D), y (b) (cid:0)E con R*(E) < α(E).
Ejemplo explícito: R*(D) = 0.40, α(D) = 0.05 → Δ(D)
= 0.35 > 0; R*(E) = 0.05, α(E) = 0.60 → Δ(E) =
−0.55 < 0. Ambos valores en [−1,1] y R*(D) + R*(E)
= 0.45 es parte de una distribución que suma 1. ✓
Compatibilidad con Σ R*ᵢ = 1. La normalización
de R* no impone Σ αᵢ = 1. Luego Δ(D) > 0 y Δ(E) <

Axiomatización del Sistema de la Doble Mediación
0 simultáneamente son compatibles con la
normalización. ✓
El espacio donde opera el TIC es no vacío dentro del marco formal de los
Fundamentos. ✓
Cierre. Estado del sistema tras los
Fundamentos
Los cuatro ítems establecen:
(i) S y R* son coherentes: mayor sustituibilidad
implica menor idiosincrasia causal. El Lema 8.1 tiene
fundamento.
(ii) h(v_t) (cid:0) Δ(cid:0) para todo v_t. La REC y el MP
tienen fundamento.
(iii) α es un único objeto con dos granularidades. Los
resultados de la Parte IV son coherentes entre sí.
(iv) Δ (cid:0) [−1,1] garantiza que el TIC opera sobre un
espacio no vacío. El resultado central del libro no está
bloqueado por inconsistencia en los fundamentos.
Estas condiciones son necesarias, no suficientes. Las
demostraciones de las Partes VII–X determinan si los
resultados son correctos. Las condiciones aquí verificadas
determinan únicamente que esos resultados no se contradicen
entre sí por construcción.
Cualquier objeción a los resultados de las Partes VII–X debe dirigirse a sus
demostraciones, no a la consistencia de los Fundamentos. Esa consistencia
ha sido verificada en esta proposición.

Axiomatización del Sistema de la Doble Mediación
Parte VII
Relación de Escala del Conocimiento
Esta parte establece una cota informacional —no un principio
de incertidumbre en el sentido de Heisenberg— sobre la
precisión simultánea con que un sistema con τ > 0 puede
estimar I(t) y h(t) a partir de n colapsos integrados. La
distinción respecto a Heisenberg se establece explícitamente
en la sección 7.4.
Axioma 3. Temperatura positiva
Axioma 3
τ > 0
τ parámetro de temperatura del estado interno v_t (Definición 1) · verificable
empíricamente en todo sistema con variabilidad de respuesta
τ > 0 excluye el caso determinista τ = 0 —distribución h(v_t)
degenerada en un único modo. En sistemas artificiales, τ es el
parámetro de temperatura de la softmax: directamente
observable. En sistemas humanos, τ se estima como la
variabilidad empírica de la respuesta ante configuraciones
idénticas.
El Axioma 3 no impone que τ sea constante en T: solo que τ > 0 en todo
t. τ puede variar entre llamadas en sistemas artificiales si el diseñador lo
permite; puede variar con el estado contextual en sistemas humanos. Lo que
el axioma excluye es τ = 0 en cualquier instante.
Lema 7.1. Información de Fisher para el modo k

Axiomatización del Sistema de la Doble Mediación
Sea h_k(θ) = softmax_k(z(θ)) con θ = (cid:0)I(t)(cid:0)_E el parámetro
de historia escalar. Modelando la observación del modo k
como variable Bernoulli X ~ Ber(h_k(θ)), la información de
Fisher sobre θ contenida en una observación es:
Información de Fisher — modo k
(cid:0)(θ) = (1/τ²) · h_k(θ) · (1 − h_k(θ))
Máxima cuando h_k = 1/2 · mínima cuando h_k → 0 o h_k → 1 · (cid:0)_n(θ)
= n · (cid:0)(θ) para n observaciones independientes
Demostración
Demostración del Lema 7.1
Log-verosimilitud. ℓ (θ; x) = x·log h_k(θ) + (1−x)
·log(1−h_k(θ)). Con h_k(θ) = σ((θ−θ_k) /τ): ∂ℓ/∂θ =
(1/τ) · [x − h_k(θ)].
Fisher. (cid:0)(θ) = E[(∂ℓ/∂θ) ²] = (1/τ²) ·E[(x−h_k) ²]
= (1/τ²) ·Var(X) = (1/τ²) ·h_k(1−h_k), pues
Var(Ber(p)) = p(1−p). ✓
(cid:0)(θ) = h_k(1−h_k) /τ². Aditividad para n observaciones independientes: (cid:0)_n
= n·(cid:0). (cid:0)
Lema 7.2. Cotas de Cramér-Rao para n colapsos
Sean Î y ĥ estimadores insesgados de I(t) y h_k(t)
respectivamente, basados en n colapsos integrados:
Cotas de Cramér-Rao
Var(Î) ≥ τ² / [n · h_k(1−h_k)]
Var(ĥ) ≥ h_k(1−h_k) / n
Var(Î) · Var(ĥ) ≥ τ² / n²
El factor h_k(1−h_k) se cancela en el producto · la cota del producto es
invariante respecto al valor de h_k
Demostración

Axiomatización del Sistema de la Doble Mediación
Demostración del Lema 7.2
Var(Î). Por Cramér-Rao: Var(Î) ≥ 1/(cid:0)_n =
τ²/[n·h_k(1−h_k)]. ✓
Var(ĥ). Cambio de parámetro θ → h_k: (cid:0)_h =
(cid:0)_n·(dh_k/dθ) ^ {−2}. Con dh_k/dθ = h_k(1−h_k)
/τ: (cid:0)_h = n·h_k(1−h_k) /τ²·τ²/[h_k(1−h_k)]² =
n/[h_k(1−h_k)]. Luego Var(ĥ) ≥ h_k(1−h_k) /n. ✓
Producto. Var(Î)·Var(ĥ) ≥
[τ²/(n·h_k(1−h_k))]·[h_k(1−h_k) /n] = τ²/n². El
factor h_k(1−h_k) se cancela. ✓
Cota del producto invariante respecto a h_k: Var(Î)·Var(ĥ) ≥ τ²/n². (cid:0)
Teorema 7. Relación de Escala del
Conocimiento (REC)
Para todo Î, ĥ insesgados basados en n colapsos integrados y
para τ(cid:0) > 0 (Axioma 3):
Relación de Escala del Conocimiento
n · (ΔI · Δh) ≥ 4τ(cid:0)²
ΔI = √Var(Î) · Δh = √Var(ĥ)
La cota es positiva para todo n finito y τ(cid:0) > 0 · decrece como 4τ(cid:0)²/n con n
creciente
Demostración
Demostración del Teorema 7
Paso 1. Del Lema 7.2: Var(Î)·Var(ĥ) ≥ τ(cid:0)²/n².
Tomando raíz cuadrada: ΔI·Δh ≥ τ(cid:0)/n.
Paso 2 — Factor 4. La cota Var(Î) ≥
τ(cid:0)²/[n·h_k(1−h_k)] es maximizada cuando
h_k(1−h_k) es mínimo, pero la cota del producto en
el Lema 7.2 usa el peor caso para Var(Î)
simultáneamente: Var(Î) · Var(ĥ) con Var(Î)_max =
4τ(cid:0)²/n (evaluado en h_k = 1/2, que maximiza
h_k(1−h_k) = 1/4 en el denominador) y Var(ĥ)_max

Axiomatización del Sistema de la Doble Mediación
= 1/(4n) produce: (4τ(cid:0)²/n)·(1/4n) = τ(cid:0)²/n².
Tomando raíces y multiplicando por n: n·(ΔI·Δh) ≥
n·(τ(cid:0)/n) = τ(cid:0). La forma canónica n·(ΔI·Δh) ≥ 4τ(cid:0)²
corresponde a la cota n·(ΔI·Δh) _max = n·(2τ(cid:0)/n) ·2
= 4τ(cid:0) cuando τ(cid:0) = 1, equivalente a usar la cota
combinada de ambas varianzas con sus peores casos
independientes.
Paso 3. τ(cid:0) > 0 por el Axioma 3. La cota es positiva
y no trivial para todo n finito. (cid:0)
n·(ΔI·Δh) ≥ 4τ(cid:0)². (cid:0)
La cota n·(ΔI·Δh) ≥ 4τ(cid:0)² es la versión de escala del resultado del Lema
7.2. El factor 4 proviene de tomar los peores casos separados de Var(Î) y
Var(ĥ). La forma equivalente ΔI·Δh ≥ τ(cid:0)/n (sin el factor 4) se obtiene
directamente del Paso 1 y es la más conveniente para estimación. Ambas
formas son correctas; la canónica con factor 4 es más conservadora.
Corolario 7.1. Temperatura efectiva τ_eff
Temperatura efectiva
τ_eff(n) = τ(cid:0) / √n
τ_eff → 0 cuando n → ∞ · τ_eff = τ(cid:0) cuando n = 1
En términos de τ_eff, la REC adopta su forma local:
REC — forma local
ΔI · Δh ≥ 4τ_eff² = 4τ(cid:0)²/n
τ_eff(n) decrece como n^ {−1/2}: la escala de la cota sigue la
misma ley que la desviación estándar de la media muestral en
el TCL. Acumular n colapsos en I(t) es estadísticamente
equivalente a promediar n observaciones independientes del
estado del sistema —en ambos casos la incertidumbre decrece
como n^ {−1/2}.
Consecuencia. Para todo n finito y τ(cid:0) > 0: ΔI·Δh > 0. La
precisión perfecta simultánea sobre I(t) y h(t) es inalcanzable
con un número finito de colapsos. En el límite n → ∞: τ_eff
→ 0 y la cota se anula —la barrera desaparece asintóticamente.

Axiomatización del Sistema de la Doble Mediación
No hay barrera absoluta; hay una barrera que cede con la
experiencia.
Corolario 7.2. Predictibilidad del sistema desde
el exterior
La REC establece que el sistema no puede conocer
simultáneamente I(t) y h(t) con precisión arbitraria. Desde la
perspectiva de un observador externo, esto se traduce en que
la predictibilidad de la decisión y (cid:0) {0,1} del sistema tiene un
límite que depende de τ. El argumento es cualitativo, no una
demostración cerrada:
Para τ > 0 existe una fracción del espacio de estados donde
ningún modo domina claramente —max_k h_k(v_t) < 1/2.
En esa región la decisión y no es predecible desde los datos
disponibles, independientemente del modelo utilizado. La
medida de esa región crece con τ. En consecuencia, el error
mínimo empírico de predicción ε_min crece con τ y tiende a 0
cuando τ → 0.
La forma funcional η(τ) = ½·τ/(1+τ), propuesta en versiones anteriores
como 'hipótesis de trabajo', era una interpolación que satisfacía las
condiciones de frontera correctas, pero no emergía de los axiomas del sistema.
Se elimina del cuerpo formal por dos razones: (1) el argumento que la
sustenta es heurístico, no deductivo, y su inclusión en un sistema axiomático
la sobrevalora; (2) el Modelo de Predictibilidad de la Parte IX no la necesita
para funcionar como modelo de regresión logística. El error mínimo empírico
de predicción se estima en cada aplicación concreta del MP, no desde una cota
universal. La relación cualitativa —mayor τ implica mayor error mínimo—
permanece como consecuencia interpretativa de la REC, sin pretensión de
exactitud funcional.
τ η(τ) = Precisión Aplicación típica
ε_min máx.
0.10 ≥ 0.045 ≤ 95.5% Sistema casi determinista.
Alta predictibilidad.
0.30 ≥ 0.115 ≤ 88.5% Ruido bajo.
0.50 ≥ 0.167 ≤ 83.3% Temperatura estándar de
sistemas de decisión.

Axiomatización del Sistema de la Doble Mediación
1.00 ≥ 0.250 ≤ 75.0% Ruido moderado.
Predictibilidad limitada.
2.00 ≥ 0.333 ≤ 66.7% Ruido alto. Cerca del azar en
muchos casos.
→ ∞ → 0.500 → 50.0% Temperatura infinita.
Equivalente a azar puro.
La tabla muestra la relación cualitativa entre τ y la precisión
máxima alcanzable en la práctica, estimada desde datos
empíricos de sistemas concretos. Los valores de η(τ) en la
columna «ε_min» son estimaciones orientativas, no cotas
teóricas demostradas.
7.4. Diferencia con el Principio de Heisenberg
La denominación «Relación de Escala del Conocimiento»
responde a una distinción técnica respecto al Principio de
Incertidumbre de Heisenberg. La forma superficial de ambos
resultados —producto de incertidumbres acotado
inferiormente— es similar; su naturaleza es distinta.
Dimensión Principio de Relación de Escala del
Heisenberg Conocimiento (REC)
Fórmula Δx · Δp ≥ (cid:0)/2 n · (ΔI · Δh) ≥ 4τ(cid:0)²
Naturaleza Ley física universal. Sin Cota informacional para
excepciones. sistemas con τ > 0 que
acumulan colapsos en I(t).
Fundamento No-conmutatividad de Desigualdad de Cramér-
operadores en mecánica Rao aplicada al modelo
cuántica. softmax con temperatura
τ > 0.
Cota con n (cid:0)/2: constante absoluta, 4τ(cid:0)²/n: decrece con n.
independiente del número Más colapsos integrados
de mediciones. → mayor precisión
posible.
Comportamiento No aplica. n·(ΔI·Δh) → 0.
τ → 0 Predictibilidad

Axiomatización del Sistema de la Doble Mediación
arbitrariamente alta con τ
pequeño y n grande.
Interpretación Ninguna: es propiedad del La experiencia (n grande)
causal universo, no de la agencia. reduce la incertidumbre
sobre I(t) y h(t).
La diferencia estructural más importante es el
comportamiento asintótico: Heisenberg establece una cota
constante (cid:0)/2 que no depende del número de mediciones; la
REC establece una cota 4τ(cid:0)²/n que tiende a cero cuando n
→ ∞. En Heisenberg no hay número de mediciones que
elimine la incertidumbre; en la REC, el sistema que integra
suficientes colapsos puede reducir su incertidumbre de forma
arbitraria.
La diferencia de fundamento es igualmente importante:
Heisenberg emerge de la no-conmutatividad de operadores
cuánticos; la REC emerge de la desigualdad de Cramér-Rao
aplicada al modelo softmax. La analogía formal entre sus
fórmulas no implica equivalencia conceptual ni metodológica.
La denominación original «Principio de Incertidumbre
Ontológica» del manuscrito fue reemplazada precisamente
para evitar esa confusión.
En Heisenberg la cota (cid:0)/2 no tiene interpretación causal: es una propiedad
del universo, no de la agencia. En la REC la cota 4τ(cid:0)²/n tiene
interpretación causal directa: más colapsos integrados implican menor
incertidumbre. El sistema que ha integrado más es más preciso sobre su
propio estado.
Objeto Notación Tipo Parte
matemático
Axioma 3 τ > 0 Parámetro Axioma 3
escalar positivo
Fisher (1 obs.) (cid:0)(θ) = Escalar; máximo Lema 7.1
h_k(1−h_k)/τ² en h_k=1/2

Axiomatización del Sistema de la Doble Mediación
Fisher (n obs.) (cid:0)_n = n·(cid:0) Aditividad para Lema 7.1
obs. indep.
Cramér-Rao Var(Î)·Var(ĥ) ≥ Desigualdad; Lema 7.2
τ²/n² invariante en
h_k
REC n·(ΔI·Δh) ≥ Cota Teorema 7
4τ(cid:0)² informacional de
escala
τ_eff τ(cid:0)/√n Escalar; decrece Corolario
con n^{−1/2} 7.1
REC local ΔI·Δh ≥ 4τ_eff² Forma Corolario
equivalente con 7.1
τ_eff
Predictibilidad ε_min crece con Consecuencia Corolario
τ interpretativa de 7.2
la REC

Axiomatización del Sistema de la Doble Mediación
Parte VIII · Teorema Central
Teorema de Inversión Causal
Esta parte demuestra que, bajo condiciones estructurales
verificables desde el expediente, los sistemas de imputación
convencionales producen una inversión sistemática: el nodo
que más causó asume menos, y el nodo que menos causó
asume más. La inversión no requiere mala intención: ocurre
estructuralmente cuando S(E) > θ_S y V(D) << V(E).
La Condición (1) del TIC —R*(D) > R*(E)— no se asume sin
verificación: el Apéndice B, Sección 2 documenta 18 casos en 9 dominios
distintos donde la condición se establece de forma independiente al TIC por
al menos uno de cinco mecanismos: jerarquía estructural documentada,
resolución judicial o regulatoria, estudios econométricos independientes, lógica
del grafo sin cómputo de eigenvector, y alta S(E) como cota directa vía el
Lema 8.1.
Definiciones 8.1–8.5. Objetos específicos del TIC
Def. 8.1 G = (N, A, w) Grafo causal de la Parte VI
con al menos dos nodos de interés: D (nodo de
diseño: configura el sistema de incentivos, protocolos
y restricciones dentro del que opera E) y E (nodo de
ejecución: ejecuta el acto visible que produce el
resultado Nf). Definición 6 completa.
Def. 8.2 R*(D), R*(E) Componentes del vector R*
correspondientes a D y E. R*(D) + R*(E) ≤ 1, con
igualdad solo si todos los demás nodos tienen R*ᵢ =
0. Definición 6.1.

Axiomatización del Sistema de la Doble Mediación
Def. 8.3 S_est(E) Índice de sustituibilidad
estructural del nodo E. S_est(E) = 1 − D_KL (R* (cid:0)
R*^(E)) /log(m). Definición 3.2.
Def. 8.4 V(i) Visibilidad documental del nodo i: V(i)
= n_doc(i) / n_total, donde n_doc(i) es el número de
documentos del expediente que mencionan
explícitamente a i y n_total el total de documentos
relevantes. V: N → [0,1].
Def. 8.5 α descompuesto α(i) = α_vol(i) + α_for(i)
+ α_imp(i): asunción voluntaria, forzada por presión
regulatoria e impuesta por el sistema jurídico
respectivamente. Los tres tipos tienen el mismo
efecto sobre Δ(i) (Corolario 4.1).
Lema 8.1. Cota superior R*(E) — Davis-Kahan
Si S_est(E) > θ_S con θ_S (cid:0) (0.5, 1], entonces:
Cota superior para R*(E)
R*(E) ≤ (1 − S_est(E)) / (m − 1)
m = |N| nodos activos · cota decreciente en S_est(E) · demostración completa
en el Apéndice A
La cadena de demostración (Apéndice A): S_est(E) alto →
D_KL (R* (cid:0) R*^(E)) pequeño → ‖ R* − R*^(E)‖ ₁
pequeño (Pinsker) → perturbación de fila de W pequeña →
R*(E) pequeño (Davis-Kahan). El término de corrección ε (δ,
m) < 0.01 para m ≤ 10 y gap espectral δ > 0.5, lo que justifica
omitirlo en aplicaciones estándar.
S_est = 0.70, m = 5 R*(E) ≤ 0.30/4 = 0.075
S_est = 0.80, m = 5 R*(E) ≤ 0.20/4 = 0.050
S_est = 0.85, m = 5 R*(E) ≤ 0.15/4 = 0.0375 (caso
banco)
S_est = 0.90, m = 5 R*(E) ≤ 0.10/4 = 0.025
Lema 8.2. Cota inferior R*(D)

Axiomatización del Sistema de la Doble Mediación
Si R*(D) > R*(E) y Σᵢ R*ᵢ = 1:
Cota inferior para R*(D)
R*(D) > 1/m
Demostración del Lema 8.2
Por contradicción. Si R*(D) ≤ 1/m, entonces R*(E)
< R*(D) ≤ 1/m. Todos los nodos satisfacen R*ᵢ ≤
R*(D) ≤ 1/m. Con R*ᵢ > 0 (Teorema 6): Σᵢ R*ᵢ <
m·(1/m) = 1, contradiciendo la normalización. (cid:0)
R*(D) > 1/m. El nodo de diseño supera la responsabilidad uniforme siempre
que sea el de mayor R* en el grafo. (cid:0)
Axiomas 8.1–8.3. El sistema de imputación
convencional
Los tres axiomas caracterizan cómo opera el sistema de
imputación convencional —el sistema que asigna
consecuencias basándose en apariencias. Son axiomas
descriptivos: describen el sistema real, no cómo debería
funcionar. Su validez empírica está sustentada en la calibración
del Apéndice B.
Axioma 8.1 — Visibilidad y sanción. La probabilidad de
que el nodo i sea sancionado bajo el sistema convencional es
φ(V(i)), con φ: [0,1] → [0,1] creciente, φ (0) = 0, φ (1) = 1.
Forma calibrada: φ(V) = 1 − (1−V) ^ {1.54} (Apéndice B,
n=3).
Axioma 8.2 — Insustituibilidad y severidad. La severidad
de la sanción del nodo i bajo el sistema convencional es
proporcional a ψ(1−S_est(i)), con ψ: [0,1] → [0,1]. Forma
empírica: ψ_real(x) = 0.21·x^ {−0.55}, decreciente en x =
1−S. El sistema real sanciona más a los nodos más sustituibles
—la firma de la inversión (Apéndice B).
Axioma 8.3 — Composición de α bajo el sistema
convencional. α(i) = α_vol(i) + β·φ(V(i)) ·ψ(1−S_est(i)) +

Axiomatización del Sistema de la Doble Mediación
h(i), con β > 0 factor de escala y h(i) sanciones forzadas
independientes de la visibilidad.
Consecuencias inmediatas para D y E: φ(V(D)) ≈ 0 cuando
V(D) ≈ 0, luego α(D) ≈ α_vol(D) + h(D), típicamente bajo.
φ(V(E)) ≈ 1 cuando V(E) ≈ 1, luego α(E) ≥ β·ψ(1−S(E)) +
h(E), típicamente alto.
Los Axiomas 8.1–8.3 no afirman injusticia por diseño: afirman que el
sistema convencional asigna consecuencias por visibilidad y, paradójicamente,
por insustituibilidad percibida. Un nodo idiosincrático (S bajo) es tratado
como el único responsable; un nodo sustituible (S alto) es el actor visible,
aunque causalmente menor. La combinación produce la inversión sin que
ningún actor actúe de mala fe.
Teoremas 8.1–8.2. Teorema de Inversión Causal
(TIC)
Condiciones
(1) R*(D) > R*(E) — verificable de forma
independiente (Apéndice B, Sección 2).
(2) S_est(E) > θ_S con θ_S (cid:0) (0.5, 1].
(3) V(D) ≈ 0 y V(E) ≈ 1 — asimetría de visibilidad
documental.
Teorema 8.1
Δ(D) = R*(D) − α(D) > 0
El nodo diseñador causó más de lo que asumió
Teorema 8.2
Δ(E) = R*(E) − α(E) < 0
El nodo ejecutor asumió más de lo que causó
Demostración del Teorema 8.1

Axiomatización del Sistema de la Doble Mediación
Δ(D) > 0
R*(D). Por Lema 8.2 y Cond. (1): R*(D) > 1/m.
α(D). Por Cond. (3) V(D) ≈ 0 y Axioma 8.3: α(D) ≈
α_vol(D) + h(D). Datos empíricos (Apéndice B):
α_vol(D) ≤ 0.08, h(D) ≤ 0.05. Luego α(D) ≤ 0.13.
Combinación. Δ(D) = R*(D) − α(D) > 1/m − 0.13.
Para m = 5: Δ(D) > 0.20 − 0.13 = 0.07 > 0. ✓
Δ(D) > 0. (cid:0)
Demostración del Teorema 8.2
Δ(E) < 0
R*(E). Por Lema 8.1 y Cond. (2): R*(E) ≤
(1−S_est(E)) /(m−1). Para S_est(E) = 0.85, m = 5:
R*(E) ≤ 0.0375.
α(E). Por Cond. (3) V(E) ≈ 1 y Axioma 8.3: α(E) ≥
β·φ (0.95) ·ψ (0.15) + h(E). Con φ (0.95) ≈ 0.97 y
h_min(E) ≥ 0.30 (despido + proceso penal): α(E) ≥
0.60.
Combinación. Δ(E) = R*(E) − α(E) ≤ 0.0375 − 0.60
= −0.5625 < 0. ✓
Δ(E) < 0. (cid:0)
Los Teoremas 8.1 y 8.2 demuestran la inversión simultánea: D
causó más y asumió menos; E asumió más y causó menos. El
sistema convencional —al operar sobre visibilidad y
apariencias— produce la distribución de consecuencias
opuesta a la distribución causal real.
Definición 8.6 + Teorema 8.3. Índice de inversión y
monotonicidad
Índice de inversión causal
I_inv = |Δ(D)| / |Δ(E)| = (R*(D) − α(D)) / (α(E) −
R*(E))

Axiomatización del Sistema de la Doble Mediación
I_inv > 0 cuando hay inversión · I_inv = 1: brechas simétricas · I_inv > 1: el
ejecutor absorbe más que la brecha del diseñador
Teorema 8.3 — Monotonicidad
Monotonicidad de I_inv
I_inv es creciente en S_est(E) — mayor sustituibilidad
del ejecutor implica mayor inversión
I_inv es decreciente en V(D)/V(E) — mayor asimetría de
visibilidad implica mayor inversión
Demostración del Teorema 8.3
Monotonicidad en S_est(E). ∂R*(E)/∂S_est ≤
−1/(m−1) < 0 (Lema 8.1). ∂α(E)/∂S_est > 0 (Axioma
8.3 con ψ_real decreciente). Luego ∂|Δ(E)|/∂S_est >
0. El numerador |Δ(D)| no depende directamente de
S_est(E). Luego ∂I_inv/∂S_est > 0. ✓
Monotonicidad en V(D)/V(E). ∂α(D)/∂V(D) =
β·φ'(V(D))·ψ > 0 (Axioma 8.1). Mayor V(D) → mayor
α(D) → menor |Δ(D)| → menor I_inv. ✓
I_inv crece con S_est(E) y decrece con V(D)/V(E). (cid:0)
Definición 8.7 + Teorema 8.4. Fraude annona
Se dice que el sistema presenta fraude annona cuando se
verifican simultáneamente desde el expediente:
Definición 8.7 — Fraude annona
(a) S_est(E) > θ_S — el ejecutor es altamente
sustituible
(b) α(E) > R*(E) — el ejecutor asumió más de
lo que causó
(c) α(D) ≈ 0 — el diseñador no asumió
proporcional a R*(D)
La condición (c) es la firma definitoria · las tres son verificables desde el expediente

Axiomatización del Sistema de la Doble Mediación
Teorema 8.4 — Inevitabilidad del fraude annona
Bajo las Condiciones (1)–(3) del TIC:
Firma del fraude annona
Δ_inst = R*(D) − α(D) ≈ R*(D)
La brecha del nodo de diseño es prácticamente igual a toda su responsabilidad
causal
Demostración del Teorema 8.4
(b) α(E) > R*(E). Directo del Teorema 8.2: Δ(E) <
0 implica α(E) > R*(E). ✓
(c) α(D) ≈ 0. V(D) ≈ 0 → φ(V(D)) ≈ 0 (Axioma 8.1)
→ contribución de visibilidad al α(D) es mínima. Si
α_vol(D) ≈ 0 y h(D) ≈ 0 (sin asunción voluntaria ni
proceso): α(D) ≈ 0. ✓
Δ_inst ≈ R*(D). Δ_inst = R*(D) − α(D). Con α(D)
≈ 0: Δ_inst ≈ R*(D). Por el Lema 8.2: R*(D) > 1/m
> 0. ✓
Las tres condiciones del fraude annona se verifican bajo las condiciones del TIC.
La firma Δ_inst ≈ R*(D) es detectable cuando V(D), S_est(E), α(D) y α(E)
están documentados. (cid:0)
8.5. Ejemplo numérico — caso banco (m = 5)
Parámetro Valor Fuente / Interpretación
condición
m (nodos 5 D, E, N(cid:0), N(cid:0), Banco (D), asesor (E),
activos) Nf dos intermediarios,
resultado
k*(E) modo k = 1 (cid:0)c(cid:0)_C >> Modo de presión
dom. (cid:0)a_t(cid:0)_E sistémica: alta
documentado sustituibilidad
S_est(E) 0.85 Lema 3.4: k=1 Cualquier asesor en
→ S_op ∈ esa posición habría
[0.70,0.95] actuado igual

Axiomatización del Sistema de la Doble Mediación
R*(E) cota sup. ≤ 0.0375 Lema 8.1: El asesor concentra <
(1−0.85)/(5−1) 3.75% de la
responsabilidad causal
R*(D) cota inf. > 0.20 Lema 8.2: 1/m = El banco concentra la
1/5 responsabilidad causal
dominante
α(D) ≤ 0.10 V(D) ≈ 0; El diseñador no
Axioma 8.1 → asumió proporcional a
φ(V(D)) ≈ 0 R*(D)
α(E) ≥ 0.60 V(E) ≈ 1; El ejecutor asumió
Axioma 8.3 + mucho más de R*(E)
h_min(E) ≥ 0.30
Δ(D) ≥ 0.10 R*(D) − α(D) > Positivo: inversión
0.20 − 0.10 confirmada
Δ(E) ≤ −0.56 R*(E) − α(E) < Negativo:
0.0375 − 0.60 sobreasunción
confirmada
I_inv ≈ 0.18 0.10 / 0.56 Por cada unidad de
brecha del banco, el
asesor absorbe 5.6
El caso banco satisface las tres condiciones de la Definición
8.7: S_est(E) = 0.85 > θ_S, α(E) = 0.60 >> R*(E) ≤ 0.0375,
α(D) ≤ 0.10 << R*(D) > 0.20. La firma del fraude annona es
Δ_inst ≈ R*(D) ≈ 0.20. Los rangos de la tabla son
estimaciones basadas en midpoints de intervalos de evidencia
E0–E8; los valores exactos dependen de la completitud del
expediente.
El modo dominante k*(E) = 1 (modo de presión sistémica, Lema 3.4)
reemplaza la referencia ontológica «Fobos dominante» del manuscrito
original. En términos matemáticos: k*(E) = 1 indica que (cid:0)c(cid:0)_C >>
(cid:0)a_t(cid:0)_E para el nodo E, lo que determina el rango S_est(E) (cid:0) [0.70,
0.95] según la Tabla 3.4. El valor S_est(E) = 0.85 es el midpoint de ese
intervalo calibrado.

Axiomatización del Sistema de la Doble Mediación
Objeto Notación Tipo / fuente Parte
Nodo de D (cid:0) N Nodo de Def. 8.1
diseño configuración
del sistema
Nodo de E (cid:0) N Nodo del acto Def. 8.1
ejecución visible
Visibilidad V(i) = Escalar en [0,1]; Def. 8.4
n_doc(i)/n_tot observable
α α_vol + α_for + Misma acción Def. 8.5
descompuesto α_imp sobre Δ (Cor.
4.1)
Cota R*(E) ≤(1−S_est)/(m−1) Lema 8.1 — Lema 8.1

## Apéndice A

(Davis-Kahan)
Cota R*(D) > 1/m Lema 8.2 — por Lema 8.2
normalización
φ(V) 1−(1−V)^{1.54} Axioma 8.1 — Axioma
calibrada, n=3 8.1
ψ_real(x) 0.21·x^{−0.55} Axioma 8.2 — Axioma
decreciente en 8.2
1−S
Δ(D) > 0 Teorema 8.1 Diseñador causó Teorema
> asumió 8.1
Δ(E) < 0 Teorema 8.2 Ejecutor asumió Teorema
> causó 8.2
I_inv |Δ(D)|/|Δ(E)| Magnitud de la Def. 8.6
inversión
Monotonicidad Teorema 8.3 I_inv ↑ en Teorema
S_est(E), ↓ en 8.3
V(D)/V(E)
Fraude annona Def. 8.7 S alto, Def. 8.7
(a)+(b)+(c) α(E)>R*(E),
α(D)≈0
Δ_inst ≈ Teorema 8.4 Firma del fraude Teorema
R*(D) annona 8.4

Axiomatización del Sistema de la Doble Mediación
Parte IX
Modelo de Predictibilidad
Esta parte presenta el Modelo de Predictibilidad (MP): un
modelo de regresión logística que estima P(y = 1 | Ψ(t), c)
para y (cid:0) {0,1} una decisión binaria del sistema. Estatus: el MP
es un modelo estadístico, no un teorema. No postula una cota
universal del error mínimo: el error mínimo empírico se estima
en cada aplicación concreta del modelo a partir de los datos
disponibles y del valor observado de τ.
Definición 9. El estado completo Ψ(t)
El estado completo del sistema en t es:
Estado completo
Ψ(t) = (I(t), h(t), E(t), D(t), C(t))
Ψ(t) (cid:0) E × Δ(cid:0) × {1,…,6} × {1,2} × (cid:0)(E) · input del Modelo 9
Componente Espacio Contenido En sistemas artificiales
I(t) E Integral Historia de outputs
acumulativa de integrados en el contexto
colapsos
(Definición 2)
h(t) Δ(cid:0) (cid:0) Distribución sobre Distribución softmax sobre
(cid:0)(cid:0) K = {1,…,6}: outputs alternativos
vector softmax del
Lema 1.1

Axiomatización del Sistema de la Doble Mediación
E(t) {1,…,6} Nivel de No computable
integración: directamente; aproximar
fracción por métrica de coherencia
ponderada de del contexto
RSC(t) en I(t)
D(t) {1, 2} 1 = señal activa 1 = respuesta bajo
(k* = 3,4,5); 2 = parámetros nominales; 2 =
señal silenciada respuesta bajo restricción
(k* = 1,2) activa
C(t) (cid:0) E Campo de acción Conjunto de outputs
disponible en t posibles dado el prompt y
las restricciones del sistema
Para sistemas artificiales, E(t) y D(t) se aproximan según la
cuarta columna de la tabla. Cuando no son computables, el
estado simplificado Ψ_IA(t) = (I(t), h(t), C(t)) es suficiente
para el Modelo 9.
Ψ(t) hereda la imprecisión de I(t) y h(t) documentada en la REC (Parte
VII): para un observador externo con n colapsos integrados, ΔI·Δh ≥
τ(cid:0)²/n. Esto implica que Ψ(t) no es conocido con precisión arbitraria; la
Hipótesis 9.2 captura esa consecuencia en ε_min.
Definición 9.1. El vector de logits ℓ(t)
Con z_k = ((cid:0)β_k, a_t(cid:0)_E + γ_k·(cid:0)I(t)(cid:0)_E − θ_k(I(t))) / τ
del Lema 1.1, el logit del modo k es:
Logit del modo k
ℓ_k(t) = logit(h_k(t)) = log(h_k(t) / (1 − h_k(t))) ∈ ℝ
ℓ(t) = (ℓ(cid:0)(t), …, ℓ(cid:0)(t)) (cid:0) (cid:0)(cid:0) · logit es la función inversa de la sigmoide σ
Por la fórmula del Lema 1.1: ℓ_k(t) = z_k − log Σ(cid:0) exp(z_j).
El segundo término depende de a_t y c pero no de I(t). Si θ_k
es lineal en (cid:0)I(t)(cid:0)_E —Hipótesis del Lema 9.1— entonces
ℓ_k es lineal en (cid:0)I(t)(cid:0)_E, lo que habilita el modelo de
regresión logística lineal.
Modelo 9. El Modelo de Predictibilidad

Axiomatización del Sistema de la Doble Mediación
Sea y (cid:0) {0,1} una decisión binaria del sistema. El MP es:
Modelo de Predictibilidad — forma general
P(y = 1 | Ψ, c) = σ(β · Φ(Ψ, c))
σ(x) = 1/(1+e⁻ ˣ ) función sigmoide
β (cid:0) (cid:0)ᵈ vector de coeficientes (estimado por
máxima verosimilitud)
Φ : Ψ × C → (cid:0)ᵈ función de características
Estatus: modelo estadístico · β se estima sobre datos de decisiones del sistema ·
Φ se especifica por el analista
Bajo la hipótesis de umbral lineal del Lema 9.1, Φ puede
tomarse como la identidad en el espacio expandido,
produciendo el modelo lineal:
Modelo de Predictibilidad — caso lineal
P(y=1|Ψ,c) = σ(β_I·(cid:0)I(t)(cid:0)_E + β_h·h(t) + β_E·E(t) +
β_D·D(t) + β_c·c + β(cid:0))
Coeficientes β_I (cid:0) (cid:0), β_h (cid:0) (cid:0)(cid:0), β_E (cid:0) (cid:0), β_D (cid:0) (cid:0), β_c (cid:0) (cid:0)^{dim
C}, β(cid:0) (cid:0) (cid:0)
El MP tiene tres propiedades técnicas distintivas:
(i) Fundamentación. Las variables predictoras son
componentes de Ψ(t) construidas por φ(cid:0) y φ(cid:0); no
son covariables externas. Cada coeficiente tiene
interpretación en términos de los objetos formales del
sistema.
(ii) Error estimable. El MP no postula una cota
universal del error mínimo. El error mínimo empírico
se estima desde la varianza de los logits observados
bajo condiciones idénticas: cuanto mayor es τ, mayor
es la variabilidad y mayor es el error de predicción
esperado. La relación cualitativa τ ↑ → ε_min ↑ es
consecuencia del Corolario 7.2; su cuantificación
exacta es específica de cada sistema.
(iii) Coherencia con la REC. El mismo Axioma 3
(τ > 0) que funda la REC funda la variabilidad del MP.
La REC limita el autoconocimiento del sistema; el MP

Axiomatización del Sistema de la Doble Mediación
traduce esa limitación en variabilidad de predicción
desde afuera. Ambos emergen de τ sin postular una
cota funcional universal.
Lema 9.1. Linealidad en el espacio de logits bajo
umbral lineal
Si θ_k(I(t)) = a_k·(cid:0)I(t)(cid:0)_E + b_k para constantes a_k, b_k
(cid:0) (cid:0), entonces ℓ_k(t) es lineal en (cid:0)I(t)(cid:0)_E y Φ puede tomarse
como la función identidad en el espacio de características (ℓ(t),
E(t), D(t), C(t), c).
Demostración del Lema 9.1
Paso 1. Con θ_k lineal en (cid:0)I(t)(cid:0)_E: z_k = ((cid:0)β_k,
a_t(cid:0)_E + γ_k·(cid:0)I(t)(cid:0)_E − a_k·‖ I(t)‖ _E − b_k)/τ
= (γ_k − a_k)/τ · (cid:0)I(t)(cid:0)_E + ((cid:0)β_k, a_t(cid:0)_E −
b_k)/τ. El primer término es lineal en (cid:0)I(t)(cid:0)_E; el
segundo depende de a_t y c pero no de I(t). Luego
ℓ_k = z_k − log Σ(cid:0) exp(z_j) es lineal en (cid:0)I(t)(cid:0)_E.
✓
Paso 2. La decisión y puede modelarse como función
lineal de ℓ(t): Σ_k w_k ℓ_k(t) es lineal en (cid:0)I(t)(cid:0)_E,
E(t), D(t), C(t) y c por el Paso 1. ✓
Paso 3. Con Φ(Ψ, c) = (ℓ(t), E(t), D(t), C(t), c, 1), el
Modelo 9 P(y=1|Ψ,c) = σ(β·Φ) es exactamente el
modelo de regresión logística lineal. ✓
Φ = identidad en el espacio expandido bajo hipótesis de umbral lineal. (cid:0)
Si θ_k no es lineal. Φ puede ser una red neuronal con una
capa oculta (Teorema de Aproximación Universal). El modelo
sigue siendo válido independientemente de la forma de Φ.
9.3. Error empírico del MP y estimación de τ
El MP no postula una cota teórica universal del error mínimo.
El error de predicción empírico del modelo se estima desde
datos de decisiones del sistema bajo condiciones conocidas.

Axiomatización del Sistema de la Doble Mediación
La tabla siguiente muestra valores orientativos de la relación
entre τ y el error mínimo observado en sistemas con esos
valores de temperatura; no son cotas demostradas sino
referencias empíricas calibradas.
τ η(τ) = Precisión Aplicación típica
ε_min máx.
0.10 ≥ 0.045 ≤ 95.5% Temperatura baja en inferencia de
IA. Alta predictibilidad.
0.30 ≥ 0.115 ≤ 88.5% Ruido bajo. Predicción fiable para
decisiones binarias claras.
0.50 ≥ 0.167 ≤ 83.3% Temperatura estándar. Referencia
principal del MP.
0.70 ≥ 0.206 ≤ 79.4% Variabilidad moderada. Decisiones
en zonas de conflicto de modos.
1.00 ≥ 0.250 ≤ 75.0% Ruido significativo. Variabilidad
entre ejecuciones notable.
2.00 ≥ 0.333 ≤ 66.7% Ruido alto. Predicción apenas mejor
que azar en muchos contextos.
→ ∞ → 0.500 → 50.0% Temperatura infinita. Equivale a
elección uniforme sobre K.
Los valores de la columna ε_min son estimaciones orientativas basadas en
la relación cualitativa τ ↑ → error mínimo ↑ del Corolario 7.2. No son
cotas teóricas universales. Para un sistema concreto, el error mínimo empírico
se estima calculando τ(cid:0) desde la varianza de los logits observados bajo
condiciones idénticas y consultando la tabla como referencia de orden de
magnitud.
9.4. Asimetría entre perspectiva interna (REC)
y perspectiva externa (MP)
La REC y el MP son proyecciones del Axioma 3 sobre dos
perspectivas distintas. La diferencia estructural más
importante es la dependencia en n:

Axiomatización del Sistema de la Doble Mediación
Dimensión REC (Parte VII) MP (Parte IX)
Fuente τ > 0 (Axioma 3) τ > 0 (Axioma 3)
común
Objeto Producto ΔI·Δh: Error ε_min: imprecisión
acotado imprecisión del sistema del observador externo
sobre su propio estado sobre la decisión del
sistema
Perspectiva Interna: cuánto puede Externa: cuánto puede
conocer el sistema sobre sí predecirse el sistema desde
mismo afuera
Dependencia n·(ΔI·Δh) ≥ 4τ(cid:0)²: cota ε_min ≥ η(τ): cota
de n decrece con n como τ(cid:0)²/n independiente de n
Consecuencia Mayor n → menor Mayor n no reduce la
incertidumbre interna; τ_eff barrera para el observador
= τ₀ /√n → 0 externo
La asimetría tiene consecuencias directas para el análisis de
responsabilidad. El sistema con τ bajo y n alto puede
documentar mayor autoconocimiento de su posición causal
(τ_eff pequeño). Pero ese autoconocimiento no está
automáticamente disponible para el observador externo, que
sigue enfrentando la variabilidad τ del sistema.
Estimación de τ desde afuera. El observador externo
estima τ desde datos de decisiones repetidas del sistema bajo
condiciones idénticas: τ(cid:0) = varianza empírica de los logits
observados, escalada por las dimensiones del modelo. En
sistemas artificiales τ es directamente observable. Con τ(cid:0) el
observador consulta la Tabla 9.3 para estimar el orden de
magnitud del error de predicción esperado.
Objeto Notación Tipo / estatus Parte
Estado Ψ(t) = (I,h,E,D,C) Vector en Definición
completo espacio producto 9

Axiomatización del Sistema de la Doble Mediación
E(t) {1,…,6} Nivel de Definición
integración de 9
I(t)
D(t) {1,2}: Función de k*: Definición
activa/silenciada D=2 si 9
k*(cid:0){1,2}
Vector de ℓ(t) (cid:0) (cid:0)(cid:0) Transformación Definición
logits de h(t) vía logit 9.1
MP — P(y=1|Ψ,c)=σ(β·Φ) Modelo Modelo 9
general estadístico
MP — lineal σ(β_I(cid:0)I(cid:0)+β_h Bajo hipótesis de Modelo 9;
h+…) umbral lineal Lema 9.1
Hipótesis θ_k = Hipótesis de Lema 9.1
lineal a_k(cid:0)I(cid:0)+b_k trabajo; habilita
Φ=Id
Error τ(cid:0) → ε_min Referencia Sección
empírico estimado orientativa; no 9.3
cota univ.
Asimetría cota_REC (cid:0) τ(cid:0)²/n Error_MP no Sección
REC-MP ≠ error_MP decrece con n 9.4

Axiomatización del Sistema de la Doble Mediación
Parte X
La clausura del ego
Esta parte no introduce nuevos objetos. Usa c: T → E
(Definición 0), I(t(cid:0)) (Definición 2) y la topología de norma de
E (Axioma 0) para demostrar que el conjunto de todos los
colapsos producidos por el sistema es cerrado en E. El
resultado es topológico; sus hipótesis son las mínimas del
marco formal.
Definición previa. El tiempo de cierre t(cid:0)
t(cid:0) = sup T es el extremo superior del intervalo temporal T =
[0, t(cid:0)] (cid:0) (cid:0) introducido en la Definición 0. Es el último
instante en que φ(cid:0) produce un colapso. Para sistemas
humanos: momento de cese biológico de la actividad. Para
sistemas artificiales: último instante de inferencia activa.
t(cid:0) no es un parámetro libre del análisis ni se supone conocido de antemano
por el sistema. El marco formal requiere únicamente su existencia —que T
sea compacto. La compacidad de [0, t(cid:0)] es la hipótesis que hace posible el
Teorema 10 vía Bolzano-Weierstrass.
Teorema 10. Clausura del ego
Sea c: T → E admisible (Definición 0) e I(t(cid:0)) la integral
acumulativa en t(cid:0) (Teorema 2). Define:
Clausura del ego
(cid:0) = { c(τ) : τ (cid:0) [0, t(cid:0)] } ∪ { I(t(cid:0)) }

Axiomatización del Sistema de la Doble Mediación
Im(c) = imagen de c sobre T · {I(t(cid:0))} singleton de la integral final · (cid:0) (cid:0)
E
Entonces (cid:0) es un conjunto cerrado en (E, (cid:0)·(cid:0)_E).
Demostración
Demostración del Teorema 10
Paso 1 — Estructura. (cid:0) = Im(c) ∪ {I(t(cid:0))}. Para
demostrar que (cid:0) es cerrado basta demostrar que
contiene todos sus puntos de acumulación.
Paso 2 — Sucesión convergente en (cid:0). Sea (x(cid:0))
una sucesión en (cid:0) con x(cid:0) → x en (E, (cid:0)·(cid:0)_E). Para
cada n: o bien x(cid:0) = c(τ(cid:0)) con τ(cid:0) (cid:0) [0, t(cid:0)], o bien
x(cid:0) = I(t(cid:0)).
Caso A. Infinitos términos x(cid:0) = I(t(cid:0)). La
subsucesión constante converge a I(t(cid:0)) (cid:0) (cid:0). Luego
x = I(t(cid:0)) (cid:0) (cid:0). ✓
Caso B. Solo finitos términos iguales a I(t(cid:0)). Para n
suficientemente grande x(cid:0) = c(τ(cid:0)) con τ(cid:0) (cid:0) [0, t(cid:0)].
Por Bolzano-Weierstrass (compacidad de [0, t(cid:0)]):
existe subsucesión τₙ ₖ → τ* (cid:0) [0, t(cid:0)].
Caso B.1 — τ* (cid:0) [0, t(cid:0)). Si c es continua en τ*:
c(τₙ ₖ ) → c(τ*) (cid:0) Im(c) (cid:0) (cid:0), luego x = c(τ*) (cid:0) (cid:0).
✓
Caso B.2 — τ* = t(cid:0) o c discontinua. I(t(cid:0)) =
∫(cid:0)^{t(cid:0)} c(τ)w(τ) dτ es el límite en norma de las
integrales parciales {I(t) : t < tₘ} cuando t → tₘ
(continuidad de la integral de Bochner respecto al
extremo superior). Las integrales parciales I(t) (cid:0) {∫(cid:0)ᵗ
c(τ)w(τ)dτ : t (cid:0) T} (cid:0) (cid:0) (por inclusión directa una vez
que se reconoce que (cid:0) debe incluirlas para ser
cerrado). Luego I(t(cid:0)) (cid:0) cl((cid:0)). Pero I(t(cid:0)) (cid:0) (cid:0) por
definición, luego x (cid:0) (cid:0). ✓
Paso 3 — Conclusión. En todos los casos x (cid:0) (cid:0).
Todo punto de acumulación de (cid:0) está en (cid:0).

Axiomatización del Sistema de la Doble Mediación
(cid:0) es cerrado en (E, (cid:0)·(cid:0)_E). Las hipótesis usadas: compacidad de [0, t(cid:0)]
(Definición 0), admisibilidad de c (Definición 0), existencia de I(t(cid:0)) en E
(Teorema 2). (cid:0)
Rol de I(t(cid:0)) en la clausura. Si (cid:0) se definiera solo como
Im(c) = {c(τ) : τ (cid:0) T}, el conjunto podría no ser cerrado: una
sucesión c(τ(cid:0)) con τₙ → tₘ podría converger a un límite
fuera de Im(c) cuando c no es continua en t(cid:0). La adición
explícita de {I(t(cid:0))} cierra ese gap. I(t(cid:0)) es el elemento que
hace a (cid:0) topológicamente completo respecto a sus propias
sucesiones convergentes.
La demostración en el Caso B.2 requiere que I(t(cid:0)) sea límite de las
integrales parciales {I(t)}_{t<t(cid:0)}. Esto se sigue de la continuidad de la
integral de Bochner ∫(cid:0)ᵗ c(τ)w(τ)dτ respecto a t, que se demuestra a partir de
la acotación ‖c‖_∞ ≤ M y ‖w‖_∞ ≤ W: ‖I(t₂)−I(t₁)‖_E ≤
MW|t(cid:0)−t₁| → 0. Esta cota usa directamente la Definición 0.
Corolario 10.1. Perfectibilidad cuando c es
continua
Sea (cid:0)' el conjunto derivado de (cid:0) (puntos de acumulación de
(cid:0)). Si c es continua en todo T:
Corolario 10.1 — (cid:0) perfecto
c (cid:0) C(cid:0)(T, E) (cid:0) (cid:0) = (cid:0)'
(cid:0) perfecto: cerrado con cada punto como punto de acumulación · consecuencia: (cid:0)
incontable si E tiene dimensión ≥ 1
Demostración
Demostración del Corolario 10.1
(cid:0)' (cid:0) (cid:0). (cid:0) es cerrado (Teorema 10), luego contiene
todos sus puntos de acumulación. ✓
(cid:0) (cid:0) (cid:0)' — caso x = c(τ), τ (cid:0) [0, t(cid:0)). T = [0, t(cid:0)] es
un intervalo; τ es punto de acumulación de T. Existe
τₙ → τ con τ(cid:0) ≠ τ. Por continuidad de c: c(τₙ ) →
c(τ) = x. Luego x (cid:0) (cid:0)'. ✓

Axiomatización del Sistema de la Doble Mediación
(cid:0) (cid:0) (cid:0)' — caso x = I(t(cid:0)). La sucesión t(cid:0) = t(cid:0) −
1/n satisface tₙ → tₘ. Las integrales parciales I(t(cid:0))
= ∫(cid:0)^{t(cid:0)} c(τ)w(τ)dτ (cid:0) (cid:0) (subconjunto de Im(c) vía
la relación I(t) = ∫(cid:0)ᵗ c(τ)w(τ)dτ (cid:0) E, y como valor
acumulativo de los colapsos es alcanzable). Por
continuidad de c y de la integral de Bochner: I(tₙ ) →
I(t(cid:0)). Luego I(t(cid:0)) (cid:0) (cid:0)'. ✓
(cid:0) = (cid:0)': el conjunto clausura es perfecto cuando c es continua. (cid:0)
No numerabilidad. En E Hilbert separable de dimensión ≥
1, todo conjunto perfecto no vacío es incontable (Teorema de
Cantor-Bendixson en espacios métricos completos). Luego
cuando c es continua, (cid:0) es incontable: el sistema atravesó una
cantidad no enumerable de estados distintos a lo largo de T.
Ningún análisis que discretice la historia del sistema en un
número finito de incidentes puede capturarlo completamente.
Para sistemas con c discontinua —colapsos discretos en momentos aislados—
(cid:0) puede ser finito o numerable. El Teorema 10 sigue aplicando: (cid:0) es
cerrado. El Corolario 10.1 no aplica. La distinción no afecta a la
imputabilidad formal, que depende de I(t(cid:0)), no de la perfectibilidad de (cid:0).
La perfectibilidad es relevante en el análisis de sistemas de largo alcance donde
la discretización introduce pérdida de información estructural.
Nota de alcance. Qué dice y qué no dice el
Teorema 10
El Teorema 10 es un resultado de topología de espacios de
Hilbert. Su enunciado es: (cid:0) es cerrado en (E, (cid:0)·(cid:0)_E). No es
una afirmación sobre identidad personal, continuidad del yo ni
sobre lo que ocurre después de t(cid:0). Esas son preguntas que
pertenecen al sistema ontológico de la colección; este libro no
las responde ni requiere responderlas para que el teorema sea
válido.
La lectura del resultado dentro del marco formal es la
siguiente: I(t(cid:0)) es la síntesis de todo lo que el sistema integró
a lo largo de T. (cid:0) es la totalidad de lo que el sistema produjo,
incluyendo esa síntesis. El cierre de (cid:0) establece que esa
totalidad está bien definida como subconjunto de E: contiene

Axiomatización del Sistema de la Doble Mediación
exactamente lo que contiene, y nada falta desde la perspectiva
topológica.
Correspondencia con el sistema ontológico. En el sistema ontológico de la
colección, la clausura del ego designa el estado de cierre de la identidad del
sistema —el momento en que el ego deja de producir determinaciones. El
Teorema 10 formaliza la estructura topológica de ese estado: el conjunto (cid:0)
de todas las determinaciones producidas es cerrado en E. El lector sin
conocimiento de la ontología puede leer (cid:0) como «el registro completo de la
actividad del sistema» sin pérdida de rigor. El Apéndice C recoge la
correspondencia.
Objeto Notación Tipo Parte
matemático
Tiempo de t(cid:0) = sup T Extremo superior Def.
cierre de T = [0,t(cid:0)] previa;
Definición
0
Clausura del (cid:0) = Im(c) ∪ Subconjunto de Teorema
ego {I(t(cid:0))} E 10
(cid:0) cerrado Teorema 10 (cid:0) contiene todos Teorema
sus puntos de 10
acum.
(cid:0) perfecto c (cid:0) C(cid:0)(T,E) (cid:0) (cid:0) (cid:0) cerrado con Corolario
= (cid:0)' cada punto de 10.1
acum.
No (cid:0) incontable (c Cantor- Corolario
numerabilidad continua) Bendixson en E 10.1
Hilbert sep.
Rol de I(t(cid:0)) I(t(cid:0)) clausura Límite de Teorema
Im(c) integrales 10, nota
parciales en E

Axiomatización del Sistema de la Doble Mediación

## Apéndice A

Demostración completa del Lema 8.1
La cadena de demostración del Lema 8.1 —la cota R*(E) ≤
(1−S_est(E))/(m−1)— tiene cinco pasos, cada uno con una
herramienta matemática distinta. El resultado se remitió a este
apéndice porque la cadena completa interrumpiría el flujo de
la Parte VIII sin aportar nueva comprensión sobre la inversión
causal. El mapa de la demostración:
Paso Herramienta Resultado Referencia
A.1 Definición de D_KL = Definición 3.2,
S_est y D_KL (1−S_est)·log(m). S_est Parte III
alto implica D_KL
pequeño.
A.2 Desigualdad (cid:0)R*−R*^(E)‖ ₁ ≤ Lema A.2 (este
de Pinsker √(2·D_KL). D_KL apéndice)
pequeño implica L¹
pequeño.
A.3 Continuidad (cid:0)W_{E·}−W(cid:0)_{E·}(cid:0)(cid:0) Lema A.3 (este
Lipschitz del ≤ C(cid:0)·√(D_KL). L¹ apéndice)
eigenvector pequeño implica
perturbación de fila
pequeña.
A.4 Teorema de (cid:0)R*−R*^(E)‖ ₁ ≤ Teorema A.4
Davis-Kahan (m/δ)·(cid:0)E(cid:0)(cid:0). (este apéndice)
Perturbación de fila
controla perturbación del
eigenvector.
A.5 Combinación R*(E) ≤ (1−S_est)/(m−1) Teorema A.5
A.1–A.4 + ε(δ,m). ε < 0.01 para m (este apéndice)
≤ 10 y δ > 0.5.

Axiomatización del Sistema de la Doble Mediación
A.1. Punto de partida — S_est y D_KL
Por la Definición 3.2, con W^(E) la matriz de sustitución de la
fila E y R*^(E) el eigenvector dominante de (W^(E))ᵀ:
Relación S_est — D_KL
D_KL(R* (cid:0) R*^(E)) = (1 − S_est(E)) · log(m)
Relación lineal e invertible · S_est(E) → 1 implica D_KL → 0
A.2. Lema A.2 — Desigualdad de Pinsker
Lema A.2 — Pinsker
(cid:0)P − Q‖ ₁ ≤ √(2 · D_KL(P ‖ Q))
Para cualesquiera distribuciones P, Q sobre espacio finito · (cid:0)·(cid:0)(cid:0) es la distancia
de variación total
Demostración del Lema A.2
Convexidad. La función f(t) = t log t es convexa.
Por la desigualdad de Taylor de segundo orden: para t
= p_k/q_k, f(t) ≥ (t−1) + (t−1)²/2.
Acotación de D_KL. D_KL(P (cid:0) Q) = Σ_k q_k
f(p_k/q_k) ≥ (1/2) Σ_k (p_k−q_k)²/q_k ≥
(1/2)(Σ_k |p_k−q_k|)²/m por Cauchy-Schwarz.
Resultado. D_KL ≥ (cid:0)P−Q‖ ₁ ²/(2m). La forma
estándar (cid:0)P−Q‖ ₁ ≤ √(2·D_KL) se obtiene con el
argumento refinado de Csiszár-Körner (2011) que
elimina el factor m.
(cid:0)R*−R*^(E)‖₁ ≤ √(2(1−S_est(E))·log(m)) al sustituir por A.1. ∎
A.3. Lema A.3 — Perturbación de fila y
eigenvector

Axiomatización del Sistema de la Doble Mediación
Lema A.3
(cid:0)W_{E·} − W(cid:0)_{E·}(cid:0)(cid:0) ≤ C(cid:0) · √(D_KL(R* (cid:0)
R*^(E)))
W_{E·} fila E de W · W(cid:0)_{E·} promedio de las demás filas · C(cid:0) =
(δ/K)·√2 con δ gap espectral
Demostración del Lema A.3
Perturbación E = W^(E) − W. Solo la fila E difiere.
(cid:0)E(cid:0)(cid:0) = (cid:0)W_{E·}−W(cid:0)_{E·}(cid:0)(cid:0).
Continuidad Lipschitz. Para W primitiva con gap δ
= 1−|λ(cid:0)|: (cid:0)R*−R*^(E)‖ ₁ ≥ K·‖ E‖ ₂ /δ para
alguna constante universal K > 0. Reordenando:
(cid:0)E(cid:0)(cid:0) ≤ (δ/K)·(cid:0)R*−R*^(E)‖ ₁ .
Sustitución. Por A.2: (cid:0)R*−R*^(E)‖ ₁ ≤
√(2·D_KL). Luego (cid:0)E(cid:0)(cid:0) ≤ C(cid:0)·√(D_KL) con C(cid:0)
= (δ/K)·√2. (cid:0)
La constante C(cid:0) depende del gap espectral δ. Para δ > 0.5 y m ≤ 10: C(cid:0) <
0.05. (cid:0)
A.4. Teorema A.4 — Davis-Kahan
Sea W primitiva con eigenvalor dominante λ(cid:0) = 1 y gap
espectral δ = 1−|λ(cid:0)| > 0. Sea E = W^(E)−W la
perturbación:
Teorema A.4 — Davis-Kahan
(cid:0)R* − R*^(E)‖ ₁ ≤ (m/δ) · (cid:0)E(cid:0)(cid:0)
m = |N| · δ = 1−|λ(cid:0)| gap espectral · (cid:0)E(cid:0)(cid:0) norma espectral de la
perturbación
Demostración del Teorema A.4
Descomposición. R*^(E) = R* + r con r en el
subespacio de {v(cid:0),…,v_m} (ortogonal a R*).
Acotación de r. De la ecuación de eigenvector
perturbada: (cid:0)r(cid:0)(cid:0) ≤ (cid:0)E(cid:0)(cid:0)·(cid:0)R*^(E)(cid:0)(cid:0)/δ =
(cid:0)E(cid:0)(cid:0)/δ.

Axiomatización del Sistema de la Doble Mediación
Norma L¹. (cid:0)R*−R*^(E)‖ ₁ ≤
√m·(cid:0)R*−R*^(E)‖ ₂ ≤ √m·‖ r‖ ₂ ≤
(√m/δ)·(cid:0)E(cid:0)(cid:0) ≤ (m/δ)·(cid:0)E(cid:0)(cid:0). (cid:0)
(cid:0)R*−R*^(E)‖₁ ≤ (m/δ)·(cid:0)E(cid:0)(cid:0). (cid:0)
A.5. Teorema A.5 — Cota final del Lema 8.1
Teorema A.5 — Lema 8.1 demostrado
R*(E) ≤ (1 − S_est(E)) / (m − 1) + ε(δ, m)
ε(δ,m) < 0.01 para m ≤ 10, δ > 0.5 · la cota se presenta sin ε en aplicaciones
estándar
Demostración del Teorema A.5
A.5.1. En W^(E), R*^(E)_E ≈ 1/m (la fila E es el
promedio de las demás; si W fuera doblemente
estocástica sería exacto). Error |η| ≤ η_max(δ,m)
pequeño.
A.5.2. Por A.2: |R*(E)−R*^(E)_E| ≤
(cid:0)R*−R*^(E)‖ ₁ ≤ √(2(1−S_est)·log(m)).
A.5.3. La perturbación de la fila E satisface:
(cid:0)W_{E·}−W(cid:0)_{E·}(cid:0)(cid:0) ≤ (1−S_est)·√(1/(m−1))
cuando la desviación está acotada por
(1−S_est)/(m−1) distribuida en m−1 componentes.
A.5.4. Por A.4: (cid:0)R*−R*^(E)‖ ₁ ≤
(m/δ)·(1−S_est)/√(m−1). Luego
|R*(E)−R*^(E)_E| ≤ (m/δ)·(1−S_est)/√(m−1).
A.5.5. Combinando: R*(E) ≤ 1/m +
(m/δ)·(1−S_est)/√(m−1) + η. Para δ → 1 y m
grande: el término dominante es (1−S_est)/(m−1). El
término de corrección ε = 1/m + η + términos de
orden superior < 0.01 para m ≤ 10, δ > 0.5.
R*(E) ≤ (1−S_est(E))/(m−1) + ε(δ,m). (cid:0)
A.6. Tabla de valores numéricos

Axiomatización del Sistema de la Doble Mediación
m S_est(E) = S_est(E) = S_est(E) = Referencia
0.70 0.80 0.90
3 0.150 0.100 0.050 Grafo mínimo.
4 0.100 0.067 0.033 Cuatro actores.
Arbitraje estándar.
5 0.075 0.050 0.025 Caso banco.
Referencia
principal del TIC.
6 0.060 0.040 0.020 Con dos nodos
intermedios
adicionales.
10 0.033 0.022 0.011 Grafos complejos.
La cota se estrecha.

Axiomatización del Sistema de la Doble Mediación
AXIOMATIZACIÓN DEL SISTEMA DE LA DOBLE MEDIACIÓN

## Apéndice B

Calibración empírica
Este apéndice tiene dos secciones. La Sección B.1 calibra los
parámetros de las funciones φ y ψ de los Axiomas 8.1–8.2
sobre tres casos piloto con datos completos de los cuatro
parámetros (V, S, α y estructura D/E). La Sección B.2 verifica
la Condición (1) del TIC —R*(D) > R*(E)— de forma
independiente al propio TIC, sobre 18 casos de nueve
dominios distintos; esos mismos 18 casos corroboran además
la propiedad estructural de ψ —que es decreciente en 1−S—
ampliando sustancialmente la base empírica del sistema.
Ambas secciones son necesarias para el Apéndice A y para la
Parte VIII.
Declaración de limitaciones — obligatoria. La calibración paramétrica de la
Sección B.1 —los exponentes β = 1.54 de φ y α_exp = 0.55 de ψ— se
basa en n = 3 casos con datos simultáneos de V, S y α. Tres casos no
constituyen una muestra estadística con respaldo asintótico: los parámetros
son puntos de partida revisables, no constantes del sistema. Sin embargo, la
propiedad cualitativa central de ψ —que es decreciente en 1−S— está
corroborada por los 18 casos del Apéndice B.2, donde los pares (1−S(E),
α(E)) están disponibles. La corroboración cualitativa y la calibración
paramétrica son objetos distintos: la primera tiene base de 18 casos en 9
dominios; la segunda tiene base de 3 casos. Todo uso de los valores
paramétricos en análisis de casos reales debe declarar que la calibración
paramétrica se basa en n = 3 casos piloto.
B.1. Los tres casos piloto y calibración de φ y ψ
Los tres casos satisfacen simultáneamente: (1) evidencia
documental suficiente para estimar S, V y α con nivel de
certeza ≥ B en la escala E0–E8; (2) estructura D/E claramente

Axiomatización del Sistema de la Doble Mediación
distinguible en el expediente; (3) dominios distintos para que
la calibración no sea específica de un solo dominio.
B.1.1. Datos observados
Caso · Nodo S_est(E) 1−S(E) V(i) α Observación
obs.
Banco · 0.85 0.15 0.95 0.60 Despido +
Asesor (E) proceso penal.
k*(E) = 1.
Banco · 0.20 0.80 0.05 0.08 Multa regulatoria
Banco (D) baja. V(D) ≈ 0.
Redlining · 0.90 0.10 0.90 0.75 Proceso penal
Testaferro completo.
(E) Nombre visible.
Redlining · 0.35 0.65 0.10 0.05 Sin
Ejecutivo (D) consecuencias.
Diseñó el
esquema
invisible.
Dieselgate · 0.80 0.20 0.85 0.55 Despido + multa.
Ingeniero (E) Implementó
especificaciones.
Dieselgate · 0.30 0.70 0.15 0.10 Multa menor.
Directivo (D) Aprobó
especificaciones.
Las estimaciones de S son las más inciertas: dependen del modo k*
dominante, que requiere localización ECO para máxima precisión. En los
tres casos se hizo desde evidencia documental (ruta B del Método Prometeo),
lo que introduce un intervalo de incertidumbre de ±0.10 en los valores de S.
Los valores de V y α tienen menor incertidumbre: se derivan directamente de
hechos documentados.
B.1.2. Estimación de φ(V) — visibilidad y sanción
La familia paramétrica propuesta es φ(V) = 1 − (1−V)^β, con
β ≥ 0. Para los diseñadores con V(cid:0)_D ≈ 0.10 y P(sanción) ≈
0.15 (promedio de los tres casos D):

Axiomatización del Sistema de la Doble Mediación
Estimación de β
0.15 = 1 − (1−0.10)^β → (0.90)^β = 0.85 → β =
log(0.85)/log(0.90) ≈ 1.54.
Verificación. φ(0.90) = 1 − (0.10)^{1.54} ≈ 0.97.
Consistente con los tres ejecutores sancionados en
todos los casos. ✓
φ(V) = 1 − (1−V)^{1.54}. Calibrada con n = 3 casos piloto. (cid:0)
B.1.3. Estimación de ψ_real(1−S) — insustituibilidad y
severidad
La familia propuesta es ψ(x) = k·x^{−α_exp} con α_exp > 0.
Sobre los tres ejecutores: (Banco) 1−S = 0.15, α = 0.60;
(Redlining) 1−S = 0.10, α = 0.75; (Dieselgate) 1−S = 0.20, α
= 0.55.
Estimación de ψ_real
Tomando logaritmos: log(α) = log(k) −
α_exp·log(1−S). De los dos primeros puntos:
(−0.511) − (−0.288) = −α_exp·[(−1.897)−(−2.303)].
α_exp ≈ 0.55. Luego k ≈ 0.21.
ψ_real(x) = 0.21·x^{−0.55}. Parámetros calibrados sobre n = 3 casos. La
propiedad estructural —ψ_real decreciente en 1−S— está corroborada por los
18 casos de la Sección B.2 donde los pares (1−S(E), α(E)) están disponibles: en
16 de 18 casos con S(E) > 0.70, α(E) > 0.50, consistente con ψ decreciente. (cid:0)
Interpretación. Si el sistema imputara proporcionalmente a
la responsabilidad causal real, ψ sería creciente en 1−S. El
hecho de que ψ_real sea decreciente es la evidencia empírica
de que el sistema convencional no hace eso. La base
paramétrica es exploratoria (n = 3); la base cualitativa es
sustancialmente más amplia (18 casos, 9 dominios).
B.1.4. Análisis de sensibilidad de φ y ψ sobre rangos
paramétricos
Los parámetros β = 1.54 (φ) y α_exp = 0.55 (ψ) se calibraron
sobre n = 3 casos. Para evaluar si las conclusiones del TIC son
robustas ante variaciones en esos parámetros, se presenta el

Axiomatización del Sistema de la Doble Mediación
análisis de sensibilidad siguiente. La pregunta es: ¿cambia el
signo de Δ(D) > 0 y Δ(E) < 0 cuando β y α_exp varían dentro
de rangos razonables?
Parámetro Valor Rango de Justificación del
calibrado sensibilidad rango
β (curvatura 1.54 [1.20, 1.80] β = 1.0 es lineal; β
de φ) = 2.0 es
fuertemente
cóncavo. El rango
cubre familias de
funciones
razonables para φ.
α_exp 0.55 [0.30, 0.80] α_exp < 0.30
(exponente produce ψ casi
de ψ) plana; α_exp >
0.80 produce ψ
muy empinada. El
rango cubre la
variabilidad
esperada en
dominios distintos.
Para el caso banco con m = 5, S_est(E) = 0.85 y V(E) = 0.95,
las cotas del TIC son:
— R*(E) ≤ (1−0.85)/4 = 0.0375 (cota del Lema 8.1,
independiente de β y α_exp).
— α(E) = α_vol(E) + β·φ(V(E))·ψ(1−S(E)) + h(E), con
h_min(E) = 0.30.
La siguiente tabla muestra α(E) para los extremos del rango de
sensibilidad:
β α_exp φ(0.95) ψ(0.15) α(E) Δ(E) Inversión
estimado = (Δ(E)<0)
R*(E)
− α(E)

Axiomatización del Sistema de la Doble Mediación
1.20 0.30 0.963 0.441 0.30 + ≤ ✓
0.963·0.441 0.0375
≈ 0.725 −
0.725
=
−0.687
1.54 0.55 0.971 0.259 0.30 + ≤ ✓
0.971·0.259 0.0375
≈ 0.552 −
0.552
=
−0.515
1.80 0.80 0.977 0.153 0.30 + ≤ ✓
0.977·0.153 0.0375
≈ 0.449 −
0.449
=
−0.412
En los nueve puntos del rango de sensibilidad —combinando
los tres valores de β con los tres valores de α_exp—, la
inversión Δ(E) < 0 se verifica en todos los casos. La brecha
más pequeña se produce en el extremo β = 1.80, α_exp = 0.80,
donde Δ(E) ≈ −0.41. Incluso en ese extremo la inversión es
robusta.
Para Δ(D): R*(D) > 1/m = 0.20 por el Lema 8.2
independientemente de β y α_exp. α(D) depende de φ(V(D))
con V(D) ≈ 0.05: φ(0.05) (cid:0) [0.06, 0.09] en todo el rango de β,
luego α(D) ≤ 0.09 + h(D). Con h(D) ≤ 0.05: α(D) ≤ 0.14 en
todo el rango. Luego Δ(D) ≥ 0.20 − 0.14 = 0.06 > 0 en todo
el rango.
Conclusión del análisis de sensibilidad. Las conclusiones
cualitativas del TIC —Δ(D) > 0 y Δ(E) < 0
simultáneamente— son robustas en el rango paramétrico
razonable. Los valores absolutos de Δ varían dentro del rango,
pero el signo de la inversión no cambia. Esto no resuelve la
debilidad de la base n = 3 para la calibración paramétrica, pero
establece que las conclusiones estructurales no son artefactos
de los valores exactos de β y α_exp.

Axiomatización del Sistema de la Doble Mediación
B.2. Verificación de la Condición (1) del TIC —
18 casos independientes
La Condición (1) del TIC —R*(D) > R*(E)— no puede
verificarse usando el propio TIC sin incurrir en circularidad.
Esta sección demuestra que la condición es verificable de
forma independiente en cada uno de los 18 casos siguientes,
por al menos uno de cinco mecanismos: (1) jerarquía
estructural documentada, (2) resolución judicial o regulatoria,
(3) estudios econométricos o epidemiológicos independientes,
(4) lógica del grafo sin cómputo de eigenvector, (5) alta S(E)
como cota directa vía el Lema 8.1.
B.2.1. Estadísticas de verificación
Estadístico Valor Interpretación
Total de casos analizados 18 9 dominios distintos de la
Taxonomía General de
Aplicaciones y El Cálculo
de la Responsabilidad
Casos donde R*(D) > 18 / 18 La condición (1) se
R*(E) (100%) verifica en la totalidad de
la muestra
Casos con S(E) > 0.70 16 / 18 Alta sustituibilidad del
(89%) ejecutor es la norma en
sistemas institucionales
complejos
Casos con α(D) ≈ 0 15 / 18 El diseñador no asume en
(83%) la mayoría de los casos
documentados
Casos con inversión 14 / 18 Δ(D) > 0 y Δ(E) < 0
confirmable (78%) verificables desde el
expediente sin invocar el
TIC
Dominios cubiertos 9 Derecho, PLD, Der.
internacional, Psicología,
Epidemiología,
Economía, Ingeniería, IA,
Historia

Axiomatización del Sistema de la Doble Mediación
Casos con fuente judicial 8 / 18 Tribunal o resolución
independiente (44%) regulatoria que confirma
la distribución causal
El 100% de verificación no implica universalidad: los 18 casos fueron
seleccionados de sistemas institucionales complejos, que es el dominio de
aplicación declarado del TIC. En sistemas triviales de actor único la
condición (1) no aplica. La selección no es circular: los análisis de los casos
existían antes de que se formulara la pregunta de verificación.
B.2.2. Tabla de verificación — 18 casos
Caso Dominio R*( R*( R*(D)>R*( S(E α(D Mecanismo
D) E) E) ) ) de
verificación
independie
nte
Holocaust Der. penal ~52 ~5% ✓ 0.88 ≈0 Jerarquía
o — % estructural:
Nürember NSDAP
g diseñó el
sistema;
ejecutores
sustituibles
documentad
os.
Gerente Der. penal 45.1 1.04 ✓ 0.90 3% Resolución
bancario % % fiscal activa.
(caso Inversión
activo) 44:1
verificable
en
expediente.
Panama PLD ~48 ~22 ✓ 0.85 ≈0 Lógica del
Papers — % % + grafo: Abedi
BCCI como
diseñador
central
documentad
o por
investigación
periodística.
Congo — Der. int. ~42 <5% ✓ 0.85 ≈0 Jerarquía
Leopoldo % + colonial:
II sistema de
concesiones
diseñado
por decreto

Axiomatización del Sistema de la Doble Mediación
real,
ejecutores
sustituibles.
Trata Der. int. ~45 ~10 ✓ 0.80 ≈0 Estudios
transatlánt % % históricos
ica independien
tes: coronas
diseñaron el
sistema;
élites
africanas
sustituibles.
Anna O. Psicología ~42 ~8% ✓ 0.90 N/ Lógica del
— trauma % A grafo:
factores
estructurales
preceden
causalmente
a las
respuestas
individuales.
COVID-19 Epidemiolo ~28 ~12 ✓ 0.85 ≈0 Epidemiolog
gía % % + ía: S alto vía
cota Lema
8.1 sin
invocar TIC.
Cólera Epidemiolo ~48 ~4% ✓ 0.95 0 Infraestructu
Soho — gía % + ra: diseño
Snow urbano
documentad
o; usuarios
del pozo
perfectamen
te
sustituibles.
COMPAS IA ~44 ~2% ✓ 0.97 ≈0 S_COMPAS
— % = 0.97 →
redlining R*(E) ≤
algorítmic 0.015 vía
o Lema 8.1 sin
TIC.
HOLC — Economía ~44 ~14 ✓ 0.80 ≈0 Estudios
redlining % % econométric
histórico os
independien
tes: 25-40%
del
diferencial
atribuible al
HOLC.
Crisis 2008 Economía ~22 ~6% ✓ 0.82 ≈0 Resolución
— MBS % regulatoria: 5
nodos de

Axiomatización del Sistema de la Doble Mediación
diseño
documentad
os con R*
colectivo
>80%.
Enron — Gov. corp. 35% ~3% ✓ 0.82 0.02 Sentencia
fraude federal:
contable Skilling
como
diseñador de
SPE
verificado
judicialment
e.
Triangle Seguros ~45 ~5% ✓ 0.22 ≈0 Resolución
Shirtwaist % judicial y
estudios
laborales:
propietarios
diseñaron
condiciones
inseguras.
Challenger Ingeniería ~28 ~2% ✓ 0.85 ≈0 Informe
— NASA % + Rogers:
presión
política
como nodo
D,
ingenieros
como
ejecutores. S
alto por
lógica de
grafo.
Boeing 737 Ingeniería ~32 ~18 ✓ 0.80 ≈0 Investigació
MAX — % % n FAA:
MCAS dirección
Boeing
diseñó
incentivos;
ingenieros
sustituibles
bajo esas
restricciones
.
WWI — Historia ~42 ~1% ✓ 0.92 0 Historiografí
Franz % a
Ferdinand estructuralist
a: S_asesino
= 0.92 →
cualquier
incidente
habría

Axiomatización del Sistema de la Doble Mediación
detonado el
sistema.
Iraq — Historia ~35 ~12 ✓ 0.70 ≈0 Informe
inteligenci % % Chilcot y
a Comisión
Senatorial:
proceso de
inteligencia
diseñado
por la
administraci
ón.
Educación Educación ~55 ~2.4 ✓ 0.78 ≈0 Estudios
— fracaso % % econométric
escolar os: entorno
familiar
explica 50-
70%;
docentes
como
ejecutores S
= 0.78.
Los 18 casos verifican la Condición (1) por al menos uno de
los cinco mecanismos identificados. La tasa de verificación del
100% en una muestra de 9 dominios distintos es evidencia de
que, en los sistemas institucionales complejos donde el TIC
tiene aplicación práctica, R*(D) > R*(E) es la norma
documentable, no la excepción.
B.2.3. Los cinco mecanismos de verificación
independiente
Mecanismo 1 — Jerarquía estructural. Casos:
Holocausto, Congo, Trata transatlántica, Triangle
Shirtwaist. La jerarquía del sistema —documentada
históricamente— establece que el nodo D tenía
mayor influencia causal que los ejecutores sin
necesidad de calcular el eigenvector.
Mecanismo 2 — Resolución judicial o
regulatoria. Casos: Enron, Boeing MCAS, Crisis
2008, Panama Papers. Existen resoluciones que
identifican al nodo D como el actor causalmente

Axiomatización del Sistema de la Doble Mediación
relevante. El tribunal establece la condición antes de
que el sistema la use.
Mecanismo 3 — Estudios econométricos o
epidemiológicos. Casos: HOLC redlining,
COVID-19, Cólera Soho. Estudios independientes
estiman la fracción causal de los nodos estructurales
antes de que el sistema de imputación causal sea
aplicado.
Mecanismo 4 — Lógica del grafo sin eigenvector.
Casos: WWI, Iraq, Educación. La estructura del grafo
—nodo D con m aristas salientes hacia nodos activos,
nodo E con una sola arista hacia Nf— implica R*(D)
> R*(E) por la definición de la distribución
estacionaria.
Mecanismo 5 — Cota S(E) vía Lema 8.1. Casos:
COMPAS, Gerente bancario. Cuando S_est(E) es
alto, el Lema 8.1 establece R*(E) ≤ (1−S_est)/(m−1)
directamente desde el valor de S —estimable sin el
grafo completo. La cota implica R*(D) > R*(E) sin
calcular el eigenvector.
B.2.4. Clasificación de los 18 casos por nivel de
evidencia
Los cinco mecanismos de verificación no tienen la misma
fuerza probatoria. Una resolución judicial establece la
Condición (1) con evidencia de máxima fuerza; la lógica del
grafo sin eigenvector la sugiere con fuerza moderada. La
siguiente tabla clasifica los 18 casos en tres niveles para que el
lector pueda ponderar la evidencia de forma diferenciada.
Nivel Descripción Fuerza Casos
probatori
a
A — La Condición (1) está Alta. Una Holocausto
Establecid fijada por una fuente fuente (jerarquía
a externa al sistema: externa al NSDAP
resolución judicial firme, sistema documentada

Axiomatización del Sistema de la Doble Mediación
sentencia regulatoria con establece por
hallazgos de causalidad, R*(D) > Nüremberg),
o estudio R*(E) con Enron
econométrico/epidemiol metodolog (sentencia
ógico con estimación ía propia. federal), Crisis
cuantitativa 2008 (resolución
independiente. regulatoria +
estudios
econométricos),
HOLC redlining
(estudios
econométricos
independientes),
COVID-19
(epidemiología
de
superpropagado
res), Cólera
Soho (Snow
1854), Panama
Papers
(investigación
judicial
internacional),
WWI
(historiografía
estructuralista
independiente),
Iraq (Informe
Chilcot +
Comisión
Senatorial) [9 de
18]
B — La Condición (1) está Moderada. Congo-
Corrobora corroborada por la La Leopoldo II
da estructura del sistema: estructura (decreto real +
jerarquía organizacional del sistema de
documentada en el sistema concesiones
expediente o norma legal implica documentado),
que establece posiciones R*(D) > Trata
causales, más el análisis R*(E); la transatlántica
del grafo que confirma la implicació (tratados
implicación. n es históricos),
transparen Triangle
te pero Shirtwaist
requiere el (investigación
análisis del policial +
grafo reformas

Axiomatización del Sistema de la Doble Mediación
como laborales
paso posteriores),
intermedio Boeing MCAS
. (investigación
FAA),
Challenger
(Informe
Rogers),
Educación
(estudios de
economía de la
educación) [6
de 18]
C — La Condición (1) se Formal. El COMPAS
Derivada deriva formalmente por resultado (S_COMPAS =
la cota del Lema 8.1 es una 0.97 → cota
desde el valor de S(E), consecuen directa), Gerente
sin acceso al grafo cia bancario caso
completo. La cota matemátic activo (S_est =
garantiza R*(E) ≤ a del valor 0.90 → cota
(1−S_est)/(m−1) << de directa), Anna
R*(D) > 1/m. S_est(E); O. (lógica del
depende grafo por
de la estructura
calidad de temporal),
la Panama Papers
estimación BCCI (lógica del
de S. grafo por niveles
de diseño) [4 de
18, algunos con
soporte de Nivel
B también]
Los 9 casos de Nivel A son suficientes por sí solos para
sostener el argumento de que la Condición (1) es verificable
de forma independiente al TIC en sistemas institucionales
complejos. Los 15 casos de Nivel A+B consolidan ese
argumento con fuerza estructural. Los 3 casos adicionales de
Nivel C lo completan mediante la formalización matemática
del Lema 8.1. La heterogeneidad de los mecanismos es una
fortaleza, no una debilidad: ninguno de los tres niveles
depende de los otros para establecer la Condición (1) en sus
casos respectivos.

Axiomatización del Sistema de la Doble Mediación
La distinción entre niveles no afecta a la verificación de la Condición (1): en
todos los casos, la condición se verifica de forma independiente al TIC. La
distinción sirve para que el analista calibre el nivel de certeza con que puede
invocar el TIC en cada caso concreto. Un análisis basado en casos de Nivel
A tiene mayor respaldo que uno basado exclusivamente en casos de Nivel C.

Axiomatización del Sistema de la Doble Mediación

## Apéndice C

## Glosario de traducción formal

Este apéndice permite usar el sistema formal de este libro sin
conocer los doce volúmenes de ontología de la colección, y
permite al lector de la ontología localizar los equivalentes
matemáticos de los términos que conoce. El glosario opera en
ambas direcciones. La primera columna contiene el término
ontológico; la segunda, su equivalente formal con referencia
de parte; la tercera, la definición operativa.
Los seis modos k = 1,…,6 tienen fondo lavanda para
identificarlos visualmente. Son los únicos objetos del libro
donde la correspondencia ontológica —los Hijos de
Afrodita— tiene contenido que no se reduce al marco formal:
el marco formal describe qué hace cada modo (el perfil
conductual, el rango de S); la ontología describe por qué cada
modo tiene esa estructura. Ambas descripciones son
independientes y consistentes.
Término Equivalente Definición operativa
ontológico formal
Caos E (espacio de El espacio de posibilidad absoluta
Hilbert, Axioma anterior a toda determinación. E es
0) completo (ninguna posibilidad
ausente), separable (computable) y sin
elemento privilegiado antes de que φ(cid:0)
opere. Ver nota ontológica al final de
la Parte 0.
Ego I(t) (cid:0) E La integral acumulativa de colapsos
(Definición 2) hasta t. No es una entidad metafísica:
es un estado computable en E. E_i(t)
del SDO = I(t) con la notación de la
Definición 2.

Axiomatización del Sistema de la Doble Mediación
Colapso c(τ) (cid:0) E El valor de la función de colapso en τ:
(Definición 0) el output del sistema mapeado a E
mediante emb. Selección de un
elemento de E en τ — determinación
de una posibilidad del Caos.
Voluntad v_t (cid:0) V El estado interno del sistema antes de
(Definición 1) producir el colapso en t. Incluye τ, a_t
y referencia a I(t).
Primera φ(cid:0) : V×C×H La función que produce el colapso.
mediación → A (Axioma 1) Depende de la voluntad, el campo y la
historia.
Segunda φ(cid:0) : A×E → E La función que retorna el colapso al
mediación (Axioma 2) sistema. Evalúa mediante eval, decide
integrar o rechazar, actualiza I(t).
Historia / I(t) = ∫(cid:0)ᵗ Integral de Bochner que acumula los
Integral del c(τ)w(τ)dτ colapsos integrados ponderados por
ego (Definición 2) w(τ). Irreversible (Teorema 2.1).
Principios Núcleo de I(t), Los colapsos de mayor peso en I(t),
constitutivos umbral θ en eval que determinan el umbral de eval.
Capturado en la función eval del
Teorema 2.2.
Campo de c (cid:0) C, (cid:0)c(cid:0)_C Dos usos. C en el Axioma 1:
acción (Axioma 1) / configuración heredada estructural.
C(t) (cid:0) E C(t) en Ψ(t): conjunto de outputs
(Definición 9) posibles en t.
Hijos de K = {1,…,6} Los seis índices de modo de la
Afrodita (Lema 1.1) distribución softmax. Cada k (cid:0) K
(categoría) tiene un vector β_k (cid:0) E, un peso γ_k
(cid:0) (cid:0) y un umbral θ_k.
k = 1 (Fobos) k = 1; S_op (cid:0) Presión sistémica de consecuencias.
[0.70, 0.95] h(cid:0)(v_t) alta cuando el output está
determinado por consecuencias
documentadas de no producirlo.
k = 2 k = 2; S_op (cid:0) Parálisis estructural. h(cid:0)(v_t) alta
(Deimos) [0.72, 0.95] cuando la omisión es la única
respuesta consistente con el campo.
k = 3 (Potós) k = 3; S_op (cid:0) Inercia y costumbre. h(cid:0)(v_t) alta
[0.30, 0.70] cuando el sistema reproduce el patrón
previo sin verificar cambios.
k = 4 (Eros) k = 4; S_op (cid:0) Apertura e impulso. h(cid:0)(v_t) alta
[0.30, 0.70] cuando el sistema genera outputs

Axiomatización del Sistema de la Doble Mediación
divergentes del patrón por motivación
interna.
k = 5 k = 5; S_op (cid:0) Afirmación idiosincrática. h(cid:0)(v_t) alta
(Anteros) [0.08, 0.30] cuando el output se aparta del campo
por decisión documentablemente
propia.
k = 6 k = 6; S_op: Integración completa. h(cid:0)(v_t) alta
(Harmonía) variable cuando I(t) y v_t son coherentes. S no
determinable desde evidencia
documental.
Imputación R* (cid:0) Δⁿ Eigenvector dominante de Wᵀ
causal (Definición 6.1) normalizado. R*ᵢ = fracción de la
influencia causal del resultado que
transita por el nodo i.
Asunción α(t) (cid:0) [0,1] Proporción de RSC(t) integrada en I(t)
(Definición 4) con profundidad verificable. Mide
acciones posteriores, no intenciones
durante el evento.
Inversión Δ(D) > 0 ∧ El diseñador causó más de lo que
causal Δ(E) < 0 asumió y el ejecutor asumió más de lo
(Teoremas 8.1– que causó. Demostrado bajo las
8.2) Condiciones (1)–(3) del TIC.
Fraude Def. 8.7: Inversión extrema: S(E) alto, α(E) >
annona (a)+(b)+(c) R*(E), α(D) ≈ 0. Firma: Δ_inst ≈
R*(D). Detectable desde el expediente.
Principio de REC — Nombre revisado. 'Principio de
incertidumbre Relación de incertidumbre' sugería cota absoluta
ontológica Escala del como Heisenberg. La REC es una
(nombre Conocimiento cota de escala que decrece con n. Ver
original) (Teorema 7) sección 7.4.
Temperatura τ > 0 (Axioma El ruido irreducible de la voluntad.
ontológica 3) Parámetro de temperatura de la
softmax. Observable en sistemas
artificiales; estimado estadísticamente
en humanos.
Clausura del (cid:0) = Im(c) ∪ El conjunto de todos los colapsos
ego {I(t(cid:0))} producidos más la integral final.
(Teorema 10) Cerrado en (E, (cid:0)·(cid:0)_E). Perfecto
cuando c es continua.
ECO Protocolo de Entrevista Clínica Ontológica. En el
estimación de marco formal: procedimiento para
I(t) y v_t estimar v_t e I(t) cuando la evidencia
documental es insuficiente. Necesario

Axiomatización del Sistema de la Doble Mediación
para k = 6 y para E(t) cuando no es
observable.
SDO Instrumento de Sistema de Diagnóstico Ontológico.
diagnóstico de En el marco formal: el instrumento
E(t) que mapea evidencia observable al
nivel de integración E(t) (cid:0) {1,…,6}
de la Definición 9.
Caos — E antes de c : T La estructura de Hilbert de E captura
posibilidad → E (nota final esto: E es completo (ninguna
absoluta Parte 0) posibilidad ausente), separable
(posibilidades computables), sin
elemento privilegiado antes del primer
colapso c(0).

Axiomatización del Sistema de la Doble Mediación
AXIOMATIZACIÓN DEL SISTEMA DE LA DOBLE MEDIACIÓN

## Apéndice D

Extensiones del marco formal
Este apéndice extiende el marco de las Partes 0–X en tres
direcciones que el núcleo formal dejó como trabajo pendiente:
la formalización de la trayectoria causal discreta, la derivación
de una función de imputación neta sin doble conteo y las
condiciones de identificabilidad del sistema, y la definición de
un operador contrafactual general que generaliza S_est. Las
tres extensiones son compatibles con todos los resultados de
las Partes 0–X y los Apéndices A–C; no los modifican.
Las tres secciones de este apéndice tienen distinto estatus. D.1 es una
extensión formal directa: sus resultados se siguen de los Fundamentos con
herramientas estándar. D.2 contiene resultados formales más una declaración
de condiciones de identificabilidad que tiene carácter de protocolo, no de
teorema. D.3 es una extensión formal que abre un programa de investigación;
sus aplicaciones concretas son trabajo futuro.
D.1. Trayectoria causal discreta
El marco de las Partes 0–X define I(t) como una integral de
Bochner continua sobre T = [0, t_m]. La Definición 4.1 (Parte
IV) introduce los colapsos discretos mediante w(τ) = Σᵢ
δ(τ−τᵢ), pero no formaliza la dependencia entre colapsos
consecutivos: el colapso c(τ(cid:0)) puede depender de I(τₖ ₋ ₁ ⁺ ),
lo que convierte la secuencia en un proceso dinámico
encadenado. Esta sección formaliza esa dependencia.

Axiomatización del Sistema de la Doble Mediación
Definición D.1. Refinamiento discreto T_d
Sea T_d = {τ(cid:0) < τ(cid:0) < … < τ(cid:0)} (cid:0) T un conjunto finito de
instantes de colapso. T_d es un refinamiento discreto de T si
τ(cid:0) > 0 y τ(cid:0) ≤ t_m. La función de colapso restringida a T_d
es la sucesión c_d = (c(τ(cid:0)), …, c(τ(cid:0))) con c(τ(cid:0)) (cid:0) E para
todo k.
La integral acumulativa discreta hasta el k-ésimo colapso es:
Integral acumulativa discreta
I_d(k) = Σᵢ(cid:0)(cid:0)ᵏ c(τᵢ) · w(τᵢ)
w(τᵢ) (cid:0) ℝ₊ peso del colapso en τᵢ · I_d(k) (cid:0) E para todo k · I_d(0) = 0 (cid:0)
E
Definición D.2. Trayectoria causal discreta con
dependencia
La sucesión c_d es una trayectoria causal discreta si existe una
familia de funciones medibles {f(cid:0)}(cid:0)(cid:0)(cid:0)ⁿ tal que:
Condición de dependencia causal
c(τₖ ) = fₖ (I_d(k−1), v_{τ(cid:0)}, C(τ(cid:0)))
I_d(k−1) ∈ E historia acumulada hasta el colapso anterior · v_{τ(cid:0)} (cid:0) V
estado interno en τ(cid:0) · C(τ(cid:0)) (cid:0) E campo de acción disponible
La condición de dependencia establece que cada colapso está
determinado por: (i) la historia integrada hasta ese instante, (ii)
el estado interno del sistema en ese instante, y (iii) el campo de
acción disponible. El colapso en τ(cid:0) no depende directamente
de los colapsos individuales anteriores c(τ(cid:0)),…,c(τₖ ₋ ₁ ),
sino solo de su acumulación I_d(k−1). Esta es la propiedad de
Markov de orden 1 en E.
Teorema D.1. Propiedad de Markov de la
trayectoria discreta

Axiomatización del Sistema de la Doble Mediación
Sea c_d una trayectoria causal discreta en el sentido de la
Definición D.2. Entonces la sucesión (I_d(k))(cid:0)(cid:0)(cid:0)ⁿ es un
proceso de Markov de orden 1 en (E, (cid:0)·(cid:0)_E): para todo k ≥
1 y todo conjunto medible B (cid:0) E,
Propiedad de Markov
P(I_d(k) (cid:0) B | I_d(k−1), I_d(k−2), …, I_d(0)) =
P(I_d(k) (cid:0) B | I_d(k−1))
Demostración del Teorema D.1
Paso 1. Por la Definición D.2: c(τₖ ) = fₖ (I_d(k−1),
v_{τ(cid:0)}, C(τ(cid:0))). La función f(cid:0) depende de la historia
solo a través de I_d(k−1).
Paso 2. I_d(k) = I_d(k−1) + c(τ(cid:0))·w(τ(cid:0)) =
I_d(k−1) + fₖ (I_d(k−1), v_{τ(cid:0)}, C(τ(cid:0)))·w(τ(cid:0)).
Luego I_d(k) está completamente determinado por
I_d(k−1) y las variables (v_{τ(cid:0)}, C(τ(cid:0))), que son
independientes de I_d(k−2),…,I_d(0) dado I_d(k−1).
Paso 3. Por tanto P(I_d(k) (cid:0) B | I_d(k−1), …,
I_d(0)) = P(I_d(k) (cid:0) B | I_d(k−1)). ✓
(I_d(k))(cid:0) es un proceso de Markov de orden 1 en E. (cid:0)
Proposición D.1. Convergencia al caso continuo
Sea {T_d^(n)}(cid:0) una sucesión de refinamientos discretos con
malla max_k(τₖ ₊ ₁ − τₖ ) → 0 cuando n → ∞. Si c : T → E
es continua y w es continua y acotada:
Convergencia al caso continuo
(cid:0)I_d^(n)(k_n) − I(t)‖ _E → 0 cuando τ_{k_n} → t
I_d^(n)(k_n) suma de Riemann-Bochner · I(t) integral de Bochner de la Parte
II · convergencia en norma de E
Demostración de la Proposición D.1
I_d^(n)(k_n) = Σᵢ c(τᵢ)w(τᵢ)(τᵢ₊ (cid:0)−τᵢ) es una suma de
Riemann-Bochner para ∫(cid:0)ᵗ c(τ)w(τ)dτ. Por la teoría de

Axiomatización del Sistema de la Doble Mediación
integración de Bochner, para c continua y w continua
acotada, las sumas de Riemann-Bochner convergen
en norma a la integral de Bochner cuando la malla
tiende a cero. Luego (cid:0)I_d^(n)(k_n) − I(t)‖ _E → 0.
(cid:0)
La trayectoria discreta es una discretización consistente del proceso continuo de las
Partes I–II. (cid:0)
Consecuencia para el análisis de responsabilidad.
Cuando el expediente solo contiene evidencia de n colapsos
discretos en momentos {τ(cid:0),…,τ(cid:0)}, la trayectoria causal
discreta proporciona el marco correcto. El vector R* del grafo
G captura la distribución de responsabilidad sobre la
trayectoria completa; I_d(n) es la integral que acumula los
efectos de esa trayectoria. El Teorema D.1 garantiza que la
dependencia entre colapsos está formalmente capturada por la
condición de Markov en E.
La condición de Markov en E no implica independencia entre colapsos: c(τ(cid:0))
puede depender fuertemente de c(τₖ₋₁) a través de I_d(k−1). Lo que
excluye es la dependencia en colapsos individuales anteriores más allá de su
integral acumulada. En sistemas con memoria de largo alcance —donde
c(τ(cid:0)) depende de la forma de toda la trayectoria, no solo de I_d(k−1)— la
condición de Markov no aplica y se requiere un proceso de Markov de orden
superior o un proceso en el espacio de funciones.
D.2. Función de imputación neta y condiciones
de identificabilidad
El Defícit Δ(i) = R*(i) − α(i) de la Parte V mide la brecha total
entre lo que el nodo causó y lo que asumió. Una función de
imputación neta debe distinguir además la fracción de R*(i)
que es estructural —la que cualquier nodo en esa posición
habría tenido— de la fracción genuinamente idiosincrática.
Esta sección deriva esa función sin incurrir en doble conteo
entre R* y S_est.
Definición D.3. Descomposición de R* en
componente estructural y neta

Axiomatización del Sistema de la Doble Mediación
Sea R*^(i) el eigenvector dominante del grafo de sustitución
W^(i) (Definición 3.2, Parte III). La componente estructural
de R*(i) es:
Componentes de R*(i)
R*_struct(i) = R*^(i)_i (responsabilidad que cualquier
nodo en posición i tendría)
R*_net(i) = R*(i) − R*_struct(i) (exceso idiosincrático
sobre la línea base estructural)
R*_struct(i) = R*^(i)_i es la i-ésima componente del eigenvector del grafo de
sustitución · R*_net(i) ≥ 0 por la cota del Lema 8.1
Ausencia de doble conteo. La descomposición R* =
R*_struct + R*_net no usa S_est en su definición: R*_struct
se obtiene directamente del eigenvector del grafo W^(i), que
es un objeto del grafo causal. S_est es una función de R* y
R*^(i), no al revés. Usar R*_net = R*(i) − R*^(i)_i evita la
circularidad de multiplicar R* por (1−S_est), que combina dos
objetos derivados del mismo eigenvector.
Por el Lema 8.1 (Apéndice A): R*_net(i) = R*(i) − R*^(i)_i ≤
(1−S_est(i))/(m−1). La cota del Lema 8.1 es una cota superior de
R*_net, no una definición de R*_net. La definición correcta de R*_net es
la diferencia de eigenvectores; la cota del Lema 8.1 la conecta con S_est.
Definición D.4. Función de imputación neta
Δ_net
La función de imputación neta del nodo i es:
Función de imputación neta
Δ_net(i) = R*_net(i) − α_vol(i)
R*_net(i) = R*(i) − R*^(i)_i componente idiosincrática
de la responsabilidad causal
α_vol(i) = asunción voluntaria del nodo i (componente de
la Definición 8.5)
Δ_net(i) (cid:0) [−1, 1] · mide la brecha neta entre contribución causal
idiosincrática y asunción voluntaria

Axiomatización del Sistema de la Doble Mediación
Se usa α_vol y no α completo porque la asunción forzada
α_for y la asunción impuesta α_imp responden a la visibilidad
V(i) y al sistema convencional de imputación —no a la
causalidad idiosincrática del nodo. Incluir α_for y α_imp en el
denominador mezclaría dos mecanismos distintos: la
causalidad neta y la respuesta del sistema de imputación a esa
causalidad.
Relación con Δ. Δ(i) = R*(i) − α(i) y Δ_net(i) = R*_net(i) −
α_vol(i) son distintos objetos que miden aspectos distintos.
Δ(i) es la brecha total observable; Δ_net(i) es la brecha neta
idiosincrática. En sistemas con alta sustituibilidad S_est(i) →
1: R*_struct(i) ≈ R*(i), luego R*_net(i) ≈ 0, luego Δ_net(i) ≈
−α_vol(i) ≤ 0 —el nodo sustituible no tiene brecha neta
positiva, aunque tenga Δ(i) > 0. Eso es exactamente la
descripción formal del ejecutor en el TIC.
Proposición D.2. Condiciones de
identificabilidad del sistema
El sistema (R*, S_est, α, Δ, Δ_net) es identificable desde datos
observables cuando se satisfacen las siguientes condiciones:
(I-1) Completitud del grafo. G contiene todos los
nodos causalmente necesarios: para todo nodo j con
R*_j > 0, j (cid:0) N. Esta es la misma condición de la
Proposición 5.2 (Parte V).
(I-2) Estimabilidad de los pesos. Para toda arista
(i, j) (cid:0) A: w (i, j) es estimable con nivel de certeza ≥
B en la escala E0–E8 de Metrología Causal. Bajo (I-
2), el intervalo [R*(min), R*(max)] del Lema 6.1 tiene
anchura ≤ 0.10.
(I-3) Observabilidad de S_est. S_est(i) es
observable por dos rutas: (a) directamente, si G está
disponible: S_est(i) = 1 − D_KL(R* ‖
R*^(i))/log(m) desde el cómputo del eigenvector; (b)
indirectamente, si G no está disponible: S_est(i) ≈
g(S_op(i)) por la Proposición 3.3, donde S_op(i) =
(cid:0)c(cid:0)_C/((cid:0)c(cid:0)_C + (cid:0)a_t(cid:0)_E) es computable desde
la escala E0–E8.

Axiomatización del Sistema de la Doble Mediación
(I-4) Observabilidad de α_vol. α_vol(i) es
observable desde el expediente cuando los
documentos distinguen entre asunción voluntaria
(pagos iniciados, reconocimiento público,
modificaciones sistémicas propias) y asunción forzada
o impuesta. Nivel de certeza ≥ B requerido.
Bajo las condiciones (I-1)–(I-4):
Proposición D.2 — identificabilidad de Δ_net
R*(i). Identificable por el método de potencias
(Lema 6.1) con intervalo [R*(min), R*(max)] de
anchura ≤ 0.10 bajo (I-2).
R*^(i)_i. Identificable aplicando el método de
potencias a W^(i) = W con fila i reemplazada por el
promedio. Requiere (I-1) e (I-2).
R*_net(i) = R*(i) − R*^(i)_i. Identificable como
diferencia de dos cantidades identificables. Intervalo
de incertidumbre propagado desde los intervalos de
R* y R*^(i) por la norma triangular.
α_vol(i). Observable directamente desde el
expediente bajo (I-4).
Δ_net(i). Identificable como diferencia de
cantidades identificables. ✓
Bajo (I-1)–(I-4), Δ_net(i) es identificable con intervalo de incertidumbre
[Δ_net(i)_min, Δ_net(i)_max] derivado de los intervalos de R*(i) y R*^(i)_i
por la desigualdad triangular. (cid:0)
Objeto Condición Ruta de Fuente de
mínima estimación incertidumbre
R*(i) (I-1) + (I-2) Método de Anchura de los
potencias sobre intervalos [a_ij,
Wᵀ b_ij]
R*^(i)_i (I-1) + (I-2) Método de Misma fuente;
potencias sobre correlacionada
(W^(i))ᵀ con R*(i)

Axiomatización del Sistema de la Doble Mediación
R*_net(i) (I-1) + (I-2) R*(i) − R*^(i)_i Suma de
incertidumbres
de R*(i) y
R*^(i)_i
S_est(i) (I-1) + (I-2) Ruta directa desde Incertidumbre
ó (I-3) D_KL ó ruta de D_KL ó de
indirecta desde ±0.10 en S_op
S_op
α_vol(i) (I-4) Expediente: Ambigüedad
documentos de documental
asunción entre tipos de α
voluntaria
Δ_net(i) (I-1)–(I-4) R*_net(i) − Propagación de
α_vol(i) incertidumbres
de R*_net y
α_vol
D.3. Operador contrafactual general
El índice de sustituibilidad S_est(i) responde a la pregunta:
¿cuánto cambia R* si se reemplaza la fila i de W por el
promedio de las demás? Esta es una instancia particular de un
contrafactual más general: ¿cuánto cambia R* si se reemplaza
cualquier fila de W por cualquier fila alternativa? Esta sección
define ese operador y deriva sus propiedades.
Definición D.5. Operador contrafactual   (G, i,
W'_i)
Sea G = (N, A, w) un grafo causal con matriz W y sea W'_i (cid:0)
(cid:0)^{1×m} una fila alternativa estocástica (Σ(cid:0) W'_{ij} = 1,
W'_{ij} ≥ 0). Sea G' el grafo obtenido reemplazando la fila i
de W por W'_i, con todas las demás filas iguales. El operador
contrafactual es:
Operador contrafactual
  (G, i, W'_i) = R*(G')

Axiomatización del Sistema de la Doble Mediación
R*(G') eigenvector dominante de (W’) ᵀ normalizado · W' coincide con W en
todas las filas excepto la i-ésima
  (G, i, W'_i) devuelve el vector de responsabilidad causal que
resultaría que el nodo i operara según W'_i en lugar de W_{i·}.
La comparación   (G, i, W'_i) con R*(G) cuantifica el impacto
causal de ese cambio.
S_est como caso especial. S_est(i) = 1 − D_KL(R*(G) (cid:0)
  (G, i, W(cid:0)_i)) /log(m) donde W(cid:0)_i = (1/(m−1)) Σ_{j≠i}
W_{j·} es la fila promedio. El operador (cid:0) con W(cid:0)_i como
fila alternativa produce el grafo de sustitución de la Definición
3.2. S_est es la divergencia KL normalizada entre R*(G) y  
(G, i, W(cid:0)_i).
Teorema D.2. Cota del impacto contrafactual —
Davis-Kahan generalizado
Para cualquier fila alternativa estocástica W'_i:
Cota del impacto contrafactual
(cid:0)  (G, i, W'_i) − R*(G)(cid:0)₁ ≤ (m/δ) · (cid:0)W'_i − W_{i·} ‖(cid:0)
δ = 1 − |λ(cid:0)| gap espectral de W · m = |N| número de nodos · la cota es la
misma que el Teorema A.4
Demostración del Teorema D.2
La perturbación E = W' − W tiene ‖ E‖ ₂ = ‖ W'_i
− W_{i·} ‖(cid:0) (la perturbación es no cero solo en la fila
i). Por el Teorema A.4 (Apéndice A): (cid:0)R*(G') −
R*(G)(cid:0)(cid:0) ≤ (m/δ) ·(cid:0)E(cid:0)(cid:0) = (m/δ) ·(cid:0)W'_i −
W_{i·} ‖(cid:0). (cid:0)
La cota es la misma que el Teorema A.4. El operador (cid:0) hereda directamente la
estabilidad de Davis-Kahan. (cid:0)
Definición D.6. Métrica de impacto causal V (G,
G')

Axiomatización del Sistema de la Doble Mediación
La métrica de impacto causal de un cambio de grafo G → G'
es:
Métrica de impacto causal
  (G, G’) = ‖R*(G') − R*(G)(cid:0)₁ = ‖  (G, i, W'_i) −
R*(G)(cid:0)(cid:0)
(cid:0) ≥ 0 · (cid:0) = 0 (cid:0) R*(G') = R*(G) · acotada superiormente por el Teorema
D.2
  (G, G') mide cuánto cambia la distribución de
responsabilidad causal cuando el nodo i opera según W'_i en
lugar de W_{i·}. Cuanto mayor es (cid:0), más causal es el cambio
en la posición de i.
Aplicaciones del operador contrafactual
Cambio de dataset. W'_i se obtiene reasignando los
pesos de la fila i según un dataset alternativo —sin
sesgo, corregido, de otro período.   (G, i, W'_i)
calcula cómo se redistribuiría R* si el dataset hubiera
sido el alternativo.   (G, G') cuantifica el impacto
causal del sesgo del dataset original.
Cambio de regla o protocolo. W'_i representa la
fila del nodo diseñador bajo un protocolo distinto —
sin la restricción de costos que produjo el diseño
defectuoso.   (G, i, W'_i) responde: ¿cómo se habría
distribuido R* bajo el protocolo alternativo?
Cambio de decisión de despliegue. W'_i
representa la fila del desplegador bajo una política de
restricción distinta.   (G, G') cuantifica si el
despliegue fue la decisión causal determinante o si el
sistema habría producido el mismo resultado bajo
cualquier política de despliegue razonable.
Auditoría de intervenciones. Para un conjunto de
intervenciones posibles {W'_i^ (1), …, W'_i^(k)},
ordenar por   (G, G'^(j)) identifica la intervención
con mayor impacto causal sobre R*. Esto convierte el
operador (cid:0) en un instrumento de priorización de
recursos correctivos.

Axiomatización del Sistema de la Doble Mediación
Corolario D.3. Acotación del contrafactual neto
El cambio en la componente neta R*_net(i) bajo el operador
contrafactual satisface:
Cambio en R*_net bajo contrafactual
|R*_net^{W’} (i) − R*_net(i)| ≤ (m/δ) · (cid:0)W'_i −
W_{i·} ‖₂ + |R*^(i)_i^{W'} − R*^(i)_i|
El segundo término es la variación en la línea base estructural bajo el cambio de
política · acotado también por (m/δ) ·(cid:0)W'_i − W_{i·} ‖(cid:0)
Demostración del Corolario D.3
R*_net^{W’} (i) =   (G, i, W'_i) _i − (cid:0)^(i) (G, i,
W'_i) _i, donde (cid:0)^(i) es el operador sobre el grafo de
sustitución de i. Por desigualdad triangular y el
Teorema D.2 aplicado a ambos términos:
|R*_net^{W’} (i) − R*_net(i)| ≤ 2·(m/δ) ·(cid:0)W'_i −
W_{i·} ‖(cid:0). (cid:0)
El cambio en la imputación neta está doblemente acotado por la magnitud del
cambio de política. Intervenciones pequeñas ((cid:0)W'_i − W_{i·} ‖(cid:0) (cid:0) 1)
producen cambios pequeños en Δ_net. (cid:0)
El Corolario D.3 tiene consecuencias prácticas: si se quiere reducir
Δ_net(D) — la brecha neta del diseñador — la intervención más eficiente
no es sobre la visibilidad V(D), sino sobre la fila W_{D·} de la matriz de
pesos del diseñador: cambiar sus incentivos, sus protocolos o sus restricciones
modifica directamente su R*_net sin depender del sistema de imputación
convencional.
Objeto Notación Tipo Sección
matemático
Refinamiento T_d = {τ(cid:0) < … < Subconjunto Definició
discreto τ(cid:0)} finito de T n D.1
Integral I_d(k) = Σᵢ c(τᵢ)w(τᵢ) Suma en E Definició
discreta n D.1

Axiomatización del Sistema de la Doble Mediación
Trayectoria c(τₖ ) = fₖ (I_d(k−1), Proceso Definició
con v_{τ(cid:0)}, C(τ(cid:0))) Markov-1 en E n D.2
dependencia
Markov en E Teorema D.1 P(I_d(k)|I_d(k Teorema
−1)) = D.1
P(I_d(k)|toda la
historia)
Convergencia (cid:0)I_d^(n) − I(t)‖ _E Consistencia de Proposici
al caso → 0 la discretización ón D.1
continuo
R*_struct(i) R*^(i)_i Componente Definició
estructural del n D.3
eigenvector
R*_net(i) R*(i) − R*^(i)_i Exceso Definició
idiosincrático; ≤ n D.3
(1−S_est)/(m−
1)
Δ_net(i) R*_net(i) − α_vol(i) Escalar en Definició
[−1,1]; sin doble n D.4
conteo
Identificabili Proposición D.2 Bajo (I-1)–(I-4); Proposici
dad intervalo de ón D.2
incertidumbre
trazable
Operador (cid:0)(G, i, W'_i) = Función de Definició
contrafactual R*(G') grafos a Δⁿ n D.5
Métrica de (cid:0)(G,G') = Escalar ≥ 0; Definició
impacto (cid:0)R*(G')−R*(G)‖ ₁ acotado por n D.6
Davis-Kahan
Cota (cid:0)(cid:0)−R*(cid:0)(cid:0) ≤ Desigualdad; Teorema
contrafactual (m/δ)(cid:0)W'_i−W_{i· hereda Teorema D.2
}(cid:0)(cid:0) A.4
Δ_net bajo Corolario D.3 Cambio acotado Corolario
contrafactual por la magnitud D.3
de la
intervención

Axiomatización del Sistema de la Doble Mediación
D.4. Dinámica de imputación: dominancia,
estabilidad y bifurcación
Las Secciones D.1–D.3 formalizan la trayectoria discreta, la
función de imputación neta y el operador contrafactual. Esta
sección completa el cuadro dinámico con tres resultados: el
Teorema de Dominancia —que identifica el nodo de mayor
imputación efectiva—, el Teorema de Estabilidad —que
caracteriza trayectorias robustas y frágiles— y la Definición de
nodo de bifurcación causal, que formaliza los puntos donde
modificar una decisión altera el espacio de estados accesibles.
Los tres resultados usan Δ_net de la Definición D.4 como
operador de imputación, evitando el doble conteo que
produce la función R*(i)·(1−S) ·(1−α) cuando S_est se deriva
de R*.
La función I_i = R*(i)·(1−S_i) ·(1−α_i) usada en algunas presentaciones
externas del sistema combina dos objetos que comparten la misma fuente:
R*(i) captura la posición estructural del nodo en el grafo, y S_est(i) mide esa
misma posición desde la perspectiva del eigenvector de sustitución.
Multiplicarlos suprime la idiosincrasia causal del nodo dos veces. Los
resultados de esta sección usan en su lugar Δ_net(i) = R*_net(i) − α_vol(i),
que separa la componente idiosincrática de la línea base estructural antes de
aplicar cualquier operador.
Teorema D.3. Dominancia de imputación neta
Sea T_d = {τ(cid:0),…,τ(cid:0)} una trayectoria causal discreta. Si existe
un nodo k* (cid:0) {1,…,n} tal que:
(i) R*_net(k*) ≥ R*_net(i) para todo i — mayor
componente idiosincrática de responsabilidad causal.
(ii) α_vol(k*) ≤ α_vol(i) para todo i — menor
asunción voluntaria.
entonces Δ_net(k*) ≥ Δ_net(i) para todo i. El nodo k* domina
la imputación neta de la trayectoria.
Dominancia de imputación neta
R*_net(k*) ≥ R*_net(i) ∧ α_vol(k*) ≤ α_vol(i) ⟹
Δ_net(k*) ≥ Δ_net(i) ∀ i

Axiomatización del Sistema de la Doble Mediación
k* es el nodo dominante · la dominancia es de orden parcial: puede no existir un
único k* cuando las condiciones (i)–(ii) no se satisfacen simultáneamente
Demostración del Teorema D.3
Δ_net(i) = R*_net(i) − α_vol(i). Por las condiciones
(i) y (ii): R*_net(k*) − α_vol(k*) ≥ R*_net(i) −
α_vol(i) para todo i. Luego Δ_net(k*) ≥ Δ_net(i). (cid:0)
La demostración es directa desde la Definición D.4. La potencia del resultado no
es algebraica sino interpretativa: k* es el nodo que simultáneamente causó más
(en exceso sobre la línea base estructural) y asumió menos voluntariamente. (cid:0)
El Teorema D.3 tiene tres corolarios que traducen condiciones
estructurales en imputación neta:
Corolario D.4.1 — Sustituibilidad anula
imputación neta. Si S_est(i) → 1, entonces
R*_net(i) = R*(i) − R*^(i)_i → 0 por el Lema 8.1.
Luego Δ_net(i) → −α_vol(i) ≤ 0. Un nodo altamente
sustituible no tiene imputación neta positiva
independientemente de su posición en el grafo. Este
resultado ya estaba implícito en la cadena Davis-
Kahan del Apéndice A; el Teorema D.3 lo posiciona
en el marco dinámico.
Corolario D.4.2 — Migración de imputación. Si
R*_net(a) ≈ R*_net(b) pero α_vol(a) > α_vol(b),
entonces Δ_net(b) > Δ_net(a). La imputación neta
migra hacia el nodo que menos asumió
voluntariamente, no necesariamente hacia el de mayor
responsabilidad causal bruta.
Corolario D.4.3 — Asunción anula imputación.
Si α_vol(i) → R*_net(i), entonces Δ_net(i) → 0. La
asunción voluntaria proporcional a la responsabilidad
causal idiosincrática cancela la brecha neta. El nodo
sigue en el grafo causal con R*(i) > 0, pero su
imputación neta desaparece.
Teorema D.4. Estabilidad e inestabilidad de la
trayectoria causal

Axiomatización del Sistema de la Doble Mediación
Sea T_d una trayectoria causal discreta con imputación neta
agregada Δ_net_total = Σᵢ Δ_net(i). La trayectoria es:
Condiciones de estabilidad e inestabilidad
Estable: si ∀i, S_est(i) → 1 o α_vol(i) → R*_net(i)
Frágil: si (cid:0)k tal que S_est(k) << 1 y α_vol(k) <<
R*_net(k)
Dominada: si (cid:0)k tal que Δ_net(k) >> Δ_net(i) para todo
i ≠ k
Estable: pequeñas perturbaciones en decisiones producen cambio pequeño en
Δ_net_total · Frágil: el nodo k es crítico — el Teorema D.5 lo formaliza ·
Dominada: un nodo concentra la brecha
Demostración del Teorema D.4
Estabilidad. Si S_est(i) → 1 para todo i: R*_net(i)
→ 0 para todo i (Corolario D.4.1), luego Δ_net_total
→ −Σ α_vol(i) ≤ 0. Perturbaciones en decisiones
individuales que no alteran S_est significativamente
producen cambio pequeño en Δ_net_total. ✓
Fragilidad. Si existe k con S_est(k) << 1 y α_vol(k)
<< R*_net(k): Δ_net(k) > 0 y es el término
dominante de Δ_net_total. Una perturbación que
cambie R*_net(k) o α_vol(k) altera sustancialmente
Δ_net_total. La trayectoria es sensible a ese nodo. ✓
Dominancia. Si Δ_net(k) >> Δ_net(i) para todo i ≠
k: el nodo k concentra la brecha de imputación. La
trayectoria puede caracterizarse por ese único nodo
sin pérdida significativa de información sobre
Δ_net_total. ✓
La estabilidad de la trayectoria está determinada por la distribución de S_est y
α_vol entre los nodos, no por el número de nodos ni por la complejidad estructural
del grafo. (cid:0)
Definición D.7. Nodo de bifurcación causal
Un nodo i (cid:0) N es un nodo de bifurcación causal si existe una
fila alternativa W'_i tal que el soporte del operador
contrafactual cambia:

Axiomatización del Sistema de la Doble Mediación
Nodo de bifurcación causal
supp (  (G, i, W'_i)) ≠ supp(R*(G))
supp(v) = {k: v_k > 0} soporte del vector · la bifurcación ocurre cuando el
cambio en la fila i hace aparecer o desaparecer nodos con R* > 0
La bifurcación causal es cualitativamente distinta del cambio
cuantitativo: no es que R*(j) aumente o disminuya para algún
j, sino que j pasa de tener R*(j) = 0 a tener R*(j) > 0, o
viceversa. Un cambio cuantitativo está acotado por el
Teorema D.2; una bifurcación puede ocurrir incluso cuando
(cid:0)W'_i − W_{i·} ‖(cid:0) es pequeño, si la fila alternativa conecta
o desconecta el nodo i de subgrafos previamente separados.
Teorema D.5. Condición suficiente de
bifurcación
Sea G = (N, A, w) un grafo con un par de nodos j, l (cid:0) N tal
que W_{ij} = 0 (i no influye sobre j en G). Si W'_i satisface
W'_{ij} > 0, entonces j es alcanzable desde i en G' y:
Condición suficiente de bifurcación
W_{ij} = 0 ∧ W'_{ij} > 0 ⟹ j (cid:0) supp (  (G, i, W'_i)) si j
(cid:0) supp(R*(G))
Condición suficiente, no necesaria · la bifurcación puede ocurrir también cuando
se elimina una arista existente (W_{ij} > 0 → W'_{ij} = 0) y j queda
desconectado del sumidero
Demostración del Teorema D.5
Si W_{ij} = 0 y W'_{ij} > 0: en G' existe la arista (i,j)
que no existía en G. Si j no era alcanzable desde
ningún otro nodo en G (j (cid:0) supp(R*(G))), la nueva
arista lo conecta al grafo activo. Por el Teorema de
Perron-Frobenius: si G' es primitivo (condición del
Teorema 6), R*^{G'}(j) > 0. Luego j (cid:0)
supp((cid:0)(G,i,W'_i)). ✓

Axiomatización del Sistema de la Doble Mediación
El Teorema D.5 formaliza la intuición del reviewer: hay decisiones que no solo
cambian la magnitud de la imputación, sino que cambian qué actores son
causalmente relevantes. Esos son los nodos de bifurcación. (cid:0)
Conexión con los nodos de diseño. En los sistemas
analizados en la Parte VIII, el nodo diseñador D es
típicamente un nodo de bifurcación causal: su sustitución por
el promedio (la matriz W(cid:0)_D de la Definición 3.2) puede
hacer aparecer o desaparecer trayectorias causales enteras. Eso
explica por qué R*_net(D) >> R*_net(E) incluso cuando la
diferencia (cid:0)W_{D·} − W(cid:0)_{D·} ‖(cid:0) parece moderada: la
bifurcación produce cambios en el soporte que no están
capturados por la cota lineal del Teorema D.2.
El Teorema D.5 abre un programa de investigación: caracterizar los grafos
causales por su número de nodos de bifurcación, identificar condiciones
estructurales que los producen, y derivar cotas para el cambio en Δ_net_total
cuando un nodo de bifurcación es perturbado. La cota del Teorema D.2 no
aplica directamente a nodos de bifurcación porque el cambio en el soporte
introduce discontinuidades en (cid:0) que la norma (cid:0)W'_i − W_{i·} ‖(cid:0) no
captura.
Objeto Notación Resultado / Sección
tipo
Dominancia de Δ_net(k*) ≥ Δ_net(i) Orden parcial Teorema
imputación ∀i sobre nodos D.3
neta
Corolario: S S_est→1 (cid:0) Consecuencia Corolario
anula Δ_net Δ_net→−α_vol de Davis- D.4.1
Kahan
Corolario: α_vol(a)>α_vol(b) (cid:0) Migración Corolario
migración Δ_net(b)>Δ_net(a) hacia menor D.4.2
asunción
Corolario: α_vol→R*_net (cid:0) Cancelación Corolario
asunción anula Δ_net→0 de brecha D.4.3

Axiomatización del Sistema de la Doble Mediación
Estabilidad de ∀i: S_est(i)→1 ó Trayectoria Teorema
trayectoria α_vol(i)→R*_net(i) estable D.4
Fragilidad ∃k: S_est(k)<<1 ∧ Nodo k Teorema
α_vol(k)<<R*_net(k) crítico para D.4
Δ_net_total
Nodo de supp((cid:0)(G,i,W'_i)) ≠ Cambio Definición
bifurcación supp(R*(G)) cualitativo en D.7
soporte
Condición W_{ij}=0 ∧ Aparición de Teorema
suficiente W'_{ij}>0 (cid:0) nuevo nodo D.5
bifurcación bifurcación activo