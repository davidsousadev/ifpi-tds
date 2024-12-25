"""

19.  Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e 
retorna o número de divisores desse valor. 

"""

def numero_divisores(n):
    return sum(1 for i in range(1, n+1) if n % i == 0)

# Teste
assert numero_divisores(6) == 4
assert numero_divisores(12) == 6
assert numero_divisores(7) == 2
print("Todos os testes passaram!")