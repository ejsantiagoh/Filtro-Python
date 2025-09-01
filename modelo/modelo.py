from collections import defaultdict

def cargar_datos():
    productos = load_csv('data/productos.dat', expected_header_len=3, header_check='CODPROD')
    clientes = load_csv('data/clientes.dat', expected_header_len=3, header_check='CODCLI')
    ventas = load_ventas('data/ventas.dat')  # Custom para ventas por más campos
    return parse_productos(productos), parse_clientes(clientes), parse_ventas(ventas)

def load_csv(file_path, expected_header_len, header_check):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    header = None
    data = []
    for line in lines:
        line = line.strip()
        if not line or ';' not in line:
            continue
        fields = line.split(';')
        if header is None and len(fields) == expected_header_len and header_check in fields[0].upper():
            header = fields
            continue
        if header and len(fields) == len(header):
            data.append(dict(zip(header, fields)))
    return data

def load_ventas(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    header = None
    data = []
    for line in lines:
        line = line.strip()
        if not line or ';' not in line:
            continue
        fields = line.split(';')
        if header is None and len(fields) == 9 and 'CODFACT' in fields[0].upper():
            header = fields
            continue
        if header and len(fields) == len(header):
            data.append(dict(zip(header, fields)))
    return data

def parse_productos(data):
    productos = {}
    for row in data:
        try:
            cod = row['CODPROD']
            productos[cod] = {
                'DESCPROD': row['DESCPROD'],
                'VALORUNIT': int(row['VALORUNIT'])
            }
        except:
            pass
    return productos

def parse_clientes(data):
    clientes = {}
    for row in data:
        try:
            cod = row['CODCLI']
            clientes[cod] = {
                'NOMBRE': row['NOMBRE'],
                'TELEFONO': row['TELEFONO']
            }
        except:
            pass
    return clientes

def parse_ventas(data):
    ventas = []
    for row in data:
        try:
            ventas.append({
                'CODFACT': row['CODFACT'],
                'AÑO': int(row['AÑO']),
                'MES': int(row['MES']),
                'DIA': int(row['DIA']),
                'CODCLI': row['CODCLI'],
                'CODPROD': row['CODPROD'],
                'UNIDADESPROD': int(row['UNIDADESPROD']),
                'VALOR': int(row['VALOR']),
                'VALORFACT': int(row['VALORFACT'])
            })
        except:
            pass
    return ventas

def leer_codigo(prompt, existentes):
    while True:
        try:
            cod = input(prompt).strip()
            if cod not in existentes:
                print(">>> Error. Código no existe.")
                continue
            return cod
        except Exception as e:
            print(f"Error al ingresar código: {e}")

def leer_mes_anio():
    while True:
        try:
            mes = int(input("Mes (1-12): "))
            if mes < 1 or mes > 12:
                print(">>> Error. Mes inválido.")
                continue
            anio = int(input("Año (e.g., 2024): "))
            return mes, anio
        except ValueError:
            print(">>> Error. Entrada inválida.")

def leer_anio():
    while True:
        try:
            anio = int(input("Año (e.g., 2024): "))
            return anio
        except ValueError:
            print(">>> Error. Entrada inválida.")

def imprimir_factura(ventas, productos, clientes):
    print("\n*** R1: Imprimir Factura ***")
    codfact = leer_codigo("Código de Factura: ", {v['CODFACT'] for v in ventas})
    
    lineas = [v for v in ventas if v['CODFACT'] == codfact]
    if not lineas:
        print("No se encontró la factura.")
        return
    
    codcli = lineas[0]['CODCLI']
    cliente = clientes.get(codcli, {'NOMBRE': 'Desconocido'})
    fecha = f"{lineas[0]['DIA']}/{lineas[0]['MES']}/{lineas[0]['AÑO']}"
    
    print(f"\nFactura: {codfact}")
    print(f"Cliente: {cliente['NOMBRE']} (COD: {codcli})")
    print(f"Fecha: {fecha}")
    print("-" * 50)
    print("CODPROD | DESCPROD | UNIDADES | VALOR UNIT | SUBTOTAL")
    print("-" * 50)
    
    subtotal = 0
    for linea in lineas:
        prod = productos.get(linea['CODPROD'], {'DESCPROD': 'Desconocido', 'VALORUNIT': 0})
        subtotal_linea = linea['VALOR']
        subtotal += subtotal_linea
        print(f"{linea['CODPROD']} | {prod['DESCPROD']} | {linea['UNIDADESPROD']} | {prod['VALORUNIT']:,} | {subtotal_linea:,}")
    
    iva = subtotal * 0.19
    total = subtotal + iva
    print("-" * 50)
    print(f"Subtotal: {subtotal:,}")
    print(f"IVA (19%): {iva:.0f}")
    print(f"Total: {total:.0f}")
    input("Presione cualquier tecla para volver al menú...")

def resumen_cliente_mes(ventas, productos, clientes):
    print("\n*** R2: Resumen Facturas Cliente/Mes ***")
    codcli = leer_codigo("Código de Cliente: ", clientes)
    mes, anio = leer_mes_anio()
    
    cliente = clientes[codcli]
    facturas = defaultdict(list)
    for v in ventas:
        if v['CODCLI'] == codcli and v['MES'] == mes and v['AÑO'] == anio:
            facturas[v['CODFACT']].append(v)
    
    if not facturas:
        print("No hay facturas para este cliente en el mes.")
        return
    
    meses_nombres = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
                     7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
    
    print(f"\nCliente: {cliente['NOMBRE']} (COD: {codcli})")
    print(f"Mes: {meses_nombres[mes]} ({anio})")
    print("-" * 50)
    
    total_subtotal = 0
    for codfact, lineas in facturas.items():
        subtotal = sum(l['VALOR'] for l in lineas)
        iva = subtotal * 0.19
        total = subtotal + iva
        total_subtotal += subtotal
        print(f"Factura {codfact}: Subtotal {subtotal:,}, IVA {iva:.0f}, Total {total:.0f}")
    
    total_iva = total_subtotal * 0.19
    total_con_iva = total_subtotal + total_iva
    print("-" * 50)
    print(f"Total Sin IVA: {total_subtotal:,}")
    print(f"Total IVA: {total_iva:.0f}")
    print(f"Total Con IVA: {total_con_iva:.0f}")
    input("Presione cualquier tecla para volver al menú...")

def diagrama_facturacion_anio(ventas):
    print("\n*** R3: Diagrama Facturación Año ***")
    anio = leer_anio()
    
    meses_valores = defaultdict(int)
    for v in ventas:
        if v['AÑO'] == anio:
            meses_valores[v['MES']] += v['VALOR']  # Sumamos VALOR (sin IVA)
    
    if not meses_valores:
        print("No hay datos para este año.")
        return
    
    max_valor = max(meses_valores.values())
    escala = max_valor / 20 if max_valor > 0 else 1  # Escala para barras de max 20 *
    
    print(f"\n====================\nFACTURACIÓN DEL {anio}\n====================")
    print("MESES\n-------------")
    for mes in range(1, 13):
        valor = meses_valores.get(mes, 0)
        barras = '*' * int(valor / escala)
        print(f"{mes:02} {barras}")
    
    input("Presione cualquier tecla para volver al menú...")

def productos_comunes(ventas, productos):
    print("\n*** R4: Productos Comunes Entre Dos Clientes ***")
    codcli1 = leer_codigo("Código Cliente 1: ", {v['CODCLI'] for v in ventas})
    codcli2 = leer_codigo("Código Cliente 2: ", {v['CODCLI'] for v in ventas})
    
    prods1 = {v['CODPROD'] for v in ventas if v['CODCLI'] == codcli1}
    prods2 = {v['CODPROD'] for v in ventas if v['CODCLI'] == codcli2}
    comunes = prods1.intersection(prods2)
    
    if not comunes:
        print("No hay productos comunes.")
        return
    
    print("\nProductos Comunes:")
    for cod in sorted(comunes):
        prod = productos.get(cod, {'DESCPROD': 'Desconocido'})
        print(f"- {cod}: {prod['DESCPROD']}")
    
    input("Presione cualquier tecla para volver al menú...")