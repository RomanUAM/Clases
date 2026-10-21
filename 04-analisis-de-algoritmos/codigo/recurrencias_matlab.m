% Guardar como recurrencias_matlab.m y ejecutar el script.
% Entradas: enteros no negativos; MergeSort: vector numerico finito.
% factorial_rec utiliza double: 50! se representa aproximadamente.
fprintf('50! aproximado = %.9e\n', factorial_rec(50));
fprintf('F10 directo = %d\n', fibonacci_rec(10));
fprintf('F10 con memoria = %d\n', fibonacci_memo(10));
hanoi_rec(3, 'A', 'B', 'C', true);
cantidad = hanoi_rec(10, 'A', 'B', 'C', false);
fprintf('Movimientos con 10 discos = %d\n', cantidad);
disp(merge_sort([8 3 5 1 9 2 7 4]));

function valor = factorial_rec(n)
    if n == 0
        valor = 1;
        return
    end
    valor = n * factorial_rec(n - 1);
end

function valor = fibonacci_rec(n)
    if n <= 1
        valor = n;
        return
    end
    valor = fibonacci_rec(n - 1) + fibonacci_rec(n - 2);
end

function valor = fibonacci_memo(n)
    memoria = nan(1, n + 1);
    memoria(1) = 0;
    if n >= 1
        memoria(2) = 1;
    end
    [valor, ~] = fib_guardado(n, memoria);
end

function [valor, memoria] = fib_guardado(n, memoria)
    if ~isnan(memoria(n + 1))
        valor = memoria(n + 1);
        return
    end
    [a, memoria] = fib_guardado(n - 1, memoria);
    [b, memoria] = fib_guardado(n - 2, memoria);
    valor = a + b;
    memoria(n + 1) = valor;
end

function cantidad = hanoi_rec(n, origen, auxiliar, destino, mostrar)
    if n == 0
        cantidad = 0;
        return
    end
    antes = hanoi_rec(n - 1, origen, destino, auxiliar, mostrar);
    if mostrar
        fprintf('Disco %d: %s -> %s\n', n, origen, destino);
    end
    despues = hanoi_rec(n - 1, auxiliar, origen, destino, mostrar);
    cantidad = antes + 1 + despues;
end

function salida = merge_sort(datos)
    if numel(datos) <= 1
        salida = datos;
        return
    end
    mitad = floor(numel(datos) / 2);
    izq = merge_sort(datos(1:mitad));
    der = merge_sort(datos(mitad + 1:end));
    salida = zeros(1, numel(datos));
    i = 1; j = 1; k = 1;
    while i <= numel(izq) && j <= numel(der)
        if izq(i) <= der(j)
            salida(k) = izq(i); i = i + 1;
        else
            salida(k) = der(j); j = j + 1;
        end
        k = k + 1;
    end
    resto = [izq(i:end), der(j:end)];
    salida(k:end) = resto;
end
