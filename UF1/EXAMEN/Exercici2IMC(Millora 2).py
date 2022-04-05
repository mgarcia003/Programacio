#Exercici 2 Càlcul IMC

nom = input("Introdueix el teu nom: ")
alçada = float(input("Introdueix la teva alçada: "))
pes = float(input("Introdueix el teu pes: "))

imc = pes / (alçada * alçada)

if imc <= 15:
    print(f"Hola {nom} el teu índex de massa corporal és {imc:.2f}\nTens primesa molt severa")
elif imc > 15 and imc < 16:
    print(f"Hola {nom} el teu índex de massa corporal és {imc:.2f}\nTens primesa severa")
elif imc > 16 and imc < 18.5:
    print(f"Hola {nom} el teu índex de massa corporal és {imc:.2f}\nTens primesa")
elif imc > 18.5 and imc < 25:
    print(f"Hola {nom} el teu índex de massa corporal és {imc:.2f}\nTens pes saludable")
elif imc > 25 and imc < 30:
    print(f"Hola {nom} el teu índex de massa corporal és {imc:.2f}\nTens sobrepès")
elif imc > 30 and imc < 35:
    print(f"Hola {nom} el teu índex de massa corporal és {imc:.2f}\nTens obesitat moderada")
elif imc > 34 and imc < 40:
    print(f"Hola {nom} el teu índex de massa corporal és {imc:.2f}\nTens obesitat severa")
elif imc >= 40:
    print(f"Hola {nom} el teu índex de massa corporal és {imc:.2f}\nTens obesitat mòrbida")
