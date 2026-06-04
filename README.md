# Trabajo Práctico Integrador – Gestión de Datos de Países en Python

## Descripción del programa

Aplicación desarrollada en Python 3.14.0 que permite gestionar un dataset de países. El sistema lee y guarda los datos desde y hacia un archivo CSV, y ofrece funcionalidades de:

- Alta de nuevos países.
- Actualización de población y superficie.
- Búsqueda por nombre (coincidencia parcial o total).
- Filtrado por continente, rango de población y rango de superficie.
- Ordenamiento por nombre, población o superficie estas ultimas 2 de forma (ascendente/descendente).
- Estadísticas básicas: país con mayor/menor población, promedio de población, promedio de superficie y cantidad de países por continente.

El proyecto fue desarrollado como Trabajo Integrador de la materia Programación 1, con el objetivo de aplicar estructuras de datos (listas, diccionarios), modularización mediante funciones, manejo de archivos CSV y algoritmos de ordenamiento.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Integrantes

- **Claudio Legrand** (Comisión 19)
- **Christian Herrero** (Comision 8)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Requisitos

- Python 3.14.0
- No se requieren librerías externas (solo se usa `os` y `unicodedata`)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Instalación y ejecución

1. Clonar el repositorio:
Mediante bash con Google Colab de ser preferencia:
!git clone (https://github.com/ClaudioLegrand/gestion_de_paises)

2. Asegurar que exista la carpeta datos/ y dentro de ella el archivo paises.csv. Si no existe, el programa lo creará automáticamente al primer intento de carga.

3. Ejecutar el programa: sistemagestiondepaises.py

4. Funcionalidades del sistema:

Se desplegará el menu principal donde se podra observar las siguentes opciones:

-----------------------------------------
            GESTION DE PAISES                       
-----------------------------------------

1 - Agregar país
2 - Actualizar datos del país
3 - Buscar país
4 - Filtrar país
5 - Ordenar paises
6 - Mostrar estadisticas
7 - Ver todos los paises
8 - Salir

5. Seleccionar una opción a través del teclado númerico para interactuar con las opciones del sistema.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
*Ejemplos de entrada/salida*

1. Agregar pais:
   
Ingrese el nombre del país para agregar: Chile
Ingrese la población del país: 19600000
Ingrese la superficie del país: 756102
Seleccione continente:
          1 - America
          2 - Europa
          3 - Oceania
          4 - Africa
          5 - Asia
Seleccione continente: 1
País agregado y guardado correctamente!

2. Filtrar por rango de población:

Seleccione una opción: 2
Población mínima (Enter para sin límite): 50000000
Población máxima (Enter para sin límite): 200000000

Nombre               Población     Superficie  Continente
----------------------------------------------------------
Brasil               213,993,437   8,515,767   América
Japón                125,800,000     377,975   Asia

3. Estadísticas:

Total de paises: 4

Población
----------------------------------------
Mayor: Brasil (213,993,437 hab.)
Menor: Argentina (45,376,763 hab.)
Promedio de población: 117,286,550.00 hab.

Superficie
----------------------------------------
Promedio de superficie: 2,982,406.00 km.

Paises por continentes
----------------------------------------
America : 2 paises.
Africa  : 0 paises.
Europa  : 1 paises.
Asia    : 1 paises.
Oceania : 0 paises.

4. Ordenar países por nombre descendente:

¿Ordenar de forma ascendente o descendente?
1 - Asc | 2 - Des: 2

Nombre               Población     Superficie  Continente
-----------------------------------------------------------------
Japón                125,800,000     377,975   Asia
Brasil               213,993,437   8,515,767   América
Alemania              83,149,300     357,022   Europa
Argentina             45,376,763   2,780,400   América

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
*Links importantes*

Video de Youtube: [link]
Documento PDF: [drive]
Repositorio de Github: https://github.com/ClaudioLegrand/gestion_de_paises
