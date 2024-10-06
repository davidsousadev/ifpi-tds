# Crie um dicionário e armazene nele os dados de livros: título, isbn, autor e preço. A chave do dicionários será um código numérico e sequencial, gerado automaticamente, iniciando pelo número 101 (cento e um). A leitura de uma descrição vazia para o título finaliza a leitura. Imprima todos os dados usando o padrão “Nome do Campo: valor”.



def adicionar_livro():
    livros = {}
    while True:
        titulo = str(input().strip())
        if titulo == "":
            break
        isbn = str(input().strip())
        autor = str(input().strip())
        preco = float(input())
        preco = f"{preco:.2f}"
        novo_codigo = len(livros) + 101
        livros[novo_codigo] = {
            "Título": titulo,
            "ISBN": isbn,
            "Autor": autor,
            "Preço": preco
        }
    return livros
    
    
    
def main():
    livros = adicionar_livro()
    for codigo, info in livros.items():
        print(f"Código: {codigo}")
        for campo, valor in info.items(): 
            print(f"{campo}: {valor}")

            
if __name__ =='__main__':
	main()