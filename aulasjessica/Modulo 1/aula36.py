
#quando usar o .capitalize sempre tem que iniciar com a letra maiscula 


cond = "Sim"

while cond.capitalize() == "Sim":
   var = int(input("digite um numero qualquer para teste >>> "))
   print(f"numero qualquer sendo impresso{var}")
   
   cond = input("voce deseja continuar \nsim \nnão \n >>>") 

   
   
print("fora do while")



