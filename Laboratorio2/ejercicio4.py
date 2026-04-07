def transformar_lista(lista, opcion):

    nueva_lista = []

    for palabra in lista:

        if opcion == 1:
            nueva_lista.append(palabra.upper())
        else:
            if opcion == 2:
                nueva_lista.append(palabra.lower())
            else:
                if opcion == 3:
                    nueva_lista.append(palabra.capitalize())

    return nueva_lista


texto = input("Ingrese palabras separadas por espacio: ")
opcion = int(input("Ingrese una opción (1,2,3): "))

lista = texto.split()

resultado = transformar_lista(lista, opcion)

print(resultado)
