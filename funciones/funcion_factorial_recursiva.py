print("*** factorial de n de forma recursiva ***")
def factorial_recursiva(n):
    if n==0 or n==1:
        print(f"resultado factorial parcial {n} es 1")
        return 1
    else:
        factorial_parcial=n*factorial_recursiva(n-1)
        print(f"resultado factorial parcial {n} es {factorial_parcial}")
        return factorial_parcial

x=int(input("Ingresa un numero: "))
print(f"el factorial de {x} = {factorial_recursiva(x)}")