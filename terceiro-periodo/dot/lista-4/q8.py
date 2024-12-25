def positivo_ou_negativo(valor):
    if type(valor) != int and type(valor) != float:
        return Exception
    return valor >= 0

# Teste
assert positivo_ou_negativo(10) == True
assert positivo_ou_negativo(-5) == False
assert positivo_ou_negativo(0) == True

assert positivo_ou_negativo("") == Exception
print("Todos os testes passaram!")