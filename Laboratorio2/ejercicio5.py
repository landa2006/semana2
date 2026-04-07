def transformar_texto(texto, opcion):

    if opcion == 1:
        print(texto.upper())
    else:
        if opcion == 2:
            print(texto.lower())
        else:
            if opcion == 3:
                print(texto.capitalize())
            else:
                print("Opción inválida")


texto = input("escriba un texto: ")
opcion = int(input("elija una opción: "))

transformar_texto(texto, opcion)
