class Tienda:
    dimension=0
    matriz=[]
    producto=""
    cantidad=0

    def __init__(self,dimension):
        self.dimension=dimension
    
    def crear(self):
        for i in range (self.dimension):
            filas=[]
            for j in range(self.dimension):
                self.producto=input("ingrese el producto a agregar: ")
                self.cantidad=int(input("ingrese cantidad del producto: "))
                filas.append({"producto":self.producto, "cantidad":self.cantidad})
            self.matriz.append(filas)

    def inventario(self):
        total=0
        for i in range(len(self.matriz)):
            for producto in self.matriz[i]:
                total+=producto["cantidad"]
        print("INVENTARIO")
        print(f"el total de productos: {total}")

productos=Tienda(2)
productos.crear()
productos.inventario()
