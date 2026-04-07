def transformar_varias(texto, lista_opciones):

    resultado = texto

    for opcion in lista_opciones:

        if opcion == 1:
            resultado = resultado.upper()
        else:
            if opcion == 2:
                resultado = resultado.lower()
            else:
                if opcion == 3:
                    resultado = resultado.capitalize()

    return resultado


texto = input("Ingrese un texto: ")

numeros = input("Ingrese números entre 1 y 3 separados por espacio: ")
lista = numeros.split()

opciones = []

for n in lista:
    opciones.append(int(n))

resultado = transformar_varias(texto, opciones)

print("Resultado:", resultado)
