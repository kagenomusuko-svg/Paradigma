# Parte V. Sustituibilidad y responsabilidad neta

## 1. El objeto de \(S\)

La sustituibilidad expresa cuánto del resultado asociado a un nodo podría reproducirse si otro elemento ocupara su posición o si se mantuviera la configuración que hizo posible el resultado.

La pregunta aplicada es:

> Si se reemplaza este nodo bajo las condiciones definidas, ¿con qué frecuencia o intensidad se conserva el resultado?

El cálculo puede operacionalizar esta pregunta de distintas maneras. Cada estimador utiliza datos diferentes y responde una pregunta específica. Un mismo valor numérico obtenido por dos procedimientos distintos no hace que los procedimientos sean equivalentes.

## 2. Score aplicado de tres componentes

En el score aplicado se consideran tres criterios:

- \(A\): formalización del procedimiento;
- \(B\): consecuencias de desobedecer la instrucción;
- \(C\): proporción de pares que habría actuado igual bajo la misma configuración.

Cada criterio se asigna en la escala discreta:

\[
A,B,C\in\left\{0,\frac12,1\right\}.
\]

El score es su promedio:

\[
S_{\mathrm{app}}=\frac{A+B+C}{3}.
\]

### Ejemplo

Sean:

\[
A=1,\qquad B=\frac12,\qquad C=0.
\]

Se suman los tres componentes:

\[
1+\frac12+0=\frac32.
\]

Se divide entre tres:

\[
S_{\mathrm{app}}=\frac{3/2}{3}
=\frac32\cdot\frac13
=\frac12.
\]

El valor obtenido es \(S_{\mathrm{app}}=1/2\).

## 3. Estimación por sustituciones observadas

Si se realizan sustituciones en condiciones elegibles y se registra si el resultado se conserva, se calcula:

\[
S_{\mathrm{prob}}=
\frac{n_{\mathrm{mismo\ resultado}}}
{n_{\mathrm{ensayos\ elegibles}}}.
\]

El número de ensayos elegibles debe ser positivo y el número de resultados iguales no puede excederlo.

### Ejemplo

En cuatro ensayos elegibles, dos sustituciones conservaron el resultado:

\[
S_{\mathrm{prob}}=\frac24=\frac12.
\]

Si tres de cuatro lo conservaran:

\[
S_{\mathrm{prob}}=\frac34.
\]

Este estimador se basa en ensayos observados; no es el promedio de los tres criterios de la sección anterior.

## 4. Razón entre peso causal y volitivo

Otra operacionalización compara el peso causal con la suma del peso causal y el peso volitivo:

\[
S_{\mathrm{ratio}}=
\frac{w_{\mathrm{causal}}}
{w_{\mathrm{causal}}+w_{\mathrm{volitivo}}}.
\]

Los pesos deben estar expresados en escalas comparables y su suma debe ser distinta de cero.

### Ejemplo

Sean \(w_{\mathrm{causal}}=3\) y \(w_{\mathrm{volitivo}}=2\). Primero se calcula el denominador:

\[
3+2=5.
\]

Luego se divide el peso causal entre el total:

\[
S_{\mathrm{ratio}}=\frac35.
\]

La razón compara dos magnitudes; no cuenta ensayos ni promedia criterios documentales.

## 5. Intervalo ponderado

Si cada escenario tiene una probabilidad \(p_j\) y un intervalo de sustituibilidad \([S_{j,\min},S_{j,\max}]\), los extremos ponderados son:

\[
S_{\min}=\sum_jp_jS_{j,\min},
\qquad
S_{\max}=\sum_jp_jS_{j,\max}.
\]

### Ejemplo

Considérense dos escenarios:

\[
p_1=\frac14,\quad [S_{1,\min},S_{1,\max}]=\left[\frac12,\frac34\right],
\]

\[
p_2=\frac34,\quad [S_{2,\min},S_{2,\max}]=\left[0,\frac14\right].
\]

Límite inferior:

\[
S_{\min}
=\frac14\cdot\frac12+\frac34\cdot0
=\frac18+0
=\frac18.
\]

Límite superior:

\[
S_{\max}
=\frac14\cdot\frac34+\frac34\cdot\frac14
=\frac3{16}+\frac3{16}
=\frac6{16}
=\frac38.
\]

Por tanto, el intervalo ponderado es:

\[
S\in\left[\frac18,\frac38\right].
\]

## 6. Sensibilidad estructural

La sensibilidad estructural compara una distribución causal original \(P\) con una distribución \(Q\) obtenida después de sustituir un nodo. Se calcula mediante el complemento de la divergencia de Kullback–Leibler normalizada:

\[
S_{\mathrm{estructural}}
=1-\frac{D_{\mathrm{KL}}(P\|Q)}{\ln(m)},
\]

donde \(m\) es el número de componentes y:

\[
D_{\mathrm{KL}}(P\|Q)
=\sum_{i=1}^{m}p_i\ln\left(\frac{p_i}{q_i}\right).
\]

Se emplea esta expresión cuando \(P\) y \(Q\) son distribuciones con componentes positivos. El cálculo de logaritmos produce aproximaciones decimales.

### Ejemplo: distribuciones cercanas

Sean:

\[
P=(0.6,0.4),\qquad Q=(0.5,0.5),\qquad m=2.
\]

Primero se calcula la divergencia:

\[
D_{\mathrm{KL}}(P\|Q)
=0.6\ln\left(\frac{0.6}{0.5}\right)
+0.4\ln\left(\frac{0.4}{0.5}\right)
\]

\[
=0.6\ln(1.2)+0.4\ln(0.8)
\approx0.0201355.
\]

Como \(\ln(2)\approx0.6931472\):

\[
S_{\mathrm{estructural}}
=1-\frac{0.0201355}{0.6931472}
\approx1-0.0290494
\approx0.9709506.
\]

### Ejemplo: distribuciones muy distintas

Sean:

\[
P=(0.99,0.01),\qquad Q=(0.01,0.99),\qquad m=2.
\]

La divergencia es:

\[
D_{\mathrm{KL}}(P\|Q)
=0.99\ln(99)+0.01\ln\left(\frac1{99}\right).
\]

Como \(\ln(1/99)=-\ln(99)\):

\[
D_{\mathrm{KL}}(P\|Q)
=(0.99-0.01)\ln(99)
=0.98\ln(99)
\approx4.5032175.
\]

Entonces:

\[
S_{\mathrm{estructural}}
=1-\frac{4.5032175}{0.6931472}
\approx1-6.4967695
\approx-5.4967695.
\]

Esta fórmula puede producir valores negativos. La expresión \(1-D_{\mathrm{KL}}/\ln(m)\) no garantiza por sí sola un resultado dentro de \([0,1]\); su salida se conserva con el signo y la magnitud que resulten de la operación.

## 7. Selección e interpretación

| Estimador | Datos que utiliza | Qué calcula |
| --- | --- | --- |
| \(S_{\mathrm{app}}\) | Tres criterios documentales en escala discreta | Promedio de criterios |
| \(S_{\mathrm{prob}}\) | Reemplazos elegibles y resultados observados | Frecuencia de conservación del resultado |
| \(S_{\mathrm{ratio}}\) | Peso causal y peso volitivo | Proporción de un peso respecto del total |
| Intervalo ponderado | Probabilidades e intervalos por escenario | Límites agregados de \(S\) |
| \(S_{\mathrm{estructural}}\) | Distribución original y distribución sustituida | Complemento normalizado de divergencia |

Se declara qué estimador se utilizó, qué datos lo alimentan y qué significa su salida. Estos procedimientos no se sustituyen entre sí por compartir el símbolo \(S\).

## 8. Responsabilidad neta

Una vez establecido \(S_i\), la responsabilidad neta del nodo se calcula así:

\[
R^*_{\mathrm{neta},i}=R^*_i(1-S_i).
\]

Para un vector, el producto se realiza componente a componente:

\[
R^*_{\mathrm{neta}}=R^*\odot(\mathbf{1}-S).
\]

Cada valor de \(S_i\) debe corresponder al mismo nodo que \(R^*_i\) y al estimador elegido para el análisis.

### Ejemplo

Sean:

\[
R^*=\left(\frac27,\frac57\right),
\qquad
S=\left(\frac12,\frac34\right).
\]

Para el primer nodo:

\[
R^*_{\mathrm{neta},1}
=\frac27\left(1-\frac12\right)
=\frac27\cdot\frac12
=\frac17.
\]

Para el segundo:

\[
R^*_{\mathrm{neta},2}
=\frac57\left(1-\frac34\right)
=\frac57\cdot\frac14
=\frac5{28}.
\]

Así:

\[
R^*_{\mathrm{neta}}=\left(\frac17,\frac5{28}\right).
\]

El vector conserva el orden de nodos de \(R^*\).

## 9. Procedimiento de cálculo

1. Elige el estimador de \(S\) adecuado para los datos disponibles.
2. Calcula y conserva cada entrada y operación intermedia.
3. Asocia cada valor de \(S_i\) con el nodo correspondiente.
4. Comprueba que \(R^*\) y \(S\) tengan la misma longitud y orden.
5. Calcula \(1-S_i\) para cada nodo.
6. Multiplica cada \(R^*_i\) por el factor correspondiente.
7. Registra el resultado como \(R^*_{\mathrm{neta}}\) e identifica el estimador de \(S\) utilizado.
