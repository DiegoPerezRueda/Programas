#Entrada de datos
n = int(input("Introduce la dimension de la matriz: "))
matriz = []

#Construcción de la matriz
for i in range(n):
    fila = []
    for i2 in range(n):
        fila.append(int(input("Introduce un número: ")))
    matriz.append(fila)
print(matriz)
