#Ex3

edat = int(input("Edat: "))

if edat==18:
    print(f"T'acabes d'estrenar en la majoria d'edat")
    
elif edat<=18:
    edat = 18 - edat
    if edat == 1:
        print(f"Et falta {edat} any per ser major d'edat")
    else:
        print(f"Et falten {edat} anys per ser major d'edat")
    
elif edat>=18:
    edat = edat - 18
    if edat == 1:
        print(f"Fa {edat} any que ets major d'edat")
    else:
        print(f"Fa {edat} anys que ets major d'edat")

