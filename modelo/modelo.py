from persistencia.persistencia import guardar


"""
    productos = {
        codprod1(str):{
            descprod:(str)
            valorunit:int
        },
        codprod2(str):{
            descprod:(str)
            valorunit:int
        }
    }
    """

def leerCodigoProducto():
    while True:
        try:
            cod = input("Código del producto: \n")
            if len(cod.strip()) == 0:
                print(">>> Error. Código inválido.")
                continue
            return cod
        except Exception as e:
            print("Error al ingresar el código.\n" + e)

def leerDescProducto():
    while True:
        try:
            tit = input("Descripción del producto: \n")
            if len(tit.strip()) == 0:
                print(">>> Error. Descripción inválida.")
                continue
            return tit
        except Exception as e:
            print("Error al ingresar la descripción.\n" + e)

def leerValorUnitario():
    while True:
        try:
            precio = int(input("Valor Unitario: \n"))
            if precio < 100:
                print(">>> Error. Valor incorrecto.")
                continue
            return precio
        except ValueError:
            print(">>> Error. Valor Unitario invalido.\n")

def insertar(prod, arch):
    print("\n\n**1. INSERTAR PRODUCTOS***")

    cod = leerCodigoProducto()
    if cod not in prod:
        descProducto = leerDescProducto()
        valorUnitario = leerValorUnitario()

        datprod = {
            "DESCPROD" : descProducto,
            "VALORUNIT" : valorUnitario
        }

        prod[cod] = datprod

        prod = dict(sorted(prod.items()))
        guardar(prod, arch)

    else:
        print("El codigo ya existe en productos.")

    input("Presione cualquier tecla para volver al menu...")
    return prod

def consultar(prod):
    print("\n\n**2. CONSULTAR PRODUCTOS ***")


    cod = input("\nCódigo del Producto: \n")

    if cod in prod:
        print("-> CODPROD: ", cod)
        print(f"-> DESCPROD: {prod[cod]} ")
        print(f"-> VALORUNIT: {prod[cod]:,.0f}")
    else:
        print(">>> Error. El código del producto no existe.")


    input("Presione cualquier tecla para volver al menu...")