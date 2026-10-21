"""Par mas cercano por dividir y vencer. Sin dependencias externas.
Cada punto es (x,y). Los identificadores se muestran desde 1, como en MATLAB.
Peor caso O(n log n). Las evaluaciones cuentan distancias, no operaciones totales.
"""
from math import isfinite, sqrt
from random import Random


def fuerza_bruta(puntos):
    """Referencia independiente. Devuelve (par de filas, distancia, contador)."""
    mejor, par, contador = float('inf'), None, 0
    for a in range(len(puntos) - 1):
        for b in range(a + 1, len(puntos)):
            dx = puntos[a][0] - puntos[b][0]
            dy = puntos[a][1] - puntos[b][1]
            d2 = dx * dx + dy * dy
            contador += 1
            if d2 < mejor:
                mejor, par = d2, (a + 1, b + 1)
    if par is None:
        raise ValueError('Se necesitan al menos dos puntos.')
    return par, sqrt(mejor), contador


def par_mas_cercano(puntos):
    """Devuelve (indices desde 1, distancia minima, evaluaciones)."""
    puntos = list(puntos)
    if len(puntos) < 2:
        raise ValueError('Se necesitan al menos dos puntos.')
    if any(len(p) != 2 or not all(isfinite(v) for v in p) for p in puntos):
        raise ValueError('Cada punto debe contener dos coordenadas finitas.')
    # Registro (x,y,id,rango por x). Ordenamos una sola vez.
    px = sorted((x, y, j + 1) for j, (x, y) in enumerate(puntos))
    px = [(x, y, j, rango) for rango, (x, y, j) in enumerate(px)]
    py = sorted(px, key=lambda p: (p[1], p[0], p[2]))
    par, d2, contador = _resolver(px, py)
    return par, sqrt(d2), contador


def _resolver(px, py):
    n = len(px)
    if n <= 3:
        mejor, par, contador = float('inf'), None, 0
        for a in range(n - 1):
            for b in range(a + 1, n):
                dx, dy = px[a][0] - px[b][0], px[a][1] - px[b][1]
                d2 = dx * dx + dy * dy
                contador += 1
                if d2 < mejor:
                    mejor, par = d2, (px[a][2], px[b][2])
        return par, mejor, contador
    # DIVIDIR por cantidad, incluso si varias coordenadas x coinciden.
    mitad = n // 2
    limite = px[mitad - 1][3]
    x_division = px[mitad - 1][0]
    izquierda_y, derecha_y = [], []
    for punto in py:
        (izquierda_y if punto[3] <= limite else derecha_y).append(punto)
    # VENCER las dos mitades.
    par_i, d_i, c_i = _resolver(px[:mitad], izquierda_y)
    par_d, d_d, c_d = _resolver(px[mitad:], derecha_y)
    par, d2 = (par_i, d_i) if d_i <= d_d else (par_d, d_d)
    contador = c_i + c_d
    if d2 == 0:
        return par, d2, contador
    # COMBINAR: tambien pueden existir parejas que crucen la division.
    franja = [p for p in py if (p[0] - x_division) ** 2 < d2]
    for a in range(len(franja)):
        for b in range(a + 1, min(a + 8, len(franja))):
            dy = franja[b][1] - franja[a][1]
            if dy * dy >= d2:
                break
            dx = franja[b][0] - franja[a][0]
            candidato = dx * dx + dy * dy
            contador += 1
            if candidato < d2:
                d2, par = candidato, (franja[a][2], franja[b][2])
                if d2 == 0:
                    return par, d2, contador
    return par, d2, contador


if __name__ == '__main__':
    azar = Random(2026)
    puntos = [(azar.uniform(-10, 10), azar.uniform(-10, 10)) for _ in range(1000)]
    par, distancia, contador = par_mas_cercano(puntos)
    _, distancia_bruta, c_bruta = fuerza_bruta(puntos)
    assert abs(distancia - distancia_bruta) <= 1e-12 * max(1, distancia_bruta)
    print('Monedas:', par)
    print('Coordenadas:', [puntos[j - 1] for j in par])
    print(f'Distancia: {distancia:.10f}')
    print('Evaluaciones divide y venceras:', contador)
    print('Evaluaciones fuerza bruta:', c_bruta)
    print('Distancia minima verificada.')
