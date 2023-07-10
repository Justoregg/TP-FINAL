from Clase_Lista_Routers import * 
from random import *

class Routing_Sim:
    
    def __init__(self, tiempo_a_simular):
        self.tiempo_a_simular = tiempo_a_simular
            
    def iniciar_simulacion (self):
        """Input: Objeto simulacion\n
        Funcion: Iniciar la simulacion del programa\n
        Output: Nada"""
        
        # Se toma el tiempo de inicio
        inicio = time.time()    
        
        # Se crea la lista enlazada y se agregan los routers
        lista = ListaRouters()  
        cant_routers = validacion_cant_routers()
        archivo = "System_log.csv"
        routers = []
        for i in range(cant_routers):
            nombre_router = "router"+str(i)
            routers.append(nombre_router)
            routers[i] = Router()
            routers[i].actualizar_csv(archivo)
            routers[i].activar_router()
            routers[i].actualizar_csv(archivo)
            lista.agregar_router(routers[i])
            
        #Se crean los mensajes y se envian aleatoriamente             
        while (time.time() - inicio) < self.tiempo_a_simular:
            for router in routers:
                mensaje = generar_mensaje()  
                if randint(1,3) == 2:
                    router.enviar_paquete(mensaje)      
        else:
            for router in cant_routers:
                router.generar_txt()
        print("Simulacion finalizada")        
                
        #Creo nodos, lista         
        """ time.sleep() 
        router1= Router()
        router1.actualizar_csv("System_log.csv")
        router1.desactivar_router()
        router2= Router()
        router2.actualizar_csv("System_log.csv")
        router2.activar_router()
        router3= Router()
        router3.actualizar_csv("System_log.csv")
        router3.activar_router()
        lista = ListaRouters() 
        lista.agregar_router(router1)
        lista.agregar_router(router2)
        lista.agregar_router(router3)
        inicio = time.time()
        while (time.time() - inicio) < self.tiempo_a_simular:
            mensaje1 = Paquete("hola", 3, 1)
            mensaje2 = Paquete("hola que tal", 3, 2)
            router3.enviar_paquete(mensaje1)
            router3.enviar_paquete(mensaje2)
            router1.actualizar_csv("System_log.csv")
            router2.actualizar_csv("System_log.csv")
            router3.actualizar_csv("System_log.csv")
            #Creo y mando mensajes, proceso, ect
        else:
            router1.generar_txt()
            router2.generar_txt()
            router3.generar_txt()
            print("Simulacion finalizada") """

############ PRUEBAS DE FUNCIONAMIENTO ########### 
 
simulacion = Routing_Sim(0.001)
simulacion.iniciar_simulacion()
