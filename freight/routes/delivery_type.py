from fastapi import Body, APIRouter
from models.package import Package
from routes.package import packages


delivery_router = APIRouter(tags=["Tipo de entrega"])
delivery_type = []




@delivery_router.get("/delivery_type")
async def validar_dimensao():
    for package in packages:
        if package.dimensao["altura"] > 10 and package.dimensao["altura"] < 200:
            if package.dimensao["largura"] > 6 and package.dimensao["largura"] < 140:
                if package.peso > 0:
                    return {"mensagem": "Chegou até aqui!"}
    



