class Teatro:
    dimension=0
    matriz=[]
    
    def __init__(self, dimension):
        self.dimension=dimension 
    
    def crear(self):
        for i in range(self.dimension):
            filas=[]
            for j in range(self.dimension):
                filas.append(None)
            self.matriz.append(filas)
        
    def agregar_asiento(self, numero, fila, precio):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.matriz[i][j] is None:
                    self.matriz[i][j]=(numero, fila, precio)
                    return True
        return False
    
    def mostrar_asientos(self):
        print("   ")
        for x in self.matriz:
            print(x)
        print("   ")
    
    