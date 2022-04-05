#Exercici 1 Formats

num1 = float(input("Primer número: "))
num2 = float(input("Segon número: "))

print(f"Format amb 2 decimals: {num1:.2f} i {num2:.2f}")
print(f"Format amd 0 decimals i agrupant milers: {num1:,.0f} i {num2:,.0f}\n")
print(f"Números ordenats")
print("-"*26)
if num1 > num2:
    print(f"Més petit: {num2:>15.3f}")
    print(f"Més gran: {num1:>15.3f}")

elif num1 < num2:
    print(f"Més petit: {num1:>15.3f}")
    print(f"Més gran: {num2:>15.3f}")
