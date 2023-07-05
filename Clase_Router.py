from Clase_paquete import *
from datetime import *
import csv

class Router:
    
    def __init__(self, posicion):
        self.estado = "AGREGADO"
        self.posicion = posicion
        self.paquetes_en_cola = []
        
    def enviar_paquete (self, contenido):
        """Input: Objeto router, Contenido del mensaje (String)\n
        Funcion: Enviar un paquete de informacion con el mensaje deseado al proximo nodo\n
        Output: Nada"""
        if self.estado == "ACTIVO":
            paquete = Paquete(mensaje = contenido)
            self.paquetes_en_cola.append(paquete)
       
    def procesar_paquete (self):
        """Input: Objeto router\n
        Funcion: Procesar un paquete de informacion\n
        Output: True/Nada"""
        if self.estado == "ACTIVO":
            for paquete in self.paquetes_en_cola:
                if paquete["destino"] == self.posicion:
                    return True
                else:
                    self.enviar_paquete(paquete)
            self.paquetes_en_cola = []
        else:
            # Acá habría que agregar toda la parte de la reparacion de nodos y los nodos inactivos...
            pass
        
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
        Funcion: Generar un archivo de texto en el cual se visualice el mensaje enviado desde un nodo a otro\n
        Output: Nada"""
        with open(f"router_{posicion_llegada}.txt", "a") as file:
            file.write(f"Origen: ROUTER_{posicion_origen}\n{mensaje}\n")
