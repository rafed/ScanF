from app import db

from model.basemodel import BaseModel
from model.form import Form

class Field(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    form_id = db.Column(db.Integer, db.ForeignKey(Form.id))
    type = db.Column(db.String(20))
    name = db.Column(db.String(100))
    default_value = db.Column(db.String(100))

    # children = db.relationship('Leave', backref='Employee', passive_deletes=True)
    
    def __init__(self, form_id, type, name, default_value):
        self.form_id = form_id
        self.type = type
        self.name = name
        self.default_value = default_value

