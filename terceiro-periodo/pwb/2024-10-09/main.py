from fastapi import FastAPI, status, HTTPException

from pydantic import BaseModel

app = FastAPI()

class Clube(BaseModel):
    id: int | None = None
    nome: str

clubes_futebol: list[Clube] = []

@app.get("/clubes", status_code=status.HTTP_200_OK)
def listar_clubes():
    return clubes_futebol

@app.get("/clubes/{clube_id}")
def detalhes_clube(clube_id: int):
    for clube in clubes_futebol:
        if clube_id == clube.id:
            return clube
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Clube não localizado com id = {clube_id}"
    )

@app.post("/clubes", status_code=status.HTTP_201_CREATED)
def adicionar_clube(novo_clube: Clube):
    clubes_futebol.append(novo_clube)
    return clubes_futebol

@app.put("/clubes/{clube_id}", status_code=status.HTTP_200_OK)
def alterar_clube(clube_id: int, clube: Clube):
    clubes_futebol[clube_id] = clube
    return clubes_futebol
    
@app.delete("/clubes/{clube_id}", status_code=status.HTTP_200_OK)
def alterar_clube(clube_id: int):
    clubes_futebol.pop(clube_id)
    return clubes_futebol    
