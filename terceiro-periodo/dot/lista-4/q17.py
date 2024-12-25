def maior_menor(valores):
    return max(valores), min(valores)

# Teste
assert maior_menor([5, 10, 15, 3, 2]) == (15, 2)
assert maior_menor([50, 30, 20]) == (50, 20)
assert maior_menor([1]) == (1, 1)
print("Todos os testes passaram!")