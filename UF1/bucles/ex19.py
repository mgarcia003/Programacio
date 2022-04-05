import random
random.seed()

n1 = random.randint(1,100)
n2 = int(input("Escriu un numero de 1 a 100: "))
vides = 5

while n1 != n2 and vides >= 1:
    if n1 > n2:
        print("INCORRECTE! El numero inventat es mes gran!!")
    elif n1 < n2: 
        print("INCORRECTE! El numero inventat es mes petit!!")
    vides = vides - 1
    print(f"Et queden {vides + 1} vides")
    print("-"*20)
    n2 = int(input("Escriu un numero de 1 a 100: "))
    

if n1 != n2:
    print ("INCORRECTE!!")
    print ("T'has quedat sense vides!")
    print (f"El numero correcte es {n1}")

else:
    print (f"Correcte! El numero correcte era {n1}")
