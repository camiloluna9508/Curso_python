variable_global=0
def incrementar_contador():
    global variable_global
    variable_global += 1
    variable_local=0
    variable_local += 1
    print(f"variable local: {variable_local}")
    print(f"variable global: {variable_global}\n")

incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()


