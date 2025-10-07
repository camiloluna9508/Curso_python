#crear un programa tipo calculadora que realice suma, resta, multiplicacion y divicion pero cada una llame una funcion que realice dicho proceso

print("*** calculadora con Funciones ***")

def mostrar_menu():
    print("--- Menú ---\n"
          "\t1. Suma\n"
          "\t2. Resta\n"
          "\t3. Multiplicacion\n"
          "\t4. División\n"
          "\t5. Salir\n")
    return int(input("Escoge una opcion: "))
def pedir_valores():
    operando1=float(input("Dame el valor 1: "))
    operando2=float(input("Dame el valor 2: "))
    return operando1, operando2
def ejecutar_operacion(opcion, salir):
    if 1<=opcion<=4:
        a,b = pedir_valores()
    resultado = 0
    if opcion == 1:
        resultado = a + b
        print(f"El resultado de la suma es: {resultado}\n")
    elif opcion == 2:
        resultado=a-b
        print(f"El resultado de la resta es: {resultado}\n")
    elif opcion == 3:
        resultado = a * b
        print(f"El resultado de la multiplicacion es: {resultado}\n")
    elif opcion == 4:
        resultado = a / b
        print(f"El resultado de la division es: {resultado}\n")
    elif opcion == 5:
        print("👋 Saliendo de la calculadora. ¡Hasta luego!")
        salir=True
    else:
        print("⚠️ Opción no válida. Intente nuevamente.")
    return salir

#programa principal
if __name__ == "__main__":
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir=ejecutar_operacion(opcion,salir)

