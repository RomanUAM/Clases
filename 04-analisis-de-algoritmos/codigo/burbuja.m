function [ordenado, comparaciones, intercambios] = burbuja(datos)
%BURBUJA Ordena de menor a mayor mediante comparaciones adyacentes.
% Ejemplo: burbuja
% Otro vector: [v,c,s] = burbuja([8 3 5 1 9 2]);
% Peor caso: Theta(n^2). Mejor caso con parada temprana: Theta(n).

if nargin == 0
    datos = [8 3 5 1 9 2];
end
validateattributes(datos, {'numeric'}, {'real','finite','vector'});
ordenado = datos;
n = numel(ordenado);
comparaciones = 0;
intercambios = 0;

for pasada = 1:n-1
    huboCambio = false;
    % Los ultimos pasada-1 elementos ya estan en su lugar.
    for j = 1:n-pasada
        comparaciones = comparaciones + 1;
        if ordenado(j) > ordenado(j+1)
            auxiliar = ordenado(j);
            ordenado(j) = ordenado(j+1);
            ordenado(j+1) = auxiliar;
            intercambios = intercambios + 1;
            huboCambio = true;
        end
    end
    % Si nadie cambio, todo el vector ya esta ordenado.
    if ~huboCambio
        break;
    end
end

fprintf('Vector original:\n'); disp(datos);
fprintf('Vector ordenado:\n'); disp(ordenado);
fprintf('Comparaciones: %d\nIntercambios: %d\n', ...
    comparaciones, intercambios);
end
