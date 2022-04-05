#Exercici 2 Càlcul IMC

nom = input("Introdueix el teu nom: ")
alçada = float(input("Introdueix la teva alçada: "))
pes = float(input("Introdueix el teu pes: "))

imc = pes / (alçada * alçada)

if imc >= 25:
    print(f"Hola {nom} el teu índex de massa corporal és {imc:.2f}\nVigila! Segurament tinguis sobrepés")
elif imc <=18.5:
    print(f"Hola {nom} el teu índex de massa corporal és {imc:.2f}\nVigila! Segurament hagis de menjar més")
else:
    print(f"Hola {nom} el teu índex de massa corporal és {imc:.2f}\nEl teu pes entra dintre del que es considera normal")
