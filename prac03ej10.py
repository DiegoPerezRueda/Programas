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
    for elem in matriz[0]:
        suma1 += elem
    sumaigual = True
    i = 1
    while sumaigual and i < n:
        suma2 = 0
        for elem in matriz[i]:
            suma2 += elem
        if suma2 != suma1:
            sumaigual = False
        i += 1
    if sumaigual:
        print("Suman:", suma1)
    else:
        print("No suma lo mismo")
