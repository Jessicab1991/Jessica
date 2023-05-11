from time import sleep

situacao = "reprovado"

while situacao == "reprovado":

### bloco 1
    nome = input("digite o seu nome >>> ")
    sobrenome = input("digite o seu sobrenome >>>")
    idade = int(input("didite a sua idade >>>"))

    lista_notas = []

### bloco 2
    for lista in range(0,2) : 
        nota = float(input("digite a sua nota >>>"))
        lista_notas = [nota]
      
    media = sum(lista_notas) / len(lista_notas)

### bloco 3
    if media < 7:
        situação = "reprovado"
        print(f"infelizmente voce foi {situacao} sua nota foi {media}")

    elif media >= 7:
  
       for c in range(0,10):
        print("*")
        sleep(1)
       situacao = "aprovado"
       print("parabens voce foi {} o mundo é pequeno para você!".format(situacao))

dicionario ={
   "nome": nome,
   "sobrenome": sobrenome,
   "idade": idade,
   "lista_notas": lista_notas,
   "media" : media,
   "situacao": situacao
}

var = input("voce deseja ter um relatorio completo do aluno \nsim \nnão \n >>>> ")
 
if var == "sim" :

 print(f'''{dicionario['nome']} 
  \n{dicionario['sobrenome']} 
  \n{dicionario['idade']}
  \n{dicionario['lista_notas']} 
  \n{dicionario['situacao']}''' )

