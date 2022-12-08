from fastapi import Body, APIRouter
from models.package import Package
from routes.package import packages
from schemas.carriers import Carriers


carrier = Carriers()
delivery_router = APIRouter(tags=["Tipo de entrega"])
delivery_type = []




@delivery_router.get("/delivery_type")
async def delivery_type():
    if  carrier.validar_ent_ninja(packages):
        print( {"mensagem": "sucesso! Ninja!"})
    if carrier.validar_ent_kabum(packages):
        print( {"mensagem": "sucesso! kabum!"})

    



