from Clase_Router import *

class Routing_Sim:
    
    def __init__(self, tiempo_a_simular):
        self.tiempo_a_simular = tiempo_a_simular
        self.routers = []
        
    def agregar_routers(self, cantidad_de_routers):
        """Input: Objeto simulacion, cantidad de routers deseados (Int)\n
        Funcion: Agregar routers a la simulacion\n
        Output: Nada"""
        for i in range(1, int(cantidad_de_routers)+1):
            router = Router(i)
            Router.actualizar_csv("AGREGADO", "System_log.csv", i)
            self.routers.append(router)
            
    def iniciar_simulacion (self, destino_final, mensaje, origen):
        """Input: Objeto simulacion, destino final del mensaje (Int), mensaje (String), origen del mensaje (Int)\n
        Funcion: Iniciar la simulacion del programa\n
        Output: Nada"""
        inicio = datetime.now()
        for nodo in range(origen, destino_final):
            nuevo_paquete = mensaje
            self.routers[nodo].enviar_paquete(nuevo_paquete)
            for router in self.routers: # Habría que hacer esto bien, con una lista enlazada
                router.procesar_paquete
                if router.estado == "AGREGADO" and router.posicion <= destino_final:
                    router.estado = "ACTIVO"
                    Router.actualizar_csv("ACTIVO", "System_log.csv", router.posicion)
                elif router.posicion == destino_final:
                    Routing_Sim.ver_paquete(destino_final, mensaje, origen)
        fin = datetime.now()
        tiempo_simulado = (fin-inicio).total_seconds() # Con esto habria que hacer que el tiempo de la simulacion sea el ingresado como parametro
        
    @staticmethod
    def ver_paquete (destino, mensaje, origen):
        """Input: Destino del mensaje (Int), mensaje (String), origen del mensaje (Int)\n
        Funcion: Ver un mensaje recibido por un router\n
        Output: Nada"""
        Router.generar_txt(destino, mensaje, origen)   


############ PRUEBAS DE FUNCIONAMIENTO ########### 


simulacion = Routing_Sim(10)
simulacion.agregar_routers(5)
simulacion.iniciar_simulacion(3,"hola que tal",1) 