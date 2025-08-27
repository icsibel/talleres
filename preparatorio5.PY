class Tienda:

    def __init__(self, dimension):
        self.dimension=dimension
        self.matriz1=[]
        self.matriz2=[]

    def crear_m1(self):
        print("MATRIZ 1")
        self.matriz1=[]
        for i in range(self.dimension):
            fila=[]
            for j in range(self.dimension):
                nombre=input("ingrese nombre del producto: ")
                precio=int(input("ingrese el precio del producto: "))
                stock=int(input("ingrese la cantidad de productos disponibles: "))
                fila.append({"nombre": nombre, "precio": precio, "stock":stock})
                print("   ")
            self.matriz1.append(fila)

    def crear_m2(self):
        print("MATRIZ 2")
        self.matriz2=[]
        for i in range(self.dimension):
            fila=[]
            for j in range(self.dimension):
                nombre=input("ingrese nombre del producto: ")
                precio=int(input("ingrese el precio del producto: "))
                stock=int(input("ingrese la cantidad de productos disponibles: "))
                fila.append({"nombre": nombre, "precio":precio, "stock":stock})
                print(" ")
            self.matriz2.append(fila)
        return self.matriz2
    
    def mostrar_matrices(self):
        print("MATRIZ 1")
        for x in self.matriz1:
            print(x)
        print("  ")
        print("MATRIZ 2")
        for x in self.matriz2:
            print(x)
        print("   ")
    
    def fucionar_matrices(self):
        productos=[]
        for fila in self.matriz1:
            for producto in fila:
                productos.append(producto)

        for fila in self.matriz2:
            for producto in fila:
                productos.append(producto)
        
        fusion={}
        for producto in productos:
            nombre=producto["nombre"]
            if nombre not in fusion:
                fusion[nombre]={"nombre":nombre, "precio":producto["precio"], "stock": producto["stock"]}
            else:
                fusion[nombre]["stock"]+= producto["stock"]
        
        filas=[]
        nueva_matriz=[]
        contador=0
        for producto in fusion.values():
            filas.append(producto)
            contador+=1
            if contador == self.dimension:
                nueva_matriz.append(filas)
                filas=[]
                contador=0
        if fila:  
            nueva_matriz.append(filas)

        print("MATRIZ FUSIONADA")
        for x in nueva_matriz:
            print(x)

dimension=int(input("ingrese dimension de las matrices: "))
t=Tienda(dimension)
t.crear_m1()
t.crear_m2()
t.mostrar_matrices()
t.fucionar_matrices()