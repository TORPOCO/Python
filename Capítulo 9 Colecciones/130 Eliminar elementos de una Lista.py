print('*** Manejo de Listas ***')

mi_lista = [1, 2, 3, 4, 5,6]

# Eliminar elementos de una lista
# usando el metodo remove
mi_lista.remove(5)
print(f'{mi_lista} -> Se removió el valor 5')


# Removemos por indice con el metodo pop
mi_lista.pop(1) # Remueve el elemento del indice 1
print(f'{mi_lista} -> Se eliminó el índice 1')


# Eliminar usando la palabra del
del mi_lista[2]
print(f'{mi_lista} -> Se eliminó el índice 2')

# Obtener sublistas
sublista = mi_lista[1:3]  # genera una sublista del indice 1 al 2 (3 no se incluye)
print(f'Sublista [1:3]: {sublista}')