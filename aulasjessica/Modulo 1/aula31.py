#função sleep dalei ,conta os segundos pra cada numero
#importação otimizada
from time import sleep


inicio = int(input("digite o numero de inicio >>>"))
fim = int(input("digite o numero de fim >>>"))
passo = int(input("digite o numero de passo >>>"))

for cronometro in range(inicio, fim, -passo) :
    sleep(2)
    print(cronometro)
    