print('*** Expresiones Generadores ***')

#Los valores pares de 0 al 10 se elevan al cuadrado
generador = (x**2 for x in range(10) if x % 2 == 0)

for cuadrado_pares in generador:
    print(cuadrado_pares)