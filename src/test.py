import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


@pytest.fixture
def city():
    return "Moscow"


def test_index():
    response = client.get("/")
    assert response.status_code == 200


def test_weather(city):
    response = client.get(f"/{city}")
    assert response.status_code == 200
