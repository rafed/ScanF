from app import db

from model.basemodel import BaseModel
from model.field import Field

class Constraint(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    field_id = db.Column(db.Integer, db.ForeignKey(Field.id))
    type = db.Column(db.String(50))
    value = db.Column(db.String(50))

    # children = db.relationship('Leave', backref='Employee', passive_deletes=True)
    
    def __init__(self, field_id, type, value):
        self.field_id = field_id
        self.type = type
        self.value = value

