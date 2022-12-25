from fastapi import APIRouter, HTTPException, status
from typing import List
from models.package import Package
from routes.freight import freights
from models.delivery_type import Delivery_type


package_router = APIRouter(tags=["Pacotes"])


packages = []
delivery_type = []


@package_router.post(response_model=List[Delivery_type], status_code=status.HTTP_201_CREATED)
async def new_package(pack: Package) -> dict:
    packages.clear()
    delivery_type.clear()

    for package in packages:
        if pack.id == package.id:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Um pacote com esse id já existe.")
        packages.append(pack)

        entrega_ninja = (package.dimensao["altura"] > 10 and package.dimensao["altura"] < 200) and (
            package.dimensao["largura"] > 6 and package.dimensao["largura"] < 140) and (package.peso > 0)

        if entrega_ninja:
            preco_ninja = round(
                (packages[0].peso * freights[0]["constante_calculo"]) / 10, 2)
            delivery_test = Delivery_type(
                nome="Ninja", valor_frete=preco_ninja, prazo_dias=6)

            delivery_type.append(delivery_test)

        entrega_kabum = (package.dimensao["altura"] > 5 and package.dimensao["altura"] < 140) and (
            package.dimensao["largura"] > 13 and package.dimensao["largura"] < 125) and (package.peso > 0)

        if entrega_kabum:
            preco_kabum = round(
                (packages[0].peso * freights[1]["constante_calculo"]) / 10, 2)
            delivery_test = Delivery_type(
                nome="Kabum", valor_frete=preco_kabum, prazo_dias=6)

            delivery_type.append(delivery_test)

    return delivery_type
