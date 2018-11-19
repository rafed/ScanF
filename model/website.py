from app import db

from model.basemodel import BaseModel

class Website(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    baseurl = db.Column(db.String(1000), unique=True)
    title = db.Column(db.String(200))

    # children = db.relationship('Page', backref='Website', passive_deletes=True)
    # children2 = db.relationship('Cookie', backref='Website', passive_deletes=True)

    def __init__(self, baseurl, title):
        self.baseurl = baseurl
        self.title = title


       
