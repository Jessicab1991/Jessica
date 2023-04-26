nome = input("digite seu nome>>>>")
sobrenome = input("digite seu sobrenome")
idade = input("digite sua idade")

#Aqui estamos ultilizando uma derivação da interpolacao de string
#Chamada mascara de substituicao pois as variaveis vao dentro da funcao
print("O nome digitado foi {} \no sobrenome é {} \na idade é {}".format(nome, sobrenome, idade))