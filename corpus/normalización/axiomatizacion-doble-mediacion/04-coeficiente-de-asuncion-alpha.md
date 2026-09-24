# Parte III. Coeficiente de asunción \(\alpha\)

## 1. Qué mide \(\alpha\)

\(\alpha_i\) registra la proporción de la posición causal del nodo \(i\) que fue efectivamente asumida en el período y dominio analizados. Su cálculo usa tres entradas por observación:

- \(I_i\): indicador de asunción efectiva;
- \(w_i\): peso de la observación;
- \(p_i\): proporción o probabilidad de asunción asociada a esa observación.

La forma discreta implementada por el motor es:

\[
\alpha=
\frac{\sum_{i=1}^{n} I_i w_i p_i}
{\sum_{i=1}^{n} w_i}.
\]

Cada caso se calcula para un nodo y un conjunto definido de observaciones. Para producir un vector de asunción, se repite la operación para cada nodo, conservando el orden de \(R^*\).

\(\alpha\) registra acciones y consecuencias verificables que recaen sobre la posición causal: reparación, reconocimiento operativo, modificación del sistema, sanción ejecutada u otra forma de carga efectiva definida para el análisis. La consecuencia puede ser voluntaria, forzada o impuesta. La fórmula mide la magnitud registrada; no codifica consentimiento ni intención.

## 2. Dominio de las entradas

Para interpretar \(\alpha\) como proporción se requiere:

\[
I_i\in\{0,1\},\qquad
w_i\geq0,\qquad
0\leq p_i\leq1,\qquad
\sum_i w_i>0.
\]

\(I_i=1\) cuando la observación cuenta como asunción efectiva en el caso estudiado; \(I_i=0\) cuando no cuenta. El motor acepta indicadores booleanos o valores exactamente iguales a 0 o 1. Las tres listas —indicadores, pesos y proporciones— deben tener la misma longitud.

El denominador suma los pesos de todas las observaciones, también aquellas cuyo indicador es cero. Si la suma de pesos es cero, el cálculo no está definido. Bajo las condiciones anteriores, \(\alpha\in[0,1]\).

## 3. Cálculo paso a paso

Considérese un nodo con tres observaciones:

| Observación | \(I_i\) | \(w_i\) | \(p_i\) |
| --- | ---: | ---: | ---: |
| Reparación parcial registrada | 1 | 2 | 0.8 |
| Sin consecuencia efectiva en el período | 0 | 1 | 0.9 |
| Sanción ejecutada | 1 | 3 | 0.5 |

### Numerador

Se multiplica el indicador, el peso y la proporción de cada observación:

\[
1\cdot2\cdot0.8=1.6,
\qquad
0\cdot1\cdot0.9=0,
\qquad
1\cdot3\cdot0.5=1.5.
\]

Se suman los productos:

\[
1.6+0+1.5=3.1.
\]

### Denominador

\[
2+1+3=6.
\]

### Resultado

\[
\alpha=\frac{3.1}{6}
=\frac{31}{60}
\approx0.5167.
\]

La asunción medida para ese nodo es aproximadamente \(0.5167\), o \(51.67\%\), conforme a los pesos y proporciones declarados.

## 4. Interpretación del indicador

El indicador \(I_i\) identifica si la observación entra como asunción efectiva. No indica si el nodo estuvo de acuerdo con ella.

Por ejemplo, una sanción ejecutada puede registrarse con \(I_i=1\) aunque el nodo sostenga que la sanción es injusta. El hecho de que la consecuencia haya recaído sobre el nodo se mide separadamente de su consentimiento, su arrepentimiento o su valoración de la decisión.

Una intención no ejecutada no aumenta \(\alpha\) por sí sola. Una consecuencia que efectivamente recae puede aumentar \(\alpha\) aunque haya sido impuesta. La selección de qué eventos cuentan como asunción debe definirse para el dominio antes de introducir sus observaciones.

## 5. De \(\alpha\) escalar al vector

Si el análisis incluye \(m\) nodos, cada nodo recibe su propio cálculo:

\[
\boldsymbol{\alpha}
=(\alpha_1,\alpha_2,\ldots,\alpha_m).
\]

El orden de componentes debe ser el mismo que en el vector \(R^*\). Las observaciones de nodos diferentes no se mezclan en una sola suma, salvo que una operación colectiva lo establezca expresamente.

Para cada componente se conservan sus entradas, sus productos, su suma ponderada y su denominador. Así se puede revisar qué eventos y pesos producen cada valor.

## 6. Comparación con \(R^*\): cálculo de \(\Delta\)

Una vez calculados ambos vectores sobre los mismos nodos y en la escala definida para el caso, el déficit de asunción se calcula componente a componente:

\[
\Delta_i=R^*_i-\alpha_i.
\]

Retomemos el vector del ejemplo de \(R^*\):

\[
R^*=
\left(\frac{2}{7},\frac{5}{7}\right).
\]

Supóngase que el primer nodo tiene \(\alpha_1=31/60\), obtenido arriba, y que las observaciones del segundo nodo producen \(\alpha_2=3/4\). Entonces:

\[
\Delta_1=\frac{2}{7}-\frac{31}{60}
=\frac{120-217}{420}
=-\frac{97}{420}
\approx-0.2310,
\]

\[
\Delta_2=\frac{5}{7}-\frac{3}{4}
=\frac{20-21}{28}
=-\frac{1}{28}
\approx-0.0357.
\]

El primer nodo carga una proporción superior a su componente de responsabilidad causal; el segundo presenta una diferencia menor en el mismo sentido. El signo negativo conserva la posibilidad de medir sobreasunción.

Si \(\Delta_i>0\), la contribución causal del nodo supera la asunción registrada. Si \(\Delta_i=0\), ambas magnitudes coinciden. Si \(\Delta_i<0\), la asunción registrada supera la contribución causal.

## 7. Interpretación metrológica

\(R^*\) y \(\alpha\) son magnitudes distintas:

| Magnitud | Pregunta |
| --- | --- |
| \(R^*_i\) | ¿Qué proporción causal corresponde al nodo respecto del resultado? |
| \(\alpha_i\) | ¿Qué proporción de asunción efectiva se registra para el nodo? |
| \(\Delta_i\) | ¿Cuál es la diferencia entre ambas proporciones? |

La resta requiere que los valores estén referidos al mismo nodo y que sus escalas de medición sean comparables en el análisis. Que ambos estén expresados entre cero y uno no basta, por sí solo, para demostrar comparabilidad entre dominios distintos.

\(\alpha\) describe una asunción registrada. No determina por sí mismo si la distribución es justa, si una sanción es legítima o qué consecuencia debería imponerse. Esas conclusiones requieren criterios adicionales.

## 8. Procedimiento reproducible del motor

Para calcular \(\alpha\):

1. reúne las observaciones de un nodo para el período definido;
2. asigna a cada observación su indicador \(I_i\), peso \(w_i\) y proporción \(p_i\);
3. verifica que las tres listas tengan igual longitud;
4. verifica que cada indicador sea booleano o exactamente 0/1;
5. calcula cada producto \(I_iw_ip_i\);
6. suma los productos para obtener el numerador;
7. suma todos los pesos para obtener el denominador;
8. divide numerador entre denominador;
9. repite para cada nodo y conserva el orden de \(R^*\);
10. calcula \(\Delta=R^*-\alpha\) después de obtener ambos vectores.

El motor registra los productos y sumas intermedias, el numerador, el denominador y la división final. Si las entradas se expresan como fracciones o cadenas decimales, el cálculo puede conservar aritmética racional exacta.


## 9. Comprobación con el motor Prometeo

El ejemplo de tres observaciones se ejecutó con la fórmula `alpha` de `prometeo-motor-calculo/motor.py`. Los decimales se ingresaron como cadenas para conservar la representación exacta:

```json
{
  "intervention": [1, 0, 1],
  "weight": ["2", "1", "3"],
  "p": [".8", ".9", ".5"]
}
```

El motor devolvió:

```json
{"numerator": 31, "denominator": 60}
```

Para el segundo nodo del ejemplo conjunto, la entrada `intervention=[1,1]`, `weight=["1","1"]`, `p=[".5","1"]` devuelve exactamente \(3/4\). Ambos valores se usan sin redondeo en las operaciones posteriores de \(\Delta\) y \(J\).
