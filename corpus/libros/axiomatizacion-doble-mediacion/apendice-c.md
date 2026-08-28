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

