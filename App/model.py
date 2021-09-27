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
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def estructuradatos(opciones):
    if opciones == 1:
        temp = 'SINGLE_LINKED'
    else:
        temp = 'ARRAY_LIST'
    return temp 

def newCatalog(): 
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'artistas': None,
               'obras': None}

    catalog['artistas'] = lt.newList(estructuradatos,cmpfunction=compareartistas)
    catalog['obras'] = lt.newList(estructuradatos)
    
    return catalog

# Funciones para agregar informacion al catalogo

def cargarCatalogoArtistas(catalog, artistaName):
    
  
    ltArtistas = catalog['artistas']
    artistaNuevo = newArtista(artistaName["ConstituentID"],artistaName["DisplayName"], artistaName["ArtistBio"], artistaName["Nationality"], artistaName["Gender"],artistaName["BeginDate"], artistaName["EndDate"],artistaName["Wiki QID"],artistaName["ULAN"])
    lt.addLast(ltArtistas, artistaNuevo)


def cargarCatalogoObras(catalog, obraName):
    
  
    ltObras = catalog['obras']
    obraNuevo = newObra(obraName["ObjectID"],obraName["Title"],obraName["ConstituentID"],obraName["Date"], obraName["Medium"], obraName["Dimensions"], obraName["CreditLine"],obraName["AccessionNumber"],obraName["Classification"],obraName["Department"], obraName["DateAcquired"],obraName["Cataloged"],obraName["URL"],obraName["Circumference (cm)"],obraName["Depth (cm)"],obraName["Diameter (cm)"], obraName["Height (cm)"],obraName["Length (cm)"],obraName["Weight (kg)"],obraName["Width (cm)"],obraName["Seat Height (cm)"],obraName["Duration (sec.)"])
    lt.addLast( ltObras, obraNuevo)    


def relacionArtistaObra(catalog,catalog2):
    if catalog['artistas']['ConstituentID']==catalog2['obras']['ConstituentID']:
        return True


'''
 artistas= catalog['artistas']
 obras=catalog2['obras']

 artistas = sortConstituentID(artistas)
 obras=sortConstituentID(obras)
 i =0 

 while i <lt.size(artistas):
     j=0
     artista= lt.getElement(artistas,i)

     while j< lt.size(obras):
         obra=lt.getElement(obras,j)

         if artista['ConstituentID'] == obra['ConstituentID']:
             lt.addLast(artista['obra'],obra)
             lt.addLast(obra['artista'],artista)
         j=+1
     i=+1
'''   

def addArtista(catalog, artistaName):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    ltArtistas = catalog['artistas']
    artistaNuevo = newArtista(artistaName["ConstituentID"],artistaName["DisplayName"], artistaName["ArtistBio"], artistaName["Nationality"], artistaName["Gender"],artistaName["BeginDate"], artistaName["EndDate"],artistaName["Wiki QID"],artistaName["ULAN"])
    print(artistaNuevo)
    posartista = lt.isPresent(ltArtistas, artistaNuevo)
    if posartista > 0:
        artista = lt.getElement(ltArtistas, posartista)
        return artista
    else:
        lt.addLast(ltArtistas, artistaNuevo)
        return artistaNuevo


def addObra(catalog, obraName):
    
    ltObras = catalog['obras']
    obraNuevo = newObra(obraName["ObjectID"],obraName["Title"],obraName["ConstituentID"],obraName["Date"], obraName["Medium"], obraName["Dimensions"], obraName["CreditLine"],obraName["AccessionNumber"],obraName["Classification"],obraName["Department"], obraName["DateAcquired"],obraName["Cataloged"],obraName["URL"],obraName["Circumference (cm)"],obraName["Depth (cm)"],obraName["Diameter (cm)"], obraName["Height (cm)"],obraName["Length (cm)"],obraName["Weight (kg)"],obraName["Width (cm)"],obraName["Seat Height (cm)"],obraName["Duration (sec.)"])
    print(obraNuevo) 
    posobra = lt.isPresent(ltObras, obraNuevo)
    if posobra > 0:
        obra = lt.getElement(ltObras, posobra)
        return obra
    else:
        lt.addLast(ltObras, obraNuevo)
        return obraNuevo

# Funciones para creacion de datos

def newArtista(id,name,artistbio,nationality,gender,beginDate,endDate,wiki,ulan):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    artista = {'ConstituentID': "", 'DisplayName': "", "ArtistBio": "" , "Nationality": "", "Gender": "","BeginDate": ""  , "EndDate" : "", "Wiki QID": "", "ULAN": "" }
    artista['ConstituentID'] = id
    artista['DisplayName'] = name
    artista['ArtistBio'] = artistbio
    artista['Nationality'] = nationality
    artista['Gender'] = gender
    artista['BeginDate'] = int(beginDate)
    artista['Nationality'] = nationality
    artista['EndDate'] = int(endDate)
    artista['ConstituentID'] = int(id)
    artista['ArtistBio'] = artistbio
    artista['WikiQID'] = wiki 
    artista['ULAN'] = ulan 
    #artista ['obra'] = lt.newList('ARRAY_LIST') 
    return artista

def newObra(objectID,title,constituentID,date,medium,dimensions,creditLine,accessionNumber,classification,department,dateAcquired,cataloged,url,circumference,depth,diameter,height,length,weight,width,seatHeight,duration):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    obra = {"ObjectID": "",'Title': "", "ConstituentID": "", "Date" : "", "Medium" : "", "Dimensions" : "", "CreditLine" : "", "AccessionNumber" : "", "Classification" : "", "Department": "", "DateAcquired" : "", "Cataloged": "", "URL" : "","Circumference (cm)": "","Depth (cm)": "", "Diameter (cm)": "","Height (cm)": "","Length (cm)": "","Weight (kg)": "","Width (cm)": "","Seat Height (cm)": "","Duration (sec.)": ""}
    obra['ObjectID'] = objectID
    obra['Title'] = title
    obra['Date'] = date
    obra['ConstituentID'] = constituentID
    obra['Medium'] = medium
    obra['Dimensions'] = dimensions
    obra['CreditLine'] = creditLine
    obra['Department'] = department
    obra['DateAcquired'] = dateAcquired
    #obra['ObjectID'] = objectID
    obra['Diameter (cm)'] = diameter
    obra['Circumference (cm)'] = circumference
    obra['Depth (cm)'] = depth 
    obra['AccessionNumber'] = accessionNumber
    obra['Classification'] = classification 
    obra['Cataloged'] = cataloged
    obra['URL'] = url 
    obra['Height (cm)'] = height
    obra['Length (cm)'] = length
    obra['Weight (cm)'] = weight
    obra['Width (cm)'] = width
    obra['Seat Height (cm)'] = seatHeight
    obra['Duration (sec.)'] = duration
    #obra['artista'] = lt.newList('ARRAY_LIST')
    return obra   
 

# Funciones de consulta


def sizesArtistas(catalog):
    """
    """
    return lt.size(catalog['artistas'])

def sizesObras(catalog):
    """
    """
    return lt.size(catalog['obras'])

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtworkByDateAcquired(artwork1,artwork2):
    """
    Devuelve verdadero (True) si el DateAcquired de artwork1 < artwork2
        Args: 
        Artwork1: informacion de la primera obra de DateAcquired
        Artwork2: informacion de la segunda obra de DateAcquired
    """
    respuesta = False 
    if artwork1['DateAcquired'] < artwork2['DateAcquired']:
        respuesta = True 
    return respuesta

def cmpArtistasPorAño(artista1, artista2):
    rta=False
    if artista1['BeginDate'] < artista2['BeginDate']:
        rta =True
    return rta

def cmpObrasPorAño(obra1, obra2):
    rta=False
    if obra1['Date'] < obra2['Date']:
        rta =True
    return rta

def artistaportecnica(catalog,name):
    """
    recibe el nombre de un artista, adquiere el ID del artista, identifica las obras creadas con el ID, clasifica las obras por medio
    """
    for artista in catalog['artistas']: 
        if name == artista['DisplayName']:
            id = artista['ConstituentID']
            break 
    lista = lt.newList()
    for obra in catalog['obras']:
        autores = obra['ConstituentID'][1:-1].split(',') 
        for i in autores:
            if i == id: 
                lista.append(obra)
    obraartista = len(lista) 
    tecnica = lt.newList()
    for j in lista: 
        tec = j['Medium'] 
        tecnica.append(tec)
    tecnica2 = list(set(tecnica))
    tecnicasartista = len(tecnica2)
    reptecnica = lt.newList()
    for k in tecnica2:
        reptecnica.append(tecnica.count(k))
    maximo = max(reptecnica)
    indice = reptecnica.index(maximo)
    masusada = tecnica2[indice] 
# Funciones de ordenamiento

def tipoSorter(opciones,lst):
    if opciones == 0:
        return insertionsort(lst)
    elif opciones == 1:
        return shellsort(lst)
    elif opciones == 2:
        return quicksort(lst)
    else:
        print ("error")

def insertionsort(lst):
    size = lt.size(lst)
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 > 1) and (cmpArtworkByDateAcquired(
               lt.getElement(lst, pos2), lt.getElement(lst, pos2-1))):
            lt.exchange(lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
    return lst


def shellsort(lst):
    n = lt.size(lst)
    h = 1
    while h < n/3:   # primer gap. La lista se h-ordena con este tamaño
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and cmpArtworkByDateAcquired(
                                lt.getElement(lst, j+1),
                                lt.getElement(lst, j-h+1)):
                lt.exchange(lst, j+1, j-h+1)
                j -= h
        h //= 3    # h se decrementa en un tercio
    return lst


def quicksort(lst):
    quicksort(lst, 1, lt.size(lst),cmpArtworkByDateAcquired)
    return lst

def InsercionOrdenarfechaobras(catalog):
    size = lt.size(catalog['obras'])
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1                                                   
        while (pos2 > 1) and (cmpArtworkByDateAcquired (lt.getElement(catalog['obras'], pos2), lt.getElement(catalog['obras'], pos2-1))):
            lt.exchange(catalog['obras'], pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
    return catalog 

def selectionsort(lst, cmpfunction):
    size = lt.size(lst)
    pos1 = 1
    while pos1 < size:
        minimum = pos1    # minimun tiene el menor elemento
        pos2 = pos1 + 1
        while (pos2 <= size):
            if (cmpfunction(lt.getElement(lst, pos2),
               (lt.getElement(lst, minimum)))):
                minimum = pos2  # minimum = posición elemento más pequeño
            pos2 += 1
        lt.exchange(lst, pos1, minimum)  # elemento más pequeño -> elem pos1
        pos1 += 1
    return lst

# funcion de ordenamiento - tiempo 
"""
def sortObras(catalog,opcion):
    sub_list = lt.subList(catalog['obras'], 1, lt.size(catalog['obras']))
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list=tipoSorter(opcion, sub_list)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg,sorted_list
"""

def mergeSort(lst, cmpfunction):
    size = lt.size(lst)
    if size > 1:
        mid = (size // 2)
        """se divide la lista original, en dos partes, izquierda y derecha,
        desde el punto mid."""
        leftlist = lt.subList(lst, 1, mid)
        rightlist = lt.subList(lst, mid+1, size - mid)

        """se hace el llamado recursivo con la lista izquierda y derecha"""
        mergeSort(leftlist, cmpfunction)
        mergeSort(rightlist, cmpfunction)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 1

        leftelements = lt.size(leftlist)
        rightelements = lt.size(rightlist)

        while (i <= leftelements) and (j <= rightelements):
            elemi = lt.getElement(leftlist, i)
            elemj = lt.getElement(rightlist, j)
            """compara y ordena los elementos"""
            if cmpfunction(elemj, elemi):   # caso estricto elemj < elemi
                lt.changeInfo(lst, k, elemj)
                j += 1
            else:                            # caso elemi <= elemj
                lt.changeInfo(lst, k, elemi)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i <= leftelements:
            lt.changeInfo(lst, k, lt.getElement(leftlist, i))
            i += 1
            k += 1

        while j <= rightelements:
            lt.changeInfo(lst, k, lt.getElement(rightlist, j))
            j += 1
            k += 1
    return lst

def sortConstituentID(lst):
    size = lt.size(lst)
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 > 1) and (cmpConstitudID(
               lt.getElement(lst, pos2), lt.getElement(lst, pos2-1))):
            lt.exchange(lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
    return lst


def getUltimosPrimerosTresArtistas(catalog,fechaInicio,fechaFin):
    """
    """
    artista = catalog['artistas']
    listaOrdenada = mergeSort(artista,cmpArtistasPorAño)
    i=0
    posicioninicial= 0
    posicionfinal= 0

    while i < lt.size(listaOrdenada): 

        artista1 = lt.getElement(listaOrdenada,i) 

        if (artista1['BeginDate'] == fechaInicio or artista1['BeginDate'] > fechaInicio) and posicioninicial == 0: 
            posicioninicial = i 

        if artista1['BeginDate'] <= fechaFin:
            posicionfinal = i
        i =  i + 1

    if posicionfinal == 0:
        posicionfinal = i-1

    elementos = (posicionfinal - posicioninicial + 1)

    listainicial=lt.subList(listaOrdenada,posicioninicial,elementos) 

    sublistaprimero3=lt.subList(listainicial,0,3) 
    var =  lt.size(listainicial)
    sublistaultimos3=lt.subList(listainicial,var-3,3)
 
    return([sublistaprimero3,sublistaultimos3]) 

def getUltimosPrimerosTresObras(catalog,fechaInicio,fechaFin):
    """
    """
    obra = catalog['obras']
    listaOrdenada = mergeSort(obra,cmpObrasPorAño)
    i=0
    posicioninicial= 0
    posicionfinal= 0


    while i < lt.size(listaOrdenada): 

        obra1 = lt.getElement(listaOrdenada,i) 
        if obra1['Date'] != '':
            fecha = int(obra1['Date'])

            if (fecha > fechaInicio) and posicioninicial == 0: 
                posicioninicial = i 

            if fecha <= fechaFin:
                posicionfinal = i
        i =  i + 1

    if posicionfinal == 0:
        posicionfinal = i-1

    elementos = (posicionfinal - posicioninicial + 1)

    listainicial=lt.subList(listaOrdenada,posicioninicial,elementos) 

    sublistaprimero3=lt.subList(listainicial,0,3) 
    var =  lt.size(listainicial)
    sublistaultimos3=lt.subList(listainicial,var-3,3)
 
    return([sublistaprimero3,sublistaultimos3]) 
    sizelt=lt.size(listaOrdenada)

    posicioninicial= 0
   
    found = False
    posicion = 0

    while  posicion < sizelt and not found:
        artista1=lt.getElement(listaOrdenada,posicion)
        
        if artista1['BeginDate']<fechaInicio:
            posicion =  posicion + 1

        elif artista1['BeginDate']>=fechaInicio:
            found = True
            posicioninicial=posicion
            
    subLista1= lt.subList(listaOrdenada,posicioninicial,(sizelt-posicioninicial))

    posicionfinal = 0
    found2 = False
    posicion2 = 0
    sizelt2=lt.size(subLista1)

    while  posicion2 < sizelt2 and not found2:
        artista2=lt.getElement(subLista1,posicion2)
        
        if artista2['BeginDate']<=fechaFin:
            posicion2 =  posicion2 + 1
            posicionfinal=posicion2+1

        if artista2['BeginDate']>fechaFin:
         found2 = True
         

    subLista2=lt.subList(subLista1,0,posicionfinal)
    return (subLista2)

