#crear un sistema de inventarios que tenga las siguientes opciones:
#mostrar un menu:
#1.mostrar inventario
#2.agregar nuevo producto
#3.buscar producto por ID
#4.salir
#detalle de un producto
#ID, nombre, precio, cantidad
from numpy.ma.core import append

# ✅ Cambiamos los paréntesis () por corchetes [] para que sea una lista
inventario_inicial = [
    {"Id": 1, "Nombre": "Camisa", "Precio": 25.99, "Cantidad": 50},
    {"Id": 2, "Nombre": "Pantalones", "Precio": 39.99, "Cantidad": 30},
    {"Id": 3, "Nombre": "Zapatos", "Precio": 49.99, "Cantidad": 20}
]

def mostrar_inventario(inventario_inicial):
    print("\n--- Inventario actual ---")
    for inventario in inventario_inicial:
        print(
            f"Id: {inventario['Id']}, "
            f"Nombre: {inventario['Nombre']}, "
            f"Precio: ${inventario['Precio']}, "
            f"Cantidad: {inventario['Cantidad']}"
        )

def Agregar_producto(nombre, precio, cantidad):
    global inventario_inicial
    id = len(inventario_inicial) + 1
    inventario_inicial.append({
        "Id": id,
        "Nombre": nombre,
        "Precio": float(precio),
        "Cantidad": cantidad
    })
    print(f"\n✅ Producto '{nombre}' agregado exitosamente al inventario.")
def Buscar_id(x):
    global inventario_inicial
    encontrado = None
    for producto in inventario_inicial:
        if producto['Id'] == x:
            encontrado = producto
            break
    if encontrado:
        print("\n✅ Producto encontrado:")
        print(
            f"Id: {encontrado['Id']}, "
            f"Nombre: {encontrado['Nombre']}, "
            f"Precio: ${encontrado['Precio']}, "
            f"Cantidad: {encontrado['Cantidad']}"
        )
    else:
        print("\n⚠️ No se encontró ningún producto con ese Id.")
while True:
    print("\n*** Sistema de Inventarios (con funciones) ***")
    print("--- Menú ---\n"
          "\t1. Mostrar inventario\n"
          "\t2. Agregar nuevo producto\n"
          "\t3. Buscar producto por Id\n"
          "\t4. Salir\n")

    try:
        opcion = int(input("Proporciona una opción: "))
    except ValueError:
        print("⚠️ Por favor, ingresa un número válido.")
        continue

    if opcion == 1:
        mostrar_inventario(inventario_inicial)
    elif opcion == 2:
        print("\n--- Ingrese los datos del producto a agregar ---")
        nombre = input("Nombre: ")
        precio = input("Precio: $")
        cantidad = int(input("Cantidad: "))
        Agregar_producto(nombre, precio, cantidad)
    elif opcion == 3:
        Buscar_id(int(input("ingrese el ID del producto a bucar: ")))
    elif opcion == 4:
        print("👋 Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("⚠️ Opción no válida. Intente nuevamente.")

