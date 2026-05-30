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
    
# --------------------------------------------------
#                   CARGA DE ARCHIVO
# --------------------------------------------------    
    
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
        print(paises)
        return paises #ESTO LO AGREGUE POR QUE NO DEVOLVIA LA LISTA DE DICCIONARIOS FUERA DE LA FUNCION
        
# --------------------------------------------------
#              ACTUALIZAR DATOS DE PAIS
# --------------------------------------------------
def actualizardatospais(paises):
    print("""
        ------------------------------------------
                    ACTUALIZAR PAIS                      
        ------------------------------------------
        """)
    nombrepais=input("Ingrese nombre de pais a actualizar: ").strip().lower()
    #verificar si pais existe
    for pais in paises:
        if pais["nombre"].lower() == nombrepais:
            #QUE SE MUESTRE ACTUALIZAR POBLACION: [SI NO QUIERE ACTUALIZAR PRESIONE "ENTER"]
            #QUE PASA SI TIENE ACENTOS? COMO HAGO PARA QUE NO LOS TENGA EN CUENTA?
            try:
                print(f"Datos actuales de -- {pais["nombre"]} --\n")
                print(f"Población: {pais["poblacion"]} | Superficie: {pais["superficie"]}")
                nuevapoblacion=input("Ingrese la nueva población [Enter para mantener la actual]\n").strip()
                nuevasuperficie=input("Ingrese la nueva superficie [Enter para mantener la actual]\n").strip()
                if nuevapoblacion:
                    pais["poblacion"]=validar_numero_correcto(nuevapoblacion)
                if nuevasuperficie:
                    pais["superficie"]=validar_numero_correcto(nuevasuperficie)
                print(f"Los datos de {pais["nombre"]} fueron actulizados correctamente")    
            except ValueError:
                print(f"Error: Valor ingresado es incorrecto [Ingrese valor entero positivo]")
                return
    else: print("Error: Pais no encontrado [puede cargar un país en la opción 1]")
            
def validar_numero_correcto(vnc_nuevapoblacion):
    numero_de_poblacion= int(vnc_nuevapoblacion)
    try:
        if numero_de_poblacion <=0:
            raise ValueError #Lanza error si pasa esto (habilita el except del valuerror)
        return numero_de_poblacion   
    except ValueError:
        raise ValueError(f"Error: El valor ingresado debe ser un valor entero positivo")

        
    
        
          
# --------------------------------------------------
#                  MAIN DEL SISTEMA
# --------------------------------------------------
print("\nCargando datos...")
#carga de datos del archivo en variable
ruta_actual = os.path.dirname(__path__ if '__path__' in locals() else __file__)
archivopaises= os.path.join(ruta_actual, "datos/paises.csv")
paises=cargardatos(archivopaises)
print(f"PRINT DE [PAISES] FUERA DE FUNCION: {paises}")
print("Datos cargados correctamente!")

while True:
    menu()
    opcion=input("Ingrese una opción numerica [1-8]: ").strip()
    try:
        if opcion== "1":
            pass
        elif opcion== "2":
            actualizardatospais(paises)
        elif opcion== "3":
            pass
        elif opcion== "4":
            pass
        elif opcion== "5":
            pass
        elif opcion== "6":
            pass
        elif opcion== "7":
            pass
        elif opcion== "8":
            pass
            break
            #guardardatos(paises) #GUARDAR ANTES DE SALIR
        else:
            print("Error: Opción seleccionada no es correcta, reintente: ")
    except ValueError:
            print("Error: Valor ingresado es incorrecto") #ponerlo????????????
    