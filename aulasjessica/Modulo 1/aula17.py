from random import shuffle, choice

n1 = str(input("digite um nome >>"))
n2 = str(input("digite um nome >>"))
n3 = str(input("digite um nome >>"))
n4 = str(input("digite um nome >>"))

lista = [n1, n2, n3, n4]
print(lista)

shuffle(lista)
print(lista)
sorteio = choice(lista)
print(sorteio)


#o modo shuffle embaralha os nomes
#choice sorteia

