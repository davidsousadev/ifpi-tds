"""

7. Faça uma função que recebe a idade de um nadador por parâmetro e retorna 
a categoria desse nada dor de acordo com a tabela abaixo: 
Idade Categoria 
5 a 7 anos Infantil A 
8 a 10 anos Infantil B 
11-13 anos Juvenil A 
14-17 anos Juvenil B 
Maiores  de  18  anos 
(inclusive)

"""

def categoria_nadador(idade):
    if type(idade) != int or idade < 5:
        return Exception
    if 5 <= idade <= 7:
        return 'Infantil A'
    elif 8 <= idade <= 10:
        return 'Infantil B'
    elif 11 <= idade <= 13:
        return 'Juvenil A'
    elif 14 <= idade <= 17:
        return 'Juvenil B'
    else:
        return 'Adulto'

# Teste
assert categoria_nadador(6) == 'Infantil A'
assert categoria_nadador(9) == 'Infantil B'
assert categoria_nadador(15) == 'Juvenil B'
assert categoria_nadador(20) == 'Adulto'

assert categoria_nadador(4) == Exception
assert categoria_nadador(5.0) == Exception
assert categoria_nadador("") == Exception
print("Todos os testes passaram!")