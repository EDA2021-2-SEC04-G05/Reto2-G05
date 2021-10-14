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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores
y otra para géneros
"""

# Construccion de modelos


def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'artistas': None,
               'artistamap':None,
               'obras': None,
               'artistaIds': None,
               'obraIds':None,
               'nombreArtista':None,
               'nombreObra':None,
               'obraMedium':None,
               'artistaNationality':None,
               'idArtistaObra':{},
               'obrasporNacionalidad':{}}

    """
    Esta lista contiene todo los libros encontrados
    en los archivos de carga.  Estos libros no estan
    ordenados por ningun criterio.  Son referenciados
    por los indices creados a continuacion.
    """
    catalog['artistas'] = lt.newList('SINGLE_LINKED', compareArtistaByName)

    catalog['obras'] = lt.newList('SINGLE_LINKED', compareObraByName)

    """
    A continuacion se crean indices por diferentes criterios
    para llegar a la informacion consultada.  Estos indices no
    replican informacion, solo referencian los libros de la lista
    creada en el paso anterior.
    """

    """
    Este indice crea un map cuya llave es el identificador del libro
    """
    catalog['artistaIds'] = mp.newMap(15223,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareArtistasIds)
    #print(catalog['artistaIds'])
    """
    Este indice crea un map cuya llave es el autor del libro
    """
    catalog['obraIds'] = mp.newMap(138150,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareObrasIds)
   
    catalog['obraMedium'] = mp.newMap(138150,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMediumByName)
    
    catalog['artistaNationality'] = mp.newMap(138150,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareNationalityByName)
    
    catalog['artistamap'] = mp.newMap(138150,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareArtistaByName)

    """
    catalog['idArtistaObra'] = mp.newMap(138150,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareArtistaById)
    """
    return catalog

# Funciones para creacion de datos

def newArtista(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    author = {'name': "",
              "books": None,
              "average": 0,
              "average_rating": 0}
    author['name'] = name
    author['books'] = lt.newList('SINGLE_LINKED', compareAuthorsByName)
    return author

def newAuthor(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    author = {'name': "",
              "books": None,
              "average": 0,
              "average_rating": 0}
    author['name'] = name
    author['books'] = lt.newList('SINGLE_LINKED', compareAuthorsByName)
    return author


def newBookTag(name, id):
    """
    Esta estructura crea una relación entre un tag y los libros que han sido
    marcados con dicho tag.  Se guarga el total de libros y una lista con
    dichos libros.
    """
    tag = {'name': '',
           'tag_id': '',
           'total_books': 0,
           'books': None,
           'count': 0.0}
    tag['name'] = name
    tag['tag_id'] = id
    tag['books'] = lt.newList()
    return tag


# Funciones para agregar informacion al catalogo

def addArtista(catalog, artista):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Adicionalmente se guarda en el indice de autores, una referencia
    al libro.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    llave = artista['ConstituentID']
    lt.addLast(catalog['artistas'], artista)
    mp.put(catalog['artistaIds'], llave, artista)
    nombre = artista['DisplayName'].split(",")  # Se() obtienen los nombres de los artistas
    mp.put(catalog['artistamap'],nombre[0], artista)
    nacionalidad = artista['Nationality']
    try:
        id=list(catalog["obrasporNacionalidad"].keys()).index(nacionalidad)
    except:
        id=-1
    if id==-1:
        catalog["obrasporNacionalidad"][nacionalidad]=[[artista["ConstituentID"]],[]]
    else:
        catalog["obrasporNacionalidad"][nacionalidad][0].append(artista["ConstituentID"])   
    return nombre

def addObra(catalog, obra):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Adicionalmente se guarda en el indice de autores, una referencia
    al libro.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    llave = obra['ObjectID'] 
    lt.addLast(catalog['obras'], obra)
    mp.put(catalog['obraIds'],llave, obra)
    if type(obra['ConstituentID']) == str:
            j = obra['ConstituentID'][1:-1].split(',')
    for i in j: 
        try: 
            id = list(catalog['idArtistaObra'].keys()).index(i)
        except:
            id = - 1 
        if id != -1:
            catalog['idArtistaObra'][i].append(obra)
        else:
            catalog['idArtistaObra'][i] = [obra] 
        for n in list(catalog["obrasporNacionalidad"].keys()):
            for artistaid in catalog["obrasporNacionalidad"][n][0]:
                if i==artistaid:
                    catalog["obrasporNacionalidad"][n][1].append(obra)
            #print(id,i)
    nombre = obra['Title'].split(",")  # Se obtienen los nombres de las obras
    return nombre

def addBook(catalog, book):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Adicionalmente se guarda en el indice de autores, una referencia
    al libro.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['books'], book)
    mp.put(catalog['bookIds'], book['goodreads_book_id'], book)
    nombre = book['authors'].split(",")  # Se obtienen los autores
    return nombre

def addBookYear(catalog, book):
    """
    Esta funcion adiciona un libro a la lista de libros que
    fueron publicados en un año especifico.
    Los años se guardan en un Map, donde la llave es el año
    y el valor la lista de libros de ese año.
    """
    try:
        years = catalog['years']
        if (book['original_publication_year'] != ''):
            pubyear = book['original_publication_year']
            pubyear = int(float(pubyear))
        else:
            pubyear = 2020
        existyear = mp.contains(years, pubyear)
        if existyear:
            entry = mp.get(years, pubyear)
            year = me.getValue(entry)
        else:
            year = newYear(pubyear)
            mp.put(years, pubyear, year)
        lt.addLast(year['books'], book)
    except Exception:
        return None


def newYear(pubyear):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'year': "", "books": None}
    entry['year'] = pubyear
    entry['books'] = lt.newList('SINGLE_LINKED', compareYears)
    return entry


def addBookAuthor(catalog, authorname, book):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    authors = catalog['authors']
    existauthor = mp.contains(authors, authorname)
    if existauthor:
        entry = mp.get(authors, authorname)
        author = me.getValue(entry)
    else:
        author = newAuthor(authorname)
        mp.put(authors, authorname, author)
    lt.addLast(author['books'], book)
    author['average'] += float(book['average_rating'])
    totbooks = lt.size(author['books'])
    if (totbooks > 0):
        author['average_rating'] = author['average'] / totbooks


def addTag(catalog, tag):
    """
    Adiciona un tag a la tabla de tags dentro del catalogo y se
    actualiza el indice de identificadores del tag.
    """
    newtag = newBookTag(tag['tag_name'], tag['tag_id'])
    mp.put(catalog['tags'], tag['tag_name'], newtag)
    mp.put(catalog['tagIds'], tag['tag_id'], newtag)


def addBookTag(catalog, tag):
    """
    Agrega una relación entre un libro y un tag.
    Para ello se adiciona el libro a la lista de libros
    del tag.
    """
    bookid = tag['goodreads_book_id']
    tagid = tag['tag_id']
    entry = mp.get(catalog['tagIds'], tagid)

    if entry:
        tagbook = mp.get(catalog['tags'], me.getValue(entry)['name'])
        tagbook['value']['total_books'] += 1
        tagbook['value']['count'] += int(tag['count'])
        book = mp.get(catalog['bookIds'], bookid)
        if book:
            lt.addLast(tagbook['value']['books'], book['value'])

def obraporNacionalidad(catalog,nacionalidad):
    lista_nacionalidad = lt.newList()
    for artista in catalog['artistas']:
        if lt.isPresent(lista_nacionalidad,artista['Nationality']) == False:
            lista_nacionalidad.append(artista['Nationality']) 
    return len(lista_nacionalidad)

# ==============================
# Funciones de consulta
# ==============================

def getObrasByNacionalidad(catalog, nombre):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    nacionalidad = mp.get(catalog['artistaNationality'], nombre)
    obras = None
    if nacionalidad:
        obras = me.getValue(nacionalidad)['obras']
    return obras

def getObrasByNacionalidad2(catalog, pais):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    try:
        obras = catalog['obrasporNacionalidad'][pais][1]
    except:
        obras = None 
    return obras 
   
def getObraByArtistaId(catalog, authorid):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    try: 
        author = catalog['idArtistaObra'][authorid]
    except:
        author = None
    return author 

def getBooksByAuthor(catalog, authorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    author = mp.get(catalog['artistamap'], authorname) 
    if author:
        return me.getValue(author)
    return None


def getBooksByTag(catalog, tagname):
    """
    Retornar la lista de libros asociados a un tag
    """
    tag = mp.get(catalog['tags'], tagname)
    books = None
    if tag:
        books = me.getValue(tag)['books']
    return books


def getBooksByYear(catalog, year):
    """
    Retorna los libros publicados en un año
    """
    year = mp.get(catalog['Date'], year)
    if year:
        return me.getValue(year)['books']
    return None


def artistaSize(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog['artistas'])


def obraSize(catalog):
    """
    Numero de autores en el catalogo
    """
    return mp.size(catalog['obras'])


# ==============================
# Funciones de Comparacion
# ==============================

def compareArtistasIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareObrasIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1
def compareArtistaById(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareMediumByName(name, medio):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(medio)
    if (name == authentry):
        return 0
    elif (name > authentry):
        return 1
    else:
        return -1

def compareArtistaByName(name, artista):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(artista)
    if (name == authentry):
        return 0
    elif (name > authentry):
        return 1
    else:
        return -1

def compareObraByName(name, obra):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(obra)
    if (name == authentry):
        return 0
    elif (name > authentry):
        return 1
    else:
        return -1

def compareNationalityByName(name, nacionalidad):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(nacionalidad)
    if (name == authentry):
        return 0
    elif (name > authentry):
        return 1
    else:
        return -1

def compareMapBookIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1


def compareAuthorsByName(keyname, author):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(author)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1


def compareTagNames(name, tag):
    tagentry = me.getKey(tag)
    if (name == tagentry):
        return 0
    elif (name > tagentry):
        return 1
    else:
        return -1


def compareTagIds(id, tag):
    tagentry = me.getKey(tag)
    if (int(id) == int(tagentry)):
        return 0
    elif (int(id) > int(tagentry)):
        return 1
    else:
        return 0


def compareMapYear(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0


def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return 0

