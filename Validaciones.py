from string import *

def validacion_cant_routers ():
    """Input: Nada
    Funcion: Verifica que la cantidad de routers sea mayor a 0
    Output: Cantidad de routers"""
    cant_routers = int(input("Inserte cantidad de routers: "))
    while cant_routers <= 0:
        print ("La cantidad de routers debe ser mayor a 0")
        cant_routers = int(input("Inserte cantidad de routers: "))
    return cant_routers

