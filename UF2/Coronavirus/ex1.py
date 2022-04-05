from datetime import *
from classes import *
from os import system, name
import re

pacients=[]
opcions=["Afegir pacient nou","Canvi estat pacient","Mostrar Pacients","Edat pacient","Mostrar pacients filtrat per estat","Mostrar pacients filtrat per data","Mostrar pacients filtrat per estat i data","Sortir"]

def clear():
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def mostrarMenu(opcions):
    for i,opcio in enumerate(opcions):
        print (f"{i+1:2}.{opcio}")

def esperaTecla():
    input("PREM INTRO PER CONTINUAR")

def nouPacient():
    patroSexe = "^[HD]$"
    patroEstat = "^(lleu|greu|uci|mort)$"
    patroCodi = "^[0-9]*$"
    fiCodi = False
    codi = input("Codi: ")
    while fiCodi == False:
        if re.search(patroCodi,codi) and codi != "":
            fiCodi = True
        else:
            print("ERROR!!! - El CODI ha de ser un numero!")
            codi = input("Codi: ")
    p = pacient(codi)
    fiSexe = False
    sexe = input("Sexe: (H,D) ")
    while fiSexe == False:
        if re.search(patroSexe,sexe.upper()):
            p.sexe = sexe.upper()
            fiSexe = True
        else:
            print("ERROR!!! - El SEXE ha de ser H o D!")
            sexe = input("Sexe: (H,D) ")
    fiDataNaix = False
    dataNaix = input("Data de naixement (d/m/a) ")
    while fiDataNaix == False:
        try:
            dataNaixOK = datetime.strptime(dataNaix, '%d/%m/%Y')
            p.dataNaixement = dataNaixOK
            fiDataNaix = True
        except:
            print("ERROR!!! - La data ha de ser DIA/MES/ANY!")
            dataNaix = input("Data de naixement (d/m/a) ")
    estat = input("Estat: (Lleu, Greu, UCI, Mort) ")
    fiEstat = False
    while fiEstat == False:
        if re.search(patroEstat,estat.lower()):
            p.estat = estat[0].upper() + estat[1:].lower()
            fiEstat = True
        else:
            print("ERROR!!! - L'estat ha de ser Lleu o Greu o UCI o Mort!")
            estat = input("Estat: (Lleu, Greu, UCI, Mort) ")
    fiIniciContagi = False
    iniciContagi = input("Data inici de contagi (d/m/a): ")
    while fiIniciContagi == False:
        try:
            iniciContagiOK = datetime.strptime(iniciContagi, '%d/%m/%Y')
            p.iniciContagi = iniciContagiOK
            fiIniciContagi = True
        except:
            print("ERROR!!! - La data ha de ser DIA/MES/ANY!")
            iniciContagi = input("Data inici de contagi (d/m/a): ")
    fiFiContagi = False
    fiContagi = input("Data fi de contagi (d/m/a): ")
    while fiFiContagi == False:
        try:
            fiContagiOK = datetime.strptime(fiContagi, '%d/%m/%Y')
            p.fiContagi = fiContagiOK
            fiFiContagi = True
        except:
            print("ERROR!!! - La data ha de ser DIA/MES/ANY!")
            fiContagi = input("Data fi de contagi (d/m/a): ")
    return p

def trobarPacient(pacients,codi):
    for p in pacients:
        if p.Codi == codi:
            return p
        else:
            p = None
            return

def nouEstat(p,estat):
    patroEstat = "^(lleu|greu|uci|mort)$"
    if re.search(patroEstat,estat.lower()):
        p.estat = estat[0].upper() + estat[1:].lower()
    else:
        print(f"No hem pogut guardar l'estat\nRecorda, les opcions per l'estat son:\nLleu, Greu, UCI, Mort")

def mostrarPacients(pacients):
    print(f"{'Codi':7}{'Data de Naixement':20}{'Edat':7}{'Sexe':7}{'Estat':8}{'Inici contagi':16}{'Fi contagi':10}")
    print("="*75)
    for p in pacients:
        print(f"{p.Codi:7} {p.dataNaixement.day:4}/{p.dataNaixement.month:2}/{p.dataNaixement.year:<4} {date.today().year - p.dataNaixement.year:9}     {p.sexe:5} {p.estat:8} {p.iniciContagi.day:2}/{p.iniciContagi.month:2}/{p.iniciContagi.year:<8} {p.fiContagi.day:2}/{p.fiContagi.month:2}/{p.fiContagi.year}\n{'-'*75}")

def mostrarPacientsPerEstat(pacients,estat):
    patroEstat = "^(lleu|greu|uci|mort)$"
    estatPacients = []
    if re.search(patroEstat,estat.lower()):
        for p in pacients:
            patroEstat = "^(lleu|greu|uci|mort)$"
            if re.search(patroEstat,estat.lower()):
                if p.estat == estat:
                    estatPacients.append(p)
    else:
        print(f"No hem pogut filtrar per l'estat\nRecorda, les opcions per l'estat son:\nLleu, Greu, UCI, Mort")
    return estatPacients

def mostrarPacientsPerData(pacients,data:datetime):
    dataPacients = []
    for p in pacients:
        if p.iniciContagi <= data:
            dataPacients.append(p)
    return dataPacients

def afegirPacient(pacients,p):
    pacients.append(p)

def edat(p,data:datetime):
    if data.year >= p.dataNaixement.year:
        return (f"El pacient amb codi {p.Codi} a data {data.day}/{data.month}/{data.year} te {data.year - p.dataNaixement.year} anys")
    else:
        return "La data introduida es inferior a la data de naixement!!"

def mostrarPacientsPerEstatData(pacients,estat,data:datetime):
    dataEstatPacients = []
    patroEstat = "^(lleu|greu|uci|mort)$"
    if re.search(patroEstat,estat.lower()):
        for p in pacients:
            if p.estat == estat and p.iniciContagi <= data:
                dataEstatPacients.append(p)
        return dataEstatPacients
    else:
        print(f"No hem pogut filtrar per l'estat\nRecorda, les opcions per l'estat son:\nLleu, Greu, UCI, Mort")


fi = False

while not fi:
    clear()
    #Mostrem el menu
    mostrarMenu(opcions)
    #Escullir opció
    opcio = (input("Opcio: "))
    if opcio == "1":
        p = nouPacient()
        afegirPacient(pacients,p)
        esperaTecla()
    elif opcio == "2":
        #demanem codi del pacient
        codi = input("Quin es el codi del pacient? ")
        #Busquem el pacient i el guardem
        p = trobarPacient(pacients,codi)
        if p != None:
            #mostrem pacient
            print(f"Dades actuals del pacient:\n{'-'*26}\nCodi: {p.Codi}\nData Naixement: {p.dataNaixement.day}/{p.dataNaixement.month}/{p.dataNaixement.year}\nSexe: {p.sexe}\nEstat: {p.estat}\nInici Contagi: {p.iniciContagi.day}/{p.iniciContagi.month}/{p.iniciContagi.year}\nFi Contagi: {p.fiContagi.day}/{p.fiContagi.month}/{p.fiContagi.year}\n{'-'*26}")
            #Demanem el nou estat
            estat = input("Nou Estat: ")
            #Modifiquem l'estat
            nouEstat(p,estat)
        else:
            print("ERROR!! - No hi ha cap pacient amb aquest codi!")
        esperaTecla()
    elif opcio == "3":
        mostrarPacients(pacients)
        esperaTecla()
    elif opcio == "4":
        codi = input("Quin es el codi del pacient? ")
        p = trobarPacient(pacients,codi)
        if p.Codi != None:
            data = datetime.strptime(input("Quina data? (d/m/a) "), '%d/%m/%Y')
        else:
            print("ERROR!! - No hi ha cap pacient amb aquest codi!")
        print(edat(p,data))
        esperaTecla()
    elif opcio == "5":
        estat = input("Per quin estat vols filtrar? ")
        estat = estat[0].upper() + estat[1:].lower()
        estatPacients = mostrarPacientsPerEstat(pacients,estat)
        if estatPacients != None:
            mostrarPacients(estatPacients)
        else:
            print("ERROR! - No hi ha cap pacient en aquest estat!")
        esperaTecla()
    elif opcio == "6":
        data = datetime.strptime(input("Per quina data vols filtrar? (d/m/a) "), '%d/%m/%Y')
        dataPacients = mostrarPacientsPerData(pacients,data)
        if dataPacients != None:
            mostrarPacients(dataPacients)
        else:
            print("ERROR!! - No hi ha cap pacient en aquesta data o anterior!")
        esperaTecla()
    elif opcio == "7":
        estat = input("Per quin estat vols filtrar? ")
        estat = estat[0].upper() + estat[1:].lower()
        data = datetime.strptime(input("Per quina data vols filtrar? (d/m/a) "), '%d/%m/%Y')
        dataEstatPacients = mostrarPacientsPerEstatData(pacients,estat,data)
        if dataEstatPacients != None:
            mostrarPacients(dataEstatPacients)
        else:
            print("ERROR! - No hi ha cap pacient en aquesta data i aquest estat!")
        esperaTecla()
    else:
        fi = True