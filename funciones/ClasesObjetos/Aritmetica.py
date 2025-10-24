#ejercicio donde se debe realizar una clase con 2 atributos y como metodos de la clase las operaciones de +,-,x,/
import inspect


#creamos o definimos la clase
class Aritmetica:
    #definimos el metodo de iniciacion de la clase
    def __init__(self, operando1,operando2):
        self.operando1 = int(operando1)
        self.operando2 = int(operando2)
    #metodo para mostrar elementos
    def mostrar_operandos(self):
        print(f"Los operandos del objeto--> {hex(id(self))} son:\n \toperando1: {self.operando1}\n \toperando2: {self.operando2}")
    #metodos que requieren en el ejercicio
    def suma(self):
        return self.operando1 + self.operando2
    def resta(self):
        return self.operando1 - self.operando2
    def multiplicacion(self):
        return self.operando1 * self.operando2
    def division(self):
        return self.operando1 / self.operando2
    #los metodos solo retornan el valor de la operacion
    def mostrar_operaciones(self):
        print(f"Los operandos del objeto ---> {hex(id(self))} son:\n \toperando1: {self.operando1}\n \toperando2: {self.operando2}")
        print(f"Operaciones del objeto {hex(id(self))}:\n \t*la suma de los operandos es: {self.suma()}\n"
              f"\t*la resta de los operandos es: {self.resta()}\n"
              f"\t*la multiplicacion de los operandos es: {self.multiplicacion()}\n"
              f"\t*la division de los operandos es: {self.division():.2f}")

if __name__ == "__main__":
    print("Clase Aritmetica")
    print("---Objeto1---")
    objeto1 = Aritmetica(5,7)
    objeto1.mostrar_operaciones()

    objeto2 = Aritmetica(12,16)
    objeto2.mostrar_operaciones()
