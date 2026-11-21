import pytest
import sys
from pathlib import Path
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.main import app
import app.db as db

@pytest.fixture(autouse=True)
def temp_db(tmp_path, monkeypatch):
    # Redirects DB_FILE to a fresh temporary file per test
    test_file = tmp_path / "test_data.json"
    monkeypatch.setattr(db, "DB_FILE", test_file, raising=False)

client = TestClient(app)

def test_get_item_not_found():
    response = client.get("/api/v1/items/2fb2f3b8-d0f7-4c3a-bbe9-2f4535da01c8")  # Non-existent UUID
    assert response.status_code == 404

def test_create_and_get_item():
    # 1. Create an item first
    create_res = client.post(
        "/api/v1/items",
        json={
            "title": "Learn pytest",
            "description": "Practice writing tests",
            "completed": False,
        },
    )
    assert create_res.status_code in (200, 201)

    create_payload = create_res.json()

    # Some implementations wrap the created item or use a UUID key.
    def find_id(payload):
        if not isinstance(payload, dict):
            return None
        for key in ("id", "item_id", "uuid", "_id"):
            if payload.get(key) is not None:
                return payload[key]
        for value in payload.values():
            if isinstance(value, dict):
                found = find_id(value)
                if found is not None:
                    return found
        return None

    created_id = find_id(create_payload)

    # If the create response omits the identifier, resolve it from the item list.
    if created_id is None:
        list_res = client.get("/api/v1/items")
        assert list_res.status_code == 200
        items = list_res.json()
        if isinstance(items, dict):
            items = items.get("items", items.get("data", []))
        created_id = next(
            (
                item.get("id") or item.get("item_id") or item.get("uuid") or item.get("_id")
                for item in items
                if isinstance(item, dict) and item.get("title") == "Learn pytest"
            ),
            None,
        )

    assert created_id is not None, f"Create response did not include an item ID: {create_payload}"

    # 2. Fetch that exact item and assert 200
    get_res = client.get(f"/api/v1/items/{created_id}")
    assert get_res.status_code == 200
    assert get_res.json()["title"] == "Learn pytest"
