from Clase_Lista_Routers import * 
from random import *

class Routing_Sim:
    
    def __init__(self, tiempo_a_simular):
        self.tiempo_a_simular = tiempo_a_simular
            
    def iniciar_simulacion (self):
        """Input: Objeto simulacion, destino final del mensaje (Int), mensaje (String), origen del mensaje (Int)\n
        Funcion: Iniciar la simulacion del programa\n
        Output: Nada"""
        
        #Automatisacion, crea los routers y los activa/desactiva aleatoriamente (falta retocar bastante)
        inicio = time.time()
        #Creo los routers
        lista = ListaRouters()
        cant_routers = int(input("Inserte cantidad de routers"))
        archivo = "System_log"
        routers = []
        for i in range(cant_routers):
            nombre_router = "router"+str(i)
            routers.append(nombre_router)
            routers[i] = Router()
            routers[i].actualizar_csv(archivo)
            if 2 == randint(1,4):
                routers[i].desactivar_router()
            else:
                routers[i].activar_router()
            routers[i].actualizar_csv(archivo)
            lista.agregar_router(routers[i])
            
        #crea los mensajes
        cantidad_mensajes = int(input("ingrese cantidad de mensajes"))
        mensajes = []
        for i in range(cantidad_mensajes+1):
            nombre_variable = "mensaje" + str(i)      
            mensajes.append(nombre_variable)
            mensajes[i] = Paquete()                     # por alguna razon, cuando ejectuto, lo primero que se corre es la clase paquete y luego no se realiza correctamente el ciclo for
            
        envios = []    
        for i in range(cantidad_mensajes+1):
            
            envioXrouter = routers[mensajes[i].posicion_origen] 
            envios.append(envioXrouter)
            envios[i].enviar_paquete(mensajes[i])
                
                
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
         
    @staticmethod
    def ver_paquete (destino, mensaje, origen):
        """Input: Destino del mensaje (Int), mensaje (String), origen del mensaje (Int)\n
        Funcion: Ver un mensaje recibido por un router\n
        Output: Nada"""
        Router.generar_txt(destino, mensaje, origen)   

############ PRUEBAS DE FUNCIONAMIENTO ########### 

            
simulacion = Routing_Sim(0.001)
simulacion.iniciar_simulacion()
