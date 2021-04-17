from typing import Optional

from fastapi import FastAPI
from models import ModelName

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


@app.get("/models/{model_name}")
def get_model(model_name):
    result = {"model_name": model_name}
    if model_name == ModelName.alexnet:
        result["message"] = "Deep Learning FTW!"
    elif model_name == ModelName.lenet:
        result["message"] = "LeCNN all the images"
    return result
