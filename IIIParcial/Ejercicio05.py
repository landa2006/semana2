nombre = input("Ingrese su nombre completo: ")

# Convertir a lista
lista_nombre = nombre.split()

# Invertir usando slicing
lista_invertida = lista_nombre[::-1]

# For anidado
for palabra in lista_invertida:

    letras = ""

    for letra in palabra:
        letras += letra + "."

    print(letras[:-1])
