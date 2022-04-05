#ex1

p1 = input("Introdueix la nova contraseña: ") 
p2 = input("Torna a introduir la contraseña: ")
vides = 3
while p1 != p2 and vides > 0:
    print(f"INCORRECTE Les contraseñas no coincideixen!!\nEt que den {vides} intents")
    print("-"*30)
    p1 = input("Introdueix la nova contraseña: ") 
    p2 = input("Torna a introduir la contraseña: ")
    vides = vides - 1

if p1 == p2:
    print("Canvi de contraseña correcte!")

else:
    print(f"INCORRECTE Les contraseñas no coincideixen!!\nT'has quedat sense intents, has d'esperar 30 minuts per a tornar-ho a intentar!!")
