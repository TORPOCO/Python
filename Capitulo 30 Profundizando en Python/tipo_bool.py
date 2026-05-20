# bool Contiene los valores de true y false
#Tipos numéricos, False para 0, True demás valores

valor = 0
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = 15
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

# Tipo str, False para '', True demás valores
valor = ''
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')


# Tipo str, False para '', True demás valores
valor = 'Hola'
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')


#Tipo de colecciones, false para colecciones vacías, true para todas las demás colecciones.
#Lista
valor = []
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = [2,3,4]
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')


#Tupla
valor = ()
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = (2,3,4)
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')



#Diccionario
valor = {}
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = {'nombre': 'Sergio',
    'edad': 30,
    'ciudad': 'México'
}
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')




#Aquí se manda a llamar al constructor bool sin que se vea
if '':
    print('Regreso verdadero')
else:
    print('Regreso falso')



#Así que básicamente aquí lo que sucede es que estaríamos haciendo la
#conversión de este valor, de esta cadena vacía a un tipo bool.
if bool(''):
    print('Regreso verdadero')
else:
    print('Regreso falso')

#tupla
if bool((2,3)):
    print('Regreso verdadero')
else:
    print('Regreso falso')



if bool('Hola'):
    print('Regreso verdadero')
else:
    print('Regreso falso')



variable = 'Hola'
if bool(variable):
    print('Regreso verdadero')
else:
    print('Regreso falso')

variable = ''
while variable:
    print('Regreso verdadero')
else:
    print('Regreso falso')


while bool(variable):
    print('Regreso verdadero')
else:
    print('Regreso falso')