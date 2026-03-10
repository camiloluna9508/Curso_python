print("comprension de listas")
#filtrar solo los numeros pares y generar una nueva lista con estos valores

numeros = range(1,10+1)
#sin usar comprension de listas
numeros_pares = []
 #iteramos cada elemento de la lista por medio del ciclo for
for numero in numeros:
    if numero % 2 == 0:
        print(f"el numero {numero} es par, lo agregamos a la lista numeros_pares")
        numeros_pares.append(numero)

print(f"numeros pares del 1 al 10 sacados por ciclo for sin comprension de listas {numeros_pares}")

#en comprension de listas seria de la siguiente forma

numeros_pares_comprension=[x for x in range(1,10+1) if x % 2 == 0]
print(f"numeros pares del 1 al 10 sacados por comprension de listas: {numeros_pares_comprension}")