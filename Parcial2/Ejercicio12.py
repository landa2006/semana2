archivo = "ING. Leydi Alas.txt"

sin_sufijo = archivo.removesuffix(".txt")

sin_prefijo = sin_sufijo.removeprefix("ING. ")

resultado = sin_prefijo.split()

print(resultado)
