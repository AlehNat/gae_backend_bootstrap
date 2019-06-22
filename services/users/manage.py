import pytest
from flask.cli import FlaskGroup

from project import app


cli = FlaskGroup(app)

@cli.command('clean_datastore')
def clean_datastore():
    print("Cleaning Datastore")
    print("TBD!!!")


@cli.command()
def test():
    """Runs the tests without code coverage"""
    pytest.main(["project"])

if __name__ == '__main__':
    cli()