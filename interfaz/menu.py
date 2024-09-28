def menu():

    while True:
        print("-" * 40)
        print("***************** MENÚ *****************")
        print("1. Insertar".center(20))
        print("2. Consultar".center(20))
        print("3. Informes".center(20))
        print("4. Salir".center(15))
        print("-" * 40)
        print(">>> opción: \n", end="")
        
        try:
            opcion = int(input())
            if opcion < 1 or opcion > 4:
                print("Error. Opción no válida.")
                input("Presione cualquier tecla para volver al menu...")
                continue
            return opcion
        except ValueError:
            print("Error. opción no válida.")
            input("Presione cualquier tecla para volver al menu...")