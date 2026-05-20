class Persona:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, other):
        return f'{self.valor}  {other.valor}'

#Ejemplo 1
a = Persona(5)
b = Persona(3)
#Como funciona
#La "a" manda a llamar __add__(y le pasamos como parametro obj2 que es b)
print(a + b)




#Ejemplo 2
persona1 = Persona('Juan')
persona2 = Persona('Maria')

#Aqui pasa lo mismo
print(persona1 + persona2)
