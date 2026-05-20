import  math
from  decimal import Decimal

# NaN - Not a number (no es número)
# NaN no es sensible a mayusculas/minúsculas
# NaN es un tipo de dato numerico indefinido
a = float('NaN')
print(f'a: {a}')
print(f'Es NaN (not a number)?: {math.isnan(a)})')


#Otra forma de definir NaN
a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN (not a number)?: {math.isnan(a)})')