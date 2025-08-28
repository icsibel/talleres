class Aula:
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
        for i in range(self.size):
            for j in range(self.size):
                if self.matriz[i][j] is None:
                    nombre = input("ingrese el nombre del estudiante: ")
                    calificacion_input = input("Ingrese la calificación del estudiante: \n1. A \n2. B \n3. C \n")
                    while calificacion_input != "1" and calificacion_input != "2" and calificacion_input != "3":
                        print("Ingresaste una opción invalida")
                        calificacion_input = input("Ingrese la calificación del estudiante: \n1. A \n2. B \n3. C \n")
                    
                    match calificacion_input:
                        case "1":
                            calificacion = "A"
                        case "2":
                            calificacion = "B"
                        case "3":
                            calificacion = "C"
                    
                    self.matriz[i][j] = {
                        "nombre": nombre,
                        "calificacion": calificacion
                    }

    def clasificacion_estudiantes(self):
        matriz_A = []
        matriz_B = []
        matriz_C = []

        for i in range(self.size):
            fila_A = []
            fila_B = []
            fila_C = []
            for j in range(self.size):
                fila_A.append(None)
                fila_B.append(None)
                fila_C.append(None)
            matriz_A.append(fila_A)
            matriz_B.append(fila_B)
            matriz_C.append(fila_C)
        
        for i in range(self.size):
            for j in range(self.size):
                estudiante = self.matriz[i][j]
                if estudiante["calificacion"] == "A":
                    matriz_A[i][j] = estudiante
                elif estudiante["calificacion"] == "B":
                    matriz_B[i][j] = estudiante
                else:
                    matriz_C[i][j] = estudiante

        grupos = {
            "A": matriz_A,
            "B": matriz_B,
            "C": matriz_C
        }
        return grupos
    
    def mostrar_matriz_original(self):
        print("         ")
        for x in self.matriz:
            print(x)
        print("         ")

    def mostrar_grupo(self, letra, matriz_grupo):
        print("Grupo de calificación:", letra)
        for fila in matriz_grupo:
            print(fila)
        print("")

escuela = Aula(2)
escuela.crearMatriz()
escuela.llenarMatriz()
print("Matriz original de estudiantes:")
escuela.mostrar_matriz_original()
grupos = escuela.clasificacion_estudiantes()
escuela.mostrar_grupo("A", grupos["A"])
escuela.mostrar_grupo("B", grupos["B"])
escuela.mostrar_grupo("C", grupos["C"])