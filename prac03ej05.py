lista = []
numero = int(input("Introduzca un número (<0 para salir): "))
while numero >= 0:
    lista.append(numero)
    numero = int(input("Introduzca un número (<0 para salir)"))
maximo = lista[0]
minimo = lista[0]
for i in lista[1:]:
    if i > maximo:
        maximo = i
    elif i < minimo:
        minimo = i

print("El valor máximo es", maximo, "y el mínimo es", minimo)
