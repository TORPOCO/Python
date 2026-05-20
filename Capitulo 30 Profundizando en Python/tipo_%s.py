
nombre = 'Juan'
edad = 23

#
mensaje_con_formato = 'Mi nombre es %s'%nombre
print(mensaje_con_formato)

mensaje_con_formato = 'Mi nombre es %s años %s '%(nombre,edad)
print(mensaje_con_formato)

persona = ('karla','gomez',5000.00)
#formato de tipo flotante %.numerof
mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.5f'%persona
print(mensaje_con_formato)

mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.5f'
print(mensaje_con_formato%persona)