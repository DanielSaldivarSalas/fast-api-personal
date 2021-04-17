from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_root():
    # when
    response = client.get("/")

    # then
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_read_item_current():
    # when
    response = client.get("items/current")

    # then
    assert response.status_code == 200
    assert response.json() == {
        "item_id": "Current item"
    }


def test_read_item():
    # when
    response = client.get("/items/87")

    # then
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 87,
        "q": None,
    }


def test_get_model_alexnet_value():
    # when
    response = client.get("models/alexnet")

    # then
    assert response.status_code == 200
    assert response.json() == {
        "model_name": "alexnet",
        "message": "Deep Learning FTW!"
    }


def test_get_model_lenet_value():
    # when
    response = client.get("models/lenet")

    # then
    assert response.status_code == 200
    assert response.json() == {
        "model_name": "lenet",
        "message": "LeCNN all the images"
    }


def test_get_model_resnet_value():
    # when
    response = client.get("models/resnet")

    # then
    assert response.status_code == 200
    assert response.json() == {
        "model_name": "resnet",
        "message": "Have some residuals"
    }


def test_get_model_returns_422_with_values_outside_the_enum():
    # when
    response_jack = client.get("models/jack")

    # then
    assert response_jack.status_code == 422
