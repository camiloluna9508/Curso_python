#ejercicio: convertidor de temperatura
#realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa

def Convertidor_celsius_fahrenheit(c):
    f=(c*9/5)+32
    print(f"La temperatura {c}°c ---> {f:.2f}°f")
def Convertidor_fahrenheit_celsius(f):
    c=(f-32)*5/9
    print(f"La temperatura {f}°f ---> {c:.2f}°c")

def mostrar_menu():
    print("--- Convertidor de temperatura ---\n"
          "\t1. celsius ---> fahrenheit\n"
          "\t2. fahrenheit ---> celsius \n"
          "\t3. Salir\n")
    return int(input("Escoge una opcion: "))
def convertir(opcion,salir):
    if opcion==1:
        Convertidor_celsius_fahrenheit(float(input("Ingrese la temperatura en grados celsius: °c"))   )
    elif opcion==2:
        Convertidor_fahrenheit_celsius(float(input("Ingrese la temperatura en grados fahrenheit: °f")))
    elif opcion == 3:
        print("👋 Saliendo del convertidor de tempetatura. ¡Hasta luego!")
        salir=True
    else:
        print("⚠️ Opción no válida. Intente nuevamente.")
    return salir



if __name__ == "__main__":
    print("*** convertidor de temperatura ***")
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir=convertir(opcion,salir)
