"""Ordenamiento burbuja con parada temprana. Sin dependencias externas."""

def burbuja(datos):
    """Devuelve (lista ordenada, comparaciones, intercambios)."""
    ordenado = list(datos)
    comparaciones = intercambios = 0
    for pasada in range(len(ordenado) - 1):
        hubo_cambio = False
        for j in range(len(ordenado) - 1 - pasada):
            comparaciones += 1
            if ordenado[j] > ordenado[j + 1]:
                ordenado[j], ordenado[j + 1] = ordenado[j + 1], ordenado[j]
                intercambios += 1
                hubo_cambio = True
        if not hubo_cambio:
            break
    return ordenado, comparaciones, intercambios


if __name__ == '__main__':
    datos = [8, 3, 5, 1, 9, 2]
    ordenado, comparaciones, intercambios = burbuja(datos)
    assert ordenado == sorted(datos)
    print('Vector original:', datos)
    print('Vector ordenado:', ordenado)
    print('Comparaciones:', comparaciones)
    print('Intercambios:', intercambios)
