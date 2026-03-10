print("*** ordenamiento en python ***")

#sintaxis: sorted(iterable, key=None, reverse=False)

empleados = ["juan","pedro","maria"]
#ordenar la lista
empleados_ordenados = sorted(empleados)#asi como esta se devolvera la lista ordenada de forma ascendente, si ponemos (empleados, reverse=True) devolvera la lista ordenada de forma decendente
print(f"empleados ordenados {empleados_ordenados}")

#ordenar un diccionario proporcionando una llave

empleados_dict = [
    {"nombre":"juan","salario":3000},
    {"nombre":"pedro","salario":3500},
    {"nombre":"maria","salario":2500},
]

empleados_ordenados_por_salario = sorted(empleados_dict, key=lambda x: x["salario"])
print(f"empleados ordenados por salarios: {empleados_ordenados_por_salario}")