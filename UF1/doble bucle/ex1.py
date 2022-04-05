l = [123,458,761,23,44]
p = 0
im = 0
for i in l:
    if i % 2 == 0:
        p = p + 1
    else:
        im = im + 1
print(f"Hi han {p} numeros parells i {im} numeros senars")