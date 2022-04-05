MarquesCotxe = ["Seat", "Renault", "Volkswaguen", "Citroën", "Opel", "Peugeot", "Fiat", "BMW", "Mercedes", "Škoda", "Mini", "Smart", "Alfa Romeo", "Lancia", "Kia", "Hiundai", "Dacia", "Toyota", "Honda", "Misubishi", "Jeep", "Tesla"]



for paraula in MarquesCotxe:
    for i in paraula:
        if i == "o" or i == "O":
            print(paraula)