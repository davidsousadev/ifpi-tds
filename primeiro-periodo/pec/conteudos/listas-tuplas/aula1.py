#funcoes
lista = [1,2,3,4,5]
print(len(lista))
lista.append(6)
print(lista)
del lista[5]
print(lista)
#
lista2 = [7,4,2,9,5,3,8,6,1,0]
print(max(lista2))
print(min(lista2))
print(lista2.sort())#ordena lista
print(lista2)
print(sorted(lista2))
del lista2[3:5]#fatia a ser removida

lista2.append("x")
lista2.insert(0,"x")
lista2.insert(5,"x")
print(lista2)
print(lista2.index("x"))
print(lista2.index("x", 1))#elemento , apartir de
print(lista2.index("x", 6, len(lista2)))#elemento , apartir de , ate o tamanho
#print(lista2.index("y")) #Errado
print("y" in lista2)#retorna True se tiver o elemento na lista