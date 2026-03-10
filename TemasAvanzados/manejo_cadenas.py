# manejo de cadenas
#dividir una cadena split() (parcing)

cadena = "Hola Mundo"

palabras = cadena.split()
print(palabras)

#buscar y reemplazar


#buscar con find
posicion = cadena.find("Mundo") #devuelve el valor de 5 por el indice
print(f"Posicion de la cadena mundo: {posicion}")

#remplazar con replace
nueva_cadena = cadena.replace("Mundo","Amigo")
print(f"Nueva cadena remplazada: {nueva_cadena}")

#multiplicador de cadenas
cadena ="Hola "
resultado_multiplicacion_cadenas = cadena*50
print(resultado_multiplicacion_cadenas)

#funcion strip elimina espacios em blanco al inicio y al final

cadena = "..hola mundo.."
print(cadena)
cadena_limpia = cadena.strip(".")
print(f"sin caracteres en blanco ni al inicio ni al final:{cadena_limpia}")