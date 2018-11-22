from app import db

from model.basemodel import BaseModel
from model.website import Website

class Cookie(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    website_id = db.Column(db.Integer, db.ForeignKey(Website.id, ondelete='CASCADE'))
    name = db.Column(db.String(1000))
    value = db.Column(db.String(1000))

    def __init__(self, website_id, name, value):
        self.website_id = website_id
        self.name = name
        self.value = value
