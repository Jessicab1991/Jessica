# variavel global pode ser requisito para alteração de comportamneto de estruturas
#O que é uma variável global e local?
#variável local Uma variável definida dentro de uma função. 
#Uma variável local só pode ser usada dentro da sua função. variável global
# Variável definida fora de uma função. As variáveis globais podem ser acessadas de qualquer função.

# função while 
from time import sleep

c = 0
while c < 10:
    sleep(2)
    print(c)
    c = c+1




