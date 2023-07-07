from Clase_paquete import *
from datetime import *
import time 
import csv
import random 

class Router:
    cantidad_routers = 1 
    routers_activos = set()
    
    def __init__(self):
        self.estado = "AGREGADO"
        self.latencia = 0 
        self.posicion = Router.cantidad_routers 
        Router.cantidad_routers += 1
        self.prox = None
        self.anterior = None
        self.mensajes_retransmitidos = 0 
        self.mensajes_en_destino = 0 
        self.lista_mensajes_en_destino = []
        self.lista_mensajes_por_router = []
        
    def activar_router (self):
        """Input: Objeto router\n
        Funcion: Cambiar el estado del router a activo\n
        Output: Nada"""
        if self.estado != "ACTIVO":
            Router.routers_activos.add(self.posicion)
            self.estado = "ACTIVO"
        else:
            return "El router ya se encuentra activo"
            
    def desactivar_router (self):
        """Input: Objeto router\n
        Funcion: Cambiar el estado del router a inactivo\n
        Output: Nada"""
        if self.estado != "INACTIVO":
            Router.routers_activos.discard(self.posicion)
            self.estado = "INACTIVO"
        else:
            return "El router ya se encuentra inactivo"
    
    def resetear_router (self):
        """Input: Objeto router\n
        Funcion: Resetear un router\n              
        Output: Nada"""                             
        if self.estado != "ACTIVO" and self.estado != "INACTIVO":
            self.estado = "EN RESET"
        else:
            return "El router se está reseteando"
        
    def recibir_mensaje (self, paquete):
        """Input: Objeto router, objeto paquete\n
        Funcion: Recibir un mensaje desde un router y enviarlo a otro si corresponde\n
        Output: nada"""
        self.mensajes_retransmitidos += 1
        if self.estado == "ACTIVO":
            if self.posicion != paquete.posicion_destino: 
                self.lista_mensajes_por_router.append(paquete)
                self.enviar_paquete(paquete)
            else:
                self.finalizar_mensaje(paquete)
        else:
            if self.posicion != paquete.posicion_destino: 
                self.enviar_paquete(paquete)
            else:
                return "No llegó a destino"
        
    def enviar_paquete (self, paquete):
        """Input: objeto router, objeto paquete\n
        Funcion: Enviar un paquete hacia otro router\n
        Output: nada"""
        if self.estado == "ACTIVO":
            if paquete.posicion_destino > self.posicion:
                self.prox.recibir_mensaje(paquete)
            else:
                self.anterior.recibir_mensaje(paquete)
        else:
            print("No puede enviar mensajes desde un router inactivo")
            
    def finalizar_mensaje (self, mensaje):
        """Input objeto router, objeto paquete\n
        Funcion: Finaliza el envio de un mensaje de un router a otro una vez llegó a su destino\n
        Output: nada"""
        self.lista_mensajes_en_destino.append(mensaje)
        self.mensajes_en_destino += 1
    
    def actualizar_csv (self, archivo):
        """Input: Estado del router (String), Archivo csv, Posicion del router (Int)\n
        Funcion: Actualizar el archivo csv segun se modifiquen los routers\n
        Output: Nada"""
        datos = [[f"ROUTER_{self.posicion}", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.estado]]
        with open(archivo, "a") as file:
            escritor_csv = csv.writer(file)
            for fila in datos: 
                escritor_csv.writerow(fila)
    
    def generar_txt (self):
        """Input: Posicion de destino del mensaje (Int), mensaje (String), posicion de origen del mensaje (Int)\n
        Funcion: Generar un archivo de texto en el cual se visualice el mensaje enviado desde un Router a otro\n
        Output: Nada"""
        with open(f"router_{self.posicion}.txt", "w") as file:
            for paquete in self.lista_mensajes_en_destino:
                file.write(paquete.__str__())
            for paquete in self.lista_mensajes_por_router:
                file.write(paquete.__str__())
            
    def __str__(self):
        return f"ROUTER_{self.posicion}"
