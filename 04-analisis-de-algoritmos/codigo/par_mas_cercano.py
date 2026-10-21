"""Dos métodos para el par más cercano. Python 3, biblioteca estándar.

Ejecutar: python par_mas_cercano.py
Cada punto interno es (identificador, x, y). Las posiciones son simuladas.
"""
from math import sqrt
from random import Random


def distancia2(a, b):
    return (a[1] - b[1])**2 + (a[2] - b[2])**2


def fuerza_bruta(P):
    if len(P) < 2:
        raise ValueError("Se necesitan al menos dos puntos")
    mejor = float("inf")
    par = None
    comparaciones = 0
    for i in range(len(P) - 1):
        for j in range(i + 1, len(P)):
            d2 = distancia2(P[i], P[j])
            comparaciones += 1
            if d2 < mejor:
                mejor = d2
                par = (P[i], P[j])
    return par, mejor, comparaciones


def resolver(Px, Py):
    n = len(Px)
    if n <= 3:
        return fuerza_bruta(Px)

    mitad = n // 2
    Lx, Rx = Px[:mitad], Px[mitad:]
    m = Rx[0][1]
    ids_L = {p[0] for p in Lx}
    Ly, Ry = [], []
    for p in Py:
        if p[0] in ids_L:
            Ly.append(p)
        else:
            Ry.append(p)

    par_L, d2_L, c_L = resolver(Lx, Ly)
    par_R, d2_R, c_R = resolver(Rx, Ry)
    if d2_L <= d2_R:
        par, mejor = par_L, d2_L
    else:
        par, mejor = par_R, d2_R
    comparaciones = c_L + c_R
    if mejor == 0:
        return par, mejor, comparaciones

    franja = [p for p in Py if (p[1] - m)**2 < mejor]
    for i in range(len(franja)):
        limite = min(i + 8, len(franja))
        for j in range(i + 1, limite):
            dy = franja[j][2] - franja[i][2]
            if dy**2 >= mejor:
                break
            d2 = distancia2(franja[i], franja[j])
            comparaciones += 1
            if d2 < mejor:
                mejor = d2
                par = (franja[i], franja[j])
                if mejor == 0:
                    return par, mejor, comparaciones
    return par, mejor, comparaciones


def divide_y_venceras(P):
    if len(P) < 2:
        raise ValueError("Se necesitan al menos dos puntos")
    Px = sorted(P, key=lambda p: (p[1], p[2], p[0]))
    Py = sorted(P, key=lambda p: (p[2], p[1], p[0]))
    return resolver(Px, Py)


def generar_puntos(n=1000, semilla=2026):
    azar = Random(semilla)
    return [(i, azar.uniform(-10, 10), azar.uniform(-10, 10))
            for i in range(n)]


def mostrar(nombre, resultado):
    par, d2, comparaciones = resultado
    print(nombre)
    print("Monedas:", par[0][0] + 1, "y", par[1][0] + 1)
    print("Coordenadas:", par[0][1:], par[1][1:])
    print(f"Distancia: {sqrt(d2):.10f}")
    print("Evaluaciones de distancia:", comparaciones)


def main():
    P = generar_puntos()
    r_fb = fuerza_bruta(P)
    r_dv = divide_y_venceras(P)
    assert r_fb[1] == r_dv[1]
    mostrar("Fuerza bruta", r_fb)
    mostrar("Divide y venceras", r_dv)
    print("Verificación: ambos métodos dan la misma distancia mínima")


if __name__ == "__main__":
    main()
