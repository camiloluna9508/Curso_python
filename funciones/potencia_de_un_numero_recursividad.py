print("*** potencia de numero recursiva ***")
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

print(f"2 elevado a la 3: {potencia_recursiva(2, 3)}")
print(f"5 elevado a la 0: {potencia_recursiva(5, 0)}")
print(f"4 elevado a la 5: {potencia_recursiva(4, 5)}")
print(f"3 elevado a la 1: {potencia_recursiva(3, 1)}")