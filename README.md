[![Build Status](https://travis-ci.org/olegnatsevsky/gae_backend_bootstrap.svg?branch=master)](https://travis-ci.org/olegnatsevsky/gae_backend_bootstrap)
[![codecov](https://codecov.io/gh/olegnatsevsky/gae_backend_bootstrap/branch/master/graph/badge.svg)](https://codecov.io/gh/olegnatsevsky/gae_backend_bootstrap)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

# gae_backend_bootstrap

Run containers

docker-compose build

docker-compose up -d

The -d flag is used to run containers in the background.

Tests:

Container
docker-compose exec users python manage.py test

Local

activate venv
python manage.py test


Black:

black . --exclude env/

Gotchas:

1. import file mismatch:
find . -name "*.pyc" -exec rm -f {} \;
