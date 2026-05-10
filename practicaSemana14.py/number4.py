def encontrar_mayor(lista):
    mayor = lista[0]

    for numero in lista:
        if numero > mayor:
            mayor = numero

    return mayor


numeros = []

for i in range(8):
    num = int(input(f"Ingrese número {i+1}: "))
    numeros.append(num)

print("El número mayor es:", encontrar_mayor(numeros))
