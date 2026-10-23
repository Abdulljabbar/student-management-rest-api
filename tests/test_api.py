
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_get_all_students():
    response = client.get("/api/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_student_not_found():
    response = client.get("/api/students/9999")
    assert response.status_code == 404


def test_invalid_student():
    response = client.post(
        "/api/students",
        json={
            "name": "",
            "rollNo": "TEST999",
            "department": "Software Engineering",
            "semester": 9
        }
    )
    assert response.status_code == 422
