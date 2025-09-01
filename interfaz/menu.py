def menu():
    while True:
        print("-" * 40)
        print("***************** MENÚ *****************")
        print("1. Imprimir Factura (R1)".center(40))
        print("2. Resumen Cliente/Mes (R2)".center(40))
        print("3. Diagrama Facturación Año (R3)".center(40))
        print("4. Productos Comunes (R4)".center(40))
        print("5. Salir".center(40))
        print("-" * 40)
        print(">>> Opción: ", end="")
        
        try:
            opcion = int(input())
            if opcion < 1 or opcion > 5:
                print("Error. Opción no válida.")
                input("Presione cualquier tecla para volver al menú...")
                continue
            return opcion
        except ValueError:
            print("Error. Opción no válida.")
            input("Presione cualquier tecla para volver al menú...")    