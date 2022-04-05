#Exercici 2 Càlcul IMC

nom = input("Introdueix el teu nom: ")
alçada = float(input("Introdueix la teva alçada: "))
pes = float(input("Introdueix el teu pes: "))

imc = pes / (alçada * alçada)

print(f"Hola {nom} el teu índex de massa corporal és {imc:.2f}")
