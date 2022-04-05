import random
random.seed()

n1 = int(input("Escriu un numero del 1 al 10: "))
n2 = random.randint(1,10)
i = 0

while n1 != n2 and i <= 11:
    print("Incorrecte!!")
    n1 = int(input("Escriu un numero del 1 al 10: "))
    i = i + 1

print(f"Correcte! El numero era {n2}.")
