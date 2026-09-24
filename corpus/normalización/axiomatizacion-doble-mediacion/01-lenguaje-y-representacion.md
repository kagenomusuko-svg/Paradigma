# Apertura. Lenguaje y representación del sistema causal

## 1. El sistema que se va a calcular

Un cálculo causal comienza con una representación explícita del proceso analizado. Esa representación identifica las unidades que intervienen, las relaciones de influencia entre ellas y el resultado respecto del cual se distribuye la contribución.

Se representa mediante un grafo dirigido ponderado:

\[
G=(N,A,W)
\]

donde:

- \(N=\{N_1,\ldots,N_m\}\) es el conjunto de nodos;
- \(A\subseteq N\times N\) es el conjunto de aristas dirigidas;
- \(W=[w_{ij}]\) es la matriz de pesos asociados a las aristas.

Un nodo puede representar una persona, una institución, una regla, un procedimiento, un sistema técnico o cualquier otro componente distinguible del proceso. La unidad de análisis se fija antes de calcular: si dos funciones deben recibir contribuciones diferentes, se representan como nodos distintos; si una misma unidad conserva una sola función causal para el problema estudiado, se representa como un nodo.

La arista \(N_i\to N_j\) indica que, dentro del modelo, la actividad o condición representada por \(N_i\) influye en \(N_j\). La dirección importa: \(N_i\to N_j\) no significa lo mismo que \(N_j\to N_i\). Una sucesión temporal, por sí sola, tampoco establece una arista; la relación debe pertenecer al modelo causal que se construye para el caso.

## 2. Pesos y matriz de relaciones

El elemento \(w_{ij}\) registra el peso asignado a la influencia de \(N_i\) sobre \(N_j\). Si no se representa una arista entre ambos nodos, \(w_{ij}=0\). Para las matrices procesadas por el motor, los pesos son no negativos. Cada fila no terminal se normaliza para que la suma de sus pesos sea igual a uno; la fila del nodo terminal es cero.

\[
w_{ij}\geq 0,\qquad
\sum_{j=1}^{m}w_{ij}=1
\quad\text{para cada nodo no terminal }N_i
\]

Si \(N_f\) representa el resultado terminal:

\[
w_{fj}=0\quad\text{para todo }j
\]

La normalización permite comparar la distribución de influencia que sale de cada nodo. No afirma que los pesos sean frecuencias observadas ni probabilidades de que ocurra el resultado. Son magnitudes de la representación causal elegida.

### Ejemplo 1. Una cadena con dos rutas de influencia

Considérese un proceso con tres nodos:

- \(D\): diseño de una regla;
- \(E\): ejecución bajo esa regla;
- \(Y\): resultado.

Supóngase que el diseño influye directamente en el resultado con peso \(0.4\) e influye en la ejecución con peso \(0.6\); la ejecución influye en el resultado. La matriz correspondiente es:

\[
W=
\begin{pmatrix}
0 & 0.6 & 0.4\\
0 & 0 & 1\\
0 & 0 & 0
\end{pmatrix}
\]

Las filas y columnas conservan el orden \((D,E,Y)\).

La primera fila suma:

\[
0+0.6+0.4=1
\]

La segunda fila suma:

\[
0+0+1=1
\]

La tercera fila suma cero porque \(Y\) es terminal: dentro de este ejemplo, el resultado no transmite influencia hacia otro nodo.

La matriz no contiene todavía el vector de responsabilidad \(R^*\). Describe la estructura ponderada que sirve de entrada para calcularlo. Esta diferencia evita confundir el peso de una relación entre nodos con la contribución final asignada a cada nodo.

## 3. Notación de vectores

Un vector con una entrada por nodo se escribe:

\[
x=(x_1,x_2,\ldots,x_m)
\]

La entrada \(x_i\) corresponde siempre al nodo \(N_i\) según el orden declarado para el caso. Entre otros usos, un vector puede contener la distribución de responsabilidad, los valores de asunción, los déficits o los pesos de sustituibilidad.

La suma de los componentes de \(x\) se escribe:

\[
\sum_{i=1}^{m}x_i
\]

El producto componente a componente de dos vectores \(x\) e \(y\) se escribe \(x\odot y\). El producto escalar se escribe:

\[
x\cdot y=\sum_{i=1}^{m}x_i y_i
\]

La operación utilizada se especifica en cada fórmula. Por ejemplo, una resta de vectores conserva el orden de los nodos y se calcula entrada por entrada:

\[
x-y=(x_1-y_1,\ldots,x_m-y_m)
\]

## 4. Datos, parámetros y resultados

En cada ejercicio se separan cuatro elementos:

| Elemento | Función |
| --- | --- |
| Nodos y aristas | Describen quién o qué interviene y cómo se relaciona. |
| Pesos de entrada | Cuantifican las relaciones incluidas en la matriz. |
| Parámetros | Fijan valores requeridos por una operación, como umbrales o pesos temporales. |
| Resultados | Son los vectores o escalares obtenidos al aplicar la fórmula. |

La separación permite reproducir el cálculo. Si cambia un peso de entrada, puede identificarse qué operación y qué resultado dependen de ese cambio.

## 5. Secuencia mínima de representación

Antes de aplicar una fórmula al caso:

1. declarar el resultado que se analizará;
2. enumerar los nodos y fijar su orden;
3. indicar cuáles son terminales;
4. registrar las aristas dirigidas;
5. asignar los pesos correspondientes;
6. comprobar las dimensiones y las sumas exigidas por la operación.

Con esta representación establecida, las partes siguientes introducen las magnitudes causales y muestran cómo se calculan.
