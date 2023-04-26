#o dicionario é dada a condição a partir de {}
#variavel recebendo um dicionario difinido pela simbologia{}
#o que é um dicionario? é a condição de agrupamneto de caracteristicas de um individo
#\n   quebra de linha
#f antes da estring chama  interpolação de instrings

nome = input("digite seu nome >> ")

cor = input("digite a sua cor >> ")

sexo = input("digite o seu sexo >> ")

tamanho = input("digite o seu tamanho >> ")

peso = input("digite o seu peso >> ")

nacionalidade = input("digite onde voce nasceu >> ")

idioma = input("digite seu idioma principal >> ")

pessoa = {
    "nome": nome,
    "cor": cor,
    "sexo": sexo,
    "tamanho": tamanho,
    "peso": peso,
    "nacionalidade": nacionalidade,
    "idioma": idioma
}

cond = int(input('''digite o numero que representa a carcteristica que deseja saber
\n1-nome
\n2-cor
\n3-sexo
\n4-tamanho
\n5-peso
\n6-pais
\n7-idioma
>>>>>>'''))

if cond == 1:
    print(f"o nome que voce deseja saber é{pessoa['nome']}")

elif cond == 2:
    print(f"a cor que voce deseja saber é{pessoa['cor']}")
 
elif cond == 3:
    print(f"o sexo que voce deseja saber é{pessoa['sexo']}")

elif cond == 4:
    print(f"a altura que voce deseja saber é{pessoa['tamanho']}")

elif cond == 5:
    print(f"o peso que voce deseja saber é{pessoa['peso']}") 

elif cond == 6:
    print(f"o pais que voce deseja saber é{pessoa['pais']}") 

elif cond == 7:
    print(f"o idioma que voce deseja saber é{pessoa['idioma']}") 

elif cond == 8:
    print(pessoa)
    

