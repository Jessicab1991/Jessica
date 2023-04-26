#estrutura de decisão

chopp = int(input("escreva quantos chopp voce tomou >>"))

if chopp < 5 :
    print("voce tomou menos que 5 chop")

elif chopp == 5 :
    print("voce tomou 5 chopp")

elif chopp > 5 :
    print("voce tomou mais que 5 chopps ja esta muito faceiro")
    multa = float(chopp * 100)
    print("voce ira pagar uma multa de R$ {:.2f}".format(multa))

else:
    print("erro")

    #para expressar as casa decimais usar  ex : {:.2f}  F de (float) (quantidade de casas decimais)
    #bloco de estrutura de condição

    
