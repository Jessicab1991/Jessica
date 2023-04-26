from random import choice

n1 = float(input("digite um numero"))
n2 = float(input("digite um numero"))
n3 = float(input("digite um numero"))
n4 = float(input("digite um numero"))
n5 = float(input("digite um numero"))

lista = [
n1,
n2,
n3,
n4,
n5
]

sorteio = choice(lista)

if sorteio == n1 :
    for c in range(20) :
        print('*')
    print("o numero sorteado foi:", n1)

elif sorteio == n2 :
    for c in range(20) :
        print('*')
    print("o numero sorteado foi:", n2)

elif sorteio == n3 :
    for c in range(20) :
        print('*')
    print("o numero sorteado foi:", n3)

elif sorteio == n4 :
    for c in range(20) :
        print('*')
    print("o numero sorteado foi:", n4)  

elif sorteio == n5 :
    for c in range(20) :
        print('*')
    print("o numero sorteado foi:", n5)

    


