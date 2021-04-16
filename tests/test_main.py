from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_root():
    # when
    response = client.get("/")

    # then
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_read_item():
    # when
    response = client.get("/items/87")

    # then
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 87,
        "q": None,
    }
