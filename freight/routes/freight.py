from fastapi import APIRouter, HTTPException, status
from models.freight import Freight

user_router = APIRouter(tags=["freight"])

freights = {}

@user_router.post("/company")
async def new_company(data:Freight) -> dict:
    if data.id or data.nome in freights:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Uma companhia com esse id ou nome já existe.")

    freights[data.id] = data
    return {"mensagem": "Companhia registrada com sucesso!"}