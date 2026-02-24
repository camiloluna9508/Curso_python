#polimorfismo
class Animal:
    def hacer_sonido(self):
        print("Hago un pitido")

class perro(Animal):
    def hacer_sonido(self):
        print(" Puedo ladrar")

class gato (Animal):
    def hacer_sonido(self):
        print(" Puedo maullar")

print("***ejemplo polimorfismo***")
print("clase padre Animal")
animal1=Animal()
animal1.hacer_sonido()

#definimos un objeto de la clase perro "clase hija"
print("\nclase hija perro")
perro1=perro()
perro1.hacer_sonido()
print("\nclase hija gato")
gato1=gato()
gato1.hacer_sonido()