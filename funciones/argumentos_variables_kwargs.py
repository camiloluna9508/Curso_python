print("*** Argumentos variables en forma de diccionario ***")

def superheroe_superpoderes(nombre,*args,**kwargs):
    print(f"superheroe:{nombre} - {args} - Mas info: {kwargs}")

superheroe_superpoderes("spiderman","Instinto aracnido", edad=17,empresa="Marvel")
superheroe_superpoderes("iroman","armadura","playboy", edad=47)
superheroe_superpoderes("mi vecino")