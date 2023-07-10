from datetime import * 
from Validaciones import *

class Paquete:
    def __init__(self, mensaje = input("ingrese el mensaje"), posicion_origen = int(input("ingrese origen")), posicion_destino = int(input("ingrese destino"))):
        self.mensaje = mensaje
        self.posicion_origen = posicion_origen
        self.posicion_destino = posicion_destino
        self.hora_de_emision = datetime.now()
        self.llegada_a_destino = False
        
    def __str__(self):
        return f"Origen: router_{self.posicion_origen}\n{self.mensaje}\nDestino: router_{self.posicion_destino}\n"

         
            
                
                
        
        


        
