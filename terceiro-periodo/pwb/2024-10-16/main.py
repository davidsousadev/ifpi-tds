# fastapi dev main.py

from fastapi import FastAPI, status, HTTPException

from pydantic import BaseModel, Field

app = FastAPI()

class Clube(BaseModel):
    id: int | None = None
    nome: str = Field(min_length=1)
    serie: str = Field(min_length=1, max_length=1)

class AterarClube(BaseModel):
    id: int | None = None
    nome: str
    serie: str = Field(min_length=1, max_length=1)

clubes_futebol: list[Clube] = []

# All clubes
@app.get("/clubes", status_code=status.HTTP_200_OK)
def listar_clubes(serie: str| None = None):
    if not serie:
        return clubes_futebol
    clubes = []
    for clube in clubes_futebol: 
        if clube.serie == serie:
            clubes.append(clube)
    return clubes

# One Clube
@app.get("/clubes/{clube_id}", status_code=status.HTTP_200_OK)
def detalhes_clube(clube_id: int):
    for clube in clubes_futebol:
        if clube_id == clube.id:
            return clube
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Clube não localizado com id = {clube_id}"
    )

# Post clube
@app.post("/clubes", status_code=status.HTTP_201_CREATED)
def adicionar_clube(novo_clube: Clube):
    clubes_futebol.append(novo_clube)
    return clubes_futebol

# My Put clube
@app.put("/clubes/{clube_id}", status_code=status.HTTP_200_OK)
async def alterar_clube(clube_id: int, clube: Clube):
    clubes_futebol[clube_id] = clube
    return clubes_futebol

@app.put("/clubes/{clube_id}", status_code=status.HTTP_200_OK)
def alterar_clubes(clube_id: int, dados: AterarClube):
    for clube in clubes_futebol:
        if clube.id == clube_id:
            clube.nome = dados.nome
    return clubes_futebol

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Clube não localizado com id = {clube_id}"
    )



# Delete all clubes
@app.delete("/clubes/", status_code=status.HTTP_200_OK)
def deletar_clubes():
    clubes_futebol.clear()
    return clubes_futebol    

# Delete one clube
@app.delete("/clubes/{clube_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_clube(clube_id: int):
    clubes_futebol.pop(clube_id)
    return clubes_futebol 

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Clube não localizado com id = {clube_id}"
    )

"""

curl -X 'POST' \
  'http://127.0.0.1:8000/clubes' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1,
  "nome": "São Paulo",
  "serie": "A"
}'

"""