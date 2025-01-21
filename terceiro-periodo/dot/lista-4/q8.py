"""

8.  Faça uma função que recebe um valor inteiro e verifica se o valor é positivo 
ou negativo. A função deve retornar um valor booleano

"""

def positivo_ou_negativo(valor):
    if type(valor) != int and type(valor) != float:
        return Exception
    return valor >= 0

# Teste
assert positivo_ou_negativo(10) == True
assert positivo_ou_negativo(-5) == False
assert positivo_ou_negativo(0) == True

assert positivo_ou_negativo("") == Exception
assert positivo_ou_negativo([]) == Exception
assert positivo_ou_negativo(None) == Exception
assert positivo_ou_negativo(True) == Exception

print("Todos os testes passaram!")