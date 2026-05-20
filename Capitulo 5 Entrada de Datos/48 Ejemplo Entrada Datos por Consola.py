# Programa: Entrada Datos Python
nombre = input("Proporciona tu nombre: ")
print(f"Tu nombre es: {nombre}")

# Cuidado con la conversión de tipos al trabajar con valores numéricos
# Forma Correcta: Envolver con int() o float()

# Para enteros (edad, cantidad)
edad = input("Tu edad: ")
print(f"Tu edad es: {edad}")
print(int(edad) + 5) # ¡funciona! (20 + 5 = 25)

# Para decimales (precio, altura)
altura = float(input("Tu altura: "))
print(f"Tu altura es: {altura}")
