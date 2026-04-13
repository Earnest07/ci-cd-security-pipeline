from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "User Management API is running"
    }

def test_users():
    response = client.get("/users")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2

    assert data[0]["id"] == 1
    assert data[0]["username"] == "admin"

    assert data[1]["id"] == 2
    assert data[1]["username"] == "dev_user"

def test_login():
    response = client.post("/login")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "Logged in"
    assert "token" in data