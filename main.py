from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


@app.get("/items/current")
def read_item_current():
    return {"item_id": "Current item"}


# Using Path parameter {item_id}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/models/alexnet")
def get_model():
    return {"model_name": "alexnet", "message": "Deep Learning FTW!"}
