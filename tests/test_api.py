from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_articles_returns_list():
    response = client.get("/articles")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all("title" in article for article in response.json())

def test_post_article():
    response = client.post("/articles", json={"title": "Test article"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test article"