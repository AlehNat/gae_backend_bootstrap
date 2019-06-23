import json

import pytest
from google.cloud import datastore

from project import create_app

app = create_app()


@pytest.fixture
def client():
    app.config.from_object("project.config.TestingConfig")
    cl = app.test_client()
    yield cl

@pytest.fixture
def datastore_client():

    import mock
    import google.auth.credentials

    credentials = mock.Mock(spec=google.auth.credentials.Credentials)
    ds_client = datastore.Client(project="project-test", credentials=credentials)
    yield ds_client


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

    key = datastore_client.key("Task")
    item = datastore.Entity(key)
    item.update(
        {
            "category": "Personal",
            "done": False,
            "priority": 4,
            "description": "Learn Cloud Datastore",
        }
    )
    datastore_client.put(item)
    assert item.id
