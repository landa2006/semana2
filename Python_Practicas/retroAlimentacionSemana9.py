serie = "Solo Leveling"

## cada variable tiene un espacio de memoria asignado

## cuando una variable cambia=>se pierde la inmutabilidad
## POO
## polimorfismo -> es el cambio de acciones sin que se rompa el codigo
## abstracciones ->
##      Tasa de cafe
#       cafe coscafe
##       azucar
##      agua
##      otros ingredientes
##  un objeto es el que toma un modelo y este modelo le da funciones y utiliza sus propiedades

## Leon ->
## tiene ojos  (propiedades)
## tiene boca
## Esta guapo
#############
#  corre        ( Funciones )
# salta

## Clases
## Estructura de datos.


## es un arreglo es una variable que tiene adentro de otra variable
## Listas.
## Arrays.-> se inicia a contar desde el 0
## Tuplas.
## Indices.


# --------------------------------------------------------------------
def saludo(nombres):
    print(nombres)


# saludo(serie) las funciones siempre van a tner ()
# --------------------------------------------------------------------
saludo(serie)
## la funciones tienen un espacio
## Scope es donde reciden las variables

## Clocar el nombre de la serie como titulo
slTemu = serie.title()
saludo(serie)
## saludo(serie)
## saludo(slTemu)
slTemuMayusculas = serie.upper()
saludo(slTemuMayusculas)
## deprogracion Lineal
SoloLevelingCapitalizer = slTemuMayusculas.swapcase().title()
## cuando encadenamos funciones se indica que la salida de la funcion actual
## es la entrada de la siguiente funcion.

saludo(SoloLevelingCapitalizer)

## compara cadenas de texto
comparar1 = "Alas"
comparar2 = "Alas"
# casefold para comparar y pasar a minuscula
variableTemporada1 = comparar2.casefold()
comparar = comparar1.casefold() == comparar2.casefold()
print(comparar)
## casefold nos dara true unicamente si los elemtos son identicos sino nos indicara un false

## para erificar si es un numero o una variable vamos a utilizar isalfa()
clasicas2005 = "Gasolina"
compararisAlpha = clasicas2005.isalpha()
# print(compararisAlpha, 2005)
# isalpha nos va a dar true si string que se le esta enviando es unicamente letras
# si lo que quiero es que sea solo numero isalnum

letraCancion = "Lo que paso, paso, entre tu y yo."
decada = "10"

ejemplo = letraCancion.isalnum()
# print(ejemplo)

ejemplo = decada.isalnum()
# print(ejemplo)
