from flask import Flask
from flask_restful import Api

from api.views.user import UsersAPI, UserAPI
from api.database import init_db


def create_app():

    app = Flask(__name__)
    app.config.from_object("api.config.Config")

    init_db(app)

    api = Api(app)
    api.add_resource(UserAPI, "/api/user/<id>")
    api.add_resource(UsersAPI, "/api/users")

    return app

app = create_app()

