from asyncio import events
from fastapi import APIRouter, Body, HTTPException,status
from typing import Dict
from models.package import Package

package_router = APIRouter(tags=["Pacotes"])

packages = {}

@package_router.get("/", response_model= Dict[Package])
async def retorna_todos_pacotes() -> dict[Package]:
    return packages
    
@package_router.get("/{id}", response_model=Package)
async def retorna_um_pacote(id: int) -> Package:
    for package in packages:
        if package.id == id:
            return package
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pacote com o ID informado não existe.")
