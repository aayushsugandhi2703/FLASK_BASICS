from integrated.rest import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

    
def test_get_video(client):
    # First, add a video
    client.put('/video/1', json={'name': 'Test Video'})

    # Then, get the video
    response = client.get('/video/1')
    assert response.status_code == 200
    assert response.json == {'id': 1, 'name': 'Test Video'}

def test_video_put(client):
    response = client.put('/video/1', json={'name': 'video1'})
    assert response.status_code == 201
    assert response.json == {'id': 1, 'name': 'video1'}