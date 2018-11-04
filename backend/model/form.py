from app import db

from model.basemodel import BaseModel
from model.page import Page

class Form(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey(Page.id))
    method = db.Column(db.String(10))
    form_action = db.Column(db.String(1000))
    
    def __init__(self, page_id, method, form_action):
        self.page_id = page_id
        self.method = method
        self.form_action = form_action
