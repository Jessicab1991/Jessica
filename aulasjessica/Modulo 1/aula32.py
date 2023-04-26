#calculo matematico usando a função range

numero = int(input("digite um numero referente a tabuada que deseja saber >>"))

for tabuada in range(1, 11):
    print("{}x{}={}". format(numero, tabuada, numero*tabuada))
