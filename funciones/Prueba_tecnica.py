print("*** Producto del arreglo excepto el elemento actual ***")

def producto_excepto_actual(nums):
    n = len(nums)
    left=[1]*n
    right=[1]*n
    resultado=[1]*n
    #productos hacia la izquierda
    for i in range(1,n):
        left[i]=left[i-1]*nums[i-1]
    #productos hacia la derecha
    for i in range(n-2,-1,-1):
        right[i]=right[i+1]*nums[i+1]

    #resultado = producto izquierda * producto derecha
    for i in range(n):
        resultado[i]=left[i]*right[i]
    return resultado

nums=[1,2,3,4]
print(producto_excepto_actual(nums))