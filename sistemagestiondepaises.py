import os

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

def menu_buscar_paises():
    print('''\n
        ------------------------------------------
                    ORDENAR PAISES                       
        ------------------------------------------
        
        1 - Por Nombre
        2 - Por Poblacion
        3 - Por Superficie
        4 - Salir al menu
        
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
    except Exception as e:
        print(f"Error inesperado: {e}")

# funcion para buscar un pais
def buscar_pais_por_nombre(paises):

    # pedimos el pais para buscarlo en la lista
    pais_usuario = pedir_texto("Ingrese el pais a buscar: ").lower()

    # lista que guarda las coincidencias encontradas
    coincidencias = []

    try:
        # recorremos la lista y buscamos el pais
        for p in paises:
            if pais_usuario in str(p["nombre"]).lower():
                coincidencias.append(p)

        outputmostrardatos(coincidencias)

    except KeyError as e:
        print(f"Error al buscar el país: {e}")
    except Exception as e:
        print(f"Error inesperado al buscar el país: {e}")

# funcion para ordenar paises
def ordenar_paises(paises, criterio, orden):

    # copiamos la lista para no modificar la original
    lista_copia = paises.copy()
    cantidad_paises = len(paises)

    try:

        # para odenar usamos el metodo burbuja
        for indice_pasada in range(cantidad_paises - 1):

            for indice_actual in range(cantidad_paises - 1 - indice_pasada):
                
                # si el criterio es ordenarlo por nombres
                lista_copia = mover_elementos(lista_copia, orden, criterio, indice_actual)

        # mostramos la lista ordenada
        outputmostrardatos(lista_copia)

    # except para captura errores cuando trabajamos con estructura de datos y con conversiones de tipos
    except KeyError:
        print(f"Error: Falta la clave en los datos de los países.")
    except ValueError:
        print(f"Error: No se pudo procesar numéricamente el criterio '{criterio}'.")
    except Exception as e:
        print(f"Error inesperado al ordenar los países: {e}")

# funcion para mover elementos en la lista
def mover_elementos(lista_copia, orden, criterio, indice_actual):
    

    if criterio == "nombre":
        ele_actual = lista_copia[indice_actual][criterio].lower()
        ele_siguiente = lista_copia[indice_actual + 1][criterio].lower()
    else: 
        ele_actual = int(lista_copia[indice_actual][criterio])
        ele_siguiente = int(lista_copia[indice_actual + 1][criterio])

    debe_mover = False

    match orden:

        # Ascendente
        case 1:  
            if ele_actual > ele_siguiente:
                debe_mover = True
        # Descendente
        case 2:  
            if ele_actual < ele_siguiente:
                debe_mover = True

    if debe_mover:
        # movemos el elemento actual a la posición del siguiente
        lista_copia[indice_actual], lista_copia[indice_actual + 1] = (
            lista_copia[indice_actual + 1], 
            lista_copia[indice_actual]
        )

    return lista_copia

def outputmostrardatos(paises):
    """Muestra una lista de países en formato tabla."""
    print("""
        ------------------------------------------
                MOSTRAR DATOS EN TABLA
        ------------------------------------------
        """)
    if not paises:
        print("[INFO]: Lista vacía.")
        return

    # Encabezado
    print(f"{'Nombre':<20} {'Población':>15} {'Superficie':>15}  {'Continente':<12}") #se usan <xx, para limitar los espacios DE CARACTERES QUE OCUPAN
    print("-" * 65)

    for p in paises:
        print(f"{p['nombre']:<20} {int(p['poblacion']):>15,} {int(p['superficie']):>15,}  {p['continente']:<12}")

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
                
                # pedimos el pais que quiere buscar y lo mostramos
                buscar_pais_por_nombre(paises)
                
            case 4:
                print("FILTRAR PAIS")
                #filtrar_pais(paises)
            case 5:
                opcion_orden = 0

                while opcion_orden != 4:

                    # mostramos el menu para ordenar los paises
                    menu_buscar_paises()

                    # pedimos al usuario que ingrese una opción y validamos
                    opcion_orden = pedir_entero("\nOpción (1-4): ")

                    if opcion_orden != 4:

                        # pedimos que forma de ordenamiento quiere, ascendente o descendente
                        if opcion_orden in [1, 2, 3]:
                            print(f"¿Ordenar de forma ascendente o descendente?")

                            while True:
                                opcion_forma = pedir_entero("1 - Asc | 2 - Des: ")

                                if opcion_forma in [1, 2]:
                                    break

                                print("Opción no válida. Por favor, seleccione 1 para ascendente o 2")

                        # ordenamos los paises por el criterio seleccionado
                        match opcion_orden:
                            case 1: ordenar_paises(paises, "nombre", opcion_forma)
                            case 2: ordenar_paises(paises, "poblacion", opcion_forma)
                            case 3: ordenar_paises(paises, "superficie", opcion_forma)
                            case _: print("No se encuentra entre las opciones")

                print("Saliendo al menú principal...")


            case 6:
                print("VER ESTADISTICAS")
                #ver_estadisticas(paises)
            case 7:
                print("VER TODOS LOS PAISES")
                outputmostrardatos(paises)
            case 8:
                #guardardatos(paises) #GUARDAR ANTES DE SALIR

                print("Saliendo del sistema...")
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 8. \n")
    except ValueError:
            print("Error: Valor ingresado es incorrecto") #ponerlo????????????
