import random
matriz=[]
dim=5
def crear():
    for i in range(dim):
        fila=[]
        for j in range(dim):
            fila.append(random.randint(1,99))
        matriz.append(fila)
    return matriz



matriz= crear()
for x in matriz:
    print(x)
print("         ")


