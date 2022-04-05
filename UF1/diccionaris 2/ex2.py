#Diccionari on la K es el producte i el value es la quantitat de productes que comprarem
carreto = {}
pagar= input("Vols passar per caixa? (S/N)")
while pagar.lower() == "n":
    producte = input("Producte: ")
    quantitat = int(input("Quantitat: "))
    #Afegim el producte al Carretó o sumem la quantitat
    if producte in carreto:
        if carreto[producte] == quantitat * -1:
            carreto.pop(producte)
        elif carreto[producte] > quantitat * -1:
                carreto[producte] = carreto[producte] + quantitat
        else:
            print("La quantitat que es vol restar es superior a la quantitat existent!!")
    elif quantitat > 0:
        carreto[producte] = quantitat
    else:
        print("Producte no introduit previament!!")
    pagar= input("Vols passar per caixa? (S/N)")
print(f"\n{'Producte':20}|{'Quantitat':20}")
print(f"{'-'*20}{'|'}{'-'*20}")
for producte,quantitat in carreto.items():
    print(f"{producte:20}|{quantitat:20}")