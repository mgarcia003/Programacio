nom = input("Nom: ")
ts = int(input("Tensió Sistòlica: "))
td = int(input("Tensió Diastòlica: "))

while nom != "" and ts != "" and td != "":
    if ts < 80 or td < 60:
        print(f"{nom}, tens nivell de tensió: Hipotensió")
    elif (ts >= 80 and ts <= 119) and (td >= 60 and td <= 79):
        print(f"{nom}, tens el nivell de tensió: Normal")
    elif (ts >= 120 and ts <= 139) or (td >= 80 and td <= 89):
        print(f"{nom}, tens el nivell de tensió: Prehipertensió")
    elif (ts >= 140 and ts <= 159) or (td >= 90 and td <= 99):
        print(f"{nom}, tens el nivell de tensió: Hipertensió Grau 1 (HTA1)")
    elif (ts >= 180) or (td >= 110):
        print(f"{nom}, tens el nivell de tensió: Crisis Hipertensiva")
    elif (ts >= 160) or (td >= 100):
        print(f"{nom}, tens el nivell de tensió: Hipertensió Grau 2 (HTA2)")
    nom = input("Nom: ")
    ts = int(input("Tensió Sistòlica: "))
    td = int(input("Tensió Diastòlica: "))