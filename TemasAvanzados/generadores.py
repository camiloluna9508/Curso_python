print("*** Generadores en python yield***")

def generador(maximo):
    contador = 0
    while contador < maximo:
        yield contador
        contador += 1

#creamos un generador

var_generador = generador(5)
#iteramos sobre el generador

for valor in var_generador:
     print(f"{valor}")