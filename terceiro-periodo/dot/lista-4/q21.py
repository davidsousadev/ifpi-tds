"""

21.  Escreva uma função que recebe por parâmetro um valor inteiro e positivo N 
e retorna o valor de S. 
S = 1 + ½ + 1/3 + ¼ + 1/5 + 1/N.

"""

def soma_frações(n):
    return sum(1/i for i in range(1, n+1))

# Teste
assert soma_frações(3) == 1 + 1/2 + 1/3
assert soma_frações(5) == 1 + 1/2 + 1/3 + 1/4 + 1/5
assert soma_frações(1) == 1
print("Todos os testes passaram!")