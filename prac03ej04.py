cadena = input("Introduce una cadena: ")
cadena2 = input("Introduce otra cadena: ")
i = 0
prefijo = True
if len(cadena) >= len(cadena2):
    prefijo = False
else:
    while i < len(cadena) and prefijo:
        if cadena[i] != cadena2[i]:
            prefijo = False
        i += 1
if prefijo:
    print("Es prefijo")
else:
    print("No es prefijo")
