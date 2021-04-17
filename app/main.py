from fastapi import FastAPI
from app.routers import path_parameters, query_parameters

app = FastAPI()
app.include_router(path_parameters.router)
app.include_router(query_parameters.router)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"msg": "Hello World"}
