from datetime import *
from os import system, name

#Variables Globals
#alumnes és un diccionari que tindrà com a Key el codi de l'alumne, i com a Value al propi alumne
alumnes={}
#materies és un diccionari que tindrà com a Key el codi de la materia i com a value la pròpia matèria
materies={}

#Classes
class Alumne:
    def __init__(self,Codi:str,Nom:str,Cognom:str,DataNaixement:date):
        self.Codi=Codi
        self.Nom=Nom
        self.Cognom=Cognom
        self.DataNaixement=DataNaixement
        #self.Materies és un diccionari que tindrà com a Key el codi de MAtèria, i com a value la nota que ha tret l'alumnes de la matèria
        self.Materies={}
class Materia:
    def __init__(self,Codi:str,Nom:str):
        self.Codi=Codi
        self.Nom=Nom
        #self.Alumnes és una llista que contindrà els alumnes que estan matriculats de cada matèria. Han de ser els alumnes(Clss Alumne), no els codis d'alumnes
        self.Alumnes=[]

#Funcions que heu de programar
def nouAlumne():
    #Ha de demanar les dades d'un alumne, crea-lo i retornar una variable de la classe Alumne
    global alumnes
    global materies
    fiCodi = False
    codi = input("Codi: ")
    while fiCodi == False:
        if codi in alumnes:
            print("Ja tens un alumne amb aquest codi!!")
            codi = input("Codi: ")
        else:
            fiCodi = True
    nom = input("Nom: ")
    cognom = input("Cognom: ")
    dataNaixement = input("Data de naixement: ")
    fiDataNaix = False
    while fiDataNaix == False:
        try:
            dataNaixement = datetime.strptime(dataNaixement, '%d/%m/%Y')
            a = Alumne(codi,nom,cognom,dataNaixement)
            fiDataNaix = True
        except:
            print("ERROR!!! - La data ha de ser DIA/MES/ANY!")
            dataNaixement = input("Data de naixement: ")
    print("Fes ENTER si no vols matricular a l'alumne a cap materia")
    materia = input("Codi Materia: ")
    while materia != "":
        try:
            materies[materia].Alumnes.append(a)
            a.Materies[materia]=None
        except:
            print("ERROR! - No hi ha cap materia amb aquest codi!!")
        print("Fes Enter Per deixar de introduir")
        materia = input("Codi Materia: ")
    return a

def novaMateria():
    #Ídem anterior però amb materia
    codi = input("Codi: ")
    nom = input("Nom: ")
    m = Materia(codi, nom)
    return m

def afegirAlumne(a:Alumne):
    #Afegirà l'alumne a al diccionari alumnes
    global alumnes
    alumnes[a.Codi] = a

def afegirMateria(m:Materia):
    #Afegirà la materia m al diccionari materies
    global materies
    materies[m.Codi] = m

def eliminarAlumne(codiAlumne:str):
    global alumnes
    global materies
    a = alumnes[codiAlumne]
    #Ha de eliminar-lo també de totes les materies que estigui matriculat
    for m in alumnes[codiAlumne].Materies:
        materies[m].Alumnes.remove(a)
    #Elimina del diccionari alumnes, l'alumne que té com a codi codiAlumne
    if codiAlumne == a.Codi:
        del alumnes[codiAlumne]

def eliminarMateria(codiMateria:str):
    global alumnes
    global materies
    m = materies[codiMateria]
    #i també del diccionari a.materies de tots els alumnes que estaven matriculats d'aquella matèria
    for a in materies[codiMateria].Alumnes:
        del alumnes[a.Codi].Materies[m.Codi]
    #Eliminar la materia amb codiMateria del diccionari materies,
    if codiMateria == m.Codi:
        del materies[codiMateria]


def matriculaAlumne(codiAlumne:str,codiMateria:str):
    global alumnes
    global materies
    #agafarà l'alumne a, que té com a codi codiAlumne del dicc alumnes
    a = alumnes[codiAlumne]
    #agafarà la materia m, que té com a codi codiMateria del dicc materies
    m = materies[codiMateria]
    #afegirà el coidiMateria a alumne a, per tant, l'afegirà al diccionai a.Materies, amb value buit, el value serà la nota
    if codiMateria in a.Materies or codiAlumne in m.Alumnes:
        print(f"L'alumne amb codi {codiAlumne} ja esta matriculat a la materia amb codi {codiMateria}")
    else:
        a.Materies[m]=None
        m.Alumnes.append(a)
    #afegirà l'alumne a la materia m, l'afegirà a la llista m.Alumnes
    #Tot l'anterior sempre comprovant que existeixen l'alumne i la materia

def desmatriculaAlumne(codiAlumne:str,codiMateria:str):
    #Ha de fer el contrari que el métode anterior
    global alumnes
    global materies
    a = alumnes[codiAlumne]
    m = materies[codiMateria]
    if codiMateria not in a.Materies and codiAlumne not in m.Alumnes:
        print(f"L'alumne amb codi {codiAlumne} NO esta matriculat a la materia amb codi {codiMateria}")
    else:
        a.Materies.pop(codiMateria)
        m.Alumnes.pop(codiAlumne)
        print("Alumne desmaticulat correctament")

def estaMatriculat(codiAlumne:str,codiMateria:str):
    global alumnes
    global materia
    #retornarà True si l'alumne ja està matriculat de la materia i false sinó està matriculat
    a = alumnes[codiAlumne]
    m = materies[codiMateria]
    if codiAlumne in m.Alumnes or codiMateria in a.Materies:
        return True
    else:
        return False

def posarNota(codiAlumne:str,codiMateria:str,nota:int):
    global alumnes
    global materies
    #Servirà per posar nota a l'alumne a
    a = alumnes[codiAlumne]
    #Comprovarà que l'alumne està matriculat de la materia, i després li possarà nota
    if a.Materies[codiMateria] != None:
        print(f"AVIS - L'alumne amb codi {codiAlumne} ja te una nota asignada a aquesta materia!!")
        actualitzar = input("Vols actualitzar la nota? [SI|NO] ")
        if actualitzar.lower() == "si":
            a.Materies[codiMateria]=nota
        else:
            print("Es mante la nota anterior")

def mostrarAlumnes():
    global alumnes
    print(f"{'Codi':7}{'Nom':10}{'Cognom':12}{'Data de naixement':19}{'Nº de materies':26}\n{'='*62}")
    for a in alumnes:
        print(f"{alumnes[a].Codi:7}{alumnes[a].Nom:10}{alumnes[a].Cognom:12}{alumnes[a].DataNaixement.day:4}/{alumnes[a].DataNaixement.month:<2}/{alumnes[a].DataNaixement.year:<13}{len(alumnes[a].Materies):<26}\n{'-'*62}")

def mostrarMateries():
    global materies
    print(f"{'Codi':7}{'Nom':25}{'Nº d`Alumnes':10}\n{'='*45}")
    for m in materies:
        print(f"{materies[m].Codi:7}{materies[m].Nom:25}{len(materies[m].Alumnes)}\n{'-'*45}")

def mostrarMenu(opcions):
    #Mostrem el menu d'opcions
    for i,opcio in enumerate(opcions):
        print (f"{i+1:2}.{opcio}")

def esperaTecla():
    input("PREM INTRO PER CONTINUAR")

def clear():
    #Netejar pantalla
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#Comprovara si l'alumne existeix
def existeixAlumne(codiAlumne:str):
    global alumnes
    if codiAlumne in alumnes:
        return True
    else:
        return False

#Comprovara si la materia existeix
def existeixMateria(codiMateria:str):
    global materies
    if codiMateria in materies:
        return True
    else:
        return False

def mostrarAlumne(codiAlumne:str):
    global materies
    #Agafem a l'alumne
    a = alumnes[codiAlumne]
    print(f"\n\nDades actuals del alumne:\n{'-'*30}\nCodi: {a.Codi}\nNom: {a.Nom}\nCognom: {a.Cognom}\nData de naixement: {a.DataNaixement.day}/{a.DataNaixement.month}/{a.DataNaixement.year}\n")
    if len(a.Materies) > 0:
        print("Materies: ")
        for m,n in a.Materies.items():
            if n == None:
                n = 0
            print(f"    {m} -- Nota: {n}")
    print(f"{'-'*30}")

def mostrarMateria(codiMateria:str):
    m = materies[codiMateria]
    print(f"\n\nDades actuals de la materia:\n{'-'*28}\nCodi: {m.Codi}\nNom: {m.Nom}\nNº d'Alumnes: {len(m.Alumnes)}\n{'-'*28}")

def demanarAlumne():
    #Demanem el codi de l'alumne
    codiAlumne = input("Codi de l'alumne: ")
    #Comprovem que el alumne introduit existeix
    e = existeixAlumne(codiAlumne)
    while e == False:
        print("ERROR! - No hi ha cap alumne amb aquest codi!!")
        codiAlumne = input("Codi de l'alumne: ")
        e = existeixAlumne(codiAlumne)
    return codiAlumne

def demanarMateria():
        #Demanem la materia
        codiMateria = input("Codi Materia: ")
        #Comprovem que la materia existeix
        e = existeixMateria(codiMateria)
        while e == False:
            print("ERROR! - No hi ha cap materia amb aquest codi!!")
            codiMateria = input("Codi Materia: ")
            e = existeixMateria(codiMateria)
        return codiMateria