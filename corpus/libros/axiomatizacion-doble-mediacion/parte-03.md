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
