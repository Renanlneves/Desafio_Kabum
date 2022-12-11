from fastapi import APIRouter, HTTPException,status
from typing import List
from models.package import Package
from routes.freight import freights
from schemas.carriers import Carriers

package_router = APIRouter(tags=["Pacotes"])
carrier = Carriers()

packages = []


@package_router.get("/", response_model= List[Package])
async def get_all_packages() -> dict[Package]:
    
    return packages


@package_router.get("/{id}", response_model=Package)
async def get_one_package(id: int) -> Package:
    for package in packages:
        if package.id == id:
            return package
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pacote com o ID informado não existe.")


@package_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_package(id:int) -> dict:
    for package in packages:
        if package.id == id:
            packages.remove(package)
            return {"mensagem": "Pacote deletado com sucesso!"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="O pacote com a ID informada não existe.")


@package_router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_all_packages() -> dict:
    packages.clear()
    return {"mensagem": "Todos os pacotes foram deletados."}


#@package_router.post("/package", status_code=status.HTTP_201_CREATED)
#async def new_package(pack:Package) -> dict:
#    for package in packages:
#        if pack.id == package.id:
#            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Um pacote com esse id já existe.")
#    packages.append(pack)
#    return {"mesagem": "pacote registrado com sucesso."}

"""fazer um novo post
pegar a primeira parte igual a do post pacakage
usar um response model para retornar o tipo de entrega. """

@package_router.post("/package", status_code=status.HTTP_201_CREATED)
async def new_package(pack:Package) -> dict:
    for package in packages:
        if pack.id == package.id:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Um pacote com esse id já existe.")
    packages.append(pack)

    if  carrier.validar_ent_ninja(packages):

        preco_ninja = (packages[0].peso * freights[0]["constante_calculo"])/ 10 
        
    if carrier.validar_ent_kabum(packages):
        preco_kabum = (packages[0].peso * freights[1]["constante_calculo"])/ 10

    return {"mensagem": "pacote registrado com sucesso!"}