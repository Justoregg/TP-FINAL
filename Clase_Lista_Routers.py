from Clase_Router import * 

class ListaRouters():
    
    def __init__(self):
        """HACER LOS DOCSTRINGS"""
        self.head = None
        self.len = 0   
        
    def agregar_router(self, router:Router):
        if (self.len) ==0:
            self.head = router
        else:
            router.prox = self.head
            self.head = router 
        self.len += 1
        
    def append_router(self, router:Router):
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
    
    def enviar_mensaje(self,mensaje):   #Completarlo bien
        routertrans=mensaje.origen
        while routertrans!=mensaje.destino:
            if routertrans.estado=="ACTIVO":
                routertrans.recibir_mensaje()
                routertrans.enviar_mensaje()
            else:
                #Hay que hacer el bypass acá
                pass
            routertrans=routertrans.prox
        routertrans.finalizar_mensaje(mensaje)
        
    def __str__(self):  #Hace falta?
        router = self.head
        cadena = " "      
        if (self.len == 0):
            return "Lista Vacia"
        else:
            while router != None:
                router += str(router.dato) + "\t"
                router = router.prox
            return cadena