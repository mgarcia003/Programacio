from institut import *
#Crear alumnes
a1 = Alumne("A1","Pep","Garcia",date(2000,10,5))
a2 = Alumne("A2","Marta","Perez",date(2002,5,1))
a3 = Alumne("A3","Marc","Lopez",date(2003,10,10))
a4 = Alumne("A4","Pere","Pi",date(2005,12,1))
a5 = Alumne("A5","Maria","Blanco",date(2001,7,17))

#Crear materies
m1 = Materia("M1","Sistemas")
m2 = Materia("M2","Bases de dades")
m3 = Materia("M3","Llenguatge de Marques")
m4 = Materia("M4","Programació")
m5 = Materia("M5","Xarxes")
#...

#Matricular
a1.Materies["M1"]=None
m1.Alumnes.append(a1)

a1.Materies["M2"]=None
m2.Alumnes.append(a1)

a2.Materies["M1"]=None
m1.Alumnes.append(a2)

a2.Materies["M2"]=None
m2.Alumnes.append(a2)

a3.Materies["M3"]=None
m3.Alumnes.append(a3)

#Posar nota
a1.Materies["M1"]=3
a2.Materies["M1"]=7

alumnes["A1"]=a1
alumnes["A2"]=a2
alumnes["A3"]=a3
alumnes["A4"]=a4
alumnes["A5"]=a5

materies["M1"]=m1
materies["M2"]=m2
materies["M3"]=m3
materies["M4"]=m4
materies["M5"]=m5
