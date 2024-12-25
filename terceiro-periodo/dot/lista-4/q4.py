def tempo_processos(segundos):
    if type(segundos) != int or segundos < 0:
        return Exception
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return horas, minutos, segundos_restantes

# Teste
assert tempo_processos(3665) == (1, 1, 5)
assert tempo_processos(59) == (0, 0, 59)
assert tempo_processos(7200) == (2, 0, 0)
assert tempo_processos(0) ==(0, 0, 0)

assert tempo_processos(-100) == Exception
print("Todos os testes passaram!")