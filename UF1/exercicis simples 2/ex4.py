#Exercicis simples 2 Exercici 4
preu = int(input("Quin es el preu? "))
diners = int(input("Quants diners em dones? "))
canvi = diners - preu
canvir = (preu%5) + canvi
print (f"Canvi original: {canvi} \nCanvi real: {canvir}")
