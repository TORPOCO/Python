nombre = input("Nombre de la Receta:")
ingredientes = input("Ingredientes de la Receta:")
tiempo = int(input("Tiempo de Prepación:"))
dificultad = input("Facil,Media,Alta:")

#Imprimir
print('----------------------------------')
print(f'Nombre de la Receta: {nombre}')
print(f'Ingredientes de la Receta: {ingredientes}')
print(f'Tiempo de prepacion(en minutos): {tiempo}'+' minutos')
print(f'Facil,Media,Alta: {dificultad}')