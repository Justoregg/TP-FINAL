from Clase_Lista_Routers import *

class Routing_Sim:
    
    def __init__(self, tiempo_a_simular):
        self.tiempo_a_simular = tiempo_a_simular
            
    def iniciar_simulacion (self, destino_final, mensaje, origen):
        """Input: Objeto simulacion, destino final del mensaje (Int), mensaje (String), origen del mensaje (Int)\n
        Funcion: Iniciar la simulacion del programa\n
        Output: Nada"""
        inicio = time.time()
        #proceso
        while (time.time() - inicio) < self.tiempo_a_simular:
            continue
        else:
            print("Simulacion finalizada")
         
    @staticmethod
    def ver_paquete (destino, mensaje, origen):
        """Input: Destino del mensaje (Int), mensaje (String), origen del mensaje (Int)\n
        Funcion: Ver un mensaje recibido por un router\n
        Output: Nada"""
        Router.generar_txt(destino, mensaje, origen)   

############ PRUEBAS DE FUNCIONAMIENTO ########### 

simulacion = Routing_Sim(10)
simulacion.iniciar_simulacion(3,"hola que tal",1) 