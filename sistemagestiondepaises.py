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

    return paises

# funcion para guardar los datos del país en la lista de diccionarios
def guardar_datos(paises):

    # ---------------------------------------------------------------- preguntar cuantos paises quieren agregar?

    nombre_repetido = True
    intentos = 3 #----------------------------------------------------- vemos si ponemos intentos

    # verificamos de que no ingrese un país que ya existe en el sistema
    while nombre_repetido and intentos > 0:

        # pedimos el nombre del país
        nombre = input("Ingrese el nombre del país para agregar: ").strip().lower()

        nombre_repetido = False
        for p in paises:
            if p["nombre"] == nombre:
                print("El país ya existe en el sistema. ingrese un país diferente.")
                nombre_repetido = True
                break

    # si se queda sin intentos, volvemos al menú principal
    if intentos == 0:
        print("Se han agotado los intentos. Volviendo al menú principal.")
        return

    poblacion = input("Ingrese la población del país: ").strip()
    superficie = input("Ingrese la superficie del país: ").strip()
    continente = input("Ingrese el continente del país: ").strip().lower()
    # ---------------------------------------------------------------------- falta mejorar validaciones

    # creamos un diccionario para el país y lo agregamos a la lista de países
    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    # lo apregamos a la lista de países
    paises.append(pais)


# ------------------------------------------------------------------ funcion solo para agregar?
# funcion para agregar datos al archivo csv
def añadir_datos_archivo(paises, archivo):
    try:
        with open(archivo, "a", encoding="utf-8") as f:
            for p in paises:
                linea = f"{p['nombre']},{p['poblacion']},{p['superficie']},{p['continente']}\n"
                f.write(linea)

    except FileNotFoundError:
        print("Error: El archivo no existe. No se pudieron guardar los datos.")
    except IOError:
        print("Error: No se pudieron guardar los datos en el archivo.") #---------------------- ver si se puede usar
    except Exception as e:
        print(f"Error inesperado: {e}")


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

                # pedimos los datos del país al usuario y los guardamos en un diccionario
                guardar_datos(paises)

                # guardamos el diccionario en el archivo csv
                añadir_datos_archivo(paises, archivopaises)
                print("País agregado y guardado correctamente!")

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
    