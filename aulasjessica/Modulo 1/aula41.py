salario1 = float(input("digite o primeiro salario >> "))
salario2 = float(input("digite o  segundo salario >> "))
salario3 = float(input("digite o  terceiro salario >> "))
salario4 = float(input("digite o  quarto  salario >> "))

soma  = (salario1 + salario2 + salario3 + salario4)


print( "="*20, "calculadora" , "="*20)


print('''\no primeiro salario digitado foi {} 
\no segundo salario digitado foi {}
\no terceiro salario digitado foi {}
\no quarto salario digitado foi {}
\n {}
''' .format(salario1, salario2, salario3 ,salario4, soma))


print("a soma do salario é :" , soma)





