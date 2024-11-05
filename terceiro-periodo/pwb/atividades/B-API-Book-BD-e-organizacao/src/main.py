"""

Crie uma API para gerenciar Livros.
Faça as Operações para:
Listar Todos (Aplicar filtro por gênero, ano de lançamento)
Obter Detalhes de um Livro por ID
Atualizar Livro
Remover Livro
Livro tem os atributos (id, titulo, genero, ano, autor, pais, quantidade de páginas)

Organize o código de acordo com o visto em sala de aula em Models, Controllers, Database e Main

Use Banco de Dados SQL. 

Sugestão: Tente conectar com BD postgreSQL

"""

from fastapi import FastAPI
from sqlmodel import SQLModel
from .livros_controller import router as livros_router
from .database import get_engine



app = FastAPI()

app.include_router(livros_router, 
                   prefix='/livros')

# Criar DB
SQLModel.metadata.create_all(get_engine())

