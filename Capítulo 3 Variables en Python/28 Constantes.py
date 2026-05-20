import math

# Definición de constantes
PI = 3.14159
MENSAJE_ERROR = 'Se ha producido un error'
NOMBRE_USUARIO_VALIDO = 'admin'
NOMBRE_BASE_DATOS = 'Clientes_DB'


# Imprimir constantes definidas
print('El valor de PI es:', PI)
print('Mensaje de error:',MENSAJE_ERROR)
print('Nombre usuario válido:',NOMBRE_USUARIO_VALIDO)
print('Nombre de la base de datos:',NOMBRE_BASE_DATOS)


# Intento de modificación (no recomendado)
NOMBRE_BASE_DATOS = 'Listado_Clientes_DB'
print('No cambiar el valor de una constante.')
print('Nuevo valor de la constante (no recomendado):',NOMBRE_BASE_DATOS)


# Usar la constante pi del módulo math
print('Constante PI del módulo math:', math.pi)

