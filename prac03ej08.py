subida = True
lista = []
listamax = []


numero = int(input("Introduzca un número (<0 para salir): "))
i = 1
while numero >= 0:
    lista.append(numero)
    numero = int(input("Introduzca un número (<0 para salir)"))

    
listaactual = [lista[0]]


while i < len(lista):
    if lista[i] > listaactual[-1]:
        listaactual.append(lista[i])
    else:
        if len(listaactual) > len(listamax):
            listamax = listaactual
        listaactual = [lista[i]]
    i += 1
    
if len(listaactual) > len(listamax):
    listamax = listaactual
    
if len(listamax) > 1:
    print("El tramo de subida más largo es", listamax)
else:
    print("No hay tramos de subida")
