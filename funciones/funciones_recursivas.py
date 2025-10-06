print("*** imprimir del 1 al 5 de forma recursiva ***")

def imprimir_recursiva_ascendente(numero):
    if numero ==1:
        print(numero, end=" ")
    else:
        imprimir_recursiva_ascendente(numero-1)
        print(numero, end=" ")


imprimir_recursiva_ascendente(5)

print("\n*** imprimir del 5 al 1 de forma recursiva ***")

def imprimir_recursiva_descendente(numero):
    if numero == 1:
        print(numero, end=" ")
    else:
        print(numero, end=" ")
        imprimir_recursiva_descendente(numero-1)

imprimir_recursiva_descendente(5)