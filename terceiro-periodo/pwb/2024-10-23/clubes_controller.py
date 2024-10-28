from fastapi import APIRouter, status, HTTPException
from .models import Clube, RequestClube
from .database import get_engine
from sqlmodel import Session, select

router = APIRouter()



# All clubes
@router.get("", status_code=status.HTTP_200_OK)
def listar_clubes(serie: str| None = None):
    # if not serie:
    #     return clubes_futebol
    # clubes = []
    # for clube in clubes_futebol: 
    #     if clube.serie == serie:
    #         clubes.append(clube)
    
    session = Session(get_engine())
    statement = select(Clube)
    
    if serie:
        statement = select(Clube.serie==serie)
    clubes = session.exec(statement).all()
    return clubes

# One Clube
@router.get("/{clube_id}", status_code=status.HTTP_200_OK)
def detalhes_clube(clube_id: int):
    for clube in clubes_futebol:
        if clube_id == clube.id:
            return clube
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Clube não localizado com id = {clube_id}"
    )

# Post clube
@router.post("", status_code=status.HTTP_201_CREATED)
def adicionar_clube(novo_clube: RequestClube):
    session = Session(get_engine())
    clube = Clube(nome=novo_clube.nome, serie=novo_clube.serie)
    session.add(clube)
    session.commit()
    session.refresh(clube)
    #clubes_futebol.append(novo_clube)
    #return clubes_futebol
    return clube

# My Put clube
@router.put("/{clube_id}", status_code=status.HTTP_200_OK)
async def alterar_clube(clube_id: int, clube: Clube):
    clubes_futebol[clube_id] = clube
    return clubes_futebol


@router.put("/{clube_id}", status_code=status.HTTP_200_OK)
def alterar_clubes(clube_id: int, dados: RequestClube):
    for clube in clubes_futebol:
        if clube.id == clube_id:
            clube.nome = dados.nome
    return clubes_futebol

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Clube não localizado com id = {clube_id}"
    )



# Delete all clubes
@router.delete("", status_code=status.HTTP_200_OK)
def deletar_clubes():
    clubes_futebol.clear()
    return clubes_futebol    

# Delete one clube
@router.delete("/{clube_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_clube(clube_id: int):
    clubes_futebol.pop(clube_id)
    return clubes_futebol 

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Clube não localizado com id = {clube_id}"
    )