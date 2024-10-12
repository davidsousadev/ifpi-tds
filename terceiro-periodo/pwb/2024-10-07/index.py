from fastapi import FastAPI

app = FastAPI()

clubes_de_futebol = ['São Paulo', 'Vasco']

@app.get("/clubes")
def listar_clubes():
    return clubes_de_futebol

@app.post("/clubes")
def criar_clube(nome: str):
    clubes_de_futebol.append(nome)
    return 