from asyncio import events
from fastapi import APIRouter, Body, HTTPException,status
from typing import List
from models.package import Package

package_router = APIRouter(tags=["Pacotes"])

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


@package_router.post("/package")
async def new_package(body: Package = Body(...)) -> dict:
    for package in packages:
        if body.id == package.id:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Um pacote com esse id já existe.")
    packages.append(body)
    return {"mesagem": "pacote registrado com sucesso."}


@package_router.delete("/{id}")
async def delete_package(id:int) -> dict:
    for package in packages:
        if package.id == id:
            packages.remove(package)
            return {"mensagem": "Pacote deletado com sucesso!"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="O pacote com a ID informada não existe.")


@package_router.delete("/")
async def delete_all_packages() -> dict:
    packages.clear()
    return {"mensagem": "Todos os pacotes foram deletados."}