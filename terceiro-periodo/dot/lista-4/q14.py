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