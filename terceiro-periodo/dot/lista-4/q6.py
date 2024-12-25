def numero_perfeito(num):
    if type(num) != int:
        return Exception
    divisores = sum(i for i in range(1, num) if num % i == 0)
    return divisores == num

# Teste
assert numero_perfeito(6) == True
assert numero_perfeito(28) == True
assert numero_perfeito(12) == False

assert numero_perfeito(12.2) == Exception
print("Todos os testes passaram!")