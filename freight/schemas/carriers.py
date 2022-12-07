from models.package import Package
from routes.package import packages

class Carriers():
    
    async def __init__(self, ninja, kabum):
        self.ninja = ninja
        self.kabum = kabum


    async def validar_ent_ninja():
        for package in packages:
            if package.dimensao["altura"] > 10 and package.dimensao["altura"] < 200:
                if package.dimensao["largura"] > 6 and package.dimensao["largura"] < 140:
                    if package.peso > 0:
                        return {"mensagem": "Chegou até aqui!"}