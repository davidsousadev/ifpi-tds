def conceito_aluno(nota):
    if type(nota) != int and type(nota) != float:
        return Exception
    if 0 <= nota <= 4.9:
        return 'D'
    elif 5 <= nota <= 6.9:
        return 'C'
    elif 7 <= nota <= 8.9:
        return 'B'
    else:
        return 'A'

# Teste
assert conceito_aluno(3) == 'D'
assert conceito_aluno(6) == 'C'
assert conceito_aluno(8) == 'B'
assert conceito_aluno(9.5) == 'A'

assert conceito_aluno("10") == Exception
print("Todos os testes passaram!")