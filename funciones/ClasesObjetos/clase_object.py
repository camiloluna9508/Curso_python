class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    #vamos a sobreescribir el metodo __str__()
    def __str__(self):
        return (f'Persona:\n'
                f'nombre: {self.nombre}\n'
                f'Apellido: {self.apellido}\n'
                f'Dir/mem.: {super.__str__(self)}')#el super. lo que hace es llamar al metodo de la clase padre, es decir el metodo original se envia self en este caso para referencial el objeto de la clase hija

#codigo principal

persona1=Persona('Ana', 'Martinez')
print(persona1)#el metodo __str__ se llama automaticamente desde print