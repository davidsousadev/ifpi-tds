"""

22.  Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S. 
S = 1 + 1/1! + ½! + 1/3! + 1 /N! 

"""

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def soma_fatorial_inverso(n):
    if type(n) != int or n <= 0:
        return Exception
    
    soma = 1
    for i in range(1, n + 1):
        soma += 1 / fatorial(i)
    
    return round(soma, 2)

# Testes
assert soma_fatorial_inverso(3) == 2.67
assert soma_fatorial_inverso(4) == 2.71
assert soma_fatorial_inverso(1) == 2.0

assert soma_fatorial_inverso(0) == Exception
assert soma_fatorial_inverso(-5) == Exception
assert soma_fatorial_inverso([5]) == Exception
assert soma_fatorial_inverso('5') == Exception
assert soma_fatorial_inverso(True) == Exception
assert soma_fatorial_inverso(None) == Exception

print("Todos os testes passaram!")