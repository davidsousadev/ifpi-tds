"""

2. Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma letra. Se a letra for A o procedimento calcula a média aritmética das notas do aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2). A função deve retornar a média calculada.

"""

def media_notas(nota1, nota2, nota3, tipo):
    if ((
        ((type(nota1) != int) and 
         (type(nota1) != float)) or 
        ((type(nota2) != int) and 
         (type(nota2) != float)) or 
        ((type(nota3) != int) and 
         (type(nota3) != float)) or
         (type(tipo) != str) or 
         (tipo.upper() != "A") and 
         (tipo.upper() != "P")
        )):
        return Exception
    
    if tipo == 'A':
        return (nota1 + nota2 + nota3) / 3
    elif tipo == 'P':
        return (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10
    
    return 0
# Testes
assert media_notas(6, 7, 8, 'A') == 7
assert media_notas(6, 7, 8, 'P') == 6.7
assert media_notas(5, 5, 5, 'A') == 5
assert media_notas(5.5, 5.5, 5.5, 'A') == 5.5

assert media_notas("", 5, 5, 'A') == Exception
assert media_notas(5, 5, 5, 'q') == Exception
assert media_notas("5", 5, 5, 'q') == Exceptionassert volume_esfera(True) == Exception
assert volume_esfera(None) == Exception

print("Todos os testes passaram!")