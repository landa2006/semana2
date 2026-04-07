def transformar(texto, opcion):

    if opcion == 1:
        return texto.upper()
    else:
        if opcion == 2:
            return texto.lower()
        else:
            if opcion == 3:
                return texto.capitalize()


texto = input("Ingrese un texto: ")
opcion = int(input("Ingrese una opción (1,2,3): "))

resultado = transformar(texto, opcion)

print("Resultado:", resultado)
