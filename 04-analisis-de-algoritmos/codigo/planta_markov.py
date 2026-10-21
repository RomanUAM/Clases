"""Evolución esperada de 100 plantas y potencia de matrices por división.

Python 3, biblioteca estándar. Ejecutar: python planta_markov.py
"""
ESTADOS = ["Semilla", "Germinación", "Primeras hojas", "Juvenil",
           "Maduración", "Floración", "Producción de semillas", "Muerte"]


def transicion():
    P = [[0.0] * 8 for _ in range(8)]
    for i in range(7):
        P[i][i] = 0.6
        P[i][i + 1] = 0.4
    P[7][7] = 1.0
    return P


def identidad(s):
    return [[float(i == j) for j in range(s)] for i in range(s)]


def multiplicar(A, B):
    s = len(A)
    C = [[0.0] * s for _ in range(s)]
    for i in range(s):
        for j in range(s):
            for k in range(s):
                C[i][j] += A[i][k] * B[k][j]
    return C


def vector_por_matriz(v, P):
    s = len(v)
    return [sum(v[i] * P[i][j] for i in range(s)) for j in range(s)]


def potencia_rapida(P, dias):
    if not isinstance(dias, int) or dias < 0:
        raise ValueError("dias debe ser un entero no negativo")
    if dias == 0:
        return identidad(len(P))
    if dias == 1:
        return [fila[:] for fila in P]
    mitad = potencia_rapida(P, dias // 2)
    resultado = multiplicar(mitad, mitad)
    if dias % 2 == 1:
        resultado = multiplicar(resultado, P)
    return resultado


def evolucion_diaria(v, P, dias):
    actual = v[:]
    for _ in range(dias):
        actual = vector_por_matriz(actual, P)
    return actual


def evolucion_rapida(v, P, dias):
    return vector_por_matriz(v, potencia_rapida(P, dias))


def main():
    P = transicion()
    inicial = [100.0] + [0.0] * 7
    for dias in [0, 1, 2, 7, 10, 30, 1000]:
        diario = evolucion_diaria(inicial, P, dias)
        rapido = evolucion_rapida(inicial, P, dias)
        assert max(abs(a - b) for a, b in zip(diario, rapido)) < 1e-9
        print(f"Día {dias}")
        for estado, cantidad in zip(ESTADOS, rapido):
            print(f"  {estado}: {cantidad:.6f}")
        print(f"  Total esperado: {sum(rapido):.6f}")


if __name__ == "__main__":
    main()
