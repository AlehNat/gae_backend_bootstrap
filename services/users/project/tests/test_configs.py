from flask import current_app

from project import create_app

app = create_app()


def test_development_config():
    app.config.from_object("project.config.DevelopmentConfig")
    assert app.config["SECRET_KEY"] == "my_precious"
    assert current_app is not None


def test_testing_config():
    app.config.from_object("project.config.TestingConfig")
    assert app.config["SECRET_KEY"] == "my_precious"
    assert app.config["TESTING"]
    assert app.config["PRESERVE_CONTEXT_ON_EXCEPTION"] is None


def test_prod_config():
    app.config.from_object("project.config.ProductionConfig")
    assert app.config["SECRET_KEY"] == "my_precious"
    assert app.config["TESTING"] == False
