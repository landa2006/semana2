palabra = "CANTANDO"

minusculas = palabra.lower()

sin_sufijo = minusculas.removesuffix("ando")

indice = sin_sufijo.find("t")

print("Palabra:", sin_sufijo)
print("Indice de t:", indice)
