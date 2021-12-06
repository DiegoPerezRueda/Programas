from string import punctuation

#Entrada de datos
cadena = input("Introduce una cadena: ")
cadena2 = ""
cambios = len(cadena)
ind = -1

#Contrucción de la cadena
while ind >= -len(cadena) and (cadena[ind] in punctuation or cadena[ind] == " "):#Quitando espacios y caracteres al final
    cambios -= 1
    ind -= 1

for i in range(cambios):#Quitando espacios y caracteres en medio y al principio
    if not(cadena[i] in punctuation) and not(cadena[i] == " " and i + 1 < len(cadena)):
        cadena2 += cadena[i]
    elif cadena[i] == " " and i + 1 < len(cadena):
        if cadena[i+1] != " " and len(cadena2) != 0:
            cadena2 += cadena[i]


print(cadena2)
