from fastapi import FastAPI
from app.routers import path_parameters

app = FastAPI()
app.include_router(path_parameters.router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"msg": "Hello World"}
