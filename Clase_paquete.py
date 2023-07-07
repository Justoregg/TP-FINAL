from datetime import * 
from Validaciones import *

class Paquete:
    def __init__(self, mensaje = None, origen = None, destino= None):
        self.mensaje = mensaje
        self.origen = origen
        self.destino = destino
        self.hora_de_emision = datetime.now()
        self.llegada_a_destino = False
        
#     @staticmethod    
#     def escribir_mensaje():
#         if mensaje == None:
#             mensaje== input("ingrese el mensaje a enviar")
    
#     def camino_paquete(self):
#         if self.origen== None:
#             p_origen =input("ingrese el numero del router origen")
#             if validacion_Router(p_origen) == True:
#                 self.origen == p_origen
#         if self.destino == None:
#             p_destino =input("ingrese el numero del router destino")
#             if validacion_Router(p_destino) == True:
#                 self.destino == p_destino
    
#     escribir_mensaje(self)
#     camino_paquete(self)  
# mensaje2 = Paquete()
            
            
                
                
        
        


        
