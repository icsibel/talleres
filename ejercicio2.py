import random
matriz=[]
dimension=5
usados=set()

for i in range(dimension):
    filas=[]
    for j in range(dimension):
        num=random.randint(1,99)
        while num in usados:
            num=random.randint(1,99)
        usados.add(num)
        filas.append(num)
    matriz.append(filas)

for x in matriz:
    print(x)
print("          ")

mayor=[0][0]
pos= [0,0]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j]>mayor:
            mayor =matriz[i][j]
            pos=[i , j]

print(f"el numero mayor es: {mayor} y esta en la posicion: {pos}" )