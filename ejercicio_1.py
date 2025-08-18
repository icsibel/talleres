import random
matriz=[]
dimension=6
def crear():
    for i in range(dimension):
        filas=[]
        for j in range(dimension):
            filas.append(random.randint(1,99))
        matriz.append(filas)
    return matriz


def sumar(suma):
    suma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma+=matriz[i][j]
    return suma


crear()
for x in matriz:
    print(x)
print("         ")
suma=sumar(matriz)
print(f"la suma de los elementos de la matriz es: {suma}")

