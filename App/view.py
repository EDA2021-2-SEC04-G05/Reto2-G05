"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
import model 
from DISClib.ADT import list as lt
assert cf

defauly_limit=1000
sys.setrecursionlimit(defauly_limit*100)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

# Funciones para la impresión de resultados

def printObrasByNacionalidad(nombre):
    """
    Imprime los libros que han sido clasificados con
    una etiqueta
    """
    if (nombre):
        print('Se encontraron: ' + str(lt.size(nombre)) + ' nacionalidad.')
        for nombre in lt.iterator(nombre):
            print(nombre['Title'])
        print("\n")
    else:
        print("No se econtraron libros.\n")

def printObrasByNacionalidad2(nombre):
    """
    Imprime los libros que han sido clasificados con
    una etiqueta
    """
    if (nombre):
        print('Se encontraron: ' + str(len(nombre)) + ' obras de esta nacionalidad.')
        for obra in nombre:
            print(obra['Title'])
        print("\n")
    else:
        print("No se encontraron libro.\n")

def printAuthorData(author,obras):
    """
    Imprime la información del autor seleccionado
    """
    if author and obras:
        nombre = author['DisplayName'].split(',')
        print('Autor encontrado: ' + nombre[0]) 
        #print('Promedio: ' + str(author['average_rating']))
        print('Total de libros: ' + str(len(obras)))
        #print(type(obras))
        for book in obras:
            print('Titulo: ' + book['Title'])
            print("\n")
    else:
        print('No se encontro el autor o no se encontraron obras de dicho autor.\n')


def printBooksbyTag(books):
    """
    Imprime los libros que han sido clasificados con
    una etiqueta
    """
    if (books):
        print('Se encontraron: ' + str(lt.size(books)) + ' Libros.')
        for book in lt.iterator(books):
            print(book['title'])
        print("\n")
    else:
        print("No se econtraron libros.\n")


def printBooksbyYear(books):
    """
    Imprime los libros que han sido publicados en un
    año
    """
    if(books):
        print('Se encontraron: ' + str(lt.size(books)) + ' Libros')
        for book in lt.iterator(books):
            print(book['title'])
        print("\n")
    else:
        print("No se encontraron libros.\n")


def printBestBooks(books):
    """
    Imprime la información de los mejores libros
    por promedio
    """
    size = lt.size(books)
    if size:
        print(' Estos son los mejores libros: ')
        for book in lt.iterator(books):
            print('Titulo: ' + book['title'] + '  ISBN: ' +
                  book['isbn'] + ' Rating: ' + book['average_rating'])
        print("\n")
    else:
        print('No se encontraron libros.\n')


# Menu de opciones

def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    print("1- Consultar la lista cronológica de los artistas")
    print("2- Consultar las obras adquiridas en el museo")
    print("3- Consultar las obras de un artista por técnica")
    print("4- Consultar las obras por la nacionalidad de sus creadores")
    print("5- Calcular el costo para transportar todas las obras de un departamento del MoMA")
    print("6- Consultar la nueva idea de exposición del museo según la disponibilidad del área del MoMA")
    print('7- Consultar obras por nacionalidad')
    print("8- Salir")

# Funciones de inicializacion  

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en el catalogo
    """
    controller.loadData(catalog)



# Menu principal

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 0: 
        print("Inicializando Catálogo ....")
        cont = controller.initCatalog()
        print("Cargando información de los archivos ....")
        controller.loadData(cont) 
        print('Artistas cargados: ' + str(controller.artistaSize(cont)))
        print('Obras cargados: ' + str(controller.obraSize(cont)))

    elif int(inputs[0]) == 1:
        number = input("Buscando libros del año?: ")
        books = controller.getBooksYear(cont, int(number)) 
        printBooksbyYear(books)

    elif int(inputs[0]) == 4:
        number = input("Buscando libros del año?: ")
        obras = controller.getObrasByNacionalidad(cont, (number))
        printObrasByNacionalidad(obras)

    elif int(inputs[0]) == 2:
        authorname = input("Nombre del autor a buscar: ")
        authorinfo = controller.getBooksByAuthor(cont, authorname) 
        authorbooks = controller.getObraByArtistaId(cont,authorinfo['ConstituentID'])
       # print(authorinfo,authorbooks) 
        printAuthorData(authorinfo,authorbooks) 

    elif int(inputs[0]) == 3:
        label = input("Etiqueta a buscar: ")
        books = controller.getBooksByTag(cont, label)
        printBooksbyTag(books)

    elif int(inputs[0]) == 7:
        number = input("Buscando obras del pais?: ")
        obras = controller.getObrasByNacionalidad2(cont, number)
        printObrasByNacionalidad2(obras)

    else:
        sys.exit(0)

