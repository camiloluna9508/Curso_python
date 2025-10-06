print("*** regresar una tupla de valores desde una funcion")
def persona_mayuscula(nombre,apellido,edad):
    print(f"esta funcion regresa varios valores (tuplan)")
    return nombre.upper(),apellido.upper(),edad

#programa principal
nombre, apellido, edad =persona_mayuscula("sandra","jimenez",42)
print(f"Resultado persona : nombre: {nombre}, apellido: {apellido}, edad: {edad}")