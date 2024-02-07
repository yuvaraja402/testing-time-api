import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_time(client):
    response = client.get('/time')
    assert response.status_code == 200
    assert 'Time' in response.json

def test_time_by_region(client):
    response = client.get('/time/america')
    assert response.status_code == 200
    assert 'America' in response.json