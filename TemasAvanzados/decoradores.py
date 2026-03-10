print("*** Decoradores en python ***")

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("antes de llamar a la funcion de saludar")
        resultado = funcion(*args, **kwargs)#llamamos a nuestra funcion
        print("Despues de llamar la funcion saludar")
        return resultado
    return wrapper


@decorador
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("carlos")

