from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_server_msg():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'Message': 'Message from fast api server'}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {'Health': 'ok'}

def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "Test Item", "description": "This is a test item"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Item created",
        "item": {"name": "Test Item", "description": "This is a test item"}
    }

def test_update_item():
    response = client.put(
        "/items/1",
        json={"name": "Updated Item"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Item 1 updated",
        "item": {"name": "Updated Item", "description": None}
    }
