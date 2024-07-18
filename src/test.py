import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.mark.asyncio
async def test_index(client):
    response = await client.get("/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_weather(client):
    response = await client.get("/Moscow")
    assert response.status_code == 200
    assert "Температура" in response.text
