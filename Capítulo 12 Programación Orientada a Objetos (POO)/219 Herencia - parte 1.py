class Animal:
    def comer(self):
        print('Como muchas veces el día')

    def dormir(self):
        print('Duermo muchas horas')
#Ponemos en el paréntesis la clase que estamos heredando
class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')
