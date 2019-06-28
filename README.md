[![Build Status](https://travis-ci.org/olegnatsevsky/gae_backend_bootstrap.svg?branch=master)](https://travis-ci.org/olegnatsevsky/gae_backend_bootstrap)

# gae_bakend_bootstrap

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
