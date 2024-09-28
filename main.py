from interfaz.menu import menu
from modelo.modelo import insertar, consultar
# from persistencia.persistencia import cargar


# Programa principal
print("-" * 40)
print("-------------- BILLIFY ACME ------------")



# billify = {}
# archivo = "data\productos.dat"
# billify = cargar(archivo)

while True:
    op = menu()
    match op:
        case 1:
            billify = insertar(billify, )
        case 2:
            consultar(billify)
        case 3:
            pass
            #informes()
        case 4:
            print("\nEstamos en mejoras constantes. ")
            print("")
            print("\nGracias por usar el software. \n")
            break
