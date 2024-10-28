# fastapi dev main.py

from fastapi import FastAPI
from .clubes_controller import router as clubes_router
from .models import Clube, RequestClube
from sqlmodel import Field, Session, SQLModel, create_engine, select
from .database import get_engine

app = FastAPI()


app.include_router(clubes_router, prefix='/clubes')

SQLModel.metadata.create_all(get_engine())

"""

curl -X 'POST' \
  'http://127.0.0.1:8000/clubes' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "nome": "São Paulo",
  "serie": "A"
}'

"""