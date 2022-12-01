from pydantic import BaseModel

class Freight(BaseModel):
    id: int
    nome: str
    constante_calculo: float
    altura_maxima: int
    altura_maxima: int
    largura_minima: int
    largura_maxima: int
    prazo_entrega: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "nome": "Entrega Ninja",
                "constante_calculo": 0.3,
                "altura_minima": 10,
                "altura_maxima": 200,
                "largura_minima": 6,
                "largura_maxima": 140,
                "prazo_entrega": "6 dias"

            }
        }