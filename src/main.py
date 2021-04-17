from typing import Optional

from fastapi import FastAPI
from src.models import ModelName
from typing import Union

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"msg": "Hello World"}


@app.get("/items/current")
def read_item_current() -> dict[str, str]:
    return {"item_id": "Current item"}


# Using Path parameter {item_id}
@app.get("/items/{item_id}")
def read_item(
    item_id: int, q: Optional[str] = None
) -> dict[str, Union[int, Optional[str]]]:
    return {"item_id": item_id, "q": q}


@app.get("/models/{model_name}")
def get_model(model_name: ModelName) -> dict[str, str]:
    result: dict[str, str] = {"model_name": model_name.value}
    if model_name == ModelName.alexnet:
        result["message"] = "Deep Learning FTW!"
    elif model_name.value == ModelName.lenet:
        result["message"] = "LeCNN all the images"
    elif model_name.value == ModelName.resnet:
        result["message"] = "Have some residuals"
    return result
