import json

from google.cloud import datastore


def test_users(client):
    """Ensure the /ping route behaves correctly."""
    resp = client.get("/users/ping")
    assert 200 == resp.status_code
    assert "pong!" == resp.json["message"]
    assert "success" == resp.json["status"]


def test_add_user(client):
    """Ensure a new user can be added to the database."""

    resp = client.post(
        "/users",
        data=json.dumps({"username": "michael", "email": "michael@mherman.org"}),
        content_type="application/json",
    )
    data = resp.json
    assert 201 == resp.status_code
    assert "michael@mherman.org was added!" == data["message"]
    assert "success" == data["status"]


def test_single_user(datastore_client):
    """Ensure get single user behaves correctly."""

    user_key = datastore_client.key("User")
    user_entity = datastore.Entity(user_key)
    user_entity.update(
        {"first_name": "John", "last_name": "Doe", "description": "Test user"}
    )
    datastore_client.put(user_entity)

    user = datastore_client.get(user_entity.key)
    assert user["first_name"] == "John"
    assert user["last_name"] == "Doe"
    assert user["description"] == "Test user"
