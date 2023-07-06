from Clase_paquete import *
from datetime import *
import time
import csv
import random 

class Router:
    
    def __init__(self, posicion):
        self.estado = "AGREGADO"
        self.posicion = posicion
        self.paquetes_en_cola = []  # Habría que usar una lista enlazada o algo del estilo
        self.latencia = 0 
        
    def enviar_paquete (self, contenido, origen, destino):
        """Input: Objeto router, Contenido del mensaje (String)\n
        Funcion: Enviar un paquete de informacion con el mensaje deseado al proximo Router\n
        Output: Nada"""
        if self.estado == "ACTIVO":
            paquete = Paquete(contenido, origen, destino)
            self.paquetes_en_cola.append(paquete)
    
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
    
    def recibir_paquete (self, paquete):
        """Input: Objeto router, paquete de informacion\n
        Funcion: Recibir un paquete\n
        Output: Nada"""
        self.paquetes_en_cola.append(paquete)
               
    def procesar_paquete (self):
        """Input: Objeto router\n
        Funcion: Procesar un paquete de informacion\n
        Output: True/Nada"""
        if self.estado == "ACTIVO":
            if self.latencia > 0: 
                self.latencia -=1
            elif self.paquetes_en_cola:
                paquete = self.paquetes_en_cola.pop(0)
                time.sleep(0,1) # Con esto hacemos la latencia
                if paquete.destino == self.posicion:
                    return True
                else:
                    self.enviar_paquete(paquete)
                    proximo_router = routers[self.posicion + 1]    ## La lista de routers esta en simulacion, por eso el error
                    proximo_router.recibir_paquete(paquete)
                    
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
            
class ListaRouters():
    def __init__(self):
        self.head = None
        self.len = 0   
    def agregarrouter(self, router:Router):
        if (self.len) ==0:
            self.head = router
        else:
            router.prox = self.head
            self.head = router 
        self.len += 1
    def append(self, router:Router):
        if (self.len == 0):
            self.head = router
        else:
            routertrans=Router()
            routertrans=self.head
            while (routertrans.prox != None):
                routertrans = routertrans.prox
            routertrans.prox = router
        self.len += 1
    def pop(self, posicion = None):
        router = Router()
        router = self.head
        if posicion == None:
            final = self.len-2
            for i in range (posicion - 1):
                router = router.prox
                router.prox = None
        else:
            for i in range(posicion-1):
                router = router.prox
                router.prox = router.prox.prox
        self.len -= 1
    def __str__(self):
        router = self.head
        cadena = ""      
        if (self.len == 0):
            return "Lista Vacia"
        else:
            while router != None:
                router += str(router.dato) + "\t"
                router = router.prox
            return cadena