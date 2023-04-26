#importação otimizada
from random import choice

nome1 = input("digite seu nome >>>")
nome2 = input("digite seu nome >>>")
nome3 = input("digite seu nome >>>")
nome4 = input("digite seu nome >>>")

#o que é uma lista é a condição de agrupamento
#variavel recebendo uma lista definida pela simbologia []
lista = [   nome1,
            nome2,
            nome3,
            nome4,
         
         
          ]

sorteado = choice(lista)

#print iltilizando polimorfismo e quebra (utilizado um )
print( "="*20, "nome sorteado" , "="*20)

if sorteado == nome1 :
    print("o nome sorteado foi o primeiro digitado")
    print(f"o nome sorteado foi{sorteado}")
elif sorteado == nome2 :
    print("o nome sorteado foi o segundo digitado")
    print(f"o nome sorteado foi{sorteado}")
elif sorteado == nome2 :
    print("o nome sorteado foi o terceiro digitado")
    print(f"o nome sorteado foi{sorteado}")
elif sorteado == nome2 :
    print("o nome sorteado foi o quarto digitado")
    print(f"o nome sorteado foi{sorteado}")
else:
    print("erro")
