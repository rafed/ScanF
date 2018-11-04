from app import db

from model.basemodel import BaseModel

class Website(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    baseurl = db.Column(db.String(1000))
    title = db.Column(db.String(200))
    
    def __init__(self, baseurl, title):
        self.baseurl = baseurl
        self.title = title


       
