import json

from google.cloud import datastore


def test_users(client):
    """Ensure the /ping route behaves correctly."""
    resp = client.get("/api/1/users/ping")
    assert 200 == resp.status_code
    assert "pong!" == resp.json["message"]
    assert "success" == resp.json["status"]


def test_add_user(client, datastore_client):
    """Ensure a new user can be added to the database."""

    resp = client.post(
        "/api/1/users/",
        data=json.dumps({"username": "John", "email": "john@mhexample.com"}),
        content_type="application/json",
    )
    data = resp.json
    assert 201 == resp.status_code
    assert "john@mhexample.com was added!" == data["message"]
    assert "success" == data["status"]
    user_query = datastore_client.query(kind="User")
    user_query.add_filter("username", "=", "John")
    user_query.add_filter("email", "=", "john@mhexample.com")
    result = list(user_query.fetch())
    assert 1 == len(result)
    assert "John" == result[0]["username"]
    assert "john@mhexample.com" == result[0]["email"]


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


def teardown_function(_):
    """Called by pytest after each test"""
    from project.tests.conftest import clean_test_data

    clean_test_data()
