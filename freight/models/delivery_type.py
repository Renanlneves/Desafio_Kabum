from pydantic import BaseModel

class Delivery_type(BaseModel):
    preco: float

#    class Config:
#        schema_extra = {
#            "example": {
#                "preco": 1.00
#            }
#        }