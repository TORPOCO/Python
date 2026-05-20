#Definimos la funcion
def sumar(a, b):
    resultado_suma = a + b
    return resultado_suma

#Que no se ejecute el codigo sumar si no es en este archivo
if __name__ == '__main__':
    print(f'Prueba función sumar desde el módulo:  {sumar(15, 30)}')