def peso_ideal(altura, sexo):
    if (type(altura) != int or type(altura) != float) or (sexo.upper() != "M" and sexo.upper() != "F"):
        return Exception
    if sexo == 'M':
        return 72.7 * altura - 58
    elif sexo == 'F':
        return 62.1 * altura - 44.7
    return 0
# Teste
assert peso_ideal(1.75, 'M') == 72.7 * 1.75 - 58
assert peso_ideal(1.60, 'F') == 62.1 * 1.60 - 44.7
assert peso_ideal(1.80, 'M') == 72.7 * 1.80 - 58

assert peso_ideal("", 0) == Exception
assert peso_ideal(0, "") == Exception
assert peso_ideal(0, "F") == Exception
assert peso_ideal(1.0, "F") == Exception
print("Todos os testes passaram!")
