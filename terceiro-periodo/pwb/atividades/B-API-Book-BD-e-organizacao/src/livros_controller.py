from fastapi import APIRouter, status, HTTPException

from src.database import get_engine
from src.models import Livro, RequestLivro
from sqlmodel import Session, select

router = APIRouter()

@router.get('', status_code=status.HTTP_200_OK)
def listar_livros(ano: int | None = None, genero: str | None = None):
    session = Session(get_engine())
  
    statement = select(Livro)
    
    if ano:
        statement = statement.where(Livro.ano == ano)
    elif genero:
        statement = statement.where(Livro.genero == genero)
    elif ano and genero:
        statement = statement.where(Livro.ano == ano, Livro.genero == genero)
        
    livros = session.exec(statement).all()
    
    return livros
    
    

@router.get('/{livro_id}', status_code=status.HTTP_200_OK)
def listar_livros_por_id(livro_id: int):
    
    session = Session(get_engine())
    
    statement = select(Livro).where(Livro.id == livro_id)
    livro = session.exec(statement).first()
    
    if livro:
        return livro
    
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Id do livro não localizado = {livro_id}"
            )
        

@router.post('', status_code=status.HTTP_201_CREATED)
def adicionar_livros(request_livro: RequestLivro):
    livro = Livro(
    titulo = request_livro.titulo,
    genero = request_livro.genero,
    ano = request_livro.ano,
    autor = request_livro.autor,
    pais = request_livro.pais,
    quantidade_de_paginas = request_livro.quantidade_de_paginas
    )
  
    session = Session(get_engine())
    session.add(livro)
    session.commit()
    session.refresh(livro)

    return livro

# UPDATE livros SET disponivel=1 WHERE titulo='O Diário de Anne Frank';

@router.put('/{livro_id}', status_code=status.HTTP_200_OK)
def atualizar_livros(livro_id: int, dados: RequestLivro):

    session = Session(get_engine())
    statement = select(Livro)
    statement = statement.where(Livro.id == livro_id)
    livro = session.exec(statement).first()
    
    if livro_id and livro:
        
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
            
        session.add(livro)
        session.commit()
        
        session.refresh(livro)

        return livro
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Livro com id {livro_id} não encontrado"
    )

@router.delete('/{livro_id}', status_code=status.HTTP_204_NO_CONTENT)
def deletar_livros(livro_id: int):

    session = Session(get_engine())
    statement = select(Livro)
    statement = statement.where(Livro.id == livro_id)
    livro = session.exec(statement).first()
    
    if livro:
        session.delete(livro)
        session.commit()
        return
    
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Livro com id {livro_id} não encontrado"
    )
    