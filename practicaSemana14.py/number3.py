def calcular_promedio(notas):
    suma = 0

    for nota in notas:
        suma += nota

    promedio = suma / len(notas)
    return promedio


notas = [8, 7, 9, 10, 10]

promedio = calcular_promedio(notas)

print("Promedio:", promedio)

if promedio >= 6:
    print("El grupo aprueba")
else:
    print("El grupo reprueba")
