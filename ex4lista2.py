import random
listaA = []
listaB = []
listaC = []
for i in range(10) :
    n1 = random.randint(1, 50)
    n2 = random.randint(1, 50)

    listaA.append(n1)
    listaB.append(n2)

for c in listaA:
    for k in listaB:
        if(c==k):
            listaC.append(c)

print("Lista A",listaA)
print("Lista B",listaB)
print("Lista C",listaC)