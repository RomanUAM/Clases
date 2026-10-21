# Análisis y Diseño de Algoritmos
## Presentación del curso y carta temática · 26O
UEA 1151040 · Grupo CSI82 · UAM Azcapotzalco
Profesor: Román Anselmo Mora Gutiérrez

---

# Tu ruta de trabajo
Al terminar sabrás justificar no sólo que un algoritmo funciona, sino cuánto cuesta, cuándo conviene y qué alternativa resulta mejor.

Esta presentación reúne la carta temática del curso: propósito, diagnóstico, temario, forma de trabajo, prácticas extraaula, calendario y evaluación.

---

# Ficha curricular y logística
- 9 créditos · UEA obligatoria
- H.TEOR. 4.5 · H.PRAC. 0.0
- Seriación: 1152001, 1151041 y 1112033
- Lunes, miércoles y viernes · 17:30–19:00
- Salón G208 · 30 sesiones planeadas en 10 semanas

H.PRAC. 0.0 significa que no existe un bloque formal de laboratorio. Las prácticas se realizan fuera del aula y se discuten o defienden en clase.

---

# Objetivos oficiales
Al final de la UEA podrás:
1. Formular recurrencias que representen la complejidad de un algoritmo.
2. Calcular complejidad temporal y espacial.
3. Aplicar técnicas de diseño y verificar que funcionan.
4. Analizar ventajas y desventajas de cada técnica.
5. Evaluar algoritmos distintos para un mismo problema.

---

# Diagnóstico inicial · pensar antes de programar
Responde individualmente y después contrasta en pareja:
1. Propón tres formas de calcular números primos. ¿Cuál usarías y por qué?
2. Calcula la suma de cuadrados del 1 al 100 en MATLAB de dos formas. ¿Cuál es mejor y con qué criterio?
3. Para una solución que “funciona”, ¿qué evidencia necesitas para afirmar que es correcta y eficiente?

No tiene calificación. Sirve para ajustar apoyos y formar equipos complementarios.

---

# Temario oficial · fundamentos
1. Análisis de correctitud y de complejidad.
2. Recursividad y ecuaciones de recurrencia.
3. Algoritmos de divide y vencerás.
4. Algoritmos de búsqueda con retroceso.

Pregunta guía: ¿cómo pasamos de “corre” a “puedo demostrar por qué funciona y cuánto cuesta”?

---

# Temario oficial · estrategias
5. Algoritmos de programación dinámica.
6. Algoritmos de búsqueda local.
7. Algoritmos glotones.
8. Problemas NP completos.

Pregunta guía: ¿qué cambia cuando buscamos una solución exacta, aproximada o viable dentro de recursos limitados?

---

# Forma de trabajo
Las prácticas se resuelven fuera del aula y se entregan como reporte técnico breve o artículo aplicado. En clase compararemos soluciones, errores, cotas y decisiones.

- Parejas para prácticas y proyecto; diagnóstico y práctica de cotas, individuales.
- Interdependencia positiva: una solución común exige aportes complementarios.
- Responsabilidad individual: bitácora, código identificable y defensa breve.
- Heterogeneidad: combinar fortalezas matemáticas, de programación y comunicación.
- Interacción promotora: explicar, cuestionar y revisar antes de entregar.

---

# Portafolio de prácticas extraaula · 40%
- P1 individual: correctitud, operación básica y cálculo de cotas.
- P2 pareja: recurrencias y contraste de tres estrategias para primos.
- P3 pareja: divide y vencerás con medición experimental.
- P4 pareja: búsqueda con retroceso y poda.
- P5 pareja: programación dinámica y reconstrucción de solución.
- P6 pareja: búsqueda local frente a algoritmo glotón.
- P7 pareja: reducción, complejidad y límites en un problema NP completo.

El conjunto vale 40%; cada entrega se juzga con una rúbrica común y no se asignan pesos individuales arbitrarios.

---

# Qué debe contener cada reporte
1. Problema y pregunta de análisis.
2. Estrategia, supuestos y pseudocódigo.
3. Correctitud o argumento de validez.
4. Complejidad temporal y espacial.
5. Experimento reproducible, datos y código.
6. Resultados, límites y comparación.
7. Contribuciones individuales y fuentes.

La evidencia debe permitir repetir el análisis; una captura aislada no basta.

---

# Proyecto integrador · 15%
En pareja, elegir un problema y comparar al menos dos estrategias de diseño.

Hitos: formulación y datos → prototipo → análisis teórico → experimento → reporte → defensa.

Criterios: corrección, elección razonada, complejidad, evidencia reproducible, interpretación, comunicación y respuesta individual durante la defensa.

---

# Evaluación del curso
Propuesta docente compatible con el programa:
- Portafolio de prácticas extraaula: 40%
- Dos evaluaciones periódicas mediante casos de estudio: 30% (15% + 15%)
- Tareas individuales: 15%
- Proyecto integrador y defensa: 15%

Total: 100%. Las evaluaciones periódicas combinan preguntas conceptuales, resolución de problemas y elaboración o análisis de programas.

---

# Escala y acreditación
- 9.0–10: MB
- 7.5–<9.0: B
- 6.0–<7.5: S
- <6.0: NA

Con promedio acumulado de 6.0 o más no se presenta evaluación terminal. La evaluación de recuperación es institucional, admite recuperación y no requiere inscripción previa; no debe confundirse con las actividades ordinarias del curso.

---

# Calendario · semanas 1 a 5
| Semana | Aprendizaje central | Trabajo extraaula y entrega |
|---|---|---|
| 1 | Correctitud y complejidad | Diagnóstico; asignación P1 |
| 2 | Cotas y análisis espacial | Entrega y discusión P1; asignación P2 |
| 3 | Recurrencias | Entrega/discusión P2 |
| 4 | Divide y vencerás | Asignación P3; evaluación periódica 1 |
| 5 | Retroceso y poda | Entrega/discusión P3; asignación P4 |

---

# Calendario · semanas 6 a 10
| Semana | Aprendizaje central | Trabajo extraaula y entrega |
|---|---|---|
| 6 | Programación dinámica | Entrega P4; asignación P5 |
| 7 | Búsqueda local | Entrega P5; asignación P6; hito de proyecto |
| 8 | Algoritmos glotones | Entrega/discusión P6 |
| 9 | NP completos | Asignación y entrega P7; evaluación periódica 2 |
| 10 | Integración y transferencia | Entrega y defensa del proyecto |

---

# Tecnología con propósito
Usaremos MATLAB, Python u otra herramienta acordada para implementar, medir y reproducir; no para sustituir la explicación.

Todo resultado computacional debe acompañarse de condiciones de prueba, tamaño de entrada, métrica, código y lectura crítica. El uso de IA debe declararse y verificarse: quien entrega responde por la corrección del contenido.

---

# Bibliografía y acompañamiento
Base: Baase y Van Gelder; Dasgupta, Papadimitriou y Vazirani; Kleinberg y Tardos; Parberry y Gasarch; Roberts; Sedgewick.

El programa exige revisar al menos un texto técnico, científico o de divulgación en inglés y favorece la presentación oral de trabajos.

Programa oficial: https://dcbi.azc.uam.mx/media/Licenciaturas/Computacion/PlanesProgEstudio/TBP/1151040.pdf

Trae preguntas, intentos y errores a clase: son material de aprendizaje.
