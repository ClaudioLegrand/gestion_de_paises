import os
import unicodedata
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
    nombre = pedir_texto("Ingrese el nombre del país para agregar: ").capitalize() #se agrega .capitalize() para que agregue en formato capital

    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print("El país ya existe en el sistema, no puede continuar.")
            return

    poblacion = pedir_entero("Ingrese la población del país: ") 
    superficie = pedir_entero("Ingrese la superficie del país: ")
    #verificar contiente -----------
    menucontinentes()
    seleccion_contiente=pedir_entero(("Seleccione continente: "))
    match seleccion_contiente:
        case 1:
            continente="America"
        case 2:
            continente="Europa"
        case 3:
            continente="Ocenia"
        case 4:
            continente="Africa"
        case 5:
            continente="Asia"
        case _:
            print("Error: Continente no seleccionado correctame")


    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)
    return pais

# funcion para agregar datos al archivo csv
def añadir_datos_archivo(pais, archivo):
    try:
        with open(archivo, "a", encoding="utf-8") as f:
            linea = f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n"
            f.write(linea)
        print("País agregado y guardado correctamente!")
    except FileNotFoundError:
        print("Error: El archivo no existe. No se pudieron guardar los datos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# --------------------------------------------------
#              ACTUALIZAR DATOS DE PAIS
# --------------------------------------------------
def actualizardatospais(paises):
    print("""
        ------------------------------------------
                    ACTUALIZAR PAIS                      
        ------------------------------------------
        """)
    while True:
        nombrepais = pedir_texto("Ingrese nombre de pais a actualizar [Use 'salir' para volver al menu principal]:  ").lower()
        if nombrepais == "salir":
            break
        for pais in paises:
            if normalizar(pais["nombre"]) == normalizar(nombrepais):
                try:
                    print(f"Datos actuales de -- {pais['nombre']} --\n")
                    print(f"Población: {pais['poblacion']} | Superficie: {pais['superficie']}")
                    nuevapoblacion = input("Ingrese la nueva población [Enter para mantener la actual]\n").strip()
                    nuevasuperficie = input("Ingrese la nueva superficie [Enter para mantener la actual]\n").strip()
                    if nuevapoblacion:
                        pais["poblacion"] = validar_numero_correcto(nuevapoblacion)
                    if nuevasuperficie:
                        pais["superficie"] = validar_numero_correcto(nuevasuperficie)
                    if not nuevapoblacion and not nuevasuperficie:
                        print("No se actualizó ningún registro")
                        break
                    else:
                        print(f"Los datos de {pais['nombre']} fueron actualizados correctamente")
                        break
                except ValueError:
                    print("Error: Valor ingresado es incorrecto [Ingrese valor entero positivo o ENTER si no requiere actualización]")
                    return
        else:
            print(f"Error: Pais '{nombrepais}' no encontrado [puede cargar un país en la opción 1]")
        return
#VALIDA NUMERO CORRECTO Y NO TIENE EN CUENTA SI EL USUARIO DEJA EL ESPACIO VACIO (NO ACTUALIZA EL REGISTRO)
def validar_numero_correcto(vnc_nuevavalidacion):
    numero_a_verificar = int(vnc_nuevavalidacion)
    try:
        if numero_a_verificar <= 0:
            raise ValueError
        return numero_a_verificar
    except ValueError:
        raise ValueError("Error: El valor ingresado debe ser un valor entero positivo")

# funcion para pedir un numero entero
def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje).strip()
        try:
            numero = int(entrada)
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
        if entrada == "":
            print("Error: El campo no puede quedar vacío.")
        elif entrada.isdigit() or entrada < "0":
            print("Error: Debe ingresar texto, no un número.")
        else:
            return entrada
        
# --------------------------------------------------
#              MOSTRAR ESTADISTICAS
# --------------------------------------------------
def mostrarestadisticas(paises):
    """Mostrar estadisticas:
     País con mayor y menor población
    - Promedio de población
    - Promedio de superficie
    - Cantidad de países por continente"""
    print(f"""
        ------------------------------------------
                MOSTRAR ESTADISTICAS                            
        ------------------------------------------
        """)
    
    print(f"\nTotal de paises: {len(paises)}\n")
    # Mayor y menor población
    mayor_poblacion = max(paises, key=lambda p: int(p["poblacion"]))
    menor_poblacion = min(paises, key=lambda p: int(p["poblacion"]))
    #MOSTRAR POBLACION
    print("-"*35)
    print("Población")
    print("-"*35)
    print(f"Mayor: {mayor_poblacion['nombre']} ({int(mayor_poblacion['poblacion']):,} hab.)")
    print(f"Menor: {menor_poblacion['nombre']} ({int(menor_poblacion['poblacion']):,} hab.)")
    #CALCULO PROMEDIO POBLACION
    total=0
    for pais in paises:
        total+=int(pais["poblacion"])
        promediopoblacion = total / len(paises)
    print(f"Promedio de población: {promediopoblacion:,.2f} hab.")
    #CALCULO PROMEDIO SUPERFICIE
    total=0
    for pais in paises:
        total+=int(pais["superficie"])
        promediosuperficie = total / len(paises)
    print("-"*35)
    print("Superficie")
    print("-"*35)    
    print(f"Promedio de superficie: {promediosuperficie:,.2f}")
    #CANTIDAD DE PAISES POR CONTINENTE
    america=0
    africa=0
    europa=0
    asia=0
    oceania=0
    for pais in paises:
        continente = normalizar(pais["continente"]).lower()
        if continente == "america":
            america+=1
        elif continente == "africa":
             africa+=1
        elif continente == "europa":
             europa+=1
        elif continente == "asia":
             asia+=1
        else: oceania+=1
    print("-"*35)
    print("Paises por continentes")
    print("-"*35)   
    print(f"{'America:':<8}: {america}")
    print(f"{'Africa:':<8}: {africa}")
    print(f"{'Europa:':<8}: {europa}")
    print(f"{'Asia:':<8}: {asia}")
    print(f"{'Oceania:':<8}: {oceania}")

# --------------------------------------------------
#              MODELO DE MOSTRAR DATOS
# --------------------------------------------------
def outputmostrardatos(paises):
    #Muestra una lista de países en formato tabla
    
    if not paises:
        print("[INFO]: Lista vacía.")
        return

    # Encabezado
    print(f"\n{'Nombre':<20} {'Población':>15} {'Superficie':>15}  {'Continente':<12}") #se usan <xx, para limitar los espacios DE CARACTERES QUE OCUPAN
    print("-" * 65)

    #datos a mostrar
    for p in paises:
        print(f"{p['nombre']:<20} {int(p['poblacion']):>15,} {int(p['superficie']):>15,}  {p['continente']:<12}")

# --------------------------------------------------
#              NORMALIZADOR DE TILDES
# --------------------------------------------------

def normalizar(texto): # ESTA FUNCION LO QUE HACE ES NORMALIZAR EL USO DE LAS TILDES, MEDIANTE LA LIBRERIA UNICODEDATA, QUITA LOS ACENTOS Y LOS IGNORA, DEJANDO SOLO ASCII
    return unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode("utf-8").lower()

# --------------------------------------------------
#               FILTRADO DE PAISES 
# --------------------------------------------------

def menu_filtrar(paises): #FILTRADO DE PAISES (4)
    while True:
        print("""
        ------------------------------------------
                    FILTRAR PAISES                      
        ------------------------------------------
        
        1 - Por continente
        2 - Por rango de población
        3 - Por rango de superficie
        4 - Volver al menú principal
        
        """)
        opcion = pedir_entero("Seleccione una opción: ")

        if opcion == 1:
            filtrar_por_continente(paises)
        elif opcion == 2:
            filtrar_por_rango_poblacion(paises)
        elif opcion == 3:
            filtrar_por_rango_superficie(paises)
        elif opcion == 4:
            break
        else:
            print("Error: Opción inválida.")
#
# FILTRADO DE RANGO SUPERFICIE --------
#
def filtrar_por_rango_superficie(paises):
    print("""
          
        ------------------------------------------
                  FILTRAR POR SUPERFICIE                      
        ------------------------------------------
        
        """)
    try:
        minimo = input("Superficie mínima (Enter para sin límite): ")
        maximo = input("Superficie máxima (Enter para sin límite): ")

        min_val = int(minimo)if minimo else 0
        max_val = int(maximo) if maximo else float("inf")

        if min_val < 0 or max_val < 0:
            raise ValueError("Los valores no pueden ser negativos.")

        resultados = []
        for p in paises:
            if min_val <= int(p["superficie"]) <= max_val:
                resultados.append(p)

        if not resultados:
            print("No hay países en ese rango de superficie.")
            return

        print(f"\nPaises con superficie desde {min_val}km hasta {max_val}km = {len(resultados)} paises encontrados")
        outputmostrardatos(resultados)

    except ValueError:
        print(f"Error: Debe ingresar numeros enteros positivos")

def filtrar_por_rango_poblacion(paises):
    print("""
          
        ------------------------------------------
                  FILTRAR POR POBLACION                      
        ------------------------------------------
        
        """)
    try:
        minimo = input("Población mínima (Enter para sin límite): ")
        maximo = input("Población máxima (Enter para sin límite): ")

        min_val = int(minimo)if minimo else 0
        max_val = int(maximo) if maximo else float("inf")

        if min_val < 0 or max_val < 0:
            raise ValueError("Los valores no pueden ser negativos.")

        resultados = []
        for p in paises:
            if min_val <= int(p["poblacion"]) <= max_val:
                resultados.append(p)
            if not resultados:
                print("No hay países en ese rango de población.")
                return
        outputmostrardatos(resultados)
    except ValueError:
        print(f"Error: Debe ingresar numeros enteros positivos")
        
        
#
# FILTRADO POR CONTINENTES --------
#
def filtrar_por_continente(paises):
    print("""
          
        ------------------------------------------
                  FILTRAR POR CONTINENTES                      
        ------------------------------------------
        
        """)
    menucontinentes() #muesta menu de continentes para seleccionar
    seleccioncontinente=pedir_entero("Seleccione un continente [1-5]: ")
    match seleccioncontinente:
        case 1: filtrar_y_mostrar_continentes(paises, "America")
        case 2: filtrar_y_mostrar_continentes(paises, "Europa")  
        case 3: filtrar_y_mostrar_continentes(paises, "Oceania")
        case 4: filtrar_y_mostrar_continentes(paises, "Africa")
        case 5: filtrar_y_mostrar_continentes(paises, "Asia") 
        case _: print("Selección invalida [reintente con números del 1 al 5]")   
#
# PROCESO DE FILTRADO Y MUESTRA DE CONTINENTES --------
#
def filtrar_y_mostrar_continentes(paises, continente):
    resultados=[]
    for p in paises:
        if normalizar(p["continente"]) == normalizar(continente):
            resultados.append(p)
    if not resultados:
        print(f"No hay paises en agregados en {continente}")
        return
    outputmostrardatos(resultados)
#
# MENU DE CONTINENTES --------
#   
def menucontinentes():
    print("""Seleccione contiente
          1 - America
          2 - Europa
          3 - Ocenia
          4 - Africa
          5 - Asia
          """)
                    
                

# --------------------------------------------------
#                  MAIN DEL SISTEMA
# --------------------------------------------------
print("\nCargando datos...")
ruta_actual = os.path.dirname(__path__ if '__path__' in locals() else __file__)
archivopaises = os.path.join(ruta_actual, "datos/paises.csv")
paises = cargardatos(archivopaises)
print("Datos cargados correctamente!")

opcion = 0

while opcion != 8:
    menu()
    opcion = pedir_entero("\nOpción (1-8): ")

    try:
        match opcion:
            case 1:
                diccionarioCreado = guardar_datos(paises)
                if diccionarioCreado:
                    añadir_datos_archivo(diccionarioCreado, archivopaises)
            case 2:
                actualizardatospais(paises)
            case 3:
                print("BUSCAR PAIS")
            case 4:
                menu_filtrar(paises)
            case 5:
                print("ORDENAR PAISES")
            case 6:
                mostrarestadisticas(paises)
            case 7:
                outputmostrardatos(paises)    
            case 8:
                print("Saliendo del sistema...")
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 8. \n")
    except ValueError:
        print("Error: Valor ingresado es incorrecto")
