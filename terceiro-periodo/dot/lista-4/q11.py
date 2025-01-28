"""

11.  Faça  uma  função  que  recebe,  por  parâmetro,  a  altura  e  o  sexo  de  uma 
pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal usando a 
fórmula peso ideal = 72.7 * altura - 58 e, para mulheres, peso ideal = 62.1 * altura 
- 44.7.

"""

def peso_ideal(altura, sexo):
    if ((
            (type(altura) != int) and 
            (type(altura) != float)
            ) or 
        (altura < 1) and
        (
            (sexo.upper() != "M" and 
             sexo.upper() != "F")
             )):
        return Exception
    if 1 >= altura <= 3:
        return Exception
    
    if sexo == 'M':
        return round((72.7 * altura - 58), 2)
    
    elif sexo == 'F':
        return round((62.1 * altura - 44.7), 2)
    return 0

# Testes
assert peso_ideal(1.75, 'M') == 69.23
assert peso_ideal(1.60, 'F') == 54.66
assert peso_ideal(1.80, 'M') == 72.86

assert peso_ideal("", 0) == Exception
assert peso_ideal(0, "") == Exception
assert peso_ideal(0, "F") == Exception
assert peso_ideal(1.0, "F") == Exception
assert peso_ideal([1.80], ['M']) == Exception
assert peso_ideal(True, True) == Exception
assert peso_ideal(None, None) == Exception

print("Todos os testes passaram!")
