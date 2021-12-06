#Entrada de datos
cadena = input("Introduce una cadena: ")
cadena2 = ""

#Sustitución de caracteres
for char in cadena:
    if "0" <= char <= "9":
        cadena2 += str(int(char)*2)
    else:
        cadena2 += char

#Salida de datos
print(cadena2)
