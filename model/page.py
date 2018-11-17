from app import db

from model.basemodel import BaseModel
from model.website import Website

class Page(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    website_id = db.Column(db.Integer, db.ForeignKey(Website.id, ondelete='CASCADE'))
    url = db.column(db.String(2000))        ## new
    screenshot_path = db.column(db.String(50))

    children = db.relationship('Website', backref='Page', passive_deletes=True)

    def __init__(self, website_id, url, screenshot_path):
        self.website_id = website_id
        self.url = url
        self.screenshot_path = screenshot_path
