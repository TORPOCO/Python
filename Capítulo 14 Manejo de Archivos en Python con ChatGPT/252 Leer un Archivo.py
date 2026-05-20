print('*** Leer Archivo con Python ***')

nombre_archivo = 'mi_archivo.txt'

# Leer un archivo usando el metodo readlineas
with open(nombre_archivo, 'r') as archivo:
    # Leer todas las lineas del archivo
    print(archivo.readlines())


# Leer el contenido del archivo usando read
print('**** Leyendo el contenido con el metodo read ***')
with open(nombre_archivo, 'r') as archivo:
    print(archivo.read().strip())

print('**** Leyendo el contenido con el metodo strip ***')
with open(nombre_archivo, "r") as archivo:
    for linea in archivo:
        print(linea.strip())

# Leer un archivo usando el metodo readlineas for
print('**** Leyendo el contenido con el metodo readlines For ***')
with open(nombre_archivo, 'r') as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())