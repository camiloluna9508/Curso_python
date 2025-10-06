print("*** funcion con argumentos por nombre ***")

def imprimir_persona(nombre, apellido="", edad=0):
    print(f"persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}")


#primero llamamos la funcion pasando los argumentos de manera posicional

imprimir_persona("Ricardo","quintana",32)

#llamar la funcion usando argumentos por nombre, ventaja podemos hacerlo sin seguir el orden implantado en la creacion de la funcion
imprimir_persona( edad="28",apellido="rojas",nombre="Carlos")

#argumentos con valor por default, para esto en la funcion al inicio cuando se establecen los argumentos se deben poner estos valores por default (apellido="", edad=0)
imprimir_persona(nombre="carlos")