print('*** Operaciones con Set ***')

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b
print(f'Union a | b: {union}')

interseccion = a & b
print(f'Intersección a & b {interseccion}')

diferencia1 = a - b
diferencia2 = b - a
print(f'Diferencia a - b {diferencia1}')
print(f'Diferencia b - a {diferencia2}')