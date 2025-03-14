"""

19.  Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor. 

"""

def numero_divisores(n):
    if type(n) != int or n <= 0:
        return Exception
    return sum(1 for i in range(1, n+1) if n % i == 0)

# Teste
assert numero_divisores(6) == 4
assert numero_divisores(12) == 6
assert numero_divisores(7) == 2

assert numero_divisores(0) == Exception
assert numero_divisores(-1) == Exception
assert numero_divisores('7') == Exception
assert numero_divisores([7]) == Exception
assert numero_divisores(True) == Exception
assert numero_divisores(None) == Exception

print("Todos os testes passaram!")