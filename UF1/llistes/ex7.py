MarquesCotxe = ["Seat", "Renault", "Volkswaguen", "Citroën", "Opel", "Peugeot", "Fiat", "BMW", "Mercedes", "Škoda", "Mini", "Smart", "Alfa Romeo", "Lancia", "Kia", "Hiundai", "Dacia", "Toyota", "Honda", "Misubishi", "Jeep", "Tesla"]
l = len(MarquesCotxe)
p = l // 2
i = p - 1
if len(MarquesCotxe) % 2 == 0:
    print (MarquesCotxe[p])
elif len(MarquesCotxe) % 2 != 0:
    print (f"{MarquesCotxe[p]} {MarquesCotxe[i]}")