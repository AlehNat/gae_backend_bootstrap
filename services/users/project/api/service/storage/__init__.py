import os

from google.cloud.datastore import Client


def create_datastore_client():
    """Create datastore client testing or prod based on config"""
    from main import app

    if app.config["TESTING"]:
        from mock import mock
        import google.auth.credentials

        credentials = mock.Mock(spec=google.auth.credentials.Credentials)
        return Client(
            project=os.getenv("DATASTORE_PROJECT_ID"), credentials=credentials
        )
    else:
        return Client(project=os.getenv("DATASTORE_PROJECT_ID"))
