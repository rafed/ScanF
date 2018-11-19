from app import db

from model.basemodel import BaseModel
from model.page import Page

class Form(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey(Page.id, ondelete='CASCADE'))
    method = db.Column(db.String(10))
    form_action = db.Column(db.String(1000))

    # children = db.relationship('Field', backref='Form', passive_deletes=True)
    # children2 = db.relationship('Test', backref='Form', passive_deletes=True)
    
    def __init__(self, page_id, method, form_action):
        self.page_id = page_id
        self.method = method
        self.form_action = form_action
