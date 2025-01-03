"""

23.  Escreva uma função que recebe por parâmetro um valor inteiro e positivo N 
e retorna o valor de S. 
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(n2+1)/(n+3) 

"""

def soma_complexa(n):
    return sum((i**2 + 1)/(i+3) for i in range(2, n+2))

# Teste
assert soma_complexa(3) == (2**2 + 1)/(2+3) + (3**2 + 1)/(3+3) + (4**2 + 1)/(4+3)
assert soma_complexa(5) == sum((i**2 + 1)/(i+3) for i in range(2, 7))
print("Todos os testes passaram!")