# Ana Laura: decisiones de inversión mediante anualidades, gradientes y flujos netos

**Ingeniería Económica · Material de clase**  
**Horizonte:** años 0 a 4 · **Tasa nominal de descuento:** 12% anual · **Capital disponible:** 300 unidades monetarias.

**Objetivo de aprendizaje:** Identificar las estructuras de los ingresos y egresos, calcular su valor presente por separado y verificar que el resultado coincide con el método de flujo neto.

---

## 1. Pregunta detonadora

**Si dos proyectos generan ingresos, ¿es suficiente comparar cuánto dinero entra para decidir cuál conviene?**

Antes de calcular debemos reconocer: el momento de cada cobro y pago; la estructura de crecimiento; el valor del dinero en el tiempo; y la diferencia entre capital disponible e inversión inicial.

---

## 2. Datos de los proyectos

| Año t | Ingreso A | Egreso A | Ingreso B | Egreso B |
|---:|---:|---:|---:|---:|
| 0 | 100 | 50 | 35.5 | 5 |
| 1 | 120 | 50 | 32.6 | 5 |
| 2 | 144 | 60 | 29.12 | 5 |
| 3 | 172.8 | 40 | 24.944 | 7 |
| 4 | 207.36 | 20 | 19.9328 | 9 |

**Convención:** Ingreso (+), egreso (−). La fecha focal es el año 0. Los flujos del año 0 no se descuentan.

---

## 3. Herramientas matemáticas

**Valor presente de un flujo en el año t:**

$$VP_t=\frac{F_t}{(1+i)^t}$$

**Anualidad uniforme:** pagos o cobros constantes en periodos igualmente espaciados. **Gradiente aritmético:** incrementos absolutos constantes. **Gradiente geométrico:** razón constante entre términos sucesivos.

**Identidad de equivalencia:**

$$\sum_{t=0}^n\frac{I_t-E_t}{(1+i)^t}=\sum_{t=0}^n\frac{I_t}{(1+i)^t}-\sum_{t=0}^n\frac{E_t}{(1+i)^t}$$

La identidad solo compara las mismas fechas y los mismos flujos.

---

## 4. Proyecto A: reconocer la estructura de los ingresos

Ingresos: **100, 120, 144, 172.8, 207.36**.

Las razones consecutivas son constantes:

$$\frac{120}{100}=\frac{144}{120}=\frac{172.8}{144}=\frac{207.36}{172.8}=1.20$$

Por tanto, los ingresos son una **serie geométrica creciente al 20% anual**, con término inicial en el año 0:

$$I_{A,t}=100(1.20)^t,\qquad t=0,1,2,3,4$$

**Discusión:** La tasa de crecimiento de ingresos (20%) no es la tasa de descuento (12%).

---

## 5. Proyecto A: valor presente de los ingresos

$$VP(I_A)=\sum_{t=0}^4\frac{100(1.20)^t}{(1.12)^t}$$

$$=100\sum_{t=0}^4\left(\frac{1.20}{1.12}\right)^t$$

Usando la suma geométrica $\sum_{t=0}^{N-1}r^t=(r^N-1)/(r-1)$:

$$VP(I_A)=100\frac{(1.20/1.12)^5-1}{(1.20/1.12)-1}$$

$$\boxed{VP(I_A)=576.7154\approx576.72}$$

---

## 6. Proyecto A: reconocer y descontar los egresos

Egresos: **50, 50, 60, 40, 20**.

No forman una anualidad ni un gradiente único: sus diferencias son **0, +10, −20, −20**. Existe una parte constante (años 0 y 1) y un tramo con decremento aritmético de 20 (años 2 a 4), pero la serie completa requiere una descomposición por tramos.

La vía más transparente en este ejercicio es descontar cada término:

$$VP(E_A)=50+\frac{50}{1.12}+\frac{60}{1.12^2}+\frac{40}{1.12^3}+\frac{20}{1.12^4}$$

$$\boxed{VP(E_A)=183.6561\approx183.66}$$

**Valor presente por componentes:**

$$VP_A=VP(I_A)-VP(E_A)=576.7154-183.6561=\boxed{393.0594}$$

---

## 7. Proyecto B: analizar las diferencias de ingresos

Ingresos: **35.5, 32.6, 29.12, 24.944, 19.9328**.

Variación año a año: **−2.9, −3.48, −4.176, −5.0112**.

Los ingresos no forman una progresión geométrica directa: **sus disminuciones** sí crecen en razón constante de 1.20.

$$\frac{3.48}{2.9}=\frac{4.176}{3.48}=\frac{5.0112}{4.176}=1.20$$

$$I_{B,t}=35.5-2.9\sum_{k=0}^{t-1}(1.20)^k$$

$$=35.5-2.9\frac{1.20^t-1}{0.20}=\boxed{50-14.5(1.20)^t}$$

En $t=0$ la suma vacía vale cero.

---

## 8. Proyecto B: valor presente de los ingresos

La forma $I_{B,t}=50-14.5(1.20)^t$ permite reconocer una **serie uniforme de 50** menos una **serie geométrica creciente**.

$$VP(I_B)=50\sum_{t=0}^4\frac{1}{(1.12)^t}-14.5\sum_{t=0}^4\left(\frac{1.20}{1.12}\right)^t$$

$$\boxed{VP(I_B)=118.2437\approx118.24}$$

**Precisión:** La serie uniforme incluye el año 0; no debe aplicarse sin ajuste la fórmula de una anualidad ordinaria que empieza en el año 1.

---

## 9. Proyecto B: anualidad y gradiente en los egresos

Egresos: **5, 5, 5, 7, 9**.

Se pueden descomponer como:

- Serie uniforme de **5** en los años 0, 1, 2, 3 y 4.
- Gradiente aritmético **diferido**: pagos adicionales de **2** en el año 3 y **4** en el año 4.

$$E_{B,t}=5+G_t,\quad G_t=\begin{cases}0,&t=0,1,2\\2(t-2),&t=3,4\end{cases}$$

$$VP(E_B)=5\sum_{t=0}^4\frac{1}{1.12^t}+\frac{2}{1.12^3}+\frac{4}{1.12^4}$$

$$\boxed{VP(E_B)=24.1524\approx24.15}$$

$$VP_B=118.2437-24.1524=\boxed{94.0914}$$

---

## 10. Método alternativo: formar los flujos netos

**Flujo neto:** $FN_t=I_t-E_t$.

| Año t | Flujo neto A | Flujo neto B |
|---:|---:|---:|
| 0 | 50 | 30.5 |
| 1 | 70 | 27.6 |
| 2 | 84 | 24.12 |
| 3 | 132.8 | 17.944 |
| 4 | 187.36 | 10.9328 |

Al restar dos series con estructuras diferentes, el flujo neto **no tiene por qué conservar un gradiente simple**.

---

## 11. Valor presente a partir del flujo neto

**Proyecto A:**

$$VP_A=50+\frac{70}{1.12}+\frac{84}{1.12^2}+\frac{132.8}{1.12^3}+\frac{187.36}{1.12^4}$$

$$\boxed{VP_A=393.0594\approx393.06}$$

**Proyecto B:**

$$VP_B=30.5+\frac{27.6}{1.12}+\frac{24.12}{1.12^2}+\frac{17.944}{1.12^3}+\frac{10.9328}{1.12^4}$$

$$\boxed{VP_B=94.0914\approx94.09}$$

---

## 12. Comparación de los procedimientos

| Indicador | Proyecto A | Proyecto B |
|---|---:|---:|
| VP de ingresos | 576.7154 | 118.2437 |
| VP de egresos | 183.6561 | 24.1524 |
| VP por componentes | **393.0594** | **94.0914** |
| VP por flujos netos | **393.0594** | **94.0914** |
| Diferencia entre procedimientos | 0 | 0 |

$$VP(\text{ingresos})-VP(\text{egresos})=VP(\text{flujos netos})$$

La equivalencia proviene de la distributividad y la linealidad; no depende del tipo de gradiente.

---

## 13. La decisión: ¿qué significa que Ana Laura tenga 300?

**Interpretación 1: las 300 unidades son un desembolso inicial adicional en ambos proyectos (no incluido en la tabla).**

$$VPN_A=393.0594-300=\boxed{93.0594}$$

$$VPN_B=94.0914-300=\boxed{-205.9086}$$

Bajo esta hipótesis, conviene A. **No sumar ni restar los 300 dos veces.**

**Interpretación 2: 300 es solo un presupuesto disponible.** No basta para calcular VPN: se necesita conocer el costo de inversión inicial de cada proyecto. Los valores de 393.06 y 94.09 son valores presentes de flujos netos **antes de cualquier inversión inicial adicional**.

---

## 14. Inflación y tasa de interés real

Si la inflación anual prevista es del 10% y la tasa nominal es 12%, la relación de Fisher da:

$$i_{real}=\frac{1+i_{nominal}}{1+\pi}-1=\frac{1.12}{1.10}-1$$

$$\boxed{i_{real}=0.0181818\approx1.82\%}$$

**Importante:** 1.82% es la tasa real equivalente de la tasa nominal de descuento, **no** la tasa interna de retorno de cada proyecto ni su ganancia monetaria.

Para trabajar en términos reales se deben deflactar adecuadamente los flujos nominales y descontarlos con la tasa real. Descontar los mismos flujos nominales con ambas tasas sin convertirlos sería inconsistente. Los valores presentes nominalmente descontados ya están expresados en unidades del año 0.

---

## 15. Preguntas de análisis y cierre

1. ¿Por qué ingresos crecientes no garantizan una inversión conveniente?
2. ¿Cuál es la diferencia entre un gradiente geométrico en los niveles y un gradiente geométrico en las diferencias?
3. ¿Por qué los egresos B se pueden modelar como una anualidad más un gradiente aritmético diferido?
4. ¿Por qué el método por componentes y el de flujos netos son equivalentes?
5. ¿Qué cambia si los 300 son presupuesto disponible y no inversión inicial?
6. ¿Qué errores aparecen al confundir la tasa de inflación, la tasa de descuento y el crecimiento de ingresos?

**Entregables del estudiante:** identificación de estructuras con justificación; diagramas de ingresos, egresos y flujos netos; cálculos en ambos métodos; verificación de equivalencia; recomendación bajo hipótesis explícitas.

**Mensaje de cierre:** identificar la estructura permite simplificar el cálculo, pero la equivalencia financiera se sostiene incluso cuando el flujo neto no tiene una estructura reconocible.
