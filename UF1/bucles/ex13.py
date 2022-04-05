import random
random.seed()
c = random.randint(1,10)
i = 0
while i <= c:
    if i % 2 != 0:
        print("*"*i)
    else:
        print("+"*i)
    i = i + 1
