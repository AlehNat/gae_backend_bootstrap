import os
from flask import Flask


def create_app(script_info=None):

    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # register blueprints
    from project.api import api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api/1")

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
