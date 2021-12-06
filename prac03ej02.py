#Entrada de datos
cadena = input("Introduce una cadena: ")
cadena2 = ""
cambios = len(cadena)
ind = -1
#Contrucción de la cadena
while ind >= -len(cadena) and cadena[ind] == " ":#Quitando espacios al final
        cambios -= 1
        ind -= 1
for i in range(cambios):#Quitando espacios en medio y al principio
    if cadena[i] == " " and i + 1 < len(cadena):
        if cadena[i+1] != " " and len(cadena2) != 0:
            cadena2 += cadena[i]
    else:
        cadena2 += cadena[i]
print(cadena2)
