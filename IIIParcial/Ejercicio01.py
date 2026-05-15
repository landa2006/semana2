etiqueta = input("Ingrese la etiqueta de rastreo: ")

if etiqueta == "" or etiqueta is None:
    print("Error: Entrada inválida")
    exit()

# Slicing
inicio = etiqueta.find("-") + 1
fin = etiqueta.rfind("-")

categoria = etiqueta[inicio:fin]

print("Categoría:", categoria)

mensaje = "Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacional"

print(mensaje)
