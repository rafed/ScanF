from flask_restful import Resource, fields, marshal_with, reqparse

from app import db
from model.test import Test

class TestController(Resource):
    def get(self, form_id):
        tests = Test.query.filter(Test.form_id == form_id)
        return [x.as_dict() for x in tests] 

    def post(self):
        pass

    def delete(self, id):
        test = Test.query.get(id)
        test.delete()
        return {"status":"ok"}
