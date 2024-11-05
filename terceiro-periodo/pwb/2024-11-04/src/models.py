
# Refatoração: Melhorar a qualidade interna de um código
# sem alterar o seu comportamento observável

# PEP-8: Manual de Estilo de Código de Python

from sqlalchemy import table
from sqlmodel import SQLModel, Field


class LivroBase(SQLModel):
    titulo: str = Field(min_length=1)
    genero: str = Field(min_length=1)
    ano: int | None = None
    autor: str = Field(min_length=1)
    pais: str = Field(min_length=1)
    quantidade_de_paginas: int | None = None

class Livro(LivroBase, table=True):
  id: int | None = Field(default=None, primary_key=True)
    

class RequestLivro(LivroBase):
    pass