"""
1. Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu volume (v = 4/3 * PI * R**3).
"""
import math

def volume_esfera(raio):
    if type(raio) != int and type(raio) != float or type(raio)== str:
        return Exception
    volume = round(((4/3) * math.pi * raio**3), 2)
    return volume

# Testes
assert volume_esfera(3) == 113.1
assert volume_esfera(0) == 0
assert volume_esfera(1) == 4.19

assert volume_esfera("a") == Exception
assert volume_esfera("3") == Exception
assert volume_esfera("") == Exception

print("Todos os testes passaram!")