print('*** Decoradores en Python ***')

def decorador(funcion):

    def wrapper(*args, **kwargs):
        print('Antes de llamar la función saludar')
        resultado = funcion(*args, **kwargs)  # llamamos a nuestra funcion
        print('Despues de llamar la funcion saludar')
        return resultado
    return wrapper



#Esta funcion se va a pasar de manera automatica atraves del parametro "nombre"
#inicio de funcion
@decorador
def saludar(nombre):
    print(f'Hola {nombre}')

saludar('Carlos')
#fin de funcion