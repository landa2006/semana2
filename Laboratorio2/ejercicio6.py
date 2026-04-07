def transformar_y_contar(texto, opcion):

    if opcion == 1:
        resultado = texto.upper()
    else:
        if opcion == 2:
            resultado = texto.lower()
        else:
            if opcion == 3:
                resultado = texto.capitalize()

    return len(resultado)


texto = input("Ingrese un texto: ")
opcion = int(input("Ingrese una opción (1,2,3): "))

cantidad = transformar_y_contar(texto, opcion)

print("Cantidad de caracteres:", cantidad)
