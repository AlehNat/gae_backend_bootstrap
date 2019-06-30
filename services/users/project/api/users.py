from flask import request
from flask_restplus import Resource, Namespace


ns_user = Namespace("users", description="Users related operations")


@ns_user.route("/ping")
class UsersPing(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}


@ns_user.route("/")
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
