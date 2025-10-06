print("*** argumentos variables ***")

def superheroe_superpoderes(superheroe,nombre,*args):
    print(f"superheroe: {superheroe}, nombre: {nombre}, poderes: {args}")
    #iteramos los superpoderes
    for superpoder in args:
        print(f"\tsuperpoder: {superpoder}")

superheroe_superpoderes("spiderman","peter parker","Instinto aracnido","Teleraña")
superheroe_superpoderes("iroman","tony stark","Armadura","playboy","millonario")
superheroe_superpoderes("mi vecino","juan perez")