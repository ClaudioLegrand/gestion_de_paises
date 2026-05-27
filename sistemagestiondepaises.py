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
'''
---------
MAIN DEL SISTEMA
---------'''
print("\nCargando datos...")
#CARGAR ARCHIVO ANTES DE ESTO
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
        else:
            print("Error: Opción seleccionada no es correcta, reintente: ")
    except ValueError:
            print("Error: Valor ingresado es incorrecto") #ponerlo????????????
    