import random
def aleatoris(n):
    i = 0
    l = []
    while i < n:
        l.append(random.randint(1,100))
        i += 1
    return l

print(aleatoris(3))