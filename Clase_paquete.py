from datetime import * 

class Paquete:
    def __init__(self, mensaje, origen, destino):
        self.mensaje = mensaje
        self.origen = origen
        self.destino = destino
        self.hora_de_emision = datetime.now()
        self.llegada_a_destino = False
        
