class Router:
    
    def __init__(self, posicion):
        self.estado = "AGREGADO"
        self.posicion = posicion
        self.paquetes_en_cola = []
        
    def enviar_paquete (self, paquete):
        if self.estado == "ACTIVO":
            self.paquetes_en_cola.append(paquete)
       
    def procesar_paquete (self):
        if self.estado == "ACTIVO":
            for paquete in self.paquetes_en_cola:
                if paquete["destino"] == self.posicion:
                    return True
                else:
                    self.enviar_paquete(paquete)
            self.paquetes_en_cola = []
                    
            
