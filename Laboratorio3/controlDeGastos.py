gastos = []

while True:
    print("\n--- CONTROL DE GASTOS ---")
    print("1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            tipo = input("Tipo de gasto (comida/transporte/otros): ").lower()
            monto = float(input("Ingrese monto: "))

            match tipo:
                case "comida":
                    categoria = "Comida"
                case "transporte":
                    categoria = "Transporte"
                case _:
                    categoria = "Otros"

            gastos.append((categoria, monto))
            print("Gasto agregado.")

        case "2":
            total = 0

            if len(gastos) == 0:
                print("No hay gastos registrados.")
            else:
                print("\nLista de gastos:")
                for categoria, monto in gastos:
                    print(f"{categoria}: ${monto}")
                    total += monto

                print("Total gastado:", total)

                limite = 200

                if total > limite:
                    print("¡Has superado el límite de gastos!")
                else:
                    print("Estás dentro del límite.")

        case "3":
            print("Programa finalizado.")
            break

        case _:
            print("Opción inválida.")
