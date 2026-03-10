print("*** Manejo de Excepciones ***")

def dividir (numerador, denominador):
    try:
        #revisamos si el denominador es igual a 0
        if denominador == 0:
            raise Exception("El denominador es igual  0")
        resultado = numerador / denominador
        print(f"Resultado de la division: {resultado}")
#    except ZeroDivisionError:
#        print("Error: No se puede dividir entre CERO")
#    except TypeError:
#        print("Error: Los operandos deben ser numericos")
    except Exception as e:
        print(f"Ocurrio un error: {e}")
    else:
        print(f"No ocurrio ningun error")
    finally:
        print("Terminamos de procesar la excepcion")

#ejemplo de uso
dividir(10,2)
dividir(10,0)