import random
random.seed()
c = random.randint(1,10)
b = 0
for i in range(1,c):
    if b % 2 != 0:
        print("*"*b)
    else:
        print("+"*b)
    b = b + 1
