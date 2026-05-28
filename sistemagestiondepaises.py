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
            next(archivopaises)
            for fila in archivopaises:
                partes=fila.strip().split(",")
                dirpaises = {
                    "pais": partes[0], #. <------------------- MEJORAR PARA NO PONER INDICES -- QUE PASA SI SE AGREGA CAPITAL? 
                    "poblacion": partes[1],
                    "superficie": partes[2],
                    "continente": partes[3]
                }
                paises.append(dirpaises)
        print(paises)
    
# --------------------------------------------------
#                  MAIN DEL SISTEMA
# --------------------------------------------------

print("\nCargando datos...")
#carga de datos del archivo en variable
ruta_actual = os.path.dirname(__path__ if '__path__' in locals() else __file__)
archivopaises= os.path.join(ruta_actual, "datos/paises.csv")
paises=cargardatos(archivopaises)
print("Datos cargados correctamente!")

while True:
    menu()
    opcion=input("Ingrese una opción numerica [1-8]: ")
    try:
        if opcion== "1":
            pass
        elif opcion== "2":
            pass
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
    