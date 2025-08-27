class Almacen:
    dimension=0
    matriz=[]
    def __init__(self, dimension ):
        self.dimension=dimension

    def crear(self):
        self.matriz = []
        for i in range(self.dimension):
            filas=[]
            for j in range(self.dimension):
                filas.append(None)
            self.matriz.append(filas)

    def agregar_producto(self, nombre, precio, cantidad):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.matriz[i][j] is None:
                    self.matriz[i][j]={"nombre":nombre,"precio": precio, "cantidad": cantidad}
                    return True
        return False

    def mostrar_almacen(self):
        print('                               ')
        for x in self.matriz:
            print(x)
        print('                               ')

    def buscar(self, nombre):
        for i in range(self.dimension):
            for j in range(self.dimension):
                producto= self.matriz[i][j]
                if producto["nombre"] == nombre:
                    print(f"el producto: {producto} esta en la fila: {i} y en la columna: {j}")
                    return (i,j)
                
        return None


almacen=Almacen(3)
almacen.crear()
almacen.agregar_producto("arroz", 2500, 40)
almacen.agregar_producto("huevos", 30000, 12)
almacen.agregar_producto("leche", 3000, 50)
almacen.agregar_producto("manzanas", 4500, 10)
almacen.agregar_producto("sal", 2000, 35)
almacen.agregar_producto("pan", 3000, 1)
almacen.agregar_producto("salchichas", 2700, 5)
almacen.agregar_producto("mangos", 5000, 15)
almacen.agregar_producto("arepas", 1800, 3)
almacen.mostrar_almacen()
almacen.buscar("mangos")


