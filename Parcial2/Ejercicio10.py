texto = "Python2026"

es_alfanumerico = texto.isalnum()

print("Es alfanumerico:", es_alfanumerico)

if es_alfanumerico:
    minusculas = texto.lower()
    separado = minusculas.replace("2026", "")
    print("Texto separado:", separado)
