Algoritmo ejercicio1
	Definir nota Como Entero
	
	Escribir "Ingrese la nota del estudiante (0-10):"
	Leer nota
	
	Si nota < 0 O nota > 10 Entonces
		Escribir "Nota invalida"
	SiNo
		Si nota >= 6 Entonces
			Escribir "Aprobado"
		SiNo
			Si nota <= 4 Entonces
				Escribir "Reprobado"
			SiNo
				Escribir "Recuperacion"
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo