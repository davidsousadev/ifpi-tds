"""

13.  Faça uma  função que  recebe, por parâmetro,  a  hora de  inicio  e  a  hora  de 
término de um jogo, ambas subdivididas em 2 valores distintos: horas e minutos. 
O  procedimento  deve  retornar,  também  por  parâmetro,  a  duração  do  jogo  em 
horas e minutos, considerando que o tempo máximo de duração de um jogo é 
de 24 horas e que o jogo pode começar em um dia e terminar no outro.

"""

def duracao_jogo(hora_inicio, minuto_inicio, hora_fim, minuto_fim):
    inicio_total = hora_inicio * 60 + minuto_inicio
    fim_total = hora_fim * 60 + minuto_fim
    if fim_total < inicio_total:
        fim_total += 24 * 60
    duracao_minutos = fim_total - inicio_total
    return duracao_minutos // 60, duracao_minutos % 60

# Teste
assert duracao_jogo(23, 50, 0, 30) == (0, 40)
assert duracao_jogo(10, 15, 12, 45) == (2, 30)
assert duracao_jogo(15, 0, 15, 30) == (0, 30)

print("Todos os testes passaram!")