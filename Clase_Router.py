from Clase_paquete import *
from datetime import *
import time
import csv
import random 

class Router:
    cantidad_routers = 0 
    routers_activos = set()
    
    def __init__(self, paquete):
        self.estado = "AGREGADO"
        self.paquete = paquete
        self.latencia = 0 
        self.posicion = Router.cantidad_routers + 1     
        self.prox = None
        self.mensajes_retransmitidos = 0 
        self.mensajes_en_destino = 0 
        self.lista_mensajes_en_destino = []
        
    def activar_router (self):
        """Input: Objeto router\n
        Funcion: Cambiar el estado del router a activo\n
        Output: Nada"""
        if self.estado != "ACTIVO":
            Router.routers_activos.add(self.posicion)
            self.estado = "ACTIVO"
            
    def deactivar_router (self):
        """Input: Objeto router\n
        Funcion: Cambiar el estado del router a inactivo\n
        Output: Nada"""
        if self.estado != "INACTIVO":
            Router.routers_activos.discard(self.posicion)
            self.estado = "INACTIVO"
    
    def resetear_router (self):
        """Input: Objeto router\n
        Funcion: Resetear un router\n
        Output: Nada"""
        self.latencia = random.randint(5,10)
    
    def recibir_mensaje (self):
        self.mensajes_retransmitidos += 1
    
    def enviar_mensaje (self):
        pass
    
    def finalizar_mensaje (self, mensaje):
        self.lista_mensajes_en_destino.append(mensaje)
        self.mensajes_en_destino += 1
    
    @staticmethod
    def generar_mensaje (): # Se puede hacer más complejo...
        mensaje = random.choice(["Hola que tal", "Soy un Router", "Como va todo?"])
        return mensaje
    
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
