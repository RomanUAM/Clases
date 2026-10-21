# Ingeniería económica: reconocimiento de estructuras y equivalencia de flujos
Material para importar a Gamma · Clase con problemas resueltos y ejercicios de aplicación

---

## 1. Pregunta detonadora
**¿Por qué dos procedimientos aparentemente distintos —analizar ingresos y egresos por separado o trabajar con el flujo neto— deben conducir al mismo valor equivalente?**

Ruta: representar el tiempo → reconocer estructuras → deducir fórmulas → elegir fecha focal → verificar con tabla de saldos → justificar decisión.

Convenciones: una tasa corresponde siempre a un periodo definido; pagos al final de cada periodo salvo que se indique otra cosa; nunca se confunde capital disponible con inversión efectivamente requerida.

---

## 2. Herramientas matemáticas
- Interés compuesto: $F=P(1+i)^n$; descuento: $P=F/(1+i)^n$.
- Valor equivalente de flujos netos: $V_0=\sum_{t=0}^{N}(I_t-E_t)/(1+i)^t$.
- Linealidad: $V_0=\sum I_t/(1+i)^t-\sum E_t/(1+i)^t$.
- Anualidad vencida: $P=A\frac{1-(1+i)^{-n}}{i}$; valor futuro: $F=A\frac{(1+i)^n-1}{i}$.
- Anualidad anticipada (primer pago en $t=0$, total $n$ pagos): $F=A\frac{(1+i)^n-1}{i}(1+i)$ medido al final del periodo $n$.
- Gradiente aritmético: incremento fijo $G$ por periodo. Gradiente geométrico: razón constante $1+g$ entre términos.
- Saldo: $S_t=(1+i)S_{t-1}+D_t-R_t$ (depósitos $D_t$ y retiros $R_t$ al final de cada periodo).

---

## 3. Ana Laura: datos de los dos proyectos
Tasa anual: $i=12\%$. Horizonte: años 0 a 4. Capital disponible: 300 unidades, sin costo inicial adicional especificado.

| Año | Ingreso A | Egreso A | Ingreso B | Egreso B |
|---:|---:|---:|---:|---:|
|0|100|50|35.5|5|
|1|120|50|32.6|5|
|2|144|60|29.12|5|
|3|172.8|40|24.944|7|
|4|207.36|20|19.9328|9|

**Consigna:** primero ingresos, después egresos, y solamente al final flujo neto.

---

## 4. Proyecto A: ingresos y egresos separados
Los ingresos siguen un gradiente geométrico: $I_t=100(1.2)^t$, para $0\leq t\leq4$.

$$VP_{I,A}=100\sum_{t=0}^{4}\left(\frac{1.2}{1.12}\right)^t\approx576.72$$

Los egresos $50,50,60,40,20$ **no forman un único gradiente**. Pueden reconocerse tramos, pero el descuento término a término evita imponer una estructura artificial:

$$VP_{E,A}=50+\frac{50}{1.12}+\frac{60}{1.12^2}+\frac{40}{1.12^3}+\frac{20}{1.12^4}\approx183.66$$

$$VP_A=VP_{I,A}-VP_{E,A}\approx393.06$$

---

## 5. Proyecto B: estructura de segundo nivel
Los ingresos $35.5,32.6,29.12,24.944,19.9328$ muestran diferencias $-2.9,-3.48,-4.176,-5.0112$; **las diferencias**, no los ingresos, tienen razón geométrica 1.2.

$$I_t=35.5-2.9\frac{1.2^t-1}{0.2}=50-14.5(1.2)^t$$

Esto equivale a una sucesión uniforme de 50 menos una sucesión geométrica creciente.

$$VP_{I,B}=\sum_{t=0}^4\frac{50-14.5(1.2)^t}{1.12^t}\approx118.24$$

Los egresos $5,5,5,7,9$ son una base de 5 por cinco fechas, más incrementos diferidos de 2 y 4 en los años 3 y 4:

$$VP_{E,B}=5\sum_{t=0}^4(1.12)^{-t}+\frac{2}{1.12^3}+\frac{4}{1.12^4}\approx24.15$$

$$VP_B\approx94.09$$

---

## 6. Ana Laura: método del flujo neto y comparación
| Año | Flujo A = ingreso − egreso | Flujo B = ingreso − egreso |
|---:|---:|---:|
|0|50|30.5|
|1|70|27.6|
|2|84|24.12|
|3|132.8|17.944|
|4|187.36|10.9328|

$$VP_A=\sum_{t=0}^4\frac{FN_{A,t}}{1.12^t}\approx393.06;\quad VP_B=\sum_{t=0}^4\frac{FN_{B,t}}{1.12^t}\approx94.09$$

El resultado coincide con la separación de ingresos y egresos por la propiedad distributiva. **Advertencia:** no restar automáticamente los 300 a los dos valores presentes: el problema dice «capital disponible», no que sea el costo inicial requerido de ambos proyectos. Si ambos exigieran expresamente una inversión adicional de 300: $VPN_A\approx93.06$, $VPN_B\approx-205.91$.

Tasa real equivalente con inflación de 10%: $i_r=1.12/1.10-1\approx1.8182\%$. No descontar dos veces la inflación.

---

## 7. Ahorro para la educación: depósitos y fecha focal
Depósitos anuales de 2,000 desde la edad 2 hasta la 17, inclusive (16 pagos), con retiro al cumplir 18 años e interés del 12% anual. El primer depósito capitaliza 16 años, el último uno.

$$F_{18}=2000\sum_{k=1}^{16}(1.12)^k=2000(1.12)\frac{(1.12)^{16}-1}{0.12}=95,767.35$$

Se aportan $16(2000)=32,000$ y se acumulan intereses de $63,767.35$. La tabla que capitaliza *un único depósito* no es la misma que la tabla del *saldo acumulado con depósitos sucesivos*.

---

## 8. Segunda tabla del ahorro: anualidad vencida y recurrencia
En la nueva tabla hay 17 aportaciones ubicadas al final de los periodos $t=1,\dots,17$ y ninguna en $t=0$. Si cada aportación es de 2,000:

$$S_t=1.12S_{t-1}+2000,\quad S_0=0$$
$$S_{17}=2000\frac{1.12^{17}-1}{0.12}=97,767.35$$

La última fila de la tabla pegada registra **2,001**, no 2,000; por eso el saldo que correspondería al dato tal como está escrito es **97,768.35**. El resultado mostrado en esa misma tabla, **97,767.35**, supone 2,000 en el periodo 17. Esta tabla no contradice la anterior: desplaza la fecha focal y/o incluye una aportación adicional. Identificar las fechas es indispensable.

---

## 9. Valor presente de una anualidad de 5,000
Pagos de 5,000 al final de los años $1,2,3,4$; tasa $10\%$ anual.

$$P=\sum_{t=1}^4\frac{5000}{1.10^t}=5000\frac{1-(1.10)^{-4}}{0.10}=15,849.33$$

Factores individuales: $4545.45$, $4132.23$, $3756.57$, $3415.07$. Atención: el año cero sirve como **fecha focal**, pero **no hay pago de 5,000 en $t=0$**.

Pregunta: ¿por qué se suma un pago *menos* al situar la anualidad vencida en $t=1$ que si existiera un pago adicional en $t=0$?

---

## 10. Cuenta con retiros: detectar contradicciones antes de calcular
Enunciado escrito: «Deposito 15,800 pesos en una cuenta que ofrece 10% de interés; si solo saco 1,500, ¿cuándo dejo la cuenta en cero?».

**Contradicción del material:** la tabla usa retiros de **1,580.90**, no de 1,500; el depósito inicial aparece en el año 1 y los retiros empiezan en el año 2.

Si el primer retiro es un año después del depósito y los retiros son 1,500 cada año, el interés anual inicial es $1,580. El retiro es menor que los intereses: **la cuenta no se agota; aumenta**.

Si los retiros son de 1,580.90, exceden los intereses iniciales en $0.90 y el saldo disminuye muy lentamente. El saldo obedece, contando $k$ retiros desde el depósito:

$$S_k=15800(1.10)^k-1580.90\frac{(1.10)^k-1}{0.10}$$

La raíz continua está cerca de $k=78.39$: se requiere **un último retiro parcial durante el año del retiro número 79**, si todos los anteriores son de 1,580.90. Es importante no confundir ambos escenarios.

---

## 11. Amortización: anualidad más gradiente aritmético
Préstamo de 500,000, interés del 10%, anualidad base de 50,000, incremento adicional fijo de 20,000 desde el segundo pago.

$$P_t=50,000+20,000(t-1),\quad S_t=1.10S_{t-1}-P_t$$

Saldos al final de años 1 a 7: 500,000; 480,000; 438,000; 371,800; 278,980; 156,878; 2,565.80.

En año 8 se liquida con **2,822.38**, en lugar del pago programado de 190,000. Interpretar saldo negativo como sobrepago programado, no como deuda negativa real.

---

## 12. Amortización: incrementos que crecen 40%
Con el mismo préstamo y tasa, los pagos adicionales registrados son 0, 20,000, 48,000, 87,200, 142,080, 218,912.

Los **incrementos** del adicional son 20,000; 28,000; 39,200; 54,880; 76,832, razón 1.4.

$$G_t=20,000\sum_{k=0}^{t-2}(1.4)^k=50,000(1.4^{t-1}-1)$$
$$P_t=50,000+G_t=50,000(1.4)^{t-1}$$

Saldo después del año 5: 177,300; intereses en año 6: 17,730. Se liquida con **195,030** en el año 6 en vez del pago programado de 268,912.

---

## 13. Ejercicio propuesto: Camilo (sin resolver)
Camilo deposita 2,500 al final de cada año durante 15 años; realiza depósitos adicionales de 3,000 en los años 3, 6, 9 y 12, y retiros de 500 al final de los años 3 al 7 inclusive. Tasa anual del 16%. ¿Cuál es el saldo al final del año 16?

Antes de resolver: dibujar el diagrama de flujos y anotar explícitamente que depósitos y retiros coincidentes en el año 3 se contabilizan en la misma fecha.

Modelo de verificación, **sin evaluar numéricamente**:

$$F_{16}=2500\sum_{t=1}^{15}(1.16)^{16-t}+3000\sum_{t\in\{3,6,9,12\}}(1.16)^{16-t}-500\sum_{t=3}^{7}(1.16)^{16-t}$$

Contrastar método de ingresos/egresos con recurrencia del saldo.

---

## 14. Ejercicio propuesto: fábrica (datos)
| Semana | Ingresos | Egresos |
|---:|---:|---:|
|0|900|0|
|1|9900|800|
|2|9900|1120|
|3|9900|1248|
|4|9900|1299.2|
|5|9900|1319.68|
|6|9900|1327.872|
|7|9900|1331.1488|
|8|9900|1332.45952|
|9|9800|1332.98381|
|10|9700|1333.19352|
|11|9600|1333.27741|
|12|9500|1333.31096|
|13|9500|1333.32439|
|14|9500|1333.32975|
|15|9500|1333.3319|
|16|9500|1333.33276|
|17|9500|1333.3331|
|18|0|1333.33324|

Texto original: «considerando una inflación del 4 [presumiblemente %], se ofrece una compra por 25,000». **Faltan datos para valorar financieramente la compra**: periodicidad de la inflación, tasa de rendimiento o descuento, fecha de la oferta, y si se trata de comprar la fábrica o de adquirir su producción. No asumir estos elementos silenciosamente.

---

## 15. Fábrica: reconocer estructuras antes de valorar
- Ingresos: $900$ en semana 0; anualidad por tramos de $9900$ en semanas 1–8; gradiente aritmético descendente de 100 en semanas 9–12; $9500$ en semanas 12–17; cero en semana 18. **Hay coincidencia en la semana 12 entre el final del gradiente y el inicio del tramo constante; evitar doble conteo.**
- Egresos: $800,1120,1248,1299.2,\dots$; sus incrementos $320,128,51.2,\dots$ forman una sucesión geométrica con razón $0.4$.

Para semanas $t\ge1$:

$$E_t=800+320\sum_{k=0}^{t-2}(0.4)^k=\frac{4000}{3}-\frac{1600}{3}(0.4)^{t-1}$$

El egreso semanal converge a $1333.33$ y **no crece indefinidamente**. Para evaluar la oferta de 25,000 hace falta elegir una tasa de descuento **semanal** consistente con el flujo; la inflación del 4% por sí sola no define una tasa mínima de rendimiento.

---

## 16. Comparación transversal: ¿qué se aprende?
| Caso | Estructura clave | Fecha focal | Principal error a evitar |
|---|---|---|---|
|Ana Laura A|Ingresos geométricos; egresos por tramos|Año 0|Confundir capital disponible con inversión requerida|
|Ana Laura B|Diferencias geométricas; egresos con gradiente diferido|Año 0|Llamar geométrica a la serie completa|
|Educación|Serie uniforme de depósitos y capitalización|Edad 18|Desplazar un año la primera/última aportación|
|Anualidad 5,000|Pagos constantes, vencidos|Año 0|Agregar un pago inexistente en $t=0$|
|Retiros|Anualidad de retiros y saldo recursivo|Fecha del depósito|Confundir 1,500 con 1,580.90|
|Deuda|Anualidad + gradientes|Inicio del préstamo|Permitir sobrepagos finales|
|Camilo|Anualidad + aportaciones puntuales − retiros|Año 16|No incluir pagos simultáneos|
|Fábrica|Ingresos por tramos y diferencias geométricas de egresos|Por definir|Inventar tasa y condiciones de la oferta|

**Cierre:** reconocer patrones no reemplaza el diagrama temporal ni la verificación numérica. Los flujos por componentes y los flujos netos deben dar el mismo valor equivalente con una fecha focal y una tasa coherentes.
