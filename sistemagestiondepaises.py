import os
from unittest import case
# --------------------------------------------------
#                   MENU PRINCIPAL
# --------------------------------------------------
def menu():
    print('''\n
        ------------------------------------------
                    GESTION DE PAISES                       
        ------------------------------------------
        
        1 - Agregar país
        2 - Actualizar datos del país
        3 - Buscar país
        4 - Filtrar país
        5 - Ordenar paises
        6 - Mostrar estadisticas
        7 - Ver todos los paises
        8 - Salir
        
        ------------------------------------------
        ''')  
    
def cargardatos(archivo):
#cargar datos desde el archivo csv  
#retorna una lista de diccionarios
    paises=[]
    dirpaises={}
    if not os.path.exists(archivo):
        print("MOSTRAR ERROR Y CREARLO")
        with open(archivo, "w", encoding="utf-8") as f:
            return paises
    else:
        with open(archivo,"r",encoding="utf-8") as archivopaises:
            encabezado=next(archivopaises).strip().split(",")
            for fila in archivopaises:
                partes=fila.strip().split(",")
                dirpaises = dict(zip(encabezado, partes))
                paises.append(dirpaises)

# funcion para guardar datos en el archivo csv
# def guardar_datos(paises, archivo):
#     with open(archivo, "w", encoding="utf-8") as f:
#         if paises:
#             f.write(",".join(paises[0].keys()) + "\n")
#             for pais in paises:
#                 f.write(",".join(pais.values()) + "\n")
#     area = input("Ingrese el área del país (en km²): ")
#     idioma = input("Ingrese el idioma oficial del país: ")



# funcion que valida numero enteros
def validar_entero(numero):
    try:
        
        while numero.strip() == "" or not numero.isdigit():
            print("Error: vuelva a intentar.")
            numero = input("vuelva a intentar: ")

        return int(numero)
    
    except ValueError:
        print("Error: Por favor, ingrese un número entero.") #----------------------- Verificar mejor las except

# --------------------------------------------------
#                  MAIN DEL SISTEMA
# --------------------------------------------------

print("\nCargando datos...")
#carga de datos del archivo en variable
ruta_actual = os.path.dirname(__path__ if '__path__' in locals() else __file__)
archivopaises= os.path.join(ruta_actual, "datos/paises.csv")
paises=cargardatos(archivopaises)
print("Datos cargados correctamente!")

print("\nBienvenido al sistema de gestión de países")

opcion = 0

while opcion != 8:

    # mostramos menu
    menu()

    # pedimos al usuario que ingrese una opción y validamos
    opcion = validar_entero(input("\nOpción (1-8): "))

    try:
        match opcion:
            case 1:
                print("AGREGAR PAIS")
                #agregar_pais(paises)
            case 2:
                print("ACTUALIZAR DATOS DEL PAIS")
                #actualizar_pais(paises)    
            case 3:
                print("BUSCAR PAIS")
                #buscar_pais(paises)
            case 4:
                print("FILTRAR PAIS")
                #filtrar_pais(paises)
            case 5:
                print("ORDENAR PAISES")
                #ordenar_paises(paises)
            case 6:
                print("VER ESTADISTICAS")
                #ver_estadisticas(paises)
            case 7:
                print("VER TODOS LOS PAISES")
                #ver_todos_los_paises(paises)
            case 8:
                #guardardatos(paises) #GUARDAR ANTES DE SALIR

                print("Saliendo del sistema...")
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 8. \n")
    except ValueError:
            print("Error: Valor ingresado es incorrecto") #ponerlo????????????
    