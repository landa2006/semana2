# las comillas triples son las que se encargan de hacer
# Cadenas de texto largas sin modificar el formato.
# 2 comillas: para texto corto ""
# 3 comillas: para texto largo """"
music = "Yeah, I, I know it's hard to remember"
"the people we used to be"
"It's even harder to picture that you're not here next to me"

music1 = """Yeah, I, I know it's hard to remember the people we used to be
It's even harder to picture that you're not here next to me
You say it's too late to make it, but is it too late to try?
And in our time that you wasted, all of our bridges burned down
I've wasted my nights, you turned out the lights
Now I'm paralyzed
Still stuck in that time when we called it love
But even the sun sets in paradise
I'm at a payphone, trying to call home
All of my change, I spent on you
Where have the times gone? Baby, it's all wrong
Where are the plans we made for two?"""

# print(muic)

##computadora -> que variable queres imprimir
## como sabe, por el metodo "print"
# print() -> es la función que se encarga de imprimir pantalla
# void -> no devuelve nada
# objeto -> devuelve un tipo de dato

# realizar una wiki, tambien se puede ver dando doble clic
# en el documeto y se les despelga el editor de texto

## MAYUSCULAS
## mutabilidad -> siempre debemos evitar transformar objeto original
## clases -> estereotipo ( defini: como un  molde)
## estan formadas por propiedades ->

## music1 es un espacio de memoria para string
## se va a llenar con el contenido de music1
music1_Mayusculas = music1.upper()
print(music1_Mayusculas)

## convertir en minusculas
## string .lower

music1_minuscula = music1.lower()
print(music1_minuscula)


mensaje = "hOlA kOMo tE VA"
## Capitalize a que la primera letra de cada palabra sea mayuscula
mensajeCorrecto = mensaje.capitalize()
print(mensajeCorrecto)

## Las flipantes aventuras de tito y loli
titulo = "Las flipantes aventuras de tito y loli"
tituloCorrecto = titulo.title()
print(tituloCorrecto)

#### swapCase() permite cambiar entre mayusuculas y minusculas
swapCaseTitulo = tituloCorrecto.swapcase()
print(swapCaseTitulo)

nombre = "Landaverde"
nombre2 = "Alas"
comparar = nombre.casefold() == nombre2.casefold()
print(comparar)

## metodos de validacion
## false numeros o espacios
## true tiene solo letras

numero = "512"
solo_letras = "El chico del apartamento"
Coro = "biribiribanban"

quieroSoloLetras = Coro.isalphaBB()
print(quieroSoloLetras)
