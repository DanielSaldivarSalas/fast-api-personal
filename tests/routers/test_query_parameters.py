from app.main import app
from fastapi.testclient import TestClient
import pytest


client = TestClient(app)


@pytest.fixture
def fake_db_results():
    fake_items_db = [
        {"item_name": "Foo"},
        {"item_name": "Bar"},
        {"item_name": "Baz"},
        {"item_name": "FooBar"},
    ]

    yield fake_items_db


def test_read_item(fake_db_results):
    # when
    response = client.get("/query_parameter/items/?skip=0&limit=10")

    # then
    assert response.status_code == 200
    assert response.json() == fake_db_results


def test_read_item_optional_parameter_not_specified():
    # when
    response = client.get("/query_parameter/items/87")

    # then
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 87,
    }


def test_read_item_optional_parameter_specified():
    # when
    response = client.get("/query_parameter/items/87?q=9")

    # then
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 87,
        "q": "9",
    }
