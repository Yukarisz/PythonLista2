import random
listaA=[]
listaB=[]
listaC=[]
for c in range(5):
    listaA.append(random.randint(1, 20))
    listaB.append(random.randint(1, 20))
    listaC.append(listaA[c-1])
    listaC.append(listaB[c-1])
quantidadePerfeito=0
for j in range(len(listaC)):
    soma=0
    for k in range(1, listaC[j]):
        if listaC[j] %k == 0:
            soma+=k
    if soma==listaC[j]:
        quantidadePerfeito+=1
print("Qntd de numeros Perfeitos:  ", quantidadePerfeito)
print(listaA)
print(listaB)
print(listaC)