#Exercicis simples 2 Exercici 4
preu = int(input("Quin es el preu? "))
diners = int(input("Quants diners em dones? "))
canvi = (preu - diners)*-1

c100 = canvi%100
c50 = c100%50
c20 = c50%20
c10 = c20%10
c5 = c10%5

m100 = canvi//100
m50 = c100//50
m20 = c50//20
m10 = c20//10
m5 = c10//5

print (f"Canvi original: {canvi} \nCanvi: \n Monedes de 100:{m100:20}\n Monedes de  50:{m50:20}\n Monedes de  20:{m20:20}\n Monedes de  10:{m10:20}\n Monedes de   5:{m5:20}\n")
