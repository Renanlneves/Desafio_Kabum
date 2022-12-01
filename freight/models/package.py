from importlib.resources import Package
from pydantic import BaseModel
from typing import Dict


class Package(BaseModel):
    id: int
    dimensao: Dict [str: int, str: int]
    peso: int
    
    class Config:
        schema_extra = {
            "exemplo": {
                "id": "01",
                "dimensao": {
                    "altura": 102,
                    "largura": 40
                },
                "peso": 400
            }
        }


