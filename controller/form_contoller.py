from flask_restful import Resource, reqparse

from app import db
from model.form import Form

class FormController(Resource):
    def get(self, id):
        forms = Form.query.filter(Form.page_id==id)
        return [x.as_dict() for x in forms]
