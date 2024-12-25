"""

20. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e 
retorna o somatório desse valor.

"""

def somatorio(n):
    return sum(range(1, n+1))

# Teste
assert somatorio(5) == 15
assert somatorio(10) == 55
assert somatorio(1) == 1
print("Todos os testes passaram!")