import random


def contar_mayores(lista):
    contador = 0

    for numero in lista:
        if numero > 50:
            contador += 1

    return contador


numeros = []

for i in range(10):
    numeros.append(random.randint(1, 100))

print("Números generados:", numeros)
print("Mayores a 50:", contar_mayores(numeros))
