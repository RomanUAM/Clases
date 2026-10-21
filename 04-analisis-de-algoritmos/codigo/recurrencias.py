"""Ejemplos del apunte. Ejecutar: python recurrencias.py"""

def factorial_rec(n):
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)

def fibonacci_rec(n):
    if n <= 1:
        return n
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

def fibonacci_memo(n, memoria=None):
    if memoria is None:
        memoria = {0: 0, 1: 1}
    if n not in memoria:
        memoria[n] = (fibonacci_memo(n - 1, memoria)
                      + fibonacci_memo(n - 2, memoria))
    return memoria[n]

def hanoi(n, origen, auxiliar, destino, mover):
    if n == 0:
        return 0
    antes = hanoi(n - 1, origen, destino, auxiliar, mover)
    mover(n, origen, destino)
    despues = hanoi(n - 1, auxiliar, origen, destino, mover)
    return antes + 1 + despues

def merge_sort(datos):
    if len(datos) <= 1:
        return datos.copy()
    mitad = len(datos) // 2
    izquierda = merge_sort(datos[:mitad])
    derecha = merge_sort(datos[mitad:])
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def resolver_damas(estado, limite, es_meta, sucesores):
    """Busqueda acotada; sucesores debe generar jugadas legales del tablero.

    Devuelve una ruta de estados o None. No genera el tablero ni sus reglas.
    estado debe poder compararse con otros estados de la ruta.
    """
    def buscar(actual, restantes, ruta):
        if es_meta(actual):
            return ruta
        if restantes == 0:
            return None
        for siguiente in sucesores(actual):
            if siguiente not in ruta:
                respuesta = buscar(siguiente, restantes - 1,
                                   ruta + [siguiente])
                if respuesta is not None:
                    return respuesta
        return None
    return buscar(estado, limite, [estado])

if __name__ == "__main__":
    print("50! =", factorial_rec(50))
    print("F10 directo =", fibonacci_rec(10))
    print("F10 con memoria =", fibonacci_memo(10))
    def mostrar(disco, origen, destino):
        print(f"Disco {disco}: {origen} -> {destino}")
    hanoi(3, "A", "B", "C", mostrar)
    cantidad = hanoi(10, "A", "B", "C", lambda d, o, t: None)
    print("Movimientos con 10 discos =", cantidad)
    print("MergeSort =", merge_sort([8, 3, 5, 1, 9, 2, 7, 4]))
