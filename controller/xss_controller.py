from flask_restful import Resource, reqparse

from app import db
from model.xss import XssStr

class XssController(Resource):
    def get(self):
        xsss = XssStr.query.all()
        return [x.as_dict() for x in xsss] 
