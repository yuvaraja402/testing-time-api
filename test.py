# test.py
from main import app

def test_get_time():
    with app.test_client() as client:
        response = client.get('/time')
        assert response.status_code == 200
        assert 'Time' in response.json
        print(response.json)

def test_time_by_region():
    with app.test_client() as client:
        response = client.get('/time/AmeRICA')
        assert response.status_code == 200
        assert 'America' in response.json
        print(response.json)