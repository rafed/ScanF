from app import db

from model.basemodel import BaseModel
from model.website import Website

class Page(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    website_id = db.Column(db.Integer, db.ForeignKey(Website.id))
    screenshot_path = db.column(db.String(50))

    def __init__(self, website_id, screenshot_path):
        self.website_id = website_id
        self.screenshot_path = screenshot_path
