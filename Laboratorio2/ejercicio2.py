def transformar_palabra(palabra, opcion):

    if opcion == 1:
        print(palabra.upper())
    else:
        if opcion == 2:
            print(palabra.lower())
        else:
            if opcion == 3:
                print(palabra.capitalize())


palabra = input("Ingrese una palabra: ")
opcion = int(input("Ingrese una opción (1,2,3): "))

transformar_palabra(palabra, opcion)
