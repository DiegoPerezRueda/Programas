lista = []
numero = int(input("Introduzca un número (<0 para salir): "))
suma = 0
resta = 0
while numero >= 0:
    lista.append(numero)
    numero = int(input("Introduzca un número (<0 para salir)"))
    
for i in range(len(lista)-1):
    if lista[i] < lista[i+1]:
        suma += lista[i+1] - lista[i]
    elif lista[i] > lista[i+1]:
        resta += lista[i+1] - lista[i]
        
print("El desnivel positivo es", suma, "y el negativo es", resta)
