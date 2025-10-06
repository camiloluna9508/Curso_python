from argumentos_por_nombres import imprimir_persona

print("*** imprimir detalles de una persona utilizando kwargs")

def impimir_detalle_persona(**kwargs):
    print("\nvalores recibidos: ")
    for llave, valor in kwargs.items():
        print(f"{llave}: {valor}")

#llamamos a la  funcion
impimir_detalle_persona(nombre="karla",edad=30,ciudad="colombia")
impimir_detalle_persona(nombre="carlos",edad=28,ciudad="colombia",puesto="gerente")

