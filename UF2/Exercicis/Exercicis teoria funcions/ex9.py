def majorLlista(l):
    i = 0
    n1 = l[i]
    while len(l) > i:
        n2 = l[i]
        if n2 > n1:
            n1 = n2
        i += 1
    return n1

l = [1,2,3,4,5,6]
print(majorLlista(l))