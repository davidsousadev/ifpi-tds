"""

3.  Faça  uma  função  que  recebe  por  parâmetro  um  valor  inteiro  e  positivo  e 
retorna  o  valor  lógico  Verdadeiro  caso  o  valor  seja  primo  e  Falso  em  caso 
contrário.

"""

import math

def numero_primo(num):
    if type(num) != int:
        return Exception
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Teste
assert numero_primo(2) == True
assert numero_primo(4) == False
assert numero_primo(17) == True

assert numero_primo("") == Exception
assert numero_primo() == Exception
print("Todos os testes passaram!")