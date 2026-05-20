# Manejo de valores infinitos
import  math

from decimal import Decimal

# constructor de la clase float
infinito_positivo = float('inf')
#'inf' es un valor que se puede representar como infinito con el constructor float
print(f'Infinito: {infinito_positivo}')
#preguntamos si un valor es infinito con isinf
print(f'es infinito: {math.isinf(infinito_positivo)}')



#Infinito negativo
infinito_positivo = float('-inf')
print(f'Infinito negativo: {infinito_positivo}')
print(f'es infinito: {math.isinf(infinito_positivo)}')



# Ahora usamos la clase math
infinito_positivo = math.inf
print(f'Infinito positivo: {infinito_positivo}')
print(f'es infinito: {math.isinf(infinito_positivo)}')


# Ahora usamos la clase -math
infinito_positivo = -math.inf
print(f'Infinito positivo: {infinito_positivo}')
print(f'es infinito: {math.isinf(infinito_positivo)}')


#Módulo decimal
infinito_positivo = Decimal('Infinity')
print(f'Infinito positivo: {infinito_positivo}')
print(f'es infinito: {math.isinf(infinito_positivo)}')


#Módulo decimal negativo
infinito_positivo = Decimal('-Infinity')
print(f'Infinito positivo: {infinito_positivo}')
print(f'es infinito: {math.isinf(infinito_positivo)}')