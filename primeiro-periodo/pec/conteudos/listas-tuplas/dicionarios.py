tabela={
    "Nome": "David"
}


tabela.get("Nome","Não encontrado")
print(tabela.values())
print(tabela.keys())
print(tabela.items())

#tupla não mexe
print(tabela.get("Nome","Não encontrado"))

print(tabela["Nome"])

for chave in tabela:
    print(tabela[chave])

    del tabela[chave]