print("*** funcion sum y next ***")
lista = [1,2,3,4,5]

#suma de todos los elementos
resultado = sum(lista)
print(f"Resultado de la suma: {resultado}")

#podemos proporcionar un valor inicial
resultado = sum(lista,20)
print(f"Resultado de la suma con valor inicial 20: {resultado}")

#la funcion next
iterador = iter(lista)

#Obtenemos el proximo elemento del iterador
elemento = next(iterador)
print(f"Siguiente elemento del iterable: {next(iterador)}")
print(f"Siguiente elemento del iterable: {next(iterador)}")
print(f"Siguiente elemento del iterable: {next(iterador)}")
print(f"Siguiente elemento del iterable: {next(iterador)}")
print(f"Siguiente elemento del iterable: {next(iterador,"No Se cuenta con mas valores")}")