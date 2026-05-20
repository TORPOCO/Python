print('*** Playlist de Canciones ***')

#Creamos la lista vacia
lista_reproduccions = []

#empezamos a agregar canciones
lista_reproduccions.append('Hotel California - Eagles')
lista_reproduccions.append('Staying Alive - Bee Gees')
lista_reproduccions.append('Dream on - Aerosmith')

#Ordenar la lista en orden alfabetico.sort
lista_reproduccions.sort(reverse=True)#desendente

#Mostrar la lista de canciones
print(f'\n Lista de Reproducción en orden alfabético')
print(lista_reproduccions)


#Mostrar la lista iterando sus elementos
print('\nIteremos el playlist')
for cancion in lista_reproduccions:
    print(f'-{cancion}')