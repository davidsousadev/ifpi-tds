from django import conf
from sqlmodel import create_engine
from decouple import config

def get_engine():
  # Usuário e Senha
  user = config('USERNAMEX')
  password = config('PASSWORD')
  # Nome do Banco de Dados
  db_name = config('DB_NAME')
  # Host e Porta
  host = config('HOST')
  port = config('PORT')
  # Montar a URL para conexão
  return create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}?sslmode=require')

  
# Local
#  return create_engine("sqlite:///livros.db")