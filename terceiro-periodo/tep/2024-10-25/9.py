"""

9) Com relação as built-in functions, assinale a alternativa incorreta:
a) type() - Retorna o tipo de um objeto
b) dict() - Cria um dicionário
c) tupla() - Cria uma tupla
d) zip() - Retorna um iterador de tuplas

"""
x = None

# a) type() - Retorna o tipo de um objeto
print(type(x))

# b) dict() - Cria um dicionário
x = dict()

print(type(x))

# Alternativa incorreta
# c) tupla() - Cria uma tupla
# x = tuple()

# d) zip() - Retorna um iterador de tuplas

x = []
y = []

z = zip(x, y)

print(type(z))