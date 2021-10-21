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
from prettytable import PrettyTable 
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from datetime import datetime, timedelta
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


def printArtistaByDate(artistas):
    """
    Imprime los artistas que nacieron en un rango de años
    """
    if(artistas):
        print('Se encontraron: ' + str(lt.size(artistas)) + ' artistas nacidos en el rango de fechas. ')
        x = PrettyTable()
        x.field_names = ['ConstituentID','DisplayName','BeginDate','Nationality','Gender','ArtistBio','Wiki QID','ULAN']
        if lt.size(artistas) <= 6:
            for artista in lt.iterator(artistas):
                x.add_row([artista['ConstituentID'],artista['DisplayName'],artista['BeginDate'],artista['Nationality'],artista['Gender'],artista['ArtistBio'],artista['Wiki QID'],artista['ULAN']]) 
            print(x)
        else:
            l = lt.size(artistas)
            #pos = [artistas[0],artistas[1],artistas[2],artistas[l-3],artistas[l-2],artistas[l-1]] 
            #pos = [artistas[1],artistas[2],artistas[3],artistas[l-2],artistas[l-1],artistas[l]] 
            pos = [
                lt.getElement(artistas,1),lt.getElement(artistas,2),
                lt.getElement(artistas,3),lt.getElement(artistas,l-2),
                lt.getElement(artistas,l-1),lt.getElement(artistas,l)
            ]
            for artista in pos:
                x.add_row([artista['ConstituentID'],artista['DisplayName'],artista['BeginDate'],artista['Nationality'],artista['Gender'],artista['ArtistBio'],artista['Wiki QID'],artista['ULAN']]) 
            print(x) 
    
    else:
        print("No se encontraron artistas en este rango de años.\n")
    
def printObraByDate(obras):
    """
    Imprime las obras que en un rango de años
    """
    if(obras):
        print('Se encontraron: ' + str(lt.size(obras)) + ' obras en el rango de fechas. ')
        x = PrettyTable()
        x.field_names = ['ObjectID','Title','ArtistsNames','Medium','Dimensions','Date','DateAcquired','URL']
        ancho_max = 18
        #x._max_width ={'Field 1': ancho_max,'Field 2': ancho_max,'Field 3': ancho_max,'Field 4': ancho_max,'Field 5':ancho_max ,'Field 6': ancho_max,'Field 7':ancho_max}
        if lt.size(obras) <= 6:
            for obra in lt.iterator(obras):
                a = [obra['ObjectID'],obra['Title'],IDtoName(obra,cont),obra['Medium'],obra['Dimensions'],obra['Date'],obra['DateAcquired'],obra['URL']]
                d = []
                for i in a:
                    d.append(salto(i,ancho_max))
                x.add_row(d)
            print(x)
        else:
            l = lt.size(obras)
            #pos = [artistas[0],artistas[1],artistas[2],artistas[l-3],artistas[l-2],artistas[l-1]] 
            #pos = [artistas[1],artistas[2],artistas[3],artistas[l-2],artistas[l-1],artistas[l]] 
            pos = [
                lt.getElement(obras,1),lt.getElement(obras,2),
                lt.getElement(obras,3),lt.getElement(obras,l-2),
                lt.getElement(obras,l-1),lt.getElement(obras,l)
            ]
            for obra in pos:
                a = [obra['ObjectID'],obra['Title'],IDtoName(obra,cont),obra['Medium'],obra['Dimensions'],obra['Date'],obra['DateAcquired'],obra['URL']]
                d = []
                for i in a:
                    d.append(salto(i,ancho_max))
                x.add_row(d)
            print(x) 
    
    else:
        print("No se encontraron artistas en este rango de años.\n")

def IDtoName(obra,cont):
    ids = str(obra['ConstituentID'][1:-1].replace(' ','')).split(',')
    nombres = ''
    for id in ids:
        renglon = controller.getArtistaById(cont,id)
        nombre = renglon['DisplayName'].split(',') 
        nombres = nombres + nombre[0] + ', ' 
    return nombres[:-2]

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

def salto(cad,lon): #texto muy largo 
	if len(cad)>lon:
		pos=lon-1
		for i in cad[lon-1:0:-1]:
			if i==" ":
				sal=cad[0:pos]+"\n"+salto(cad[pos+1:],lon)
				return sal
			pos=pos-1
		sal=cad[0:lon-1]+"\n"+salto(cad[lon-1:],lon)
		return sal
	else:
		return cad

def rango_fechas(fi,ff):
    format = "%Y-%m-%d"
    inicio = datetime.strptime(fi,format)
    fin = datetime.strptime(ff,format)
    lista_fechas = [(inicio + timedelta(days=d)).strftime("%Y-%m-%d")
                    for d in range((fin - inicio).days + 1)] 
    return lista_fechas 

# Menu de opciones

def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    print("1- Consultar los artistas nacidos entre dos fechas")
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
        print(mp.get(cont['obraAcquisition'],'1963-11-08'))
        #print(controller.getArtistaById(cont,'3716'))
        #print(controller.getArtistaById(cont,'3716')['DisplayName'])
        #print(mp.get(cont['artistaIds'],'3716')['3716']) 
        #print(mp.get(mp.get(cont['artistaIds'],'3716'),'3716')) 

    elif int(inputs[0]) == 1:
        anho1 = input("Agregar año inicial:")
        anho2 = input("Agregar año final:")
        lista = lt.newList()
        for i in range(int(anho1),int(anho2) + 1):
            nacidos = controller.getArtistaByDate(cont,i)
            controller.concatlist(lista,nacidos)
        printArtistaByDate(lista)

    elif int(inputs[0]) == 4:
        number = input("Buscando libros del año?: ")
        obras = controller.getObrasByNacionalidad(cont, (number))
        printObrasByNacionalidad(obras)

    elif int(inputs[0]) == 2:
        anho1 = input("Agregar fecha inicial en formato AAAA-MM-DD:")
        anho2 = input("Agregar fecha final en formato AAAA-MM-DD:")
        lista = lt.newList()
        for i in rango_fechas(anho1,anho2):
            creados = controller.getObraByAcquisition(cont,i)
            controller.concatlist2(lista,creados)
        printObraByDate(lista)

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

