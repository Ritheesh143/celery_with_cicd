from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app=app)


def test_get_home():
    response = client.get('/')

    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {"message":"home"}