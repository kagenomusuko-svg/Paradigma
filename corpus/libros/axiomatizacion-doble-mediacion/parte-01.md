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
