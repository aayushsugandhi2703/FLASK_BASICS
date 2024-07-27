from integrated.app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    
def test_hello_world(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'
    assert response.status_code == 200