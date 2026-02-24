class Animal:
    def comer(self):
        print("Como muchas veces al dia")
    def dormir(self):
      print("duermo muchas horas al dia")
      
class Perro(Animal):
    def hacer_sonido(self):
        print("guau guau")
    def dormir(self):
        print("Duermo 15 horas al dia")#se crea funcion que reescribe la funcion heredada de la clase padre 