"""

14.  Escreva uma função que recebes 3 valores reais X, Y e Z e que verifique se 
esses valores podem ser os comprimentos dos lados de um triângulo e, neste 
caso, retornar qual o tipo de triângulo formado. Para que X, Y e Z formem um 
triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento 
de cada lado de um triângulo é menor do que a soma do comprimento dos outros 
dois lados. O procedimento deve identificar o tipo de triângulo formado 
observando as seguintes definições: 
o Triângulo Equilátero: os comprimentos dos 3 lados são iguais. 
o Triângulo Isósceles: os comprimentos de 2 lados são iguais. 
o Triângulo Escaleno: os comprimentos dos 3 lados são diferentes. 

"""

def tipo_triangulo(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        if x == y == z:
            return 'Equilátero'
        elif x == y or x == z or y == z:
            return 'Isósceles'
        else:
            return 'Escaleno'
    return 'Não é um triângulo'

# Teste
assert tipo_triangulo(3, 3, 3) == 'Equilátero'
assert tipo_triangulo(3, 3, 5) == 'Isósceles'
assert tipo_triangulo(3, 4, 5) == 'Escaleno'
assert tipo_triangulo(1, 2, 3) == 'Não é um triângulo'
print("Todos os testes passaram!")