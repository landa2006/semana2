def transformar(texto, opcion):

    if opcion == 1:
        return texto.upper()
    else:
        if opcion == 2:
            return texto.lower()
        else:
            if opcion == 3:
                return texto.capitalize()
            else:
                return "Opción inválida"


texto = input("Ingrese un texto: ")

print("1. Convertir a MAYÚSCULAS")
print("2. Convertir a minúsculas")
print("3. Primera letra mayúscula")

opcion = int(input("Seleccione una opción: "))

resultado = transformar(texto, opcion)

print("Resultado:", resultado)
