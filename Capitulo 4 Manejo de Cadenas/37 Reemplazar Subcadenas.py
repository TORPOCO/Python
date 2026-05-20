# Programa: Reemplazar texto en python

mensaje = "Hola Mundo, Mundo"

# Remplazar TODAS las apariciones
nuevo = mensaje.replace("Mundo","Python)")
print(nuevo)

# Salida: "Hola python, Python

#remplazar solo UNA vez
uno_solo = mensaje.replace("Mundo","Dev",3)
print(uno_solo)
# Salida: "Hola Dev, Mundo"