from mundo_pc.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados=0
    def __init__(self,marca,tipo_entrada):
        Teclado.contador_teclados+=1
        self.id_teclado=Teclado.contador_teclados
        super().__init__(marca,tipo_entrada)

    def __str__(self):
        return f"Id: {self.id_teclado} Marca: {self.marca} Tipo Entrada: {self.tipo_entrada}"

#codigo principal hacer pruebas
if __name__=="__main__":
    teclada1=Teclado("Asus","inalambrica")
    print(teclada1)
    teclado2=Teclado("Hp","Usb")
    print(teclado2)
