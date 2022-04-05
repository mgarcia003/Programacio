paraula = input("Paraula: ")
c = 0
i = 0

while c <= len(paraula) -1:
    if paraula[c] == "a":
        i = i + 1       

    c = c + 1

if i == 4:
    print("La paraula te les 4 vocals")
elif i >= 5:
    print("La paraula te mes de 4 as")
elif i <= 3:
    print("La paraula te menos de 4 as")
    
