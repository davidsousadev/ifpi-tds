"""

Crie uma API para gerenciar Livros.
Faça as Operações para:
Listar Todos (Aplicar filtro por gênero, ano de lançamento)
Obter Detalhes de um Livro por ID
Atualizar Livro
Remover Livro
Livro tem os atributos (id, titulo, genero, ano, autor, pais, quantidade de páginas)

"""
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

class Livro(BaseModel):
    id: int | None = None
    titulo: str = Field(min_length=1)
    genero: str = Field(min_length=1)
    ano: int | None = None
    autor: str = Field(min_length=1)
    pais: str = Field(min_length=1)
    quantidade_de_paginas: int | None = None

class AlterarLivro(BaseModel):
    titulo: str = Field(min_length=1)
    genero: str = Field(min_length=1)
    ano: int | None = None
    autor: str = Field(min_length=1)
    pais: str = Field(min_length=1)
    quantidade_de_paginas: int | None = None

livros: List[Livro] = []

livros.append(Livro(
    id=1,
    titulo="Oi",
    genero="Romance",
    ano=2024,
    autor="David",
    pais="Brasil",
    quantidade_de_paginas=100
))

livros.append(Livro(
    id=2,
    titulo="Tial",
    genero="Terror",
    ano=2023,
    autor="Sousa",
    pais="Portugal",
    quantidade_de_paginas=500
))

app = FastAPI()

@app.get('/livros', status_code=status.HTTP_200_OK)
def listar_livros(ano: int | None = None, genero: str | None = None):
    
    if not genero and not ano:
        return livros
    livros_por_filtro = []
    if genero != None and genero != "" and ano != None and ano != "":
        for livro in livros:
            if livro.genero == genero and livro.ano == ano:
                livros_por_filtro.append(livro)
    else:
        for livro in livros:
            if livro.ano == ano:
                livros_por_filtro.append(livro)
            if livro.genero == genero:
                livros_por_filtro.append(livro)
                
    return livros_por_filtro

    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum livro encontrado"
        )

@app.get('/livros/{livro_id}', status_code=status.HTTP_200_OK)
def listar_livros_por_id(livro_id: int):
    for livro in livros:
        if livro.id == livro_id:
            return livro
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Id do livro não localizado = {livro_id}"
    )

@app.post('/livros', status_code=status.HTTP_201_CREATED)
def adicionar_livros(novo_livro: Livro):
    livros.append(novo_livro)
    return livros

@app.put('/livros/{livro_id}', status_code=status.HTTP_200_OK)
def atualizar_livros(livro_id: int, dados: AlterarLivro):
    for livro in livros:
        if livro.id == livro_id:
            if dados.titulo: 
                livro.titulo = dados.titulo
            if dados.genero: 
                livro.genero = dados.genero
            if dados.ano: 
                livro.ano = dados.ano
            if dados.autor: 
                livro.autor = dados.autor
            if dados.pais:
                livro.pais = dados.pais
            if dados.quantidade_de_paginas: 
                livro.quantidade_de_paginas = dados.quantidade_de_paginas
            return livro
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Livro com id {livro_id} não encontrado"
    )

@app.delete('/livros/{livro_id}', status_code=status.HTTP_204_NO_CONTENT)
def deletar_livros(livro_id: int):
    for livro in livros:
        if livro.id == livro_id:
            livros.remove(livro)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Livro com id {livro_id} não encontrado"
    )
