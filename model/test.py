from app import db

from model.basemodel import BaseModel
from model.form import Form

class Test(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    form_id = db.Column(db.Integer, db.ForeignKey(Form.id, ondelete='CASCADE'))
    input_json = db.Column(db.String(2000))
    html_output_path = db.Column(db.String(50))
    screenshot_path = db.Column(db.String(50))
    time = db.Column(db.DateTime)
    duration = db.Column(db.Float)
    result = db.Column(db.String(100))

    def __init__(self, form_id, input_json, html_output_path, screenshot_path, time, duration, result):
        self.form_id = form_id
        self.input_json = input_json
        self.html_output_path = html_output_path
        self.screenshot_path = screenshot_path
        self.time = time
        self.duration = duration
        self.result = result
