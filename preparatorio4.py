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
                    self.matriz[i][j]={"numero": numero, "fila": fila, "precio":precio}
                    return True
        return False 
    
    def mostrar_asientos(self):
        print("   ")
        for x in self.matriz:
            print(x)
        print("   ")
    
    def ordenar_matriz(self):
        for i in range(self.dimension):
            fila = self.matriz[i]
            num = len(fila)
            for a in range(num -1):
                for b in range(num - 1 - a):
                    if fila[b]["precio"] > fila[b + 1]["precio"]:
                        temp = fila[b]
                        fila[b] = fila[b + 1]
                        fila[b + 1] = temp
            self.matriz[i] = fila



teatro=Teatro(3)
teatro.crear()
teatro.agregar_asiento(3, 4, 5000)
teatro.agregar_asiento(5, 6, 4000)
teatro.agregar_asiento(1, 2, 8000)
teatro.agregar_asiento(9, 7, 1000)
teatro.agregar_asiento(6, 3, 100)
teatro.agregar_asiento(7, 2, 2000)
teatro.agregar_asiento(2, 5, 42000)
teatro.agregar_asiento(8, 3, 3000)
teatro.agregar_asiento(4, 1, 10000)
teatro.mostrar_asientos()
teatro.ordenar_matriz()
teatro.mostrar_asientos()
    