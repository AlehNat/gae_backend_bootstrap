import coverage
import pytest
import sys
from flask.cli import FlaskGroup

from project import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)

COV = coverage.coverage(
    branch=True, include="project/*", omit=["project/tests/*", "project/config.py"]
)
COV.start()


@cli.command()
def test():
    """Runs the tests without code coverage"""
    pytest.main(["project"])


@cli.command()
def test_cov():
    """Runs the tests with code coverage"""
    res = pytest.main(["project"])
    if res == 0:
        COV.stop()
        COV.save()
        print("Coverage Summary:")
        COV.report()
        COV.xml_report()
        COV.erase()
        return 0
    sys.exit(res)


if __name__ == "__main__":
    cli()
