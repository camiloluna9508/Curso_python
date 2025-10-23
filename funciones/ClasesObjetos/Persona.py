# Definicion de una clase
class Persona:
    def __init__(self,nombre,apellido):
        #atridutos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f"Persona:\n"
              f"\tNombre: {self.nombre}\n"
              f"\tApellido: {self.apellido}\n")
        print(f"Dir. mem self: {id(self)}")
        print(f"Dir. mem hex self: {hex(id(self))}")
#########################################################################

#creacion de objetos

if __name__=="__main__":

    #creacion del primer objeto
    persona1 = Persona("Laila","Acosta")
    print("---persona1 objeto1---")
    persona1.mostrar_persona()
    print(f"Dir. mem persona1: {id(persona1)}")
    print(f"Dir. mem hex persona1: {hex(id(persona1))}")

    #creamos objeto 2
    persona2 = Persona("Ian","Sanchez")
    print("---persona2 objeto2---")
    persona2.mostrar_persona()
    print(f"Dir. mem persona2: {id(persona2)}")
    print(f"Dir. mem hex persona2: {hex(id(persona2))}")
