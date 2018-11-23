from flask_restful import Resource, reqparse

from app import db
from model.sql import SQLiStr

class SQLiController(Resource):
    def get(self):
        sqls = SQLiStr.query.all()
        return [x.as_dict() for x in sqls] 
