listacor=[]
for i in range(4):
    cor=str(input("Escreva para receber uma cor:"))
    listacor.append(cor)

pesq=str(input("Digite a cor para ser pesquisada"))
for j in range (4):
    if pesq == listacor[j-1]:
        print(listacor)
        print("A cor {} está localizada no {}° elemento da lista.".format(pesq,j))
    else:
        print("Essa cor não está na lista.")
