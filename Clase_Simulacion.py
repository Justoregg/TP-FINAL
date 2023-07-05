from Clase_Router import *
from Clase_paquete import * 

class Routing_Sim:
    
    def __init__(self, tiempo_a_simular):
        self.tiempo_a_simular = tiempo_a_simular
        self.routers = []
        
    def agregar_routers(self, cantidad_de_routers):
        for i in range(1, cantidad_de_routers):
            router = Router(i)
            self.routers.append(router)
            
    def iniciar_simulacion (self, destino_final):
        while True:
            nuevo_paquete = {"origen": 0, "destino": destino_final}
            self.routers[0].enviar_paquete(nuevo_paquete)
            for router in self.routers:
                if router.estado == "AGREGADO" and router.posicion < destino_final:
                    router.estado = "ACTIVO"
                    