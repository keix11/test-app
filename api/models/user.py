from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy_utils import UUIDType
from api.database import db
import uuid

ma = Marshmallow()

class UserModel(db.Model):

    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(200))

    def __init__(self, name, state):
        self.name = name
        self.state = state

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel

