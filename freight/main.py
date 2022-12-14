from fastapi import FastAPI
from routes.freight import freight_router
from routes.package import package_router
import uvicorn

app = FastAPI()

app.include_router(freight_router, prefix="/companys")
app.include_router(package_router, prefix="/packages")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)