
def idade_em_dias(anos, meses, dias):
    if (type(anos) != int or type(meses) != int or type(dias) != int) or (anos < 0 or meses < 0 or dias < 0):
        return Exception
    return anos * 365 + meses * 30 + dias

# Teste
assert idade_em_dias(1, 0, 0) == 365
assert idade_em_dias(0, 6, 0) == 180
assert idade_em_dias(0, 0, 30) == 30
assert idade_em_dias(0, 0, 0) == 0

assert idade_em_dias(-10, -10, -10) == Exception
assert idade_em_dias("-10", "-10", "-10") == Exception
print("Todos os testes passaram!")