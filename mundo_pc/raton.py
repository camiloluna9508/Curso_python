from mundo_pc.dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones=0
    def __init__(self, marca,tipo_entrada):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        #self.marca = marca
        #self.tipo_entrada = tipo_entrada
        super().__init__(marca, tipo_entrada)#se utiliza el super para heredar de la clase padre los valores.

    def __str__(self):
        return f"Id:{self.id_raton} Marca:{self.marca} Tipo Entrada:{self.tipo_entrada}"


#codigo principal

if __name__ == '__main__':
    raton1=Raton("hp","usb")
    print(raton1)
    raton2=Raton("ph","usb")
    print(raton2)
