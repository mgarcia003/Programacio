#Ex19

año = int(input("Quin any es: "))
a = año % 400
e = año % 4
u = año % 100
if a == 0:
    print("Es any de traspas")
elif e == 0 and u != 0:
    print("Es any de traspas")
else:
    print("No es any de traspas")
