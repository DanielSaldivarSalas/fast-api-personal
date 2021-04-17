from typing import Optional, Union
from app.models import ModelName
from fastapi import APIRouter
router = APIRouter()


@router.get("/path_parameter/items/current")
async def read_item_current() -> dict[str, str]:
    return {"item_id": "Current item"}


# Using Path parameter {item_id}
@router.get("/path_parameter/items/{item_id}")
async def read_item(
    item_id: int, q: Optional[str] = None
) -> dict[str, Union[int, Optional[str]]]:
    return {"item_id": item_id, "q": q}


@router.get("/path_parameter/models/{model_name}")
async def get_model(model_name: ModelName) -> dict[str, str]:
    result: dict[str, str] = {"model_name": model_name.value}
    if model_name == ModelName.alexnet:
        result["message"] = "Deep Learning FTW!"
    elif model_name.value == ModelName.lenet:
        result["message"] = "LeCNN all the images"
    elif model_name.value == ModelName.resnet:
        result["message"] = "Have some residuals"
    return result


@router.get("/path_parameter/files/{file_path:path}")
async def read_file(file_path: str) -> dict[str, str]:
    return {"file_path": file_path}
