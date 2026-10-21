# Semana 1 · Control docente de los tres guiones

**UEA de referencia:** 1153001, Probabilidad y Estadística, UAM Azcapotzalco. **Público:** licenciatura en ingeniería. **Duración:** tres sesiones de 90 minutos. **Ruta temática:** el Word 1150018 es la **guía docente activa de Román para diez semanas**; la primera semana propone datos y descriptiva. Se contrasta con el programa oficial 1153001 y se desarrolla con sus notas *Probabilidad y Estadística*. Lederer complementa la relación entre datos y exploración. Las dos presentaciones SCIROM y el PDF *Gatos y grandes números* aportan actividades y casos. El encabezado y las reglas de evaluación del Word no se atribuyen al programa 1153001.

Los archivos TXT están redactados para pegarse como tres presentaciones separadas en Gamma: cada `---` separa una tarjeta. Las instrucciones visibles se dirigen al alumnado; esta guía conserva las soluciones, el control de tiempo y las decisiones docentes. No se generaron presentaciones en Gamma ni se consumieron créditos.

## Correspondencia y función de cada clase

| Sesión | Contenido 1153001 | Reorganización cognitiva | Evidencia |
|---|---|---|---|
| 1. Datos y medición | Introducción y estadística descriptiva; pregunta diagnóstica sobre azar | De «contar gatos» a dato, unidad, muestra y variable operacional | Protocolo, cinco registros, frecuencia, diagrama, media y límite; salida individual |
| 2. Monedas y estadísticos | Estadística descriptiva; variable aleatoria como anticipo | De quince lanzamientos a cinco unidades de análisis; de una media aislada a forma y dispersión | Secuencias, tabla, gráfico, x̄, mediana, moda, s², s; salida individual |
| 3. Auditoría del PDF | Descriptiva, lectura crítica e introducción a muestreo como pregunta | De «más datos prueban convergencia» a comprobar protocolos, cálculos, supuestos y alcance | Dictamen de tres afirmaciones con cálculo y evidencia faltante; salida individual |

**Decisión de alcance:** en la primera clase se activa la idea de azar, pero se formalizan dato, unidad, muestra, variable y frecuencia. En la segunda se calcula varianza muestral sin convertir cinco corridas en prueba de sesgo. En la tercera se auditan afirmaciones de convergencia sin desarrollar formalmente la ley de grandes números ni el TCL. El cálculo de probabilidades corresponde a la segunda semana de la guía; DOE, regresión, ANOVA y pruebas tampoco se enseñan en la primera.

Los rótulos «semana 1–11» del índice de las notas describen la organización del manuscrito y no establecen la planeación actual de diez semanas. La guía Word dirige esa planeación y empieza con descriptiva. La pregunta inicial de Román sobre azar se usa como diagnóstico, sin desplazar el contenido de la primera semana. En las notas hay formulaciones que requieren revisión antes de proyectarse: «muestra representativa» como definición, «individuo» equiparado con «valor estadístico» y un ejemplo de materias aprobadas cuyo texto no coincide con los datos. Los guiones usan definiciones corregidas y ejemplos calculados de nuevo.

## Materiales e implementación

- Clase 1: reloj, hoja de protocolo y tabla de cinco intervalos. Realizar observación únicamente desde un punto seguro y accesible sin interactuar con animales. Si no es viable, proporcionar `{2,3,1,4,2}` identificado como conjunto didáctico con duración de un minuto por intervalo. La observación de campo puede asignarse fuera del aula y traer los registros para la discusión; no presentarla como laboratorio.
- Clase 2: una moneda por equipo o secuencias preparadas, tabla de cinco corridas y calculadora opcional. Cada corrida contiene tres símbolos C/S.
- Clase 3: extracto de las tres tablas del PDF, sus afirmaciones sobre convergencia y la tabla de equipos externos. Disponer de una hoja de cuatro columnas para el dictamen. El PDF completo puede consultarse, pero las cifras cuestionadas deben marcarse como afirmaciones a auditar.

## Respuestas verificadas

### Clase 1

La primera clase plantea «¿qué entiendes por azar, posibilidad y probabilidad?» como diagnóstico. El espacio muestral y el cálculo de probabilidades se reservan para la segunda semana de la guía Word. Ninguna respuesta intuitiva del diagnóstico se califica como modelo ya demostrado.

Para `{2,3,1,4,2}`, la suma es 12, `f(1)=1`, `f(2)=2`, `f(3)=1`, `f(4)=1`, `Σf=5` y `x̄=12/5=2.4` entradas por intervalo de un minuto. La conclusión aceptable describe **entradas**, no individuos distintos ni una tasa poblacional. Cinco intervalos consecutivos pueden ser dependientes; no aplicar un intervalo de confianza sin revisar el diseño.

### Clase 2

Para `A={0,1,1,3,3}`, `x̄=8/5=1.6`, mediana 1, modas 1 y 3, rango 3. Desviaciones cuadradas: `2.56,0.36,0.36,1.96,1.96`; suma 7.20. `s²=7.20/4=1.80`, `s=√1.80≈1.342`. Para `B={1,1,2,2,2}`, suma 8, media 1.6 y suma de cuadrados 1.20, así que `s²=1.20/4=0.30`. Una corrida no puede contener diez caras. El valor teórico esperado bajo una moneda justa se calcula al desarrollar el modelo en la semana 2.

### Clase 3

| n | `f(0),f(1),f(2),f(3)` | `Σgf` | `Σg²f` | `ḡ` | `vₙ` divisor n | `s²` divisor n−1 |
|---:|---|---:|---:|---:|---:|---:|
| 10 | 5,3,1,1 | 8 | 16 | 0.8000 | 0.9600 | 1.0667 |
| 20 | 11,6,2,1 | 13 | 23 | 0.6500 | 0.7275 | 0.7658 |
| 30 | 18,8,3,1 | 17 | 29 | 0.5667 | 0.6456 | 0.6678 |

Reconstrucción: `vₙ=(Σg²f)/n−ḡ²` y `s²=[n/(n−1)]vₙ`. El PDF llama «varianza muestral» a valores próximos a `vₙ`, con redondeos que tampoco reproducen exactamente la operación. Las medias externas `0.78` con `n=10`, `0.66` con `n=20` y `0.571` con `n=30` implican sumas no enteras de conteos; no aceptarlas como observaciones verificadas. Esto permite señalar una incompatibilidad aritmética, no atribuir intención ni inventar registros.

## Actividad y evaluación de equipos de cuatro

La meta compartida y el registro común producen interdependencia. Los papeles de protocolo, ejecución, registro y auditoría son distintos; rotarlos entre clases evita una división permanente entre quien calcula y quien solo presenta. Cada persona predice antes del trabajo grupal y entrega una respuesta propia al final. El equipo revisor debe señalar una discrepancia concreta y el equipo autor debe corregirla o responder con cálculo.

Usar cuatro criterios formativos de 0 a 2 puntos por producto: **variable/unidad/protocolo** (0 ausente, 1 incompleto, 2 reproducible); **cálculo** (0 incorrecto, 1 correcto con pasos faltantes, 2 reconstruible); **coherencia de representaciones** (0 discrepancia, 1 revisión parcial, 2 datos, tabla y gráfico coinciden); **alcance** (0 generaliza sin soporte, 1 señala un límite vago, 2 expresa una conclusión delimitada y el dato faltante). Total máximo 8; es una herramienta de retroalimentación de estas actividades, no una ponderación oficial ni calificación final del curso.

Devolver un error concreto con acción: «f(2)=2, pero pusieron un solo punto sobre 2; corrijan gráfico», o «dividieron entre 5 y escribieron s²; revisen divisor y etiqueta». Revisar después la corrección, no solo asignar puntos.

## Instrucciones visuales para producirlas en Gamma

Mantener tres decks separados, 32/34/34 tarjetas y formato 16:9. La clase 1 necesita un diagrama exacto de Ω y A, una tabla de cinco intervalos y un diagrama de puntos; la clase 2 requiere secuencias de C/S, tabla de frecuencias, diagramas de A y B y desarrollo de cuadrados; la clase 3 requiere tablas numéricas editables, comparación de protocolos, dos columnas de divisores y matriz de dictamen. Usar objetos nativos para datos y fórmulas. Reservar imágenes contextuales para el escenario de observación o lanzamiento solo si ayudan a comprender qué se cuenta; no generar fotografías como sustituto de tablas.

La progresión visible en cada deck es `predecir → confrontar → construir → formalizar → auditar → transferir`. Diferenciar con etiquetas constantes dato observado, modelo supuesto y afirmación por verificar. Evitar notas de profesor en tarjetas, colores que codifiquen juicios sin leyenda y tipografía reducida. Antes de publicar un deck en Gamma, revisar cada tarjeta como estudiante y exportar para comprobar fórmulas, símbolos y cortes de texto. Estos guiones todavía son texto plano, no presentaciones verificadas visualmente.

## Dictamen de agentes aplicado

| Lente | Decisión comprobable |
|---|---|
| Román | Conservar gatos y monedas como situaciones próximas; comenzar por probabilidad y medición; mantener tres preguntas distintas y aplazar inferencia formal. |
| Estadística | Verificar `3/8`, medias, `s²`, dominio 0–3 y las tres tablas del PDF; bloquear una demostración falsa de convergencia. |
| Pedagogía | Tres sesiones con tiempos completos de 90 min, equipo de cuatro, predicción personal, control intermedio, auditoría y salida individual. |
| Comunicación | Separar dato, modelo y conclusión; atribuir explícitamente el PDF y presentar sus cifras inconsistentes como objeto de revisión. |
| Diseño educativo | Guiones de 32–34 tarjetas, sin alertas automáticas de densidad ni frases docentes visibles; la revisión visual queda pendiente de generar los decks. |

## Fuentes

- Programa institucional 1153001: https://dcbi.azc.uam.mx/media/Licenciaturas/Electronica/PlanesProgEstudio/TG/1153001.pdf
- Word `Programa_1150018_Temario_actualizado_pedagogico_10_semanas(1).docx`: guía docente de Román, semana 1 «datos y descriptiva»; su clave no identifica el programa oficial de 1153001.
- Mora Gutiérrez, R. A., et al. *Probabilidad y Estadística: notas de curso (con ejemplos y ejercicios)*, PDF adjunto `LibroPyE (1).pdf`: §§1.1.1–1.1.3 para estas clases; §§2.2–2.3 como continuidad.
- Lederer, J. (2025). *A First Course in Statistical Learning: With Data Examples and Python Code*. Springer, DOI 10.1007/978-3-031-30276-3: §§1.2–1.3 y 2.2–2.3.
- `Clase-1-or-Introduccion-a-la-estadistica-y-la-probabilidad-or-SCIROM.pptx` (adjunto).
- `Clase-2-or-Estadisticos-con-lanzamientos-de-moneda-or-SCIROM.pptx` (adjunto).
- `Gatos-y-grandes-numeros (1).pdf` (adjunto, caso de auditoría).
