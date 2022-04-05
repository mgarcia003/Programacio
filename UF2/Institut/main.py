from institut import *
from omplir import *
import re

opcions=["Afegir alumne","Afegir materia","Matricular alumne","Mostrar alumnes","Mostrar alumne","Mostrar materies","Mostrar materia","Comprovar matricula","Posar nota","Desmatricular alumne","Eliminar Alumne","Eliminar Materia","Sortir"]

fi = False

while not fi:
    clear()
    mostrarMenu(opcions)
    opcio = (input("Opcio: "))
    if opcio == "1":
        a = nouAlumne()
        afegirAlumne(a)
        esperaTecla()

    elif opcio == "2":
        m = novaMateria()
        afegirMateria(m)
        esperaTecla()

    elif opcio == "3":
        codiAlumne = demanarAlumne()
        codiMateria = demanarMateria()
        matriculaAlumne(codiAlumne,codiMateria)
        esperaTecla()

    elif opcio == "4":
        mostrarAlumnes()
        esperaTecla()

    elif opcio == "5":
        codiAlumne = demanarAlumne()
        mostrarAlumne(codiAlumne)
        esperaTecla()

    elif opcio == "6":
        mostrarMateries()
        esperaTecla()

    elif opcio == "7":
        codiMateria = demanarMateria()
        mostrarMateria(codiMateria)
        esperaTecla()

    elif opcio == "8":
        codiAlumne = demanarAlumne()
        codiMateria = demanarMateria()
        comprova = estaMatriculat(codiAlumne, codiMateria)
        if comprova == True:
            print(f"L'alumne amb codi {codiAlumne} esta matriculat a la materia amb codi {codiMateria}")
        else:
            print(f"L'alumne amb codi {codiAlumne} NO esta matriculat a la materia amb codi {codiMateria}")
        esperaTecla()

    elif opcio == "9":
        codiAlumne = demanarAlumne()
        codiMateria = demanarMateria()
        #Comprovem que l'alumne que ens han introduit esta matriculat a la materia que ens han introduit
        if estaMatriculat(codiAlumne,codiMateria) == True:
            #Definim el patro per la nota
            patroNota="^[0-10]*$"
            #Demanem la nota
            nota = input("Quina nota vols posar? [0-10]")
            #Comprovem que la nota introduida es correcte
            while re.search(patroNota,nota) == False:
                print("ERROR! - La nota ha de ser un numero entre 0 i 10!!")
                nota = input("Quina nota vols posar? [0-10]  ")
            nota = int(nota)
            posarNota(codiAlumne,codiMateria,nota)
        else:
            print("ERROR! - L'alumne no esta matriculat a la materia indicada!!")
        esperaTecla()

    elif opcio == "10":
        codiAlumne = demanarAlumne()
        codiMateria = demanarMateria()
        desmatriculaAlumne(codiAlumne, codiMateria)
        esperaTecla()

    elif opcio == "11":
        codiAlumne = demanarAlumne()
        eliminarAlumne(codiAlumne)
        esperaTecla()

    elif opcio == "12":
        codiMateria = demanarMateria()
        eliminarMateria(codiMateria)
        esperaTecla()

    else:
        fi = True
