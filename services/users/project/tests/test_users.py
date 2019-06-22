import json

import pytest

from project import app


@pytest.fixture
def client():
	app.config.from_object('project.config.TestingConfig')
	cl = app.test_client()
	yield cl


def test_users(client):
	"""Ensure the /ping route behaves correctly."""
	resp = client.get('/users/ping')
	assert 200 == resp.status_code
	assert 'pong!' == resp.json['message']
	assert 'success' == resp.json['status']