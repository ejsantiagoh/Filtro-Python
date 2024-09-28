from pathlib import Path
import data 

def guardar(prod, arch):
    with open(arch, "w") as fd:
        data.dump(prod, fd)

    if not fd.closed:
        fd.close()


# def cargar(arch):
#     archivo = Path(arch)
#     prod = {}
#     if archivo.is_file(): 
#         try:
#             with open(arch, "r") as fd:
#                 lib = data.load(fd)

#             if not fd.closed:
#                 fd.close()
#         except Exception as e:
#             print(">>> Error al abrir el archivo. \n" + e)
#     else:
#         print(">>> Error. El archivo no existe.")
#         input(">>> Presione cualquier tecla para continuar... ")

#     return prod
