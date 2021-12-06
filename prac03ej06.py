subida = True
lista = []
numero = int(input("Introduzca un número (<0 para salir): "))
i = 0
while numero >= 0:
    lista.append(numero)
    numero = int(input("Introduzca un número (<0 para salir)"))
while i < len(lista) - 1 and subida == True:
    if lista[i] > lista[i+1]:
        subida = False
    i += 1
if subida:
    print("La ruta es de subida.")
else:
    print("La ruta no es de subida.")
