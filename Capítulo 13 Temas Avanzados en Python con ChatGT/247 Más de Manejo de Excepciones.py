print('*** Manejo de Excepciones ***')

def dividir(numerador, denominador):
    try:
        # Revisamos si el denominador es igual a 0
        if denominador == 0:
            raise Exception('El denominador es igual a 0')
        resultado = numerador / denominador
        print(f'Resultado de la división: {resultado}')
    except Exception as e:
        print(f'Ocurrio un error: {e}')
    else:
        print(f'No ocurrió ningún error')



# Ejemplo de uso
dividir(10, 2)
dividir(10, 0)
