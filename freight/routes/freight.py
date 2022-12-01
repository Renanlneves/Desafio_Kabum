from fastapi import APIRouter, HTTPException, status
from models.freight import Freight

freight_router = APIRouter(tags=["Frete"])

freights = {}

@freight_router.post("/company")
async def new_company(data:Freight) -> dict:
    if data.id in freights:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Uma companhia com esse id já existe.")

    freights[data.id] = data
    return {"mensagem": "Companhia registrada com sucesso!"}