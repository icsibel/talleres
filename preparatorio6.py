class Supermercado:
    matriz = []
    size = 0

    def __init__(self, size):
        self.size = size

    def crearMatriz(self):
        for i in range(self.size):
            fila = []
            for j in range(self.size):
                fila.append(None)
            self.matriz.append(fila)

    def llenarMatriz(self):
        count = 1
        for i in range(self.size):
            for j in range(self.size):
                if self.matriz[i][j] is None:
                    nombre = input("ingrese el nombre del producto: ")
                    precio = input("Ingrese el precio del producto: ")
                    disponibilidad = True if (count % 2 == 0) else False
                    self.matriz[i][j] = {
                        "nombre": nombre,
                        "precio": precio,
                        "disponibilidad": disponibilidad,
                    }
                    count += 1

    def filtrarMatriz(self):
        nueva_matriz = []
        for i in range(self.size):
            nueva_fila = []
            for j in range(self.size):
                producto = self.matriz[i][j]
                if producto["disponibilidad"] == True:
                    nueva_fila.append(producto)
            nueva_matriz.append(nueva_fila)
        return nueva_matriz
    
    def mostrar_matriz_original(self):
        print("         ")
        for x in self.matriz:
            print(x)
        print("         ")

    def mostrar_nueva_matriz(self, matriz):
        print("")
        for x in matriz:
            print(x)
        print("  ")
    
almacen = Supermercado(3)
almacen.crearMatriz()
almacen.llenarMatriz()
almacen.mostrar_matriz_original()
matriz_filtrada = almacen.filtrarMatriz()
almacen.mostrar_nueva_matriz(matriz_filtrada)

