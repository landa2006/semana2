def contar_pares_impares(lista):
    pares = 0
    impares = 0

    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares


numeros = [10, 7, 4, 9, 12, 3, 8]

pares, impares = contar_pares_impares(numeros)

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
