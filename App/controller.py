"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    #model.estructuradatos(opciones)
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)

def loadArtists(catalog):
    """
    Carga los libros del archivo.  Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    """
    artistsfile = cf.data_dir.replace("\\","/") + '/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile,encoding= 'utf-8'))
    for artists in input_file:
        model.addArtista(catalog,artists)

def loadArtworks(catalog):
    """
    Carga todos los tags del archivo e indica al modelo
    que los adicione al catalogo
    """
    artworksfile = cf.data_dir.replace("\\","/") + '/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile,encoding= 'utf-8'))
    for artworks in input_file:
        model.addObra(catalog,artworks) 

# Funciones de consulta sobre el catálogo

def getUltimosPrimerosTresArtistas(catalog,fechaInicio,fechaFin):

    ultimastres= model.getUltimosPrimerosTresArtistas(catalog,fechaInicio,fechaFin)
    return ultimastres

def getUltimosPrimerosTresObra(catalog,fechaInicio,fechaFin):

    ultimastres= model.getUltimosPrimerosTresObras(catalog,fechaInicio,fechaFin)
    return ultimastres

def getObrasByNacionalidad(catalog, nombre):
    """
    Retorna los libros que fueron etiquetados con el tag
    """
    return model.getObrasByNacionalidad(catalog, nombre)

def getObrasByNacionalidad2(catalog, pais):
    """
    Retorna los libros que fueron etiquetados con el tag
    """
    return model.getObrasByNacionalidad2(catalog, pais)

def getBestBooks(catalog, number):
    """
    Retorna los mejores libros según su promedio
    """
    bestbooks = model.getBestBooks(catalog, number)
    return bestbooks

def countBooksByTag(catalog, tag):
    """
    Retorna los libros que fueron etiquetados con el tag
    """
    return model.countBooksByTag(catalog, tag)

def artistaSize(catalog):
    """
    Numero de libros cargados al catalogo
    """
    return model.artistaSize(catalog)

def obraSize(catalog):
    """
    Numero de libros cargados al catalogo
    """
    return model.obraSize(catalog)

def booksSize(catalog):
    """
    Numero de libros cargados al catalogo
    """
    return model.booksSize(catalog)


def authorsSize(catalog):
    """
    Numero de autores cargados al catalogo
    """
    return model.authorsSize(catalog)


def tagsSize(catalog):
    """
    Numero de tags cargados al catalogo
    """
    return model.tagsSize(catalog)


def getBooksByAuthor(catalog, authorname):
    """
    Retorna los libros de un autor
    """
    authorinfo = model.getBooksByAuthor(catalog, authorname)
    return authorinfo

def getObraByArtistaId(catalog, authorid):
    """
    Retorna los libros de un autor
    """
    authorinfo = model.getObraByArtistaId(catalog, authorid)
    return authorinfo

def getBooksByTag(catalog, tagname):
    """
    Retorna los libros que han sido marcados con
    una etiqueta
    """
    books = model.getBooksByTag(catalog, tagname)
    return books


def getBooksYear(catalog, year):
    """
    Retorna los libros que fueron publicados
    en un año
    """
    books = model.getBooksByYear(catalog, year)
    return books
