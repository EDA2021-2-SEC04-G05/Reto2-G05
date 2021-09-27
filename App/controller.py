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
def initCatalog(opciones):
    """
    """
    model.estructuradatos(opciones)
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    """
    Cargar los datos de los archivos y cargar los datos en la estructura de datos
    """
    loadArtworks(catalog)
    loadArtists(catalog)
    
    

def loadArtists(catalog):
    """

    """
    artistsfile = cf.data_dir.replace("\\","/") + '/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile,encoding= 'utf-8'))
    for artists in input_file:
        model.cargarCatalogoArtistas(catalog,artists)

def loadArtworks(catalog):
    """

    """
    artworksfile = cf.data_dir.replace("\\","/") + '/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile,encoding= 'utf-8'))
    for artworks in input_file:
        model.cargarCatalogoObras(catalog,artworks) 

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def getUltimosPrimerosTresArtistas(catalog,fechaInicio,fechaFin):

    ultimastres= model.getUltimosPrimerosTresArtistas(catalog,fechaInicio,fechaFin)
    return ultimastres

def getUltimosPrimerosTresObra(catalog,fechaInicio,fechaFin):

    ultimastres= model.getUltimosPrimerosTresObras(catalog,fechaInicio,fechaFin)
    return ultimastres

def getTamañoSubLista(catalog,valor):
    tamaño = model.tamañoMuestra(catalog, valor)
    return tamaño 

def getSorter(catalog,sort):
   ordenamiento = model.tipoSorter(catalog,sort)
   return ordenamiento
    

