from pydantic import BaseModel

class Delivery_type(BaseModel):
    nome : str
    valor_frete : float
    prazo_dias : int


    class Config:
        schema_extra = {
            "example":{
                "nome":"Kabum",
                "valor_frete": 4.5,
                "prazo_dias": 6
            }
        }