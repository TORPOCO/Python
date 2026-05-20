print('*** Manejo de Excepciones ***')

def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
        print(f'Resultado de la división: {resultado}')
    except ZeroDivisionError:
         print('Error: No se puede dividir entre cero')
    except TypeError:
         print('Error: Los operandos deben ser numericos')

# Ejemplo de uso
dividir(10, 2)
dividir(10, 0)
dividir(10, '0')
