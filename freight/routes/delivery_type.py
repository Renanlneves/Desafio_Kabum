from fastapi import Body, APIRouter
from models.package import Package
from routes.package import packages


delivery_router = APIRouter(tags=["Tipo de entrega"])
delivery_type = []




@delivery_router.get("/tipo_entrega")
async def validar_dimensao():
    for package in packages:
        if package.dimensao:
            return package.dimensao["altura"]
    



