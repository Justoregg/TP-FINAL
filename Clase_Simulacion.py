from Clase_Lista_Routers import * 
from random import *
from os import * 

class Routing_Sim:
    
    def __init__(self, tiempo_a_simular):
        self.tiempo_a_simular = tiempo_a_simular
            
    def iniciar_simulacion (self):
        """Input: Objeto simulacion\n
        Funcion: Iniciar la simulacion del programa\n
        Output: Nada"""
        
        # Se toma el tiempo de inicio
        
        inicio = time.time()    
        
        # Se crea la lista enlazada y se agregan los routers activados
        
        lista = ListaRouters()  
        archivo = "System_log.csv"

        router1 = Router()
        router2 = Router()
        router3 = Router()
        router4 = Router()
        router5 = Router()
        
        router1.actualizar_csv(archivo)
        router2.actualizar_csv(archivo)
        router3.actualizar_csv(archivo)
        router4.actualizar_csv(archivo)
        router5.actualizar_csv(archivo)
        
        router1.activar_router()
        router1.actualizar_csv(archivo)
        
        router2.activar_router()
        router2.actualizar_csv(archivo)
        
        router3.activar_router()
        router3.actualizar_csv(archivo)
        
        router4.activar_router()
        router4.actualizar_csv(archivo)
        
        router5.activar_router()
        router5.actualizar_csv(archivo)
        
        lista.agregar_router(router1)
        lista.agregar_router(router2)
        lista.agregar_router(router3)
        lista.agregar_router(router4)
        lista.agregar_router(router5)
        
        tiempo_reseteo = time.time()
        cant_segundos = random() 
        router3.resetear_router()     
        router3.actualizar_csv(archivo)
        
        # Se verifica que la simulacion dure el tiempo estipulado
        while (time.time() - inicio) < self.tiempo_a_simular:
            
            # Se simula un reseteo
            if time.time()-tiempo_reseteo > cant_segundos:
                router3.activar_router()
            
            # Se envia un mensaje    
            mensaje1 = generar_mensaje()
            paquete1 = Paquete(mensaje1,1,4)
            router1.enviar_paquete(paquete1)

            # Se desactiva un router durante la ejecucion
            router2.desactivar_router()
            
            #Se envia otro mensaje
            mensaje2 = generar_mensaje()
            paquete2 = Paquete(mensaje2,5,2)
            router5.enviar_paquete(paquete2)
        
        router2.actualizar_csv(archivo)
        
        # Se muestran los mensajes que pasaron por cada router    
        router1.generar_txt()
        router2.generar_txt()
        router3.generar_txt()
        router4.generar_txt()
        router5.generar_txt()
        
        print("Simulacion finalizada")  
        
        #Se borran los archivos
        opcion = input("Presione 1 para borrar los datos: ")
        if opcion == "1":         
            for i in range(1,6):
                if path.exists('router_'+str(i)+'.txt'):
                    remove('router_'+str(i)+'.txt')
            print("archivos eliminados correctamente")
            
############ PRUEBAS DE FUNCIONAMIENTO ########### 
 
simulacion = Routing_Sim(0.1)
simulacion.iniciar_simulacion()
