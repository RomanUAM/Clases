# Semana 1 · Probabilidad y Estadística (1153001)

Tres sesiones de 90 minutos, para estudiantes de licenciatura en ingeniería. Este guion acompaña las tres presentaciones revisadas. El programa institucional 1153001 incluye introducción, estadística descriptiva, probabilidad, variables aleatorias, modelos, muestreo, estimación y pruebas de hipótesis. **En esta semana se enseñan introducción y descriptiva**; las otras materias aparecen como preguntas que motivan semanas posteriores. El Word adjunto, clave 1150018, corresponde a otra propuesta de UEA y no modifica el programa 1153001.

## Decisión docente y ritmo

Cada equipo tiene cuatro integrantes. La meta, los registros y el producto son comunes, pero cada estudiante hace una predicción y una salida individual. Formar equipos con experiencias diversas cuando sea posible. Los papeles rotan en cada sesión, y dentro de la sesión de monedas cambian después de la tercera corrida. El alumnado puede trabajar con datos suministrados cuando observar animales o manipular una moneda resulte inaccesible o inseguro. El objetivo y los criterios son los mismos.

Cada sesión alterna explicación breve, cálculo visible, producción y revisión. Las preguntas sobre independencia, modelos, estimación y ley de grandes números se dejan abiertas explícitamente. No se presenta una demostración que el grupo todavía no puede justificar.

## Sesión 1. Medir antes de calcular

**Aprendizaje observable.** Cada estudiante define la unidad y la variable de un conteo, y cada equipo produce un registro reproducible con una conclusión que no excede sus cinco observaciones.

### Definiciones y ejemplo que deben quedar en la pizarra

- **Unidad de observación:** un intervalo de un minuto en un lugar y bajo un protocolo fijados. Cinco minutos consecutivos aportan cinco unidades, aunque se registren doce eventos.
- **Variable:** \(X_i\) es el número de entradas al radio aproximado de tres metros durante el intervalo \(i\), con \(X_i\in\{0,1,2,\ldots\}\). Un reingreso cuenta como otro evento. Esta variable mide eventos de entrada, no individuos distintos.
- **Muestra:** los cinco intervalos efectivamente registrados. **Población estadística de interés:** los intervalos comparables sobre los que querríamos aprender, según lugar, horario y protocolo. No equiparar esa población con la población biológica de gatos.
- **Frecuencia absoluta:** \(f(x)=\#\{i:X_i=x\}\); comprobar \(\sum_x f(x)=n\).
- **Media descriptiva:** \(\bar X=\frac1n\sum_{i=1}^{n}X_i\). Con \((2,3,1,4,2)\): \(\bar X=12/5=2.4\) entradas por intervalo de un minuto. El total es doce entradas en cinco minutos. Si los intervalos tienen igual duración, el cociente también equivale a 2.4 entradas observadas por minuto en esa ventana.

### Actividad ejecutable (90 minutos)

| Tiempo | Acción del equipo de cuatro | Evidencia o control |
|---|---|---|
| 0–8 | Cada integrante responde: «¿Doce entradas implican doce gatos distintos?». Comparten las cuatro respuestas y anotan qué dato falta. | Cuatro predicciones individuales. |
| 8–25 | Acuerdan pregunta, unidad, variable, sitio, punto fijo, referencia de tres metros, regla de entrada/reingreso y cinco intervalos consecutivos. | Protocolo escrito antes de mirar datos. |
| 25–40 | Integrante A comunica el protocolo y vigila seguridad; B observa; C cronometra y registra los cinco intervalos; D anota incidencias y audita reingresos. Si se usa el conjunto \((2,3,1,4,2)\), señalan que es un **ejemplo suministrado**, no una observación propia. | Tabla con intervalo, hora, conteo e incidencia; se conservan los ceros. |
| 40–60 | Construyen tabla de frecuencias, diagrama de puntos, total y media con unidades. B y D cotejan los datos crudos con la gráfica. | \(\sum_x f(x)=5\) y cinco marcas en el diagrama. |
| 60–78 | Intercambian el registro con otro equipo. El equipo revisor localiza una ambigüedad concreta y pregunta si la conclusión se sostiene. | Anotación del par y corrección o justificación. |
| 78–85 | Entregan una página: pregunta, protocolo, datos, gráfica, cálculo, conclusión descriptiva y dos límites. | Producto común con cuatro nombres y aportes. |
| 85–90 | Cada integrante define \(X_i\), explica por qué doce entradas no equivalen a doce gatos, y propone una mejora de repetición. | Salida individual de tres respuestas. |

**Alternativa segura.** Se puede observar desde un punto accesible y sin interactuar con animales. Si no es viable, se proporciona una tabla de cinco intervalos ya registrados y sus metadatos; el equipo hace diseño, auditoría e interpretación sin simular que levantó esos datos.

**Criterio de revisión.** Dar crédito a una conclusión como «En estos cinco intervalos observamos doce entradas, con una media de 2.4 por minuto bajo el protocolo declarado». Solicitar corrección a «hay doce gatos en el campus» o «la tasa habitual es 2.4».

## Sesión 2. Monedas y estadísticos

**Aprendizaje observable.** Cada integrante distingue una corrida de un lanzamiento y calcula media, mediana, moda y dispersión de cinco valores posibles entre cero y tres. El equipo puede detectar un dato imposible y un divisor incorrecto.

### Definiciones y cálculo visible

- **Experimento:** una corrida de tres lanzamientos. Con C=cara y S=sello, \(\Omega=\{CCC,CCS,CSC,SCC,CSS,SCS,SSC,SSS\}\). Las ocho secuencias son resultados **posibles**; no son ocho corridas efectuadas.
- **Variable aleatoria discreta:** \(X:\Omega\to\{0,1,2,3\}\), número de caras de la corrida; \(X(CCS)=2\). Cinco corridas producen cinco valores de \(X\), aunque se lancen quince veces.
- **Frecuencia relativa:** \(h(x)=f(x)/5\); comprobar \(\sum_x h(x)=1\).
- **Mediana:** dato central después de ordenar cinco valores. **Moda:** valor o valores con frecuencia máxima. Explicitar si se adopta la convención «sin moda única» cuando todos los valores empatan.
- **Rango:** máximo menos mínimo. **Varianza muestral:** \(s^2=\frac{1}{n-1}\sum_i(X_i-\bar X)^2\). **Desviación estándar muestral:** \(s=\sqrt{s^2}\). El divisor \(n-1\) se usa al estimar la varianza de un proceso a partir de la muestra bajo los supuestos pertinentes; la dispersión descriptiva con divisor \(n\) es otra cantidad y debe rotularse así.

Para \(A=(0,1,1,3,3)\), \(\bar X=1.6\), mediana 1, modas 1 y 3, rango 3. Las desviaciones cuadradas suman \(2.56+0.36+0.36+1.96+1.96=7.20\), por lo que \(s_A^2=7.20/4=1.80\) y \(s_A\approx1.342\). Para \(B=(1,1,2,2,2)\), la misma media 1.6 acompaña \(s_B^2=1.20/4=0.30\). El contraste muestra por qué una media aislada oculta la forma de los datos.

### Actividad ejecutable (90 minutos)

| Tiempo | Acción del equipo de cuatro | Evidencia o control |
|---|---|---|
| 0–8 | Cada persona predice el valor de X más habitual e indica si presupone moneda equilibrada. | Predicción individual antes de lanzar. |
| 8–22 | A identifica unidad y secuencias posibles; B enuncia X; C revisa el dominio 0–3; D lee el protocolo. Asignan lanzamiento, registro, verificación y comunicación. | Tabla vacía con cinco filas, tres símbolos y X. |
| 22–35 | Realizan cinco corridas. Cambian los papeles después de la tercera. Si no hay moneda, utilizan secuencias preparadas y declaran su origen. | Cinco secuencias de tres símbolos, quince símbolos en total; todos los X entre 0 y 3. |
| 35–50 | Construyen tabla f(x), h(x) y diagrama de puntos. Calculan media, mediana y moda de su muestra. | Frecuencias que suman cinco y proporciones que suman uno. |
| 50–66 | Calculan rango, tabla de \(X_i-\bar X\), cuadrados, suma, \(s^2\) y \(s\). Revisan el ejemplo A. | Divisor escrito, unidades y redondeo explícitos. |
| 66–78 | Comparan A y B. Otro equipo audita su tabla y señala una diferencia comprobable. | Corrección de cálculo o explicación sustentada. |
| 78–85 | Entregan datos originales, gráfico, estadísticos y una comparación con otra muestra sin declarar sesgo de la moneda. | Producto común con trazabilidad. |
| 85–90 | Individualmente calculan media y mediana de A y explican por qué cinco corridas no prueban que la moneda sea injusta. | Respuesta personal con cálculo y límite. |

**Pregunta de transferencia.** Bajo un modelo con \(P(C)=0.5\) e independencia, \(E(X)=3(0.5)=1.5\). Se menciona como predicción condicional de un modelo; la distribución binomial y la comprobación de supuestos se desarrollan después. No sustituir el resultado observado de un equipo por el valor 1.5.

## Sesión 3. Auditoría de *Gatos y grandes números*

**Aprendizaje observable.** El equipo reproduce cálculos publicados, detecta una imposibilidad aritmética y reescribe una afirmación con el alcance que permiten los datos. La sesión utiliza el PDF como **objeto de auditoría**, no como prueba de la ley de grandes números.

### Problemas específicos que deben hacerse visibles

1. **Protocolos distintos.** La sesión 1 cuenta entradas al radio de 3 m durante un minuto. El PDF cuenta gatos observados en intervalos de dos minutos en varias zonas e intenta distinguir individuos. Las variables no son intercambiables ni sus datos se deben sumar.
2. **Medias reproducibles.** Para \(g=0,1,2,3\), las frecuencias publicadas son \((5,3,1,1)\), \((11,6,2,1)\) y \((18,8,3,1)\). Se obtienen \(\sum g f(g)=8,13,17\) y medias \(0.800,0.650,0.5667\), respectivamente.
3. **Varianzas mal etiquetadas.** Usando \(\sum g^2 f(g)=16,23,29\), se puede calcular \(v_n=\sum g^2f(g)/n-\bar g^2\): \(0.9600,0.7275,0.6456\). Con divisor \(n-1\), \(s^2=\frac{n}{n-1}v_n\): **1.0667, 0.7658, 0.6678**. El PDF denomina varianza muestral a valores próximos a los calculados con divisor \(n\); sus redondeos tampoco coinciden exactamente.
4. **Medias de otros equipos aritméticamente imposibles.** Si cada \(g_i\) es entero, \(\bar g=k/n\) para un entero \(k\). Con \(n=10\), 0.78 exigiría suma 7.8; con \(n=20\), 0.66 exigiría suma 13.2; con \(n=30\), 0.571 exigiría suma 17.13. Sin registros originales y explicación de otro denominador, esas cifras no se aceptan como promedios de los conteos declarados.
5. **Alcance de la inferencia.** Que una secuencia de tres medias disminuya no demuestra convergencia a una media poblacional conocida. La varianza de los **datos** puede crecer o bajar al añadir observaciones. Bajo muestreo independiente con varianza común finita, \(\operatorname{Var}(\bar X)=\sigma^2/n\) describe variabilidad del **estimador entre muestras**. Aquí el diseño por zonas, horarios e intervalos no acredita esos supuestos. El teorema central del límite tampoco se comprueba con una media por tamaño de muestra.

### Actividad ejecutable (90 minutos)

| Tiempo | Acción del equipo de cuatro | Evidencia o control |
|---|---|---|
| 0–8 | Individualmente escriben qué comprobarían ante la frase «demuestra convergencia a 0.57». | Cuatro preguntas iniciales. |
| 8–23 | A revisa protocolos; B reconstruye frecuencias y medias; C varianzas; D conclusiones y fuentes. | Hoja de cuatro columnas con nombres y hallazgos. |
| 23–40 | Verifican \(\sum f=n\), \(\sum g f\), \(\sum g^2f\) y las tres medias. | Cálculos completos de al menos un tamaño y revisión de los otros dos. |
| 40–57 | Calculan \(v_n\) y \(s^2\) para una tabla, comparan con el PDF e intercambian papeles para auditar. | Definición, divisor, valor y etiqueta concordantes. |
| 57–68 | Demuestran con \(k/n\) que tres medias de otros equipos no son posibles para los conteos declarados. | Argumento entero breve, sin presuponer intención o inventar registros. |
| 68–78 | Separan «lo que muestran estas tablas» de «lo que requeriría repetición o una justificación de diseño». | Dos frases reescritas sin causalidad ni convergencia demostrada. |
| 78–85 | Dictamen: afirmación, dato/cálculo, corrección y evidencia faltante. Cada integrante explica al menos una decisión. | Producto común con tres hallazgos verificables. |
| 85–90 | Individualmente escriben una conclusión válida, una inválida y un cálculo que justifica la distinción. | Salida personal. |

**Conclusión defendible de ejemplo:** «En las tres tablas publicadas, las medias calculadas son 0.800, 0.650 y 0.567 gatos observados por intervalo de dos minutos. Para generalizar a otros intervalos necesitamos los registros originales, un protocolo homogéneo y una justificación del muestreo». No afirmar que 0.567 es el valor real del campus.

## Criterios de evaluación formativa de la semana

En cada producto de equipo se revisan cuatro rasgos con evidencia visible: (1) variable y unidad definidas de forma que otra persona pueda repetir el registro; (2) operaciones y divisor correctos; (3) correspondencia entre datos crudos, tabla, gráfica y conclusión; (4) límites expresados sin atribuir a la muestra una propiedad de toda la población. Las salidas individuales verifican que nadie dependa sólo de los cálculos de su equipo. Para corregir, el docente devuelve **un error concreto y una acción de revisión**; no basta una etiqueta como «incompleto».

## Corrección del sistema de agentes para este curso

La versión anterior pasó de un resumen de materiales a las láminas sin una etapa que obligara a escribir definiciones, cálculos y consignas completas. Además, los agentes emitieron recomendaciones, pero no había una **puerta de aceptación** que impidiera publicar un guion insuficiente. Propongo esta secuencia de trabajo, aplicable a cada semana:

| Control | Pregunta que debe contestar | Producto exigido para pasar |
|---|---|---|
| **Agente Román** | ¿Qué aprendizaje importa esta semana y qué se aplaza? | Objetivos observables, decisión sobre ejemplos, límites de tiempo y vínculo con 1153001. |
| **Profesor de estadística** | ¿Son válidas definiciones, ecuaciones, operaciones, datos y supuestos? | Hoja de verificación numérica y semántica; puede bloquear una conclusión falsa. |
| **Agente pedagógico** | ¿Puede un equipo de cuatro ejecutar la consigna en tiempo real? | Secuencia minuto a minuto, papeles, insumos, alternativa accesible, producto, retroalimentación y salida individual. |
| **Comunicación de la ciencia** | ¿Distingue cada frase entre dato, modelo, inferencia y límite? | Texto comprensible para estudiantes; afirmaciones emparejadas con evidencia y alcance. |
| **Diseño educativo y prueba como estudiante** | ¿Se leen ecuaciones y se entiende la acción sin explicación adicional? | Revisión de proyección, móvil, densidad y recorrido completo de una actividad con números reales. |

**Regla de cierre.** Antes de producir diapositivas, elaborar una matriz por sesión con `concepto → definición → ecuación → ejemplo resuelto → decisión del estudiante → evidencia → criterio`. El agente estadístico recalcula todos los ejemplos y verifica unidades y supuestos. El pedagógico simula el tiempo de trabajo de cuatro personas; si el producto no cabe, reduce alcance, no tamaño de fuente. Román resuelve el conflicto de prioridad curricular. Comunicación revisa el texto final. La prueba como estudiante debe poder contestar: «qué hago, con qué datos, en qué orden, qué entrego y cómo sé si está bien». Si falla cualquiera de estas comprobaciones, el material sigue siendo borrador.

**Trazabilidad.** Registrar en cada semana tres etiquetas: `oficial 1153001`, `decisión docente` y `caso de práctica`. No trasladar porcentajes, equipos de tres o DOE del Word 1150018 al programa 1153001. Conservar el PDF original como fuente de afirmaciones a examinar, junto al dictamen de errores, para que nadie lo reutilice como evidencia depurada.

## Fuentes de trabajo

- Programa institucional de 1153001: https://dcbi.azc.uam.mx/media/Licenciaturas/Electronica/PlanesProgEstudio/TG/1153001.pdf
- Presentaciones de Clase 1 y Clase 2 adjuntas, empleadas como antecedentes docentes y reorganizadas.
- *Gatos y grandes números*, PDF adjunto, empleado exclusivamente como caso de auditoría en la tercera sesión.
