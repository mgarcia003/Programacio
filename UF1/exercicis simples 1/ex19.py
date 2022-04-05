#Exercici 19

numero= int(input("Numero de 3 xifres: "))

primer= numero // 10
segon= numero % 10
n1 = primer % 10
n2 = primer // 10

print (segon,n1,n2,sep="")
