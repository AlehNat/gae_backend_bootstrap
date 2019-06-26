import mock
import pytest
import google.auth.credentials
from google.cloud import datastore
from project import create_app

app = create_app()


class MemorizingClient(datastore.Client):
    """Datastore client. Stores all stored keys in self.stored_object_keys"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stored_object_keys = set()

    def put(self, entity):
        super().put(entity)
        self.stored_object_keys.add(entity.key)


@pytest.fixture
def client():
    app.config.from_object("project.config.TestingConfig")
    cl = app.test_client()
    yield cl


@pytest.fixture
def datastore_client():
    """Datastore client that clean up all created entities"""

    credentials = mock.Mock(spec=google.auth.credentials.Credentials)
    ds_client = MemorizingClient(project="project-test", credentials=credentials)
    yield ds_client
    if ds_client.stored_object_keys:
        ds_client.delete_multi(ds_client.stored_object_keys)
