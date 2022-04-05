llista=[1,34,2,56,123,36,2345,456,8,9,45,33,12,567,23,123,9876]
i = 0
una = 0
dos = 0
tres = 0
g = "-" * 21
while i < len(llista):
    if len(str(llista[i])) == 1:
        una = una + 1
    elif len(str(llista[i])) == 2:
        dos = dos + 1
    elif len(str(llista[i])) >= 3:
        tres = tres + 1
    i = i + 1
print(f"Xifres      Quantitat\n{g}\n1{una:>20}\n2{dos:>20}\n3 o més{tres:>14}")