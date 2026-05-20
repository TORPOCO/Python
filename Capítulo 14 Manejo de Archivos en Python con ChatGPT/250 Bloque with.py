# Crear un archivo
nombre_archivo = 'mi_archivo.txt'

# Abrir el archivo en modo escritura ('w')
with open(nombre_archivo, 'w') as archivo:
    archivo.write('Hola como estas\n')
    archivo.write('estoy agregando informacion al archivo\n')

print(f'Se creo el archivo: {nombre_archivo}')