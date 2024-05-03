# test_app.py
import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_weather_data(client):
    response = client.get('/weather')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'weather' in data
    assert 'main' in data
    assert 'name' in data
