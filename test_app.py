import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "online"


def test_suma_calculo(client):
    response = client.get("/calc/sum/10/15")

    assert response.status_code == 200

    data = response.get_json()

    assert data["resultado"] == 999
