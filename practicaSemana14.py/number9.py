def suma_pares(lista):
    suma = 0

    for numero in lista:
        if numero % 2 == 0:
            suma += numero

    return suma


numeros = [2, 5, 8, 7, 10, 3]

print("Suma de números pares:", suma_pares(numeros))
