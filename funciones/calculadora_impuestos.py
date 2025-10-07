#ejercicio: calculadora de impuestos
#crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado.
#formula: pago_total = pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)


def calcular_impuesto():
    pago_sin_impuesto = float(input("proporcione el pago sin impuesto: $"))
    impuesto=float(input("proporcione el monto del impuesto: %"))
    total=pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)
    print(f"pago con impuesto: ${total} ")


print("*** calculadora de impuesto ***")
if __name__ == "__main__":
    calcular_impuesto()