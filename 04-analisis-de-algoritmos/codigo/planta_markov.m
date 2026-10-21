function [vFinal, P, productos] = planta_markov(dias)
%PLANTA_MARKOV Evolucion esperada de 100 plantas y potencia rapida.
% Ejemplo: planta_markov       (30 dias)
% Otro horizonte: [v,P,c] = planta_markov(1000);
% Los conteos son esperanzas; pueden tener valores no enteros.
% No se simulan aqui las trayectorias individuales de las plantas.

if nargin == 0
    dias = 30;
end
validateattributes(dias, {'numeric'}, ...
    {'real','finite','scalar','integer','nonnegative'});
estados = {'Semilla','Germinacion','Primeras hojas','Juvenil', ...
    'Maduracion','Floracion','Produccion de semillas','Muerte'};
s = numel(estados);
P = zeros(s);
for j = 1:s-1
    P(j,j) = 0.6;   % Permanecer en el estado actual.
    P(j,j+1) = 0.4; % Avanzar al siguiente estado.
end
P(s,s) = 1;         % Muerte es absorbente: no se puede salir.
% P(fila,columna): probabilidad de pasar de la fila a la columna.
assert(all(abs(sum(P,2)-1) < 1e-12));
v0 = [100 0 0 0 0 0 0 0]; % Vector fila de conteos iniciales.

fprintf('Matriz de transicion:\n'); disp(P);
v1 = v0*P;
v2 = v1*P;
fprintf('Dia 1 (esperados):\n'); disp(v1); % 60,40,0,...
fprintf('Dia 2 (esperados):\n'); disp(v2); % 36,48,16,0,...

% Divide y venceras se aplica al exponente, no a los estados de la planta.
[Pn, productos] = potencia_rapida(P, dias);
vFinal = v0*Pn;
% ^ es potencia matricial. .^ elevaria cada entrada por separado.
vReferencia = v0*(P^dias);
assert(norm(vFinal-vReferencia,Inf) < 1e-8, ...
    'La potencia rapida y la potencia de MATLAB no coinciden.');
assert(abs(sum(vFinal)-100) < 1e-8, ...
    'El total esperado de individuos debe permanecer en 100.');

fprintf('Conteos esperados en el dia %d:\n', dias);
for j = 1:s
    fprintf('%-24s %.6f\n', estados{j}, vFinal(j));
end
fprintf('Productos matriz por matriz en nuestra potencia: %d\n', ...
    productos);
fprintf('El producto final vector por matriz no se cuenta arriba.\n');

% Para conocer todos los dias, avanzamos un dia a la vez.
% Se limita la grafica a los primeros 60 dias para no almacenar miles.
horizonte = min(dias,60);
historia = zeros(horizonte+1,s); historia(1,:) = v0;
for t = 1:horizonte
    historia(t+1,:) = historia(t,:)*P;
end
figure;
plot(0:horizonte,historia,'LineWidth',1.5);
xlabel('Dia'); ylabel('Numero esperado de plantas'); grid on;
legend(estados,'Location','eastoutside');
title('Evolucion esperada de los ocho estados');
end

function [resultado, productos] = potencia_rapida(P,n)
% Casos base: P^0 = identidad, P^1 = P.
if n == 0
    resultado = eye(size(P,1)); productos = 0;
    return;
elseif n == 1
    resultado = P; productos = 0;
    return;
end
% Una sola llamada recursiva; reutilizamos su matriz resultado.
[mitad, productos] = potencia_rapida(P,floor(n/2));
resultado = mitad*mitad;
productos = productos + 1;
if mod(n,2) == 1
    resultado = resultado*P;
    productos = productos + 1;
end
% O(log n) productos matriciales. Con s estados y multiplicacion
% convencional, el costo aritmetico es O(s^3 log n).
end
