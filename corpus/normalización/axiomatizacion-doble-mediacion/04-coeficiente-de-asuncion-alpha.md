# Parte III. Coeficiente de asunción \(\alpha\)

## 1. Qué mide \(\alpha\)

\(\alpha_i\) representa la proporción de la posición causal del nodo \(i\) que fue efectivamente asumida durante el período y en el dominio analizados. Para calcularla se consideran, por observación:

- \(I_i\): indicador de que la observación cuenta como asunción efectiva;
- \(w_i\): peso asignado a la observación;
- \(p_i\): proporción o probabilidad de asunción asociada a ella.

La forma discreta es:

\[
\alpha=
\frac{\sum_{i=1}^{n} I_iw_ip_i}
{\sum_{i=1}^{n}w_i}.
\]

Cada nodo se calcula por separado. Para construir el vector de asunción, se repite el procedimiento para todos los nodos y se conserva el orden de \(R^*\).

\(\alpha\) registra acciones y consecuencias verificables que recaen sobre la posición causal: reparación, reconocimiento operativo, modificación del sistema, sanción ejecutada u otra forma de carga efectiva definida para el análisis. La consecuencia puede ser voluntaria, forzada o impuesta. La magnitud registrada no equivale a consentimiento ni a intención.

## 2. Dominio de las entradas

Para interpretar \(\alpha\) como proporción, se requiere:

\[
I_i\in\{0,1\},\qquad
w_i\geq0,\qquad
0\leq p_i\leq1,\qquad
\sum_iw_i>0.
\]

\(I_i=1\) cuando la observación cuenta como asunción efectiva; \(I_i=0\) cuando no cuenta. El denominador suma los pesos de todas las observaciones, incluidas las que tienen indicador cero.

Con estas condiciones, el numerador no es negativo y no supera al denominador; por ello \(\alpha\in[0,1]\). Si la suma de pesos es cero, la división no está definida.

## 3. Cálculo paso a paso

Considérese un nodo con tres observaciones:

| Observación | \(I_i\) | \(w_i\) | \(p_i\) |
| --- | ---: | ---: | ---: |
| Reparación parcial registrada | 1 | 2 | \(0.8\) |
| Sin consecuencia efectiva en el período | 0 | 1 | \(0.9\) |
| Sanción ejecutada | 1 | 3 | \(0.5\) |

### Numerador

Se calcula \(I_iw_ip_i\) para cada observación:

\[
1\cdot2\cdot0.8=1.6,
\qquad
0\cdot1\cdot0.9=0,
\qquad
1\cdot3\cdot0.5=1.5.
\]

Se suman los tres productos:

\[
1.6+0+1.5=3.1.
\]

### Denominador

\[
2+1+3=6.
\]

### Cociente

\[
\alpha=\frac{3.1}{6}
=\frac{31}{10}\cdot\frac16
=\frac{31}{60}
\approx0.5167.
\]

La asunción medida para el nodo es \(31/60\), aproximadamente \(51.67\%\).

## 4. Interpretación del indicador

El indicador \(I_i\) determina si la observación entra en la medición de la asunción efectiva. No señala si el nodo estuvo de acuerdo con ella.

Una sanción ejecutada puede contar con \(I_i=1\) aunque el nodo considere injusta la sanción. La consecuencia ocurrió y recayó sobre su posición causal; su consentimiento, arrepentimiento o valoración son cuestiones distintas.

Una intención que no se concreta en acción o consecuencia no aumenta \(\alpha\) por sí sola. Una consecuencia que efectivamente recae puede aumentar \(\alpha\) aunque haya sido impuesta. Antes de calcular, se define qué acciones o consecuencias cuentan en el dominio estudiado.

## 5. De \(\alpha\) escalar al vector

Para \(m\) nodos, se calcula un coeficiente por nodo:

\[
\boldsymbol{\alpha}
=(\alpha_1,\alpha_2,\ldots,\alpha_m).
\]

El orden debe coincidir con el de \(R^*\). Las observaciones de actores distintos no se suman en un mismo numerador salvo que una regla colectiva defina expresamente esa agregación.

Por ejemplo, para un segundo nodo con dos observaciones de igual peso, con \(I=(1,1)\) y \(p=(0.5,1)\):

\[
\alpha_2=
\frac{1\cdot1\cdot0.5+1\cdot1\cdot1}{1+1}
=\frac{0.5+1}{2}
=\frac{1.5}{2}
=\frac34.
\]

Así, los dos coeficientes del ejemplo conjunto son:

\[
\boldsymbol{\alpha}
=\left(\frac{31}{60},\frac34\right).
\]

## 6. Relación con \(R^*\): cálculo de \(\Delta\)

Una vez calculados ambos vectores para los mismos nodos, el déficit se obtiene componente a componente:

\[
\Delta_i=R^*_i-\alpha_i.
\]

Retomemos:

\[
R^*=\left(\frac27,\frac57\right),
\qquad
\boldsymbol{\alpha}=\left(\frac{31}{60},\frac34\right).
\]

Para el primer nodo, buscamos un denominador común, \(420\):

\[
\Delta_1
=\frac27-\frac{31}{60}
=\frac{120}{420}-\frac{217}{420}
=-\frac{97}{420}.
\]

Para el segundo nodo, usamos denominador común \(28\):

\[
\Delta_2
=\frac57-\frac34
=\frac{20}{28}-\frac{21}{28}
=-\frac1{28}.
\]

Por tanto:

\[
\Delta=\left(-\frac{97}{420},-\frac1{28}\right)
\approx(-0.2310,-0.0357).
\]

Un valor positivo indica que la contribución causal supera la asunción registrada. Un valor cero indica igualdad. Un valor negativo indica que la asunción registrada supera la contribución causal.

## 7. Interpretación metrológica

| Magnitud | Pregunta |
| --- | --- |
| \(R^*_i\) | ¿Qué proporción causal corresponde al nodo respecto del resultado? |
| \(\alpha_i\) | ¿Qué proporción de asunción efectiva se registra para el nodo? |
| \(\Delta_i\) | ¿Cuál es la diferencia entre ambas proporciones? |

La resta requiere que \(R^*\) y \(\alpha\) correspondan al mismo nodo y se expresen en escalas comparables para el análisis. Que ambas magnitudes estén entre cero y uno no demuestra por sí solo que sus escalas sean comparables entre dominios distintos.

\(\alpha\) describe una asunción registrada. No determina por sí mismo si la distribución es justa, si una sanción es legítima o qué consecuencia debería imponerse. Esas conclusiones requieren criterios adicionales.

## 8. Procedimiento reproducible

1. Reúne las observaciones del nodo para el período definido.
2. Asigna a cada observación \(I_i\), \(w_i\) y \(p_i\).
3. Multiplica \(I_iw_ip_i\) para cada fila.
4. Suma los productos para obtener el numerador.
5. Suma todos los pesos para obtener el denominador.
6. Divide el numerador entre el denominador.
7. Repite el cálculo para cada nodo, en el orden de \(R^*\).
8. Resta \(\alpha_i\) de \(R^*_i\) para obtener cada componente de \(\Delta\).

El desarrollo muestra cada producto, cada suma y la división final. Cuando los datos son racionales, conservar fracciones permite evitar redondeos prematuros.
