[![Build Status](https://travis-ci.org/olegnatsevsky/gae_backend_bootstrap.svg?branch=master)](https://travis-ci.org/olegnatsevsky/gae_backend_bootstrap)
[![codecov](https://codecov.io/gh/olegnatsevsky/gae_backend_bootstrap/branch/master/graph/badge.svg)](https://codecov.io/gh/olegnatsevsky/gae_backend_bootstrap)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

## Welcome

This template developed to speed up the process of development REST API with GAE and Cloud Datastore. It built on top of Flask, Flask-RESTPlus.

We have configured CI pipeline using [Travis-CI](https://travis-ci.org) with integration tests, code style check using [Black](https://github.com/python/black), code coverage report with [codecov.io](https://codecov.io)

The application can be run locally or inside a Docker container.


## Quick Strat

1. Clone the repo
  ```
  $ git clone https://github.com/olegnatsevsky/gae_backend_bootstrap.git
  $ cd gae_backend_bootstrap
  ```
2. Run containers
  ```
  $ docker-compose up
  ```
3. Open ping endpint
  http://localhost:5001/api/1/users/ping

4. Swagger docs
  http://localhost:5001/api/1/docs

   
## Testing, code style

1. To run integration tests
  ```
  $ docker-compose exec users python manage.py test
  ```
2. To run tests with coverage
  ```
  $ docker-compose exec users python manage.py test-cov
  ```
3. To check code style with flake8
  ```
  $ docker-compose exec users flake8 project
  ```
4. To check code style with Black
  ```
  $ docker-compose exec users black . --check --diff  --exclude env/
  ```

## Deployment to Google App Engine
(TBD)

## Author

- <a href="https://www.linkedin.com/in/onats/">Aleh Natseuski</a> (@<a href="https://twitter.com/natsevsky_oleg">natsevsky_oleg</a> on Twitter)

  
