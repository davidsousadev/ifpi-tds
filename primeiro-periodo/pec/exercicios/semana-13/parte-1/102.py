# Escreva um programa que leia um número n. Considere uma lista com n posições, e então: a) preencha com 0 (zero) e imprima a lista; b) preencha com os números de 1 a n e imprima a lista; c) preencha com valores lidos pelo teclado e imprima a lista; d) preencha na ordem inversa com valores lidos pelo teclado e imprima a lista; dica: use insert para sempre incluir os elementos no início da lista;



def prencherListaZero(n, l, c):
    while True:
        for x in range(n):
            l.append(c)
        if (n > 0):
            return l
            break


def prencherListaSeguencia(n, s, c):
    while True:
        for x in range(n):
            c += 1
            s.append(c)
        if (n > 0):
            return s
            break

def prencherListaInput(n, i):
    while True:
        for x in range(n):
            c = int(input("Insira um item a lista: "))
            i.append(c)
        if (n > 0):
            return i
            break

def prencherListaInputReverso(n, r):
    while True:
        for x in range(n):
            c = int(input("Insira um item a lista: "))
            r.insert(0, c)
        if (n > 0):
            return r
            break

def main():
    n = int(input("Digite a quantidade de itens na lista: "))
    c = 0
    l = []
    s = []
    i = []
    r = []
    if n>0:
        listaZero = prencherListaZero(n, l, c)
        listaRange = prencherListaSeguencia(n, s, c)
        listaInput = prencherListaInput(n, i)
        listaReverso = prencherListaInputReverso(n, r)
        print(f"Lista com Zeros {listaZero}")
        print(f"Lista com a Seguencia {listaRange}")
        print(f"Lista com a quantidade {listaInput}")
        print(f"Lista com a quantidade de traz pra frente {listaReverso}")
    else:
        print(l,s,i,r, sep='\n')
    
    
if __name__ == '__main__':
    main()