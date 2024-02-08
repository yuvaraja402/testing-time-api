from main import app

def test_get_time():
    with app.test_client() as client:
        response = client.get('/time')
        assert response.status_code == 200
        assert 'Time' in response.json

def test_time_by_region():
    with app.test_client() as client:
        response = client.get('/time/AmeRICA')
        assert response.status_code == 200
        assert 'America' in response.json
        assert 'africa' in response.json


from selenium import webdriver

def test_end_to_end():
    # Assuming your Flask app is running locally on port 5000
    driver = webdriver.Chrome()
    driver.get('http://localhost:5000/time')
    assert 'Time' in driver.page_source
    driver.quit()

# summa adding text
a = 123
