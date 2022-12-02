from pydantic import BaseModel, ValidationError, validator
from typing import Dict

delivery_type = []



class Package(BaseModel):
    nome: str
    valor_frete: int
    prazo_dias: int

    



