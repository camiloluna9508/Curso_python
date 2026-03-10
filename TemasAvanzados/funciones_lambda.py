from functools import reduce

print("*** funciones lambda")

#funcion cuadrado sin usar lambda

def cuadrado(x):
    return x**2

print(f"cuadrado de 5 es: {cuadrado(5)}")

#funcionb lambda (anonima)

cuadrado_lambda = lambda x: x ** 2
print(f"cuadrado de 2 es: {cuadrado_lambda(2)}")

# con map y lambda creamos una lista de numeros
numeros = [1,2,3,4,5]

#aplicar una funcion lambda para obtener el cuadrado de cada numero

cuadrados = list(map(lambda x: x ** 2, numeros))
print(f"Resultado de usar map y lambda: {cuadrados}")

#con filter y lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))#por filter, solo se guardan en la lista nueva los valores que cumplan la condicion
print(f"Resultado de USAR FILTER para sacar numeros pares: {pares}")

#reduce y map
#la finalidad de reduce es reducir los valores de una lista a solo uno, tipo acumulativo
suma_acumativa = reduce(lambda x, y: x + y, numeros)
print(f"resultado de la suma acumativa utilizando reduce en la lista {numeros} es: {suma_acumativa}")

