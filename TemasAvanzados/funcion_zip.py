nombres =["juan","maria","pedro"]
edades = [30,25,35]
ciudades = ["Madrid", "Barcelona","Sevilla"]

# combinar los elementos correspondientes usando la funcion zip

personas = zip(nombres, edades, ciudades)

# iterar sobre el resultado de laq funcion zip

for persona in personas:
    print(persona)