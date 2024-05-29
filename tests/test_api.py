
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_create_store():
    response = client.post("/stores/test_store", json={"operation": "supply", "item_id": "item1", "quantity": 10})
    assert response.status_code == 200
    assert response.json() == {"store": {"store_id": "test_store", "report": [{"item_id": "item1", "quantity": 10}]}}

def test_get_store():
    response = client.get("/stores/test_store")
    assert response.status_code == 200
    assert response.json() == {"store_id": "test_store", "report": [{"item_id": "item1", "quantity": 10}]}
