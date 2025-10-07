#crear un programa donde podras comprar snack de una lista inicial
#cada snack tiene su id,nombre y precio
#para comprar un snack a comprar y se agregara a una lista de productos comprados
#ademas se debe mostrar el ticket de venta final con el total de productos y el total de la venta

print("*** Maquina de Snacks ***")

snacks=[
    {"id":1,"nombre":"Papas","precio":30},
    {"id":2,"nombre":"Refresco","precio":50},
    {"id":3,"nombre":"Sandwich","precio":120}
]
comprar=[]
#funciones

def mostrar_snacks():
    print("--- Snacks disponibles ---\n")
    for snack in snacks:
        print(f"\tId: {snack["id"]} -> {snack['nombre']} - ${snack['precio']}")
def comprar_snack():
    producto=int(input(" Que snack quieres comprar (id):"))
    resultado = None
    for i in snacks:
        if i["id"]==producto:
            resultado=i
            comprar.append(i)
            break
    if resultado:
        print(f"Se agrego el snack Id: {resultado['id']}-> {resultado['nombre']} - ${resultado['precio']} a tu compra")
    else:
        print(f"\n⚠️ No se encontró ningún Snack con el Id: {producto}\n.")
def mostrar_ticket():
    print("--- Ticket de venta ---")
    total=0
    for producto in comprar:
        print(f"\t- {producto['nombre']} - ${producto['precio']}")
        total+=producto['precio']
    print(f"\n\tTotal -> ${total}")

#programa principal
while True:

    print("--- Menú ---\n"
          "\t1. Mostrar Snacks\n"
          "\t2. Comprar snack\n"
          "\t3. Mostrar ticket\n"
          "\t4. Salir\n")

    try:
        opcion = int(input("Escoge una opción: "))
    except ValueError:
        print("⚠️ Por favor, ingresa un número válido.")
        continue
    if opcion == 1:
        mostrar_snacks()
    elif opcion == 2:
        comprar_snack()
    elif opcion == 3:
        mostrar_ticket()
    elif opcion == 4:
        print("👋 Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("⚠️ Opción no válida. Intente nuevamente.")