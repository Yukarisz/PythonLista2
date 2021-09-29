import random
listaA=[]
listaB=[]
listaC=[]
for k in range (5):
    num1=random.randint(1,50)
    num2=random.randint(1,50)
    listaA.append(num1)
    listaB.append(num2)
    listaC.append(num1)
    listaC.append(num2)

for i in listaA:
    for j in listaB:
        if(i==j):
            listaC.remove(i)
            listaC.remove(j)

print(listaA)
print(listaB)
print(listaC)