import random
aposta = int(input("Aposta: "))
llistaCartes=[]
carta = ["1 Oros","2 Oros","3 Oros","4 Oros","5 Oros","6 Oros","7 Oros","Sota Oros","Cavall Oros","Rei Oros","1 Copes","2 Copes","3 Copes","4 Copes","5 Copes","6 Copes","7 Copes","Sota Copes","Cavall Copes","Rei Copes","1 Bastos","2 Bastos","3 Bastos","4 Bastos","5 Bastos","6 Bastos","7 Bastos","Sota Bastos","Cavall Bastos","Rei Bastos","1 Espadas","2 Espadas","3 Espadas","4 Espadas","5 Espadas","6 Espadas","7 Espadas","Sota Espadas","Cavall Espadas","Rei Espadas"]
cartaAleatoria = random.choice(carta)
llistaCartes.append(cartaAleatoria)
i = 0
carta.remove(cartaAleatoria)
a = 0
print(f"\nCARTES QUE TENS: {llistaCartes}\n")
resposta = input("Et plantes? (SI/NO): ")
if cartaAleatoria[0] in ("1","2","3","4","5","6","7"):
    a = a + int(cartaAleatoria[0])
elif cartaAleatoria[0] in ("S","C","R"):
    a = a + 0.5
while resposta.upper() != "SI" and a <= 7.5:
    cartaAleatoria = random.choice(carta)
    carta.remove(cartaAleatoria)
    i = i + 1
    if resposta.upper() == "NO":
        llistaCartes.append(cartaAleatoria)
        if cartaAleatoria[0] in ("1","2","3","4","5","6","7"):
            a = a + int(cartaAleatoria[0])
        else:
            a = a + 0.5
    print(f"\nCARTES QUE TENS: {llistaCartes}\n")
    if a < 7.5:
        resposta = input("Et plantes? (SI/NO): ")
if resposta.upper() == "SI":
    print("EL JUGADOR ES PLANTA!!")
elif a == 7.5:
    print(f"Has Guanyat {aposta * 2}€")
elif a > 7.5:
    print("Has perdut!!!")
