from flask_restful import Resource, reqparse

from app import db
from model.page import Page
from model.form import Form

class PageController(Resource):
    def get(self, id):
        pages = Page.query.filter(Page.website_id == id)
        j = [x.as_dict() for x in pages] 
        
        for i in range(len(j)):
            forms = Form.query.filter(Form.page_id==j[i]['id'])
            f = [x.as_dict() for x in forms]
            j[i]['forms'] = f

        return j


    def delete(self, id):
        page = Page.query.get(id)
        page.delete()
        return {"status":"ok"}
