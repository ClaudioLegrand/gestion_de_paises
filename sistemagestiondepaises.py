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
    
# ----------------------------------------------------------------  EXCEPT POR SI SE UTILIZA EL ARCHIVO
# ----------------------------------------------------------------  EXCEPT POR SI CAMBIA EL NOMBRE
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
    # ----------------------------------------------------------------------- LISTA PARA VERIFICAR SI EXISTE EL PAIS

    # verificamos de que no ingrese un país que ya existe en el sistema
    
    # pedimos el nombre del país
    nombre = pedir_texto("Ingrese el nombre del país para agregar: ")

    # recorremos la lista por si ya existe el pais
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print("El país ya existe en el sistema, no puede continuar.")
            return

    # pedimos la poblacion del pais y validamos
    poblacion = pedir_entero("Ingrese la población del país: ") #------------------------- verificar si es solo entero

    # pedimos la superficie del pais
    superficie = pedir_entero("Ingrese la superficie del país: ")

    # pedimos el continente del pais
    continente = pedir_texto("Ingrese el continente del país: ").lower()
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
    return True


# ------------------------------------------------------------------ funcion solo para agregar?
# funcion para agregar datos al archivo csv
def añadir_datos_archivo(paises, archivo):
    try:
        with open(archivo, "a", encoding="utf-8") as f:
            for p in paises:
                linea = f"{p['nombre']},{p['poblacion']},{p['superficie']},{p['continente']}\n"
                f.write(linea)

        print("País agregado y guardado correctamente!")

    except FileNotFoundError:
        print("Error: El archivo no existe. No se pudieron guardar los datos.")
    except IOError:
        print("Error: No se pudieron guardar los datos en el archivo.") #---------------------- ver si se puede usar
    except Exception as e:
        print(f"Error inesperado: {e}")


# funcion para pedir un numero entero
def pedir_entero(mensaje):
    
    # usamos un whale para validar de que sea un numero entero y no un texto o un numero decimal
    while True:

        # pedimos un numero entero y validamos con try except
        entrada = input(mensaje).strip()
        
        try:
            # lo convertimos a entero
            numero = int(entrada)
            
            # si es un numero entero positivo, lo retornamos, sino mostramos un mensaje de error
            if numero >= 0:
                return numero
            else:
                print("Error: El numero no puede ser negativo")

        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

# funcion para pedir texto
def pedir_texto(mensaje):
    while True:
        entrada = input(mensaje).strip()
        
        # validamos que no esté vacío
        if entrada == "":
            print("Error: El campo no puede quedar vacío.")
            
        # validamos que no sean solo números (ej: "1234")
        elif entrada.isdigit() or entrada < "0":
            print("Error: Debe ingresar texto, no un número.")
            
        else:
            return entrada

# --------------------------------------------------
#                  MAIN DEL SISTEMA
# --------------------------------------------------

print("\nCargando datos...")
#carga de datos del archivo en variable
ruta_actual = os.path.dirname(__path__ if '__path__' in locals() else __file__)
archivopaises= os.path.join(ruta_actual, "datos/paises.csv")
paises=cargardatos(archivopaises)
print("Datos cargados correctamente!")

opcion = 0

while opcion != 8:

    # mostramos menu
    menu()

    # pedimos al usuario que ingrese una opción y validamos
    opcion = pedir_entero("\nOpción (1-8): ")

    try:
        match opcion:
            case 1:

                # pedimos los datos del país al usuario y los guardamos en un diccionario
                diccionarioCreado = guardar_datos(paises)

                # guardamos el diccionario en el archivo csv
                if diccionarioCreado:
                    añadir_datos_archivo(paises, archivopaises)

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
