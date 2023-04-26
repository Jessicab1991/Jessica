n1 = int(input("digite um numero >>"))
#o simbolo da % no pyton não representa porcentagem e sim resto da divisão 
resultado = n1 % 2

print("O resultado é {}".format(resultado))


if resultado  == 0 :
    print("o numero é par")

elif resultado == 1 :
    print("o numero é impar")


   # o if e elif funcionam sem o else perfeitamente
   