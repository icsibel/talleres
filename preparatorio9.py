class Ventas:
    matriz = []
    size_filas = 0
    size_columnas = 0
    vendedores = []

    def __init__(self, filas, columnas):
        self.size_filas = filas
        self.size_columnas = columnas
        self.matriz = []
        self.vendedores = []

    def crearMatriz(self):
        self.matriz = []
        for i in range(self.size_filas):
            fila = []
            for j in range(self.size_columnas):
                fila.append(0)
            self.matriz.append(fila)

    def llenarMatriz(self):
        print("Ingrese los datos de las ventas de cada vendedor (12 meses).")
        for i in range(self.size_filas):
            nombre = input(f"Ingrese el nombre del vendedor {i+1}: ")
            self.vendedores.append(nombre)
            for j in range(self.size_columnas):
                valor = int(input(f"Ventas de {nombre} en el mes {j+1}: "))
                self.matriz[i][j] = valor

    def calcularMayorVenta(self):
        mayor = 0
        vendedor_mayor = ""
        for i in range(self.size_filas):
            suma = 0
            for j in range(self.size_columnas):
                suma += self.matriz[i][j]
            print(f"Total anual de {self.vendedores[i]}: {suma}")
            if suma > mayor:
                mayor = suma
                vendedor_mayor = self.vendedores[i]
        print("\nEl vendedor con mayores ventas es:", vendedor_mayor, "con un total de", mayor)

    def mostrarMatriz(self):
        print("Matriz de ventas:")
        for fila in self.matriz:
            print(fila)
        print("")

ventas = Ventas(5, 12)
ventas.crearMatriz()
ventas.llenarMatriz()
ventas.mostrarMatriz()
ventas.calcularMayorVenta()