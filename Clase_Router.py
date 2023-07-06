from Clase_paquete import *
from datetime import *
import time
import csv
import random 

class Router:
    
    def __init__(self, posicion):
        self.estado = "AGREGADO"
        self.posicion = posicion 
        self.latencia = 0 
              
    def activar_router (self):
        """Input: Objeto router\n
        Funcion: Cambiar el estado del router a activo\n
        Output: Nada"""
        if self.estado != "ACTIVO":
            self.estado = "ACTIVO"
            
    def deactivar_router (self):
        """Input: Objeto router\n
        Funcion: Cambiar el estado del router a inactivo\n
        Output: Nada"""
        if self.estado != "INACTIVO":
            self.estado = "INACTIVO"
    
    def resetear_router (self):
        """Input: Objeto router\n
        Funcion: Resetear un router\n
        Output: Nada"""
        self.latencia = random.randint(5,10)
                    
    @staticmethod
    def actualizar_csv (estado, archivo, posicion):
        """Input: Estado del router (String), Archivo csv, Posicion del router (Int)\n
        Funcion: Actualizar el archivo csv segun se modifiquen los routers\n
        Output: Nada"""
        datos = [[f"ROUTER_{posicion}", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), estado]]
        with open(archivo, "a") as file:
            escritor_csv = csv.writer(file)
            for fila in datos: 
                escritor_csv.writerow(fila)
    
    @staticmethod
    def generar_txt (posicion_llegada, mensaje, posicion_origen):
        """Input: Posicion de destino del mensaje (Int), mensaje (String), posicion de origen del mensaje (Int)\n
        Funcion: Generar un archivo de texto en el cual se visualice el mensaje enviado desde un Router a otro\n
        Output: Nada"""
        with open(f"router_{posicion_llegada}.txt", "a") as file:
            file.write(f"Origen: ROUTER_{posicion_origen}\n{mensaje}\n")
    
    def __str__(self):
        return f"ROUTER_{self.posicion}"
            
class Diccionario_Routers:
    
    def __init__(self):
        self.dict = {}
    
    def agregar_routers (self, cantidad):
        for i in range(1,cantidad+1):
            router = Router(i)
            router.activar_router()
            self.dict[router]=[]
        
    def crear_paquete (self, contenido, origen, destino):
        """Input: ...\n
        Funcion: Crea un paquete de informacion con el mensaje deseado\n
        Output: Nada"""
        paquete = Paquete(contenido, origen, destino)
        for router in self.dict.keys():
            if router.posicion == origen and router.estado == "ACTIVO":
                lista = self.dict[router] 
                lista.append(paquete)
                self.dict[router] = lista
                
    def enviar_paquete (self):
        """Input: ...\n
        Funcion: Manda un paquete al proximo Router\n
        Output: Nada"""
        for router in self.dict.keys():
            if router.estado == "ACTIVO":
                for paquetes in self.dict.values():
                    for paquete in paquetes:
                        if paquete.destino != router.posicion:
                            lista = self.dict[router] 
                            lista.remove(paquete)
                            self.dict[router] = lista
                            posicion_proximo = router.posicion + 1
                            for router in self.dict.keys():
                                if router.posicion == posicion_proximo:
                                    lista = self.dict[router] 
                                    lista.append(paquete)
                                    self.dict[router] = lista
                        
    def recibir_paquete (self, paquete):
        """Input: ...\n
        Funcion: Recibir un paquete\n
        Output: Nada"""
        self.paquetes_en_cola.append(paquete)  
               
    def procesar_paquete (self):
        """Input: ...\n
        Funcion: Procesar un paquete de informacion\n
        Output: True/Nada"""
        for paquete in self.paquetes_en_cola:
            if paquete.destino == self.posicion:
                print("Llegó a destino")
            else:
                self.enviar_paquete()
        time.sleep(0.1) # Con esto hacemos la latencia
        
diccionario = Diccionario_Routers()
diccionario.agregar_routers(5)
diccionario.crear_paquete("hola que tal", 3,4)
diccionario.enviar_paquete()
for i in diccionario.dict.items():
    print(i) 