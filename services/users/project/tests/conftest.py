import pytest
from project import create_app
from project.api.service.storage import create_datastore_client

app = create_app()


@pytest.fixture
def client():
    """Standard flask testing client"""
    app.config.from_object("project.config.TestingConfig")
    cl = app.test_client()
    yield cl


@pytest.fixture
def datastore_client():
    """Datastore client that clean up all created entities"""
    return create_datastore_client()


def clean_test_data():
    """Searches all data in the datastore and delete"""
    ds_client = create_datastore_client()
    query = ds_client.query()
    keys = [entity.key for entity in query.fetch()]
    ds_client.delete_multi(keys)
