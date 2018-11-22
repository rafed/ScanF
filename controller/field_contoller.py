from flask_restful import Resource, reqparse

from app import db
from model.field import Field

class FieldController(Resource):
    def get(self, id):
        fields = Field.query.filter(Field.form_id==id)
        return [x.as_dict() for x in fields]
