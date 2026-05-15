def ordenar_lista(lista):
    n = len(lista)

    for i in range(n):
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

    return lista


numeros = []

for i in range(6):
    num = int(input(f"Ingrese número {i+1}: "))
    numeros.append(num)

print("Lista ordenada:", ordenar_lista(numeros))
