n1 = float(input("digite a primeira nota >> "))
n2 = float(input("digite a segunda nota>> "))

media = (n1 + n2) /2



if media  < 7 :
    print("o aluno tirou menos que 7")
    print("o aluno tirou menos que 5 tem que prestar mais ateção na aula")

elif media == 7 :
    print("o aluno tirou igual a 7")

elif media > 7 :
    print("parabens o aluno passou de ano")

    

else:
    print("erro")