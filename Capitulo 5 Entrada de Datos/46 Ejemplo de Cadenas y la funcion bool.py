# ERROR COMÚN DE PRINCIPIANTE
respuesta_usuario = "False" #Esto es texto

# La función bool evalúa si el string está vacio
es_verdad = bool(respuesta_usuario)

print(f"El valor es: {es_verdad}")
# Output: El valor es: True
# ¿Por qué? Porque el string "False" tiene 5 letras. NO está vacio.

# Forma correcta de validar vacio:
texto_vacio = ""
print(bool(texto_vacio)) # False