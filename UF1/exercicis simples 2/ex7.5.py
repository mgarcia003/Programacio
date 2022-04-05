#Ex7.5
seg = int(input("Quin es el segon? "))

horas = (seg//3600)
rh = (seg%3600)
minut = (rh//60)
segon = (rh%60)
resultat = (f"{horas}:{minut}:{segon}")

print (resultat)
