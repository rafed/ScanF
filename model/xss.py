from app import db

from model.basemodel import BaseModel

class XssStr(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    payload = db.Column(db.String(100))

    def __init__(self, payload):
        self.payload = payload
