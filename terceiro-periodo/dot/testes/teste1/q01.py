# Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o
# seu volume (v = 4/3 * PI * R**3).
PI = 3.14
def volume(r):
    if type(r) != int and type(r) != float:
        return Exception
    
    return round(((4 / 3) * PI * r**3), 2)

print(volume(10))

# assert volume(10) == None


print("Todos os testes ok!")