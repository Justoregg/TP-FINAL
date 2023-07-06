class Nodo():
    def __init__(self, dato =None , prox =None):
        self.dato = dato
        self.prox = prox
        
    def __str__(self):
        return str(self.dato)
    
class Lista():
    def __init__(self):
        self.head = None
        self.len = 0
        
    def agregarinicio(self, nodo:Nodo):
        if (self.len) ==0:
            self.head = nodo
        else:
            nodo.prox = self.head
            self.head = nodo 
        self.len += 1
        
    def append(self, nodo:Nodo):
        if (self.len == 0):
            self.head = nodo
        else:
            nodomov=Nodo()
            nodomov=self.head
            while (nodomov.prox != None):
                nodomov = nodomov.prox
            nodomov.prox = nodo
        self.len += 1
        
    def pop(self, posicion = None):
        nodo = Nodo()
        nodo = self.head
        if posicion == None:
            final = self.len-2
            for i in range (posicion - 1):
                nodo = nodo.prox
                nodo.prox = None
        else:
            for i in range(posicion-1):
                nodo = nodo.prox
                nodo.prox = nodo.prox.prox
        self.len -= 1
        
    def __str__(self):
        nodo = self.head
        cadena = ""      
        if (self.len == 0):
            return "Lista Vacia"
        else:
            while nodo != None:
                cadena += str(nodo.dato) + "\t"
                nodo = nodo.prox
            return cadena         
if __name__ == "__main__":                
    lista1 = Lista()