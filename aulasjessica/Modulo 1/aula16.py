import random 
#array é agrumamento de dados
# a lista é um agrupamento de dados
#conceito de importação otimizada

n1 = str(input("digite um nome >>"))
n2 = str(input("digite um nome >>"))
n3 = str(input("digite um nome >>"))
n4 = str(input("digite um nome >>"))

lista = [n1, n2, n3, n4]
sorteio = random.choice(lista)


print(sorteio)
