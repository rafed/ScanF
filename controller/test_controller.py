from flask_restful import Resource, fields, marshal_with, reqparse

from app import db
from model.test import Test

test_fields = {
    'id': fields.Integer,
    'form_id': fields.Integer,
    'type': fields.String,
    'input_json': fields.String,
    'html_output_path': fields.String,
    'screenshot_path': fields.String,
    'time': fields.String,
    'duration': fields.String,
    'result': fields.String
}

class TestController(Resource):
    @marshal_with(test_fields)
    def get(self, form_id):
        tests = Test.query.filter(Test.form_id == form_id).all()

        for i in range(len(tests)):
            tests[i].time = tests[i].time.strftime("%H:%M:%S %d/%m/%Y")
        return tests

    def post(self):
        pass

    def delete(self, id):
        test = Test.query.get(id)
        test.delete()
        return {"status":"ok"}
