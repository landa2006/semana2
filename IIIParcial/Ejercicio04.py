for numero in range(1, 51):

    # Detener en 42
    if numero == 42:
        print("Brecha de seguridad detectada")
        break

    # Saltar múltiplos de 3
    if numero % 3 == 0:
        continue

    print(f"Procesando registro ID: {numero}")
