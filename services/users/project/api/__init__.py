from flask import Blueprint
from flask_restplus import Api

from project.api.users import ns_user

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint, doc="/docs")


api.add_namespace(ns_user)
