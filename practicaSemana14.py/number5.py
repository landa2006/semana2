def numeros_positivos(lista):
    positivos = []

    for numero in lista:
        if numero > 0:
            positivos.append(numero)

    return positivos


numeros = [-5, 10, -2, 8, 0, 15, -1]

print("Números positivos:", numeros_positivos(numeros))
