n1 = int(input("Primer numero: "))
n2 = int(input("Segon numero: "))
print(f"Els numeros que hi han del {n1} al {n2} son:")
if n1 < n2:
    for i in range(n1,n2 + 1):
        print(i)
else:
    for i in range(n1,n2 - 1,-1):
        print(i)