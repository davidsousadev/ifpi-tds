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
print("Todos os testes passaram!")