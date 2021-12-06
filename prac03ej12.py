#Entrada de datos
n = int(input("Introduce la dimension de la matriz: "))
matriz = []

#Construcción de la matriz
for i in range(n):
    fila = []
    for i2 in range(n):
        fila.append(int(input("Introduce un número: ")))
    matriz.append(fila)

#Caso 1
if n == 1:
    print("Suman:", matriz[0][0])
else: #Caso 2
    suma1 = 0
    for elem in matriz[0]:#Suma de la primera fila
        suma1 += elem
    sumaigual = True
    i = 1
    while sumaigual and i < n:#Suma de las filas
        suma2 = 0
        for elem in matriz[i]:
            suma2 += elem
        if suma2 != suma1:
            sumaigual = False
        i += 1
    i = 0
    while sumaigual and i < n:#Suma de columnas
        suma2 = 0
        for i2 in range(n):
            suma2 += matriz[i2][i]
        if suma2 != suma1:
            sumaigual = False
        i += 1
    suma2 = 0
    for i in range(n):
        suma2 += matriz[i][i]
    if suma2 != suma1:
        sumaigual = False
    else:
        suma2 = 0
        for i in range(n):
            suma2 += matriz[i][n - (i+1)]
        if suma2 != suma1:
            sumaigual = False
    if sumaigual:
        print("Es un cuadrado mágico que suma:", suma1)
    else:
        print("No es un cuadrado mágico")
