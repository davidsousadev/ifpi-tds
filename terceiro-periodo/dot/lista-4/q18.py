"""

18. Faça uma função que recebe, por parâmetro, um valor N e calcula e escreve 
a      tabuada      de      1      até      N.      Mostre     a     tabuada     na     forma: 
1 x N = N 
2 x N = 2N 
... 
N x N = N2

"""

def tabuada(N):
    return [(i, N, i * N) for i in range(1, N+1)]

# Teste
assert tabuada(3) == [(1, 3, 3), (2, 3, 6), (3, 3, 9)]
assert tabuada(1) == [(1, 1, 1)]
assert tabuada(5) == [(1, 5, 5), (2, 5, 10), (3, 5, 15), (4, 5, 20), (5, 5, 25)]
print("Todos os testes passaram!")