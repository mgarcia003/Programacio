import random
random.seed()

n1 = int(input("Escriu un numero del 1 al 10: "))
n2 = random.randint(1,10)
i = 1

while n1 != n2:
    if n1 > n2:
        print("Incorrecte!!, PISTA: El numero mes petit.")
    else:
        print("Incorrecte!!, PISTA: El numero mes gran.")
    n1 = int(input("Escriu un numero del 1 al 10: "))
    


    i = i + 1

print(f"Correcte! El numero era {n2}, i l'has encertat en {i} intents!")
