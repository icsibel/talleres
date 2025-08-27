class Libreria:
    matriz=[]
    dimension=0
    def __init__(self,dimension):
        self.dimension=dimension
    
    def crear(self):
        self.matriz=[]
        for i in range(self.dimension):
            filas=[]
            for j in range(self.dimension):
                filas.append(None)
            self.matriz.append(filas)
    
    def agregar_libro(self,titulo, autor, precio):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.matriz[i][j] is None:
                    self.matriz[i][j]={"titulo":titulo, "autor":autor, "precio": precio}
                    return True
        return False

    def mostrar_libreria(self):
        print("             ")
        for x in self.matriz:
            print(x)
        print("           ")
    
    def buscar_libro(self):
        mas_caro=None
        for i in range(self.dimension):
            for j in range(self.dimension):
                libro=self.matriz[i][j]
                if libro is not None:
                    if mas_caro is None or libro["precio"]>mas_caro["precio"]:
                        mas_caro=libro
        print(f"el libro mas caro es {mas_caro}")

libreria=Libreria(2) 
libreria.crear()
libreria.agregar_libro("metamorfosis", "frank kafka", 70000)
libreria.agregar_libro("la odisea", "Homero", 50000)
libreria.agregar_libro("100 años de soledad", "gabriel garcia marquez", 100000)
libreria.agregar_libro("fahrenheit 451", " ray bradbury", 60000)

libreria.mostrar_libreria()
libreria.buscar_libro()

                

                


        
        