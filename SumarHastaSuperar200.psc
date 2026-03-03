Algoritmo SumarHastaSuperar200
	
    Definir numero Como Real
    Definir total Como Real
    Definir superar Como Logico
	
    total <- 0
    superar <- Falso
	
    Repetir
        
        Escribir "Ingrese un numero:"
        Leer numero
        
        total <- total + numero
        
        Si total > 200 Entonces
            superar <- Verdadero
        FinSi
        
    Hasta Que superar
	
    Escribir "La suma total es: ", total
    Escribir "Se supero 200."
	
FinAlgoritmo