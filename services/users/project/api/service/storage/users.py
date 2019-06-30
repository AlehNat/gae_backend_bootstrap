from google.cloud import datastore

from project.api.service.storage import create_datastore_client

datastore_client = create_datastore_client()


def store_user(username, email):
    """Stores user entity to datastore"""
    user_key = datastore_client.key("User")
    user_entity = datastore.Entity(user_key)
    user_entity.update({"username": username, "email": email})
    datastore_client.put(user_entity)
