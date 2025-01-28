"""

10.  Faça uma  função que  recebe  a  média  final  de  um  aluno  por  parâmetro e 
retorna o seu conceito, conforme a tabela abaixo: 
Nota Conceito 
de 0,0 a 4,9  D 
de 5,0 a 6,9  C 
de 7,0 a 8,9  B 
de 9,0 a 10,0 A 


"""

def conceito_aluno(nota):
    if type(nota) != int and type(nota) != float:
        return Exception
    if nota < 0 or nota > 10.0:
        return Exception
    if nota <= 4.9 and nota >= 0:
        return 'D'
    elif 5 <= nota <= 6.9:
        return 'C'
    elif 7 <= nota <= 8.9:
        return 'B'
    elif nota <=10:
        return 'A'

# Testes
assert conceito_aluno(3) == 'D'
assert conceito_aluno(6) == 'C'
assert conceito_aluno(8) == 'B'
assert conceito_aluno(9.5) == 'A'

assert conceito_aluno(0) == 'D'
assert conceito_aluno(-10) == Exception
assert conceito_aluno(11) == Exception

assert conceito_aluno("10") == Exception
assert conceito_aluno([]) == Exception
assert conceito_aluno(True) == Exception
assert conceito_aluno(None) == Exception

print("Todos os testes passaram!")