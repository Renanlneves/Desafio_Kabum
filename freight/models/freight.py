from pydantic import BaseModel

class Freight(BaseModel):
    id: str
    nome: str
    constante_calculo: int
    altura_maxima: int
    altura_maxima: int
    largura_minima: int
    largura_maxima: int
    prazo_entrega: str

    class Config:
        schema_extra = {
            "exemplo": {
                "id": "01",
                "nome": "Entrega Ninja",
                "constante_calculo": 0.3,
                "altura_minima": 10,
                "altura_maxima": 200,
                "largaura_minima": 6,
                "largura_maxima": 140,
                "prazo_entrega": "6 dias"

            }
        }