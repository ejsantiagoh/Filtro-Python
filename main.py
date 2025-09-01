from interfaz.menu import menu
from modelo.modelo import cargar_datos, imprimir_factura, resumen_cliente_mes, diagrama_facturacion_anio, productos_comunes

# Programa principal
print("-" * 40)
print("-------------- BILLIFY ACME ------------")
print("-" * 40)

# Cargar datos al inicio
try:
    productos, clientes, ventas = cargar_datos()
except Exception as e:
    print(f"Error al cargar datos: {e}")
    input("Presione cualquier tecla para salir...")
    exit()

while True:
    op = menu()
    if op == 1:
        imprimir_factura(ventas, productos, clientes)
    elif op == 2:
        resumen_cliente_mes(ventas, productos, clientes)
    elif op == 3:
        diagrama_facturacion_anio(ventas)
    elif op == 4:
        productos_comunes(ventas, productos)
    elif op == 5:
        print("\nGracias por usar el software.\n")
        break