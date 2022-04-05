MarquesCotxe = ["Seat", "Renault", "Volkswaguen", "Citroën", "Opel", "Peugeot", "Fiat", "BMW", "Mercedes", "Škoda", "Mini", "Smart", "Alfa Romeo", "Lancia", "Kia", "Hiundai", "Dacia", "Toyota", "Honda", "Misubishi", "Jeep", "Tesla"]
vocals=[]

for paraula in MarquesCotxe:
    for i in paraula.lower():
        if i == "a" and i not in vocals:
            vocals.append(i)
        if i == "e" and i not in vocals:
            vocals.append(i)
        if i == "i" and i not in vocals:
            vocals.append(i)
        if i == "o" and i not in vocals:
            vocals.append(i)
        if i == "u" and i not in vocals:
            vocals.append(i)
    if len(vocals) >= 3:
        print(paraula)
    vocals=[]