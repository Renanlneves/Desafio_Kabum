from fastapi import FastAPI
from routes.freight import user_router
import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/company")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8038, reload=True)