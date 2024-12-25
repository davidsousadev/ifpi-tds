"""

25.  Escreva uma função que recebe, por parâmetro um valor inteiro e retorna o 
seu fatorial.

"""

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

# Teste
assert fatorial(5) == 120
assert fatorial(3) == 6
assert fatorial(0) == 1
print("Todos os testes passaram!")