mi_lista = [1, 2, 3, 4, 5]


# Modificar los elementos de una lista
mi_lista[1] = 10
print(f'Modificamos el valor del indice 1: {mi_lista[1]}')

# Agregar un nuevo elemento al final de la lista
mi_lista.append(6)
print(f'{mi_lista} -> Se agregó el elemento 6')

# Añadir un nuevo elemento en un indice especifico sin eliminar ningun otro
mi_lista.insert(2, 15)
print(f'{mi_lista} -> Se añadió el valor de 15 en el índice 2')