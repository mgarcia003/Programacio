#Ex2

edat = int(input("Edat: "))

if edat==18:
    print(f"T'acabes d'estrenar en la majoria d'edat")
    
elif edat<=18:
    edat = 18 - edat 
    print(f"Et falten {edat} anys per ser major d'edat")
    
elif edat>=18:
    edat = edat - 18
    print(f"Fa {edat} anys que ets major d'edat")
