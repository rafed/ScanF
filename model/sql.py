from app import db

from model.basemodel import BaseModel

class SQLiStr(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    queryStr = db.Column(db.String(100))

    def __init__(self, queryStr):
        self.queryStr = queryStr
