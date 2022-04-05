edat = int(input("Introdueix la teva edat: "))
nom = input("Introdueix la teva edat: ")
grup = input("A quin grup vas? ")
#amb str.format
#missatge = "Hola {0} tens {1} i vas al grup {2}".format(nom,edat,grup)
missatge = f"Hola {nom} tens {edat} i vas al grup {grup}"
print (missatge)
