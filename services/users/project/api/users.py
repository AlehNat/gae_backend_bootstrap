from flask import Blueprint
from flask import request
from flask_restplus import Resource, Api


users_blueprint = Blueprint("users", __name__)
api = Api(users_blueprint)


class UsersPing(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}


class UsersList(Resource):
    def post(self):
        post_data = request.get_json()
        # username = post_data.get("username")
        email = post_data.get("email")

        # TODO update
        # db.session.add(User(username=username, email=email))
        # db.session.commit()
        response_object = {
            "status": "success",
            "message": "{} was added!".format(email),
        }
        return response_object, 201


api.add_resource(UsersPing, "/users/ping")
api.add_resource(UsersList, "/users")
