from contactes import *
from datetime import date,datetime
from os import system, name
import re

def clear():
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def mostrarMenu(opcins):
    for i,opcio in enumerate(opcions):
        print (f"{i+1:2}.{opcio}")

def mostrarContactes(contactes):
    print(f"{'Nom':30}{'Telefon':>12}")
    print("="*42)
    for c in contactes:
        print(f"{c.nom:30}{c.telefon:>12}")

def afegirContacte(contactes):
    patroNom = "^[a-zA-ZÀ-ù ]{3,}$"
    patroTelefon = "^\d{9,12}$"
    nom = input("Nom: ")
    telefon = input("Telefon: ")
    dataNaix = input("Data de naixement (d/m/a): ")
    if re.search(patroNom,nom) and re.search(patroTelefon,telefon):
        c = contacte(nom,telefon)
        contactes.append(c)
        try:
            data = datetime.strptime(dataNaix, '%d/%m/%Y')
            c.dataNaixement = data
        except:
            print("Data naixement no afegida")
    else:
        print("No hem pogut afegir el contacte. Dades incorectes")
opcions = ("Mostrar tots","Afegir","Eliminar","Modificar","Buidar tots","Sortir")

def esperaTecla():
    input("PULSA INTRO PER CONTINUAR")

def buidaContactes(contactes):
    contactes.clear()

def eliminarContacte(contactes):
    telefon = input("Telefon que vols eliminar: ")
    for i,c in enumarate(contactes):
        if c.telefon == telefon:
            print(f"Telefon: {c.telefon} \nNom: {c.nom}")
            resposta = input("Segur que vols eliminar-lo? (s/n)")
            if resposta.lower() == "s":
                contactes.pop(i)
                print("Contacte eliminat")
            return
    print("Contacte no trobat")

fi = False
contactes=[]
while not fi:
    clear()
    #Mostrar opcions de menú
    mostrarMenu(opcions)
    #Escullir opció
    opcio = int(input("Opcio: "))
    if opcio == 1:
        mostrarContactes(contactes)
        esperaTecla()
    elif opcio == 2:
        afegirContacte(contactes)
        esperaTecla()
    elif opcio == 3:
        pass
        eliminarContacte(contactes)
    elif opcio == 4:
        pass
        #modificarContacte(contactes)
        esperaTecla()
    elif opcio == 5:
        buidaContactes(contactes)
        esperaTecla()
    elif opcio == 6:
        fi = True