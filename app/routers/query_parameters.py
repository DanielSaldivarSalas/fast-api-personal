from typing import Optional, Union
from fastapi import APIRouter

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
    {"item_name": "FooBar"},
]

# When you declare other function parameters
# that are not part of the path parameters,
# they are automatically interpreted as "query" parameters.

router = APIRouter()


@router.get("/query_parameter/items")
async def read_item(skip: int = 0, limit: int = 10) -> list[dict[str, str]]:
    return fake_items_db

# Using Path parameter {item_id}
@router.get("/query_parameter/items/{item_id}")
async def read_item_optional_parameter(
    item_id: int, q: Optional[str] = None
) -> dict[str, Union[int, Optional[str]]]:
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
