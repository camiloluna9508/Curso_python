from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

print("---Mundo Pc---")

#computadora 1
teclado1 = Teclado("Hp", "Usb")
raton1 = Raton("Hp", "Usb")
monitor1 = Monitor("Hp", "20 pulgadas")
computador1 = Computadora("Hp", monitor1, teclado1, raton1)

#computadora 2
teclado2 = Teclado("Gamer", "Bluetooth")
raton2 = Raton("Gamer", "Bluetooth")
monitor2 = Monitor("Gamer", "34 pulgadas")
computador2 = Computadora("Gamer", monitor2, teclado2, raton2)

#crear la lista de computadoras

computadoras1=[computador1,computador2]
orden1=Orden(computadoras1)
print(orden1)

teclado3=Teclado("Dell", "Bluetooth")
raton3 = Raton("Dell", "Bluetooth")
monitor3 = Monitor("Dell", "34 pulgadas")
computador3 = Computadora("Dell",monitor3, teclado3, raton3)

orden1.agregar_computadora(computador3)
print(orden1)

computadoras2=[computador1,computador3,computador2]

orden2=Orden(computadoras2)
print(orden2)