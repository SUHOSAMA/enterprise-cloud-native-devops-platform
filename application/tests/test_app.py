import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"CloudOps Employee Service" in response.data


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"
    assert data["service"] == "CloudOps Employee Service"


def test_info_endpoint(client):
    response = client.get("/api/info")

    assert response.status_code == 200

    data = response.get_json()

    assert data["service"] == "CloudOps Employee Service"
    assert "version" in data
    assert "hostname" in data
    assert "environment" in data


def test_employees_endpoint(client):
    response = client.get("/api/employees")

    assert response.status_code == 200

    data = response.get_json()

    assert "employees" in data
    assert len(data["employees"]) == 3

    assert data["employees"][0]["id"] == 101
    assert data["employees"][1]["id"] == 102
    assert data["employees"][2]["id"] == 103
