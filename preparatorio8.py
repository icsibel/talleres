class Almacen:
    matriz = []
    size = 0
    productos = []

    def __init__(self, size):
        self.size = size

    def crearMatriz(self):
        self.matriz = []
        for i in range(self.size):
            fila = []
            for j in range(self.size):
                fila.append(None)
            self.matriz.append(fila)
    
    def cargarListaProductos(self, lista_productos):
        self.productos = []
        for item in lista_productos:
            self.productos.append(item)

    def agruparPorCategoria(self):
        grupos = {}
        for i in range(len(self.productos)):
            prod = self.productos[i]
            cat = prod["categoria"]

            if cat not in grupos:
                grupos[cat] = []

            grupos[cat].append(prod)

        return grupos
    
    def llenarMatrizPorCategorias(self):
        grupos = self.agruparPorCategoria()

        categorias = []
        for cat in grupos:
            categorias.append(cat)

        lista_lineal = []
        for i in range(len(categorias)):
            cat_actual = categorias[i]
            vector_de_cat = grupos[cat_actual]
            for j in range(len(vector_de_cat)):
                lista_lineal.append(vector_de_cat[j])

        indice = 0
        capacidad = self.size * self.size
        for i in range(self.size):
            for j in range(self.size):
                if indice < len(lista_lineal) and indice < capacidad:
                    self.matriz[i][j] = lista_lineal[indice]
                    indice += 1
                else:
                    self.matriz[i][j] = None

    def mostrar_matriz(self):
        print("Matriz de estanterías:")
        for i in range(self.size):
            print(self.matriz[i])
        print("")

    def mostrar_productos_por_categoria(self):
        grupos = self.agruparPorCategoria()
        print("Productos agrupados por categoría:")
        for cat, prod in grupos.items():
            print("\n")
            print("Categoría:", cat)
            print(prod)
        print("")

lista = [
    {"nombre": "Arroz",   "peso": 1.0, "categoria": "Granos"},
    {"nombre": "Lentejas","peso": 0.5, "categoria": "Granos"},
    {"nombre": "Manzana", "peso": 0.2, "categoria": "Frutas"},
    {"nombre": "Banano",  "peso": 0.25,"categoria": "Frutas"},
    {"nombre": "Leche",   "peso": 1.0, "categoria": "Lacteos"},
    {"nombre": "Yogur",   "peso": 0.2, "categoria": "Lacteos"},
    {"nombre": "Gaseosa", "peso": 1.5, "categoria": "Bebidas"},
    {"nombre": "Agua",    "peso": 0.6, "categoria": "Bebidas"},
]

almacen = Almacen(3)
almacen.crearMatriz()
almacen.cargarListaProductos(lista)
almacen.mostrar_productos_por_categoria()
almacen.llenarMatrizPorCategorias()
almacen.mostrar_matriz()