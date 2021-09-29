import random
livend=[]
listaVenda=[]
comiss=[]
for i  in range(5):
    vend=str(input("Qual e o nome do vendedor:"))
    venda=random.randint(300,30000)
    comissao = venda * 0.1

    livend.append(vend)
    listaVenda.append(venda)
    comiss.append(comissao)
medvenda=sum(listaVenda)/len(listaVenda)

mais=0
for k in range(5):
    if listaVenda[k-1]<medvenda:
        mais += 1

local=listaVenda.index(max(listaVenda))

for j in range(5):
    print(" O vendedor {}, ganhou um total de R${}".format(livend[j-1],listaVenda[j-1]))
print("O total vendido pelos 5 é de R${}".format(sum(listaVenda)))
print("A média de vendas é de R${}".format(medvenda))
print("{} vendedores venderam mais que a média".format(mais))
print("{} teve maior valor de comissão de R${}".format(livend[local],listaVenda[local]))