from Clase_Router import * 

class ListaRouters():
    
    def __init__(self):
        self.head = None
        self.len = 0   
        
    def agregar_router (self, router:Router):
        """Input: objeto lista, objeto router\n
        Funcion: agregar un router a la lista enlazada\n
        Output: nada"""
        if (self.len == 0):
            self.head = router
        else:
            routertrans=self.head
            while (routertrans.prox != None):
                routertrans = routertrans.prox
            routertrans.prox = router
            router.anterior = routertrans
        self.len += 1
        
    def __str__(self):  
        router = self.head
        cadena = " "      
        if (self.len == 0):
            return "Lista Vacia"
        else:
            while router != None:
                cadena += router.__str__() + "\t"
                router = router.prox
            return cadena
