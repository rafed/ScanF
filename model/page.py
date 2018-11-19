from app import db

from model.basemodel import BaseModel
from model.website import Website

class Page(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    website_id = db.Column(db.Integer, db.ForeignKey(Website.id, ondelete='CASCADE'))
    url = db.Column(db.String(2000)) 
    screenshot_path = db.Column(db.String(50))

    # children = db.relationship('Form', backref='Page', passive_deletes=True)

    def __init__(self, website_id, url, screenshot_path=None):
        self.website_id = website_id
        self.url = url
        self.screenshot_path = screenshot_path
