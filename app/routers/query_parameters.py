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
