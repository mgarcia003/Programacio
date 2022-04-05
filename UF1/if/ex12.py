#Ex12

dn_dia = int(input("Quin es el teu dia de naixement? "))
dn_mes = int(input("Quin es el teu mes de naixement? "))
dn_any = int(input("Quin es el teu any de naixement? "))

da_dia = int(input("Quin dia es avui? "))
da_mes = int(input("En quin mes estem? "))
da_any = int(input("En quin any estem? "))

if da_any < dn_any:
    print("Error")

elif da_any > dn_any:
    if da_mes > dn_mes:
        print(f"El teu aniversari va ser el {dn_dia}/{dn_mes}/{da_any}")
    elif da_mes < dn_mes:
        print(f"El teu aniversari sera el {dn_dia}/{dn_mes}/{da_any}")
