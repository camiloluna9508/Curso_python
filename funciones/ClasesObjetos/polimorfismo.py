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

# Funcion polimorfica

def hacer_sonido_animal(animal):#duck typing
    animal.hacer_sonido()


print("***ejemplo polimorfismo***")
print("clase padre Animal")
animal1=Animal()
hacer_sonido_animal(animal1)

#definimos un objeto de la clase perro "clase hija"
print("\nclase hija perro")
perro1=perro()
hacer_sonido_animal(perro1)
print("\nclase hija gato")
gato1=gato()
hacer_sonido_animal(gato1)