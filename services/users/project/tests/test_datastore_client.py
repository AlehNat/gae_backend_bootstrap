def test_empty_entities(datastore_client):
    """Datastore_client fixture should clean up data after execution"""
    query = datastore_client.query()
    all_entities = list(query.fetch())
    assert len(all_entities) == 0
