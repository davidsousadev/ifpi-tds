"""

9.  Faça uma função que recebe um  valor inteiro e verifica se o valor é par ou 
ímpar. A função deve retornar um valor booleano.

"""

def par_ou_impar(valor):
    if type(valor) != int and type(valor) != float:
        return Exception
    return valor % 2 == 0

# Teste
assert par_ou_impar(4) == True
assert par_ou_impar(7) == False
assert par_ou_impar(0) == True
assert par_ou_impar(-50) == True

assert par_ou_impar("") == Exception
assert par_ou_impar([]) == Exception
assert par_ou_impar(True) == Exception
assert par_ou_impar(None) == Exception
print("Todos os testes passaram!")