
nombre = 'Juan'
edad = 23
sueldo = 3000
#
mensaje_con_formato = 'Mi nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

mensaje_con_formato = 'Mi nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

mensaje_con_formato = 'Mi nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
print(mensaje_con_formato)

#Con diccionarios
diccionario = {'nombre':'Juan','edad':23,'sueldo':3000}
diccionario2 = ({'nombre':'Ernes','edad':25})
mensaje_con_formato='Nombre {dic[nombre]} Edad {dic[edad]} Nombre {dic2[nombre]}'.format(dic=diccionario,dic2=diccionario2)
print(mensaje_con_formato)