from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado


class Computadora:
    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora += 1
        self.id_computadora = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return (f"{self.nombre}:{self.id_computadora}\n"
                f"\tMonitor: {self.monitor}\n"
                f"\tTeclado: {self.teclado}\n"
                f"\tRaton: {self.raton}\n")


if __name__ == "__main__":
        teclado1=Teclado("Hp","Usb")
        raton1=Raton("Hp","Usb")
        monitor1=Monitor("Hp","20 pulgadas")
        computador1=Computadora("Hp",monitor1,teclado1,raton1)
        print(computador1)

        teclado2=Teclado("Gamer","Bluetooth")
        raton2=Raton("Gamer","Bluetooth")
        monitor2=Monitor("Gamer","34 pulgadas")
        computador2=Computadora("Gamer",monitor2,teclado2,raton2)
        print(computador2)

