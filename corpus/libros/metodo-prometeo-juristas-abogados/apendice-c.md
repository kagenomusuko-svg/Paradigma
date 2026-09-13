### Apéndice C Guía de la plantilla de

### cálculo

Estructura, celdas y lógica de la hoja de cálculo automatizada para el

Método Prometeo

La plantilla de cálculo automatiza los pasos 2 al 5 del método para casos con hasta seis nodos activos. No requiere conocimientos de programación: el analista introduce los pesos de la hoja de calibración y obtiene directamente R*, S, R*_neta, α, Δ y AD_i para cada nodo, en los tres escenarios de sensibilidad. El presente apéndice describe la estructura de la plantilla para que el lector pueda entender qué calcula, verificar sus resultados, y reproducirla en cualquier entorno de hoja de cálculo si lo necesita.

⚠ Sobre el uso de la plantilla en el expediente: la plantilla es un instrumento de cálculo, no un documento del expediente. Lo que se incorpora al expediente es la hoja de calibración (Apéndice B) y los cuatro documentos del análisis. Los cálculos intermedios pueden presentarse como anexo técnico del peritaje si el tribunal lo solicita, pero la plantilla en sí es el instrumento de trabajo del perito, no una pieza procesal autónoma.

### C.1 Estructura de la plantilla: las cinco pestañas

Pestaña Nombre Contenido y función

Página | XXV

1 Calibración Entrada de datos: los pesos mínimo, central y máximo de cada arista. Máximo 6 aristas activas + 2 aristas excluidas. Las celdas de entrada están en amarillo. El perito introduce únicamente los valores de la columna 'Rango [a, b]' de su hoja de calibración. La pestaña calcula automáticamente el punto central.

2 R* Cálculo del vector R* para los tres escenarios (mínimo, central, máximo). Muestra la fórmula de normalización y el porcentaje de cada nodo. Resalta automáticamente el nodo de mayor R* en cada escenario. Incluye la verificación de suma = 100%.

3 S y R*_neta Entrada de las respuestas A, B, C del protocolo de S para cada nodo (valores 0, 0.5 o 1). Calcula S_i y R*_neta = R*_i × (1 − S_i) automáticamente. Incluye campo de texto para registrar la justificación de cada respuesta.

4 Sensibilidad La tabla de sensibilidad completa: R* de cada nodo en los tres escenarios, comparación de órdenes, y diagnóstico automático del tipo de declaración (A, B o C). El diagnóstico se basa en si el nodo de mayor R* es el mismo en los tres escenarios y si el orden completo se mantiene.

5 Ajuste Debitor

Entrada de D_total (mínimo y central) y de los valores α de cada nodo. Calcula AD_i = R*_i × D_total y Δ_i = R*_i − α_i en valor absoluto (porcentaje) y en pesos. Incluye el panel final con todos los indicadores del caso.

### C.2 Flujo de trabajo con la plantilla

Paso Acción Qué produce

### Página | XXVI

1 Completar la hoja de calibración (Apéndice B)

Tener los rangos [a, b] de cada arista con su tipo E y su fuente. Este es el único paso que requiere juicio analítico del perito: el resto de la plantilla es cálculo automático.

2 Introducir los rangos en la pestaña 'Calibración'

La pestaña calcula los puntos centrales y prepara los tres escenarios. Tiempo estimado: 5-10 minutos para un caso con 4-6 nodos.

3 Revisar la pestaña 'R*'

Verificar que la suma de R* sea exactamente 100% en los tres escenarios. Si no suma 100%, hay un error de entrada en la pestaña 1.

4 Introducir las respuestas A, B, C en la pestaña 'S y R*_neta'

La pestaña calcula S_i y R*_neta para cada nodo. Registrar la justificación de cada respuesta en el campo de texto correspondiente: ese texto es el que el perito defenderá en el interrogatorio.

5 Revisar la pestaña 'Sensibilidad'

Verificar el diagnóstico automático del tipo de declaración. Si el diagnóstico es Declaración C, identificar la arista sensible y decidir si hay evidencia adicional que reduciría su rango.

6 Introducir D_total y α en la pestaña 'Ajuste Debitor'

La pestaña produce el panel final completo con AD_i en escenario mínimo y central, Δ_i en porcentaje y en pesos, y el diagnóstico de déficit por nodo.

7 Exportar los cuatro documentos

Las pestañas 1, 4 y 5 producen directamente la hoja de calibración, la tabla de sensibilidad y el ajuste debitor. La declaración de robustez (Documento 3) se redacta manualmente usando las plantillas del Capítulo 6 §6.5.

### C.3 Reproducir la plantilla manualmente

### Página | XXVII

Si el entorno de trabajo no permite usar la plantilla (acceso restringido a herramientas, requisitos de seguridad del expediente, preferencia de trabajo en papel), los cálculos pueden reproducirse manualmente con las fórmulas del Capítulo 2. El siguiente resumen es la referencia rápida.

Cálculo Fórmula Dónde se describe

R*(i) R*(i) = w_i / Σ w_j (para cada escenario min / central / max)

Cap. 2, §2.2 — Paso 3a. La suma de todos los R* debe ser exactamente 1.0 (100%).

S(i) S(i) = (A + B + C) / 3 donde A, B, C □ {0, 0.5, 1}

Cap. 2, §2.3.1 — Paso 4. Las tres preguntas y los criterios de respuesta están en la tabla del §2.3.1.

R*_neta(i) R*_neta(i) = R*(i) × (1 − S(i))

Cap. 2, §2.3.2. R*_neta es la responsabilidad causal idiosincrática: el peso que no puede ser redistribuido al sistema.

α(i) α(i) = [monto reconocido o reparado por i] / AD(i)

Cap. 2, §2.4. En PLD: proporción del cumplimiento de la obligación de reporte. Ver tabla del Cap. 6, §6.6.

Δ(i) Δ(i) = R*(i) − α(i) (resultado en puntos porcentuales)

Cap. 2, §2.5. Δ positivo = déficit (nodo causó más de lo que asumió). Δ negativo = sobre-imputación.

AD(i) AD(i) = R*(i) × D_total   (resultado en unidad monetaria)

Cap. 2, §2.6 — Paso 5. Usar R* (no R*_neta): el daño existe independientemente de la sustituibilidad.

Shapley φ(i)

φ(i) = Σ sobre todos los órdenes de [aporte de i en ese orden] / n!

Cap. 6, §6.7.3. Solo cuando ningún nodo es individualmente condición necesaria del resultado.

Ejemplo de verificación rápida. Caso Meridiano (Cap. 7): w_PM=0.625, w_CD=0.790, w_MC=0.695, w_SS=0.380. Σw=2.490. R*(CD)=0.790/2.490=31.7%. R*_neta(SS)=15.3%× (1−0.85) =2.3%. AD(MC) con D_total=$26.5M: 27.9%×$26.5M=$7.39M. Todos estos

### Página | XXVIII

valores deben coincidir con los de la plantilla descargada. Si no coinciden, hay un error de entrada en los pesos de la columna 'Calibración'.

### Sobre los tres apéndices

✓ Apéndice A — Tabla E0-E8: la referencia de calibración central. Cubre los nueve tipos de evidencia con su rango w admisible, ejemplos por dominio, y las reglas de consistencia. Se usa como consulta permanente durante la construcción de la hoja de calibración.

✓ Apéndice B — Hoja de calibración en blanco: el único documento del apéndice que se incorpora directamente al expediente. Incluye instrucciones de uso, encabezado de identificación, formulario con seis filas activas y dos filas de exclusión, fila de suma de verificación, y la nota de uso procesal.

✓ Apéndice C — Guía de la plantilla de cálculo: descripción de las cinco pestañas de la plantilla, el flujo de trabajo en siete pasos, y la tabla de referencia rápida de fórmulas para reproducción manual.

### Página | XXIX

## Notas al pie

[^1]: E — 
Empresa
