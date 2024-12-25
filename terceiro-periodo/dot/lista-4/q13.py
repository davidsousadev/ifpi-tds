def duracao_jogo(hora_inicio, minuto_inicio, hora_fim, minuto_fim):
    inicio_total = hora_inicio * 60 + minuto_inicio
    fim_total = hora_fim * 60 + minuto_fim
    if fim_total < inicio_total:
        fim_total += 24 * 60  # Considera o jogo terminando no dia seguinte
    duracao_minutos = fim_total - inicio_total
    return duracao_minutos // 60, duracao_minutos % 60

# Teste
assert duracao_jogo(23, 50, 0, 30) == (0, 40)
assert duracao_jogo(10, 15, 12, 45) == (2, 30)
assert duracao_jogo(15, 0, 15, 30) == (0, 30)
print("Todos os testes passaram!")