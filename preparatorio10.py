class Productos:
    matriz = []
    size = []
    total_ofertas = 0

    def __init__(self, size):
        self.size = size
    
    def crearMatriz(self):
        self.matriz = []
        for i in range(self.size):
            fila = []
            for j in range(self.size):
                fila.append(None)
            self.matriz.append(fila)
    
    def llenarMatriz(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matriz[i][j] is None:
                    nombre = input("ingrese el nombre del producto: ")
                    oferta_str = input("El producto está en oferta? (s/n): ").lower()
                    oferta = True if oferta_str == 's' else False

                    self.matriz[i][j] = {
                        "nombre": nombre,
                        "oferta": oferta
                    }

                    if oferta == True:
                        self.total_ofertas += 1

    def mostrarMatriz(self):
        print("\nMatriz de productos:")
        for fila in self.matriz:
            print(fila)
        print("")

    def mostrarTotalOfertas(self):
        print("Total de productos en oferta:", self.total_ofertas)

productos = Productos(3)
productos.crearMatriz()
productos.llenarMatriz()
productos.mostrarMatriz()
productos.mostrarTotalOfertas()                        