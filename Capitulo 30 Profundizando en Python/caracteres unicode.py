
#caracteres unicode
#https://symbl.cc/en/unicode-table/

#Secuencias Unicode con \u
#4 dígitos hexadecimales
print('Hola \u0020 Mundo')
print('Notación simple:','\u0041')

#Con caracteres grandes \U
#Usa 8 dígitos.
print('Notación extendida:','\U00000041')

#agregamos x solo funciona para los que tienen 2 caracteres al final
print('Notación hexadecimal:','\x41')

print('Notación gato:','\u2664')
print('Notación corazon:','\U0001F643')