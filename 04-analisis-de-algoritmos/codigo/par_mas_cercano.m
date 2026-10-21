function [par, distancia, evaluaciones] = par_mas_cercano(puntos)
%PAR_MAS_CERCANO Divide y venceras para puntos del plano.
% Ejemplo de 1000 monedas: par_mas_cercano
% Datos propios: [par,d,c] = par_mas_cercano([0 0; 3 4; 0.1 0]);
% Cada fila de puntos contiene [x y]; par contiene indices de sus filas.
% Peor caso Theta(n log n), espacio auxiliar O(n).
% Las evaluaciones cuentan distancias, no todas las operaciones.

mostrar = nargin == 0;
if mostrar
    rng(2026, 'twister');
    puntos = -10 + 20*rand(1000,2);
end
validateattributes(puntos, {'numeric'}, ...
    {'real','finite','2d','ncols',2});
n = size(puntos,1);
if n < 2
    error('Se necesitan al menos dos puntos.');
end

% ID = fila original. Ordenamos por x y por y una sola vez.
Px = sortrows([puntos, (1:n)'], [1 2 3]);
% El rango por x identifica a que mitad pertenece cada punto.
Px(:,4) = (1:n)';
Py = sortrows(Px, [2 1 3]);
[par, d2, evaluaciones] = resolver(Px, Py);
distancia = sqrt(d2); % Una sola raiz al final.

fprintf('Filas del par mas cercano: %d y %d\n', par(1), par(2));
fprintf('Coordenadas:\n'); disp(puntos(par,:));
fprintf('Distancia: %.10f\nEvaluaciones: %d\n', ...
    distancia, evaluaciones);

if mostrar
    % Comprobacion independiente sobre los mismos 1000 puntos.
    [~, d2Bruta, cBruta] = fuerza_bruta(Px);
    tolerancia = 1e-12 * max(1,abs(d2Bruta));
    assert(abs(d2-d2Bruta) <= tolerancia, ...
        'Las distancias minimas no coinciden.');
    fprintf('Fuerza bruta: %d evaluaciones. Distancia verificada.\n', ...
        cBruta);
    figure;
    plot(puntos(:,1), puntos(:,2), '.', 'Color', [0.4 0.5 0.6]);
    hold on;
    plot(puntos(par,1), puntos(par,2), 'ro-', 'LineWidth', 2);
    axis equal; grid on; xlabel('x'); ylabel('y');
    title('El par mas cercano entre 1000 puntos');
end
end

function [par, d2, contador] = resolver(Px, Py)
n = size(Px,1);
if n <= 3
    [par, d2, contador] = fuerza_bruta(Px);
    return;
end

% DIVIDIR: dos mitades equilibradas por numero de puntos.
mitad = floor(n/2);
xDivision = Px(mitad,1);
esIzquierda = Py(:,4) <= Px(mitad,4);
% La seleccion conserva el orden por y incluso cuando hay empates en x.

% VENCER: resolver cada mitad recursivamente.
[parI, dI, cI] = resolver(Px(1:mitad,:), Py(esIzquierda,:));
[parD, dD, cD] = resolver(Px(mitad+1:end,:), Py(~esIzquierda,:));
contador = cI + cD;
if dI <= dD
    par = parI; d2 = dI;
else
    par = parD; d2 = dD;
end
if d2 == 0
    return; % No existe una distancia menor que cero.
end

% COMBINAR: el par global tambien podria cruzar la division.
% La franja ya esta ordenada por y: no se vuelve a ordenar.
franja = Py((Py(:,1)-xDivision).^2 < d2,:);
m = size(franja,1);
for a = 1:m
    % Por el argumento geometrico bastan los siguientes siete puntos.
    for b = a+1:min(a+7,m)
        dy = franja(b,2)-franja(a,2);
        if dy^2 >= d2
            break;
        end
        dx = franja(b,1)-franja(a,1);
        candidato = dx^2 + dy^2;
        contador = contador + 1;
        if candidato < d2
            d2 = candidato;
            par = [franja(a,3), franja(b,3)];
            if d2 == 0
                return;
            end
        end
    end
end
end

function [par, d2, contador] = fuerza_bruta(P)
% Caso base y metodo de referencia: comparar todas las parejas distintas.
n = size(P,1);
d2 = Inf; par = [NaN NaN]; contador = 0;
for a = 1:n-1
    for b = a+1:n
        dx = P(a,1)-P(b,1);
        dy = P(a,2)-P(b,2);
        candidato = dx^2 + dy^2;
        contador = contador + 1;
        if candidato < d2
            d2 = candidato;
            par = [P(a,3), P(b,3)];
        end
    end
end
end
