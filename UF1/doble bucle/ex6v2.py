#Lectura de dades
dades=[]
dada = input("Dades: ")
while dada:
    dades.append(dada)
    dada = input("Dades: ")

#Mostrem resultats
print(f"{'Alumne':10}{'Mitjana':>10}{'Aval.':>10}{'Suspeses':>10}{'%Suspeses':>10}")
print("-"*50)
for dada in dades:
    alumne=dada.split(",")
    nom = alumne[0]
    notes = alumne[1:]
    sumaNotes=0
    suspeses=0
    for nota in notes:
        sumaNotes+=int(nota)
        if int(nota)<5:
            suspeses+=1
    avaluades = len(notes)
    mitjana = sumaNotes/avaluades
    perSuspeses=suspeses/avaluades
    print(f"{nom:10}{mitjana:10.1f}{avaluades:10}{suspeses:10}{perSuspeses:10.0%}")