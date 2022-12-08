

from contextlib import nullcontext


class Carriers():
        
    async def validar_ent_ninja(self, packages): 
        for package in packages:
            if package.dimensao["altura"] > 10 and package.dimensao["altura"] < 200:
                if package.dimensao["largura"] > 6 and package.dimensao["largura"] < 140:
                    if package.peso > 0:
                        return {"mensagem": "Chegou até aqui!"}
        return None


    async def validar_ent_kabum(self, packages):
        for package in packages:
            if package.dimensao["altura"] > 5 and package.dimensao["altura"] < 140:
                if package.dimensao["largura"] > 13 and package.dimensao["largura"] < 125:
                    if package.peso > 0:
                        return {"mensagem": "Chegou até aqui(kabum)!"}
        return None
