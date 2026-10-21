"""Ocho estados de una planta y potencia matricial rapida.
Sin dependencias externas. Los conteos son esperanzas, no una simulacion
individual. El vector es fila: v(t) = v(0) P^t.
"""
ESTADOS = ('Semilla', 'Germinacion', 'Primeras hojas', 'Juvenil',
           'Maduracion', 'Floracion', 'Produccion de semillas', 'Muerte')


def matriz_transicion():
    p = [[0.0] * 8 for _ in range(8)]
    for j in range(7):
        p[j][j], p[j][j + 1] = 0.6, 0.4
    p[7][7] = 1.0  # Estado absorbente.
    return p


def multiplicar(a, b):
    """Producto matricial; no producto elemento por elemento."""
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def vector_por_matriz(v, p):
    return [sum(v[k] * p[k][j] for k in range(len(v)))
            for j in range(len(p[0]))]


def potencia_rapida(p, n):
    """Devuelve (P^n, numero de productos matriz por matriz).
    Una llamada recursiva y reutilizacion: O(log n) productos matriciales.
    Con s estados y producto convencional: O(s^3 log n) operaciones.
    """
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError('n debe ser un entero no negativo.')
    if n == 0:
        return [[float(i == j) for j in range(len(p))]
                for i in range(len(p))], 0
    if n == 1:
        return [fila[:] for fila in p], 0
    mitad, productos = potencia_rapida(p, n // 2)
    resultado = multiplicar(mitad, mitad)
    productos += 1
    if n % 2:
        resultado = multiplicar(resultado, p)
        productos += 1
    return resultado, productos


def planta_markov(dias=30):
    p = matriz_transicion()
    v0 = [100.0] + [0.0] * 7
    pn, productos = potencia_rapida(p, dias)
    return vector_por_matriz(v0, pn), p, productos


def evolucion_diaria(dias):
    # Referencia: avanzar un dia a la vez.
    if not isinstance(dias, int) or isinstance(dias, bool) or dias < 0:
        raise ValueError('dias debe ser un entero no negativo.')
    p, actual = matriz_transicion(), [100.0] + [0.0] * 7
    for _ in range(dias):
        actual = vector_por_matriz(actual, p)
    return actual


if __name__ == '__main__':
    dias = 30  # Cambiar para estudiar otro horizonte.
    resultado, p, productos = planta_markov(dias)
    referencia = evolucion_diaria(dias)
    assert max(abs(a - b) for a, b in zip(resultado, referencia)) < 1e-8
    assert abs(sum(resultado) - 100) < 1e-8
    print('Dia 1:', evolucion_diaria(1))
    print('Dia 2:', evolucion_diaria(2))
    print(f'Conteos esperados en el dia {dias}:')
    for estado, valor in zip(ESTADOS, resultado):
        print(f'{estado:24s} {valor:.6f}')
    print('Productos matriz por matriz:', productos)
    print('El producto final vector por matriz no se cuenta arriba.')
