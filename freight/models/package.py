from pydantic import BaseModel
from typing import Dict


class Package(BaseModel):
    id: int
    dimensao: Dict[str, int]
    peso: int
    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "dimensao": {
                    "altura": 102,
                    "largura": 40
                },
                "peso": 400
            }
        }


