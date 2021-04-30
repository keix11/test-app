from flask_restful import Resource, reqparse, abort
from flask import jsonify
from api.models.user import UserModel, UserSchema

from api.database import db

class UsersAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("name", required=True)
        self.reqparse.add_argument("state", required=False)
        super(UsersAPI, self).__init__()


    def get(self):
        results = UserModel.query.all()
        jsonData = UserSchema(many=True).dump(results)
        return jsonData, 201


    def post(self):
        args = self.reqparse.parse_args()
        user = UserModel(args.name, args.state)

        db.session.add(user)
        db.session.commit()

        response = UserSchema().dump(user)

        return response, 201


class UserAPI(Resource):

    def get(self, id):
        user = db.session.query(UserModel).filter_by(id=id).first()
        json = UserSchema().dump(user)
        return json, 201

    def delete(self, id):

        user = db.session.query(UserModel).filter_by(id=id).first()

        if user is not None:
            db.session.delete(user)
            db.session.commit()

        return None, 204

